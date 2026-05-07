# Chapter 14 – Cloud Forensics
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/14_Cloud.pdf`](Slides/Atzeni/14_Cloud.pdf)
**Covered in Lectures:** [Lecture 26](Lectures_MD/Lecture_26_Vaciago.md)

---

## Introduction

Cloud forensics applies digital forensic methodology to environments where physical access, stable storage, and direct hardware control are often unavailable. Evidence is mediated by cloud provider APIs, contracts, logs, and cooperation.

---

## 1. Peculiarities

> 📎 *Slide reference: `14_Cloud.pdf` — Cloud forensics peculiarities*

| Peculiarity | Forensic Impact |
|-------------|-----------------|
| **Multi-tenancy** | A physical disk cannot simply be seized or imaged because it contains other customers' data. |
| **Ephemeral resources** | VMs, containers, serverless functions, logs, and local storage may disappear quickly. |
| **Provider dependency** | Evidence access depends on cloud model, APIs, credentials, and cooperation. |
| **Jurisdictional fragmentation** | Data may be replicated across countries with conflicting laws. |
| **Log incompleteness** | Some events are not logged by default, especially data-plane actions. |

---

## 2. Cloud Service Models

| Model | Evidence Visibility |
|-------|--------------------|
| **SaaS** | Mostly user-level logs and application records; strong provider dependency. |
| **PaaS** | Application and platform-level logs; no hardware control. |
| **IaaS** | VM, disk, and network configuration access; still mediated by provider infrastructure. |

The lower the user's control, the more the investigator depends on provider cooperation.

---

## 3. Cloud Storage and S3

> 📎 *Slide reference: `14_Cloud.pdf` — Cloud storage example of service*

Amazon S3 illustrates cloud evidence opportunities:
- versioning;
- WORM-like retention options;
- encryption options;
- cloud logs, depending on configuration;
- multiple storage classes including long-term archive.

These features may be excellent for evidence preservation, but only if configured before the incident.

---

## 4. Provider Trust and Logging Limits

The lecture stresses that investigators often use cloud-provider tools and APIs rather than direct hardware access. This makes provider trust central: logs, signatures, and retained data may be very useful, but their reliability depends on cooperation and on what was configured before the incident.

Atzeni also highlights that management operations may be logged by default while data-plane operations, such as reading stored objects, may not be logged unless explicitly enabled.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **CSP** | Cloud Service Provider. |
| **SaaS/PaaS/IaaS** | Cloud service models with different user control and forensic visibility. |
| **Data Plane Event** | Action involving data access, such as reading an object. |
| **Control Plane Event** | Administrative action, such as changing IAM policy or launching an instance. |
| **Provider Dependency** | Need to rely on cloud-provider APIs, logs, signatures, and cooperation rather than direct physical access. |

---

## Summary
- Cloud forensics often lacks direct physical acquisition.
- Evidence visibility depends heavily on SaaS, PaaS, or IaaS model.
- Provider APIs and logs are both useful and a source of trust dependency.
- Ephemeral resources require fast logging and snapshot strategies.
- Redundancy can preserve evidence but complicates physical-location assumptions.
- Jurisdiction and provider-controlled signatures must be documented carefully.
