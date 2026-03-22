# Chapter 5 – Scene Assessment and Data Source Identification

**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.pdf`]  
**Covered in Lectures:** Lecture 7

---

## Introduction

Before a single device is touched, before a write blocker is connected, and before any acquisition begins, a skilled digital forensics investigator must perform systematic **scene assessment and data source identification**. This phase operationalises the first two of the five investigation phases — **Identification** and **Collection** — at the practical level of an actual scene.

The core intellectual challenge of this chapter is not technical but strategic: given an unknown environment, how does an investigator quickly establish what data sources exist, which are most fragile, and how to approach each of them without destroying the very evidence being sought? The answers depend on OSINT work done before arriving at the scene, the skill level of the suspect, the cooperative or adversarial stance of surrounding parties, and the physical and logical perimeter of the incident.

> 📝 *The theoretical five-phase framework into which this chapter fits is covered in [03_investigation_phases.md](03_investigation_phases.md).*  
> 📝 *Write blocker tools used during the acquisition phase that follows this chapter are covered in [04_Write-Blocker-Tools.md](04_Write-Blocker-Tools.md).*

---

## 1. Pre-Analysis: OSINT

### 1.1 Purpose

**Open Source Intelligence (OSINT)** is intelligence gathered from publicly available sources without actively probing or interacting with the target systems. Conducting OSINT before attending a scene allows the investigator to:

- Understand the suspect's technical infrastructure.
- Identify the likely boundaries of the investigative perimeter.
- Form initial hypotheses about which data sources to prioritise.
- Reduce the risk of making incorrect assumptions on arrival.

OSINT is strictly **passive** with respect to the target: no packets are sent to the suspect's systems, no accounts are accessed without authorisation, and no interaction takes place that could alert the subject or trigger countermeasures.

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Pre-Analysis and OSINT*

### 1.2 OSINT Techniques and Sources

#### Domain and Network Infrastructure

| Source | What It Reveals | Tools |
|--------|-----------------|-------|
| **Whois records** | Domain registrar, registration date, registrant contact, name servers; registration history can reveal how long an infrastructure has been active | `whois` CLI; public Whois web services |
| **DNS records (A, MX, NS, TXT)** | IP addresses associated with the domain; mail server configuration (MX); name servers; SPF/DKIM entries that imply email infrastructure | `dig`, `nslookup`; online DNS lookup services |
| **IP geolocation** | Approximate physical location of servers linked to the domain; useful for establishing jurisdictional context | Public IP-geolocation APIs |

#### Suspect Profile

| Source | What It Reveals | Notes |
|--------|-----------------|-------|
| **LinkedIn** | Employment history, skills, professional connections, "open to opportunities" / "in transition" language that may indicate intent to change organisations | Increasingly restricted by API limitations |
| **X (formerly Twitter), Facebook** | Public statements, associations, location check-ins, timestamps | Declining usefulness as platforms restrict automated access |

#### Network Topology (Passive)

- `nmap` against the suspect's network ranges to enumerate open ports, services, and OS fingerprints; useful for understanding what software and systems the suspect runs.

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — OSINT Sources and Tools*

### 1.3 Current Limitations of OSINT

OSINT effectiveness is **declining** for social media sources due to:

1. **API monetisation**: major platforms (X, Reddit, Meta) have moved data access behind paid commercial APIs, limiting what automated tools can retrieve.
2. **Declining personal content**: as influencer and advertising content displaces personal posts, the signal-to-noise ratio for investigative purposes decreases.
3. **Increased privacy awareness**: suspects and targets are more likely to configure accounts as private.

Despite these trends, OSINT remains valuable, particularly for infrastructure reconnaissance (domain, DNS, IP) which remains largely open.

---

## 2. Establishing the Investigative Perimeter

### 2.1 The Perimeter Concept

The **investigative perimeter** is the complete set of physical and logical resources that may contain evidence relevant to the investigation. Defining it upfront — even if it later requires revision — prevents both **under-collection** (missing critical sources) and **over-collection** (examining data the warrant does not authorise, which can invalidate findings).

The analogy to risk analysis is explicit: just as risk analysis begins with defining the scope of what is being assessed, forensic investigation begins with defining the boundary of what will be examined.

### 2.2 Physical Perimeter

| Element | Examples |
|---------|---------|
| **Primary computing devices** | Laptop, desktop workstation, server |
| **Mobile devices** | Smartphones, tablets, smartwatches |
| **Removable media** | USB drives, external HDDs, SD cards, optical media |
| **Peripheral devices** | Printers, scanners, NAS, IoT devices, smart TVs (see §5.2) |
| **Physical locations** | Home office, employer workplace, co-working space, residence |

### 2.3 Logical Perimeter

| Element | Examples |
|---------|---------|
| **Local network infrastructure** | Wi-Fi router, Ethernet switches, DHCP server, gateway firewall |
| **Internal servers** | File shares, email servers, intranet portals, document management systems |
| **Cloud storage and services** | Dropbox, Google Drive, OneDrive, iCloud; any SaaS the suspect used |
| **Email** | Corporate Exchange/Office 365; personal Gmail/ProtonMail; webmail access from corporate network |
| **ISP and carrier records** | Network traffic metadata, IP address assignments from the ISP; mobile carrier call/data records |
| **Third-party logs** | Web server access logs for sites the suspect administered; CDN logs |

**Example application:** If the suspect regularly connected to a corporate Wi-Fi, the logical perimeter includes the Wi-Fi controller, the DHCP lease logs, and the border firewall/proxy logs for that network segment — even though none of these are "the suspect's devices."

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Establishing the Perimeter*

---

## 3. Context-Dependent Approach

No single investigative procedure applies to all cases. Three major contextual factors shape how the scene assessment proceeds:

### 3.1 Suspect Skill Level

| Skill Level | Implication |
|-------------|-------------|
| **Low-skill suspect** | It is generally safe to briefly review the running environment (active connections, running processes) before shutdown. The risk of triggered countermeasures is low. |
| **High-skill suspect** | The device may have active countermeasures: dead-man's switches that trigger a wipe on unexpected input, encrypted volumes that auto-lock on VPN disconnect, scripts monitoring for analyst tool signatures. Approach with extreme caution; any interaction may be destructive. |

### 3.2 Suspect Role within the Target Organisation

| Scenario | Recommended Approach |
|----------|----------------------|
| Suspect is **an employee** damaging the organisation | System administrator is likely fully cooperative; contact them for credentials, logs, and technical context |
| Suspect is **the system administrator** | The sysadmin may be a co-conspirator; do not alert them; seek internal escalation or external legal compulsion |
| Suspect is the **owner or executive** | Entire IT department may be aligned with the suspect; obtain records via independent legal channel (e.g., directly from ISP or cloud provider) |

### 3.3 Cooperative vs Adversarial Context

- In a **corporate internal investigation**, the HR/legal team may have pre-positioned evidence (e.g., email monitoring logs) that can be collected immediately.
- In a **criminal investigation**, warrants control what can be collected and from whom; timing and sequencing of approach must preserve the element of surprise to prevent destruction of evidence.

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Context-Dependent Investigation Approach*

---

## 4. Volatility-Based Evidence Prioritisation

### 4.1 Volatility Order

Evidence sources differ enormously in how long they persist. The fundamental rule is: **acquire the most volatile evidence first**. Every minute of delay increases the probability of irreversible loss.

| Priority | Evidence Source | Persistence | Notes |
|----------|----------------|-------------|-------|
| 1 | CPU registers, CPU cache | Microseconds after power-off | Rarely recoverable in practice |
| 2 | RAM (system memory) | Seconds to minutes after power-off | **Cold-boot attack** can extend this; RAM imaging must be first if encryption keys are needed |
| 3 | Active network connections | Disappear on disconnect or power-off | Record with `netstat -an`, `ss -antp`, `arp -a` |
| 4 | Running processes and open file handles | Lost on shutdown | `ps aux`, `lsof`, `/proc` filesystem |
| 5 | Temporary files, application buffers | May be deleted on orderly shutdown | Word/Office auto-recovery files; browser cache |
| 6 | Persistent storage (HDD/SSD) | Survives power-off | Degraded only by overwriting; image with write blocker |
| 7 | Remote/cloud data | Subject to third-party retention policies | May be purged on a schedule; access can be revoked by suspect |
| 8 | External logs (ISP, CDN, email server) | Retention period varies; legal request needed | Hours to months; depends on provider retention policy |

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Volatility Order*

### 4.2 Background Processes That Modify Persistent Storage

Even after identifying a device, the clock is ticking: **background processes on a live system continuously modify persistent storage** even with no user interaction:

| Background Process | Storage Impact |
|--------------------|----------------|
| Cloud sync daemons (Dropbox, OneDrive) | May upload, download, or modify local sync state continuously |
| Application auto-recovery (Word, LibreOffice) | Creates/updates `.tmp` files on every keystroke |
| System indexing (`mlocate`, Windows Search) | Reads and catalogues new files; updates index database |
| Antivirus real-time scanning | Modifies access timestamps; may quarantine or delete suspected files |
| Log rotation daemons | May overwrite or compress old log files |

This is a further argument for minimising the time between identifying a device and beginning write-blocked acquisition.

**Temporary files** deserve specific attention: productivity applications (e.g., word processors) create auto-recovery `.tmp` files on every open document. These are highly evidential — and if deleted, may still be recoverable via file carving, since deletion only marks the space as free without erasing the content. A forensic investigator can compose multiple approaches: file carving of unallocated space may reveal deleted temp file data that was never visible to the OS.

**Hidden data** can also be found in filesystem structures that normal user tools do not expose: **slack space** (unused portion of the last allocated cluster of a file) and **reserved sectors** may contain data fragments from previous files.

---

## 5. Data Sources

### 5.1 Remote and Cloud Evidence

| Location | Characteristics | Challenge |
|----------|----------------|-----------|
| **Local (seized device)** | Fully under investigator control once seized | Straightforward with write blocker |
| **Organisational server** (under investigative organisation's control) | Accessible with internal cooperation | Manageable |
| **ISP / carrier records** | Network-layer metadata; IP address assignments; call records | Requires legal request; usually cooperative within 24–72 h in many jurisdictions |
| **Cloud provider** (multinational) | Data is under a foreign company's jurisdiction; may span multiple countries | Most challenging: provider may decline, legal process takes weeks, jurisdiction conflicts may arise |

For cloud evidence, the optimal tactic is to capture **live session tokens from RAM** before the suspect is informed of the investigation. Once aware, the suspect can:
- Revoke active sessions.
- Change credentials.
- Delete cloud-stored files.

After revocation, even a valid court order directed at the provider may take weeks to process — and may ultimately fail due to jurisdictional complexity or provider policy.

> *"Even with powerful technical means, attempting to access cloud evidence without either provider cooperation or suspect cooperation might be finally not possible."*

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Remote and Cloud Evidence Sources*

### 5.2 Peripheral Devices as Evidence Sources

The investigative perimeter must not be limited to the primary computing device. Any peripheral that interacted with the suspect's data flow is a potential evidence source:

| Peripheral | Possible Evidence | Why It Is Often Overlooked |
|------------|------------------|---------------------------|
| **USB drives** | File system metadata: copy timestamps of transferred files; deleted files in unallocated space | Small, easily missed at scene |
| **External HDDs** | Full file system image; deleted files; volume shadow copies | Often present but not immediately visible |
| **NAS (Network-Attached Storage)** | Full directory listing; access logs; file modification history | Requires network access or on-site inspection |
| **Printers** | Memory buffer holding last-printed document(s); print job log | Very commonly overlooked; can contain highly incriminating printed material |
| **Scanners / MFPs (Multi-Function Printers)** | Memory buffer of last scanned document(s); scan job history | Same as printers |
| **Any unusual peripheral** | Any device that interacted with the suspect's data flow — including unusual or unexpected ones — may hold evidence | Easy to dismiss as unimportant; should always be enumerated |

> *"Printers and scanners are a funny example, but the rule is: try to understand all the possible, even unusual, peripherals attached or that performed any kind of interaction during the last hours or days."*

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Data Sources: Peripheral Devices*

---

## 6. On-Scene Documentation

### 6.1 Photograph and Video First

Before any device is moved, unplugged, or interacted with:
- **Photograph every device in situ** — its physical position, screen state (on or off), cable connections, orientation.
- Photograph the **screen contents** if the device is on (may show logged-in user, active applications, last accessed files).
- Use video to document the physical environment as a whole before individual items are bagged.
- All photographs must be **timestamped** by the camera and logged in the chain-of-custody record.

This photographic documentation is typically required by forensic Standard Operating Procedures and forms part of the official investigation file submitted in legal proceedings.

### 6.2 Chain of Custody — First Contact

The chain of custody record begins at the exact moment of first physical contact with each evidence item:

| Field | Example Value |
|-------|--------------|
| Item identifier | EV-007 |
| Description | Samsung 870 EVO 1TB SSD, S/N S4XXXXX |
| Location found | Suspect's desk, top-right drawer |
| Date / time of first contact | 2026-03-14 09:47:32 UTC |
| Handler name | [Examiner full name] |
| Condition on receipt | Powered off; no visible physical damage |
| Transfer to | Secure evidence bag #SEB-007A |

Every subsequent transfer or interaction is added as a new line. No gap in the chain is permissible.

---

## 7. Structured Documentation: Topology and Asset Inventory

Investigators must produce structured, queryable documentation of all identified evidence sources from the earliest phase. This is not just useful — it is necessary for:
- **Anomaly detection**: a node that appears in network logs but is not in the asset inventory flags an unexpected device.
- **Cross-referencing**: correlating a MAC address seen in a firewall log with a specific device.
- **Team communication**: other investigators can understand the environment without a full briefing.
- **Gap identification**: seeing which nodes are documented allows identification of what is missing.

### 7.1 Network Topology Diagram

| Content | Minimum Required Detail |
|---------|------------------------|
| Network nodes | All devices visible on the suspect's network(s) |
| IP addresses | Static and DHCP-assigned; timestamp of assignment |
| MAC addresses | For all identifiable hosts |
| Connections | Physical and WiFi; switch/AP through which each device connected |
| Anomalies | Any device present on only one day; unusual external connections |

### 7.2 Asset Inventory Database

A structured database (even a spreadsheet) with one row per evidence item:

| Column | Example |
|--------|---------|
| Evidence ID | EV-007 |
| Device type | SSD (internal) |
| Make / Model | Samsung 870 EVO 1TB |
| Serial Number | S4XXXXX |
| MAC Address | N/A (internal storage) |
| IP Address | N/A (internal storage) |
| Physical Location | Workstation case, bay 1 |
| Chain of custody reference | SEB-007A |
| Date/time of seizure | 2026-03-14 09:47 UTC |

When the database is structured, simple queries can answer questions such as: "Which device had IP 192.168.1.45 at 14:32 on the day of the incident?" — answers that would require manual file searches without this structure.

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Documentation: Network Topology and Asset Inventory*

---

## 8. Proposed Scene Assessment Workflow

The following workflow is a baseline framework, customisable per investigation:

```
Phase 0 — Pre-Analysis (Before Scene Arrival)
├── OSINT: Whois, DNS, IP geolocation, social media, nmap (authorised)
├── Map preliminary logical perimeter (domains, IPs, cloud services)
└── Assess suspect's technical skill level based on available information

