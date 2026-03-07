# Computer Forensics and Cybercrime Analysis – Lecture Notes

> **Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
> **Programme:** MSc in Cybersecurity – 2nd Year, 2nd Semester  
> **Credits:** 8 CFU  
> **Academic Year:** 2025/2026

---

## Professors

| Professor | Background | Topics Covered |
|-----------|------------|----------------|
| **Prof. Atzeni** | Computer Science / Technical | Digital forensics methodology, investigation phases, acquisition tools, anti-forensics |
| **Prof. Vaciago** | Law / Legal | Cybercrime law, jurisdiction, data retention, digital evidence admissibility |

---

## Repository Structure

```
.
├── Lectures_MD/              # Per-lecture structured notes (chronological)
│   ├── Lecture_1_Atzeni.md
│   ├── Lecture_2_Atzeni.md
│   ├── Lecture_3_Vaciago.md
│   ├── Lecture_4_Atzeni.md
│   ├── Lecture_5_Atzeni.md
│   └── Lecture_6_Vaciago.md
│
├── Chapters_MD/              # Per-chapter notes grouped by topic and professor
│   ├── Atzeni/
│   │   └── 01_IntroCF.md
│   └── Vaciago/
│       └── 0_Introduction.md
│
├── Lectures_txt/             # Raw transcriptions of lectures (source material, read-only)
│   ├── Lecture_1_Atzeni.txt
│   ├── Lecture_2_Atzeni.txt
│   ├── Lecture_3_Vaciago.txt
│   ├── Lecture_4_Atzeni.txt
│   ├── Lecture_5_Atzeni.txt
│   └── Lecture_6_Vaciago.txt
│
├── Slides/                   # Official course slide decks
│   ├── Atzeni/
│   │   ├── 01_introCF.pdf
│   │   ├── 01b_Cybersecurity-History-MorrisWorm.pdf
│   │   ├── 02_terms.pdf
│   │   ├── 03_investigation_phases.pdf
│   │   ├── 03b_Forensic-USB-Drive-Acquisition.pdf
│   │   └── Digital-Forensics-Case-Study.pdf
│   └── Vaciago/
│       ├── 0_Introduction.pdf
│       ├── 1_Definition.pdf
│       ├── 2_Cybercrime_Convention.pdf
│       └── 3_Law_48_08.pdf
│
├── AI_Context.md             # Persistent context file for AI assistants
└── README.md
```

---

## Lecture Index

### Prof. Atzeni – Technical Track

| # | File | Topic | Key Slides |
|---|------|-------|------------|
| 1 | [Lecture_1_Atzeni.md](Lectures_MD/Lecture_1_Atzeni.md) | Introduction to Computer Forensics & the Morris Worm | `01_introCF.pdf`, `01b_Cybersecurity-History-MorrisWorm.pdf` |
| 2 | [Lecture_2_Atzeni.md](Lectures_MD/Lecture_2_Atzeni.md) | Digital Evidence, Chain of Custody & Data Acquisition | `02_terms.pdf` |
| 4 | [Lecture_4_Atzeni.md](Lectures_MD/Lecture_4_Atzeni.md) | Investigation Phases – Part I: Identification & Collection | `03_investigation_phases.pdf` |
| 5 | [Lecture_5_Atzeni.md](Lectures_MD/Lecture_5_Atzeni.md) | Investigation Phases – Part II: Acquisition & Examination | `03_investigation_phases.pdf`, `03b_Forensic-USB-Drive-Acquisition.pdf`, `Digital-Forensics-Case-Study.pdf` |

### Prof. Vaciago – Legal Track

| # | File | Topic | Key Slides |
|---|------|-------|------------|
| 3 | [Lecture_3_Vaciago.md](Lectures_MD/Lecture_3_Vaciago.md) | Legal Introduction: Technology, Law & Digital Forensics | `0_Introduction.pdf` |
| 6 | [Lecture_6_Vaciago.md](Lectures_MD/Lecture_6_Vaciago.md) | Legal Frameworks: Data Retention, Jurisdiction & Digital Evidence | `1_Definition.pdf`, `2_Cybercrime_Convention.pdf` |

