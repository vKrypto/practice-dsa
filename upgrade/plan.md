# 9 Days Hardcore Interview Prep Plan

| Day | Topics Covered                   | Subtopics / Actions                                                                                   | Resources / Tasks                             |
|-----|----------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| 1   | DSA (Easy/Medium)                | Arrays, Strings, Linked List, Trees, Graphs, Stack/Queue, Sliding Window                              | 15 problems + solution review                 |
| 2   | DSA (Advanced/Hard)              | DP, Recursion, Backtracking, Bit Manipulation, Top LC Hard, System Design-y DSA                       | 10 hard problems, discuss tradeoffs           |
| 3   | Database Internals               | Indexing, Locking, ACID, CAP, Consistency, 2PC, Saga, Caching, SQL, Partitioning, Data Movement       | Implement queries, cache demo                 |
| 4   | Database/NoSQL Comparison        | DynamoDB, Redis, Cassandra, Time Series DB, PostgreSQL, SQL, MySQL, MongoDB, Use-case analysis        | Use-case matrix, when to use what             |
| 5   | Message Queues & Patterns        | Kafka, RabbitMQ, Redis PubSub, SMS, Orchestration, CQRS, Event Sourcing, Circuit Breaker, Design Patterns | Diagrams, design integration              |
| 6   | Monitoring, Infra, Cloud, DevOps | Kubernetes, Docker, Prometheus, Grafana, AWS/GCP/Azure, Terraform, Alerts, SLO/SLA, Tracing, IAM, Security | Dockerize app, deploy on K8s, infra demo |
| 7   | System Design (HLD/LLD/Tradeoffs)| Uber, Netflix, WhatsApp, Rate Limiter, E-commerce, Instagram, Multi-region, CDN, Failover, Case Studies | HLD/LLD diagrams, APIs, bottleneck deep-dive  |
| 8   | Mock Interviews (Tech+Behavioral)| DSA, System Design, Leadership, Conflict, Mentoring, 1:1s, Feedback Loops                             | 2-3 mocks, collect detailed feedback          |
| 9   | Resume/LinkedIn/Blogs/Apply      | Update resume, write blogs, LinkedIn posts, referrals, bulk apply, brag doc, outreach                 | Final review, outreach, track jobs            |


## Topic Checklist

| Main Topic         | Subtopics to Cover                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| **DSA**            | Arrays, Strings, Trees, Graphs, DP, Backtracking, Bit manipulation, Sliding window, Heap, Trie, Real-world coding    |
| **Database**       | Indexing, Locking, ACID, CAP, Consistency, 2PC, Saga, Partitioning, Caching, SQL, Data Movement, Sharding            |
| **Databases/NoSQL**| DynamoDB, Redis, Cassandra, Time Series DB, PostgreSQL, SQL, MySQL, MongoDB, Use-case tradeoffs                      |
| **Message Queues** | Kafka, RabbitMQ, Redis PubSub, SMS, Orchestration, CQRS, Event Sourcing, Circuit Breaker, Design Patterns            |
| **Monitoring/Infra**| Kubernetes, Docker, Prometheus, Grafana, AWS/GCP/Azure, Terraform, Alerts, Tracing, IAM, Security, Infra basics    |
| **System Design**  | Uber, Netflix, WhatsApp, Instagram, Rate Limiter, E-commerce, Multi-region, CDN, API Versioning, HLD, LLD, Bottlenecks |
| **Cloud & Security**| Managed DBs, IAM, Secret Management, Cost & Scaling, Security Basics, Disaster Recovery, Load Balancing             |
| **OS/Networking**  | Threads, Processes, Scheduling, File Systems, HTTP, TLS, Load Balancers, CDN, DNS, Performance debugging             |
| **Testing/Observability** | Testing strategies, Unit/Integration/E2E tests, Observability, SLO/SLA, Incident handling                   |
| **Leadership/Behavioral**| Mentoring, Conflict resolution, Stakeholder management, 1:1s, Feedback, Business impact stories                |
| **Mock Interviews**| DSA, System Design, Behavioral, Peer/Platform-based, Feedback, Staff-level questions                                 |
| **Portfolio/Outreach**| Resume, Blogs, LinkedIn, Open Source, Referrals, Bulk Apply, Brag Doc                                            |



# DSA Topics Breakdown for Interviews

| Topic           | Key Concepts / Subtopics                                                                           | Must-Do Patterns / Notes                        |
|-----------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Arrays          | - Prefix Sum <br> - Kadane's Algo <br> - Two Pointer <br> - Sorting/Searching <br> - Hashing       | Classic: Max Subarray, Move Zeroes, Dutch Flag  |
| Strings         | - Pattern Matching (KMP, Z Algo) <br> - Palindrome <br> - Substrings/Subsequence <br> - Anagrams   | Think: Manacher’s, Rabin-Karp, Sliding Window   |
| Linked List     | - Reverse (Iterative/Recursive) <br> - Detect Cycle <br> - Merge k Lists <br> - Intersection Point | Never trust a Linked List, edge cases OP        |
| Trees           | - Traversals (In, Pre, Post) <br> - BST ops <br> - Diameter <br> - LCA <br> - Depth/Balanced       | Recursive > Iterative unless interviewer hates  |
| Graphs          | - BFS/DFS <br> - Topo Sort <br> - Shortest Path (Dijkstra, Bellman-Ford) <br> - Union Find         | Graph = Adjacency List, Edge List, Matrix       |
| Stack / Queue   | - Monotonic Stack <br> - Min/Max Stack <br> - LRU Cache <br> - Queue via Stack/Stack via Queue     | Don’t forget balanced parentheses, Next Greater |
| Sliding Window  | - Fixed / Variable Window <br> - Max/Min Subarray <br> - Longest Substring Without Repeat          | “Brute + Optimize” is the real pattern          |

---

## Bro tips:
- *Arrays and Strings*: If you’re not O(n), you’re already losing.
- *Linked List*: Always prep for corner cases, and don’t sleep on “fast/slow pointer” tricks.
- *Trees/Graphs*: If you forget recursion, just tell them you only do “cloud native BFS”.
- *Sliding Window*: Interviewer ka favourite for anything “longest/shortest/maximum sum/unique”.

Stay sharp, stay OP.   



