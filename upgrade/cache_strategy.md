## 🧠 Common Read Strategies

| **Aspect**                  | **Read-Aside (Cache-Aside)**                                                                                          | **Read-Through**                                                                                                   |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Working (Step-by-step)**  | 1. App checks cache → <br>2. On **miss**, queries DB → <br>3. App manually updates cache                                  | 1. App queries cache → <br>2. On **miss**, cache fetches from DB → <br>3. Cache returns result to app                 |
| **App Responsibility**      | ✅ Full: cache lookup, DB fallback, cache update                                                                          | ✅ Minimal: just query cache                                                                                           |
| **Cache Responsibility**    | Simple key-value store                                                                                                   | Handles cache population, DB fetch                                                                                    |
| **Pros**                    | ✅ Simple & flexible <br>✅ Tolerant to cache failure <br>✅ App has full control                                           | ✅ Simplified logic <br>✅ Fewer DB hits <br>✅ Unified behavior across services                                       |
| **Cons**                    | ❌ Manual cache invalidation <br>❌ Stale data risk <br>❌ Thundering herd                                                 | ❌ Single point of failure (cache) <br>❌ Stale data <br>❌ Rigid schema                                                |
| **Latency**                 | ⏱️ Fast on hit <br>⏳ Slower on miss                                                                                       | ⏱️ Consistently fast (central handling)                                                                               |
| **Fault Tolerance**         | ✅ High (fallback to DB)                                                                                                   | ❌ Low (cache down = app down)                                                                                        |
| **Best Use Cases**          | Read-heavy systems <br>Rarely changing data <br>App needs cache control                                                  | Centralized services <br>Standardized APIs <br>High-read traffic                                                      |

---

## ✍️ Common Write Strategies

| **Aspect**                  | **Write-Aside**                                                                                      | **Write-Through**                                                                                     | **Write-Behind / Back**                                                                                  |
|-----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Working (Step-by-step)**  | 1. App writes to DB → <br>2. App updates or invalidates cache                                           | 1. App writes to cache → <br>2. Cache writes to DB synchronously                                          | 1. App writes to cache → <br>2. Cache asynchronously writes to DB (e.g. via queue)                          |
| **App Responsibility**      | ✅ Full: write DB and manage cache                                                                      | ✅ Low: only write to cache                                                                               | ✅ Low: only write to cache                                                                                  |
| **Cache Responsibility**    | Passive (manual updates)                                                                                | Active (writes to DB in sync)                                                                            | Active (writes to DB in background)                                                                         |
| **Pros**                    | ✅ Fine-grained control <br>✅ Prevents stale reads (if handled right)                                    | ✅ Consistent DB and cache <br>✅ No miss on new entries                                                   | ✅ Fastest writes <br>✅ Highly fault-tolerant <br>✅ Perfect for async-heavy workloads                        |
| **Cons**                    | ❌ Write fails if DB is down <br>❌ Manual invalidation complexity                                        | ❌ Higher latency <br>❌ Needs 2PC or coordination for durability                                         | ❌ Risk of data loss on crash <br>❌ Data may vanish if TTL < DB downtime                                     |
| **Latency**                 | ⏱️ Medium                                                                                               | 🐢 Slow (DB sync)                                                                                         | ⚡ Fast                                                                                                       |
| **Fault Tolerance**         | ❌ Low (relies on DB)                                                                                   | ❌ Low (sync failure fails all)                                                                           | ✅ High (buffered with queues/workers)                                                                       |
| **Best Use Cases**          | Low write frequency <br>App-managed cache <br>Reads dominate                                           | High consistency apps <br>Critical systems <br>Write = Read frequency                                     | Event streaming <br>Telemetry/logs <br>Heavy write → eventual persistence OK                                 |




## 🔍 Other Read Caching Strategies


### 1. **Write-Through Read (Pre-warmed Cache)**
- ❌ **Problem**: New data causes cache miss on first access.
- ✅ **Solution**: Cache is populated during writes, ensuring read hits.
- ⚠️ **Tradeoff**: Memory wasted on unread data.

---

### 2. **Refresh-Ahead (Auto-Refresh on Expiry)**
- ❌ **Problem**: TTL expiry causes read spikes and cache miss storms.
- ✅ **Solution**: Background job refreshes cache before it expires.
- ⚠️ **Tradeoff**: Extra compute for unused data; TTL tuning required.

---

### 3. **Near Cache (Multi level Cache)**
- ❌ **Problem**: Remote cache introduces latency on every read.
- ✅ **Solution**: Clients maintain fast in-memory local caches.
- ⚠️ **Tradeoff**: Data may be inconsistent across nodes.


## 🔍 Other Write Caching Strategies

### 1. Write-Combining / Coalesced Writes (Bonus)
- ❌ **Problem**: High write frequency overwhelms DB with small updates.
- ✅ **Solution**: Aggregate multiple writes in memory or queue and flush in batches.
- ⚠️ **Tradeoff**: Complexity in batching + risk of data loss if not flushed timely.
