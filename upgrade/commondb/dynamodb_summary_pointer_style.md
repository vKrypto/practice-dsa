# Amazon DynamoDB

## 🔥 Best Use Cases

- Apps needing **massive scalability** & single-digit ms latency (e-commerce, gaming, IoT, real-time analytics, serverless)
- **Primary-key only** (partition/sort key) access; design for **eventual consistency**/**high availability**

## ⚡ Conditions for Best Performance

1. **Embrace Eventual Consistency:** Strongly consistent reads optional, higher latency/cost.
2. **No Complex Joins:** Denormalize/precompute; DynamoDB isn’t for multi-table queries or SQL joins.
3. **Partition Key Design:** Avoid “hot” keys—uneven access throttles/wastes capacity.
4. **Indexes:** Queries should not required more than one partition. Avoid More GSI, if really necessary try having LSI, as GSI are costly, also for each query only one partion key will be used from (primary partition, all GSI partition keys)
5. **Transactions:** ACID for up to 25 items (single-region); not for complex relational/multi-table ops.

> **Working Principle:**\
> Fetch by partition (and sort) key—then filter, sort, and aggregate *within* the partition. Any cross-partition (scatter-gather) = **bad performance**.

## 🚫 Worst Use Cases

- Complex joins/relational data, multi-table transactions, or full-table analytics/aggregations
- Strong consistency *everywhere*, low-traffic use (costly/overkill)

## 🛑 Limits (2025)

- **Item:** 400 KB max
- **Partition:** 10 GB, 3,000 RCU, 1,000 WCU
- **Indexes:** 20 GSIs, 5 LSIs/table (limits may change)
- **Query:** Key-value/range only (no joins/subqueries)
- **PITR:** Up to 35 days
- **Transaction:** Max 25 items or 4 MB

## ⚡ Features

- **High availability, multi-region, auto scaling**
- **3x durability** (multi-node replication)
- **Configurable consistency:** per-request (eventual or strong)
- **Minimal ops:** No server mgmt, auto backup/restore/failover
- **Streams, snapshots, global tables, direct export (S3/Kinesis/Redshift)**

---

## Indexing:

### Primary Index
- Every table has **1 Primary Index**.
    - **Partition Key** (mandatory)
    - **Sort Key** (optional)
- Used for direct (fastest) queries.


### Local Secondary Index (LSI)
- **Up to 5 LSIs per table**
    - **Same Partition Key** as table
    - **Different Sort Key**
    - **Created only at table creation**
    - **Local**: operates within the partition
    - **10GB limit** per partition key (across all items in partition for that LSI)
- **Use case:** Alternate range queries within a single partition.


### Global Secondary Index (GSI)
- **Up to 20 GSIs per table**
    - **Different Partition Key** and/or **Sort Key**
    - **Created any time** (add/remove as needed)
    - **Global**: index spans all partitions, is distributed
    - **No size limit** like LSI
    - **Supports alternate query patterns**
- **Downside:** More GSIs = higher write costs, potential for throttling, slower writes due to extra index maintenance.


### Querying & Patterns
- **Each query uses only one index** (primary or one GSI)  
    - *You can’t combine multiple GSIs in a single query.*
- **LSIs** can be used in combination with the primary index for range queries within a partition.
- **Multiple query patterns?**  
    - Add multiple GSIs (think: each GSI = one new query pattern)


### Caveats
- **More GSIs = higher costs, write throttling, and slower write performance** (each write may update multiple indexes)
- **LSI = local, limited, and strong consistency**
- **GSI = global, flexible, but may lag (eventual consistency by default)**


### Summary Table

| Type   | Count | Partition Key | Sort Key | Add/Remove | Limit     | Scope   | Use Case                |
|--------|-------|--------------|----------|------------|-----------|---------|-------------------------|
| Primary| 1     | Required     | Optional | On creation| -         | Global  | Direct access           |
| LSI    | 5    | Same as tbl  | Diff     | Create only| 10GB/part | Local   | Range queries/partition |
| GSI    | 20    | Any          | Any      | Any time   | -         | Global  | Alt. query patterns     |

### Pro Tip

Design GSIs only for necessary query patterns; more GSIs = more cost and operational headaches.

---

## DAX (DynamoDB Accelerator)
DAX is an in-memory caching layer that sits in front of DynamoDB, managed by AWS to boost performance.

| Feature                | Description                                                                    |
|------------------------|--------------------------------------------------------------------------------|
| In-memory caching      | Uses RAM for ultra-fast data access and lookups.                               |
| Write-through caching  | Writes/updates via DAX update both DynamoDB and cache for consistency.         |
| Read-through caching   | Reads served from cache; on miss, fetch from DB, then cache result.            |
| Clustered              | Multiple nodes for high availability, fault tolerance, and horizontal scaling. |

---
### TL;DR:

- **DynamoDB = Zero ops, high scale, always-on, key-value DB.**
- **Not for analytics/relational queries.**
- **Great for microservices, IoT, and any ultra-low latency, high throughput app.**
- **DAX = DynamoDB on steriod mode**


