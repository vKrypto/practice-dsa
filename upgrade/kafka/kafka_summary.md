# 🔥 Kafka Summary – Core Concepts, Responsibilities & Delivery Guarantees

---

## 🧱 Broker

- Kafka server that **stores messages** and manages **partitions** and **replication**.
- **Responsibilities**:
  - Accept data from producers.
  - Store data in partition logs.
  - Serve data to consumers.
  - Partition leadership election & failover.
  - Handle **replication**, **retention**, **compaction**, **metrics**, and **ACLs**.
  - Acts as **Consumer Group Coordinator** & **Transaction Coordinator**.

**Important Broker Settings**:
```properties
log.retention.hours=168
num.partitions=3
default.replication.factor=3
```

---

## ✉️ Producer

- Sends data to Kafka topics.
- **Responsibilities**:
  - Serialize and send messages.
  - Choose partition (based on key or round-robin).
  - Batch & compress messages.
  - Handle retries and delivery guarantees.

### ✅ At-Least-Once Producer Settings
```properties
acks=all
retries=5
linger.ms=5
```

### 🛡️ Exactly-Once Producer Settings
```properties
acks=all
enable.idempotence=true
transactional.id=my-txn-id
max.in.flight.requests.per.connection=1
```

---

## 📥 Consumer

- Pulls messages from Kafka topics.
- **Responsibilities**:
  - Fetch messages from partitions.
  - Deserialize and process records.
  - Manage offsets (auto or manual).
  - Handle group coordination and rebalancing.

### ✅ At-Least-Once Consumer Strategy
- Commit **after** processing.
- Use `commitSync()` or `commitAsync()`.

### 🛡️ Exactly-Once Consumer Strategy (End-to-End)
- Use `isolation.level=read_committed`
- Use **transactional producer**
- Call `sendOffsetsToTransaction(offsets, groupId)` before `commitTransaction()`

---

## 🔁 Offset

- Uniquely identifies a message in a partition.
- Used for tracking how far a consumer has read.

---

## 🧾 Partition

- A topic is split into multiple partitions.
- Ensures scalability and parallelism.
- Ordering is guaranteed **only within** a single partition.

---

## 📦 Delivery Guarantees

| Mode             | Duplicates Possible? | Data Loss Possible? | Requires Idempotence / Txn? |
|------------------|----------------------|----------------------|-----------------------------|
| At-most-once     | ❌ No                 | ✅ Yes               | No                          |
| At-least-once    | ✅ Yes                | ❌ No                | Optional                    |
| Exactly-once     | ❌ No                 | ❌ No                | ✅ Yes                      |