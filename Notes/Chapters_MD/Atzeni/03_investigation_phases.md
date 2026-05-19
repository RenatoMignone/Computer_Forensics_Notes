# Chapter 3 – Forensic Investigation Phases
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/03_investigation_phases.pdf`]  
**Covered in Lectures:** Lecture 4, Lecture 5

---

## Introduction
Digital forensic investigations are not freeform activities. They are structured into phases, each with its own objectives and documentation expectations. Atzeni presents the five-phase model as a useful conceptual frame, while noting that recognised standards may merge or rename phases. This chapter covers the major framework examples mentioned in lecture, then provides an in-depth treatment of each phase: Identification, Collection, Acquisition, Examination, and Presentation.

---

## 1. Forensic Investigation Frameworks and Standards

Several bodies have published guidelines defining forensic investigation phases. They converge on the same core activities despite using different terminology.

| Standard | Organisation | Phases |
|----------|-------------|--------|
| **ACPO Guidelines** | UK Association of Chief Police Officers | Influential UK standard; widely adopted across Europe |
| **NIST family** | US National Institute of Standards & Technology | Open standards; Atzeni notes that NIST uses a four-phase model rather than his five-phase teaching model |
| **ISO standards** | International Organisation for Standardisation | Respected and well structured, but described by Atzeni as less practically useful in some contexts |

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
| Very volatile | **RAM (system memory)** | Lost on shutdown unless specialist live or cold-acquisition techniques are used |
| Volatile | **Running processes and active network connections** | Can disappear within seconds or minutes |
| Moderately volatile | **Temporary files, deleted files, hidden/residual storage areas** | May be overwritten by normal system activity |
| Less volatile | **Persistent storage** (HDD, SSD, flash) | Survives power-off, but normal use can still alter metadata and deleted areas |
| External / remote | **Cloud data, logs, network devices, organisational systems** | May require cooperation from administrators, providers, or legal authorities |

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
- **Remote wipe commands**: Remotely triggered commands that can destroy evidence on mobile or connected systems
- **Synchronisation with cloud services**: Cloud sync clients may fetch updates or push deletions
- **Command-and-Control callbacks**: Malware on a running system may receive new instructions or send data out

| Method | Use Case |
|--------|---------|
| **RF isolation / jammer where lawful and appropriate** | Prevents wireless or mobile-network communication, including remote wipe attempts |
| **Network cable disconnection** | For wired-only systems; simple and effective |
| **VLAN/firewall isolation** | For virtual machines or systems that cannot easily be physically disconnected |

> *Practical note*: Atzeni explicitly mentions remote wiping as a reason to prevent wireless or mobile-network communication as early as possible.

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
| Condition at collection | Observable physical state; powered on/off; damage; indicator lights |
| Packaging / label details | Bag or box identifier, labels, and other information needed to distinguish similar devices |
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
- A system is running with storage encryption active — the decryption keys may still be available in memory while the system is unlocked and powered on
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
- Use a currently sound hash algorithm such as **SHA-256**
- **MD5 alone is insufficient** (known collision attacks exist)
- In important cases, compute **two hashes with different algorithms**, preferably as close to the copy operation as possible
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
| System and application logs | Local or server-side event traces | Must be correlated with other sources |
| Firewall, proxy, or gateway logs | Connection timing and traffic patterns | Useful for reconstructing communication paths |
| Email server logs and headers | Message path and timing information | Require domain knowledge of email protocols |
| Physical or organisational records | Presence, HR, or access-context information where available | Useful for corroborating digital activity |

**Clock consistency**: Different systems may not have synchronised clocks, so timestamp correlation must account for possible differences before drawing conclusions.

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

### Quality Assurance Double-Check
Before finalising:
1. A second examiner or colleague checks that evidence, hashes, and referenced artefacts are properly identified.
2. The report is checked against the underlying data so unsupported personal interpretation does not enter the record.
3. The chain of custody and links between report claims and evidence are verified.

> 📎 *Slide reference: `03_investigation_phases.pdf` — Phase 5: Presentation*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **ACPO Principles** | UK guidelines that significantly influenced forensic investigation methodology worldwide |
| **Volatility Order** | Hierarchy of evidence sources from most to least transient; volatile evidence must be captured first |
| **OSINT** | Open Source Intelligence — intelligence gathered from publicly available sources without interacting with systems under investigation |
| **RF isolation / jammer** | Means of blocking wireless or mobile-network communication where lawful and appropriate, used to reduce risks such as remote wipe |
| **Static Acquisition** | Bit-for-bit copy of powered-off storage; the default forensic acquisition method when no volatile data is at risk |
| **Live Acquisition** | Forensic acquisition of a running system's memory or state; requires careful documentation of any modifications made |
| **Cold-Boot Attack** | Technique using temperature reduction to extend RAM data retention for analysis after power-off |
| **Clock Skew** | Discrepancy between clocks on different systems; must be calculated and documented when correlating timestamps |
| **Anti-Forensics** | Deliberate techniques to obstruct forensic investigation; also arises inherently from modern OS features such as encryption and HTTPS |
| **Authenticity** | The evidence genuinely represents the events or actions alleged; requires contextual corroboration beyond hash integrity |
| **Scope Limitation** | Legal constraint that restricts examination to only the devices and data types specified in the authorising warrant or consent |

---

## Summary

- Multiple international frameworks (ACPO, NIST, ISO) cover similar concepts, but may use four phases, five phases, merged phases, or different names.
- **Phase 1 (Identification)**: Use OSINT (Spiderfoot, Maltego, Shodan) before touching any device; follow the **volatility order**.
- **Phase 2 (Collection)**: Immediately isolate all devices; photograph in situ; start the **chain of custody record** at first contact.
- **Phase 3 (Acquisition)**: Never examine originals; use hardware write blockers; hash with SHA-256 or better; choose **live acquisition** when encrypted storage or volatile data makes shutdown risky.
- **Phase 4 (Examination)**: Distinguish **integrity** (hash verification) from **authenticity** (contextual corroboration); reconstruct the **timeline** from multiple independent sources; identify and counter **anti-forensics** techniques; respect strict **scope limitations**.
- **Phase 5 (Presentation)**: Tailor the report to the audience; keep claims tied to the underlying evidence; perform a double-check before submission.

> 📝 *The practical USB drive acquisition procedure is covered in [03b_Forensic-USB-Drive-Acquisition.md](03b_Forensic-USB-Drive-Acquisition.md).*  
> 📝 *An end-to-end case study applying all five phases is in [Digital-Forensics-Case-Study.md](06_Digital-Forensics-Case-Study.md).*