---

## Chapter Index

Chapter notes aggregate content **across multiple lectures** per topic, using the slide deck as the structural backbone. They are the recommended starting point for exam revision.

### Prof. Atzeni – Technical Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Atzeni/01_IntroCF.md](Chapters_MD/Atzeni/01_IntroCF.md) | ✅ Complete | Introduction to Computer Forensics | Lecture 1 |
| `Chapters_MD/Atzeni/02_terms.md` | ⏳ Pending | Digital Evidence & Chain of Custody | Lecture 2 |
| `Chapters_MD/Atzeni/03_investigation_phases.md` | ⏳ Pending | Investigation Phases (all five) | Lectures 4 & 5 |

### Prof. Vaciago – Legal Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Vaciago/0_Introduction.md](Chapters_MD/Vaciago/0_Introduction.md) | ✅ Complete | Technology, Law & Digital Forensics | Lecture 3 |
| `Chapters_MD/Vaciago/1_Definition.md` | ⏳ Pending | Forensic Definitions & Standards | Lecture 6 |
| `Chapters_MD/Vaciago/2_Cybercrime_Convention.md` | ⏳ Pending | Data Retention, Jurisdiction & Budapest Convention | Lecture 6 |
| `Chapters_MD/Vaciago/3_Law_48_08.md` | ⏳ Pending | Italian Law 48/2008 | Not yet covered |

---

## Topics at a Glance

<details>
<summary><strong>Technical Track (Atzeni)</strong></summary>

- History and evolution of digital forensics
- The Morris Worm (1988) – first major internet incident and legal precedent
- Digital evidence: properties, chain of custody, admissibility
- NSRL (National Software Reference Library) and hash databases
- Five investigation phases: Identification → Collection → Acquisition → Examination → Presentation
- OSINT tools: Spiderfoot, Maltego, Shodan
- Evidence volatility and acquisition prioritisation
- Static vs live acquisition; cryogenic RAM extraction
- Write blockers and trusted tool hierarchy
- Forensic imaging: `dd`, `dc3dd`/`dcfldd`, FTK Imager
- Hashing protocols: SHA-256 vs MD5
- Anti-forensics: encryption, timestomping, Tor, fileless malware
- Timeline construction and cross-source correlation
- Report writing for technical, legal, and executive audiences

</details>

<details>
<summary><strong>Legal Track (Vaciago)</strong></summary>

- Interaction between technology and law (3 paradigms)
- Legal design and dark patterns (GDPR Article 22, Lex Machina, COMPAS)
- Three forensics domains: criminal, civil, corporate
- Forensic standards: ISO 27037, NIST SP 800-86, ACPO
- Jurisdiction challenges in cross-border digital investigations
- Data retention: EU Directive 2006/24/EC, national variations, Italy's 5-year retention
- Freezing procedures and ISP cooperation
- Tor and the erosion of IP address as evidence
- GDPR vs the US CLOUD Act
- Freedom of speech: First Amendment (US) vs Article 595 Italian Penal Code
- Platform cooperation and transparency reports (Google, Meta, Telegram, X)
- China/Yahoo case and tech company responsibility
- Mobile forensics: Cellebrite UFED
- US vs EU/Italian prosecutorial models

</details>

---

## Notes on the Material

- **`Lectures_MD/`** — Per-lecture notes synthesised from transcriptions and slides. Structured with section headings, tables, key concept definitions, and bullet-point summaries. One file per lecture session.
- **`Chapters_MD/`** — Thematic chapter notes that aggregate content from all relevant lectures per topic. Organised by professor. These are the primary revision resource.
- **`Lectures_txt/`** — Unedited audio-to-text transcriptions. Provided as source material only; may contain transcription artefacts.
- **`Slides/`** — Official slide PDFs distributed by the professors. Used as the structural skeleton for all notes.
- **`AI_Context.md`** — Persistent context file describing the full project structure, naming conventions, and current state. Hand this file to an AI assistant when adding new lectures to continue work without prior conversation history.

---

## Disclaimer

These notes are personal study material created for academic purposes. They are based on lecture content from the CFCCA course. They are not official course documents and should not be cited as primary sources.
