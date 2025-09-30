# FallRisk Kit: Project Presentation & Concept Guide

Last updated: 2025-09-30

This document presents a structured, presentation-ready overview of the FallRisk Kit concept. It consolidates brainstorming ideas into a concise reference for academic project committees and collaborators. The emphasis is on remote health monitoring for at-risk populations (e.g., Parkinson’s patients or the elderly), with a focus on feasibility, impact, and research value. This is a fictional/academic concept with no commercialization intent.

- Audience: Academic teams, researchers, clinicians, caregivers, and technical reviewers
- Scope: Concept summary, scientific background, hardware, integrations, SDK/API design, stakeholders, presentation outline, and a 3-week prototype plan

---

## 1) Project Overview

FallRisk Kit is an open-source software development kit (SDK) that simplifies fall risk monitoring and early prediction using wearable inertial sensors. It:

- Ingests real-time IMU data (accelerometers + gyroscopes)
- Computes gait/balance features and basic risk scores (variance/thresholds, simple logistic/sigmoid)
- Integrates with EHRs via standardized FHIR APIs
- Enables remote monitoring, alerts, and longitudinal trend analysis
- Prioritizes plug-and-play customization, open-source extensibility, and HIPAA-aligned data workflows

Target users include Parkinson’s patients, seniors, post-stroke individuals, and diabetics. The SDK bridges the gap between IMU telemetry and EHR interoperability, differentiating from reactive SOS pendants by enabling proactive, data-driven fall prevention.

Key advantages vs. consumer devices:
- Predictive analytics from gait patterns, not just fall detection
- Open-source and research-friendly with EHR-standard outputs (FHIR)
- Designed for interoperability and customization, not lock-in

---

## 2) Background and Basic Science

- Public health impact: ~3M elderly Americans treated annually for falls; ~$50B in costs
- Vulnerable groups: Seniors (balance decline), Parkinson’s (tremor/freezing gait), post-stroke (hemiparesis), diabetics (neuropathy)
- Remote monitoring opportunity: Detect risk trends early to reduce ER visits and injuries

Sensor science overview:
- Accelerometers: Linear acceleration along x/y/z (m/s²)
- Gyroscopes: Angular velocity (°/s) across pitch/roll/yaw
- Together: 6-DoF streams enabling 3D motion context

Core methods (simple, explainable):
- Filtering/fusion: Complementary or basic Kalman to limit noise/drift
- Feature extraction: Variance, standard deviation, stride symmetry, tilt maxima
- Heuristics and simple models: Thresholds and logistic/sigmoid transforms to 0–100 risk
  - Example: risk = sigmoid(β0 + β1 · gait_variance + β2 · tilt_max)

Datasets for research/prototyping:
- SisFall, MHEALTH (for offline testing, simulation, and backtesting)

Differentiation from existing solutions:
- Pendants: Primarily SOS/fall-reactive; higher false positives; limited analytics
- Piecemeal tools (e.g., niche APIs): Lack unified, EHR-focused, open-source SDK path

---

## 3) Sensors and Hardware

- Sensor type: MEMS IMUs combining 3-axis accelerometers + gyroscopes (e.g., MPU-6050, Bosch BMA280)
- Cost/efficiency: ~$1–10/unit; low power (<1 mA); sample at 50–100 Hz
- Form factors: Wrist, ankle, belt/pendant; modular placement for gait/balance signal quality
- Receiver hub: Raspberry Pi Zero class device via BLE; buffers offline and forwards
- Data flow: BLE → receiver → pre-processing (e.g., filtering) → stream to platform
- Rationale: MEMS are ubiquitous, sensitive to subtle tremors/tilts, and compatible with public datasets

Note: For early prototypes, no hardware required—use simulators and public datasets to stream synthetic IMU data.

---

## 4) Value Proposition

- Impact potential: Simulations suggest 15–20% fall reduction via early alerts and trend monitoring
- Research value: Facilitates studies on Parkinson’s gait, medication tuning, and fall prevention protocols
- Unique qualities:
  - Plug-and-play ingestion for diverse sensors
  - FHIR-standard outputs for frictionless EHR integration
  - Open-source baseline for reproducible academic research
- Academic adoption: GitHub distribution, documentation, and dataset-driven examples
- Optional future funding (if ever scaled beyond academic scope): Dual licensing, grants, premium models

Broader applications:
- Home health: Solo monitoring, caregiver alerts
- Telehealth: Remote triage, longitudinal trends
- Rehab: Adherence tracking, balance exercises
- Daily activities: Risk around bed exits, bathroom transitions

---

## 5) Platform Integrations

- Ingestion/scaling: AWS IoT (MQTT) for low-latency streams (<100 ms)
- Rules/processing: IoT Rules → Lambda/Kinesis for routing and transforms
- EHR gateway: FHIR (e.g., Epic/Cerner interoperability)
  - Example Observation: { code: "Fall Risk", value: 85 }
- Flow reference: Sensor/receiver → AWS IoT → Lambda mapper → FHIR POST to EHR
- Simulation support: AWS IoT Device Simulator for synthetic IMU payloads
- Extensibility: IFTTT/smart home hooks; TinyML at the edge for on-hub scoring

