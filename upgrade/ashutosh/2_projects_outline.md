# Project Portfolio - Ashutosh Verma

## Executive Snapshot

Senior Software Engineer / Technical Lead with 8 years of experience across high-throughput backend systems, distributed architectures, AI governance platforms, RAG systems, ETL pipelines, observability, and e-commerce platforms.

### High-Impact Metrics

| Area | Impact |
|---|---:|
| AI governance platform reach | 400+ employees, 20+ AI tools |
| AI telemetry processed | Millions of token-consumption and usage events |
| Claude-powered engineering automation | ~90% reduction in manual PR review effort |
| NAV Accounts API optimization | p99 latency reduced from ~60s to ~40-50ms |
| Exchange data ingestion optimization | Runtime reduced from ~200s to ~5-9s |
| High-concurrency processing | 10k+ concurrent jobs, ~500k API requests/min |
| FastAPI memory leak RCA | Fixed 1.5TB data-loss leak over 5 days; infra cost reduced ~35% |
| RAG chatbot automation | 70-80% customer query resolution |
| TDD migration | 98%+ test coverage; 90+ critical defects caught before production |
| Retail/POS integration scale | 2,600+ U.S. Petco stores |
| ORNAZ PWA performance | 100/100 Lighthouse, <0.5s load time |
| ORNAZ platform reliability | 99.99% uptime; MTTR reduced up to 60% |

---

# Personal Projects

## Job-Seeker - Autonomous AI Career Agent

- **Timeline:** April 2026 - Present
- **Link:** Private
- **Tech Stack:** Python, FastAPI, LangGraph, LangChain, OpenAI, Claude, Gemini, Multi-Agent Systems, Agentic AI, LLM Orchestration, RAG, Prompt Engineering, Structured Outputs, Function Calling, Tool Calling, MCP, A2A, Qdrant, Pinecone, Embeddings, Semantic Search, Long-Term Memory, PostgreSQL, Redis, Playwright, Gmail API, Google Calendar API, LinkedIn Integration, Naukri Integration, ATS Integrations, React, Next.js, Docker, Kubernetes, CI/CD, Observability & Tracing

### Project Context

Built an autonomous AI-powered job acquisition platform designed to automate the end-to-end job search lifecycle: job discovery, fit analysis, resume tailoring, ATS optimization, application submission, recruiter communication, interview scheduling, and application tracking.

### Core Capabilities

- Built a **multi-agent architecture** with specialized agents for job discovery, resume generation, ATS optimization, application submission, recruiter communication, interview coordination, and workflow tracking.
- Implemented a **Multi-LLM orchestration layer** across OpenAI, Claude, and Gemini with dynamic model routing, fallback strategies, structured outputs, function calling, and tool calling.
- Designed **LangGraph-based stateful workflows** with agent state persistence, human-in-the-loop approval gates, memory-backed execution, retry handling, and fault-tolerant recovery.
- Developed **AI-powered email agents** that analyze recruiter conversations, detect intent, generate contextual replies, manage follow-ups, and coordinate interviews through Gmail and Calendar automation.
- Built dynamic resume generation pipelines producing role-specific resumes with **ATS scores above 90**, based on job descriptions, recruiter requirements, skills mapping, and keyword alignment.
- Integrated job portals, email systems, calendar scheduling, document management, and conversational AI into a unified automation platform.
- Added guardrails for document sharing, privacy control, approval workflows, hallucination prevention, incorrect submission prevention, and sensitive action protection.
- Created a dashboard to monitor application pipelines, recruiter engagement, interview stages, agent activities, workflow execution states, and overall job-search performance.

### Architecture Notes

- **Agent Layer:** Job Discovery Agent, Resume Agent, ATS Scoring Agent, Recruiter Communication Agent, Calendar Agent, Application Tracker Agent.
- **Memory Layer:** Long-term profile memory, historical recruiter communication memory, job preference memory, application-state memory.
- **Retrieval Layer:** RAG pipeline for matching role descriptions with profile/project experience using embeddings and semantic search.
- **Automation Layer:** Playwright-driven portal actions, Gmail workflows, Calendar workflows, and external ATS integrations.
- **Safety Layer:** Approval checkpoints before resume sharing, recruiter replies, application submission, and scheduling actions.

