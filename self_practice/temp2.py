import time
import asyncio
import requests
import aiohttp
import aiohttp
import asyncio
from aiohttp import TraceConfig
import csv
from asgiref import sync
import time
from collections import defaultdict
from asgiref import sync

def timed(func):
    """
    records approximate durations of function calls
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        print('{name:<30} started'.format(name=func.__name__))
        result = func(*args, **kwargs)
        duration = "{name:<30} finished in {elapsed:.2f} seconds".format(
            name=func.__name__, elapsed=time.time() - start
        )
        print(duration)
        timed.durations.append(duration)
        return result
    return wrapper

timed.durations = []
url = 'https://postman-echo.com/delay/1'
# url = "https://www.ornaz.com/express/api/rest/v5/products/rings/ara1183-women-brenda-solitare-engagement-rings/"



@timed
def sync_requests_get_all(urls):
    session = requests.Session()
    return [session.get(url).json() for url in urls]


@timed
def async_requests_get_all(urls):
    session = requests.Session()
    def get(url):
        return session.get(url).json()
    async_get = sync.sync_to_async(get)

    async def get_all(urls):
        return await asyncio.gather(*[
            async_get(url) for url in urls
        ])
    return sync.async_to_sync(get_all)(urls)

@timed
def async_aiohttp_get_all(urls):
    async def get_all(urls):
        async with aiohttp.ClientSession() as session:
            async def fetch(url):
                async with session.get(url) as response:
                    return await response.json()
            return await asyncio.gather(*[
                fetch(url) for url in urls
            ])
    return sync.async_to_sync(get_all)(urls)


@timed
def async_aiohttp_get_all(urls):
    timelines = []
    
    event_bindings = {
        'TraceConnectionQueuedStartParams': 'on_connection_queued_start',
        'TraceConnectionQueuedEndParams': 'on_connection_queued_end',
        'TraceConnectionCreateStartParams': 'on_connection_create_start',
        'TraceConnectionCreateEndParams': 'on_connection_create_end',
        'TraceConnectionReuseconnParams': 'on_connection_reuseconn',
        'TraceDnsResolveHostStartParams': 'on_dns_resolvehost_start',
        'TraceDnsResolveHostEndParams': 'on_dns_resolvehost_end',
        'TraceDnsCacheHitParams': 'on_dns_cache_hit',
        'TraceDnsCacheMissParams': 'on_dns_cache_miss',
        'TraceRequestStartParams': 'on_request_start',
        'TraceRequestChunkSentParams': 'on_request_chunk_sent',
        'TraceResponseChunkReceivedParams': 'on_response_chunk_received',
        'TraceRequestRedirectParams': 'on_request_redirect',
        'TraceRequestEndParams': 'on_request_end',
        'TraceRequestExceptionParams': 'on_request_exception',
        'TraceRequestHeadersSentParams': 'on_request_headers_sent'
    }

    async def on_request_start(session, trace_config_ctx, params):
        trace_config_ctx.start_time = time.monotonic()
        trace_config_ctx.timeline = {
            'url': str(params.url),
            'start_time': trace_config_ctx.start_time,
            'events': [{'event': 'on_request_start', 'time': time.monotonic()}]
        }

    async def on_request_end(session, trace_config_ctx, params):
        elapsed = time.monotonic() - trace_config_ctx.start_time
        trace_config_ctx.timeline['end_time'] = time.monotonic()
        trace_config_ctx.timeline['events'].append({'event': 'request_end', 'time': round(elapsed, 10)})
        timelines.append(trace_config_ctx.timeline)

    async def generic(session, trace_config_ctx, params):
        elapsed = time.monotonic() - trace_config_ctx.start_time
        key = params.__class__.__name__
        trace_config_ctx.timeline['events'].append({'event': event_bindings.get(key, key), 'time': round(elapsed, 10)})

    async def get_all(urls):
        trace_config = TraceConfig()
        trace_config.on_request_start.append(on_request_start)
        trace_config.on_request_end.append(on_request_end)
        
        custom = ['_on_acquire_connection', '_on_headers_received', '_on_exception', 
                   '_on_connection_queued_start', '_on_connection_create_start',
                   '_on_connection_queued_end', '_on_connection_create_end',
                   '_on_connection_reuseconn', ]
        common = [l[1:] for l in trace_config.__dict__.keys()]
        trace_config.on_request_end.append(on_request_end)
        for key in set(common +  custom + list(event_bindings.values())):
            if key.startswith("_"):
                key = key[1:]
            getattr(trace_config, key, []).append(generic)
            
        for _, val in event_bindings.items():
            getattr(trace_config, val, []).append(generic)

        connector = aiohttp.TCPConnector(limit_per_host=50, ttl_dns_cache=3000, keepalive_timeout=75, loop=asyncio.get_event_loop())
        # force_close = True
        # connector = None
        async with aiohttp.ClientSession(trace_configs=[trace_config], connector=connector) as session:
            async def fetch(url, params=None):
                async with session.get(url, params=params) as response:
                    return  await response.json()
            return await asyncio.gather(*[
                fetch(url, params={"q": 0}) for i, url in enumerate(urls)
            ])
    result = sync.async_to_sync(get_all)(urls)

    # Process and visualize the timelines as needed
    for timeline in timelines:
        print(timeline)
        break
    write_to_csv(timelines)

    return result


def write_to_csv(data):
    output_data = defaultdict(dict)

    # Collect all unique event names
    event_names = set()

    # Process each entry in the input data
    for entry in data:
        url = entry['url']
        for event in entry['events']:
            event_name = event['event']
            event_time = event['time']
            output_data[url][event_name] = event_time
            event_names.add(event_name)

    # Convert the output_data to a list for CSV writing
    csv_data = []
    header = ['url'] + sorted(event_names)
    csv_data.append(header)

    for url, events in output_data.items():
        row = [url] + [events.get(event, '') for event in sorted(event_names)]
        csv_data.append(row)

    # Write to CSV
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)


if __name__ == '__main__':
    urls = [url]*30
    async_aiohttp_get_all(urls)
    # async_requests_get_all(urls)
    sync_requests_get_all([url])
    print('----------------------')
    [print(duration) for duration in timed.durations]
