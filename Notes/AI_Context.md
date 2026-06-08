# AI_Context.md

> **Purpose of this file**: Persistent context for AI assistants. When new lectures or slides are added to this project, hand this file to a new AI session along with the new materials. The AI should be able to read this file and immediately continue working with no prior conversation history.

---

## Project Purpose

This is a university lecture notes project for the course **Computer Forensics and Cybercrime Analysis (CFCCA)**, part of an **MSc in Cybersecurity** (2nd Year, 2nd Semester, 8 CFU).

The course is taught by two professors covering complementary perspectives:
- **Prof. Atzeni** — Computer Science / Technical track (forensic methodology, investigation phases, tools, acquisition)
- **Prof. Vaciago** — Law / Legal track (cybercrime law, conventions, jurisdiction, data retention, digital evidence admissibility)

The project generates two types of structured Markdown notes from raw lecture transcriptions. Slide PDFs are used only as structural/reference aids; substantive note content must be supported by the transcriptions.
1. **Per-lecture notes** (`Lectures_MD/`) — one file per lecture, following the chronological lecture order
2. **Per-chapter notes** (`Chapters_MD/`) — one file per slide deck / topic, aggregating relevant content across all lectures from that professor

---

## Directory Structure

```
.
├── Lectures_txt/              # READ ONLY — raw audio-to-text transcriptions of each lecture
├── Lectures_MD/               # Per-lecture structured Markdown notes (one file per lecture)
├── Chapters_MD/
│   ├── Atzeni/                # Chapter notes for Prof. Atzeni, grouped by slide deck / topic
│   └── Vaciago/               # Chapter notes for Prof. Vaciago, grouped by slide deck / topic
├── Side_Events_MD/            # Dedicated notes for guest/non-slide side events
├── Side_Events_Index.txt      # Index of presentations, labs, homework feedback, and admin material
├── Slides/
│   ├── Atzeni/                # PDF slide decks from Prof. Atzeni
│   └── Vaciago/               # PDF slide decks from Prof. Vaciago
├── README.md                  # GitHub repository description
└── AI_Context.md              # This file
```

### Folder Roles

| Folder | Role | Editable? |
|--------|------|-----------|
| `Lectures_txt/` | Raw transcriptions — source material only | READ ONLY |
| `Lectures_MD/` | Chronological per-lecture notes; one file per lecture session | Yes (output) |
| `Chapters_MD/Atzeni/` | Thematic chapter notes for Atzeni; aggregated across lectures | Yes (output) |
| `Chapters_MD/Vaciago/` | Thematic chapter notes for Vaciago; aggregated across lectures | Yes (output) |
| `Side_Events_MD/` | Full notes for guest sessions and non-slide side events | Yes (output) |
| `Side_Events_Index.txt` | Master index of presentations, labs, homework feedback, guest sessions, and admin material | Yes (output) |
| `Slides/Atzeni/` | Atzeni's slide PDFs — used as structural skeleton for notes | READ ONLY |
| `Slides/Vaciago/` | Vaciago's slide PDFs — used as structural skeleton for notes | READ ONLY |

---

## Professors & Their Materials

### Prof. Atzeni — Technical Track

