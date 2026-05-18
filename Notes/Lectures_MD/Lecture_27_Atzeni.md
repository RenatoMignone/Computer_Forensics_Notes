# Lecture 27 – Cloud Forensics Effects and Acquisition Strategy
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/14_Cloud.pdf`

---

## Overview
This lecture continues the cloud forensics chapter. Atzeni focuses on how cloud peculiarities change each phase of a forensic investigation: identification, collection, acquisition, analysis, and presentation.

The central idea is that the investigator often cannot act as the physical owner or root administrator of the evidence environment. In cloud contexts, evidence is mediated by cloud service provider interfaces, contracts, logs, and cooperation.

---

## 1. Lack of Physical Access

> 📎 *Slide reference: `14_Cloud.pdf` — Cloud peculiarity effects*

In traditional investigations, the examiner may seize a device, disconnect it, image it, and operate with high privilege over the hardware. In cloud investigations, that model usually fails.

Most investigations cannot physically access the data centre. The investigator must instead request information from the cloud service provider or use the provider's APIs and tools. This affects:
- **identification**, because the provider may be needed to list processes, virtual machines, accounts, logs, and operations;
- **collection**, because API limits, contract limits, and shared infrastructure can slow or restrict access;
- **acquisition**, because physical bit-by-bit copying is usually replaced by snapshots, exports, or logical acquisition;
- **analysis**, because low-level artifacts may be missing or abstracted away;
- **presentation**, because the report must explain reliance on third-party data and provider-provided integrity information.

---

## 2. Provider Dependency and Tool Knowledge

Atzeni stresses that cloud investigations require concrete knowledge of the specific provider's tools and outputs. The examiner must understand not only that a log exists, but also its syntax, semantics, granularity, retention, and limitations.

Examples include:
- AWS CloudTrail or equivalent cloud audit logs;
- Azure Monitor or Google Cloud Logging;
- provider command-line tools and APIs;
- snapshot, clone, and export mechanisms;
- storage tools for object stores such as Amazon S3.

The provider acts as a powerful third party. Unless the provider itself is under suspicion, investigators often rely on provider cooperation, but this reliance must still be documented and made explicit.

---

## 3. Redundancy and the Primary Copy

Cloud redundancy can help evidence preservation because the same information may exist in multiple places. It also creates ambiguity: not every copy has the same forensic meaning.

Atzeni introduces the concept of a **primary copy**, meaning the authoritative or actively used instance from which backups or replicas derive. Identifying the primary copy matters because acquiring every redundant copy may waste time and resources, while acquiring only a secondary copy may miss relevant metadata or recent changes.

Indicators for primary-copy identification include:
- timestamps;
- replication tags or provider metadata;
- access logs;
- frequency of interaction;
- provider confirmation.

The chain of custody must document which copy was collected, why it was selected, and whether other replicas were checked or excluded.

---

## 4. Virtualisation

Cloud environments are virtualised. This can help acquisition because snapshots of virtual machines, disks, and sometimes memory can be created from outside the guest system.

The positive side is that external snapshotting may reduce direct interference with the target system. The negative side is practical scale: snapshots can quickly produce terabytes of data, and normal forensic operations such as carving or deep indexing may take days or weeks.

The examiner must also distinguish:
- assets owned only by the suspect;
- shared assets that include unrelated users' data;
- hypervisor-level information that only the provider can access;
- guest-level information that the customer may export directly.

---

## 5. Volatility in the Cloud

Cloud instances, containers, serverless functions, and logs may exist only briefly. Auto-scaling and maintenance can create and destroy resources without the investigator ever touching a stable physical device.

Atzeni presents two strategies:
- rapid acquisition through snapshots, memory dumps, and automated provider APIs;
- indirect reconstruction through logs, deltas between snapshots, and correlation with persistent evidence.

The report must be clear when evidence is missing because a volatile resource disappeared before acquisition. This is not merely a technical limitation; it is a point that can affect admissibility and certainty.

---

## 6. Cloud-Aware Forensic Tools

Modern forensic tools increasingly support cloud acquisition and cloud artifact parsing. Atzeni mentions that established tools have evolved from local-image analysis toward direct or semi-direct acquisition of provider data.

Examples include tools that can:
- acquire S3-like objects;
- use API credentials;
- import cloud logs;
- analyze virtual machine images;
- correlate cloud artifacts with local disk, memory, and network evidence.

This does not remove the need to understand provider semantics. A tool can download or parse an object, but the examiner must still explain what the object represents.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **CSP** | Cloud Service Provider, the third party controlling the physical and management layer of the cloud environment. |
| **Primary Copy** | The authoritative or actively used copy of an object or VM instance for forensic purposes. |
| **Replica** | A redundant copy created for availability, backup, recovery, or performance. |
| **Snapshot** | Point-in-time logical capture of a VM, disk, or storage resource. |
| **Infrastructure as Code** | Cloud management model where infrastructure can be created, changed, and acquired through scripts and APIs. |

---

## Summary
- Cloud forensics often lacks physical access and ordinary root-level control.
- Identification and collection depend on provider cooperation and provider-specific tools.
- Acquisition usually relies on snapshots, exports, APIs, and hashes rather than physical imaging.
- Redundancy can preserve evidence but requires careful primary-copy identification.
- Virtualisation enables useful snapshots but can create massive analysis workloads.
- Volatile cloud resources may disappear before acquisition.
- Cloud-aware tools help, but the examiner must still document semantics, limitations, and provider dependency.
