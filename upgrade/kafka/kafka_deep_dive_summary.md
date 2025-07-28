# 🦾 Kafka Deep-Dive: Comprehensive Summary

---

## 🏗️ Core Components

- **Broker**
  - Stores messages, manages partitions and replication.
  - Handles client requests (produce/consume), partition leadership, metrics, and log retention.
  - Acts as consumer group & transaction coordinator.

- **Producer**
  - Serializes and sends messages to topics/partitions.
  - Handles batching, compression, retries, and partition assignment.
  - Can enable idempotence and transactions for stronger delivery guarantees.

- **Consumer**
  - Reads messages from broker partitions.
  - Manages offsets (auto/manual), joins consumer groups, balances partition assignment.
  - Can replay messages by seeking offsets.

---

## 🌐 Kafka Ecosystem Components

| Component                  | Role/Responsibility                                         | Use Cases                                   |
|----------------------------|-------------------------------------------------------------|---------------------------------------------|
| ZooKeeper *(legacy)*       | Cluster coordination, leader election                       | Cluster metadata & controller (pre KRaft)   |
| Kafka Connect              | Source/sink integration with external systems               | DB ↔ Kafka, S3 ↔ Kafka                      |
| Kafka Streams              | Library for client-side, stateful stream processing         | Real-time analytics, joins, aggregates      |
| ksqlDB                     | Streaming SQL engine on Kafka                              | Live queries, transformation, ad-hoc ETL    |
| Schema Registry            | Schema validation for Avro/Protobuf/JSON                   | Data governance, contract enforcement       |
| REST Proxy                 | HTTP API for Kafka produce/consume/admin                    | Integration with non-Kafka apps/services    |
| Confluent Control Center   | GUI for monitoring, management, alerting                    | Observability, SLA tracking                 |
| Replicator / MirrorMaker2  | Cross-cluster replication                                   | DR, geo-replication, migration              |
| Self-Balancing Clusters    | Automatic partition rebalancing                             | Scaling, zero-touch ops                     |
| Tiered Storage             | Offloads old segments to object storage                     | Infinite retention, cost savings            |
| RBAC & Audit Logs          | Access control, audit trail                                 | Security, compliance                        |

---

## 🔑 Delivery Guarantees & Required Settings

| Guarantee         | Producer Settings                                   | Consumer Settings              | Broker Role                                   | Edge Cases/Notes                    |
|-------------------|-----------------------------------------------------|-------------------------------|-----------------------------------------------|--------------------------------------|
| **At-least-once** | `acks=all`, `retries>0`                            | Manual offset commit after processing | Persists messages, may deliver duplicates   | Duplicates if crash after processing before commit |
| **Exactly-once**  | `acks=all`, `enable.idempotence=true`, `transactional.id`, `max.in.flight.requests.per.connection=1` | Use `isolation.level=read_committed`, commit offsets inside transaction | Transaction coordinator ensures atomic write & offset commit | External sinks still need idempotency/deduplication logic |

---

## 🔁 Replay & Offset Management

- Kafka **retains messages** as per topic retention policy, regardless of consumption.
- Consumers can **seek** to any offset (replay, backfill, audits, bug fixes).
- Consumer group offsets can be reset via:
  - `seek(partition, offset)`
  - `seekToBeginning()` / `seekToEnd()`
  - Using a new group id (`auto.offset.reset`)
  - Kafka CLI tools: `kafka-consumer-groups --reset-offsets ...`

---

## 🛡️ Deduplication & Idempotency

- EOS within Kafka: No duplicates unless you opt out of idempotence or transactions.
- EOS to external systems (DB, S3, etc): **Dedup logic required**.
  - Use Kafka offset or message UUID as a dedup key.
  - Enforce idempotent upserts or atomic transactions in external sinks.
- No mutex/locks—use DB primary key or unique constraint.

---

## ⚡ Other Advanced Topics

- **Rebalance**: Consumers may be reassigned partitions; handle with care to avoid duplicate or missed processing.
- **Consumer Groups**: Each partition is assigned to one consumer per group; more consumers than partitions = idle consumers.
- **Metrics**: Brokers expose health, lag, throughput, consumer group progress, etc.
- **Leader Election**: ZK/KRaft handles controller election, failover.
- **Transactions**: Required for end-to-end exactly-once; commits both data and offset atomically.
- **Tiered Storage**: Offloads older logs transparently, infinite topic retention possible.
- **Security**: RBAC, SSL, SASL, audit logs for compliance.

---

## 🚦 Typical Troubleshooting/Edge Cases

- **Consumer crash after processing, before offset commit**: Message re-processed by new consumer (duplicate unless deduped).
- **Producer retry with no idempotence**: Duplicate messages on broker.
- **Offset commit failure or group rebalance**: Lost or duplicated processing.
- **Cross-cluster/legacy sink**: EOS may break; always validate downstream.

---

## 🧾 Sample Settings for At-Least-Once and Exactly-Once

```properties
# At-Least-Once Producer
acks=all
retries=5

# At-Least-Once Consumer
enable.auto.commit=false
# commitSync() after successful processing

# Exactly-Once Producer
acks=all
enable.idempotence=true
transactional.id=my-txn-id
max.in.flight.requests.per.connection=1

# Exactly-Once Consumer
isolation.level=read_committed
# Use sendOffsetsToTransaction before commitTransaction
```

---

# 💡 TL;DR
- **Producer** = push data, batch, compress, (optional) enable transactions.
- **Broker** = store, replicate, coordinate, retain, expose metrics, manage offsets & transactions.
- **Consumer** = pull, process, commit offset, join group, handle replay/seek, dedup if needed.
- **Edge Cases** always lurk at delivery, offset commit, and cross-system boundaries—**plan for them**.