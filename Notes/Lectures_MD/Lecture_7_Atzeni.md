# Lecture 7 – Write Blocker Tools & Scene Assessment

**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:**
- `Slides/Atzeni/04_Write-Blocker-Tools.pdf`
- `Slides/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.pdf`

---

## Overview

Lecture 7 opened with a brief collaborative discussion of the ongoing case study (the "ShockWave" scenario distributed the previous week), revisiting student hypotheses, evidence chains, and constructed timelines before the full case debrief scheduled for the following session. The bulk of the lecture then focused on two practical topics. The first was **write blocker tools**: the rationale for their use, the distinction between hardware and software blockers, representative commercial products, common configuration errors, and documentation requirements. The second was **scene assessment and data source identification**: how to prepare before arriving at a scene, how to establish the investigative perimeter, OSINT techniques, the handling of volatile evidence, and how to document the environment using network topology diagrams and asset inventories.

---

## 1. Case Study Brief Session — Recap & Hypotheses

Before moving to new material, Prof. Atzeni invited the class to share initial thoughts on the case study distributed the previous week. The educational objective was emphasised:

> *"An infinite amount of reasonable cases is possible starting from this one. What is the educational outcome is reflecting on what you can find, how you can approach the case."*

Key principles reinforced during the discussion:

- Any logically consistent storyline is acceptable: the evidence set is abstract enough to support multiple valid hypotheses.
- A hypothesis is made credible by tracing a reproducible chain from the initial premise through the evidence items to the conclusions — "I was able to find this piece of evidence, therefore I can conclude X."
- The exercise also involves constructing a **timeline** that correlates discovered artefacts with timestamps.
- The full debrief of the case study was deferred to the following session.

---

## 2. Write Blocker Tools

### 2.1 Purpose and Rationale

A **write blocker** is a device or software configuration that prevents any write operation from reaching an evidence storage device during acquisition or analysis. Its use is mandatory when handling original evidence for three reasons:

| Requirement | Explanation |
|-------------|-------------|
| **Technical soundness** | Guarantees that no bit in the evidence has been altered during handling — including both file content and metadata |
| **Legal admissibility** | Demonstrates to the court that the chain of manipulation was controlled; each party (including opposing counsel) was able to predict the exact outcome |
| **Repeatability** | If every step of the acquisition is documented and write-blocked, another examiner using the same hardware and procedure will produce a bitwise-identical result |

Even a **single bit modification** is enough to invalidate the entire subsequent analysis: it breaks the hash match and renders the evidence legally inadmissible, regardless of how minor the semantic effect might be.

> *"This can be pretty frustrating — the modification of just one bit, completely fine from the perspective of the semantic content of my file, is nonetheless no longer admissible after weeks of analysis."*

Write protection is also critical for **metadata**. File-level metadata (access time, modification time, creation time) is modified by routine OS operations even without user interaction. This matters because metadata is often the primary source of timeline evidence.

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Why Write Blockers Are Required*

---

### 2.2 Hardware Write Blockers

Hardware write blockers are the preferred solution in forensic practice — both technically and legally.

#### Categories

| Category | Description |
|----------|-------------|
| **Pure (dependent) write blocker** | A small passive device that intercepts the bus between the evidence drive and the analysis workstation. Has no OS of its own; requires an external computer to initiate and manage the copy. |
| **Standalone write blocker** | A self-contained unit with an embedded (minimal, hardened) Linux OS that can perform the full acquisition independently, without an external laptop. Typically larger and more expensive. |

Standalone units mount a deliberately stripped-down Linux build: a minimal kernel with no known bugs and the least possible feature surface, reducing the risk of unexpected OS interaction with evidence.

#### Representative Products

