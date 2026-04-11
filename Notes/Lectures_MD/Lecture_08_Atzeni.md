# Lecture 8 – Digital Forensics Case Study: Debrief & Prefetch Analysis

**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/Digital-Forensics-Case-Study_partial.pdf`

---

## Overview

Lecture 8 was structured as a workshop and debrief session around the case study distributed during Lecture 7. Prof. Atzeni released an updated version of the scenario on the course portal — including more specific data on evidence sources, a partial timeline, and interpretation prompts — and students worked through it in class. Atzeni then debriefed one possible reconstruction of events, covering the evidence chain, the timeline, the identification of the suspect, and the investigative conclusions. A focused technical digression explained **Windows Prefetch files** as a forensic artefact class, prompted by their central role in reconstructing the suspect's actions.

---

## 1. Case Study Scenario

### 1.1 Scenario

| Element | Detail |
|---------|--------|
| **Victim organisation** | Shockwave Analytics — specialises in predictive threat detection tools for the finance sector |
| **Central asset** | Project Triton — a machine learning engine representing a significant competitive advantage |
| **Triggering event** | Competitor Basel Core System announced a new product with architectural similarities to Project Triton far beyond coincidence |
| **Suspect** | John Matthews — senior software engineer at Shockwave Analytics |
| **Nature of incident** | Insider intellectual property exfiltration |

### 1.2 Investigative Goal

The investigation targets the five standard forensic questions:

| Question | Applied to this scenario |
|----------|--------------------------|
| **Who** | Whether John acted alone, was assisted, or was compromised |
| **Where** | Physical or logical location of the actions |
| **When** | Timeline of events |
| **How** | Technical method of exfiltration |
| **Why** | Motive |

### 1.3 Initial Phases Already Completed

By the time of the lecture debrief, the first investigation phases had already been accomplished:
- **Identification** of evidence sources
- **Collection** and **Acquisition**

Evidence sources collected:

| Source | Type |
|--------|------|
| John's company laptop | Endpoint device |
| Firewall logs | Network infrastructure |
| File server logs | Network infrastructure |
| Windows security and event logs | Endpoint / OS |
| Email server logs | Infrastructure |
| HR records | Administrative |

---

## 2. Windows Prefetch Files

### 2.1 Purpose

**Prefetch files** are created by Windows to speed up application startup. When an application is launched, Windows records the executable and its dependencies so they can be pre-loaded into memory before the next launch, making the application appear to start faster.

### 2.2 Location and Naming

- **Location**: `C:\Windows\Prefetch\`
- **Naming format**: `[PROGRAMNAME]-[HASH].pf`
  - The hash is derived from the **full executable path** — not just the filename
  - Example: a single program installed in two different locations produces two distinct prefetch entries

### 2.3 Forensic Content

| Field | Forensic Value |
|-------|----------------|
| **Executable name** | Identifies which program was run |
| **Execution count** | Number of times the application has been launched |
| **Last run timestamp** | Most recent execution time — primary timeline artefact |
| **Up to 8 recent timestamps** | Available in more recent Windows versions; allows finer timeline reconstruction |
| **Dependency list** | Files accessed at startup — can indicate what data the application touched |
| **Volume information** | Identifies the drive from which the executable was launched |

### 2.4 Forensic Significance

- A prefetch file **persists even after the executable is deleted** — the `.pf` entry remains in `Windows\Prefetch\` even if the tool has been removed from the system
- **Volume information** can confirm whether a tool was run from an external USB drive rather than the internal system drive — a common pattern when an attacker wants to avoid leaving executables on the host
- Prefetch entries from multiple tools, combined with timestamps, allow reconstruction of a **behavioural sequence** — identifying execution patterns consistent with a specific type of attack
- Prefetch files are **not well known to casual users**, making them a reliable source of evidence against suspects who are not forensically aware

> 📎 *Slide reference: `Digital-Forensics-Case-Study_partial.pdf` — Prefetch Files*

---

## 3. Timeline Reconstruction

### 3.1 Pre-Exfiltration Phase

| Event | Evidence Source | Interpretation |
|-------|----------------|----------------|
| John begins searching for external job opportunities | Laptop image — browser history | Establishes window of opportunity and financial motivation |
| John searches for "non-compete enforceability" | Laptop image — browser history | Researching the legal consequences of joining a competitor |
| John submits formal resignation | HR records | Marks start of notice period — access privileges still active |

### 3.2 Reconnaissance and Testing

| Date | Event | Evidence Source | Interpretation |
|------|-------|----------------|----------------|
| **8 March** | Unusual system access at after-work hours | Access logs | Anomalous timing — suspect activity outside normal working hours |
| **8 March** | Prefetch entry created for `7zfm.exe` (7-Zip File Manager) | Windows Prefetch — `7ZFM-[HASH].pf` | Testing whether compression tool functions; no actual compression performed — interpreted as a dry run |

### 3.3 Exfiltration Phase

| Event | Evidence Source | Interpretation |
|-------|----------------|----------------|
| **10 March** — large USB drive connected to laptop | USB connection logs / Windows device logs | First insertion of the exfiltration device |
| **10 March** — operations on Project Triton files on file server | File server logs | Access and staging of target intellectual property |
| **10 March** — suspect folder created | File server / laptop file system | John stages files under a labelled folder — itself a forensic artefact |
| Encrypted archive created | Prefetch (compression tool), MFT of NTFS, Windows registry | Project Triton data compressed and encrypted before exfiltration |
| John searches "how to send large email with Gmail" | Laptop image — browser history | Researching email exfiltration channel |
| Encrypted archive copied to USB drive | USB logs, file system | First exfiltration channel used |
| Encrypted archive sent to personal Gmail account | Firewall logs, email server logs | Second exfiltration channel — redundant method to ensure delivery |
| Just after midnight — firewall flags unusually large outbound data transfer (multiple gigabytes) | Firewall logs | Anomalous traffic volume detected; content encrypted but volume itself is suspicious |
| Shortly after — `eraser.exe` run | Windows Prefetch | Attempt to destroy traces; interpreted as consciousness of guilt |
| Final week — USB inserted again | USB connection logs | No further data operations observed |

> *The use of both USB and email as exfiltration channels is interpreted as a redundancy measure — John wanted to ensure at least one delivery method succeeded. The practical effect was to double the forensic evidence available.*

> 📎 *Slide reference: `Digital-Forensics-Case-Study_partial.pdf` — Timeline*

---

## 4. Investigative Conclusions

### 4.1 Who

John Matthews acted **alone**. The following alternative scenarios were considered and ruled out:

| Hypothesis | Evidence outcome |
|------------|-----------------|
| Basel Core System actively involved | No log evidence of Basal Core involvement in any system |
| John compromised by malware or remote adversary | No malware indicators, no C2 connections, no suspicious inbound traffic, no antivirus alerts, no anomalous activity from any other agent |
| John used by a more sophisticated inside actor as a proxy | No log evidence; all artefacts point exclusively to the John Matthews user profile |

> *"Artifact shows only the involvement of John Matthew user profile, no particularly actions from the basal core organization."*

### 4.2 Where

John was **physically present at company premises** outside normal working hours (after colleagues had left). An alternative — remote access via SSH or Remote Desktop — was discussed as a technically feasible scenario but is **not corroborated by the available logs**.

### 4.3 When

The exfiltration itself occurred over **two days in John's final week of work**. The pre-exfiltration phase (job searches, resignation) extends earlier but the IP theft was concentrated in a short window.

### 4.4 How

- **Target**: Project Triton files on the file server
- **Method**: Staged locally → compressed and encrypted with 7-Zip → exfiltrated via two channels: USB drive and personal Gmail
- **Anti-forensics**: attempted trace deletion with `eraser.exe` — unsuccessful, as traces remained in prefetch files, MFT, Windows registry, and firewall logs

### 4.5 Why

**Financial motivation and career advancement**: John sought a better salary and used privileged access to Project Triton to provide proprietary data to Basel Core, which had announced a product with striking architectural similarities.

---

## 5. Forensic Awareness Assessment

Prof. Atzeni characterised John Matthews as **not forensically aware**:

- Did not know that prefetch files persist after deletion of the tools they reference
- Did not clear MFT or Windows registry entries following operations
- Applied `eraser.exe` narrowly, leaving multiple artefact classes intact
- Using two exfiltration channels created redundant evidence rather than reducing it

The attempt to destroy evidence using `eraser.exe` is itself forensically significant: it constitutes **consciousness of guilt** — awareness of wrongdoing and a deliberate effort to conceal it.

> *"From a forensic perspective is not a big challenge this kind of case — we can find pretty easily evidences of his actions."*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Prefetch file** | Windows performance file recording application execution details; persists after executable deletion; stored in `C:\Windows\Prefetch\` |
| **7zfm.exe** | 7-Zip File Manager executable; used to compress and encrypt the exfiltrated archive |
| **eraser.exe** | Secure deletion tool run by John Matthews in an attempt to destroy traces; the attempt was unsuccessful |
| **MFT (Master File Table)** | NTFS structure recording metadata for every file and directory; retains records of deleted files and is a primary forensic artefact |
| **Consciousness of guilt** | Legal concept: deliberate post-crime attempts to destroy evidence are themselves indicative of knowing wrongdoing |
| **Anti-forensics** | Techniques used to hinder forensic investigation; here: file deletion and use of `eraser.exe` |
| **Exfiltration** | Unauthorised transfer of data outside an organisation's control |
| **Project Triton** | The machine learning engine and intellectual property at the centre of the Shockwave Analytics insider theft |

---

## Summary

- The lecture debriefed the **Shockwave Analytics / John Matthews** case study, with Atzeni presenting one detailed reconstruction of events as one of several valid scenarios.
- **Windows Prefetch files** are a key forensic artefact: they record application execution — including tools later deleted — with timestamps and volume information that can reveal execution from external USB drives.
- The investigation confirmed John Matthews as the sole actor; external involvement, malware compromise, and proxy scenarios were all ruled out on the basis of log evidence.
- The exfiltration used two redundant channels (USB + personal Gmail encrypted archive), which doubled the available forensic evidence.
- `eraser.exe` was run post-exfiltration but failed to remove traces from prefetch files, MFT, Windows registry, and firewall logs.
- The anti-forensics attempt itself constitutes **consciousness of guilt** — a legally significant indicator of intentional wrongdoing.
- Forensic reconstruction answered all five questions: **who** (John Matthews, alone), **where** (company premises), **when** (two-day window in final work week), **how** (encrypted 7-Zip archive via USB + Gmail), **why** (financial and career motivation).
