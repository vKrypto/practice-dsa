# 📊 MongoDB vs DynamoDB (Cluster Version)

---

## ✅ Detailed Comparison Table

| Feature / Aspect          | **MongoDB (Clustered/Atlas)**                                                                 | **DynamoDB (AWS Managed)**                                                               |
|---------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Type**                  | NoSQL Document Store                                                                         | NoSQL Key-Value & Document Store                                                         |
| **Query Type**                  | More Like JS functions `db.users.find({}, { name: 1, email: 1, _id: 0 })` | More like SQL queries `SELECT "name", "email" FROM "users"`|
|**Data Model**            | BSON (Binary JSON), flexible schema                                                          | JSON-like documents, schema-less                                                         |
| **Primary Key**           | `_id` (overridable), per-document                                                            | Partition Key (required) + optional Sort Key                                             |
| **Indexing**              | Single, Compound, TTL, Text, Geo, Wildcard, Partial                                          | Primary Index, GSI, LSI, TTL                                                             |
| **Query Language**        | MongoDB Query Language (MQL)                                                                 | Key-based access + limited PartiQL                                                       |
| **Joins**                 | Supported via `$lookup`, `$graphLookup`                                                      | ❌ No joins (must denormalize or join in app logic)                                      |
| **Aggregation**           | Full-featured aggregation pipeline                                                           | ❌ No pipeline; only basic filtering/PartiQL + Streams/Lambda                            |
| **Transactions**          | Multi-document ACID (even across shards)                                                     | Supported (same partition strongly consistent; cross-partition = limited)               |
| **Scaling**               | Manual or Auto-sharding (via Atlas), configurable shard keys                                 | Auto-scaled based on partition keys & throughput units                                   |
| **Consistency**           | Tunable: eventual, majority, linearizable, causal                                            | Tunable: eventual by default, strong optional                                            |
| **Availability**          | High via Replica Sets; Multi-region via Atlas                                                | High via Multi-AZ & Global Tables                                                        |
| **Replication**           | Asynchronous + Failover (Replica Set); Global Clusters in Atlas                              | Sync across AZs; Global Tables support async cross-region replication                   |
| **Partitioning Strategy** | Sharded clusters with custom shard key                                                       | Automatic partitioning using hashed PK                                                  |
| **Backup & Restore**      | Continuous + On-demand via Atlas                                                             | PITR + On-demand snapshots                                                               |
| **Hosting & Management**  | Atlas, Kubernetes Operator, or Self-hosted                                                   | Fully managed by AWS                                                                    |
| **Pricing Model**         | Based on vCPU, RAM, storage, ops/sec, backups                                                | Pay-per-RCU/WCU, storage, backup                                                        |
| **TTL Support**           | Yes (indexed TTL per document)                                                              | Yes (attribute-based expiration)                                                         |
| **Access Control**        | Role-based + field-level + network rules                                                     | IAM-based + fine-grained access via AWS Policies                                         |
| **Triggers / Change Streams** | Change Streams (real-time event handling)                                               | DynamoDB Streams + Lambda                                                               |
| **Use Case Fit**          | Analytics-heavy apps, flexible-schema workloads, real-time dashboards, mobile apps          | Massive scale, serverless, IoT, game state mgmt, real-time low-latency use cases        |

---

## ✅ Similarities

| Feature               | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **NoSQL**            | Both are non-relational and schema-flexible                                  |
| **Document Support** | JSON-like document storage                                                    |
| **High Availability**| Built-in HA support                                                           |
| **Horizontal Scale** | Designed for distributed workloads                                            |
| **TTL Support**      | Native TTL expiration supported                                               |
| **Transactions**     | Both support ACID (with limitations)                                          |
| **Managed Option**   | Fully managed options available (Atlas, DynamoDB)                             |
| **Multi-region**     | Both support global clusters/tables                                           |