### Outcome

Reduced manual job-search operations by automating repetitive workflows while preserving human control for high-risk actions like document submission, recruiter communication, and interview scheduling.

---

## Local ERP - Healthcare ERP Platform

- **Timeline:** Jan 2026 - March 2026
- **Link:** https://github.com/vKrypto/marg-erp
- **Tech Stack:** Node.js, Express.js, React.js, MySQL, HTML, CSS, Bootstrap, Material UI, Browser-SQL

### Project Context

Developed a healthcare ERP platform and cost-effective alternative to MARG ERP for hospitals, clinics, pharmacies, and healthcare providers.

### Core Capabilities

- Implemented a hybrid **offline/online architecture** for uninterrupted healthcare operations even during network instability.
- Built modules for inventory management, billing, invoicing, patient management, appointment scheduling, reporting, supplier management, medicine stock tracking, purchase management, sales management, role-based access control, and financial records.
- Designed browser-side persistence using Browser-SQL patterns to support offline workflows and later synchronization.
- Built responsive UI flows for operational teams handling billing counters, pharmacy inventory, patient workflows, and administrative reports.

### Outcome

Delivered a practical ERP foundation focused on healthcare workflows, reduced administrative overhead, and improved continuity for facilities with intermittent connectivity.

---

# Professional Project Portfolio

## Fluxon Pvt. Ltd. - Senior Software Engineer (Contract)

- **Timeline:** Mar 2026 - Present
- **Location:** Remote, India

## FluxMetrics - AI Governance, Cost Intelligence & Observability Platform

- **Link:** https://metrics.fluxon.io/
- **Tech Stack:** NestJS, TypeScript, PostgreSQL, BigQuery, GCP, Docker, CI/CD, GenAI, RBAC, Observability, Claude AI

### Project Context

Architected and built an enterprise AI governance, cost intelligence, and observability platform serving **400+ employees** across **20+ AI tools**, including Claude, OpenAI, and internal AI platforms.

### Scope & Responsibilities

- Led backend architecture and service design for centralized AI usage governance.
- Designed scalable ingestion and analytics services to process **millions of AI telemetry and token-consumption events**.
- Built backend services using NestJS, TypeScript, PostgreSQL, BigQuery, GCP, Docker, and CI/CD pipelines.
- Established organization-level governance controls for AI usage visibility, spend control, access management, and leadership reporting.

### Core Systems Built

- **AI Cost Analytics:** Token-level visibility, team-wise usage breakdowns, model/provider usage analysis, cost attribution, budget controls, forecasting, and utilization dashboards.
- **GenAI Anomaly Detection:** Detection of abnormal token spikes, cost outliers, inefficient prompt patterns, unusual provider behavior, and budget-risk events before thresholds were breached.
- **Intelligent Alerting:** Configurable hourly, daily, weekly, and monthly monitoring windows with automated escalation and AI-generated cost optimization recommendations.
- **Governance & RBAC:** Enterprise-grade role-based access control, audit logging, team-level visibility, user-level attribution, and governance workflows.
- **Claude Engineering Automation:** Integrated Claude AI into engineering workflows for automated pull request reviews, security validation, code-quality analysis, documentation feedback, and fix recommendations.

### Measurable Impact

- Enabled centralized governance across **20+ AI platforms** and **400+ employees**.
- Processed **millions of telemetry events** to provide adoption, utilization, ROI, and spend-efficiency insights.
- Reduced manual engineering review effort by approximately **90%** through Claude-assisted PR review automation.
- Improved leadership visibility into AI adoption, platform utilization, spend efficiency, anomaly patterns, and compliance posture.

---

## NAV Backoffice Pvt. Ltd. - Platform Engineer

- **Timeline:** Aug 2024 - Feb 2026
- **Location:** Jaipur, India

## Accounts API Optimization

- **Tech Stack:** Golang, REST APIs, Async Workers, DB Optimization, Query Profiling, Multi-Layer Caching

### Project Context

Optimized a critical NAV Accounts API that had severe tail-latency issues and inconsistent response times under operational load.

