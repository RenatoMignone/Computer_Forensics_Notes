# Lecture 5 – Investigation Phases: Acquisition & Examination
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:**  
- `Slides/Atzeni/03_investigation_phases.pdf`  
- `Slides/Atzeni/03b_Forensic-USB-Drive-Acquisition.pdf`  
- `Slides/Atzeni/Digital-Forensics-Case-Study.pdf`

---

## Overview
This lecture continues the five-phase forensic investigation framework, covering **Phase 3 – Acquisition** and **Phase 4 – Examination/Evaluation** in depth. The lecture includes a practical walkthrough of forensic USB acquisition using `dd` and `dc3dd`, and concludes with general advice on report writing (Phase 5 – Presentation).

---

## 1. Phase 3 – Acquisition

**Acquisition** is the process of creating a **forensically sound copy** of the collected evidence using **trusted tools** in a controlled environment (usually the forensic lab).

The core principle: *never work directly on original evidence*. All examination and analysis must be performed on **forensic copies (images)**. The original must be preserved and re-hashed periodically to prove it has not been modified.

### Acquisition Without Lab Access (Field Acquisition)
When the environment requires it (e.g., a server that cannot be physically removed), acquisition can occur on-site using a **forensic workstation and write blocker** brought to the scene.

---

## 2. The Trusted Tool Hierarchy

When connecting to a potentially compromised system, the **investigator cannot trust the tools installed on the suspect's machine**. Malware, rootkits, or user modifications could make system commands return manipulated output.

The trusted tool hierarchy resolves this:

| Level | Method | Trust Level | Scenario |
|-------|--------|-------------|---------|
| 1 | **Use suspect's installed tools** | Lowest — output may be manipulated | Emergency/no alternative |
| 2 | **Mount investigator's USB** with pre-built trusted binaries (e.g., SysInternals Suite on Windows) | Medium — OS kernel still suspect, but executables are clean | Practical for most investigations |
| 3 | **Boot from investigator's forensic OS** (e.g., Kali, CAINE, Tsuruji) via USB | Highest — full OS under investigator control | Gold standard |

> **Key insight**: even if the OS kernel has been compromised (rootkits modifying system calls), booting from an external forensic OS bypasses the installed kernel entirely.

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Trusted Tool Hierarchy*

---

## 3. Static vs Live Acquisition

Before proceeding with acquisition, the investigator must decide whether to perform a **live** or **static** acquisition.

| Criterion | Static Acquisition | Live Acquisition |
|-----------|-------------------|-----------------|
| **System state** | Powered off; only disk image is captured | System running; RAM and network state also captured |
| **Volatility** | Does not capture RAM or running processes | Captures volatile data (RAM, open files, active connections) |
| **Risk of modification** | Lower — minimal exposure to running software | Higher — system interaction can modify metadata |
| **Use case** | Default choice when no volatile evidence is critical | Needed when encryption keys, running processes, or network connections are key evidence |
| **Encryption impact** | Encrypted at rest — content may be inaccessible | Encryption keys may be in RAM; can capture the decrypted state |

### Encryption and Live Acquisition
If a device's storage is **encrypted** and the system is **currently unlocked**, the keys are almost certainly in RAM. Powering down the device would lose the keys and render the data inaccessible. In this scenario:
- Perform live RAM acquisition first
- Then capture disk image while live (or perform forensic copy via OS-level access)

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Live vs Static Acquisition*

### Cryogenic RAM Extraction
In cases where the system is powered off but there is reason to believe critical data was in RAM:
- Immediately after power-off, DRAM transistors retain charge for a period at room temperature
- **Cryogenic cooling** (placing the RAM modules in a cryogenic bag — well below −200°C) can significantly extend this retention period
- The cooled modules are then physically transferred to a forensic workstation for extraction
- This technique requires specialist equipment (a cryogenic bag) but is viable when the resources are available

---

## 4. Hashing in Acquisition

Every forensic acquisition must be accompanied by cryptographic **hash verification** to establish integrity.

### Requirements for Forensic Hashing

| Requirement | Explanation |
|-------------|-------------|
| **Hash the source before acquisition** | Establishes the baseline state of the original |
| **Hash the image after acquisition** | Must match the source hash to confirm faithful copying |
| **Hash must match** | If hashes differ, the image is invalid as evidence |
| **Use strong algorithms** | MD5 is **not sufficient** alone due to collision vulnerability |
| **Prefer SHA-2 (SHA-256)** | Industry standard for current forensic practice |
| **Multiple algorithms (belt and suspenders)** | Some jurisdictions require or recommend hashing with multiple algorithms simultaneously |

