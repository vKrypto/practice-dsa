# 15 Engineering Impact Layers with Amazon Leadership Principles

## 1. Async HTTP Migration

### Amazon LPs

* **Primary:** Bias for Action
* **Secondary:** Invent and Simplify

### Problem

The existing implementation was making HTTP calls sequentially using synchronous request handling. Because every request waited for the previous one to finish, overall execution time became very high.

### What I Observed

* API execution was taking around **92 seconds**.
* Most of the time was spent waiting on network I/O.
* CPU was not the bottleneck.
* The workload was I/O-bound, not compute-bound.

### Step-by-Step Action

1. Analyzed request execution flow.
2. Identified that HTTP calls were happening one by one.
3. Replaced synchronous calls with `aiohttp`.
4. Added async task batching.
5. Added proper timeout handling.
6. Added rate limiting to avoid overwhelming downstream APIs.
7. Added retry handling for transient failures.
8. Tested with different concurrency levels.
9. Tuned batch size based on latency and downstream capacity.
10. Deployed safely with monitoring.

### Result

Execution time reduced from **92 seconds → 30 seconds**.

### Interview Positioning

I did not wait for a full redesign. I identified the immediate bottleneck, used async I/O where it made sense, added safety controls like rate limiting and timeout handling, and delivered measurable improvement quickly.

---

## 2. Redis Compression & Cache Optimization

### Amazon LPs

* **Primary:** Frugality
* **Secondary:** Invent and Simplify

### Problem

Large payloads were being stored and transferred repeatedly through Redis, causing high I/O usage, memory pressure, and slower response times.

### What I Observed

* Redis payload size was around **150MB**.
* Same or similar data was fetched repeatedly.
* Network I/O was unnecessarily high.
* Redis memory usage was inefficient.

### Step-by-Step Action

1. Inspected Redis keys and payload sizes.
2. Identified large repeated data structures.
3. Checked whether all fields were required every time.
4. Added compression before storing data.
5. Added decompression only at the consumer side.
6. Implemented conditional fetching to avoid unnecessary reads.
7. Avoided fetching unchanged data.
8. Verified CPU overhead of compression.
9. Compared network savings versus CPU cost.
10. Rolled out with monitoring on Redis latency, memory, and CPU.

### Result

Payload size reduced from **150MB → 13MB**, around **90% I/O reduction**.

### Interview Positioning

Instead of scaling Redis blindly, I reduced unnecessary data movement. That saved memory, network, and infrastructure cost.

---

## 3. AccountsAPI Optimization

### Amazon LPs

* **Primary:** Dive Deep
* **Secondary:** Deliver Results

### Problem

AccountsAPI was slow under high concurrency. At around **20K concurrent requests**, p95 latency was around **2 seconds**.

### What I Observed

* Latency spikes were not caused by one single query.
* Lock contention was present.
* Mutex strategy was creating unnecessary waiting.
* Distributed locking was adding overhead.
* Logging patterns were also contributing to latency.

### Step-by-Step Action

1. Collected p95 and p99 latency metrics.
2. Added detailed logs around critical sections.
3. Measured time spent in mutex lock acquisition.
4. Reviewed distributed lock usage.
5. Identified unnecessary locking scope.
6. Reduced lock duration.
7. Moved non-critical work outside the lock.
8. Optimized database access pattern.
9. Reduced excessive synchronous logging.
10. Load tested with **20K concurrent requests**.
11. Compared before/after latency.
12. Rolled out gradually.

### Result

p95 latency improved from **2 seconds → 8–9ms** at **20K concurrent requests**.

### Interview Positioning

This was not a surface-level optimization. I had to go deep into locking behavior, logging overhead, and request contention to fix the real bottleneck.

---

## 4. System Reliability / CI-CD

### Amazon LPs

* **Primary:** Insist on the Highest Standards
* **Secondary:** Ownership

### Problem

Frequent emergency releases were happening because issues were being detected late, often after deployment.

### What I Observed

* Manual testing was unreliable.
* PR quality was inconsistent.
* Regression bugs were reaching production.
* Release confidence was low.

### Step-by-Step Action

1. Reviewed failure patterns from past releases.
2. Identified gaps in testing and review process.
3. Added automated test execution in CI.
4. Added sandbox testing before production release.
5. Added PR quality gates.
6. Blocked merge if critical checks failed.
7. Added basic regression coverage.
8. Improved deployment validation.
9. Added rollback readiness.
10. Monitored release failure frequency.

### Result

Emergency releases reduced by around **90%**.

### Interview Positioning