### Core Work

- Profiled API execution paths, database queries, serialization costs, and blocking operations.
- Reworked slow data-access paths with query tuning, caching, and asynchronous worker patterns.
- Implemented multi-layer caching to reduce repeated expensive database calls and improve API responsiveness.
- Improved API throughput and stabilized performance under high-traffic workloads.

### Measurable Impact

- Reduced API latency from **p90 ~2s / p99 ~60s** to approximately **p95 ~2ms / p99 ~40-50ms**.
- Improved user experience by eliminating high-latency tail spikes in critical financial workflows.

---

## Exchange Data Fetch Optimization

- **Tech Stack:** FastAPI, Python AsyncIO, High-Concurrency Processing, Caching, Profiling

### Project Context

Re-engineered market/exchange data ingestion workflows that were slow, blocking, and unable to scale reliably with high job volume.

### Core Work

- Converted blocking data-fetch workflows into async FastAPI + AsyncIO pipelines.
- Improved job orchestration and execution scheduling for large-scale concurrent workloads.
- Added caching and profiling-driven optimizations to reduce redundant calls and bottlenecks.
- Hardened error handling for external exchange/API instability.

### Measurable Impact

- Reduced job runtimes from **~200s to ~5-9s**.
- Scaled the system to handle **10k+ concurrent jobs**.
- Supported approximately **500k API requests per minute** with robust async execution.

---

## Semantic Search Chatbot / AI Chatbot

- **Link:** https://github.com/vKrypto/semantics-search
- **Tech Stack:** FastAPI, LangChain, Elasticsearch, Vector Database, Transformers, OpenAI/Ollama, Large Language Models

### Project Context

Developed a retrieval-augmented chatbot for intelligent contextual Q&A and automated customer query resolution.

### Core Work

- Built RAG workflows combining semantic embeddings, vector search, Elasticsearch retrieval, and LLM response generation.
- Implemented vector-based document retrieval for efficient semantic matching.
- Designed scalable FastAPI services for query processing, retrieval, prompt assembly, and response generation.
- Optimized search and response paths for latency, relevance, and answer accuracy.

### Measurable Impact

- Improved customer query resolution by **70-80%**.
- Automated approximately **80% of user queries** through AI-assisted semantic retrieval and response generation.

---

## FastAPI Memory Leak RCA & Infrastructure Cost Optimization

- **Tech Stack:** FastAPI, Python, Profiling, Memory Analysis, Observability, RCA, Performance Engineering

### Project Context

Investigated and resolved a severe FastAPI memory leak affecting production workloads and infrastructure cost.

### Core Work

- Performed L3 root-cause analysis across services, memory growth patterns, request paths, and background tasks.
- Used profiling and observability data to isolate leak sources and reduce repeated memory retention.
- Stabilized service behavior and improved production reliability.

### Measurable Impact

- Fixed a memory leak associated with approximately **1.5TB data loss over 5 days**.
- Reduced infrastructure cost by approximately **35%**.
- Reduced incident MTTR by approximately **35%** through stronger RCA and monitoring practices.

---

## Full-Stack Observability & Health Monitoring

- **Tech Stack:** Grafana, Prometheus, Kibana, Jaeger, Graylog, Elasticsearch, cAdvisor, Node Exporter, Docker, OpenTelemetry Concepts

### Project Context

Built a distributed monitoring and health-observability layer across services, containers, infrastructure, logs, and traces.

### Core Work

- Implemented a health-monitoring agent across services and infrastructure components.
- Integrated node/system metrics, container metrics, centralized logs, traces, dashboards, and alerting.
- Built real-time visibility for service health, container behavior, error patterns, and operational incidents.

### Measurable Impact

- Reduced MTTR across distributed workloads.
- Improved reliability and troubleshooting efficiency through unified logging, metrics, and tracing.

---

## .NET Legacy Data Sync Re-Engineering

- **Tech Stack:** .NET, SQL Server, Stored Procedures, ETL, Windows Services, Repository Pattern, Factory Pattern, Dependency Injection

### Project Context

Refactored legacy .NET data synchronization pipelines that carried high maintenance cost and reliability risk.

