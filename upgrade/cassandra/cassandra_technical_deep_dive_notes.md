# ⚡️ Apache Cassandra Technical Notes (Deep Dive)

---

## **1. Use Cases & Features**

- Built for distributed, scalable, write-heavy workloads (e.g., Facebook Inbox, IoT, analytics).
- Peer-to-peer, no SPOF, cross-DC replication; used by Netflix, Apple, etc.
- **Eventual and tunable consistency**: You can configure the consistency level per operation (ONE, QUORUM, ALL, etc.) and further tune it for read and write seperatly.
- **High availability**: Survives node, rack, or even data center failures without downtime.
- **Partition tolerance**: Remains available and functional even under network partition events (AP in CAP theorem).

## 3. **Cassandra vs SQL Structure/Format**

| Feature             | SQL (RDBMS)                              | Cassandra (NoSQL)                                      |
| ------------------- | ---------------------------------------- | ------------------------------------------------------ |
| Top-level Container | Database                                 | Keyspace                                               |
| Table Structure     | Table (rows, columns, types)             | Table (rows, columns, types)                           |
| Primary Key         | Single/composite, global uniqueness      | Composite: Partition Key + Clustering Columns          |
| Indexing            | Global, multi-column, rich index types   | Local to node, simple secondary, materialized views    |
| Query Language      | SQL (rich, ad hoc, JOIN, GROUP BY, etc.) | CQL (SQL-like, no JOINs/aggregates, query-first model) |
| Joins               | Supported                                | Not supported                                          |
| Transactions        | ACID, multi-table/multi-row              | Limited (LWT, per partition, higher latency)           |
| Schema Evolution    | DDL, mature, online/offline changes      | Online DDL, some distributed caveats                   |
| Data Modeling       | Normalized, foreign keys, constraints    | Denormalized, no referential integrity                 |
| Query Pattern       | Flexible, any WHERE, JOIN, GROUP BY      | Rigid: Must use partition key, limited filtering       |
| Scaling             | Vertical (scale-up), limited sharding    | Horizontal (scale-out), consistent hashing             |
| Flexibility         | High query flexibility, less scalable    | High scalability, query-rigid                          |
| Availability        | Master/slave, possible SPOF              | Masterless, peer-to-peer, no SPOF                      |
| Use Case Fit        | OLTP, analytics, transactional           | High-write, large-scale, distributed, IoT, logs, etc.  |

---

## 4. \*\*Indexing: \*\***Cassandra vs DynamoDB**

- **Primary Partition Key**: Same in both; defines data distribution (hash-based).
- **Clustering Key (Cassandra) / Sort Key (DynamoDB)**: Both define row ordering within a partition.
- **Secondary Index (Cassandra)** ≈ **Local Secondary Index (LSI, DynamoDB)**:
  - Both are local to the partition/node, can slow down queries at scale, not ideal for high-cardinality columns. sync in nature.
- **Materialized View (Cassandra)** ≈ **Global Secondary Index (GSI, DynamoDB)**:
  - Both provide alternate query patterns (across partition keys), maintained asynchronously.
  - Both can lag or become inconsistent during heavy writes/outages.

---

## 4. **Partitioning & Distribution**

- **Consistent Hashing** ring: each node holds token ranges.
- **Virtual Nodes (vnodes)**: Node gets multiple ranges for load balancing.
- Edge: Bad hash or poorly chosen partition key → hot partitions/skew.

---

## 5. **Replication**

- **Replication Factor**: Number of copies per row (RF=3 common).
- **Replication strategies**: SimpleStrategy (single DC), NetworkTopologyStrategy (multi-DC/rack).
- Edge: RF < #DCs → not all DCs get a replica; uneven failure domains if racks/DCs are misconfigured.

---

$1
---

## 7. **Handling Conflict Resolution (Inconsistent Data)**

- **Last Write Wins (LWW)**: Conflicts are resolved using timestamps; latest timestamp wins.
- **Read Repair**: On inconsistent reads, the coordinator updates out-of-date replicas in the background.
- **Hinted Handoff**: Writes missed due to node downtime are replayed when the node is back, reducing inconsistency windows.
- **Anti-entropy Repair**: Manual/periodic repair compares data across replicas and syncs differences.
- **Lightweight Transactions (LWT)**: Paxos protocol for per-partition linearizability where strict conflict avoidance is needed (slower, not for bulk writes).
- **Tie-breaker**: If two writes have the exact same timestamp, Cassandra uses byte-wise lexicographical order to break the tie.

