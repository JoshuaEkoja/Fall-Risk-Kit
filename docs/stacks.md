# AWS Stacks Overview and Local Mapping

This project is a local Python simulation of an AWS-native, event-driven solution. The following stacks outline a comprehensive AWS architecture for production. Below, we include the proposed stacks as-is and then assess how each maps to the current local project.

## Proposed Stacks (AWS)

| Stack | Key Components (AWS) | Purpose | Description |
| ------------------------------------- | ----------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| core-foundation-stack | IAM, CloudTrail, GuardDuty, org tags | Org bootstrap & security baseline | Establishes the foundational security and governance posture for the account. It ensures logging, auditing, and threat detection are consistent across environments while enforcing org-wide tags for traceability. |
| network-baseline-stack | VPC, Subnets, NAT, Endpoints, SGs | Private, secure networking | Defines the network fabric where all services run, balancing isolation with connectivity. By standardizing VPCs and endpoints, this stack creates secure pathways for Lambda, IoT, and AI workloads. |
| kms-secrets-ssm-stack | KMS CMKs, Secrets, SSM | Central secrets & config | Provides a centralized key and secret management layer, ensuring encryption at rest and in transit. It also stores application parameters for consistent retrieval across all stacks. |
| compliance-guardrails-stack | Config, Security Hub, Macie | Continuous compliance | Monitors AWS resources against compliance standards such as HIPAA or CIS benchmarks. It enables automated remediation and unified visibility of security posture. |
| observability-stack | CloudWatch logs/alarms, X-Ray, Synthetics | End-to-end monitoring | Collects, visualizes, and alerts on infrastructure and application metrics. It supports proactive detection of failures and gives teams observability into distributed workflows. |
| cost-governance-stack | CUR, Athena views | Cost visibility | Provides detailed cost tracking, enabling tagging-based cost allocation and reporting. It acts as the financial telemetry layer of the project. |
| backup-dr-stack | AWS Backup, DR copy | Data protection | Implements automated backups and disaster recovery strategies across environments. This stack ensures critical data sets can be recovered in the event of failure or compliance audits. |
| budget-guardrails-stack | AWS Budgets, Actions, Anomaly Detection | Proactive budget control | Proactively tracks and controls AWS spending with alerts and automated actions. It integrates anomaly detection and budget enforcement to prevent runaway costs. |
| iot-core-fleet-stack | IoT Registry/Policies/Jobs/Defender | Device identity & fleet mgmt | Manages registration, identity, and lifecycle operations for connected devices. Provides fleet-level jobs, updates, and security posture validation. |
| iot-ingestion-rules-stack | IoT Rules → Kinesis/Firehose/Lambda | Real-time ingestion | Captures telemetry data from devices and routes it into streaming, analytics, or storage destinations. It forms the first stage of the device data pipeline. |
| stream-processing-stack | Kinesis Streams/Analytics, Lambda | Streaming transforms | Performs real-time enrichment and aggregation on streaming data. Enables near real-time insights and anomaly detection on device telemetry. |
| timeseries-db-stack | Timestream | Time-series analytics | Stores device telemetry in a time-series optimized database. Supports analytics and dashboards over trends, metrics, and longitudinal patterns. |
| data-lake-core-stack | S3 zones, Glue, Lake Formation | Governed data lake | Provides a multi-zone data lake architecture (raw, clean, curated) to store and organize all incoming data. Integrates with Glue and Lake Formation to enable discoverability and governed access. |
| etl-orchestration-stack | Step Functions, Lambda | Batch/mini-batch ETL | Automates transformations and data quality pipelines, moving datasets from raw to curated states. Enables reproducible, event-driven ETL flows. |
| fhir-healthlake-stack | HealthLake datastore | FHIR repository & APIs | Hosts clinical data in FHIR format, enabling healthcare-grade storage and retrieval. Provides a secure foundation for downstream analytics and interoperability. |
| fhir-transform-gateway-stack | API GW + Lambda | Map device → FHIR | Translates device telemetry into standardized FHIR resources. Ensures interoperability with clinical and research applications. |
| interop-apis-stack | API Gateway, WAF | Partner access APIs | Provides managed and secure external access to data and workflows. Supports throttling, usage plans, and security enforcement. |
| embeddings-and-rag-stack | Bedrock/SageMaker, OpenSearch | Search & retrieval (RAG) | Runs embeddings jobs and indexes them into a vector store for semantic search. Supports retrieval-augmented generation for clinical or operational queries. |
| feature-store-mlops-stack (opt) | SageMaker Feature Store, Pipelines | ML feature governance | Manages feature definitions and storage for ML training and inference. Integrates with CI/CD pipelines to ensure reproducible ML workflows. |
| analytics-warehouse-stack | Athena, Glue Views, Redshift | BI/SQL analytics | Provides warehouse-style analytics for large-scale queries across curated datasets. Optimized for BI tools and joins with governance from the data lake. |
| quicksight-dashboards-stack | QuickSight dashboards | Dashboards | Creates user-facing dashboards that visualize operational, financial, and clinical insights. Provides secured, role-aware access to visual analytics. |
| app-services-stack | Lambda/ECS, DynamoDB, SQS/SNS | Core business services | Hosts the core application logic in a serverless or containerized model. Connects workflow, data, and API layers into cohesive business services. |
| events-bus-stack | EventBridge bus/rules/scheduler | Event-driven backbone | Serves as the central nervous system for event-driven operations. Routes and fans out events between ingestion, ETL, and applications. |
| workflows-stack | Step Functions | Long-running flows | Orchestrates long-running or multi-step workflows with human-in-the-loop steps. Provides reliability and visibility into complex processes. |
| notifications-stack | SNS, SQS, Chatbot | Alerts & fan-out | Provides alerting and message distribution services. Ensures critical events reach users and systems through multiple channels. |
| cognito-auth-stack | Cognito User/Identity Pools | App/user authN/Z | Handles identity management for app users and developers. Integrates with APIs for secure and federated authentication. |
| partner-access-stack | Cross-acct roles, API keys | Third-party access | Governs controlled access for external partners and collaborators. Supports fine-grained access control and auditing. |
| frontend-edge-stack | S3, CloudFront, WAF | Frontend delivery | Hosts static frontends and serves them with low latency globally. Protects delivery with caching, TLS, and WAF rules. |
| docs-portal-stack | S3/CloudFront, CodeBuild | Living docs & runbooks | Provides a knowledge hub for architecture, configuration, and operational playbooks. Automatically publishes documentation updates with each release. |
| cicd-pipeline-stack | CodePipeline/Build/Deploy | Infra/app delivery | Automates the deployment lifecycle of infrastructure and applications. Provides gates, approvals, and rollbacks for safe delivery. |
| ecr-repositories-stack | ECR repos | Container image registry | Provides private repositories for Lambda containers and ECS images. Enforces lifecycle policies for efficient image management. |
| artifacts-bucket-stack | S3 + KMS | Build artifacts | Stores versioned build artifacts and provenance data. Acts as the single source of truth for deployed assets. |
| governed-datasets-stack | Lake Formation grants/LF-tags | Data product governance | Applies fine-grained access controls for datasets. Supports producer-consumer patterns for controlled sharing. |
| metadata-config-stack | DynamoDB, S3 schemas | Schemas & feature flags | Stores schema definitions, feature flags, and configs centrally. Acts as the system registry for ETL and API consistency. |
| veeva-authenticate-stack (opt) | Secrets, SSM, DDB, Lambda | Veeva session mgmt | Authenticates and maintains session state with Veeva Vault. Centralizes secrets and session data for downstream queries. |
| veeva-integration-stack (opt) | Lambda, S3 staging, DDB, SFN | VQL execution/export | Automates execution of VQL queries and manages result delivery to S3. Integrates Veeva data into downstream pipelines. |
| egress-controls-stack (opt) | VPC egress, test Lambda | Egress control & tests | Enforces controlled egress from workloads. Provides continuous tests to prevent data leaks or misconfigurations. |
| device-simulator-stack | Lambda/ECS publishers, IoT | Synthetic load & scenarios | Generates synthetic device data to simulate real-world scenarios. Enables safe, cost-controlled testing of ingestion and analytics. |
| sandbox-data-stack | S3, Glue | Demo & dev data | Hosts synthetic datasets for safe experimentation. Provides a red/blue separation for demos and education. |

