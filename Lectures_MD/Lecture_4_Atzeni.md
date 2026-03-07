# Lecture 4 – Investigation Phases: Identification & Collection
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/03_investigation_phases.pdf`

---

## Overview
This lecture introduces the **five-phase framework** for digital forensic investigations, then covers the first two phases — **Identification** and **Collection** — in detail. The framework is presented as a conceptual tool rather than a rigid standard, with references to how various national and international standards map to similar (but not identical) phase structures.

---

## 1. Investigation Phases – Overview

The investigation phases are a **conceptual framework**, not an inherently valuable structure. Their purpose is to:
- Help practitioners understand *what to do* and *why* at each stage
- Identify subtleties that could compromise evidence if overlooked
- Provide a mental model for approaching any investigation

### Why Phases May Differ Across Standards
Many forensic standards exist worldwide (ACPO, NIST, ISO, country-specific guidelines), and they often prescribe slightly different phase structures:
- Some define **4 phases** (e.g., NIST: Collection, Examination, Analysis, Reporting)
- Some **merge** phases (e.g., collection and acquisition treated as one)
- Some use different terminology for the same conceptual steps

The goal is to understand the **underlying concepts**, not to memorise a specific standard's list.

### Prof. Atzeni's Five-Phase Framework

| Phase | Name | Core Activity |
|-------|------|---------------|
| 1 | **Identification** | Recognise sources of evidence without disturbing them |
| 2 | **Collection** | Physically or logically secure and gather identified evidence |
| 3 | **Acquisition** | Create forensically sound copies using trusted tools in a secure lab |
| 4 | **Examination / Evaluation** | Correlate evidence, build timeline, extract findings |
| 5 | **Presentation / Reporting** | Communicate results tailored to the intended audience |

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Investigation Phases Overview*

### Referenced Standards
| Standard | Notes |
|----------|-------|
| **ACPO Guidelines (UK)** | Highly influential historically; shaped investigations worldwide |
| **NIST SP 800-86** | Open-source, freely accessible; 4-phase model: Collection, Examination, Analysis, Reporting |
| **ISO/IEC 27037** | Structured but sometimes less practically useful; requires paid access |
| **Mobile Forensics Standards** | Specific standards for mobile device acquisition |
| **SWGDE Guidelines** | Scientific Working Group for Digital Evidence |

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Forensic Standards*

---

## 2. Phase 1 – Identification

**Identification** is the process of recognising all relevant sources of information (potential evidence) without yet acquiring or modifying them.

### What Happens in Identification
- Enumerate all **devices, systems, and locations** that may contain evidence related to the suspect/incident
- Assign a **tentative relevance level** to each identified source
- Understand the **volatility** of each source (how quickly the data may change or disappear)
- Plan the **order of acquisition** based on volatility and relevance

### Pre-Scene Investigation (OSINT Phase)
Before physically attending a crime scene, investigators can gather information through:
- **OSINT** (Open Source Intelligence): publicly available information about a suspect
- **Social media intelligence**: behaviour patterns, social connections, posts
- **Corporate directories / internal monitoring**: for insider threat investigations
- **Network scans** (if operating under cover without alerting the suspect)
- **Surveillance photos / videos** of the scene (e.g., from security cameras or social media)

This pre-investigation helps formulate a **plan of action** before physically interacting with evidence that could be inadvertently disturbed.

#### Understanding the Suspect's Technical Level
Knowing whether the suspect is technically sophisticated informs the investigation approach:
- **Non-technical suspect**: unlikely to have installed logic bombs, anti-forensic tools, or modified OS components; standard tools and procedures likely sufficient
- **Technical suspect**: may have installed OS modifications, self-destructing tools, or specifically crafted environments; standard tools may produce manipulated output

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slides: Identification Phase*

### OSINT Tools for Identification

| Tool | Description | Cost |
|------|-------------|------|
| **Spiderfoot** | Python-based open-source OSINT tool; uses freely available data; no cost | Free |
| **Maltego** | Correlates and visualises OSINT data; free version is limited | Commercial (free tier) |
| **Shodan** | Search engine for internet-connected devices; finds open ports, services, and associated data | Commercial |

#### Practical Use Cases
- Check if an email address has appeared in a **known data breach** (via Spiderfoot/Maltego)
- Identify which IPs are associated with a **DNS name** and when the domain was registered (newly registered domains are frequently malicious)
- Build a **behavioural profile** of a suspect or organisation

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: OSINT & Pre-Investigation Tools*

### Volatility – Prioritising Evidence
Evidence sources have varying **volatility** — the speed at which they can change, be overwritten, or become inaccessible.

**General volatility order (most volatile first):**
1. CPU registers and cache
2. **RAM / main memory** — lost on power-off; may contain running processes, encryption keys, active network connections
3. **Network state** — open connections, listening ports (lost within seconds to minutes)
4. **Running processes and logged-in users**
5. File system **temporary files** and **recently deleted files** (can be overwritten quickly)
6. Hard drive / SSD data (longer-lived but can be overwritten)
7. Remote logs, cloud data (may be retained for days to months)
8. Backups, archival media (most stable)

**Practical implication**: a running system should be treated differently from a powered-off one. If encryption keys are known to exist in RAM, powering off the device will destroy them.

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Evidence Volatility*

### Covert Investigation Techniques (During Identification)
When the suspect is still unaware of the investigation, the investigator may:
- Connect to a **network node adjacent** to the target to capture traffic (Wireshark packet sniffing)
- Take **covert photographs/videos** of the suspect's workspace
- Interact via a **different account** on a shared corporate machine
- Use administrator access for **"routine maintenance"** to quietly inspect connected devices, open files, and network activity

#### Useful Examination Commands (Unix/Linux)

| Command | Purpose |
|---------|---------|
| `lsusb` | List USB-connected devices |
| `lsblk` | List all block storage devices mounted on the system |
| `mount \| grep '^/dev'` | Show physically mounted devices |
| `lsof` | List all open files (including network connections) |
| `netstat -tulnp` | Display active network connections and listening ports |
| `ps aux` | List all running processes |
| `nmap` (on another node) | Network scan to identify open services on the suspect's device |

**Caution**: running any command on the suspect's system may modify metadata. These commands are appropriate only in specific contexts — for example, during a covert investigation with the system still in normal operation.

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Covert Investigation Commands*

### Worked Scenario: Insider Threat
In an organisation where an employee is suspected of exfiltrating sensitive financial documents via a USB drive:

**Pre-identification actions:**
- Collect publicly available information on suspect employees
- Consult corporate directory and internal monitoring dashboards
- Use Spiderfoot/Maltego to check for email breaches or associated malicious domains

**On-scene identification:**
- Document all devices visible on the suspect's desk (pen drives, laptop, mobile, external drives)
- Observe what is connected and what is powered, without touching
- Correlate with prior intel (e.g., the suspect ordered a specific brand of pen drive online — if that brand appears on the desk, it becomes a higher-priority evidence target)

---

## 3. Phase 2 – Collection

**Collection** is the process of physically or logically securing and gathering the identified evidence sources — fully initiating the **chain of custody** documentation.

### Key Distinguishing Feature vs. Identification
- **Identification**: observe and enumerate without modifying
- **Collection**: actively secure, physically or logically seize, and place under custodial control

> *Key risk at this phase*: **Data loss** — which can be intentional (suspect destroying evidence) or accidental (investigator inadvertently altering metadata)

### Isolation – Preventing Further Evidence Modification or Destruction

#### Physical Isolation
- Remove the suspect from physical access to the devices
- Place devices under physical custody

#### Logical / Network Isolation
All **network connections** to and from the suspect's devices must be severed:

| Direction | Risk if Not Severed |
|-----------|---------------------|
| **Ingress** | Remote commands can trigger self-destruction, encryption, or selective deletion of evidence |
| **Egress** | The suspect (or malware) can continue exfiltrating data or send an "alarm" to external accomplices |

Isolation actions include:
- Modifying **firewall rules** at the gateway
- Changing **security group settings** in cloud/virtualised environments
- Modifying **network topology** to isolate the target segment

> *The optimal result of the identification phase is a complete graph of all contact points between the suspect's devices and the external world — this graph is used to design the isolation procedure.*

#### Remote Wipe Prevention
Modern mobile devices support **remote wiping** — the ability to erase all content via a remote command. To prevent this:
- Use a **Faraday bag or RF jammer** to block wireless and cellular signals immediately upon seizure
- This prevents the device owner from issuing a remote wipe command

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Collection & Isolation*

### Physical Handling of Evidence
Different physical media require different handling:
- **Magnetic drives**: shield from strong magnetic fields (can alter stored bits)
- **SSDs / NAND flash**: less susceptible to magnetic damage, but sensitive to electrical discharge
- **Optical media (CD/DVD/Blu-ray)**: do not touch the reflective surface; fingerprints reduce optical readability
- **RAM modules**: optionally place in a **cryogenic container** (at approx. −196°C) to preserve transistor charge and allow later extraction of RAM content in the lab

### Chain of Custody – Starting the Record
At the beginning of the collection phase, the **chain of custody record** must be initiated and maintained continuously:

**What to record for each device/artefact:**

| Field | Description |
|-------|-------------|
| Date and time of collection | Exact timestamp (including timezone) |
| Device identifier | Make, model, serial number, unique identifiers |
| Physical condition | Photographs and written description of the device state |
| Collector identity | Full name of the person performing the action |
| Physical location | Where the collection occurred |
| Witnesses present | Names of all personnel present during the action |
| Transfer events | Every subsequent movement of the evidence with identities and timestamps |

**Common historical error**: collecting multiple USB drives or mobile phones of the same manufacturer/model without noting their individual serial numbers — making it impossible during examination to associate data with a specific device.

### Write Blockers (Review)
Hardware write blockers are typically deployed during the **collection-to-acquisition handoff** when connecting devices to the forensic workstation. Their role was explained in Lecture 2.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Identification phase** | Recognising and inventorying all potential evidence sources without modifying them |
| **Collection phase** | Physically and logically securing identified evidence and initiating chain of custody |
| **Volatility** | The rate at which a data source can be lost or modified; determines acquisition priority |
| **OSINT** | Open Source Intelligence — intelligence gathered from publicly available sources |
| **Isolation** | Severing all physical and logical connections to evidence to prevent modification or destruction |
| **Remote wipe** | Feature allowing a device owner to delete all data on a device via remote command |
| **Faraday bag** | RF-shielding bag that blocks all wireless signals, preventing remote wiping or communication |
| **Covert investigation** | An investigation phase conducted without alerting the suspect |
| **Spiderfoot** | Open-source OSINT tool for correlating publicly available information about a target |
| **Maltego** | Commercial OSINT visualisation and correlation tool |
| **Shodan** | Search engine for internet-connected devices; useful for identifying attack surfaces |
| **Cryogenic acquisition** | Preservation of RAM modules at near-absolute zero temperatures to maintain transistor state for laboratory extraction |

---

## Summary

- The **five investigation phases** (Identification → Collection → Acquisition → Examination → Presentation) provide a structured mental model for approaching forensic investigations; they are conceptual, not rigid.
- **Identification** precedes any physical contact with evidence: the investigator builds a picture of the environment through OSINT and covert methods.
- **Volatility** determines which evidence must be acquired first; RAM and network state are the most perishable.
- **Collection** secures evidence both physically and logically — network isolation and remote wipe prevention are critical to prevent evidence destruction at this stage.
- **Chain of custody** documentation begins the moment any evidence is touched and must be maintained unbroken until the investigation concludes.
- Write blockers, jamming/shielding of wireless devices, and forensically sound handling procedures are non-negotiable best practices.