**Lectures:**
| File | Topic |
|------|-------|
| `Lectures_txt/Lecture_01_Atzeni_24-02_.txt` | Introduction to Computer Forensics & the Morris Worm |
| `Lectures_txt/Lecture_02_Atzeni_25-02_.txt` | Digital Evidence, Chain of Custody & Data Acquisition |
| `Lectures_txt/Lecture_04_Atzeni_03-03_.txt` | Investigation Phases – Part I: Identification & Collection |
| `Lectures_txt/Lecture_05_Atzeni_04-03_.txt` | Investigation Phases – Part II: Acquisition & Examination |
| `Lectures_txt/Lecture_07_Atzeni_10-03_.txt` | Write Blocker Tools & Scene Assessment |
| `Lectures_txt/Lecture_08_Atzeni_11-03_.txt` | Digital Forensics Case Study: Debrief & Prefetch Analysis |
| `Lectures_txt/Lecture_10_Atzeni_17-03_.txt` | Untrusted Domains and Malware Infection Vectors |
| `Lectures_txt/Lecture_11_Atzeni_18-03_.txt` | Memory Exploitation, Supply Chain Attacks, and APTs |
| `Lectures_txt/Lecture_13_Atzeni_24-03_.txt` | Forensic Lab Setup and Tools Requirements |
| `Lectures_txt/Lecture_14_Atzeni_25-03_.txt` | Advanced Lab Resilience and Technical Requirements |
| `Lectures_txt/Lecture_15_Atzeni_31-03_.txt` | Fundamentals of File System Forensics |
| `Lectures_txt/Lecture_17_Atzeni_10-04_.txt` | File System Forensics II: Metadata & FAT |
| `Lectures_txt/Lecture_18_Atzeni_14-04_.txt` | File System Forensics III: Slack Space and FAT Recovery |
| `Lectures_txt/Lecture_20_Atzeni_21-04_.txt` | NTFS, forensic copying, slack space, data carving, and SSD introduction |
| `Lectures_txt/Lecture_21_Atzeni_22-04_.txt` | SSD acquisition, data sanitisation, and network forensics introduction |
| `Lectures_txt/Lecture_23_Atzeni_28-04_.txt` | Network forensics, OSINT, social media evidence, and homework presentation |
| `Lectures_txt/Lecture_24_Atzeni_05-05_.txt` | Network anti-forensics and attack obfuscation |
| `Lectures_txt/Lecture_25_Atzeni_06-05_.txt` | TOR and cloud forensics |
| `Lectures_txt/Lecture_27_Atzeni_12-05_.txt` | Cloud forensic acquisition strategy |
| `Lectures_txt/Lecture_28_Atzeni_13-05_.txt` | OS forensics and memory acquisition |
| `Lectures_txt/Lecture_30_Atzeni_19-05.txt` | Memory forensics, LiME, Volatility, and malware indicators |
| `Lectures_txt/Lecture_31_Atzeni_22-05.txt` | Kubernetes forensics, anti-forensics, and countermeasures |
| `Lectures_txt/Lecture_33_Atzeni_27-05.txt` | Autopsy, timelines, and LLMs in digital forensics |

**Slide PDFs** (`Slides/Atzeni/`):
| File | Topic |
|------|-------|
| `01_introCF.pdf` | Introduction to Computer Forensics |
| `01b_Cybersecurity-History-MorrisWorm.pdf` | Morris Worm case study |
| `02_terms.pdf` | Digital evidence terminology and chain of custody |
| `03_investigation_phases.pdf` | Five investigation phases (Identification → Presentation) |
| `03b_Forensic-USB-Drive-Acquisition.pdf` | Practical USB acquisition walkthrough |
| `06_Digital-Forensics-Case-Study.pdf` | Insider IP exfiltration case study |
| `06_Digital-Forensics-Case-Study.pdf` | Extended case study: named scenario, prefetch analysis, detailed timeline (Lecture 08) |
| `04_Write-Blocker-Tools.pdf` | Write blocker tools: hardware, software, documentation requirements |
| `05_Scene-Assessment-and-Data-Source-Identification.pdf` | Scene assessment, OSINT, data source identification, volatility prioritisation |
| `07_untrusted_domain.pdf` | Untrusted environments, node/network compromise, LKMs |
| `07a_HTTPS-Session-Hijacking.pdf` | HTTP session hijacking & XSS |
| `07b_Man-in-the-Disk-MitD-Vulnerability.pdf` | Storage vulnerabilities and MitD |
| `08_tools_and_labs.pdf` | Forensic Lab Setup, Tool Requirements, Physical & Logical Security |
| `09_FS_forensics.pdf` | File System Fundamentals, Mounting, Device Types |
| `10_HDD-vs-SSD-in-Digital-Forensics.pdf` | HDD vs SSD forensic acquisition, TRIM, garbage collection, wear levelling |
| `11_Data-Sanitisation-Techniques.pdf` | Data sanitisation, NIST Clear/Purge/Destroy, overwriting, crypto-erase, degaussing |
| `12_Network.pdf` | Network forensics, OSINT, social media forensics, anti-forensics |
| `13_Digital-Forensics-in-the-TOR-Network.pdf` | TOR architecture, daemon, guard nodes, relay identification, traffic correlation |
| `14_Cloud.pdf` | Cloud forensics, cloud models, S3, logs, jurisdiction, redundancy, virtualisation, volatility |
| `15_OS.pdf` | Operating-system artifacts, rootkits, memory acquisition, LiME, and introductory Volatility/Rekall workflow |
| `16_volatile.pdf` | Detailed Volatility triage, process analysis, DLL/handle analysis, network analysis, malfind, registry analysis, artifact extraction, and timelines |
| `17_anti_forensics.pdf` | Anti-forensics taxonomy, examples, and countermeasures |
| `18_autopsy.pdf` | Autopsy workflow, modules, NSRL, and timelines |
| `19_LLM.pdf` | LLMs in forensic investigations and associated risks |

---

### Prof. Vaciago — Legal Track

