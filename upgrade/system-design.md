# 📘 System Design Topics (90% Coverage)

## 1. API Gateways & Edge

-   Examples: **Netflix Zuul/APIGW**, **Kong/Nginx fronting
    microservices**\
-   *Hint:* routing, auth at edge, rate-limiting, circuit breakers,
    canary/blue-green, observability at L7.

## 2. Load Balancing & Traffic Management

-   Examples: **HAProxy + Nginx tier**, **Envoy + Service Mesh
    (Istio/Linkerd)**\
-   *Hint:* L4 vs L7, sticky sessions, health checks, outlier ejection,
    consistent hashing.

## 3. Caching Layers

-   Examples: **Redis/Memcached sidecar**, **CDN (CloudFront/Akamai) +
    origin cache**\
-   *Hint:* cache aside vs write-through vs write-back, TTL/SLAs,
    stampede protection, key design, invalidation.

## 4. Primary Datastores (OLTP)

-   Examples: **PostgreSQL (single + read replicas)**, **MySQL +
    ProxySQL**\
-   *Hint:* schema design, secondary indexes, transactions, connection
    pooling, hot rows, read/write split.

## 5. Sharding & Replication

-   Examples: **Twitter MySQL shards**, **MongoDB sharded cluster**\
-   *Hint:* shard keys, resharding, rebalancing, cross-shard queries,
    replication lag, failover.

## 6. Search

-   Examples: **Elasticsearch product search**, **OpenSearch log
    search**\
-   *Hint:* inverted index, analyzers, relevance/filters, write
    pipeline, hot-warm-cold tiers.

## 7. Async Processing & Queues

-   Examples: **RabbitMQ for tasks**, **Kafka for event streams**\
-   *Hint:* at-least-once vs exactly-once, ordering keys, consumer
    groups, DLQs, idempotency.

## 8. Workflow/Orchestration

-   Examples: **Temporal/Cadence**, **Airflow for ETL DAGs**\
-   *Hint:* retries/backoff, saga patterns, timeouts, compensation,
    state visibility.

## 9. File/Object Storage

-   Examples: **S3 + presigned URLs**, **GCS + Cloud CDN**\
-   *Hint:* multipart upload, lifecycle/IA tiers, integrity (MD5/ETag),
    directory listings.

## 10. Real-Time & Pub/Sub

-   Examples: **WebSocket chat (Slack-like)**, **SSE live scores**\
-   *Hint:* fan-out, backpressure, presence, connection scaling,
    fallbacks (long-poll).

## 11. Notifications

-   Examples: **Email + SMS (SES/Twilio)**, **Push (FCM/APNs)**\
-   *Hint:* templates, user prefs, throttling, retries, deliverability,
    dedupe.

## 12. Analytics/OLAP

-   Examples: **ClickHouse event analytics**, **BigQuery batch
    dashboards**\
-   *Hint:* columnar vs row, partitioning, late-arriving data,
    materialized views, cost controls.

## 13. Recommendation/Search Pipelines

-   Examples: **Embedding-based semantic search**, **Graph-based "People
    You May Know"**\
-   *Hint:* offline vs online features, feature store, cold-start, A/B
    testing.

## 14. CDN & Edge Compute

-   Examples: **CloudFront + Lambda@Edge**, **Fastly VCL**\
-   *Hint:* cache keys, invalidations, image resize at edge, geo
    routing.

## 15. AuthN/AuthZ & Identity

-   Examples: **OAuth2/OIDC with Keycloak/Auth0**, **RBAC/ABAC in
    services**\
-   *Hint:* token lifetimes, refresh flows, JTI/jti-based revocation,
    mTLS/service-to-service.

## 16. Rate Limiting & Abuse Prevention

-   Examples: **Token bucket in Redis**, **Cloudflare/WAF rules**\
-   *Hint:* global vs per-route limits, sliding window, distributed
    counters, burst vs sustained, shadow mode.