### Core Work

- Re-architected data-sync workflows using cleaner design patterns and modular components.
- Improved stored procedure usage, ETL structure, and service-level maintainability.
- Reduced technical debt by introducing repository, factory, and dependency-injection patterns.

### Outcome

Improved maintainability, throughput, data consistency, and reliability for critical business synchronization workflows.

---

## Python Version Upgrade & Dependency Modernization

- **Tech Stack:** Python 3.x, Dependency Refactor, CI/CD, Test Automation, Unit Testing, Integration Testing

### Project Context

Modernized legacy Python services by upgrading Python versions, replacing deprecated APIs, and hardening automated validation pipelines.

### Core Work

- Resolved breaking changes and dependency incompatibilities.
- Refactored deprecated APIs and legacy service assumptions.
- Added automated unit/integration testing inside CI/CD pipelines.

### Outcome

Improved maintainability, reduced upgrade risk, and increased confidence in service releases.

---

## ShyftLabs - Senior Software Engineer

- **Timeline:** Nov 2023 - Aug 2024
- **Location:** Gurugram, India

## FastAPI to TDD Migration

- **Tech Stack:** FastAPI, Python, SQLite Test Harness, Pytest, Tox, GitLab CI/CD, Docker

### Project Context

Migrated a FastAPI project to strict test-driven development practices to improve production stability and release confidence.

### Core Work

- Built SQLite-backed test harnesses for deterministic API and data-layer testing.
- Added unit and integration tests across business-critical APIs.
- Integrated Tox and GitLab CI/CD pipelines for automated validation.
- Refactored test-unfriendly code paths to support reliable automation and regression detection.

### Measurable Impact

- Achieved **98%+ test coverage**.
- Identified and resolved **90+ critical defects** before production.
- Improved release confidence and reduced regression risk.

---

## Multi-Tenant ETL Pipelines for Marketplace Analytics

- **Link:** https://www.trycarter.com/
- **Tech Stack:** Python, MongoDB, Cassandra, Airflow, Kestra, Airbyte, Batch Pipelines, Streaming Pipelines

### Project Context

Designed and built multi-tenant ETL pipelines for marketplace analytics and event-log processing at high data volume.

### Core Work

- Built fault-tolerant data pipelines using hybrid batch and streaming orchestration.
- Processed high-volume event logs across tenant-specific data boundaries.
- Used Airflow, Kestra, and Airbyte to orchestrate ingestion, transformation, and downstream delivery.
- Integrated MongoDB/Cassandra-backed storage and analytics flows.

### Measurable Impact

- Supported data pipelines processing **billions of events daily**.
- Improved reliability of marketplace analytics and downstream reporting workflows.

---

## Pricing Change Implementation - Petco

- **Tech Stack:** Python, SQL, API Development, CI/CD

### Project Context

Delivered pricing-change workflows for offline U.S. Petco retail stores and integrated pricing APIs with enterprise retail systems.

### Core Work

- Built pricing-change API workflows for enterprise retail operations.
- Integrated backend systems with POS/platform requirements.
- Added CI/CD automation for reliable deployments and validation.

### Measurable Impact

- Supported pricing/POS platform integrations across **2,600+ U.S. Petco stores**.

---

## CI/CD with Tox and GitLab Pipelines

- **Tech Stack:** Tox, GitLab CI/CD, Docker, Automated Testing

### Core Work

- Automated build, test, and deployment workflows.
- Standardized CI execution through Tox environments.
- Improved consistency across local and pipeline validation.

### Outcome

Improved delivery reliability, reduced manual release friction, and made regression detection part of the default engineering workflow.

---

## Kestra Cassandra Plugin - Open Source Contribution

- **Tech Stack:** Java, Kestra, Cassandra, Open-Source Contribution

### Project Context

Contributed to the Kestra Cassandra plugin to improve connector stability and ingestion reliability.

### Core Work

- Reviewed and merged pull request **#45** to improve pipeline robustness and error handling.
- Enhanced connector behavior for data ingestion reliability and fault tolerance.
- Improved plugin stability for higher-throughput pipeline workloads.