**Lectures:**
| File | Topic |
|------|-------|
| `Lectures_txt/Lecture_03_Vaciago_27-02_.txt` | Legal Introduction: Technology, Law & Digital Forensics |
| `Lectures_txt/Lecture_06_Vaciago_06-03_.txt` | Legal Frameworks: Data Retention, Jurisdiction & Digital Evidence |
| `Lectures_txt/Lecture_09_Vaciago_13-03_.txt` | International Cooperation & The Budapest Convention |
| `Lectures_txt/Lecture_12_Vaciago_20-03_.txt` | Italian Law 48/2008 and Corporate Liability (Decree 231/2001) |
| `Lectures_txt/Lecture_16_Vaciago_01-04_.txt` | Forensic Expert Insights and the Garlasco Case Study |
| `Lectures_txt/Lecture_19_Vaciago_17-04_.txt` | The 10 Rules for a Digital Forensic Report |
| `Lectures_txt/Lecture_22_Vaciago_24-04_.txt` | Digital Alibi Feedback and the Hacking Team Case |
| `Lectures_txt/Lecture_26_Vaciago_08-05_.txt` | Malware Production, Mens Rea, and Criminal Liability |
| `Lectures_txt/Lecture_29_Vaciago_15-05.txt` | Malware-production homework feedback and professional digital forensics |
| `Lectures_txt/Lecture_32_Vaciago_26-05.txt` | Corporate forensics and the TechMed data breach laboratory |

**Slide PDFs** (`Slides/Vaciago/`):
| File | Topic |
|------|-------|
| `0_Introduction.pdf` | Technology evolution, jurisdiction, legal design, dark patterns, GDPR Art. 22 |
| `1_Definition.pdf` | Digital forensics definitions, forensic standards, evidence location model |
| `2_Cybercrime_Convention.pdf` | Budapest Convention, data retention directive, jurisdiction problem |
| `3_Law_48_08.pdf` | Italian Law 48/2008 implementing the Budapest Convention |
| `5_Rules_Digital_Forensics.pdf` | Rules for forensic expert reports and legal presentation |
| `6_Hacking_Team_Case.pdf` | Hacking Team case, spyware, SoftHack search and seizure lab scenario |
| `Articoli_Codice_Penale.pdf` | Articles 615-ter and 615-quater, malware production, and access-tool liability |
| `07_TechMed_Forensics_Law.pdf` | TechMed corporate-forensics case, BEC fraud, data breach, and organisational remediation |
| `Caso-Garlasco-digital-forensics-timeline.pdf` | Garlasco digital-forensics timeline reference package; keep aligned with side-event isolation rules |

---

## Naming Conventions

### Lecture files (`Lectures_txt/` and `Lectures_MD/`)
Pattern: `Lecture_[NN]_[Professor]_[DD-MM]_.txt` for raw transcripts and `Lecture_[NN]_[Professor].md` for structured notes.
- `[NN]` = sequential lecture number (always two digits, e.g., 01, 09, 10)
- `[Professor]` = `Atzeni` or `Vaciago`
- `[DD-MM]` = lecture date in day-month format for `Lectures_txt/`
- Example: `Lecture_04_Atzeni_03-03_.txt` = 4th lecture of the course, delivered by Atzeni on 03 March

### Chapter files (`Chapters_MD/`)
Pattern: `[SlidePrefix]_[ShortTitle].md` — mirrors the slide PDF filename
- Stored in the matching professor's subfolder (`Atzeni/` or `Vaciago/`)
- Example: `01_IntroCF.md` corresponds to `Slides/Atzeni/01_introCF.pdf`
- Example: `0_Introduction.md` corresponds to `Slides/Vaciago/0_Introduction.pdf`