| Vendor | Product Range | Notes |
|--------|---------------|-------|
| **Tableau** (Guidance Software / OpenText) | T8i, T35, and others (model varies by supported interface) | De facto legal standard; widely cited in court documentation; certified under specific forensic standards |
| **WiebeTech / RealTech** | Various models | Slightly lower price point; predominantly pure (non-standalone) write blockers; common in private labs; technically very reliable |
| **Logicube** | Duplicator series | Another well-known and widely deployed option |

The **Tableau T8i**, for example, does not support some older interface types; the exact model determines which port types are available. This makes model documentation critical (see §2.4 below).

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Hardware Write Blockers: Products and Interfaces*

---

### 2.3 Software Write Blockers

A **software write blocker** is a properly configured OS environment that restricts all write access to the evidence drive at the kernel or application level. Two forms exist:

1. **OS configuration**: correct mount options, kernel parameters, and system policies that suppress write-path system calls.
2. **Privileged application**: a forensic tool running with root/administrator privileges that intercepts device I/O and enforces a read-only policy.

#### Mounting under Linux — a practical example

Mounting a file system with `-o ro` (read-only) is **not sufficient** on its own:

```bash
# Insufficient — may still alter file-system journal metadata:
mount -o ro /dev/sdb1 /mnt/evidence

# Correct — adds 'noload' to suppress journal replay:
mount -o ro,noload /dev/sdb1 /mnt/evidence
```

The `noload` (or `norecovery`) flag prevents the kernel from replaying the ext3/ext4 journal after mounting. Without it, the OS may write journal-commit metadata to the device even in nominal read-only mode — silently corrupting the evidence integrity.

> *"I need to understand very well many details of how the operating system works to avoid any unwanted modification — that's why the pure software approach is very challenging and hardware write blockers are preferred by far."*

**Legal standing**: software write blockers are significantly harder to defend in court because they require the examiner to demonstrate deep and specialised OS knowledge about every edge case that might have introduced a write. Courts strongly prefer hardware devices whose internal design and certifications are independently verifiable.

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Software Write Blockers and Mount Options*

---

### 2.4 Documentation Requirements

Every component involved in an acquisition must be meticulously documented. The documentation must be sufficient for a different examiner — possibly the opposing party's expert — to replicate every step.

#### Required documentation items

| Item | Why It Matters |
|------|----------------|
| **Device make, model, serial number** | The exact model defines which interfaces are available; a wrong model name makes the report non-reproducible |
| **Firmware version** | Different firmware versions of the same model may have different bugs or behaviours |
| **Firmware update history** | Updates may introduce or fix bugs that affect the acquisition process |
| **Mode of connection** | Which port type was used; how the drive was physically attached; any adapters used |
| **Photographs and/or video** | Visual record of each device, cable, connection, and step in the procedure |

A citation in the investigation report such as:

> *"Digital evidence was acquired using a Tableau T35 write blocker (serial number XXXX, firmware version Y.Z)"*

is considered professionally required and is reinforced by many forensic standards that certify specific products (including the Tableau range).

#### Common errors

| Error | Consequence |
|-------|-------------|
| **Connecting evidence drive directly to any workstation** (even briefly) | The OS immediately begins interacting with the device on plug-in, modifying metadata — even a momentary connection without a write blocker may be enough to corrupt the evidence |
| **Incorrect mount options** (e.g., omitting `noload` on Linux) | Journal replay silently writes metadata to the device |
| **Documenting the wrong write blocker model** | Opposing expert cannot replicate the acquisition; the chain of analysis is broken |
| **Not documenting the exact device connected** (confusing USB drive with old-format drive) | Same reproducibility failure as wrong model number |
| **Missing photographs of connection steps** | Visual record required by most forensic Standard Operating Procedures |

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Common Errors and Documentation Checklist*

---

### 2.5 Hashing

Hash verification after write-blocked acquisition is treated as part of the atomic acquisition step:

- Compute the hash of the **acquired image** immediately after imaging completes.
- Tools such as `dc3dd` integrate hashing into the imaging process atomically, removing the gap between imaging and hashing.
- For high-stakes cases, use **two independent hash algorithms** to provide defence-in-depth against any hash-collision argument.

