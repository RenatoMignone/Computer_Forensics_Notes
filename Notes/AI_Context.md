# AI_Context.md

> **Purpose of this file**: Persistent context for AI assistants. When new lectures or slides are added to this project, hand this file to a new AI session along with the new materials. The AI should be able to read this file and immediately continue working with no prior conversation history.

---

## Project Purpose

This is a university lecture notes project for the course **Computer Forensics and Cybercrime Analysis (CFCCA)**, part of an **MSc in Cybersecurity** (2nd Year, 2nd Semester, 8 CFU).

The course is taught by two professors covering complementary perspectives:
- **Prof. Atzeni** — Computer Science / Technical track (forensic methodology, investigation phases, tools, acquisition)
- **Prof. Vaciago** — Law / Legal track (cybercrime law, conventions, jurisdiction, data retention, digital evidence admissibility)

The project generates two types of structured Markdown notes from raw lecture transcriptions and slide PDFs:
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
| `Slides/Atzeni/` | Atzeni's slide PDFs — used as structural skeleton for notes | READ ONLY |
| `Slides/Vaciago/` | Vaciago's slide PDFs — used as structural skeleton for notes | READ ONLY |

---

## Professors & Their Materials

### Prof. Atzeni — Technical Track

**Lectures:**
| File | Topic |
|------|-------|
| `Lectures_txt/Lecture_01_Atzeni.txt` | Introduction to Computer Forensics & the Morris Worm |
| `Lectures_txt/Lecture_02_Atzeni.txt` | Digital Evidence, Chain of Custody & Data Acquisition |
| `Lectures_txt/Lecture_04_Atzeni.txt` | Investigation Phases – Part I: Identification & Collection |
| `Lectures_txt/Lecture_05_Atzeni.txt` | Investigation Phases – Part II: Acquisition & Examination |
| `Lectures_txt/Lecture_07_Atzeni.txt` | Write Blocker Tools & Scene Assessment |
| `Lectures_txt/Lecture_08_Atzeni.txt` | Digital Forensics Case Study: Debrief & Prefetch Analysis |

**Slide PDFs** (`Slides/Atzeni/`):
| File | Topic |
|------|-------|
| `01_introCF.pdf` | Introduction to Computer Forensics |
| `01b_Cybersecurity-History-MorrisWorm.pdf` | Morris Worm case study |
| `02_terms.pdf` | Digital evidence terminology and chain of custody |
| `03_investigation_phases.pdf` | Five investigation phases (Identification → Presentation) |
| `03b_Forensic-USB-Drive-Acquisition.pdf` | Practical USB acquisition walkthrough |
| `Digital-Forensics-Case-Study.pdf` | Insider IP exfiltration case study |
| `Digital-Forensics-Case-Study_partial.pdf` | Extended case study: named scenario, prefetch analysis, detailed timeline (Lecture 08) |
| `04_Write-Blocker-Tools.pdf` | Write blocker tools: hardware, software, documentation requirements |
| `05_Scene-Assessment-and-Data-Source-Identification.pdf` | Scene assessment, OSINT, data source identification, volatility prioritisation |

---

### Prof. Vaciago — Legal Track

**Lectures:**
| File | Topic |
|------|-------|
| `Lectures_txt/Lecture_03_Vaciago.txt` | Legal Introduction: Technology, Law & Digital Forensics |
| `Lectures_txt/Lecture_06_Vaciago.txt` | Legal Frameworks: Data Retention, Jurisdiction & Digital Evidence |

**Slide PDFs** (`Slides/Vaciago/`):
| File | Topic |
|------|-------|
| `0_Introduction.pdf` | Technology evolution, jurisdiction, legal design, dark patterns, GDPR Art. 22 |
| `1_Definition.pdf` | Digital forensics definitions, forensic standards, evidence location model |
| `2_Cybercrime_Convention.pdf` | Budapest Convention, data retention directive, jurisdiction problem |
| `3_Law_48_08.pdf` | Italian Law 48/2008 implementing the Budapest Convention |

---

## Naming Conventions

### Lecture files (`Lectures_txt/` and `Lectures_MD/`)
Pattern: `Lecture_[NN]_[Professor].txt` / `.md`
- `[N]` = sequential lecture number (globally across both professors)
- `[Professor]` = `Atzeni` or `Vaciago`
- Example: `Lecture_04_Atzeni.txt` = 4th lecture of the course, delivered by Atzeni

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
| `Digital-Forensics-Case-Study.pdf` | Atzeni | Lecture 05 |
| `Digital-Forensics-Case-Study_partial.pdf` | Atzeni | Lecture 08 |
| `04_Write-Blocker-Tools.pdf` | Atzeni | Lecture 07 |
| `05_Scene-Assessment-and-Data-Source-Identification.pdf` | Atzeni | Lecture 07 |
| `0_Introduction.pdf` | Vaciago | Lecture 03 |
| `1_Definition.pdf` | Vaciago | Lecture 06 |
| `2_Cybercrime_Convention.pdf` | Vaciago | Lecture 06 |
| `3_Law_48_08.pdf` | Vaciago | Not yet covered |