### Slide → Lecture mapping (current)
| Slide PDF | Professor | Used In |
|-----------|-----------|---------|
| `01_introCF.pdf` | Atzeni | Lecture 01 |
| `01b_Cybersecurity-History-MorrisWorm.pdf` | Atzeni | Lecture 01 |
| `02_terms.pdf` | Atzeni | Lecture 02 |
| `03_investigation_phases.pdf` | Atzeni | Lectures 4 & 5 |
| `03b_Forensic-USB-Drive-Acquisition.pdf` | Atzeni | Lecture 05 |
| `06_Digital-Forensics-Case-Study.pdf` | Atzeni | Lecture 05 |
| `06_Digital-Forensics-Case-Study.pdf` | Atzeni | Lecture 08 |
| `04_Write-Blocker-Tools.pdf` | Atzeni | Lecture 07 |
| `05_Scene-Assessment-and-Data-Source-Identification.pdf` | Atzeni | Lecture 07 |
| `07_untrusted_domain.pdf` | Atzeni | Lectures 10 & 11 |
| `07a_HTTPS-Session-Hijacking.pdf` | Atzeni | Lecture 10 |
| `07b_Man-in-the-Disk-MitD-Vulnerability.pdf` | Atzeni | Lecture 10 |
| `0_Introduction.pdf` | Vaciago | Lecture 03 |
| `1_Definition.pdf` | Vaciago | Lecture 06 |
| `2_Cybercrime_Convention.pdf` | Vaciago | Lectures 06 & 09 |
| `3_Law_48_08.pdf` | Vaciago | Lecture 12 |
| `08_tools_and_labs.pdf` | Atzeni | Lectures 13 & 14 |
| `09_FS_forensics.pdf` | Atzeni | Lectures 15 & 17 |
| `10_HDD-vs-SSD-in-Digital-Forensics.pdf` | Atzeni | Lectures 20 & 21 |
| `11_Data-Sanitisation-Techniques.pdf` | Atzeni | Lecture 21 |
| `12_Network.pdf` | Atzeni | Lectures 21, 23 & 24 |
| `13_Digital-Forensics-in-the-TOR-Network.pdf` | Atzeni | Lecture 25 |
| `14_Cloud.pdf` | Atzeni | Lectures 25 & 27 |
| `15_OS.pdf` | Atzeni | Lectures 28 & 30 |
| `16_volatile.pdf` | Atzeni | Lecture 30 |
| `17_anti_forensics.pdf` | Atzeni | Lecture 31 |
| `18_autopsy.pdf` | Atzeni | Lecture 33 |
| `19_LLM.pdf` | Atzeni | Lecture 33 |
| `5_Rules_Digital_Forensics.pdf` | Vaciago | Lectures 19 & 22 |
| `6_Hacking_Team_Case.pdf` | Vaciago | Lecture 22 |
| `Articoli_Codice_Penale.pdf` | Vaciago | Lecture 26 |
| `07_TechMed_Forensics_Law.pdf` | Vaciago | Lecture 32 |
| `Caso-Garlasco-digital-forensics-timeline.pdf` | Vaciago | Reference package for Garlasco side-event material |

---

## Current State

### `Lectures_MD/` — Per-Lecture Notes

Current active generated set is Lecture 01 through Lecture 33. Lectures 29 through 33 now have transcript-backed lecture notes and matching chapter material where applicable.

| File | Status | Topic |
|------|--------|-------|
| `Lecture_01_Atzeni.md` | ✅ Complete | Introduction to Computer Forensics & the Morris Worm |
| `Lecture_02_Atzeni.md` | ✅ Complete | Digital Evidence, Chain of Custody & Data Acquisition |
| `Lecture_03_Vaciago.md` | ✅ Complete | Legal Introduction: Technology, Law & Digital Forensics |
| `Lecture_04_Atzeni.md` | ✅ Complete | Investigation Phases – Part I: Identification & Collection |
| `Lecture_05_Atzeni.md` | ✅ Complete | Investigation Phases – Part II: Acquisition & Examination |
| `Lecture_06_Vaciago.md` | ✅ Complete | Legal Frameworks: Data Retention, Jurisdiction & Digital Evidence |
| `Lecture_07_Atzeni.md` | ✅ Complete | Write Blocker Tools & Scene Assessment |
| `Lecture_08_Atzeni.md` | ✅ Complete | Digital Forensics Case Study: Debrief & Prefetch Analysis |
| `Lecture_09_Vaciago.md` | ✅ Complete | International Cooperation & The Budapest Convention |
| `Lecture_10_Atzeni.md` | ✅ Complete | Untrusted Domains and Malware Infection Vectors |
| `Lecture_11_Atzeni.md` | ✅ Complete | Memory Exploitation, Supply Chain Attacks, and APTs |
| `Lecture_12_Vaciago.md` | ✅ Complete | Italian Law 48/2008 and Corporate Liability |
| `Lecture_13_Atzeni.md` | ✅ Complete | Forensic Lab Setup and Principles |
| `Lecture_14_Atzeni.md` | ✅ Complete | Advanced Lab Resilience and Technical Requirements |
| `Lecture_15_Atzeni.md` | ✅ Complete | Fundamentals of File System Forensics |
| `Lecture_16_Vaciago.md` | ✅ Complete | Garlasco Case Study & Forensic Ethics |
| `Lecture_17_Atzeni.md` | ✅ Complete | File System Forensics II: Metadata & FAT |
| `Lecture_18_Atzeni.md` | ✅ Complete | File System Forensics: Slack Space and FAT Recovery |
| `Lecture_19_Vaciago.md` | ✅ Complete | The 10 Rules for a Digital Forensic Report |
| `Lecture_20_Atzeni.md` | ✅ Complete | NTFS, Forensic Copying, Slack Space, Data Carving, and SSD Introduction |
| `Lecture_21_Atzeni.md` | ✅ Complete | SSD Acquisition, Data Sanitisation, and Network Forensics Introduction |
| `Lecture_22_Vaciago.md` | ✅ Complete | Digital Alibi Feedback and the Hacking Team Case |
| `Lecture_23_Atzeni.md` | ✅ Complete | Network Forensics, OSINT, and Social Media Evidence |
| `Lecture_24_Atzeni.md` | ✅ Complete | Network Anti-Forensics and Attack Obfuscation |
| `Lecture_25_Atzeni.md` | ✅ Complete | TOR and Cloud Forensics |
| `Lecture_26_Vaciago.md` | ✅ Complete | Malware Production, Mens Rea, and Criminal Liability |
| `Lecture_27_Atzeni.md` | ✅ Complete | Cloud Forensics Effects and Acquisition Strategy |
| `Lecture_28_Atzeni.md` | ✅ Complete | Video Carving, OS Forensics, and Memory Acquisition |
| `Lecture_29_Vaciago.md` | ✅ Complete | Malware-Production Homework Feedback and Professional Digital Forensics |
| `Lecture_30_Atzeni.md` | ✅ Complete | Memory Forensics, LiME, Volatility, and Malware Indicators |
| `Lecture_31_Atzeni.md` | ✅ Complete | Kubernetes Forensics, Anti-Forensics, and Countermeasures |
| `Lecture_32_Vaciago.md` | ✅ Complete | Corporate Forensics and the TechMed Data Breach Laboratory |
| `Lecture_33_Atzeni.md` | ✅ Complete | Autopsy, Timelines, and LLMs in Digital Forensics |

