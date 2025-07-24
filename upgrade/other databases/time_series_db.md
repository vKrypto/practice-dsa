## 🧠 InfluxDB vs MongoDB vs PostgreSQL (TimescaleDB) — Time-Series Short Notes

---

### 🎯 Summary (One-liners)

- **InfluxDB**: Purpose-built time-series DB with blazing write/read speed and compression.
- **MongoDB**: General-purpose NoSQL with decent TS support since v5+, but heavier.
- **TimescaleDB (PostgreSQL)**: Best for relational + TS hybrid use cases with full ACID and SQL.

---

### 📊 InfluxDB

- **Storage**: TSM (TS Merge Tree), block-based, compression built-in.
- **Data types**: timestamp, float, int, bool, string, tags (indexed).
- **Query**: InfluxQL (SQL-like), Flux (functional).
- **ACID**: Only durability; lacks full transactional guarantees.
- **Use case**: High-ingestion TS workloads, low-disk footprint.
- **Performance**:
  - ~1.9x higher write throughput than MongoDB
  - ~5x faster query speed than MongoDB
  - ~7.3x lower disk usage (160 MB vs 1178 MB for 24h data)

---

### 🗂️ MongoDB (TS Collections)

- **Storage**: BSON with auto-bucketing for TS collections.
- **Data types**: Full BSON support (flexible schema).
- **Query**: Aggregation pipeline, limited TS optimization.
- **ACID**: Document-level; multi-doc via transactions.
- **Use case**: Semi-structured data + TS in same workload.
- **Performance**:
  - Slower write/query compared to InfluxDB
  - 7x more disk used for same TS data

---

### 🐃 PostgreSQL + TimescaleDB

- **Storage**: Hypertables with auto-chunking; uses relational tables.
- **Data types**: Full SQL support, TS extensions like `time_bucket()`.
- **Query**: Native SQL, joins, time-aware indexes.
- **ACID**: Full transactional guarantees.
- **Use case**: Relational + TS analysis, analytics workloads.
- **Performance**:
  - ~1.6x faster than InfluxDB on aggregations (varies by query)
  - Efficient storage with compression options

---

### 🔄 Feature Comparison Table

| Feature                | InfluxDB              | MongoDB Time-Series         | TimescaleDB (PostgreSQL)   |
|------------------------|------------------------|------------------------------|-----------------------------|
| Data model             | TS-first NoSQL         | Document + TS                | Relational + TS             |
| Schema flexibility     | Moderate (typed)       | High (BSON)                  | Strict                      |
| Write throughput       | 1.0x (baseline)         | ~0.5x                        | Comparable (schema-based)   |
| Query speed            | 1.0x                   | ~0.2x                        | ~1.6x on agg queries        |
| Disk usage             | 1.0x                   | ~7.3x more                   | 1.0x (with compression)     |
| ACID level             | Durability only        | Document-level               | Full ACID                   |
| Query language         | InfluxQL / Flux        | Aggregation Pipeline         | Standard SQL                |
| Best for               | Real-time TS dashboards| Mixed semi-structured + TS   | TS + business logic (SQL)   |

---

### ✨ Recommendations

- ✅ Use **InfluxDB** for real-time, high-throughput, storage-efficient TS workloads.
- ✅ Choose **MongoDB** if already invested in BSON + want TS without another DB.
- ✅ Pick **TimescaleDB** for deep analytics, joins, or combining TS with business data.

---