I treated reliability as an engineering responsibility, not QA’s job. The goal was to catch issues before production, not debug them after users were impacted.

---

## 5. System Observability

### Amazon LPs

* **Primary:** Dive Deep
* **Secondary:** Learn and Be Curious

### Problem

When production issues happened, debugging was slow because system behavior was not clearly visible.

### What I Observed

* Logs were scattered.
* Metrics were incomplete.
* Edge cases were hard to identify.
* Debugging depended too much on manual inspection.

### Step-by-Step Action

1. Identified critical user journeys.
2. Added structured logging.
3. Added request IDs / correlation IDs.
4. Integrated logs with **Graylog**.
5. Added infrastructure and application metrics in **Grafana**.
6. Used **Kibana** for deeper log analysis.
7. Added dashboards for latency, errors, throughput, and resource usage.
8. Added alerts for abnormal patterns.
9. Used observability data to identify edge cases.
10. Improved debugging speed.

### Result

Production behavior became easier to understand, and debugging became faster and more data-driven.

### Interview Positioning

Observability helped us move from guessing to knowing. Once logs and metrics were properly connected, we could identify real production behavior instead of relying on assumptions.

---

## 6. Kafka Producer Optimization

### Amazon LPs

* **Primary:** Invent and Simplify
* **Secondary:** Deliver Results

### Problem

Kafka producer publishing was slow. Each publish flow was taking around **1 second**, which was too high for the expected throughput.

### What I Observed

* Messages were published inefficiently.
* Producer batching was not optimal.
* Partition usage was not tuned.
* Some repeated DB-side work was slowing down publishing.

### Step-by-Step Action

1. Measured producer-side latency.
2. Checked Kafka batch configuration.
3. Reviewed partitioning strategy.
4. Added batch publishing.
5. Improved partition affinity.
6. Reduced unnecessary per-message overhead.
7. Moved some repeated DB operations into stored procedures.
8. Horizontally scaled producer workers.
9. Load tested publish throughput.
10. Monitored broker load and consumer lag.

### Result

Kafka publish time reduced from **1 second → 150–200ms**.

### Interview Positioning

I optimized the full publishing path instead of only changing Kafka config. The fix involved batching, partition strategy, DB-side simplification, and horizontal scaling.

---

## 7. Kafka Consumer Optimization

### Amazon LPs

* **Primary:** Invent and Simplify
* **Secondary:** Deliver Results

### Problem

Kafka consumers were taking more than **2 seconds** to consume and process messages.

### What I Observed

* Consumer lag was increasing.
* DNS resolution overhead was visible.
* Consumer scaling was not balanced.
* Some network-level delays were affecting processing.

### Step-by-Step Action

1. Measured consumer lag.
2. Checked processing time per message.
3. Checked network and DNS timing.
4. Identified DNS overhead in service communication.
5. Used **Cilium eBPF** to optimize DNS/network behavior.
6. Scaled consumer instances.
7. Tuned consumer concurrency.
8. Verified partition assignment.
9. Monitored lag reduction.
10. Load tested under higher event volume.

### Result

Consume time reduced from **>2 seconds → 200–250ms**.

### Interview Positioning

The issue was not only application code. I looked at consumer processing, network behavior, DNS overhead, and scaling together.

---

## 8. TCP Window Tuning

### Amazon LPs

* **Primary:** Dive Deep
* **Secondary:** Learn and Be Curious

### Problem

Some requests were failing or slowing down because of connection timing issues and `recvWindow` expiry.

### What I Observed

* Failures were more visible at high latency percentiles.
* Average latency looked fine, but p99/p999 had problems.
* TTFB and connection timing showed abnormal delays.

### Step-by-Step Action

1. Collected latency percentile data.
2. Focused on p99 and p999 instead of only average latency.
3. Measured TTFB.
4. Inspected TCP connection timing.
5. Identified `recvWindow` expiry behavior.
6. Tuned TCP/window-related parameters.
7. Reduced timing mismatch.
8. Re-tested under production-like load.
9. Compared p99/p999 before and after.
10. Added monitoring for recurrence.

### Result

Improved high-percentile latency and reduced `recvWindow` expiry related failures.

### Interview Positioning

The average latency was misleading. I had to look at tail latency and connection-level behavior to find the actual issue.

---

## 9. Datacenter Migration

### Amazon LPs

* **Primary:** Think Big
* **Secondary:** Have Backbone; Disagree and Commit

### Problem

A large part of request latency was caused by datacenter distance and network hops.

### What I Observed