---

## 3. Scene Assessment and Data Source Identification

### 3.1 Pre-Analysis: OSINT (Open Source Intelligence)

Before physically attending a scene or interacting with any device, a good investigator performs OSINT — gathering intelligence exclusively from **publicly available, freely accessible sources** without interacting with the target systems.

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — OSINT and Pre-Analysis*

#### OSINT Sources and Techniques

| Source | What It Reveals | Tool / Method |
|--------|-----------------|---------------|
| **Whois records** | Domain registration details, registrar, registration date, name servers | `whois` command; public Whois web services |
| **DNS records** | IP addresses, MX (mail server) records, NS (name server) records, SPF/DKIM entries | `dig`, `nslookup`; DNS lookup services |
| **IP geolocation** | Approximate physical location of servers | Public IP-geolocation APIs and services |
| **Social media** (LinkedIn, X, Facebook) | Suspect's professional history, associates, recent activity, "open to opportunities" language | Manual search across platforms |
| **Network scanning** | Open ports, detected services, OS fingerprinting on target network | `nmap` |

**Note on declining effectiveness:** Social media OSINT has become less effective in recent years as major platforms moved monetised API access behind paid tiers, reducing the ability of automated tools to collect profile data at scale. User content volume from non-commercial accounts is also declining as influencer and advertising content dominates platforms.

**Practical example using publicly available tools:**
- Query a domain's Whois record to find out its registration history, registrar, and linked name servers.
- Query DNS to discover IP addresses and mail server infrastructure.
- Combine IP geolocation data with social media activity to correlate the suspect's usual physical work locations with network infrastructure used.
- Use `nmap` to enumerate open ports and services on a network node to understand what software the suspect runs.

---

### 3.2 Establishing the Investigative Perimeter

Before any acquisition begins, the investigator must define the **scope**: every system, device, and data flow that may contain relevant evidence. This mirrors the scope-definition phase in risk analysis.

The perimeter has two dimensions:

| Dimension | Content |
|-----------|---------|
| **Physical** | The specific rooms, workstations, mobile devices, removable media, and peripheral devices the suspect used |
| **Logical** | Network segments, wireless access points, router/firewall logs, cloud services, remote storage, and any application-layer infrastructure involved in the suspected activity |

**Example:** If a suspect regularly connected to a specific corporate Wi-Fi, the investigative perimeter logically includes the Wi-Fi router, the DHCP server logs, and the gateway firewall logs for that network segment — even though those are not "the suspect's devices."

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Establishing the Perimeter*

---

### 3.3 Understanding the Suspect's Environment and Context

The investigation approach must adapt to the specific context of each case. Three key factors shape how the scene assessment proceeds:

