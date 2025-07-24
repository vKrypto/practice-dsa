# 🧠 In-Depth DB Tech Mind Map (with Key Subtopics)

DB Universe
|
├── Neo4j (Native Graph DB)
|    ├─ **Model**: Native property graph; nodes/edges with flexible schema.
|    ├─ **Query**: Cypher language; expressive for graph traversals.
|    ├─ **Use-Case**: Social, fraud, recommendations—anything “relationship-first”.
|    ├─ **ACID**: Strong ACID on single op; not built for multi-graph distributed tx.
|    ├─ **Scaling**: Vertical (cluster sharding is tricky, not linear).
|    ├─ **Indexing**: Node/relationship indexes, not like RDBMS.
|    ├─ **Edge Cases**: Deep traversals fast; not ideal for analytical queries or massive unrelated data.
|    └─ **Limitations**: Memory-intensive, not for general OLTP, not a document or tabular DB.

|
├── Cassandra (Wide Column, AP, Masterless)
|    ├─ **Model**: Wide-column, partitions (row keys), columns are flexible.
|    ├─ **Consistency**: Tunable (from eventual to strong), via QUORUM/ONE/ALL.
|    ├─ **Write Path**: Fast (append-only, memtable+SSTable), LSM tree.
|    ├─ **Read Path**: Multi-step (memtable, bloom filters, SSTables); good with right keys.
|    ├─ **Indexing**: Primary, clustering, secondary (inefficient for high-cardinality).
|    ├─ **Transactions**: No multi-row ACID; lightweight via Paxos (slow).
|    ├─ **Replication**: Built-in, multi-DC, snitch/replication strategies.
|    ├─ **Scaling**: Linear, just add nodes (masterless).
|    ├─ **Durability**: Commit log (WAL), hints, repair for anti-entropy.
|    ├─ **Schema Design**: Query-based, denormalize everything, avoid joins.
|    ├─ **Monitoring**: JMX exporter, Datastax exporter.
|    ├─ **Tools**: nodetool, cqlsh, OpsCenter.
|    ├─ **Edge Cases**: Tombstones (deletes linger), hot partitions, time-series friendly.
|    └─ **Limitations**: Not for transactional (OLTP), weak ad-hoc queries.

|
├── DynamoDB (AWS KV/Document, Managed NoSQL)
|    ├─ **Model**: Table (KV or Document); primary key: partition + optional sort key.
|    ├─ **Scaling**: Auto-sharded, fully managed, scales to petabytes.
|    ├─ **Consistency**: Default eventual, option for strong reads.
|    ├─ **Concurrency**: OCC (optimistic, versioned writes), no locks.
|    ├─ **Indexes**: GSI (global), LSI (local), but add cost/latency.
|    ├─ **Durability**: Multi-AZ replication, point-in-time restore, backups.
|    ├─ **Caching**: DAX for in-memory, low-latency cache layer.
|    ├─ **Transactions**: Multi-item ACID with “transactWrite”, but with limits.
|    ├─ **Limits**: 400KB item size, partition throughput, hot partition risk.
|    ├─ **Monitoring**: CloudWatch, DAX metrics.
|    ├─ **Edge Cases**: TTL for auto-expiry, no joins, query design is crucial.
|    └─ **Limitations**: Expensive at scale (R/W units), secondary index costs.

|
├── InfluxDB (Time-Series, Metrics-first)
|    ├─ **Model**: Measurement (table), tags (indexed), fields (not indexed), time is primary key.
|    ├─ **Storage**: LSM/SSTable-like, columnar, optimized for append/write.
|    ├─ **Write**: Super-fast ingest, batch inserts, retention policies.
|    ├─ **Query**: InfluxQL/Flux, optimized for aggregations, windowing.
|    ├─ **ACID**: No strict ACID, focuses on durability and performance.
|    ├─ **Retention**: Auto-drop old data (configurable), compaction.
|    ├─ **Indexing**: Time and tags only; fields are not indexed.
|    ├─ **Scaling**: Horizontal (cluster/enterprise), but OSS is single-node.
|    ├─ **Durability**: WAL, snapshots, hinted handoff for reliability.
|    ├─ **Edge Cases**: Not for OLTP, limited full-text/search, schema is fixed after first write.
|    └─ **Limitations**: Joins are painful, no rich relations.