### Outcome

Strengthened open-source data pipeline infrastructure around Kestra and Cassandra integration.

---

## ORNAZ - Senior Software Engineer / Tech Lead

- **Timeline:** Jun 2018 - Nov 2023
- **Location:** Gurugram, India

## Desktop E-Commerce Replatform - Next.js PWA

- **Timeline:** Apr 2021 - Nov 2023
- **Tech Stack:** Next.js, SSG, SSR, ISR, Node.js, Nginx, CDN, Payment Gateways

### Project Context

Rebuilt the ORNAZ desktop e-commerce experience into a high-performance Next.js progressive web application.

### Core Work

- Implemented modern rendering strategy using SSG, SSR, and ISR.
- Optimized assets, CDN delivery, server-side rendering, and caching behavior.
- Integrated multiple payment gateways and improved SEO/UX across product and checkout journeys.

### Measurable Impact

- Achieved **100/100 Lighthouse score**.
- Optimized page load times to **<0.5s**.
- Improved SEO performance, UX, and conversion readiness.

---

## Monolith to Microservices Migration

- **Timeline:** 2021 - 2023
- **Tech Stack:** FastAPI, Django, Docker Swarm, gRPC, REST, PostgreSQL HA, Celery, RabbitMQ, Distributed Workers

### Project Context

Migrated legacy monolithic systems into a cloud-native, service-oriented architecture with fault-tolerant workers and high-availability infrastructure.

### Core Work

- Split monolithic architecture into **4 core services + distributed workers**.
- Designed service boundaries and communication patterns using REST/gRPC.
- Built asynchronous processing with Celery and RabbitMQ.
- Architected PostgreSQL high-availability cluster with **2 master + 3 slave** topology.
- Containerized services and deployed using Docker Swarm.

### Measurable Impact

- Achieved approximately **99.99% uptime**.
- Improved maintainability, deployment isolation, and operational resilience.

---

## ORNAZ Observability Platform

- **Timeline:** 2021 - 2023
- **Tech Stack:** Grafana, Prometheus, ELK Stack, Jaeger, Sentry, Docker Swarm

### Project Context

Built centralized monitoring and observability across microservices, APIs, infrastructure, and production incidents.

### Core Work

- Implemented metrics dashboards, alerting, distributed tracing, logs, and error monitoring.
- Added single-pane visibility for service health and production failure investigation.
- Connected observability with incident response workflows.

### Measurable Impact

- Reduced MTTR by approximately **60%**.
- Improved production reliability across distributed workloads.

---

## Realtime AR Try-On - Cross-Platform Native + Web

- **Timeline:** 2020 - 2021
- **Tech Stack:** C++, MediaPipe, WebGL, WASM, Bazel, Swift, Java, Android, iOS, JavaScript

### Project Context

Built real-time jewelry try-on experiences for Android, iOS, and Web to improve product engagement and conversion.

### Core Work

- Developed shared C++ AR core with MediaPipe-based image processing.
- Built native integrations for Android and iOS using Java and Swift.
- Built WebGL/WASM-based browser rendering for web try-on experiences.
- Leveraged GPU acceleration for real-time overlays and rendering performance.
- Added fallback flows for low-end devices to preserve user experience.

### Measurable Impact

- Reused approximately **90% shared C++ AR core** across platforms.
- Increased engagement by approximately **50%**.
- Increased sales conversion by approximately **30%**.

---

## Virtual Trial Room - Web

- **Timeline:** 2020 - 2021
- **Tech Stack:** JavaScript, WebGL, MediaPipe C++, WASM, CDN, SSR

### Project Context

Launched browser-based AR trial room for users to preview jewelry from the web experience without installing mobile apps.

### Core Work

- Implemented WebGL/WASM rendering for in-browser AR overlays.
- Used CDN and SSR optimizations to reduce initial load cost.
- Added static fallback for low-end or unsupported devices.

### Measurable Impact

- Reduced load times by approximately **80%**.
- Increased engagement by approximately **30-40%**.

---

## Mobile Apps - React Native

- **Timeline:** 2020 - 2021
- **Tech Stack:** React Native, REST APIs, GraphQL APIs, Multi-Payment Integration