#### 3.3.1 Skill Level of the Suspect
- **Low-skill suspect**: it may be safe to briefly interact with the running environment (e.g., quickly noting active network connections) without triggering countermeasures.
- **High-skill suspect**: the device may have active countermeasures that respond to investigator actions (e.g., a dead-man's switch that wipes evidence on unexpected input or network disconnect). In this case, extreme caution is required before any live interaction.

#### 3.3.2 Cooperative vs Adversarial Parties
- If the suspect is **damaging an organisation**, the system administrator is likely fully cooperative and can provide logs, credentials, and context.
- If the suspect **is** the system administrator, or the owner of the organisation, care must be taken not to alert them through official channels that could lead to evidence being destroyed.

#### 3.3.3 Active Network Connections
Where safe to do so, documenting active network connections at the time of seizure provides highly volatile evidence:
- Open TCP/UDP connections
- VPN tunnels
- Currently active authenticated sessions (cloud, email, intranet)

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Context-Dependent Approach*

---

### 3.4 Volatility-Based Prioritisation

The general principle is: **acquire the most volatile data first**, as its loss is irreversible once power is cut. The broader volatility hierarchy (from most to least transient):

| Order | Source | Notes |
|-------|--------|-------|
| 1 | CPU registers, CPU cache | Lost on power-off |
| 2 | RAM (system memory) | Lost on power-off; cold-boot attack extends retention |
| 3 | Active network connections and routing tables | Disappear on disconnect/power-off |
| 4 | Running processes | Lost on power-off |
| 5 | Open files and handles; temporary files | Temp files may be deleted on shutdown |
| 6 | Persistent storage (HDD, SSD) | Survives power-off; degraded only if overwritten |
| 7 | Remote logs and cloud data | Controlled by third parties; may be purged on a schedule |

Also note: **background processes** on a running system may be silently modifying persistent storage (cloud sync daemons, automatic temp-file creation by productivity applications, system indexing). Minimising the time between identifying a device and beginning write-blocked acquisition reduces this risk.

Additionally, **temporary files** — such as those created by word processors on every open document — may survive deletion and remain recoverable via file carving (since deleting a file only marks the space as free without erasing the content). Atzeni highlighted the investigative value of composing different techniques: *"we can compose our knowledge of forensic investigation merging different theoretical kinds of investigations in the same sequence in order to enrich the result"* — for example, recovering a deleted temp file that still contains partial document content.

**Hidden data** may also reside in filesystem structures beyond the main data area: **slack space** (the unused portion of the last cluster of a file) and **reserved sectors** are two examples of locations that standard OS read operations do not surface but forensic tools can examine.

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Volatility Order and Evidence Prioritisation*

---

### 3.5 Local vs Remote Evidence — Cloud Challenges

Evidence can reside in three principal locations:

| Location | Challenge |
|----------|-----------|
| **Local (physical device)** | Straightforward if device is seized; apply write blocker and image |
| **Organisational remote** (server still under the investigating organisation's control) | Manageable with internal cooperation |
| **Cloud** (third-party multinational provider) | Highly challenging: different jurisdiction, provider may decline to cooperate swiftly, suspect can revoke access at any time |

For cloud evidence specifically, a key tactic is **live acquisition of cloud session tokens from RAM** before the suspect is alerted. Once the suspect terminates their session or changes credentials, even a court order directed at the provider may take weeks and may ultimately fail due to jurisdictional complexity.

> *"Even with powerful technical means, access to cloud evidence without either provider cooperation or suspect cooperation might be finally not possible."*

---

### 3.6 Peripheral Devices

The investigative perimeter should not be limited to the primary workstation or mobile device. Any peripheral that interacted with the suspect's data is a potential evidence source:

| Peripheral | Possible Evidence |
|------------|------------------|
| USB drives | File copy/transfer artefacts; file system metadata; deleted files in unallocated space |
| Network-Attached Storage (NAS) | Full directory listings; network share access logs |
| **Printers and scanners** | Memory buffers holding last-printed or last-scanned documents; print job logs |
| Smart TVs / IoT devices | HDMI-over-IP session logs; streaming history; connected device logs |

Printers and scanners are highlighted as a "funny but real" example: they may retain the last few pages in memory and can produce significant evidence.

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Data Sources: Peripherals and Remote Locations*

---

### 3.7 Documentation: Network Topology and Asset Inventory

Investigators should produce **structured, queryable documentation** of all identified evidence sources from the earliest phase of identification. This serves multiple purposes:
- Allows quick cross-referencing during examination.
- Makes anomalies visible (e.g., a day with no log entries when all other days have them).
- Enables the team to check for missing components.

#### Recommended artefacts:

| Artefact | Content | Use |
|----------|---------|-----|
| **Network topology diagram** | All network nodes, connections, IP addresses, MAC addresses in the suspect's environment | Visual overview; highlights anomalous connections; identifies missing nodes |
| **Asset inventory database** | Each device with make, model, serial number, MAC address, IP address, physical location | Queryable; enables cross-referencing between timeline events and specific hardware |
| **Chain of custody record** | Each evidence item with a handling log from first contact onward | Legal requirement |

Both high-level (component-level network map) and low-level (serial numbers, MAC addresses) detail should be captured from the very first phase.

---

## 4. Proposed Investigation Workflow

Prof. Atzeni presented a summary workflow that can serve as a starting framework, customisable per case:

```
Pre-analysis
  └─ OSINT (Whois, DNS, social media, nmap)
  └─ Identify and map perimeter (physical + logical)

Scene Arrival
  └─ Photograph all devices in situ before touching
  └─ Assess suspect skill level → decide on live vs immediate shutdown
  └─ Capture volatile data (RAM, active connections) if applicable
  └─ Isolate devices (Faraday bag for mobile; network disconnect for workstations)

Identification & Collection
  └─ Document every item: model, serial, firmware
  └─ Begin chain of custody record at first contact

Acquisition
  └─ Write-blocked imaging of persistent storage
  └─ Hash verification immediately after imaging
  └─ Record all tools, models, and command parameters

Examination → Presentation
  └─ (Covered in Chapters 03 and 03_investigation_phases.md)
```

> 📎 *Slide reference: `05_Scene-Assessment-and-Data-Source-Identification.pdf` — Investigation Workflow Summary*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Write blocker** | A device or software configuration that prevents write operations on an evidence storage medium during forensic handling |
| **Pure write blocker** | A hardware write blocker with no internal OS; requires an external workstation to manage the acquisition |
| **Standalone write blocker** | A self-contained write blocker with an embedded OS that can perform acquisition independently |
| **`noload` / `norecovery`** | Linux mount options that suppress ext3/ext4 journal replay, preventing silent metadata writes during read-only mounting |
| **OSINT** | Open Source Intelligence — intelligence derived from publicly available sources without actively probing target systems |
| **Investigative perimeter** | The complete set of physical and logical resources that may contain evidence relevant to the investigation |
| **Volatility order** | The hierarchy of evidence sources from most ephemeral (CPU registers, RAM) to most persistent (cloud logs), used to determine acquisition sequence |
| **SOP (Standard Operating Procedure)** | A documented, stepwise procedure derived from a recognised forensic standard; defines exactly how an investigation must be conducted in a way that is court-compliant |
| **Temporal anomaly** | An absence, gap, or inconsistency in a timeline that may indicate tampering, deleted logs, or a device in a different time zone |
| **Faraday bag** | An RF-shielded enclosure that blocks all wireless signals, preventing remote wipe of seized mobile devices |

---

## Summary

- A write blocker is mandatory for any forensic acquisition; even a momentary direct connection without one risks permanently altering metadata and invalidating the evidence.
- **Hardware write blockers** are strongly preferred over software equivalents both technically and legally; Tableau, WiebeTech, and Logicube are the leading commercial products.
- **Standalone write blockers** embed their own minimal OS; **pure write blockers** depend on an external workstation.
- For software-based blocking under Linux, `mount -o ro` alone is insufficient; `noload`/`norecovery` must be added to suppress journal replay.
- Documentation must include make, model, serial number, firmware version, connection method, and photographic evidence for every device involved.
- **OSINT** (Whois, DNS, social media, nmap) should always precede physical scene approach to build a preliminary picture of the suspect's environment.
- The investigative **perimeter** has both a physical dimension (devices, rooms) and a logical dimension (network segments, cloud services, log sources).
- Evidence must be acquired in **volatility order**: RAM and active connections before persistent storage; cloud evidence before the suspect can revoke access.
- Even peripheral devices like printers and scanners are valid evidence sources; the rule is to enumerate every device that interacted with the suspect's data.
- Structured documentation (network topology diagram, asset inventory database) enables anomaly detection and cross-source correlation throughout the full investigation.