|
├── TimescaleDB (PostgreSQL Extension for Time-Series)
|    ├─ **Model**: Native SQL, adds “hypertables” (partitioned by time, space).
|    ├─ **Query**: Full SQL, aggregates, window functions, JOINs.
|    ├─ **ACID**: Full PostgreSQL ACID compliance.
|    ├─ **Storage**: Chunked tables, automatic partitioning.
|    ├─ **Compression**: Native compression, saves storage for historical data.
|    ├─ **Scaling**: Vertical in OSS, distributed in Enterprise.
|    ├─ **Indexing**: All PostgreSQL indexes + time-based optimizations.
|    ├─ **Durability**: WAL, PITR, snapshots (as in Postgres).
|    ├─ **Edge Cases**: No “out-of-order” time inserts, hypertable management.
|    └─ **Limitations**: Not as fast as Influx for pure metrics, but better for hybrid workloads.

|
├── MongoDB Time-Series Collection
|    ├─ **Model**: Documents, each “bucket” stores many points.
|    ├─ **Write**: High ingest for time-stamped data, data auto-bucketed.
|    ├─ **Query**: Aggregation pipeline, basic time-series ops.
|    ├─ **Indexing**: Indexed on time, meta fields; fields inside bucket are not indexed.
|    ├─ **ACID**: Per-document only (like all MongoDB), not cross-bucket.
|    ├─ **Scaling**: Native sharding/replication.
|    ├─ **Durability**: WiredTiger storage engine, journaling, Oplog for replication.
|    ├─ **Edge Cases**: Poor for heavy analytics; good for IoT/metrics, not as fast as purpose-built TSDBs.
|    └─ **Limitations**: No joins, bucket size limit, lack of advanced analytics.

|
├── PostgreSQL Graph Extension (e.g., AGE, pgGraph, Apache AGE)
|    ├─ **Model**: Adds property graph support, Cypher queries, overlays on relational tables.
|    ├─ **Query**: Cypher/Gremlin support (depends on extension).
|    ├─ **Indexing**: Uses PSQL B-tree/GiST/GIN for nodes/edges.
|    ├─ **ACID**: Full PostgreSQL.
|    ├─ **Durability**: WAL, PITR, as per PostgreSQL.
|    ├─ **Edge Cases**: Not as fast as Neo4j for deep traversals, good for “graph over SQL data”.
|    └─ **Limitations**: Extension-specific quirks; sometimes limited language coverage.

|
├── MongoDB Graph Workloads ($graphLookup)
|    ├─ **Model**: Document-centric; $graphLookup for recursion.
|    ├─ **Query**: Aggregation pipeline; recursive traversal with depth limits.
|    ├─ **Indexing**: No native edge index; relies on document model.
|    ├─ **Edge Cases**: Suitable for shallow/medium graph; falls short for deep graph ops.
|    ├─ **Scaling**: As per Mongo sharding/replication.
|    └─ **Limitations**: Inefficient for deep/complex traversals; not a true graph DB.

---

# Summary Table of Key Points (for all):

| DB/Extension            | Best For               | Scaling    | ACID      | Indexing              | Special Edge Case                 |
|------------------------ |-----------------------|------------|-----------|-----------------------|-----------------------------------|
| Neo4j                  | Deep relationships     | Vertical   | Yes (1 op)| Native node/edge      | Fast traversals, not for OLTP     |
| Cassandra              | Massive scale, writes  | Linear     | Limited   | Primary, 2ndary weak  | Tombstones, partition planning    |
| DynamoDB               | Managed, auto-scale    | Linear     | Yes (scoped) | PK, GSI, LSI       | Hot partitions, 400KB limit       |
| InfluxDB               | Time-series, metrics   | Horizontal | No        | Time+tag only         | High ingest, fixed schema         |
| TimescaleDB            | SQL+Time-series        | Vertical   | Yes       | All PSQL + time       | Hypertable, chunk management      |
| Mongo Time-Series      | IoT, time docs         | Horizontal | Per-doc   | Time/meta fields      | Buckets, not for analytics        |
| PSQL Graph Extension   | Graph over SQL         | Vertical   | Yes       | PSQL                  | Not native graph perf             |
| Mongo $graphLookup     | Small graphs           | Horizontal | Per-doc   | None                  | Not true graph DB                 |

---