## Do these make sense for this project?

Short answer: Yes, as an aspirational AWS target architecture. For this local simulation, many stacks are conceptually relevant but not implemented as cloud resources. Below is how each stack maps to the current codebase and where it would live in AWS.

Legend:
- Implemented (local): there is a concrete analogue in this repo.
- Partial (local): some aspects are simulated or could be trivially added.
- Future/Not Applicable (local): no local analogue; relevant only in cloud.

### Mapping to FallRisk Kit components

- core-foundation-stack — Future/Not Applicable (local)
  - Cloud IAM/CloudTrail/GuardDuty have no local equivalents. We rely on Python logging and local processes.
- network-baseline-stack — Future/Not Applicable (local)
  - No VPC/SGs here. Everything runs in-process.
- kms-secrets-ssm-stack — Partial (local)
  - fallrisk_kit.config.Config holds parameters; secrets could be wired via environment variables or a .env loader if needed.
- compliance-guardrails-stack — Future/Not Applicable (local)
  - Would be AWS-native (Config/SecurityHub/Macie). For local, linting/tests act as quality gates.
- observability-stack — Partial (local)
  - Python logging and structured JSONL outputs; could be extended with OpenTelemetry exporters.
- cost-governance-stack — Future/Not Applicable (local)
  - No cloud billing locally.
