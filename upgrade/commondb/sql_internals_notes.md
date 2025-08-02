# 📚 SQL Internals & Architecture – Full Notes

## 1. Data Types
- **Numeric**: `INT`, `BIGINT`, `DECIMAL`, `FLOAT`
- **Character**: `CHAR`, `VARCHAR`, `TEXT`
- **Date & Time**: `DATE`, `DATETIME`, `TIME`, `TIMESTAMP`
- **Binary**: `BINARY`, `VARBINARY`
- **Others**: `BOOLEAN`, `JSON`, `XML`, `UUID` (varies by DBMS)

---

## 2. Storage Architecture
- **MDF**: Primary data file (`.mdf`) – holds schema & data
- **NDF**: Secondary data files (`.ndf`) – used when DB spans multiple disks
- **LDF**: Log file (`.ldf`) – used for transactional log (WAL)
- **Filegroups**: Logical groupings of MDF/NDF files for I/O distribution
- **Storage Engine**: Manages physical data handling (e.g., InnoDB, SQL Server Engine)

---

## 3. File Partitioning & Filegroups
- Split large tables for:
  - Parallel I/O
  - Partition pruning
  - Optimized maintenance
- Example: Separate data by year in different partitions

---

## 4. Indexing

### 4.1 Types of Indexes

#### a. By Structure
- **Clustered Index**: Physically sorts the data; only **one** allowed
- **Non-Clustered Index**: Logical index with pointer to actual data; many allowed

#### b. By Columns
- **Single-column**: Basic index on one column
- **Composite/Multi-column**: Combined column index

#### c. By Usage
- **Covering Index**: Includes all columns needed for the query
- **Filtered Index**: Includes rows based on WHERE conditions
- **Unique Index**: Enforces uniqueness
- **Full-text Index**: For search
- **Spatial Index**: For geo-spatial data

#### d. By Structure Internally
- **B-tree** (standard), **Hash**, **Bitmap**, **XML**

### 4.2 Index Rules and Facts
- Only **1 Clustered Index** per table; auto-created with PK unless overridden
- Without clustered index → **Heap Table** (unordered data)
- Clustered Index = Faster lookup (**O(log N)**); Heap = **O(N)**
- Composite indexes supported

---

## 5. Heap Storage vs Clustered
- **Heap Table**: Unordered data, no clustering = slow lookups
- **Clustered Table**: Sorted by clustered index
- **Tip**: Prefer clustered index on large tables with frequent queries

---

## 6. Locking Mechanism
- Types:
  - Row-level, Page-level, Table-level
- Modes:
  - Shared (`S`), Exclusive (`X`), Intent (`IS`, `IX`), Update (`U`)
- Concepts:
  - **Deadlock**, **Blocking**, **Lock Escalation**

---

## 7. Write-Ahead Logging (WAL)
- All changes written to WAL before disk
- Ensures **Durability** (ACID)
- Powers crash recovery, replication, PITR

---

## 8. Recovery & Checkpoint
- **Crash Recovery**:
  - **Redo** committed
  - **Undo** partial/uncommitted
- **Checkpoint**: Flushes in-memory changes to disk

---

## 9. Point-in-Time Recovery (PITR)
- Uses base **snapshot + WAL**
- Recovers to any specific timestamp
- Used for:
  - Accidental deletes
  - Data corruption
  - Logical mistakes

---

## 10. Replication & Snapshots
- **Types**:
  - Transactional, Merge, Snapshot Replication
- **Snapshot**: Read-only frozen copy for reporting/backups

---

## 11. Partitioning & Clustering

### 11.1 Table Partitioning
- Break large table logically
- Types:
  - Range, List, Hash, Composite

### 11.2 Table Clustering
- Physical layout follows clustered index
- Only one clustered index/table
- Clustering improves scan performance

---

## 12. Scaling SQL Systems

### 12.1 Vertical Scaling
- Add CPU, RAM, SSD
- Simple but limited

### 12.2 Horizontal Scaling
- **Sharding**: Range/hash partitioned tables
- **Replication**: Read replicas for load balancing
- **Distributed SQL**: CockroachDB, Citus

---

## 13. SQL Limitations
- Max row size (~8KB), column count limits (~1,600)
- No native sharding (manual)
- Triggers = hard to debug
- Complex locking model
- Index bloat/maintenance
- Cross-shard JOINs not scalable
- Heap tables slow for read-heavy workloads

---

## 14. Use Cases

### ✅ Best
- Relational OLTP
- Structured data
- Auditable, transactional data
- Well-defined schema

### ❌ Worst
- Schema-less data (NoSQL better)
- High-ingestion logs/streams
- Time-series (use TSDBs)
- Multi-region low-latency writes

---
