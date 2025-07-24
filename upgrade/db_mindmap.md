# 📚 Database Systems: ASCII Mind Map (Extended)

## 1. Database Isolation Levels
```
Database Isolation Levels
│
├─ Read Uncommitted
│   ├─ Dirty Read 😬
│   └─ Non-repeatable Read
│
├─ Read Committed
│   ├─ Avoids Dirty Read
│   └─ Allows Non-repeatable Read
│
├─ Repeatable Read
│   ├─ Prevents Dirty/Non-repeatable Read
│   └─ Allows Phantom Read 👻
│
└─ Serializable
    └─ Highest Isolation (Prevents all anomalies)
```

## 2. Concurrency Control
```
Concurrency Control
│
├─ Pessimistic (PCC)
│   ├─ Locks resources (block/blocker)
│   └─ Used when conflicts are frequent
│
└─ Optimistic (OCC)
    ├─ No locks, validate at commit
    └─ Used when conflicts are rare
```

## 3. Caching Strategies
```
Caching Strategies
│
├─ Read-Aside (Lazy Loading)
│   ├─ App checks cache, loads from DB on miss
│   └─ Manual cache update
│
├─ Read-Through
│   ├─ Cache auto-fetches from DB on miss
│   └─ App only queries cache
│
├─ Write-Aside (Write-Around)
│   ├─ Write to DB, update cache manually
│   └─ Cache may be stale
│
├─ Write-Through
│   ├─ Write to cache & DB simultaneously
│   └─ Ensures cache & DB sync
│
└─ Write-Behind (Write-Back)
    ├─ Write to cache first, async flush to DB
    └─ Fast writes, risk of data loss
```

## 4. Partitioning
```
Partitioning
│
├─ Horizontal (Sharding)
│   ├─ Row-wise split
│   └─ Used for scale out
│
├─ Vertical
│   ├─ Column-wise split
│   └─ Separate hot/cold data
│
└─ Functional/Directory
    ├─ By function (tables/data types)
    └─ Common in legacy systems
```

## 5. Indexing
```
Indexing
│
├─ B-Tree (General, Range)
│
├─ Hash (Equality)
│
├─ Bitmap (OLAP, low-cardinality)
│
├─ Composite/Multicolumn
│
├─ Covering Index (Included Columns)
│
├─ Full-Text Index
│
├─ Spatial (GIS, Geospatial)
│
└─ Unique Index
```

## 6. SQL Databases
```
SQL Databases
│
├─ ACID properties
│   ├─ Atomicity
│   ├─ Consistency
│   ├─ Isolation
│   └─ Durability
│
├─ Schema (Structured)
│
├─ Joins (Inner, Outer, Self, Cross)
│
├─ Constraints (PK, FK, Unique, NotNull)
│
└─ Indexes (See above)
```

## 7. NoSQL Databases
```
NoSQL Databases
│
├─ Types
│   ├─ Document (MongoDB)
│   ├─ Key-Value (Redis, DynamoDB)
│   ├─ Wide-Column (Cassandra, HBase)
│   └─ Graph (Neo4j)
│
├─ CAP Theorem
│   ├─ Consistency
│   ├─ Availability
│   └─ Partition Tolerance
│
├─ BASE Properties
│   ├─ Basically Available
│   ├─ Soft state
│   └─ Eventually Consistent
│
└─ Query Patterns
    ├─ Aggregation
    ├─ Map-Reduce
    └─ Secondary Indexes
```

## 8. Logging & Change Data Capture
```
Logging & Change Data Capture
│
├─ Write-Ahead Log (WAL)
│   ├─ Sequential record of DB changes
│   └─ Used in PostgreSQL, SQLite
│
├─ Change Logs
│   ├─ Captures all changes (CDC)
│   └─ Used for audit, replication, recovery
│
├─ Oplog (MongoDB)
│   ├─ Operation log for replica sets
│   └─ Tailable, size-bound collection
│
├─ WiredTiger Log (MongoDB)
│   ├─ Storage engine log
│   └─ Handles journaling, checkpoints
│
└─ Transaction Log (SQL Server)
    └─ For recovery and rollback
```

## 9. File Management & Storage Formats
```
File Management & Storage
│
├─ Data Files
│   ├─ MDF (SQL Server main data file)
│   ├─ NDF (Secondary data file)
│   └─ LDF (Log file in SQL Server)
│
├─ MongoDB Files
│   ├─ WiredTiger (.wt)
│   └─ Oplog.bson
│
├─ MySQL Files
│   ├─ .frm (Table format)
│   ├─ .ibd (InnoDB tablespace)
│   └─ binlog (binary log)
│
└─ SQLite File
    └─ .db file, includes WAL if enabled
```

## 10. Replication & Syncing Strategies
```
Replication & Syncing
│
├─ Master-Slave (Primary-Secondary)
│   ├─ Writes go to master, reads from slaves
│   └─ Asynchronous or Semi-sync
│
├─ Multi-Master
│   ├─ Writes accepted everywhere
│   └─ Conflict resolution needed
│
├─ Log-based (CDC)
│   ├─ Replication via log tailing (Oplog, WAL, Binlog)
│   └─ Used in MongoDB, MySQL
│
├─ File/Chunk-based
│   ├─ Data split into chunks for sharding
│   └─ Each chunk can have replicas
│
└─ Quorum/Consensus
    ├─ Paxos/Raft for distributed DBs
    └─ Used in etcd, CockroachDB, etc.
```

## 11. Redis & Redis Cluster
```
Redis & Redis Cluster
│
├─ Standalone Replication
│   ├─ Master/Replica model
│   └─ Replication is asynchronous
│
├─ Redis Sentinel
│   ├─ Monitors masters & replicas
│   └─ Auto-failover
│
└─ Redis Cluster
    ├─ Data partitioned by hash slots (0-16383)
    ├─ Horizontal scalability
    ├─ Multiple masters, each with replicas
    └─ Supports partial availability
```