### Why MD5 Is Insufficient
MD5 was broken: it is computationally feasible to **generate two different files with the same MD5 hash**. This means a defence team could potentially argue that the forensic image is a fabricated file that was crafted to match the original's hash. SHA-256 (or higher) does not have this vulnerability at present.

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Hashing & Integrity*

---

## 5. Forensic Acquisition Tools

### 5.1 `dd` – Unix Disk Duplicator

`dd` is a standard Unix utility for creating raw byte-for-byte copies of block devices.

**Basic forensic usage:**
```bash
dd if=/dev/sdb of=usbimage.dd bs=512
```

| Parameter | Meaning |
|-----------|---------|
| `if=` | Input file — the source device (e.g., `/dev/sdb` for a USB drive) |
| `of=` | Output file — the destination image file |
| `bs=512` | Block size — 512 bytes per block (matches typical sector size) |

**Limitations of `dd`:**
- Does not natively compute hashes of source or destination
- No built-in verification
- Must run separate `sha256sum` commands on both before and after

> 📎 *Slide reference: `Slides/Atzeni/03b_Forensic-USB-Drive-Acquisition.pdf`*

### 5.2 `dc3dd` – Forensic Extension of `dd`

`dc3dd` is a forensic evolution of `dd` that adds capabilities required for sound forensic acquisition.

**Key improvements over `dd`:**
- Integrated hashing (SHA-256 and other algorithms) computed during the copy — no separate hash step needed
- Automatic hash log file generation
- Progress reporting
- Documented handling of read errors

**Example with hashing:**
```bash
dc3dd if=/dev/sdb hof=usbimage.dd hash=sha256 log=acquisition.log
```

This command:
- Reads from `/dev/sdb`
- Writes the image to `usbimage.dd`
- Computes a SHA-256 hash during copying
- Writes a log of the operation

### 5.3 FTK Imager

**FTK Imager** is a widely-used GUI-based forensic imaging tool:
- Runs on Windows
- Creates forensic images in multiple formats (`.dd`, `.E01`, `.AFF`)
- Computes hashes automatically
- Provides a drive preview without mounting (preview is read-only)
- Creates a detailed acquisition report with chain of custody fields

> 📎 *Slide reference: `Slides/Atzeni/03b_Forensic-USB-Drive-Acquisition.pdf`*

---

## 6. Practical Walkthrough – USB Drive Acquisition

### Lab Setup
| Component | Purpose | Example |
|-----------|---------|---------|
| **Forensic workstation** | Trusted OS for running acquisition tools | Kali Linux, CAINE, Tsuruji |
| **Write blocker** | Prevents *any* write commands from reaching the suspect device | Hardware write blocker (Tableau, Wiebetech) |
| **Suspect device** | The evidence to be imaged | USB drive seized from the scene |
| **Forensic storage device** | Destination for the image; must be pre-wiped | Dedicated forensic hard drive |

### Step-by-Step Procedure

1. **Pre-wipe forensic storage** with verified zeros (ensures no contamination from prior cases)
2. **Connect write blocker** between suspect USB and forensic workstation
3. **Identify device node** of the suspect USB: `lsblk`, `dmesg | tail`
4. **Hash the source before imaging**:
   ```bash
   sha256sum /dev/sdb > usbimage_pre_hash.txt
   ```
5. **Create the forensic image**:
   ```bash
   dc3dd if=/dev/sdb hof=usbimage.dd hash=sha256 log=acquisition.log
   ```
6. **Hash the image after creation** (should match the pre-hash):
   ```bash
   sha256sum usbimage.dd > usbimage_post_hash.txt
   diff usbimage_pre_hash.txt usbimage_post_hash.txt
   ```
7. **Document all chain of custody fields** (see below)
8. **Seal original** in an evidence bag; label with case number and action performed

### Chain of Custody Fields Required at Acquisition

| Field | Example Value |
|-------|---------------|
| Date and time | 2025-03-15 14:32:00 UTC+1 |
| Operator name and role | Dr. Mario Rossi, Forensic Analyst |
| Location | Forensic Lab, Room 104 |
| Witnesses | Lt. Carla Bianchi (Carabinieri RIS) |
| Evidence identifier | USB-01, Samsung FIT MUF-256AB, S/N: XXXXX |
| Source hash (pre) | sha256:a4b3c2... |
| Image hash (post) | sha256:a4b3c2... |
| Tool name and version | dc3dd v7.2.641-dev |
| Hardware write blocker | Tableau T8-R2, Firmware v1.03 |

