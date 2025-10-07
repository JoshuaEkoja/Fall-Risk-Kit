# FallRisk Kit – Build-a-thon Advisor Check-in

## Slide 1 – Hypothesize Need
- Falls are a leading cause of ER visits; patients often can’t recall event details (real case: mom’s fall).  
- Current solutions focus only on detection, missing context transfer to care teams.  
- Scale: **36M falls/year in the U.S., >$50B annual costs**.  
- Impact: **Economic, human, and social burden** across patients, families, and healthcare systems.  
- Need: A system that captures, transfers, and standardizes fall data for ERs, researchers, and device makers.  

---

## Slide 2 – Stakeholder Validation & Iteration
- **Patient / ER:** Needs immediate, contextual fall info for better emergency care.  
- **Researcher:** Feedback → requested **API batch upload** (not just real-time sensors) to support retrospective studies & commercial pilots.  
- **Device Manufacturer:** Feedback → prefers a **SaaS cloud model** with simplified integration, reducing custom build costs.  
- **Iteration:** Refined from *“real-time wearable detector”* → **hybrid ingestion model (real-time + batch API)**.  
- Stakeholder input guided pivot toward a scalable **AWS SaaS architecture**.  

---

## Slide 3 – Solution Definition with Key Features
- **Hybrid ingestion (from feedback):** Supports **real-time streaming** for ER + **API batch upload** for research and vendor use.  
- **FHIR interoperability:** Normalizes outputs into HL7 FHIR for clinical, research, and regulatory adoption.  
- **Context capture:** Automatically records fall timestamp, activity, and severity for care teams.  
- **SaaS model:** Cloud-native architecture deployable in AWS; includes **free-tier entry (minimum devices)** for research adoption.  
- **Planned outputs:**  
  - GitHub repo: SDK + infrastructure code.  
  - AWS information architecture: modular stacks for ingestion, storage, analytics.  

---

## Deliverables
- GitHub Repository (this repo).  
- Information Architecture for AWS components and stacks.  
- Open-source SDK supporting **FallRisk Kit ingestion pipeline**.  