### `Chapters_MD/Atzeni/` — Atzeni Chapter Notes

| File | Status | Corresponding Slide | Source Lectures |
|------|--------|---------------------|-----------------|
| `01_IntroCF.md` | ✅ Complete | `01_introCF.pdf` | Lecture 01 |
| `01b_MorrisWorm.md` | ✅ Complete | `01b_Cybersecurity-History-MorrisWorm.pdf` | Lecture 01 |
| `02_terms.md` | ✅ Complete | `02_terms.pdf` | Lecture 02 |
| `03_investigation_phases.md` | ✅ Complete | `03_investigation_phases.pdf` | Lectures 4 & 5 |
| `03b_Forensic-USB-Drive-Acquisition.md` | ✅ Complete | `03b_Forensic-USB-Drive-Acquisition.pdf` | Lecture 05 |
| `06_Digital-Forensics-Case-Study.md` | ✅ Complete | `06_Digital-Forensics-Case-Study.pdf`, `06_Digital-Forensics-Case-Study.pdf` | Lectures 5 & 8 |
| `04_Write-Blocker-Tools.md` | ✅ Complete | `04_Write-Blocker-Tools.pdf` | Lecture 07 |
| `05_Scene-Assessment-and-Data-Source-Identification.md` | ✅ Complete | `05_Scene-Assessment-and-Data-Source-Identification.pdf` | Lecture 07 |
| `07_untrusted_domain.md` | ✅ Complete | `07_untrusted_domain.pdf`, `07a_HTTPS-Session-Hijacking.pdf`, `07b_Man-in-the-Disk-MitD-Vulnerability.pdf` | Lectures 10 & 11 |
| `08_tools_and_labs.md` | ✅ Complete | `08_tools_and_labs.pdf` | Lectures 13 & 14 |
| `09_FS_forensics.md` | ✅ Complete | `09_FS_forensics.pdf` | Lectures 15, 17, 18 & 20 |
| `10_HDD-vs-SSD-in-Digital-Forensics.md` | ✅ Complete | `10_HDD-vs-SSD-in-Digital-Forensics.pdf` | Lectures 20 & 21 |
| `11_Data-Sanitisation-Techniques.md` | ✅ Complete | `11_Data-Sanitisation-Techniques.pdf` | Lecture 21 |
| `12_Network.md` | ✅ Complete | `12_Network.pdf` | Lectures 21, 23 & 24 |
| `13_Digital-Forensics-in-the-TOR-Network.md` | ✅ Complete | `13_Digital-Forensics-in-the-TOR-Network.pdf` | Lecture 25 |
| `14_Cloud.md` | ✅ Complete | `14_Cloud.pdf` | Lectures 25 & 27 |
| `15_OS.md` | ✅ Complete | `15_OS.pdf` | Lectures 28 & 30 |
| `16_volatile.md` | ✅ Complete | `16_volatile.pdf` | Lecture 30 |
| `17_anti_forensics.md` | ✅ Complete | `17_anti_forensics.pdf` | Lecture 31 |
| `18_autopsy.md` | ✅ Complete | `18_autopsy.pdf` | Lecture 33 |
| `19_LLM.md` | ✅ Complete | `19_LLM.pdf` | Lecture 33 |