> 📎 *Slide reference: `Slides/Atzeni/03b_Forensic-USB-Drive-Acquisition.pdf`*

### Common Pitfalls During Acquisition

| Mistake | Consequence |
|---------|-------------|
| Mounting the drive without a write blocker | Access time metadata (atime) modified on every file read; integrity compromised |
| Using MD5 alone for hashing | Theoretically forgeable; may be challenged in court |
| Power failure during imaging | Corrupted or partial image; timestamp inconsistencies |
| Imaging to a non-pre-wiped destination | Destination may contain data from a previous case; risks contamination claims |
| Missing timezone in timestamps | Logs from different systems cannot be correlated without timezone |
| Undocumented interruptions | If the acquisition was paused or restarted, this must be recorded |

---

## 7. Phase 4 – Examination & Evaluation

**Examination** is the analytical work performed on forensic copies (never on originals) to extract findings, correlate evidence, and build a narrative of events.

### Primary Goal
The examiners must determine:
- **What happened** (the sequence of events)
- **Who did it** (attribution)
- **When** (construction of a timeline)
- **How** (means and method)
- **Why / motive** (inferred from available evidence)

### 7.1 Authenticity vs Integrity

| Concept | Meaning |
|---------|---------|
| **Integrity** | The data has not changed since acquisition (verified by matching hashes) |
| **Authenticity** | The data genuinely originates from the claimed source and has not been fabricated |

Hashing proves integrity. Authenticity is harder: it requires contextual corroboration — multiple evidence sources pointing to the same conclusion.

### 7.2 Deep Fake & Manufactured Evidence
In the modern environment, AI-generated media (images, audio, video) represents a significant authenticity challenge.

**Indicators of manipulation to look for:**
- **Inconsistent metadata**: a file's embedded timestamps or internal data may contradict observable details (e.g., a clock visible in a photo showing a different time than the file's metadata states)
- **Implausible or physically impossible details**: AI-generated images may contain errors a human would not produce (e.g., a person shown performing a physically impossible action)

**Cross-correlation as a defence:**
If a suspect claims: *"This meeting never took place"*, and investigators have:
- A photo (could be faked)
- A logged entry at an access-controlled building (harder to fake)
- A cell tower ping for the involved phone (from ISP records)
- Witness testimony

...then the confluence of independent evidence sources all pointing to the same fact significantly raises the evidentiary weight even if any single piece could theoretically be manipulated.

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Examination Phase*

### 7.3 Timeline Construction

A timeline maps every recovered event to a timestamp, creating a **chronological narrative** of the investigation.

**Sources for timeline entries:**
- **File system metadata**: creation, modification, access times (be careful — `atime` can be very easily altered)
- **Application logs**: browser history, email timestamps, document "last modified"
- **System event logs** (Windows Event Log, Unix `syslog`, `auth.log`)
- **Server-side logs**: web server access logs, firewall logs, database logs
- **Email headers**: `Received:` header chain reveals relay timestamps
- **Network traffic captures**: each packet has a timestamp from the capture device's clock
- **Mobile device records**: call logs, SMS timestamps, location history

**Note on clock skew**: different systems may have unsynchronised clocks. A key forensic task is to identify each system's clock offset against a trusted reference (e.g., NTP server) and apply corrections when constructing cross-system timelines.

### 7.4 Anti-Forensics
Suspects and adversaries may take deliberate steps to hinder investigation:

| Anti-forensic Technique | Effect | Investigator Response |
|------------------------|--------|----------------------|
| **Encryption at the OS level** | Storage encrypted by default in modern OSes; data unreadable without the decryption key | Live acquisition to capture keys from RAM while the system is unlocked |
| **HTTPS / TLS** | Application-layer network traffic is encrypted; IDS and traffic-based monitoring cannot inspect payloads | Endpoint acquisition; server-side logs; DNS queries may still be visible |
| **File deletion and data wiping** | Deliberate removal or overwriting of data before investigators arrive | Recovery may still be possible from unallocated space or residual artefacts depending on the media and method used |

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Anti-Forensic Techniques*

### 7.5 Legal and Ethical Constraints During Examination
Even once evidence is legally obtained, the **examination scope may be limited**:
- In labour law disputes (e.g., corporate forensics), employees retain privacy rights; access to personal documents stored on company devices may require specific legal authorisation
- Examining communications (emails, instant messages) may require a warrant beyond the initial seizure warrant
- **Over-scoping** an examination (looking at areas not authorised by the warrant) can result in evidence being inadmissible