* Application-level optimization had limits.
* Network latency was adding around **250ms per request**.
* The current datacenter location was not ideal for the traffic pattern.

### Step-by-Step Action

1. Measured request latency across network paths.
2. Identified datacenter-related latency.
3. Compared current setup with alternative datacenter options.
4. Prepared a data-driven proposal.
5. Shared analysis with the NSD team.
6. Highlighted business and performance impact.
7. Discussed risks and migration complexity.
8. Aligned stakeholders.
9. Supported migration planning.
10. Validated latency improvement after migration.

### Result

Latency reduced by around **250ms per request**.

### Interview Positioning

This required thinking beyond code. The right solution was infrastructure-level change, and I had to back the proposal with data.

---

## 10. Python Upgrade `3.9.5 → 3.13.2`

### Amazon LPs

* **Primary:** Bias for Action
* **Secondary:** Deliver Results

### Problem

CPU-bound processing was slower than expected, and the application was running on an older Python version.

### What I Observed

* Execution time was around **7 seconds**.
* CPU processing could benefit from runtime improvements.
* Python version upgrade had potential performance gains.

### Step-by-Step Action

1. Checked current Python version.
2. Reviewed compatibility of dependencies.
3. Tested application on Python `3.13.2`.
4. Ran unit and integration tests.
5. Benchmarked CPU-heavy flows.
6. Fixed dependency/version issues.
7. Updated Docker/runtime configuration.
8. Deployed gradually.
9. Monitored errors and performance.
10. Compared execution time before and after.

### Result

CPU processing improved by around **40%**, and execution time reduced from **7 seconds → 5–6 seconds**.

### Interview Positioning

Sometimes performance improvement does not require complex redesign. A runtime upgrade, if tested properly, can give direct gains.

---

## 11. Long-Running Job Termination

### Amazon LPs

* **Primary:** Ownership
* **Secondary:** Insist on the Highest Standards

### Problem

Timeout middleware was marking jobs as timed out, but the underlying execution was still continuing.

### What I Observed

* API/request timeout happened at middleware level.
* Worker execution did not actually stop.
* Long-running jobs continued consuming CPU/memory.
* This created hidden resource leaks.

### Step-by-Step Action

1. Reproduced the timeout behavior.
2. Verified that middleware timeout only stopped waiting, not execution.
3. Checked active process/thread behavior after timeout.
4. Identified that execution needed hard termination.
5. Used `ctypes`-based termination for the running execution path.
6. Added safe cleanup handling.
7. Added logs for timeout and termination.
8. Tested with long-running jobs.
9. Verified that resources were released.
10. Added monitoring for timeout frequency.

### Result

Long-running jobs were properly stopped instead of silently continuing in the background.

### Interview Positioning

The system looked like it had timeout handling, but technically it was incomplete. I owned the full behavior, not just the visible API response.

---

## 12. Memory Leak Resolution

### Amazon LPs

* **Primary:** Dive Deep
* **Secondary:** Ownership

### Problem

Application memory kept growing abnormally over time, eventually creating stability risks.

### What I Observed

* Memory grew from around **400GB → 1.5TB**.
* Normal profiling was not enough.
* Leak was related to low-level object retention.
* Issue was connected to `SSLContext` garbage collection behavior.

### Step-by-Step Action

1. Monitored memory growth over time.
2. Compared normal traffic versus memory growth.
3. Captured core dump using `gcore`.
4. Analyzed memory objects from dump.
5. Identified retained SSL-related objects.
6. Investigated `SSLContext` lifecycle.
7. Found GC-related retention issue.
8. Fixed object cleanup/reuse behavior.
9. Re-ran long-duration tests.
10. Monitored memory after deployment.

### Result

Memory growth stabilized from **400GB → 1.5TB** down to **400GB → 450GB**.

### Interview Positioning

This required deep debugging beyond application logs. I used core dump analysis to identify the actual retained object pattern.

---

## 13. GIL Bypass Using Subprocess

### Amazon LPs

* **Primary:** Invent and Simplify
* **Secondary:** Deliver Results

### Problem

CPU-bound Python workload was not utilizing available CPU cores properly because of GIL limitations.

### What I Observed

* CPU utilization was only around **10–12%**.
* Workload was CPU-heavy.
* Threads were not giving real parallelism.
* System had enough CPU capacity, but Python was not using it effectively.

### Step-by-Step Action

1. Profiled CPU usage.
2. Confirmed workload was CPU-bound.
3. Verified that threading was limited by GIL.
4. Evaluated multiprocessing/subprocess options.
5. Used subprocess isolation for parallel execution.
6. Split workload into independent chunks.
7. Ran chunks across multiple subprocesses.
8. Collected and merged results.
9. Added timeout and failure handling per subprocess.
10. Benchmarked CPU utilization and execution time.