---

## Current State

### `Lectures_MD/` — Per-Lecture Notes

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

### `Chapters_MD/Atzeni/` — Atzeni Chapter Notes

| File | Status | Corresponding Slide | Source Lectures |
|------|--------|---------------------|-----------------|
| `01_IntroCF.md` | ✅ Complete | `01_introCF.pdf` | Lecture 01 |
| `01b_MorrisWorm.md` | ✅ Complete | `01b_Cybersecurity-History-MorrisWorm.pdf` | Lecture 01 |
| `02_terms.md` | ✅ Complete | `02_terms.pdf` | Lecture 02 |
| `03_investigation_phases.md` | ✅ Complete | `03_investigation_phases.pdf` | Lectures 4 & 5 |
| `03b_Forensic-USB-Drive-Acquisition.md` | ✅ Complete | `03b_Forensic-USB-Drive-Acquisition.pdf` | Lecture 05 |
| `Digital-Forensics-Case-Study.md` | ✅ Complete | `Digital-Forensics-Case-Study.pdf`, `Digital-Forensics-Case-Study_partial.pdf` | Lectures 5 & 8 |
| `04_Write-Blocker-Tools.md` | ✅ Complete | `04_Write-Blocker-Tools.pdf` | Lecture 07 |
| `05_Scene-Assessment-and-Data-Source-Identification.md` | ✅ Complete | `05_Scene-Assessment-and-Data-Source-Identification.pdf` | Lecture 07 |

### `Chapters_MD/Vaciago/` — Vaciago Chapter Notes

| File | Status | Corresponding Slide | Source Lectures |
|------|--------|---------------------|-----------------|
| `0_Introduction.md` | ✅ Complete | `0_Introduction.pdf` | Lecture 03 |
| `1_Definition.md` | ✅ Complete | `1_Definition.pdf` | Lecture 06 |
| `2_Cybercrime_Convention.md` | ✅ Complete | `2_Cybercrime_Convention.pdf` | Lecture 06 |
| `3_Law_48_08.md` | ⏳ Placeholder | `3_Law_48_08.pdf` | Not yet covered |

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
- Transcript → `Lectures_txt/Lecture_[NN]_[Professor].txt`
- Slide PDF → `Slides/[Professor]/[filename].pdf`

### Step 4 — Create the `Lectures_MD/` entry
Read the `.txt` file and any matching slide PDF(s), then write `Lectures_MD/Lecture_[NN]_[Professor].md` using the per-lecture format (see Note-Taking Style Guide below).

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
[Content from transcript, cleaned and organised. Use slide structure as skeleton.]

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
[Content aggregated from all relevant lectures. Slides define structure; transcripts provide depth.]

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
| **No invention** | Never add content that does not appear in the transcription or slide material |
| **Summary bullets** | 6–10 bullet points; each capturing one distinct key idea; no sub-bullets |
| **Lab Lectures** | If the transcript indicates a Laboratory/Lab session, compress the information heavily. Write much shorter `.md` files to reduce token usage. Strip out useless details. |

---

## Last Updated

**Date:** 2026-03-12  
**Changes (initial session):**
- Created all 6 `Lectures_MD/` files (Lectures 1–6, both professors)
- Created `Chapters_MD/Atzeni/01_IntroCF.md` (Chapter 1: Introduction to Computer Forensics)
- Created `Chapters_MD/Vaciago/0_Introduction.md` (Chapter 0: Technology, Law & Digital Forensics)
- Created `README.md` (GitHub repository description)
- Created `AI_Context.md` (this file)

**Changes (follow-up session):**
- Added `Lectures_txt/Lecture_07_Atzeni.txt` (raw transcript, read-only)
- Added `Slides/Atzeni/04_Write-Blocker-Tools.pdf` and `Slides/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.pdf`
- Created `Lectures_MD/Lecture_07_Atzeni.md` (Write Blocker Tools & Scene Assessment)
- Created `Chapters_MD/Atzeni/04_Write-Blocker-Tools.md`
- Created `Chapters_MD/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.md`
- Updated `README.md` to reflect all new files
- Updated `AI_Context.md` (this file)

**Changes (Lecture 08 session):**
- Added `Lectures_txt/Lecture_08_Atzeni.txt` (raw transcript, read-only)
- Added `Slides/Atzeni/Digital-Forensics-Case-Study_partial.pdf`
- Created `Lectures_MD/Lecture_08_Atzeni.md` (Digital Forensics Case Study: Debrief & Prefetch Analysis)
- Updated `Chapters_MD/Atzeni/Digital-Forensics-Case-Study.md` to add Lecture 08 content (named scenario, prefetch files, detailed timeline, investigative conclusions, extended Key Concepts and Summary)
- Updated `AI_Context.md` (this file)

**Still pending:**
- `Chapters_MD/Atzeni/02_terms.md`
- `Chapters_MD/Vaciago/1_Definition.md`
- `Chapters_MD/Vaciago/2_Cybercrime_Convention.md`
- `Chapters_MD/Vaciago/3_Law_48_08.md` (slides present; lecture not yet held)
