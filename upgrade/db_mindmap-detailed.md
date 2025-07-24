# 📚 Database Systems: ASCII Mind Map (Extended, Annotated)

## 1. Database Isolation Levels
```
Database Isolation Levels
│
├─ Read Uncommitted
│   ├─ Dirty Read 😬         # Reads uncommitted data; classic “phantom balance” bug in banking.
│   └─ Non-repeatable Read  # Value can change during same txn, race condition galore.
│
├─ Read Committed
│   ├─ Avoids Dirty Read    # Still not safe from lost updates—think two users editing profile.
│   └─ Allows Non-repeatable Read  # "What you see may not be what you update!"
│
├─ Repeatable Read
│   ├─ Prevents Dirty/Non-repeatable Read # Inserted rows mid-txn still visible = phantom reads.
│   └─ Allows Phantom Read 👻           # Range queries are the weak spot.
│
└─ Serializable
    └─ Highest Isolation (Prevents all anomalies) # Great for consistency, but slow—deadlocks and rollbacks common.
```

## 2. Concurrency Control
```
Concurrency Control
│
├─ Pessimistic (PCC)
│   ├─ Locks resources (block/blocker)   # Classic “table lock” woes; can stall the DB.
│   └─ Used when conflicts are frequent  # Can kill performance if overused; deadlock-prone.
│
└─ Optimistic (OCC)
    ├─ No locks, validate at commit      # Fast when conflicts are rare; retry storm if contention spikes.
    └─ Used when conflicts are rare      # Used in modern NoSQL, but not for hot tables!
```

## 3. Caching Strategies
```
Caching Strategies
│
├─ Read-Aside (Lazy Loading)
│   ├─ App checks cache, loads from DB on miss   # Manual eviction, risk of stale cache if app forgets.
│   └─ Manual cache update                      # Great for rarely changed data; app owns logic.
│
├─ Read-Through
│   ├─ Cache auto-fetches from DB on miss       # Transparent to app; cache can get overloaded on DB outage.
│   └─ App only queries cache                   # “Single source” at runtime, but cache warmup is slower.
│
├─ Write-Aside (Write-Around)
│   ├─ Write to DB, update cache manually       # First read = cache miss; common in batch loads.
│   └─ Cache may be stale                       # Not for hot write scenarios!
│
├─ Write-Through
│   ├─ Write to cache & DB simultaneously       # Always in sync, but adds write latency.
│   └─ Ensures cache & DB sync                  # Not all caches support this natively.
│
└─ Write-Behind (Write-Back)
    ├─ Write to cache first, async flush to DB  # Lightning writes, but a server crash can drop data.
    └─ Fast writes, risk of data loss           # Always set up persistence or backup!
```

## 4. Partitioning
```
Partitioning
│
├─ Horizontal (Sharding)
│   ├─ Row-wise split                          # True scale-out; tricky to rebalance!
│   └─ Used for scale out                      # Joins across shards = pain.
│
├─ Vertical
│   ├─ Column-wise split                       # Hot columns separate from cold; can optimize I/O.
│   └─ Separate hot/cold data                  # Changing schema later is tough.
│
└─ Functional/Directory
    ├─ By function (tables/data types)         # E.g., separate tables for logs, users, audit.
    └─ Common in legacy systems                # Hard to enforce referential integrity.
```

## 5. Indexing
```
Indexing
│
├─ B-Tree (General, Range)                     # Default for most DBs; great for range queries.
│
├─ Hash (Equality)                             # Lightning fast for exact lookups, useless for range scans.
│
├─ Bitmap (OLAP, low-cardinality)              # Shines in analytics, bloats if too many distinct values.
│
├─ Composite/Multicolumn                       # Order of columns matters! Best for multi-col WHERE.
│
├─ Covering Index (Included Columns)           # Query served from index only, avoids table lookups.
│
├─ Full-Text Index                             # Specialized for searching text/blobs.
│
├─ Spatial (GIS, Geospatial)                   # Geographical coordinates—think Uber/Swiggy.
│
└─ Unique Index                                # Enforces data uniqueness; can slow down inserts.
```

## 6. SQL Databases
```
SQL Databases
│
├─ ACID properties
│   ├─ Atomicity    # All-or-nothing; partial updates auto-rollback.
│   ├─ Consistency  # Enforces rules (PK/FK) before commit.
│   ├─ Isolation    # Controls concurrent effects; see above.
│   └─ Durability   # Survives power loss, relies on WAL/logs.
│
├─ Schema (Structured)     # Rigid schema, migration = planned event.
│
├─ Joins (Inner, Outer, Self, Cross)  # Joins are power—but can be slow on huge tables.
│
├─ Constraints (PK, FK, Unique, NotNull)  # Keep data clean, but can block inserts/updates.
│
└─ Indexes (See above)                   # Choose wisely, or suffer slow queries.
```

