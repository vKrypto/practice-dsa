#  System Design Topics + Real Interview Questions

Below is the lean and mean list—each category has **2 commonly asked interview questions**, based on 2024–25 prep sources like I GOT AN OFFER, GeeksforGeeks, UFL CareerHub, and Reddit.

---

## 1. API Gateways & Edge
- How would you design an API gateway that supports **multi-tenant authentication**, **rate limiting per tenant**, and **zero-downtime deployments**?
- What’s the difference between an **API Gateway** and a **Load Balancer**, and when would you use each? :contentReference[oaicite:2]{index=2}

---

## 2. Load Balancing & Traffic Management
- Explain how you’d design a system where **sticky sessions** are needed (e.g., shopping cart) but must support **auto-scaling**.
- What’s the difference between **Reverse Proxy** and **Forward Proxy**, and how does that apply to load balancing? :contentReference[oaicite:3]{index=3}

---

## 3. Caching Layers
- When would you choose **write-through vs write-back vs cache-aside** in a high-traffic API?
- How would you design a **distributed web cache** that handles high throughput and avoids cache stampede? :contentReference[oaicite:4]{index=4}

---

## 4. Primary Datastores (OLTP)
- How do you design a **Postgres-backed inventory system** that avoids **lost updates** under high concurrency?
- What’s the difference between **horizontal scaling** and **vertical scaling** in database design? :contentReference[oaicite:5]{index=5}

---

## 5. Sharding & Replication
- You’re designing a social graph database—how do you choose a **shard key** to avoid hotspots and enable efficient friend-of-friend queries?
- Design a **distributed key-value store**—how do you handle sharding and replication? :contentReference[oaicite:6]{index=6}

---

## 6. Search
- For an **Elasticsearch product search**, how do you handle **reindexing** when the schema changes without downtime?
- How would you design an **autocomplete (typeahead)** feature for a search engine? :contentReference[oaicite:7]{index=7}

---

## 7. Async Processing & Queues
- In a **payment system**, how do you guarantee **idempotency** with Kafka when consumers might process the same message twice?
- Design a **distributed queue** (like RabbitMQ/Kafka)—how would you ensure ordering, retries, and scaling? :contentReference[oaicite:8]{index=8}

---

## 8. Workflow/Orchestration
- Design a workflow engine for **order processing** (payment → inventory → shipment). How do you ensure **eventual consistency** if a step fails?
- How would you implement retries and compensation in a saga-style orchestration for long-lived transactions? *(composite of known patterns—no direct web citation)*

---

## 9. File/Object Storage
- How would you design a system for **uploading large (5 GB+) files** to object storage (e.g., S3) with **resume**, **integrity**, and **secure client uploads**?
- Design a **file-sharing system** (like Dropbox/Google Drive)—how would you ensure consistency and scalability? :contentReference[oaicite:9]{index=9}

---

## 10. Real-Time & Pub/Sub
- How would you design a **real-time chat system** (like Slack) that guarantees **message ordering per channel**?
- How would you build a **live comment stream** (like Facebook Live commenting) with backpressure and high throughput? :contentReference[oaicite:10]{index=10}

---

## 11. Notifications
- Design a **notification system** that supports email, SMS, and push, including **user preference management** and **deduplication**.
- How would you design a **push notification** system that scales and handles retries? *(industry standard—no direct citation)*

---

## 12. Analytics/OLAP
- How would you build a **real-time dashboard** showing sales per region with **<1-minute latency**, even when data arrives late or out-of-order?
- Design a **metrics logging and aggregation system** for thousands of servers (like Datadog/Prometheus). :contentReference[oaicite:11]{index=11}

---

## 13. Recommendation/Search Pipelines
- How do you design a **personalized recommendation system** that serves results in **<50 ms**, while retraining occurs daily?
- How would you design a system to get **Top-K trending items** in real time (like social media trending topics)? :contentReference[oaicite:12]{index=12}

---

## 14. CDN & Edge Compute
- How do you design a system where **user-uploaded images** are resized at the edge with caching and cost-efficiency?
- How would you **design a CDN** to serve static assets globally with low latency? *(common question—no direct citation)*

---

## 15. AuthN/AuthZ & Identity
- How do you design a system supporting **OAuth2 login** and **service-to-service JWT validation**, including **token revocation**?
- What’s the difference between **JWT, OAuth, and SAML**, and where would each be used? :contentReference[oaicite:13]{index=13}

---

## 16. Rate Limiting & Abuse Prevention
- How would you implement **distributed rate limiting** across multiple API servers while avoiding **hotspot counters**?
- Design an **API rate limiter** that works at scale with sliding windows and fairness. :contentReference[oaicite:14]{index=14}

---

> “45 system design questions I curated for interviews” includes key ones like designing rate limiter, stream processing, metrics aggregation, KV store, etc. :contentReference[oaicite:15]{index=15}  
> Sites like GeeksforGeeks list typical systems: URL shortener, chat, storage services, search typeahead, file-sharing. :contentReference[oaicite:16]{index=16}  
> And “difference between API Gateway vs Load Balancer,” and concept vs problem questions are common. :contentReference[oaicite:17]{index=17}

---

Let me know if you want **hints** for what an interviewer expects, or want to deep-dive on any category—fast and punchy, just how you like it.
::contentReference[oaicite:18]{index=18}