### 7.6 Iterative Hypothesis Formation
Examination is not a single-pass activity. The process is:
1. Form an initial **hypothesis** about what happened
2. Gather evidence that could either **confirm or refute** the hypothesis
3. **Update the hypothesis** based on new findings
4. Repeat until a consistent narrative is established

This scientific approach prevents confirmation bias (only looking for evidence that confirms the initial assumption).

---

## 8. Phase 5 – Presentation / Reporting

### Core Principle: Know Your Audience
The same investigation findings must be communicated differently to different recipients:

| Audience | Report Focus |
|----------|-------------|
| **Technical team** | Full technical detail, commands run, tool versions, raw hashes, technical timeline |
| **Legal/prosecution team** | Evidence mapped to legal elements of the offence; chain of custody verification |
| **Judge / jury** | Plain-language explanation of key findings; avoid jargon; visual aids |
| **Corporate executive (C-suite)** | Business impact; what data was at risk; what actions are recommended |

### Report Integrity
The report itself is part of the **chain of custody**:
- Must be signed/dated by the forensic analyst(s)
- Should include a version history if revised
- Any subsequent corrections must be documented as addenda, not silent changes

### Quality Assurance
Before finalising a report:
- A second forensic analyst should **independently verify** the findings
- This "double-check" step protects against individual errors and bias
- Any discrepancies between analysts must be resolved before submission

> 📎 *Slide reference: `Slides/Atzeni/03_investigation_phases.pdf`, slide: Presentation Phase*

---

## 9. Case Study Exercise (Introduced)

Towards the end of the lecture, Atzeni briefly introduced a simplified forensic scenario for students to reflect on:

**Scenario (summary):** A suspect inside an organisation used a USB pen drive to exfiltrate sensitive financial spreadsheets. The scenario focuses on the acquisition phase — identifying the USB drive, deploying a write blocker, and creating a verified forensic image. This was framed as a simplified example; Atzeni noted that real investigations are almost never this straightforward.

The full interactive case study was uploaded to the course portal (*Digital-Forensics-Case-Study.pdf*) as an exercise for the following session. Students were invited to reason through the investigation steps, hypothesise about evidence sources, and raise questions for group discussion.

> 📎 *Slide reference: `Slides/Atzeni/Digital-Forensics-Case-Study.pdf` — Case Study*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Acquisition** | Creating a forensically sound, bit-for-bit copy of evidence; never working on originals |
| **Static acquisition** | Acquiring data from a powered-off device; captures only persistent storage |
| **Live acquisition** | Acquiring data from a running device; captures RAM, network state, decrypted data |
| **Trusted tool hierarchy** | The principle that tools used during investigation must be from a trusted source, not the suspect's system |
| **`dd`** | Unix byte-for-byte disk copy utility; basic forensic imaging tool |
| **`dc3dd`** | Forensic extension of `dd` with integrated hashing, log file output, and progress reporting |
| **FTK Imager** | GUI-based Windows forensic imaging tool supporting multiple image formats |
| **SHA-256** | Cryptographic hash function; preferred standard for forensic integrity verification |
| **MD5** | Older hash function; insufficient alone due to known collision vulnerabilities |
| **Cryogenic acquisition** | Preservation of RAM at near absolute-zero temperatures to extend transistor charge retention |
| **Timeline reconstruction** | Cross-correlation of evidence timestamps from multiple sources to produce a chronological narrative |
| **Deep fake detection** | Assessment of whether digital media (images, video, audio) may have been synthetically generated or manipulated; requires both technical inspection and cross-correlation with independent evidence sources |
| **Anti-forensics** | Deliberate techniques used to hinder, mislead, or prevent forensic investigation |
| **Clock skew** | Difference between a device's internal clock and a trusted time reference; must be corrected in multi-system timelines |

---

## Summary

- **Acquisition** creates a forensically sound image of the original evidence; no analysis is ever performed on originals.
- The choice between **live vs static acquisition** depends on whether critical data (e.g., encryption keys) resides in RAM.
- All acquisitions require **hashing before and after** using SHA-256 (MD5 alone is insufficient).
- `dd` provides raw copying; `dc3dd` adds integrated hashing and logging; **FTK Imager** provides a GUI with chain-of-custody report generation.
- The **trusted tool hierarchy** ensures that investigator tools are not subject to manipulation by OS-level rootkits.
- **Examination** involves timeline construction from multiple independent evidence sources; single-source evidence is always weaker.
- **Anti-forensic techniques** (encryption, HTTPS, data wiping) must be anticipated; the response is multi-source correlation and live acquisition.
- Reports must be tailored to their audience and their integrity protected by the chain of custody.
