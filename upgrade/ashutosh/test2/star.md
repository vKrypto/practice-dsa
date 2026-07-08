# System Optimization - Interview Notes

## 1. Async/Concurrency Optimization

### HTTP Async Migration

- **S**: `requests` lib blocking at 500K concurrent requests
- **A**: Migrated to `aiohttp` with request batching + rate limiting
- **R**: 92s → 30s avg execution, 500K concurrent requests
- API Service Optimization

- **S**: API/proxy bottleneck: p95=2s, p99=30-40s at 5K concurrent
- **A**:Optimized mutex strategy (reduced contention)

  Dragonfly distributed locks (horizontal scaling)

  In-memory log buffering (async flush pattern)
- **R**: p95=8-9ms at 20K concurrent, 18s → 12s execution

---

## 2. Caching & Data Optimization

### Redis Compression & Cache Strategy

- **S**: Redis I/O bottleneck with 150MB market data, 20K concurrent
- **A**:
  - Conditional fetch (removed market data for balance-only jobs)
  - Gzip compression (150MB → 13MB, 90% I/O reduction)
  - File-based secondary cache with container-level invalidation
- **R**: 11s saved per job, 30s → 18s execution

---

## 3. Message Queue Optimization

### Kafka Producer

- **S**: 1s to publish 20K messages
- **A**:
  - Batch publish with partition affinity (vs round-robin)
  - Scaled to 60 partitions/consumers per stack
  - DB query → Stored Procedure + pre-cache in peak hours (p99: 600ms → 50ms)
  - Multi-producer horizontal scaling
  - Container placement optimization (subnet proximity)
- **R**: 150-200ms publish time, 12s → 11s execution

### Kafka Consumer

- **S**: >2s to consume 20K messages
- **A**:
  - Cilium eBPF mode for DNS optimization
  - Scaled to 60 consumers
- **R**: 200-250ms consume time, 11s → 9-10s execution

---

## 4. Observability & Monitoring

### Full-Stack Observability

- **S**: Production blackbox, no visibility
- **A**:
  - Graylog: Enhanced logging with multi-param dashboards (request tracing)
  - Grafana: Node/container/console metrics & logs
  - Kibana: Heartbeat/health monitoring per component
- **R**: Complete visibility → identified/fixed multiple unhandled exceptions, enabled further optimizations

---

## 5. System Reliability & Testing

### CI/CD & Quality Gates

- **S**: Unexpected job failures, frequent emergency releases
- **A**:
  - Automated test pipelines
  - Sandbox testing (provided + custom) for exception scenarios
  - SonarQube + pytest results in PR gates
  - Template setup for 2 exchanges, team replicated for others
- **R**: 90% reduction in emergency releases, smooth deployments

---

## 6. Infrastructure & Network Optimization

### TCP Window Tuning

- **S**: 500K concurrent requests causing exchange bottlenecks
- **A**: Monitored TTFB/connection timing (Grafana/Graylog), increased TCP recvWindow
- **R**: Eliminated recvWindow expiry, improved p99, most jobs <9s

### Datacenter Migration

- **S**: 80% Binance traffic, US datacenter requiring Asia proxy (250ms latency)
- **A**: Metrics-driven proposal to NSD team, migrated to India datacenter
- **R**: Reduced RTO/ProxyError, 10s → 7s execution

### Node Isolation

- **S**: AccountAPI sharing node with datafetch (I/O latency > CPU scheduling time)
- **A**: Dedicated 2-node cluster for AccountAPI
- **R**: 30% performance improvement (eliminated CPU scheduling bottleneck)

---

## 7. Runtime & Performance

### Python Upgrade

- **S**: CPU-bound processing bottleneck
- **A**: Migrated Python 3.9.5 → 3.13.2
- **R**: 40% faster CPU processing, 7s → 5-6s execution

### GIL Bypass

- **S**: GIL limiting CPU to 10-12% on long-running jobs (trades/orders/txns)
- **A**: Multi-thread/process failed → subprocess isolation
- **R**: CPU utilization 1200-1400%, 2x faster execution

---

## 8. Resource Management

### Memory Leak Resolution

- **S**: RAM growth 400GB → 1.5TB in 4-5 days
- **A**:
  - Manual object dereferencing
  - Core dump analysis (gcore): SSLContext not properly GC'd → added sleep for cleanup
  - Periodic C-based + Python GC
- **R**: Memory stabilized at 400GB → 450GB

### Kubernetes Node Optimization

- **S**: Subprocess solution (20K Python forks) → K8s nodes NotReady, cascade failure
- **A**:
  - CPU affinity: 80% cores for workload, 20% reserved for K8s
  - Jitter for process fork distribution (context switch: 2500ms → 200ms)
  - Node tuning: ulimit, tcp_max_syn_backlog, net.ipv4 params
- **R**: Context switch reduced, CPU 500-600%, stable nodes

---

## 9. Error Handling & Timeouts

### Long-Running Job Termination

- **S**: Middleware timeout (3hr) returned response but function continued (Python default)
- **A**:
  - Exception handling in common paths
  - Middleware using ctypes to inject exception into thread call stack
- **R**: Proper execution termination on timeout

---

## Optimization Summary (Order-Wise)

| #  | Section                               | Optimization                       | Job Execution Time Result                |
| -- | ------------------------------------- | ---------------------------------- | ---------------------------------------- |
| 1  | Async/Concurrency Optimization        | HTTP Async Migration               | 92s → 30s avg execution                 |
| 2  | Caching & Data Optimization           | Redis Compression & Cache Strategy | 30s → 18s execution (11s saved per job) |
| 3  | Async/Concurrency Optimization        | API Service Optimization           | 18s → 12s execution                     |
| 4  | Message Queue Optimization            | Kafka Producer                     | 12s → 11s execution                     |
| 5  | Message Queue Optimization            | Kafka Consumer                     | 11s → 9-10s execution                   |
| 6  | Infrastructure & Network Optimization | Datacenter Migration               | 10s → 7s execution                      |
| 7  | Infrastructure & Network Optimization | TCP Window Tuning                  | Most jobs <9s execution                  |
| 8  | Runtime & Performance                 | Python Upgrade                     | 7s → 5-6s execution                     |
| 9  | Runtime & Performance                 | GIL Bypass                         | 2x faster execution                      |
| 10 | Infrastructure & Network Optimization | Node Isolation                     | 30% performance improvement              |

---

## Summary Metrics

| Metric              | Before       | After         | Improvement               |
| ------------------- | ------------ | ------------- | ------------------------- |
| Avg Job Execution   | 92s          | 5-6s          | **93% reduction**   |
| Concurrent Requests | 5K           | 500K          | **100x scale**      |
| API p95 Latency     | 2s           | 8-9ms         | **99.5% reduction** |
| API p99 Latency     | 30-40s       | <9s           | **~75% reduction**  |
| Redis I/O           | 150MB        | 13MB          | **90% reduction**   |
| Memory Leak         | 400GB→1.5TB | 400GB→450GB  | **Stabilized**      |
| Emergency Releases  | High         | 90% reduction | **Reliability**     |
