# Chapter 3 – Forensic Investigation Phases
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/03_investigation_phases.pdf`]  
**Covered in Lectures:** Lecture 4, Lecture 5

---

## Introduction
Digital forensic investigations are not freeform activities. They are structured into a defined sequence of phases, each with its own objectives, mandatory procedures, and documentation requirements. Adherence to a recognised model or standard is what transforms a technical examination into legally defensible evidence. This chapter covers the major international frameworks, then provides an in-depth treatment of each phase: Identification, Collection, Acquisition, Examination, and Presentation.

---

## 1. Forensic Investigation Frameworks and Standards

Several bodies have published guidelines defining forensic investigation phases. They converge on the same core activities despite using different terminology.

| Standard | Organisation | Phases |
|----------|-------------|--------|
| **ACPO Guidelines** | UK Association of Chief Police Officers | Influential UK standard; widely adopted across Europe |
| **NIST SP 800-86** | US National Institute of Standards & Technology | Collection → Examination → Analysis → Reporting |
| **ISO/IEC 27037:2012** | International Organisation for Standardisation | Identification → Collection → Acquisition → Preservation |

### ACPO Guidelines
ACPO guidelines from the UK influenced the investigation methodology worldwide.

> 📎 *Slide reference: `03_investigation_phases.pdf` — Investigation Frameworks*

---

## 2. Phase 1: Identification

**Objective**: Determine the scope of the investigation; identify all relevant evidence sources before any physical interaction.

### OSINT and Reconnaissance
Before touching any device, the investigator builds the fullest possible picture of the target using **Open Source Intelligence (OSINT)** — information gathered from publicly available sources without interacting with infrastructure the subject controls.

| OSINT Tool | Function |
|------------|---------|
| **Spiderfoot** | Automated OSINT aggregator; correlates information from dozens of public data sources |
| **Maltego** | Graph-based link analysis; visualises relationships between entities (IPs, domains, persons, organisations) |
| **Shodan** | Internet-facing device search engine; identifies open ports, service banners, and potential attack surfaces |

### Volatility Order
When deciding which evidence sources to handle first, follow the **volatility hierarchy** from most to least volatile. Higher-volatility items must be captured first because they are the most likely to be lost.

| Volatility Level | Evidence Source | Notes |
|-----------------|----------------|-------|
| Most volatile | **CPU registers**, CPU cache | Milliseconds to seconds of retention; only capturable with specialised hardware tools |
| Very volatile | **RAM (system memory)** | Survives seconds to a few hours after power loss (with cold-boot attack potential up to minutes) |
| Volatile | **Running processes**, open network connections, logged-in sessions, clipboard | Lost immediately on shutdown |
| Moderately volatile | **Virtual memory / swap file**, temporary files | May persist briefly after shutdown |
| Less volatile | **Persistent storage** (HDD, SSD, flash) | Survives power-off; the primary target of most forensic imaging |
| Least volatile | **Remote logs**, CCTV, access badge records, physical media backups | Controlled by third parties; may require formal legal process to obtain |

### Insider Threat Identification Scenario
Identifying an insider threat requires correlating multiple low-signal indicators:
- **Behaviour analytics**: Abnormal access times, volumes, or file types accessed by a known account
- **Email and communication logs**: Large attachments, contact with personal email addresses, unusual recipients
- None of these alone constitutes evidence; the investigation hypothesis is formed from their correlation.

> 📎 *Slide reference: `03_investigation_phases.pdf` — Phase 1: Identification*

---

## 3. Phase 2: Collection

**Objective**: Physically or logically acquire custody of all identified evidence sources while preserving their integrity and documenting the collection with chain of custody records.

### Isolation
As soon as collection begins, all devices must be **isolated from external networks** to prevent:
- **Remote wipe commands**: Remotely triggered commands that overwrite storage (common for mobile phones and laptops enrolled in MDM — Mobile Device Management — systems)
- **Synchronisation with cloud services**: Cloud sync clients may fetch updates or push deletions
- **Command-and-Control callbacks**: Malware on a running system may receive new instructions or send data out

| Method | Use Case |
|--------|---------|
| **Faraday bag** | Blocks all RF signals (Wi-Fi, 4G/5G, Bluetooth, NFC) for mobile devices and laptops with wireless capability |
| **Network cable disconnection** | For wired-only systems; simple and effective |
| **VLAN/firewall isolation** | For virtual machines or systems that cannot easily be physically disconnected |

> *Practical note*: A mobile phone seized without immediate Faraday bagging may receive a remote wipe command while in the evidence room if cellular signal is available.

### Physical Handling of Media
- Label all evidence items with a **unique identifier** (case number + item number) before handling
- **Do not power off a running system immediately** — volatile evidence may be lost; assess the value of live acquisition first (see Phase 3)
- Photograph every device **in situ** before any movement: exact position, cable connections, peripheral connections, on-screen state
- **Protect magnetic drives from strong magnetic fields** — these can alter or erase stored bits
- **RAM modules**: if capturing volatile memory, use a cryogenic container (below approximately −200°C) to preserve transistor charge for later lab extraction

### Chain of Custody Record Fields
A chain of custody record must be started at the moment the first evidence item is seized. Minimum required fields:

| Field | Description |
|-------|-------------|
| Case reference | Unique investigation identifier |
| Item identifier | Unique item number within the case |
| Item description | Make, model, serial number; capacity; distinguishing features |
| Date and time | UTC timestamp of collection |
| Location collected | Physical address and specific location (e.g., drawer #2, third shelf) |
| Collected by | Full name and badge/employee number of collecting officer |
| Witness | Second officer or independent witness, if present |
| Condition at collection | Observable physical state; powered on/off; damage; indicator lights |
| Packaging details | Bag type, seal number, labelling |
| Transfer record | Every subsequent custodian, date/time of transfer, and reason |

> 📎 *Slide reference: `03_investigation_phases.pdf` — Phase 2: Collection*

---

## 4. Phase 3: Acquisition

**Objective**: Create a forensically sound, verified copy of every identified evidence source for examination — preserving the original in an unmodified state.

### The Fundamental Rule
**Always work on a verified forensic copy, never on the original**. Even a read operation on an original may modify metadata (atime). The forensic image is the working copy; the original is sealed and preserved.

### The Trusted Tool Hierarchy
See Chapter 2 for full detail. Summary: use the **investigator's own forensic OS** booted from trusted media whenever possible to eliminate any risk from a compromised operating system on the suspect's machine.

### Static Acquisition
The standard approach when no volatile evidence is at risk:

1. Attach source drive via a **hardware write blocker**
2. Compute hash of the source (`sha256sum /dev/sdX`)
3. Run the forensic imaging tool to produce a bit-for-bit image
4. Compute hash of the resulting image
5. Verify hashes match — **document the hashes in the chain of custody record**
6. Seal the original; work only on the image

### Live Acquisition
Required when:
- A system is running with **full-disk encryption** (BitLocker, FileVault, LUKS) — the decryption keys are only available while the system is unlocked and powered on
- **Volatile data** (RAM, running processes, network connections) is specifically needed
- A **virtual machine** is running and its live state (heap, active connections) is relevant

> ⚠️ *Live acquisition inherently modifies the target system*: the process of capturing RAM requires running tools that consume memory and CPU. These modifications must be carefully documented as known and intentional.

### Cold-Boot Attack for RAM Acquisition
If a suspect machine is running but investigator tools cannot be safely installed:
1. Use a **cryogenic bag or container** to cool the RAM modules to well below −200°C (reduces electron diffusion, extends retention from seconds to minutes)
2. Physically move the cooled RAM modules to an investigator-controlled machine
3. Acquire RAM contents on the investigator's machine before thermal decay completes

This technique is specialist and used only when software-based RAM capture is not feasible.

### Hashing Requirements
- At least **SHA-256** is required
- **MD5 alone is insufficient** (known collision attacks exist)
- Best practice: compute **two hashes with different algorithms simultaneously** (e.g., SHA-256 + SHA-512) — simultaneous computation eliminates the argument that a hash was taken after undetected modification
- Tools like `dc3dd` support simultaneous multi-algorithm hashing during acquisition

> 📎 *Slide reference: `03_investigation_phases.pdf` — Phase 3: Acquisition*

---

## 5. Phase 4: Examination and Analysis

**Objective**: Extract legally significant information from the forensic copies; reconstruct events; build the timeline; detect anti-forensics techniques.

### Authenticity vs. Integrity
Two distinct concepts that must both be established:

| Concept | Question Answered | How Established |
|---------|------------------|----------------|
| **Integrity** | Has the evidence been modified since acquisition? | Hash comparison (original hash vs. current hash of the forensic image) |
| **Authenticity** | Is this evidence genuinely associated with the alleged events and persons? | Contextual corroboration — corroborating file metadata, network logs, physical access records, witness testimony |

Integrity alone does not establish authenticity. A file can be unmodified since capture yet still be a planted document — authenticity requires independent corroboration.

### Deep Fakes and AI-Manipulated Evidence
As generative AI advances, examiners must assess **deep fake risk** when evaluating digital media. AI-generated images may contain errors that a human would not produce. Additionally, metadata inconsistencies — such as a clock visible in an image showing a different time than the file metadata — can indicate manipulation.

**Cross-correlation** with independent evidence sources is the primary defence: even a realistic-looking image can be shown to be fabricated when it contradicts witness testimony, access records, or other independent sources all pointing to a different fact.

> *Deep fake detection is an emerging forensic specialisation — courts are increasingly encountering challenges to digital media authenticity on these grounds.*

### Timeline Construction

Constructing a reliable timeline requires correlating timestamps from **multiple independent sources**:

| Source | Timestamp Type | Reliability Notes |
|--------|---------------|-------------------|
| File system metadata | Created / Modified / Accessed / MFT record change | Can be modified by any user with write access to the file |
| Windows Event Logs | System, Application, Security, PowerShell logs | Require admin rights to clear; clearing itself is logged |
| Firewall and proxy logs | Connection timestamps, URL, bytes transferred | Controlled by infrastructure team; harder to tamper from an endpoint |
| Email server logs | Send/receive timestamps per hop | Each relay adds a `Received:` header; timestamps cross-checkable |
| Mobile phone records | Call/data metadata from carrier (via legal request) | Carrier-controlled; high reliability |
| CCTV footage | Physical presence timestamps | External system; requires subpoena |

**Clock skew**: Different systems may not have synchronised clocks. A ±30-second discrepancy between an endpoint event log and a firewall log is acceptable; a ±2-hour discrepancy may indicate a tampered system clock or a device in a different time zone. Always record the **clock delta** between evidence sources.

### Anti-Forensics Techniques

| Technique | Description | Forensic Counter-Technique |
|-----------|-------------|---------------------------|
| **Encryption at the OS level** | Storage encrypted by default in modern operating systems; data unreadable without decryption key | Live acquisition for keys in RAM while system is unlocked |
| **HTTPS / TLS** | Application-layer network traffic encrypted; IDS and network-based monitoring cannot inspect payloads | Endpoint acquisition; server-side logs; DNS queries may still be visible |
| **File deletion and data wiping** | Deliberate removal or overwriting of data before or during investigation | Recovery may still be possible from unallocated space or residual artefacts depending on media and method |

### Legal and Ethical Constraints on Examination
- **Scope limitation**: The authority (warrant, consent) defines exactly which devices and which categories of data may be examined. An investigator who exceeds the scope commits a legal violation that can invalidate the investigation.
- **Third-party data**: A seized device may contain data belonging to persons not named in the investigation. Data minimisation principles require examining only the data directly relevant to the investigation.
- **Encryption challenges**: If storage is encrypted, the investigator may need to perform live acquisition to capture decryption keys from RAM; the legal basis for compelling a suspect to provide decryption keys varies by jurisdiction.

### Iterative Hypothesis Process
Forensic examination is not linear — it is iterative:

1. Develop an initial **hypothesis** (e.g., "Subject X exfiltrated files between Monday and Thursday")
2. Identify **artefacts consistent with the hypothesis** and document them
3. Actively search for **artefacts that contradict the hypothesis** — the investigation must disprove as well as confirm
4. **Revise the hypothesis** if contradictory evidence is found and repeat
5. Final conclusions must account for all artefacts, including those that complicate the narrative

> 📎 *Slide reference: `03_investigation_phases.pdf` — Phase 4: Examination & Analysis*

---

## 6. Phase 5: Presentation

**Objective**: Communicate findings accurately and clearly to the appropriate audience in a way that is defensible, complete, and properly contextualised.

### Report Audiences
Different stakeholders require different report formats containing the same underlying facts presented at different levels of technical depth:

| Audience | Report Type | Key Requirements |
|----------|------------|-----------------|
| **Court / judge** | Expert witness report / statement | Legally precise; conclusions stated as findings of fact or expert opinion; methodology detailed; conclusions couched in probabilistic terms if disputed |
| **Prosecution / defence counsel** | Legal brief supplement | Organised around legal elements; technical detail in appendices; accessible language in the main body |
| **Technical IT/security team** | Technical report | Full technical detail; allows the organisation to understand attack vectors and patch vulnerabilities |
| **Executive / board** | Executive summary | Non-technical language; business impact focus; recommendations |

### Report Integrity — Versioning
Reports go through multiple drafts and quality assurance reviews. All versions must be clearly labelled and preserved:
- **Draft 1**: Initial examiner draft before any review
- **Draft 2**: After senior examiner / QA peer review
- **Final**: The version submitted to court or client

In litigation, *all prior drafts may be discoverable*. Never delete draft reports.

### Quality Assurance Double-Check
Before finalising:
1. **Independent technical review**: A second examiner repeats key steps on the same forensic images and confirms that the same results are obtained (demonstrates repeatability)
2. **Legal review**: Counsel confirms that conclusions are properly constrained and do not exceed what the evidence supports
3. **Chain of custody audit**: Every item referenced in the report is verified to have a complete, unbroken chain of custody entry

> 📎 *Slide reference: `03_investigation_phases.pdf` — Phase 5: Presentation*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **ACPO Principles** | UK guidelines that significantly influenced forensic investigation methodology worldwide |
| **Volatility Order** | Hierarchy of evidence sources from most to least transient; volatile evidence must be captured first |
| **OSINT** | Open Source Intelligence — intelligence gathered from publicly available sources without interacting with systems under investigation |
| **Faraday Bag** | RF-shielded enclosure that blocks all wireless signals; used to prevent remote wipe of mobile devices post-seizure |
| **Static Acquisition** | Bit-for-bit copy of powered-off storage; the default forensic acquisition method when no volatile data is at risk |
| **Live Acquisition** | Forensic acquisition of a running system's memory or state; requires careful documentation of any modifications made |
| **Cold-Boot Attack** | Technique using temperature reduction to extend RAM data retention for analysis after power-off |
| **Clock Skew** | Discrepancy between clocks on different systems; must be calculated and documented when correlating timestamps |
| **Anti-Forensics** | Deliberate techniques to obstruct forensic investigation; also arises inherently from modern OS features such as encryption and HTTPS |
| **Authenticity** | The evidence genuinely represents the events or actions alleged; requires contextual corroboration beyond hash integrity |
| **Scope Limitation** | Legal constraint that restricts examination to only the devices and data types specified in the authorising warrant or consent |

---

## Summary

- Multiple international frameworks (ACPO, NIST, ISO 27037) converge on the same five phases; adherence to a recognised framework is what makes results **legally defensible**.
- **Phase 1 (Identification)**: Use OSINT (Spiderfoot, Maltego, Shodan) before touching any device; follow the **volatility order**.
- **Phase 2 (Collection)**: Immediately isolate all devices; photograph in situ; start the **chain of custody record** at first contact.
- **Phase 3 (Acquisition)**: Never examine originals; use hardware write blockers; hash with SHA-256 or better; choose **live acquisition** when full-disk encryption is active.
- **Phase 4 (Examination)**: Distinguish **integrity** (hash verification) from **authenticity** (contextual corroboration); reconstruct the **timeline** from multiple independent sources; identify and counter **anti-forensics** techniques; respect strict **scope limitations**.
- **Phase 5 (Presentation)**: Tailor the report to the audience; preserve **all draft versions**; perform an independent QA technical review to establish repeatability before submission.

> 📝 *The practical USB drive acquisition procedure is covered in [03b_Forensic-USB-Drive-Acquisition.md](03b_Forensic-USB-Drive-Acquisition.md).*  
> 📝 *An end-to-end case study applying all five phases is in [Digital-Forensics-Case-Study.md](Digital-Forensics-Case-Study.md).*