Note: For local academic prototypes, a FastAPI service + file/SQLite storage is sufficient.

---

## 6) API and SDK Details

Languages and packaging:
- SDK name (example): fallrisk-kit
- Distribution targets: PyPI/npm/Swift Package (as applicable)
- Install example: pip install fallrisk-kit
- Containerization: Docker image for quick demos
- CLI: fallrisk init to scaffold a project

Core features:
- Ingestion: client.ingest_imu_data(batch)
- Feature extraction: variance, tilt maxima, symmetry
- Risk scoring: REST POST /predict → { "risk_score": 85 }
- Trends: GET /trends → CSV/JSON time series
- Alerts: POST /alert (webhook for caregivers)
- Dashboards: Plotly charts for quick visualization
- Sample datasets and notebooks for reproducibility

FHIR integration:
- Mapper service converts IMU-derived metrics to FHIR Observations
- OAuth flows for EHR sync (mocked in academic prototype)

Math example:
- risk = sigmoid(β0 + β1 · gait_variance + β2 · tilt_max)

License: MIT (open, research-friendly)

---

## 7) Stakeholders

- Primary: Academic team/committee; patient groups (e.g., Parkinson’s) for feedback
- Secondary: Clinicians/telehealth providers; researchers adopting the SDK
- Tertiary: Tech partners (e.g., AWS); funders for grants; caregivers/families

Engagement strategies:
- Needs surveys (e.g., prioritize bathroom/bed-exit monitoring)
- Demos showing simulated 15–20% risk reduction
- Feedback loops via pilot studies and office hours

---

## 8) Presentation Plan (10–15 minutes)

Recommended slide flow:
1. Intro (2 min)
   - Fall statistics and problem framing
   - FallRisk Kit as the gap-filling SDK for remote monitoring
2. Background & Problem (3 min)
   - Gait/sensor science; target populations; competitor gaps
3. Solution Details (4 min)
   - MEMS sensor diagram; SDK/API code snippets; AWS/FHIR flow
4. Value & Use Cases (3 min)
   - Impact metrics; home/telehealth scenarios; differentiation
5. Build Plan & Next Steps (2 min)
   - 3-week timeline; resources and asks
6. Q&A (1–2 min)
   - Prepare for questions on simulation vs. hardware, privacy, data quality

Tips for delivery:
- Use flow diagrams and mock dashboards
- Demo simulated data flow end-to-end
- Emphasize academic merits (open-source, publications, grants)

---

## 9) 3-Week Build Plan (Prototype)

Assumptions: 10–20 hours/week; Python-first; AWS Free Tier where applicable.

| Week | Goals & Tasks | Deliverables | Resources |
|------|----------------|--------------|-----------|
| 1: Foundation & Simulation | - Initialize repo and dependencies (e.g., awsiotsdk, fhir.resources) <br> - Build a simple IMU simulator (randomized vectors or dataset replay) <br> - (Opt) Deploy AWS IoT Device Simulator via CDK for MQTT streams <br> - Implement basic math: variance, tilt, simple risk | - Working simulator publishing JSON <br> - Basic README/docs | - AWS account (optional) <br> - Public datasets (SisFall) <br> - Team: 1–2 coders |
| 2: API/SDK Core | - Implement SDK: ingestion client, CLI init, /predict endpoint (Flask/FastAPI) <br> - Add FHIR mapper (Lambda prototype or local service) <br> - Mock EHR POST to a dummy server <br> - Test Parkinson’s scenarios (tremor spikes) | - Prototype SDK package (pip-installable) <br> - E2E: sim data → risk → FHIR JSON | - Jupyter for tests <br> - GitHub for version control <br> - Unit tests and CI |
| 3: Polish & Demo Prep | - Dashboards (Plotly), alerts (webhooks) <br> - Dockerize; add sample datasets/models <br> - Backtest on dataset (aim for ~15% simulated reduction) <br> - Prepare slides and a live simulation demo | - Demo-ready app + docs <br> - Slides with flow diagrams | - Presentation tools <br> - Feedback from advisors |

---

## 10) Quick References

- Example risk output: { "risk_score": 0–100, "confidence": 0–1, "timestamp": ISO8601 }
- FHIR Observation template (conceptual):
  - code: "Fall Risk"
  - valueQuantity: { value: score, unit: "%" }
  - subject: Patient/{id}
  - effectiveDateTime: timestamp

---

## 11) Notes and Assumptions

- Privacy/compliance: Treat as HIPAA-aligned research; use de-identified datasets during development
- Data quality: Emphasize filtering and windowing; keep models simple and explainable initially
- Extensibility: Hooks for ML upgrades, additional sensors, and smart-home integrations

---

## 12) How to Use This Guide

- For committees: Use as a briefing document and agenda outline
- For developers: Use as a blueprint for a 3-week prototype sprint
- For collaborators: Identify where to contribute (datasets, EHR integration, dashboards)

---

End of document.
