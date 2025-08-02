# 📘 MongoDB: Deep Dive Notes (Cluster-Level, Staff-Level)

---

## 🔧 Basics

- **Type**: NoSQL Document Database  
- **Storage Model**: BSON (Binary JSON)  
- **Schema**: Flexible (schemaless)  
- **Core Components**:  
  - **Database > Collections > Documents**  
  - **Replica Sets** for HA  
  - **Sharding** for scalability  

---

## ⚙️ Architecture (Cluster Mode)

- **Replica Set**: 1 primary, N secondaries  
  - Auto-failover supported  
- **Sharded Cluster**:
  - Uses **mongos router**
  - **Shards** can be replica sets
  - Shard key is critical — bad design leads to imbalance or scatter-gather  
- **mongod**: DB server process  
- **mongos**: Query router for sharded setup  

---

## 🚀 Best Use Cases

| Use Case             | Why                                  |
|----------------------|---------------------------------------|
| Product catalog      | Flexible schema, deep nesting         |
| Real-time analytics  | Fast reads/writes                     |
| IoT data ingestion   | High write throughput                 |
| Event logging        | Append-only, TTL indexes              |
| E-commerce user carts| Atomic updates on single document     |

---

## 🧨 Worst Use Cases

| Use Case                   | Problem                                    |
|----------------------------|--------------------------------------------|
| Multi-doc transactions     | Weak consistency, high latency             |
| Complex joins              | Not a relational DB                        |
| Write-heavy w/ bad keys    | Shard imbalance                            |
| Heavy ACID needs           | Use RDBMS instead                          |

---

## 🧠 Internals & Considerations

### 💾 Storage & Indexing

- Uses **WiredTiger** by default  
- Index types: compound, TTL, partial, text, geospatial  
- Avoid **unbounded arrays**  
- Index size should ideally fit in RAM  

### ⚠️ Edge Cases

- Update non-shard key in sharded cluster: allowed only on single-shard target  
- Large documents (>16MB): Not allowed — use GridFS  
- Change streams: Only for replica sets  
- Unacknowledged writes: Risky unless `writeConcern` is set  
- No swap-based eviction — OOM kills possible  
- Reads from secondary can be stale unless `readConcern: majority` used  

---

## ⚖️ MongoDB vs DynamoDB

| Feature         | MongoDB (Cluster)       | DynamoDB                          |
|----------------|--------------------------|-----------------------------------|
| Hosting         | Self-hosted or Atlas     | Fully managed (AWS)               |
| Schema          | Flexible                 | Flexible                          |
| Consistency     | Eventual (tweakable)     | Eventual (can be strong)          |
| Availability    | High (replica sets)      | High (Multi-AZ/global tables)     |
| Querying        | Rich aggregation         | Limited (GSIs, LSIs)              |
| Scalability     | Manual (sharding)        | Auto                              |
| Cost Model      | Compute + Storage        | Pay-per-request                   |
| Backups         | Manual / Atlas           | Automated                         |
| Partitioning    | Manual shard key         | Automatic partition key           |

---

## 📈 Scaling MongoDB

### 📌 Things to Watch

- **Shard key**: high cardinality, avoid hotspot keys like timestamps  
- **Chunk balancing**: use `getShardDistribution()`  
- **Index pressure**: each index uses memory  
- **Connection limits**: configure mongod/mongos limits  

### 📈 Tips

- Compound index order matters  
- Use `$match`, `$project` early in pipeline  
- Avoid scatter-gather queries  
- Use replica sets even for dev  
- Prefer **MongoDB Atlas** for auto-scaling & performance tools  

---

## 🛡️ Availability / Consistency / Partition Tolerance (CAP)

| Property       | MongoDB                     |
|----------------|-----------------------------|
| Availability   | High (Replica Set)          |
| Consistency    | Eventual (tweakable)        |
| Partition      | Tolerant via replication    |

---

## 🧪 Tuning & Pitfalls

- Monitor **oplog size**  
- Avoid long transactions  
- Use retryable writes & idempotent operations  
- `$in` on large arrays = CPU spike  
- Multi-region → use **Atlas Global Clusters**  

---

## 📋 Summary

- MongoDB = **flexibility + speed**, but scaling and consistency need care  
- Replica set vs Sharded cluster — choose per access pattern  
- DynamoDB wins for **fully managed + auto scaling** setups  
- MongoDB offers richer query interface & dev experience  

---