## 7. NoSQL Databases
```
NoSQL Databases
│
├─ Types
│   ├─ Document (MongoDB)         # Flexible JSON-like docs; “schema-less”, but not “structure-less”.
│   ├─ Key-Value (Redis, DynamoDB) # Ultra fast, but query = key or nothing.
│   ├─ Wide-Column (Cassandra, HBase) # Designed for sparse data and time series.
│   └─ Graph (Neo4j)               # Think “friends of friends” or network traversals.
│
├─ CAP Theorem
│   ├─ Consistency   # Every read = latest write, but may cost availability.
│   ├─ Availability  # DB always answers, even if it’s “stale” data.
│   └─ Partition Tolerance # Survives network splits, but often must trade-off other two.
│
├─ BASE Properties
│   ├─ Basically Available   # Always on, but maybe not up-to-date.
│   ├─ Soft state            # Intermediate state is ok, eventual convergence.
│   └─ Eventually Consistent # After some time, everyone agrees (hopefully).
│
└─ Query Patterns
    ├─ Aggregation          # Think map-reduce, big data ops.
    ├─ Map-Reduce           # Distributed compute, not instant.
    └─ Secondary Indexes    # Not always supported—beware secondary index “gotchas” in NoSQL.
```

## 8. Logging & Change Data Capture
```
Logging & Change Data Capture
│
├─ Write-Ahead Log (WAL)
│   ├─ Sequential record of DB changes    # Always written BEFORE data page is updated.
│   └─ Used in PostgreSQL, SQLite         # Recovery depends on this.
│
├─ Change Logs
│   ├─ Captures all changes (CDC)         # Enables ETL, downstream sync, audit trails.
│   └─ Used for audit, replication, recovery # CDC lag can cause sync drift.
│
├─ Oplog (MongoDB)
│   ├─ Operation log for replica sets     # Capped collection; size managed automatically.
│   └─ Tailable, size-bound collection    # Oplog rollover can break late-joining replicas.
│
├─ WiredTiger Log (MongoDB)
│   ├─ Storage engine log                 # Handles crash recovery, periodic checkpoints.
│   └─ Handles journaling, checkpoints    # Faster but needs careful tuning.
│
└─ Transaction Log (SQL Server)
    └─ For recovery and rollback          # Too big = restore pain, too small = slow performance.
```

## 9. File Management & Storage Formats
```
File Management & Storage
│
├─ Data Files
│   ├─ MDF (SQL Server main data file)    # Core data, can grow huge.
│   ├─ NDF (Secondary data file)          # For spreading load across disks.
│   └─ LDF (Log file in SQL Server)       # All changes until checkpoint; crucial for recovery.
│
├─ MongoDB Files
│   ├─ WiredTiger (.wt)                   # Modern default, fast and space efficient.
│   └─ Oplog.bson                         # Oplog stored as capped BSON file.
│
├─ MySQL Files
│   ├─ .frm (Table format)                # Table metadata, pain in manual migration.
│   ├─ .ibd (InnoDB tablespace)           # Row data and indexes.
│   └─ binlog (binary log)                # Used for replication and point-in-time recovery.
│
└─ SQLite File
    └─ .db file, includes WAL if enabled  # Entire DB in a file—portable, but single-writer lock!
```

## 10. Replication & Syncing Strategies
```
Replication & Syncing
│
├─ Master-Slave (Primary-Secondary)
│   ├─ Writes go to master, reads from slaves   # Common for scaling reads; risk: stale reads.
│   └─ Asynchronous or Semi-sync               # Possible data loss if master crashes before slaves sync.
│
├─ Multi-Master
│   ├─ Writes accepted everywhere              # Great for uptime, but watch out for conflicts!
│   └─ Conflict resolution needed              # Last write wins ≠ correct business logic.
│
├─ Log-based (CDC)
│   ├─ Replication via log tailing (Oplog, WAL, Binlog) # True near-real-time sync.
│   └─ Used in MongoDB, MySQL                  # “Log lag” can create recovery windows.
│
├─ File/Chunk-based
│   ├─ Data split into chunks for sharding     # Can move or rebalance as traffic shifts.
│   └─ Each chunk can have replicas            # Hotspots possible if chunks unbalanced.
│
└─ Quorum/Consensus
    ├─ Paxos/Raft for distributed DBs          # True HA, but slow on big clusters.
    └─ Used in etcd, CockroachDB, etc.         # Watch for split-brain, network partitioning edge cases.
```

## 11. Redis & Redis Cluster
```
Redis & Redis Cluster
│
├─ Standalone Replication
│   ├─ Master/Replica model                    # Single master, all writes go there.
│   └─ Replication is asynchronous             # Replica lag possible.
│
├─ Redis Sentinel
│   ├─ Monitors masters & replicas             # Provides auto-failover.
│   └─ Auto-failover                          # Split-brain can still happen if network flaky.
│
└─ Redis Cluster
    ├─ Data partitioned by hash slots (0-16383) # Each node owns a range; rebalancing needed for growth.
    ├─ Horizontal scalability                  # Scale out, but multi-key ops need keys on same slot.
    ├─ Multiple masters, each with replicas    # Partition tolerance but needs client awareness.
    └─ Supports partial availability           # Will serve if >half masters up, else fail closed.
```

