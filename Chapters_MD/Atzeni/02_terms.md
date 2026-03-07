# Chapter 2 – Core Concepts: Digital Evidence, Chain of Custody & Data Acquisition
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/02_terms.pdf`]  
**Covered in Lectures:** Lecture 2

---

## Introduction
Before any forensic investigation can begin, practitioners must understand the foundational vocabulary and procedures that govern how digital evidence is identified, preserved, acquired, and verified. This chapter defines computer forensics formally, introduces the six investigative questions, explains the properties of digital evidence and how they differ from physical evidence, and covers the two mechanisms that protect evidence integrity: the chain of custody and forensic hashing. It concludes with a structured overview of forensic imaging tools and the principle of trusted tools.

---

## 1. Automation and Accuracy – The State of the Field

The evolution of digital forensics has been characterised by three complementary trends:

| Trend | Description |
|-------|-------------|
| **Evidence databases** | Hash libraries of known-good software (e.g., NSRL) enable rapid elimination of irrelevant files |
| **Integrated toolchains** | Platforms like EnCase and FTK handle acquisition, categorisation, integrity verification, and storage in a single workflow |
| **Machine learning** | Automated comparison and correlation across large evidence sets; always requires expert validation |

### The NSRL (National Software Reference Library)
A US government initiative maintaining a database of **cryptographic hashes of legitimate, widely-distributed software**. Forensic use:
- Match file hashes on a suspect's drive against the NSRL database
- Files matching the NSRL are **known-good standard software** → exclude from detailed analysis
- Files that differ from their expected NSRL hash are **modified or substituted binaries** → flag for investigation

**Impact of LLMs**: Large language models can now compare, synthesise, and highlight differences across terabytes of structured log data — automating tasks that previously required extensive manual review. All LLM outputs require expert verification before use in evidence.

> 📎 *Slide reference: `02_terms.pdf` — Milestones & Tools*

---

## 2. Formal Definition of Computer Forensics

> **Working definition**: Computer forensics is the capability to **identify, gather, acquire, examine**, and **present** relevant digital evidence in a way that supports reaching conclusions in an investigation.

Computer forensics is present in **95–98% of modern investigations** in some form — even non-digital investigations eventually produce digital reports and records that must be preserved as evidence.

### Core Properties — Every Phase Must Be:

| Property | Meaning |
|----------|---------|
| **Sound** | Technically correct, compliant with accepted standards |
| **Repeatable** | Any qualified third party should be able to reproduce the same results from the same evidence |
| **Documented** | Every action, tool, parameter, and result must be recorded |
| **Non-altering** | Evidence must not be modified, even unintentionally, during any phase |

A single undocumented or improperly handled step can **compromise the admissibility of all evidence** gathered in an investigation.

> 📎 *Slide reference: `02_terms.pdf` — Core Concepts*

---

## 3. The Six Investigative Questions

A forensic investigation must answer six questions. Together their answers constitute the **narrative of the investigation**.

| Question | Description |
|----------|-------------|
| **What** happened? | The full sequence of events and actions that occurred |
| **Who** was involved? | Both human actors *and* automated agents (malware, scripts, scheduled tasks) |
| **When** did it happen? | Precise timestamps enabling construction of a **timeline** |
| **Where** did it occur? | Physical location (device, room, campus) or logical location (file path, IP address, cloud instance) |
| **Why** did it happen? | Motive, goal, or trigger |
| **How** did it occur? | Technical mechanisms and any vulnerabilities exploited |

### The Timeline
The **timeline** is the centrepiece of most forensic investigations: a chronological reconstruction of events with correlated timestamps from multiple sources. It transforms isolated artefacts into a coherent, defensible narrative.

> *Example*: If logs show a user obtained a key the day after their access to a system is recorded in a different system, the timeline is incoherent — indicating either tampering or a clock synchronisation error.

> 📎 *Slide reference: `02_terms.pdf` — Forensic Investigation Purposes*

---

## 4. Domain-Specific Knowledge

Each category of digital evidence requires the forensic examiner to hold **specialised domain expertise**. Generic forensic knowledge is necessary but not sufficient.

### File System Forensics
- Understanding how the **file system mediates access** to raw storage blocks
- Knowing that **access time (atime) is modified** whenever a file is opened — requiring analysis tools to avoid triggering this
- Understanding that deleted files may still exist in **slack space** (unused bytes at the end of a cluster) or in unallocated sectors

### Email Forensics
- Understanding the **S/MIME format** and the **hop-by-hop path** of a message through multiple mail servers
- Knowing which header fields are modified at each relay hop (`Received:`) and which are end-to-end preserved (`From:`, `Date:`)
- Extracting **metadata from email headers** to reconstruct delivery timelines

### Network Forensics
- Understanding **TLS session key** management and how to recover session keys for decryption
  - Chrome and other browsers can be launched with the `SSLKEYLOGFILE` environment variable to dump session keys to a file — these can be imported into Wireshark to decrypt captured TLS traffic
- Network **flow analysis** to identify infection topologies (as in the Morris Worm ARPANET propagation graph)

### Cloud Forensics
- Most data may reside entirely in the cloud with **no local copy** on the seized device
- Access requires **cooperation from the cloud provider**, often governed by foreign law
- Standard physical acquisition procedures are **insufficient** — cloud forensics is primarily a legal and API-based process

> 📎 *Slide reference: `02_terms.pdf` — Digital Evidence Types*

---

## 5. Digital Evidence

**Digital evidence** is any piece of data — stored, transmitted, or manipulated in any digital form — that can be used in an investigation to reach a conclusion.

### Key Property: Fragility
Digital evidence is **inherently fragile** in two dimensions:

| Dimension | Examples |
|-----------|---------|
| **Physical** | Magnetic fields can alter bits on magnetic hard drives; fingerprints on optical discs (DVD/CD) reduce the reflective surface's readability |
| **Logical** | Accessing a file through the OS modifies the file's `atime` (last-accessed) metadata timestamp; opening a directory listing updates directory access metadata |

The forensic examiner must be aware that **normal interaction with evidence causes modification**. This is why write blockers and forensic copies are mandatory before any examination.

### Chain of Evidentiary Relationships
Beyond individual artefacts, the forensic examiner must document the **relationships between artefacts** — which files created which processes, which accounts accessed which resources, which network connections led to which data transfers. This relationship map itself becomes part of the evidence record.

> 📎 *Slide reference: `02_terms.pdf` — Digital Evidence*

---

## 6. Chain of Custody

The **chain of custody** is the complete, unbroken, documented record of how every piece of evidence was handled — from the moment it was first identified through to the final verdict.

### Why It Is Critical
If any handling event is undocumented or unclear, an adversarial party can argue that evidence was **tampered with at that gap**, rendering it inadmissible. Courts apply a presumption: if the chain cannot be shown to be unbroken, the evidence may be excluded.

### Physical Chain of Custody
Documents the **physical handling** of evidence items:
- Who took possession of a device, when, and from where
- How it was transported (sealed evidence bag, locked container, vehicle)
- Under what conditions it was stored (temperature, humidity, access controls)
- Every transfer between custodians, with signatures

### Logical Chain of Custody
Documents **digital operations** performed on evidence:
- Which examiner mounted which file system, using which tool, at what time
- Whether a write-blocking mechanism was in place (if not, `atime` and directory metadata may have been inadvertently altered)
- Which hash values were verified, when, and with which tool

**Both dimensions must be documented in full. A broken link in either is sufficient to challenge the entire investigation in court.**

> 📎 *Slide reference: `02_terms.pdf` — Chain of Custody*

---

## 7. Data Acquisition

Data acquisition is the process of creating a **forensically sound copy** of evidence for examination. It is the phase most vulnerable to irreversible errors.

### Live vs. Static Acquisition Decision

| Scenario | Recommended Approach | Rationale |
|----------|---------------------|-----------|
| System powered off | **Static acquisition** — do not power on; extract storage directly | Lowest risk; no additional metadata modification |
| System running, no encryption | Consider powering off first | Avoid live system complexity unless volatile data is needed |
| System running with encrypted storage | **Live acquisition** — capture RAM before powering off | Encryption keys are in RAM; powering off destroys them permanently |
| Compromised OS (rootkit suspected) | Boot from investigator's own forensic OS | Cannot trust tools on the suspect's machine |

> *Switching off a running system causes hundreds of metadata changes: open files are closed, memory is cleared, timestamps updated, file system journals flushed.*

### Write Blockers

**Write blockers** intercept any write command directed at the source device, ensuring the original is never modified during acquisition.

| Type | Description | Trust Level |
|------|-------------|-------------|
| **Hardware write blocker** | Physical device placed between source drive and acquisition workstation; intercepts write signals at the hardware level | Highest — fully hardware-enforced |
| **Software / logical write blocker** | OS-level mechanism mounting a device in read-only mode | Lower — can potentially be bypassed by a privileged process |

Hardware write blockers are the professional standard. A forensic investigator's kit invariably contains at least one.

> 📎 *Slide reference: `02_terms.pdf` — Data Acquisition & Write Blockers*

---

## 8. Hashing for Integrity Verification

Cryptographic hash functions provide the **primary mechanism for proving evidence has not been modified**.

### Protocol
1. Compute hash of the source device **before acquisition**
2. Create the forensic image
3. Compute hash of the resulting image **after acquisition**
4. Hashes must **match exactly** — any difference means the acquisition failed or the evidence was altered

### Algorithm Requirements

| Algorithm | Status | Reason |
|-----------|--------|--------|
| **MD5** | ❌ Not sufficient alone | Collision attacks are feasible: two different files can be crafted to share the same MD5 hash; a defence team could argue the image was fabricated |
| **SHA-256** | ✅ Current standard | No known feasible collision attacks; produces 256-bit digest |
| **SHA-512** | ✅ Highest assurance | 512-bit digest; preferred in high-stakes investigations |
| **Multiple algorithms simultaneously** | ✅ Best practice | Some jurisdictions require or recommend using multiple algorithms concurrently |

### Command-line Hashing Tools

```bash
sha256sum /dev/sdb > pre_image_hash.txt       # Hash source before acquisition
dd if=/dev/sdb of=image.dd bs=512             # Create image
sha256sum image.dd > post_image_hash.txt      # Hash image after acquisition
diff pre_image_hash.txt post_image_hash.txt   # Verify match
```

Specialised tools (`dc3dd`, `dcfldd`) integrate hashing into the copy operation, computing the source and destination hash simultaneously during the bit-by-bit copy.

> 📎 *Slide reference: `02_terms.pdf` — Forensic Imaging & Tools*

---

## 9. Forensic Imaging Tools

A **forensic image** is a bit-for-bit copy of a storage device, created using forensically sound tools. It preserves all data blocks including deleted content, slack space, and unallocated sectors.

| Tool | Type | Key Features |
|------|------|-------------|
| **EnCase** | Commercial (GUI) | Industry standard; expensive; widely accepted in courts; integrated acquisition, analysis, and reporting |
| **FTK Imager** | Commercial (GUI, free tier) | Multiple output formats (.dd, .E01, .AFF); integrated hashing; drive preview without mounting |
| **`dd`** | Open-source (CLI) | Standard Unix bit-copy utility; available on any Linux/macOS system; no built-in hashing |
| **`dc3dd` / `dcfldd`** | Open-source (CLI) | Enhanced `dd` with integrated hashing, progress reporting, split output, and log generation |
| **Autopsy / Sleuth Kit** | Open-source (GUI+CLI) | Full forensic analysis platform; used for examination rather than acquisition |

> 📎 *Slide reference: `02_terms.pdf` — Forensic Imaging & Tools*

---

## 10. Trusted Tools

A forensic investigator must **never use tools found on the suspect's own system**:
- The suspect may have compiled a **modified version** of a standard tool (e.g., a `ls` or `dd` that skips or alters specific regions)
- Shared libraries used by the tools may be **compromised at the OS level** (rootkits modifying system calls)

### The Trusted Tool Hierarchy

| Level | Method | Trust Level |
|-------|--------|-------------|
| 1 | Tools from the **suspect's machine** using suspect's OS and libraries | Lowest |
| 2 | **Investigator's binaries on a USB drive**, run under the suspect's OS | Partial — executables trusted but kernel may not be |
| 3 | Full **forensic Linux distribution booted from investigator's media** (Kali, CAINE, Tsuruji) | Highest — suspect's kernel is bypassed entirely |

> 📎 *Slide reference: `02_terms.pdf` — Tools & Trust*

---

## 11. Typical Forensic Investigation Scenarios

| Scenario | Key Evidence Sources | Challenge |
|----------|---------------------|-----------|
| **Internal network abuse** | Firewall logs, DNS logs, proxy logs, employee workstation | Balancing privacy rights with abuse detection; scope limitation |
| **Online fraud / banking malware** | Anomalous transaction logs; keylogger artefacts; unusual process tree on victim machine | Reconstructing initial infection vector; correlating bank server logs with endpoint artefacts |
| **Unauthorised data exfiltration** | Server access logs; file system metadata; email logs; network traffic | Proving *what* was taken, *when*, and *by whom* |
| **Malware infection extent** | Log artefacts, file system traces, registry entries (Windows), cron jobs (Linux) | Malware may have self-deleted; must rely on secondary artefacts |

The output of forensic analysis is **dual-purpose**: it supports legal proceedings *and* enables the organisation to understand the attack path and prevent recurrence.

> 📎 *Slide reference: `02_terms.pdf` — Forensic Scenarios*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Digital Evidence** | Any digital data that can support conclusions in a legal or organisational investigation |
| **Chain of Custody** | Complete documented history of all evidence handling from discovery through to final verdict |
| **Forensic Image** | Bit-for-bit copy of a storage device created using forensically sound tools and procedures |
| **Write Blocker** | Hardware or software device that prevents write operations to a storage medium during acquisition |
| **Hash / Digest** | Fixed-length cryptographic fingerprint of data; used to verify that no modification has occurred |
| **Timeline** | Chronological reconstruction of events based on correlated timestamps from multiple sources |
| **NSRL** | National Software Reference Library — US government database of hashes of known-good software |
| **Slack Space** | Unused bytes at the end of an allocated disk cluster that may contain remnants of deleted data |
| **Live Acquisition** | Forensic acquisition performed on a running system to capture volatile data (RAM, network state) |
| **Static Acquisition** | Forensic acquisition performed on a powered-off device; captures only persistent storage |
| **atime** | File system "last accessed" timestamp — modified whenever a file is read; forensically sensitive |
| **Repeatable** | A forensic property: the same results can be independently produced from the same evidence by a third party |

---

## Summary

- Digital evidence is present in **virtually every modern investigation**: computer forensics skills are universally required.
- All forensic work must be **sound, repeatable, documented, and non-altering** — failure in any dimension can invalidate evidence in court.
- The six investigative questions (what, who, when, where, why, how) and **timeline reconstruction** are the structural backbone of any investigation.
- **Digital evidence is fragile**: normal system interaction modifies metadata; physical threats (magnetic fields, fingerprints) can damage storage media.
- The **chain of custody** must be unbroken in both its physical and logical dimensions; a single undocumented step is sufficient to challenge admissibility.
- **Write blockers** and **cryptographic hashing** (SHA-256 minimum; MD5 alone is insufficient) are the primary technical mechanisms protecting evidence integrity.
- Forensic tools must come from the **investigator's own trusted kit**, not from the suspect's machine; the gold standard is booting from the investigator's own forensic OS.