### `Chapters_MD/Vaciago/` — Vaciago Chapter Notes

| File | Status | Corresponding Slide | Source Lectures |
|------|--------|---------------------|-----------------|
| `0_Introduction.md` | ✅ Complete | `0_Introduction.pdf` | Lecture 03 |
| `1_Definition.md` | ✅ Complete | `1_Definition.pdf` | Lecture 06 |
| `2_Cybercrime_Convention.md` | ✅ Complete | `2_Cybercrime_Convention.pdf` | Lectures 06 & 09 |
| `3_Law_48_08.md` | ✅ Complete | `3_Law_48_08.pdf` | Lecture 12 |
| `5_Rules_Digital_Forensics.md` | ✅ Complete | `5_Rules_Digital_Forensics.pdf` | Lectures 19 & 22 |
| `6_Hacking_Team_Case.md` | ✅ Complete | `6_Hacking_Team_Case.pdf` | Lecture 22 |
| `Articoli_Codice_Penale.md` | ✅ Complete | `Articoli_Codice_Penale.pdf` | Lecture 26 |
| `07_TechMed_Forensics_Law.md` | ✅ Complete | `07_TechMed_Forensics_Law.pdf` | Lecture 32 |

---

## Side Events, Presentations, and Non-Slide Material

Use `Side_Events_Index.txt` as the master map for material that happened during lectures but should not be treated as normal slide-backed chapter content. This includes student presentations, homework feedback, lab logistics, course administration, guest lectures, and professional/case digressions.

Current dedicated side-event notes:

| File | Source Lecture | Type |
|------|----------------|------|
| `Side_Events_MD/Lecture_16_Guest_Paolo_Dal_Checco_Garlasco.md` | Lecture 16 | Guest expert lecture / professional case discussion |

Isolation rule:
- `Lectures_MD/` may keep these items because they record the chronological lecture.
- `Side_Events_Index.txt` must reference them so future AI sessions can identify them quickly.
- `Chapters_MD/` should not absorb student presentations, homework feedback, exam/admin logistics, or non-slide guest/professional discussions.
- If the user explicitly wants a full note for a side event, create it under `Side_Events_MD/`, not under `Chapters_MD/`.

---

## How to Add New Lectures

When the user provides a new `.txt` transcription and/or a new slide PDF, follow these steps in order:

### Step 1 — Identify the professor
- From the filename: `Lecture_[NN]_Atzeni.txt` → Atzeni; `Lecture_[NN]_Vaciago.txt` → Vaciago
- If ambiguous, ask the user

### Step 2 — Determine the next lecture number
- Check the highest `[N]` in `Lectures_txt/` for that professor
- New file should be `Lecture_[NN+1]_[Professor].txt`
- Note: numbering is global (Atzeni and Vaciago lectures share the same sequence)

### Step 3 — Place files
- Transcript → `Lectures_txt/Lecture_[NN]_[Professor]_[DD-MM]_.txt`
- Slide PDF → `Slides/[Professor]/[filename].pdf`

### Step 4 — Create the `Lectures_MD/` entry
Read the `.txt` file and use any matching slide PDF(s) only as structural/reference aids, then write `Lectures_MD/Lecture_[NN]_[Professor].md` using the per-lecture format (see Note-Taking Style Guide below). Substantive claims must come from the transcription.

### Step 5 — Update or create `Chapters_MD/` entries
- Identify which chapter(s) the new lecture contributes to (by matching its slide PDF to existing or new chapter files)
- If the chapter file **already exists**: add the new content as additional sections or expand existing ones
- If the chapter file **does not exist**: create it following the chapter format (see Note-Taking Style Guide)
- Chapter files mirror slide PDF filenames: `Slides/Atzeni/03_investigation_phases.pdf` → `Chapters_MD/Atzeni/03_investigation_phases.md`

### Step 6 — Update `AI_Context.md`
After completing the notes:
- Add the new transcript to the **Professors & Their Materials** table
- Add the new slide PDF(s) to the slides table
- Update the slide → lecture mapping
- Update the **Current State** tables to reflect the new files
- Update the **Last Updated** section

---

## Note-Taking Style Guide

All Markdown files in this project follow a consistent format. New notes must match this style exactly.

### Per-Lecture Files (`Lectures_MD/`)

```markdown
# Lecture [N] – [Full Descriptive Title]
**Professor:** [Atzeni | Vaciago]  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/[Professor]/filename.pdf`

---