---


---

## 7. **Write Path**

- Client → any node (coordinator).
- Coordinator routes to replicas; write = Commit Log + Memtable.
- **Commit Log**: Durability, crash recovery. Write ack after CL met.
- **Memtable**: In-memory, flushed to immutable **SSTable** on disk.
- **Hinted Handoff**: Down node? Hint stored for later delivery.
- Edge: Commit log corruption = possible data loss (rare). Hinted handoff buildup = OOM risk.

---

## 8. **Read Path**

- Coordinator picks replicas, merges Memtable + SSTable + cache.
- **Bloom filters**: Skip unnecessary SSTables.
- **Row/Key cache** for hot data.
- **Read repair**: On inconsistent reads, slowest node updated.
- Edge: Read repair can cause heavy background traffic, affects latency.

---

## 9. **Compaction & Tombstones**

- **Compaction**: Merges/rewrites SSTables, clears tombstones (deletions).
- Strategies: Size-Tiered, Leveled, Time-Window.
- **Tombstones**: Mark deletes; purged after **gc\_grace\_seconds** (\~10 days).
- Edge: Excess tombstones = high read latency/OOM, anti-pattern: wide rows with frequent deletes.

---

## 10. **Failure Handling**

- **Gossip Protocol**: Nodes share cluster state.
- **Phi Accrual Failure Detector**: Tunable, avoids false positives.
- **Bootstrap/Decommission**: Nodes can join/leave with token reassignment.
- Edge: Network partitions = risk of split-brain unless careful with CL.

---

## 11. **Scaling & Ops**

- **Elastic scaling**: Add/remove nodes live; vnodes auto-balance.
- **Multi-DC**: Active-active replication, per-DC CL possible.
- **Docker/K8s/Cloud native**: Supported.
- Edge: Rebalancing can cause compaction storms; plan maintenance windows.

---

## 12. **Security**

- **Auth**: Internal, LDAP, Kerberos.
- **Encryption**: At-rest (disk), in-transit (SSL/TLS), internode encryption.
- Edge: Misconfig = unencrypted internode traffic, beware during upgrades.

---

## 13. **Performance Tuning**

- JVM pauses are there, tune JVM heap/GC configs for better performance  (avoid full GCs).
- Tune memtable, SSTable, compaction size/threads.
- Monitor: tombstone warnings, dropped messages, GC pauses.
- Edge: Hot partitions; overloaded nodes cause cluster-wide backpressure.

---

## 14. **Backups & Recovery**

- **Snapshots**: Point-in-time backups (hard-link SSTables, provide fast SNAPSHOT).
- **Incremental backups**: For delta changes.
- Edge: Restore is manual/slow for large clusters; backup consistency not guaranteed unless quiesced.
- **Change Data Capture (CDC)**: Log row-level changes for streaming.

## 16. **Compaction & Maintenance Edge Cases**

- Disk full during compaction = cluster can halt.
- Manual compaction is needed for tombstone-heavy tables.
- **Repair** (anti-entropy): Required to keep replicas consistent, but resource-heavy.

---

## 17. **Real-World Failure Scenarios**

- Partial writes: Not rolled back if consistency is not met, but may still exist on some replicas.
- Split-brain: Solution: Use LOCAL\_QUORUM for geo-distributed clusters to avoid n/w partition.
- Downtime recovery: Prefer multi-DC, proper rack config, and run regular repairs.

---

## 18. **Recent Enhancements (4.x+)**

- Zero-copy streaming for ultimate fast node ops(inspired from kafka zero-copy model)
- Improved audit logging, JVM stability, SAI (Storage Attached Index).
- Better metrics, automated repair options.

---

## 19. **Best Practices**

- Always model data for your **queries** (read/query-first).
- Avoid unbounded partitions.
- Schedule regular repairs, monitor compaction & tombstone metrics.
- Test backup & restore in staging.
- Use NetworkTopologyStrategy for production.

---

**Anything you want to expand further, or export as markdown file?**
Let me know if you want extra “gotchas” or deeper dives on specific subsystems.

