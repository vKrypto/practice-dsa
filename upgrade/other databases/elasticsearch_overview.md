# 📘 Elasticsearch Overview

- **Type**: Distributed, NoSQL, document-based search engine built on Lucene  
- **Data Format**: JSON documents  
- **Storage Model**: Index → Shards → Lucene Segments  
- **Primary Use Cases**: Full-text search, log analytics, real-time dashboards, vector search

---

## ⚙️ Architecture Components

- **Cluster**: Collection of nodes
- **Node**: A single server in the cluster (can be master, data, ingest, coordinating)
- **Index**: Logical namespace for documents (like a database)
- **Shard**: Physical unit of storage (primary & replicas)
- **Segment**: Lucene-level immutable files created per shard

---

## 🔍 Read (Search) Request Flow

1. Client sends a request to **any node** → it becomes the **coordinating node**.
2. Coordinating node:
   - Checks **cluster state** to locate shards.
   - Sends the query to **one active copy** (primary or replica) of **each shard**.
3. **Query Phase**:
   - Each shard executes the query locally and returns metadata (doc IDs, scores).
4. **Merge Phase**:
   - Coordinating node merges all shard results and performs **global sorting**.
5. **Fetch Phase**:
   - Requests full documents for top N hits from respective shards.
6. Final result is sent back to the client.

---

## 📝 Write Flow (Indexing)

1. Document → Hashed to a **specific primary shard**.
2. Coordinating node forwards write to that **primary shard**.
3. Primary:
   - Writes to **translog** + in-memory Lucene buffer.
   - Forwards the operation to **replica shards**.
4. Once **acknowledged by required shards** (based on `wait_for_active_shards`), response is sent back.

---

## 💡 Key Features

- ✅ Full-text search with scoring & relevance
- ✅ Real-time indexing & querying
- ✅ Powerful **aggregations**
- ✅ Built-in **vector similarity** (ANN)
- ✅ **Geo queries**
- ✅ RESTful APIs & Kibana for UI
- ✅ Scalable horizontally
- ✅ Plugin ecosystem (alerting, security, etc.)

---

## 🔐 Durability & Consistency

- **Translog** + **Lucene segments** ensure durability
- `translog.durability = request` → fsyncs per write
- Uses **eventual consistency**
- **Tunable consistency** via:
  - `wait_for_active_shards`
  - Replica acknowledgment settings

---

## 🔄 Concurrency & Isolation

- No native ACID for multi-docs
- **Document-level atomicity** only
- No **true isolation**; risk of race conditions
- Supports **manual OCC** using:
  - `_version`
  - `_seq_no` + `_primary_term`
- No native PCC — must be implemented externally (e.g., via distributed locks)

---

## 🎯 Ideal Use Cases

- E-commerce product search
- Log & metric analytics (ELK stack)
- Autocomplete, suggestion engines
- Recommendation systems
- Real-time dashboards
- Geo-based search (e.g., food delivery)
- Vector search (semantic, image similarity)

---

## 🚫 Limitations

- ❌ No full ACID (multi-doc writes not atomic)
- ❌ No native transaction/locking
- ❌ RAM hungry (Lucene + aggregations)
- ❌ Deep pagination is expensive (`from` + `size`)
- ❌ Write-heavy workloads can strain IO
- ❌ Large number of small indices = cluster state bloat
- ❌ JVM tuning can be tricky

---

## 🧠 Extras

- **Noise handling**: You control it via analyzers (e.g., stop words, stemmers)
- **ANN support**: k-NN, HNSW for vector similarity
- **NoSQL**: Yes — schema-less document store
- **Isolation**: Only per-document
- **Not SQLite**: Elasticsearch ≠ relational; it's distributed NoSQL