Phase 1 — Scene Arrival
├── Do not interact with any device immediately
├── Photograph / video all devices in situ before any action
├── Assess power state of each device (on / off / sleep)
└── Brief all team members on context and approach before proceeding

Phase 2 — Volatile Data Capture (if devices are live)
├── Photograph screen contents of all live devices
├── Capture RAM image (highest priority if full-disk encryption detected)
├── Document active network connections and routing table
├── Document running processes and open file handles
└── If suspect is unskilled: brief interaction with live environment acceptable
    If suspect is skilled: extreme caution; consider immediate controlled shutdown

Phase 3 — Isolation
├── Mobile devices → Faraday bag immediately (block remote wipe)
├── Wired devices → network cable disconnection
└── Document each isolation step with timestamp

Phase 4 — Physical Evidence Collection
├── Photograph each device before and after disconnection
├── Bag and tag each item; start chain of custody record at first contact
├── Document all peripherals: printers, scanners, NAS, USB drives
└── Identify cloud services in use on live devices (for prioritised legal requests)

Phase 5 — Asset Inventory Construction
├── One record per evidence item: type, make, model, serial number, location
├── Build or update network topology diagram
└── Identify and flag any anomalous devices (in logs but not physically found)
```

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Investigation Workflow Summary*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **OSINT** | Open Source Intelligence — intelligence gathered from publicly available sources without actively probing the target |
| **Investigative perimeter** | The complete set of physical and logical resources potentially containing evidence; defined before the investigation begins and updated as new sources are discovered |
| **Volatility order** | The sequence in which evidence sources must be acquired, from most transient (CPU registers, RAM) to most persistent (archived logs, cloud data) |
| **Dead-man's switch** | A countermeasure configured by a technically skilled suspect that triggers destructive action (e.g., secure wipe) when an unexpected event occurs (power loss, loss of network, input from unknown device) |
| **DHCP lease log** | A record from the DHCP server of which IP address was assigned to which MAC address at what time; critical for correlating IP-level log entries to specific devices |
| **Faraday bag** | An RF-shielded enclosure that blocks all wireless signals; used to prevent remote wipe commands from reaching a seized mobile device |
| **Cloud session token** | An authentication credential held in RAM on a live system that grants access to a cloud account; capturing it during live acquisition may allow investigators to access cloud evidence before the suspect revokes access |
| **Network topology diagram** | A visual map of all nodes, connections, IP/MAC addresses, and data flows in the suspect's network environment; used for anomaly detection and cross-referencing |
| **Asset inventory** | A structured record of every evidence item, including identity, location, custody history, and technical specifications |
| **SOP (Standard Operating Procedure)** | A documented, stepwise procedure derived from a recognised forensic standard that prescribes exactly how the scene assessment and collection must be conducted to remain court-compliant |

---

## Summary

- **OSINT precedes scene arrival**: use Whois, DNS, social media (LinkedIn, Facebook, X), and `nmap` to map the suspect's infrastructure and skill level before touching any device.
- The **investigative perimeter** has a physical dimension (devices, locations) and a logical dimension (networks, cloud, ISP records); both must be explicitly defined to avoid under-collection or over-collection.
- The approach must adapt to the **skill level of the suspect** and the **cooperative or adversarial stance** of parties with access to infrastructure (system administrators, cloud providers).
- Evidence must be acquired in **volatility order**: RAM and active connections before persistent storage; cloud session tokens before the suspect is alerted.
- **Cloud evidence** is the most challenging category: session tokens should be captured from live RAM; after suspect awareness, access may be permanently revoked.
- **Peripheral devices** (especially printers and scanners) are recurring overlooked sources: they may retain last-used document memory and print/scan job logs.
- **Documentation starts at first physical contact**: photographs in situ, Faraday bag for mobile devices, chain-of-custody record from moment of seizure.
- A **network topology diagram** and **asset inventory database** should be built from the identification phase onward to enable anomaly detection and cross-source correlation.
- The entire process must follow a documented **Standard Operating Procedure** compliant with a recognised forensic standard (ISO/IEC 27037, NIST SP 800-86, ACPO) to ensure court admissibility.