### Result

CPU utilization increased from **10–12% → 1200–1400%**, and execution became around **2x faster**.

### Interview Positioning

Instead of fighting the GIL with threads, I used process-level parallelism. Simple, effective, and much more aligned with CPU-bound workloads.

---

## 14. Kubernetes Node Optimization

### Amazon LPs

* **Primary:** Dive Deep
* **Secondary:** Ownership

### Problem

Kubernetes nodes were facing uneven process distribution and CPU scheduling issues, which created instability and risk of cascade failures.

### What I Observed

* Some nodes were overloaded while others were underused.
* CPU scheduling was not predictable.
* Multiple heavy workloads could spike at the same time.
* Cascading failures were possible during load spikes.

### Step-by-Step Action

1. Reviewed node-level CPU usage.
2. Checked pod placement and scheduling behavior.
3. Identified workload clustering issues.
4. Added CPU affinity rules.
5. Added jitter to avoid simultaneous execution spikes.
6. Tuned node-level parameters.
7. Improved process distribution.
8. Tested under load.
9. Monitored node stability.
10. Reduced risk of cascade failures.

### Result

Kubernetes workload distribution became more stable, reducing CPU contention and failure propagation risk.

### Interview Positioning

This was not just pod scaling. I had to understand node-level behavior, CPU scheduling, process timing, and failure patterns.

---

## 15. Node Isolation for AccountAPI

### Amazon LPs

* **Primary:** Think Big
* **Secondary:** Deliver Results

### Problem

AccountAPI was sharing compute resources with other workloads, causing CPU scheduling bottlenecks and unpredictable latency.

### What I Observed

* AccountAPI was performance-sensitive.
* Shared cluster workloads created noisy-neighbor problems.
* CPU scheduling contention was affecting response time.
* Scaling alone was not solving the root issue.

### Step-by-Step Action

1. Analyzed AccountAPI resource usage.
2. Compared performance during low and high cluster contention.
3. Identified noisy-neighbor impact.
4. Proposed dedicated node/cluster isolation.
5. Created separate resource allocation strategy.
6. Moved AccountAPI to a dedicated cluster.
7. Tuned CPU and scheduling configuration.
8. Ran load tests after isolation.
9. Monitored latency and throughput.
10. Compared before/after performance.

### Result

CPU scheduling bottleneck was removed, and AccountAPI achieved around **30% performance improvement**.

### Interview Positioning

For critical services, isolation can be better than generic shared scaling. This improved predictability and protected AccountAPI from unrelated workloads.

---

# Final Interview Summary

These 15 layers show a pattern of engineering ownership across different levels of the stack:

1. Application-level optimization.
2. Cache and I/O optimization.
3. API latency reduction.
4. CI/CD reliability.
5. Observability.
6. Kafka producer tuning.
7. Kafka consumer tuning.
8. TCP/network-level debugging.
9. Datacenter-level latency reduction.
10. Runtime upgrade.
11. Long-running execution control.
12. Memory leak debugging.
13. CPU parallelism through subprocesses.
14. Kubernetes node-level optimization.
15. Dedicated infrastructure isolation.

The common theme is that I did not only optimize code. I looked at the full system: application behavior, cache, database, Kafka, network, runtime, Kubernetes, infrastructure, observability, and operational reliability.

# One-Line Interview Pitch

I usually approach performance and reliability problems by first measuring the real bottleneck, then fixing it at the correct layer — sometimes that is code, sometimes Redis, Kafka, Python runtime, Kubernetes scheduling, network tuning, or even datacenter placement.




# Amazon Leadership Principles Mapping (15 Stories)

