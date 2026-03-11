# Lecture 2 – Digital Evidence, Chain of Custody & Data Acquisition
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/02_terms.pdf`

---

## Overview
This lecture builds on the historical introduction from Lecture 1 by defining the core technical concepts of computer forensics: digital evidence, chain of custody, and the data acquisition process. A prerequisite knowledge quiz is discussed to gauge students' baseline understanding of cybersecurity and file system fundamentals. The lecture concludes with practical forensic investigation scenarios.

---

## 1. Recap – Digital Forensics Milestones & Tools

### Automation and Accuracy in Digital Forensics
The field has developed towards increasing **automation** and **accuracy** in three main ways:
- Creation of **databases of evidence** (e.g., hash libraries of known-good software)
- Development of **integrated tools** (e.g., EnCase, FTK) that handle acquisition, categorisation, integrity verification, and storage in one workflow
- Application of **machine learning** and automatic comparison between evidence sources

### The NSRL (National Software Reference Library)
An initiative from the **United States** that maintains a database of cryptographic hashes (forensically sound) for legitimate, widely-distributed software. A forensic analyst can compare hashes found on a suspect's hard drive against this library to:
- Quickly identify **unmodified standard software** (no need for detailed analysis)
- Identify **modified or substituted binaries** that differ from the original

### Impact of Large Language Models
LLMs can compare, synthesise, and highlight differences in **structured information** across terabytes of data — automating what would otherwise require extensive manual review. However, their outputs require expert verification.

Beyond forensic automation, LLMs also enable new attack vectors — notably **voice cloning**: with as little as one to two minutes of recorded speech, an attacker can generate an acoustically accurate replica of a specific person's voice. This makes phone-based social engineering attacks (vishing) significantly more convincing and harder to detect.

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Milestones & Tools*

---

## 2. What is Computer Forensics?

Computer forensics is involved in **95–98% of modern investigations** in some capacity — even non-digital investigations eventually produce digital reports, which must be preserved as evidence.

### Formal Definition (Working Definition)
> Computer forensics is the capability to **identify, gather, acquire, examine**, and **present** relevant digital evidence in a way that supports reaching conclusions in an investigation.

### Core Requirements
Every phase of a computer forensic investigation must be:

| Property | Description |
|----------|-------------|
| **Sound** | Technically correct and compliant with accepted standards |
| **Repeatable** | Any third party should be able to reproduce the same results from the same evidence |
| **Documented** | Every action, tool, and parameter must be recorded |
| **Non-altering** | Evidence must not be modified, even unintentionally, during examination |

A single undocumented or improperly handled step can **compromise the admissibility** of all evidence in a legal proceeding.

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Core Concepts*

---

## 3. Investigative Goals – The Key Questions

A forensic investigation aims to reconstruct a course of events by answering:

| Question | Description |
|----------|-------------|
| **What** happened? | The full sequence of events and actions |
| **Who** was involved? | Both human actors *and* automated agents (malware, programs) |
| **When** did it happen? | Precise timestamps allowing the construction of a **timeline** |
| **Where** did it occur? | Physical location (device, room, network segment) or logical location (file system path, IP address, cloud instance) |
| **Why** did it happen? | Motive, goal, or trigger for the incident |
| **How** did it occur? | Technical mechanisms and vulnerabilities exploited |

### The Concept of Timeline
A **timeline** is one of the most central concepts in digital forensics. It is the reconstruction of the precise sequence of events — with correlated timestamps from multiple sources — that allows a forensic expert to produce a coherent, defensible narrative of what took place.

> *Example:* If logs show a user obtained a key the day after entry was recorded in a different system, the timeline is incoherent and indicates either tampering or an error.

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Forensic Investigation Purposes*

---

## 4. Domain-Specific Knowledge in Forensics

For each type of digital evidence, the forensic expert must have **specialised domain knowledge**. Examples include:

### File System Forensics
- Understanding how the file system mediates access to raw storage
- Knowing that **access times are modified** when a file is opened — so analysis tools must not trigger this
- Understanding deleted files may still exist in **slack space** or unallocated sectors

### Email Forensics
- Understanding the **S/MIME format** and the path of email through multiple servers
- Knowing which header fields are modified **hop-by-hop** and which are end-to-end preserved
- Knowing what information can be extracted from email metadata

### Network Forensics
- Understanding **TLS session keys** and how to recover them
- Example: Chrome (and other browsers) can be launched with a flag to dump session keys to a file — importable into Wireshark to decrypt captured TLS traffic
- Network flow analysis to identify infection patterns (as in the Morris Worm ARPANET graph reconstruction)

### Cloud Forensics
- Most data may reside on the cloud, not on the physical device
- Requires cooperation with the cloud provider
- Standard acquisition procedures are insufficient

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Digital Evidence Types*

---

## 5. Digital Evidence

**Digital evidence** is any piece of data — stored, transferred, or manipulated in any form — that can be used in an investigation to reach a conclusion.

### Key Properties

#### Fragility
Digital evidence is **inherently fragile**:
- **Physical threats**: magnetic fields can alter magnetic hard drives; fingerprints on optical discs (DVDs/CDs) can reduce readability
- **Logical threats**: merely accessing a file through the OS modifies the file's **last-accessed metadata timestamp**

The forensic expert must be aware of *both* dimensions of fragility.

#### Chain of Evidentiary Relationships
The forensic expert must document not only individual artefacts but the **relationships between them** — creating a record that itself becomes evidence.

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Digital Evidence*

---

## 6. Chain of Custody

The **chain of custody** is the complete, documented history of how digital evidence was handled — from the moment it was first identified until the final verdict.

### Why it Matters
If any step is undocumented or unclear, an adversarial party can argue that the evidence was tampered with at that point, rendering it **legally inadmissible**.

### Physical Chain of Custody
- Who took physical possession of a device, when, and where
- How it was transported between locations (e.g., from crime scene to forensic lab)
- Under what conditions it was stored

### Logical Chain of Custody
- Who mounted which file system, how, and with which tools
- If a write-blocking mechanism was not used, metadata like **last-access time** may have been inadvertently altered — compromising specific evidence points

### Both dimensions must be documented. A single missing link is sufficient to challenge the entire investigation in court.

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Chain of Custody*

---

## 7. The Data Acquisition Process

Data acquisition is a **critical phase** — mistakes here can permanently compromise the legal admissibility of evidence.

### Running vs. Powered-Off System
A key decision the forensic investigator must make:

| Situation | Approach | Risk |
|-----------|----------|------|
| System powered off | Avoid powering on; directly extract storage | Lower risk of metadata modification |
| System running | Live acquisition; capture RAM, active connections | Powering off destroys volatile data |
| Encrypted storage | Must keep system running to recover keys from RAM | Powering off may make storage permanently inaccessible |
| Compromised OS | Running tools on it may produce misleading results | |

Switching off a running system causes **hundreds of metadata changes**: open files are closed, memory is cleared, file access times are modified, file system logs are updated.

### Write Blockers
**Write blockers** prevent any write operations to the target storage device during acquisition, ensuring the original evidence is not modified.

- **Physical write blockers**: dedicated hardware that provides an exclusive channel to the source device and impedes any interference during the copy. Most robust protection; a professional forensic kit always includes at least one.
- **Logical write blockers**: OS-level mechanisms that mount a device in read-only mode. Less robust but acceptable in lower-stakes investigations, provided the operating system itself is not compromised.

A forensic investigator typically carries a **professional kit** containing physical write blockers.

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Data Acquisition & Write Blockers*

### Hashing for Integrity Verification
Hash functions are the **primary tool** for proving that evidence has not been modified.

- A hash (digest) must be computed **before and after** any acquisition or manipulation
- Hashes must be compared to confirm integrity
- **Multiple hash algorithms** should be used simultaneously for increased robustness
- **MD5 is NOT recommended** as a standalone algorithm (collision vulnerabilities, short digest)
- Preferred: **SHA-256 or SHA-512** (SHA-2 family)

#### Why Multiple Algorithms?
Using two or more algorithms simultaneously makes it computationally infeasible for an attacker to produce a file that matches both hashes simultaneously.

#### Command-line tools for hashing:
- `sha256sum` / `sha512sum`
- `hashdeep` — batch hashing of multiple files
- `dc3dd` / `dcfldd` — enhanced versions of `dd` that integrate hashing into the copy process

### Forensic Imaging Tools
A **forensic image** is a bit-for-bit copy of a storage device produced using forensically sound tools. It preserves:
- All data blocks (including deleted and unallocated space)
- Metadata
- Slack space

| Tool | Description |
|------|-------------|
| **EnCase** | Industry-standard commercial tool; expensive but widely used and accepted in courts |
| **FTK Imager** | Supports popular forensic formats; commonly used in real investigations |
| **dd** | Classic Unix bit-by-bit copy command; available on any Linux/macOS system |
| **dc3dd / dcfldd** | Enhanced dd with built-in hashing, logging, and error handling |
| **Autopsy / Sleuth Kit** | Open-source forensic analysis platform |

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slides: Forensic Imaging & Tools*

---

## 8. Trusted Tools

A forensic investigator must **never** use tools found on the suspect's own system:
- The suspect may have compiled a modified version of a tool (e.g., `dd`) that selectively skips specific memory regions containing incriminating data
- Tools used must come from the investigator's own **trusted, verified kit**

The hierarchy of trust (from lowest to highest):
1. Tool on the **suspect's machine** using the suspect's OS libraries — vulnerable to both compiled and library-level tampering
2. Tool on investigator's **USB drive**, but relying on the suspect system's shared libraries — partial trust
3. **Full live Linux distribution** booted from the investigator's own media (e.g., Kali, Tsuruji, Caine) — fully trusted environment, best practice

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Tools & Trust*

---

## 9. Typical Forensic Investigation Scenarios

| Scenario | Description |
|----------|-------------|
| **Internal network abuse** | Employee accessing restricted sites or external addresses; must balance privacy rights with abuse detection |
| **Online fraud investigation** | Anomalous banking behaviour (many high-value transfers in unusual hours) indicating malware-driven account compromise |
| **Data unauthorised manipulation** | Analysing server and network logs to trace exfiltration of sensitive data |
| **Malware infection extent** | Reconstructing the spread of an infection through an organisation's network using log artefacts and file system traces — even after malware has self-deleted |

The outcome of forensic analysis is **dual-purpose**: supporting legal proceedings *and* preventing future incidents by explaining the attack path.

> 📎 *Slide reference: `Slides/Atzeni/02_terms.pdf`, slide: Forensic Scenarios*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Digital Evidence** | Any digital data that can support conclusions in an investigation |
| **Chain of Custody** | Documented history of all handling of evidence from discovery to presentation |
| **Forensic Image** | A bit-for-bit copy of a storage device created using forensically sound tools |
| **Write Blocker** | Hardware or software device that prevents write operations to a storage medium during acquisition |
| **Hashing / Digest** | A fixed-length fingerprint of data used to verify that no modification has occurred |
| **Timeline** | A chronological reconstruction of events based on correlated timestamps from multiple evidence sources |
| **NSRL** | National Software Reference Library; database of hashes of known-good software |
| **Slack Space** | Unused space within an allocated disk cluster that may contain remnants of previously deleted data |
| **Live Acquisition** | Forensic acquisition performed on a running system to capture volatile data (RAM, network state) |
| **Static Acquisition** | Forensic acquisition performed on a powered-off device |
| **APT** | Advanced Persistent Threat — a sophisticated, prolonged attack that uses lateral movement to persist inside a target network |

---

## Summary

- Digital evidence can be found in virtually **every modern investigation**; proper handling requires domain expertise for every evidence type.
- The six core investigative questions are: **what, who, when, where, why, how** — with timeline reconstruction being central.
- The **chain of custody** must be documented at every step, both physically and logically; a single undocumented step can invalidate evidence in court.
- **Write blockers** and **hashing** are the primary technical mechanisms that protect evidence integrity during acquisition.
- Tool selection matters: only **tested, trusted tools from the investigator's own kit** are acceptable; using tools from the suspect's system is inadmissible.
- Forensic investigation results serve both **legal proceedings** and **organisational prevention** by revealing how incidents occurred.