- backup-dr-stack — Partial (local)
  - Data is written to data/ directories and SQLite. Backups are manual; could add export scripts.
- budget-guardrails-stack — Future/Not Applicable (local)
- iot-core-fleet-stack — Future/Not Applicable (local)
  - Local simulator (simulator/imu_stream.py) stands in for device fleet, without identity policies.
- iot-ingestion-rules-stack — Implemented (local)
  - fallrisk_kit.ingestion: validates telemetry and emits events via fallrisk_kit.events (EventBridge analogue).
- stream-processing-stack — Implemented (local)
  - fallrisk_kit.features and fallrisk_kit.risk perform windowing and scoring in near real-time.
- timeseries-db-stack — Partial (local)
  - We persist JSONL and SQLite; no Timestream, but time-indexed data exists.
- data-lake-core-stack — Implemented (local)
  - data/raw and data/curated directories simulate S3 zones (raw, curated). Glue/LF are not present.
- etl-orchestration-stack — Implemented (local)
  - fallrisk_kit.runner orchestrates async workflows; analogous to Step Functions + Lambda.
- fhir-healthlake-stack — Partial (local)
  - fallrisk_kit.fhir_mapper writes FHIR resources to local JSON. No managed datastore.
- fhir-transform-gateway-stack — Implemented (local)
  - fhir_mapper consumes events and produces FHIR resources; FastAPI could front this if needed.
- interop-apis-stack — Partial (local)
  - fallrisk_kit.api exposes read-only endpoints; no WAF/throttling.
- embeddings-and-rag-stack — Future/Not Applicable (local)
  - Could be added later with a small vector store and embedding lib.
- feature-store-mlops-stack (opt) — Future/Not Applicable (local)
- analytics-warehouse-stack — Future/Not Applicable (local)
  - Could map to DuckDB/SQLite + SQL views locally.
- quicksight-dashboards-stack — Future/Not Applicable (local)
  - Could map to local notebooks or lightweight dashboards.
- app-services-stack — Implemented (local)
  - Core business logic spans ingestion → features → risk → alerts; API provides access.
- events-bus-stack — Implemented (local)
  - fallrisk_kit.events is the in-process EventBridge analogue.
- workflows-stack — Implemented (local)
  - fallrisk_kit.runner composes steps; long-running flows can be modeled with asyncio tasks.
- notifications-stack — Partial (local)
  - fallrisk_kit.alerts writes alerts to SQLite; could add email/webhook senders.
- cognito-auth-stack — Future/Not Applicable (local)
  - API is unauthenticated for simplicity; could add auth middleware.
- partner-access-stack — Future/Not Applicable (local)
- frontend-edge-stack — Future/Not Applicable (local)
  - Docs are served via MkDocs locally; no CDN/WAF.
- docs-portal-stack — Implemented (local)
  - MkDocs site with auto-generated API docs plays this role.
- cicd-pipeline-stack — Future/Not Applicable (local)
  - Use GitHub Actions in cloud; not simulated here.
- ecr-repositories-stack — Future/Not Applicable (local)
- artifacts-bucket-stack — Future/Not Applicable (local)
- governed-datasets-stack — Future/Not Applicable (local)
  - In AWS, governed sharing via Lake Formation; locally, simple file access.
- metadata-config-stack — Partial (local)
  - Config and schema validation could live in fallrisk_kit.config and pydantic models in the future.
- veeva-authenticate-stack (opt) — Future/Not Applicable (local)
- veeva-integration-stack (opt) — Future/Not Applicable (local)
- egress-controls-stack (opt) — Future/Not Applicable (local)
- device-simulator-stack — Implemented (local)
  - simulator/imu_stream.py generates synthetic telemetry for testing and demos.
- sandbox-data-stack — Implemented (local)
  - The synthetic telemetry and sample outputs under data/ serve as sandbox datasets.

## Next steps (if/when targeting AWS)

- Start with core-foundation-stack and network-baseline-stack to establish guardrails.
- Implement events-bus, ingestion rules, data lake core, and ETL orchestration stacks.
- Add observability and notifications early for operational insight.
- Iterate toward FHIR data store, interop APIs, and cost/budget guardrails.
