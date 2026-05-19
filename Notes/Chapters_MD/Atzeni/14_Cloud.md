# Chapter 14 – Cloud Forensics
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/14_Cloud.pdf`](../../Slides/Atzeni/14_Cloud.pdf)
**Covered in Lectures:** [Lecture 25](../../Lectures_MD/Lecture_25_Atzeni.md)

---

## Introduction

Cloud forensics applies digital forensic methodology to environments where physical access, stable storage, and direct hardware control are often unavailable. Evidence is mediated by cloud provider APIs, contracts, logs, and cooperation.

Atzeni presents cloud forensics as a stress test for the normal forensic phases. The investigator often cannot behave as the root owner of a seized machine: identification, collection, acquisition, analysis, and presentation are all filtered through virtualisation, provider dependency, redundancy, volatility, and jurisdiction.

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

## 5. Lack of Physical Access Across the Forensic Phases

> 📎 *Slide reference: `14_Cloud.pdf` — Cloud peculiarity effects*

| Phase | Cloud-Specific Effect |
|-------|----------------------|
| **Identification** | The investigator may need the CSP to list VMs, processes, operations, regions, and relevant logs. |
| **Collection** | API limits, contracts, rate limits, and shared infrastructure can delay or restrict collection. |
| **Acquisition** | Physical bit-by-bit imaging is usually replaced by snapshots, exports, and logical acquisition. |
| **Analysis** | Low-level metadata may be absent, abstracted, or only accessible through provider tools. |
| **Presentation** | The report must explain provider dependency, integrity checks, and uncertainty introduced by lack of direct access. |

The practical consequence is that cloud investigations require provider-specific technical knowledge before the emergency begins. It is not enough to know that "logs exist"; the examiner must know which logs exist, what they record, how long they are retained, and whether data-plane events were enabled.

---

## 6. Redundancy and Primary Copies

Cloud redundancy can preserve evidence in multiple places, but it complicates the meaning of the collected object. A replica, backup, or secondary copy may not be the authoritative source.

A **primary copy** is the original or actively used version of the data for forensic purposes. It may be identified through timestamps, replication tags, access logs, provider metadata, and CSP cooperation.

The examiner must document:
- which copy was acquired;
- whether it was primary, secondary, or unknown;
- whether redundant copies were ignored to save time;
- whether inconsistencies appeared between copies;
- how hashes and timestamps were preserved.

---

## 7. Virtualisation and Scale

Virtualisation can help because VM snapshots, disk exports, and sometimes memory captures can be produced from outside the guest system. This may reduce interaction with the target machine.

However, virtualisation also creates scale problems. Multiple snapshots and large virtual disks can quickly become terabytes of evidence. Expensive operations such as data carving, indexing, and full-disk analysis may take days or weeks if the scope is not narrowed.

The examiner must separate suspect-owned assets from shared resources involving unrelated users, and must request hypervisor-level logs from the CSP when guest-level evidence is not enough.

---

## 8. Volatility and Automation

Cloud resources may disappear quickly: containers, serverless functions, temporary disks, and auto-scaled VMs can exist for seconds or minutes. When direct acquisition is too late, the examiner may need to reconstruct activity from logs, snapshots, deltas, and provider monitoring.

Cloud APIs also create a positive possibility: acquisition can be automated. Scripts and cloud-aware forensic tools can rapidly collect many objects, snapshots, or logs when credentials and authorisation are available.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **CSP** | Cloud Service Provider. |
| **SaaS/PaaS/IaaS** | Cloud service models with different user control and forensic visibility. |
| **Data Plane Event** | Action involving data access, such as reading an object. |
| **Control Plane Event** | Administrative action, such as changing IAM policy or launching an instance. |
| **Provider Dependency** | Need to rely on cloud-provider APIs, logs, signatures, and cooperation rather than direct physical access. |
| **Primary Copy** | Authoritative or actively used version of a cloud object or VM instance. |
| **Replica** | Redundant copy created for availability, backup, recovery, or performance. |
| **Snapshot** | Point-in-time logical capture of a virtual machine, disk, or storage resource. |

---

## Summary
- Cloud forensics often lacks direct physical acquisition.
- Evidence visibility depends heavily on SaaS, PaaS, or IaaS model.
- Provider APIs and logs are both useful and a source of trust dependency.
- Ephemeral resources require fast logging and snapshot strategies.
- Redundancy can preserve evidence but complicates physical-location assumptions.
- Jurisdiction and provider-controlled signatures must be documented carefully.
- Primary-copy identification prevents both over-collection and weak evidentiary selection.
- Virtualisation helps snapshotting but can create very large analysis workloads.
- Presentation must clearly explain what was acquired directly, what came from the CSP, and what remained uncertain.