### Project Context

Built iOS and Android apps for ORNAZ using React Native to expand customer reach and reduce mobile development overhead.

### Core Work

- Built cross-platform mobile application flows.
- Integrated product browsing, checkout, APIs, and payment flows.
- Connected mobile apps with existing backend and e-commerce infrastructure.

### Measurable Impact

- Reduced mobile development cycle by approximately **30%**.
- Increased platform reach by approximately **40%**.

---

## Diamond Compare Tool

- **Timeline:** 2022 - 2023
- **Tech Stack:** Next.js, FastAPI, PostgreSQL, Elasticsearch, SSR, ISR

### Project Context

Created a diamond comparison and discovery tool to improve buyer decision-making and product engagement.

### Core Work

- Built real-time indexed search and comparison flows.
- Used Elasticsearch for fast filtering and discovery.
- Integrated comparison experience into the commerce journey.

### Measurable Impact

- Increased engagement by approximately **35%**.
- Improved conversion by approximately **20%**.

---

## Campaign Orchestrator

- **Timeline:** 2022 - 2023
- **Tech Stack:** Node.js, Next.js, Redis, Webhooks, Email APIs, SMS APIs

### Project Context

Built trigger-based customer journey and campaign orchestration workflows for commerce conversion.

### Core Work

- Implemented event-driven campaign triggers.
- Integrated webhooks, email APIs, SMS APIs, and Redis-backed workflow state.
- Enabled real-time customer journey actions based on user behavior.

### Outcome

Improved campaign responsiveness and conversion workflows through real-time journey orchestration.

---

## CRM + Journey Analytics

- **Timeline:** 2019 - 2020
- **Tech Stack:** Django, PostgreSQL, Celery, Grafana, Prometheus, Real-Time Session Monitoring

### Project Context

Implemented CRM and customer journey analytics to improve sales workflow visibility and lead response efficiency.

### Core Work

- Built CRM workflows for lead tracking and sales operations.
- Implemented per-session analytics and real-time session monitoring.
- Integrated metrics dashboards for sales and operational visibility.

### Measurable Impact

- Improved sales efficiency by approximately **40%**.
- Reduced lead response times through real-time tracking and CRM workflow automation.

---

## E-Commerce Core - ORNAZ v1

- **Timeline:** 2018 - 2020
- **Tech Stack:** Django MVT, PostgreSQL, Redis, RabbitMQ, Celery, HTML, Jinja2, JavaScript, PayU, Razorpay

### Project Context

Built the original mobile-first ORNAZ e-commerce platform with backend commerce workflows, payment integrations, and operational automation.

### Core Work

- Developed product, cart, checkout, payment, and user workflows.
- Integrated PayU and Razorpay payment gateways.
- Used Redis, RabbitMQ, and Celery for async workloads and background processing.
- Built mobile-first UI flows using Django templates, HTML, Jinja2, and JavaScript.

### Measurable Impact

- Increased mobile sales by approximately **40%**.
- Reduced cart drop-offs by approximately **25%**.
- Improved returning-user behavior through better performance and commerce workflows.

---

# Cross-Project Strengths Demonstrated

| Strength | Evidence |
|---|---|
| Performance engineering | Accounts API p99 60s -> 40-50ms; exchange jobs 200s -> 5-9s |
| High-concurrency backend design | 10k+ concurrent jobs; ~500k API requests/min |
| Distributed systems ownership | Microservices, async workers, HA database clusters, Docker Swarm, observability |
| AI/LLM systems | FluxMetrics, Job-Seeker, semantic chatbot, Claude PR automation, RAG pipelines |
| Reliability engineering | MTTR reduction, memory leak RCA, observability platforms, L3 support |
| Test engineering | TDD migration, 98%+ coverage, 90+ critical bugs found pre-production |
| Data engineering | Billions of daily events, Airflow/Kestra/Airbyte, Cassandra/MongoDB pipelines |
| Product engineering | PWA, AR try-on, campaign orchestration, CRM, mobile apps, ERP workflows |
| Leadership | Architecture ownership, PR review automation, team-level governance, cross-functional delivery |