| # | Story / Layer | Primary LP | Secondary LP | Tags |
|---|---------------|------------|--------------|------|
| 1 | Async HTTP Migration | **Bias for Action** | Invent and Simplify | `python` `aiohttp` `asyncio` `http` `performance` `concurrency` `rate-limiting` |
| 2 | Redis Compression & Cache | **Frugality** | Invent and Simplify | `redis` `compression` `cache` `serialization` `cost-optimization` `performance` |
| 3 | AccountsAPI Optimization | **Dive Deep** | Deliver Results | `distributed-lock` `mutex` `redis-lock` `concurrency` `profiling` `latency` `api` |
| 4 | System Reliability (CI/CD) | **Insist on the Highest Standards** | Ownership | `ci-cd` `github-actions` `gitlab-ci` `testing` `quality-gates` `automation` |
| 5 | System Observability | **Dive Deep** | Learn and Be Curious | `grafana` `graylog` `kibana` `prometheus` `logging` `metrics` `tracing` `monitoring` |
| 6 | Kafka Producer Optimization | **Invent and Simplify** | Deliver Results | `kafka` `producer` `batching` `partitioning` `throughput` `scaling` |
| 7 | Kafka Consumer Optimization | **Invent and Simplify** | Deliver Results | `kafka` `consumer` `cilium` `ebpf` `dns` `autoscaling` `performance` |
| 8 | TCP Window / Network Optimization | **Dive Deep** | Learn and Be Curious | `tcp` `networking` `ttfb` `recv-window` `latency` `packet-analysis` |
| 9 | Datacenter Migration | **Think Big** | Have Backbone; Disagree and Commit | `network` `latency` `architecture` `migration` `infra` `benchmarking` |
| 10 | Python Upgrade (3.9 → 3.13) | **Bias for Action** | Deliver Results | `python` `runtime` `upgrade` `benchmark` `cpu` `optimization` |
| 11 | Long-Running Job Termination | **Ownership** | Insist on the Highest Standards | `python` `timeout` `process-management` `ctypes` `signals` `jobs` |
| 12 | Memory Leak Resolution | **Dive Deep** | Ownership | `memory-leak` `gcore` `gdb` `sslcontext` `garbage-collection` `debugging` |
| 13 | GIL Bypass (Subprocess Isolation) | **Invent and Simplify** | Deliver Results | `python` `gil` `multiprocessing` `subprocess` `parallelism` `cpu-bound` |
| 14 | Kubernetes Node Optimization | **Dive Deep** | Ownership | `kubernetes` `cpu-affinity` `scheduler` `jitter` `node-tuning` `linux` |
| 15 | Node Isolation (AccountsAPI) | **Think Big** | Deliver Results | `kubernetes` `dedicated-nodes` `node-selector` `taints` `tolerations` `cluster` `performance` |

---

# Leadership Principle Coverage

## Bias for Action
- Async HTTP Migration
- Python Runtime Upgrade

## Customer Obsession
- *(Can be mapped if any story directly improves customer experience.)*

## Ownership
- System Reliability (CI/CD)
- Long-Running Job Termination
- Memory Leak Resolution
- Kubernetes Node Optimization

## Invent and Simplify
- Async HTTP Migration
- Redis Compression
- Kafka Producer Optimization
- Kafka Consumer Optimization
- GIL Bypass

## Dive Deep
- AccountsAPI Optimization
- System Observability
- TCP Window Optimization
- Memory Leak Resolution
- Kubernetes Node Optimization

## Learn and Be Curious
- System Observability
- TCP Window Optimization

## Think Big
- Datacenter Migration
- Node Isolation

## Have Backbone; Disagree and Commit
- Datacenter Migration

## Deliver Results
- AccountsAPI Optimization
- Kafka Producer Optimization
- Kafka Consumer Optimization
- Python Upgrade
- GIL Bypass
- Node Isolation

## Frugality
- Redis Compression & Cache

## Insist on the Highest Standards
- System Reliability (CI/CD)
- Long-Running Job Termination

---

# Technology Tags

## Python
`python`
`asyncio`
`aiohttp`
`gunicorn`
`uvicorn`
`gil`
`multiprocessing`
`subprocess`
`ctypes`
`profiling`
`memory`
`debugging`

## Backend
`django`
`fastapi`
`api`
`microservices`
`rest`
`grpc`

## Kubernetes
`kubernetes`
`node-selector`
`taints`
`tolerations`
`autoscaling`
`hpa`
`cpu-affinity`
`scheduler`
`pod`
`cluster`

## Kafka
`kafka`
`producer`
`consumer`
`batching`
`partitioning`
`throughput`

## Redis
`redis`
`cache`
`compression`
`distributed-lock`

## Infrastructure
`linux`
`networking`
`tcp`
`dns`
`cilium`
`ebpf`
`latency`
`observability`

## Monitoring
`grafana`
`prometheus`
`graylog`
`kibana`
`logging`
`metrics`
`tracing`

## DevOps
`docker`
`ci-cd`
`gitlab`
`github-actions`
`automation`

## Performance
`benchmark`
`optimization`
`concurrency`
`parallelism`
`throughput`
`latency`
`scalability`
`profiling`

## Debugging
`gdb`
`gcore`
`heap`
`memory-leak`
`core-dump`
`garbage-collection`