## Overview
[2–4 sentence contextual introduction to the lecture's content]

---

## [N]. [Section Title]
[Content from transcript, cleaned and organised. Use slide structure only as a skeleton/reference aid.]

> 📎 *Slide reference: `filename.pdf` — [section or topic name]*

### [Subsection Title]
[Additional depth where needed]

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Term** | Definition text |

---

## Summary
- Bullet-point takeaways
- One point per key idea
- 6–10 bullets
```

### Per-Chapter Files (`Chapters_MD/`)

```markdown
# Chapter [N] – [Full Topic Title]
**Professor:** [Atzeni | Vaciago]  
**Reference Slides:** [`Slides/[Professor]/filename.pdf`]  
**Covered in Lectures:** Lecture [N], Lecture [M]

---

## Introduction
[Contextual intro situating this chapter within the broader course]

---

## [Section from slide structure]
[Content aggregated from all relevant lecture transcriptions. Slides define structure only; transcripts provide the substantive content.]

> 📎 *Slide reference: `filename.pdf` — [section/topic name]*

### [Subsection if needed]
...

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Term** | Definition text |

---

## Summary
- Bullet-point takeaways
- ...
```

### General Formatting Rules

| Rule | Detail |
|------|--------|
| **Slide references** | Always use `> 📎 *Slide reference: \`filename.pdf\` — [topic]*` format immediately after the relevant section |
| **Tables** | Use for: milestones, comparisons, tool lists, definitions, vulnerability breakdowns |
| **Bold terms** | Bold all technical terms on first use within a section |
| **Code blocks** | Use fenced code blocks (` ``` `) for all commands; inline backticks for command names, tool names, file paths |
| **Quotes from lecture** | Use `>` blockquotes for direct quotes from professors |
| **Section numbering** | Number top-level sections (`## 1.`, `## 2.`, ...) in per-lecture files; optional in chapter files |
| **Horizontal rules** | Separate every top-level section with `---` |
| **Terminology** | Preserve all technical and legal terminology exactly as used in the source material |
| **No invention** | Never add substantive content that does not appear in the transcription. Slides may guide structure and reference labels only. |
| **Summary bullets** | 6–10 bullet points; each capturing one distinct key idea; no sub-bullets |
| **Lab Lectures** | If the transcript indicates a Laboratory/Lab session, compress the information heavily. Write much shorter `.md` files to reduce token usage. Strip out useless details. |
| **Side events** | Student presentations, homework feedback, admin logistics, and guest/non-slide discussions may remain in `Lectures_MD/`, but must be indexed in `Side_Events_Index.txt` and kept out of `Chapters_MD/` unless the user explicitly asks otherwise. |

---

## Last Updated

**Date:** 2026-05-07
**Changes (initial session):**
- Created all 6 `Lectures_MD/` files (Lectures 1–6, both professors)
- Created `Chapters_MD/Atzeni/01_IntroCF.md` (Chapter 1: Introduction to Computer Forensics)
- Created `Chapters_MD/Vaciago/0_Introduction.md` (Chapter 0: Technology, Law & Digital Forensics)
- Created `README.md` (GitHub repository description)
- Created `AI_Context.md` (this file)

**Changes (follow-up session):**
- Added `Lectures_txt/Lecture_07_Atzeni_10-03_.txt` (raw transcript, read-only)
- Added `Slides/Atzeni/04_Write-Blocker-Tools.pdf` and `Slides/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.pdf`
- Created `Lectures_MD/Lecture_07_Atzeni.md` (Write Blocker Tools & Scene Assessment)
- Created `Chapters_MD/Atzeni/04_Write-Blocker-Tools.md`
- Created `Chapters_MD/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.md`
- Updated `README.md` to reflect all new files
- Updated `AI_Context.md` (this file)

**Changes (Batch 1 processing):**
- Processed Lectures 09, 10, and 11.
- Created `Lectures_MD/Lecture_09_Vaciago.md`, `Lectures_MD/Lecture_10_Atzeni.md`, `Lectures_MD/Lecture_11_Atzeni.md`.
- Updated `Chapters_MD/Vaciago/2_Cybercrime_Convention.md` with Lecture 09's detailed Article 32b breakdown.
- Created `Chapters_MD/Atzeni/07_untrusted_domain.md` aggregating content from Lectures 10 & 11 and their respective slide decks.
- Updated `AI_Context.md` tables and history.

**Changes (Batch 2 processing):**
- Processed Lectures 12 and 13.
- Created `Lectures_MD/Lecture_12_Vaciago.md` and `Lectures_MD/Lecture_13_Atzeni.md`.
- Updated `Chapters_MD/Vaciago/3_Law_48_08.md` from placeholder to full chapter notes.
- Created `Chapters_MD/Atzeni/08_tools_and_labs.md` with forensic lab requirements and principles.
- Updated `AI_Context.md` to reflect new files and mapping.

**Changes (Batch 4 processing):**
- Processed Lectures 16 and 17.
- Created `Lectures_MD/Lecture_16_Vaciago.md` and `Lectures_MD/Lecture_17_Atzeni.md`.
- Created a dedicated side-event note for the Paolo Dal Checco / Garlasco guest discussion, now located at `Side_Events_MD/Lecture_16_Guest_Paolo_Dal_Checco_Garlasco.md`.
- Expanded `Chapters_MD/Atzeni/09_FS_forensics.md` with MBR/GPT and FAT structure details from Lecture 17.
- Updated `AI_Context.md` to reflect new files and mapping.

**Changes (Quality Audit & Standardization):**
- Performed a systematic quality audit of all 17 lectures against transcripts and slides.
- Fixed major content gap in `Lecture_14_Atzeni.md` (added UFED and mobile forensics section).
- Standardized all `Lectures_MD/` filenames to the two-digit `Lecture_NN_Professor.md` format.
- Trimmed summaries in `Lecture_03` and `Lecture_06` to meet the 6–10 bullet requirement.
- Synced `Chapters_MD/Atzeni/08_tools_and_labs.md` with missing UFED/Mobile details.
- Verified all cross-references in `Chapters_MD/` and updated `AI_Context.md` and `README.md` manifests.
- **Repository status: 100% Audited and Verified.**

**Changes (Batch 5 processing):**
- Processed Lectures 18 through 25 from the newly dated transcript set.
- Created and realigned per-lecture notes for `Lecture_18_Atzeni.md` through `Lecture_25_Atzeni.md`.
- Expanded `Chapters_MD/Atzeni/09_FS_forensics.md` with slack space, NTFS, carving, and forensic copy details.
- Created Atzeni chapters `10_HDD-vs-SSD-in-Digital-Forensics.md`, `11_Data-Sanitisation-Techniques.md`, and `12_Network.md`; later corrected TOR and Cloud chapter ownership back to Atzeni after the official slide packs were restored under `Slides/Atzeni/`.
- Created Vaciago chapters `5_Rules_Digital_Forensics.md` and `6_Hacking_Team_Case.md`.

### 2026-05-18 — Lecture 01-25 Refactor Scope Check and TOR/Cloud Ownership Fix
- Corrected Lecture 25 generated material to Atzeni ownership: `Lecture_25_Atzeni.md`, transcript `Lecture_25_Atzeni_06-05_.txt`, and chapters `13_Digital-Forensics-in-the-TOR-Network.md` / `14_Cloud.md` under `Chapters_MD/Atzeni/`.
- Set the active documentation scope to Lecture 01 through Lecture 25; Lectures 26, 27, and 28 are intentionally ignored until their transcriptions are ready.
- Realigned old post-Lecture-18 professor/number assignments to match the dated `Lectures_txt/` filenames as the source of truth.
- Updated `AI_Context.md`, `README.md`, per-lecture note filenames, and chapter cross-references for the corrected architecture.

### 2026-05-18 — Side-Event Isolation Audit
- Created `Side_Events_Index.txt` to track student presentations, homework feedback, lab/admin material, guest sessions, and non-slide professional/case discussions.
- Moved the Paolo Dal Checco / Garlasco guest discussion out of `Chapters_MD/Vaciago/` and into `Side_Events_MD/`.
- Confirmed that explicit student presentations from Lectures 23, 24, and 28 are present in lecture notes but not in chapter notes.
- Documented the rule that future side-event material should be indexed separately and kept out of slide-backed chapter notes.

### 2026-06-08 — Lectures 29-33 Processing and Chapter 16 Correction
- Processed new transcripts `Lecture_29_Vaciago_15-05.txt` through `Lecture_33_Atzeni_27-05.txt`.
- Created per-lecture notes `Lecture_29_Vaciago.md`, `Lecture_30_Atzeni.md`, `Lecture_31_Atzeni.md`, `Lecture_32_Vaciago.md`, and `Lecture_33_Atzeni.md`.
- Corrected the chapter split: memory acquisition content from the old `16_volatile.md` now belongs to `15_OS.md`; `16_volatile.md` now covers the real Volatility and volatile-memory-analysis material from Lecture 30.
- Created Atzeni chapters `17_anti_forensics.md`, `18_autopsy.md`, and `19_LLM.md`.
- Created Vaciago chapter `07_TechMed_Forensics_Law.md` for the official TechMed corporate-forensics laboratory.
- Updated `Side_Events_Index.txt` to isolate Lecture 29 homework/professional material, Lecture 31 student presentations, and Lecture 32 bonus-point administration from slide-backed chapters.
- Updated `README.md` and `AI_Context.md` indexes, slide mappings, and current-state tables through Lecture 33.
