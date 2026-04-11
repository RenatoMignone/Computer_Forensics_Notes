# Computer Forensics and Cybercrime Analysis – Lecture Notes

> **Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
> **Programme:** MSc in Cybersecurity – 2nd Year, 2nd Semester  
> **Credits:** 8 CFU  
> **Academic Year:** 2025/2026

---

## 🤝 How to Contribute – Create New Lecture Notes

This project welcomes contributions! Follow this step-by-step workflow to add new lectures:

### Step 1: Download Course Materials
1. Visit the **Politecnico di Torino – Portale della Didattica** website
2. Find the course *Computer Forensics and Cybercrime Analysis*
3. Download the latest PDF slide decks and save them to:
   - `Notes/Slides/Atzeni/` for Prof. Atzeni's materials
   - `Notes/Slides/Vaciago/` for Prof. Vaciago's materials

### Step 2: Configure Transcription Pipeline
1. In the Portale della Didattica, find the lecture video corresponding to the new material
2. Right-click the lecture video and select *Copy link address...*
3. Open `Script/Transcription/data.json` and add the URL to the `Lecture_URLs` list
4. Add the desired output filename (e.g., `Lecture_09_Atzeni.txt`) to the `File_Names` list, ensuring the lengths of both lists match

### Step 3: Run AI Transcription
1. Open a terminal in the `Script/Transcription/` directory
2. Run the python script:
   ```bash
   python 01_AI_Model_Script.py
   ```
3. The script will automatically:
   - Download the video in the background thread
   - Transcribe the audio using the `faster_whisper` GPU model
   - Save the token-optimized `.txt` transcript directly into `Notes/Lectures_txt/`
4. Review the generated `.txt` file for any obvious transcription errors (optional)

### Step 6: Generate Structured Notes (with AI Assistance)
1. Prepare your AI assistant context:
   - Use **Claude Haiku 4.5** via VS Code GitHub Copilot, or
   - Use **Claude Sonnet 4.6** via Anthropic's Claude API, or
   - Use **Antigravity** client if available
2. In your AI chat session:
   - Attach [Notes/AI_Context.md](Notes/AI_Context.md) to provide project context
   - Attach the new `Lectures_txt/Lecture_[NN]_[Professor].txt` file
   - Attach the corresponding slide PDFs from `Notes/Slides/[Professor]/`
   - Attach any related existing chapter notes from `Notes/Chapters_MD/[Professor]/` for consistency
   - Provide this prompt to the AI:
     > Based on the attached `AI_Context.md`, transcription file, and slides, generate:
     > 1. A per-lecture note file in `Notes/Lectures_MD/Lecture_[NN]_[Professor].md`
     > 2. Updates to existing chapter files in `Notes/Chapters_MD/[Professor]/` by integrating new lecture content
     > Follow the existing structure, tone, and formatting conventions. Update the `AI_Context.md` mapping if this lecture introduces new slide materials.

3. Save the generated files to their respective locations
4. Review and manually edit if needed for accuracy or clarity

### Step 7: Update Documentation
- Update [Notes/AI_Context.md](Notes/AI_Context.md) to reflect new lectures and slide materials
- Update the **Lecture Index** and **Chapter Index** sections below with new entries
- Commit all changes to version control

**Questions?** Refer to [Notes/AI_Context.md](Notes/AI_Context.md) for detailed project structure and conventions.

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
├── README.md                 # This file
├── Script/
│   ├── Transcription/
│   │   ├── 01_AI_Model_Script.py  # Python script to download and transcribe lecture videos via GPU
│   │   └── data.json              # Configuration file with video URLs and transcript filenames
│   └── Old/                       # Deprecated shell scripts for manual audio splitting
│
└── Notes/
    ├── AI_Context.md         # Persistent context file for AI assistants working on this project
    │
    ├── Lectures_MD/          # Per-lecture structured Markdown notes (one file per lecture)
    │   ├── Lecture_01_Atzeni.md
    │   ├── Lecture_02_Atzeni.md
    │   ├── Lecture_03_Vaciago.md
    │   ├── Lecture_04_Atzeni.md
    │   ├── Lecture_05_Atzeni.md
    │   ├── Lecture_06_Vaciago.md
    │   ├── Lecture_07_Atzeni.md
    │   └── Lecture_08_Atzeni.md
    │
    ├── Chapters_MD/          # Per-chapter notes grouped by topic and professor
    │   ├── Atzeni/
    │   │   ├── 01_IntroCF.md
    │   │   ├── 01b_MorrisWorm.md
    │   │   ├── 02_terms.md
    │   │   ├── 03_investigation_phases.md
    │   │   ├── 03b_Forensic-USB-Drive-Acquisition.md
    │   │   ├── Digital-Forensics-Case-Study.md
    │   │   ├── 04_Write-Blocker-Tools.md
    │   │   └── 05_Scene-Assessment-and-Data-Source-Identification.md
    │   └── Vaciago/
    │       ├── 0_Introduction.md
    │       ├── 1_Definition.md
    │       ├── 2_Cybercrime_Convention.md
    │       └── 3_Law_48_08.md
    │
    ├── Lectures_txt/         # Raw audio transcriptions (source material only)
    │   ├── Lecture_01_Atzeni.txt
    │   ├── Lecture_02_Atzeni.txt
    │   ├── Lecture_03_Vaciago.txt
    │   ├── Lecture_04_Atzeni.txt
    │   ├── Lecture_05_Atzeni.txt
    │   ├── Lecture_06_Vaciago.txt
    │   ├── Lecture_07_Atzeni.txt
    │   └── Lecture_08_Atzeni.txt
    │
    └── Slides/               # Official course slide PDFs (organized by professor)
        ├── Atzeni/
        │   ├── 01_introCF.pdf
        │   ├── 01b_Cybersecurity-History-MorrisWorm.pdf
        │   ├── 02_terms.pdf
        │   ├── 03_investigation_phases.pdf
        │   ├── 03b_Forensic-USB-Drive-Acquisition.pdf
        │   ├── Digital-Forensics-Case-Study.pdf
        │   ├── Digital-Forensics-Case-Study_partial.pdf
        │   ├── 04_Write-Blocker-Tools.pdf
        │   └── 05_Scene-Assessment-and-Data-Source-Identification.pdf
        └── Vaciago/
            ├── 0_Introduction.pdf
            ├── 1_Definition.pdf
            ├── 2_Cybercrime_Convention.pdf
            └── 3_Law_48_08.pdf
```

### Directory Roles

| Folder | Purpose | Editable? | Source |
|--------|---------|-----------|--------|
| `Script/` | automated Python script for GPU transcription | No | Provided |
| `Notes/Lectures_MD/` | Per-lecture chronological notes | **Yes** | Generated from transcriptions + slides |
| `Notes/Chapters_MD/` | Per-topic thematic chapter notes | **Yes** | Aggregated & synthesized from lectures |
| `Notes/Lectures_txt/` | Raw lecture transcriptions | **Yes** | Transcribed from video audio |
| `Notes/Slides/` | Official course slide PDFs | No | Downloaded from Portale della Didattica |
| `Notes/AI_Context.md` | Project metadata and conventions | **Yes** | Updated as lectures are added |

---

## Lecture Index

### Prof. Atzeni – Technical Track

| # | File | Topic | Key Slides |
|---|------|-------|------------|
| 1 | [Lecture_01_Atzeni.md](Notes/Lectures_MD/Lecture_01_Atzeni.md) | Introduction to Computer Forensics & the Morris Worm | `01_introCF.pdf`, `01b_Cybersecurity-History-MorrisWorm.pdf` |
| 2 | [Lecture_02_Atzeni.md](Notes/Lectures_MD/Lecture_02_Atzeni.md) | Digital Evidence, Chain of Custody & Data Acquisition | `02_terms.pdf` |
| 4 | [Lecture_04_Atzeni.md](Notes/Lectures_MD/Lecture_04_Atzeni.md) | Investigation Phases – Part I: Identification & Collection | `03_investigation_phases.pdf` |
| 5 | [Lecture_05_Atzeni.md](Notes/Lectures_MD/Lecture_05_Atzeni.md) | Investigation Phases – Part II: Acquisition & Examination | `03_investigation_phases.pdf`, `03b_Forensic-USB-Drive-Acquisition.pdf`, `Digital-Forensics-Case-Study.pdf` |
| 7 | [Lecture_07_Atzeni.md](Notes/Lectures_MD/Lecture_07_Atzeni.md) | Write Blocker Tools & Scene Assessment | `04_Write-Blocker-Tools.pdf`, `05_Scene-Assessment-and-Data-Source-Identification.pdf` |
| 8 | [Lecture_08_Atzeni.md](Notes/Lectures_MD/Lecture_08_Atzeni.md) | Digital Forensics Case Study: Debrief & Prefetch Analysis | `Digital-Forensics-Case-Study_partial.pdf` |

### Prof. Vaciago – Legal Track

| # | File | Topic | Key Slides |
|---|------|-------|------------|
| 3 | [Lecture_03_Vaciago.md](Notes/Lectures_MD/Lecture_03_Vaciago.md) | Legal Introduction: Technology, Law & Digital Forensics | `0_Introduction.pdf` |
| 6 | [Lecture_06_Vaciago.md](Notes/Lectures_MD/Lecture_06_Vaciago.md) | Legal Frameworks: Data Retention, Jurisdiction & Digital Evidence | `1_Definition.pdf`, `2_Cybercrime_Convention.pdf` |

---

## Chapter Index

Chapter notes aggregate content **across multiple lectures** per topic, using the slide deck as the structural backbone. They are the recommended starting point for exam revision.

### Prof. Atzeni – Technical Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Atzeni/01_IntroCF.md](Notes/Chapters_MD/Atzeni/01_IntroCF.md) | ✅ Complete | Introduction to Computer Forensics | Lecture 01 |
| [Chapters_MD/Atzeni/01b_MorrisWorm.md](Notes/Chapters_MD/Atzeni/01b_MorrisWorm.md) | ✅ Complete | The Morris Worm – Case Study | Lecture 01 |
| [Chapters_MD/Atzeni/02_terms.md](Notes/Chapters_MD/Atzeni/02_terms.md) | ✅ Complete | Digital Evidence, Chain of Custody & Data Acquisition | Lecture 02 |
| [Chapters_MD/Atzeni/03_investigation_phases.md](Notes/Chapters_MD/Atzeni/03_investigation_phases.md) | ✅ Complete | Forensic Investigation Phases (all five) | Lectures 4 & 5 |
| [Chapters_MD/Atzeni/03b_Forensic-USB-Drive-Acquisition.md](Notes/Chapters_MD/Atzeni/03b_Forensic-USB-Drive-Acquisition.md) | ✅ Complete | USB Drive Acquisition – Tools & Procedure | Lecture 05 |
| [Chapters_MD/Atzeni/Digital-Forensics-Case-Study.md](Notes/Chapters_MD/Atzeni/Digital-Forensics-Case-Study.md) | ✅ Complete | Insider IP Exfiltration – End-to-End Case Study | Lecture 05 |
| [Chapters_MD/Atzeni/04_Write-Blocker-Tools.md](Notes/Chapters_MD/Atzeni/04_Write-Blocker-Tools.md) | ✅ Complete | Write Blocker Tools – Hardware, Software & Documentation | Lecture 07 |
| [Chapters_MD/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.md](Notes/Chapters_MD/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.md) | ✅ Complete | Scene Assessment & Data Source Identification | Lecture 07 |

### Prof. Vaciago – Legal Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Vaciago/0_Introduction.md](Notes/Chapters_MD/Vaciago/0_Introduction.md) | ✅ Complete | Technology, Law & Digital Forensics | Lecture 03 |
| [Chapters_MD/Vaciago/1_Definition.md](Notes/Chapters_MD/Vaciago/1_Definition.md) | ✅ Complete | Definitions, Standards & Evidence Location Model | Lecture 06 |
| [Chapters_MD/Vaciago/2_Cybercrime_Convention.md](Notes/Chapters_MD/Vaciago/2_Cybercrime_Convention.md) | ✅ Complete | Data Retention, Jurisdiction & Budapest Convention | Lecture 06 |
| [Chapters_MD/Vaciago/3_Law_48_08.md](Notes/Chapters_MD/Vaciago/3_Law_48_08.md) | ⏳ Placeholder | Italian Law 48/2008 | Not yet covered |

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

- **`Notes/Lectures_MD/`** — Per-lecture notes synthesised from transcriptions and slides. Structured with section headings, tables, key concept definitions, and bullet-point summaries. One file per lecture session.
- **`Notes/Chapters_MD/`** — Thematic chapter notes that aggregate content from all relevant lectures per topic. Organised by professor. These are the primary revision resource.
- **`Notes/Lectures_txt/`** — Unedited audio-to-text transcriptions. Provided as source material only; may contain transcription artefacts.
- **`Notes/Slides/`** — Official slide PDFs distributed by the professors. Used as the structural skeleton for all notes.
- **`Notes/AI_Context.md`** — Persistent context file describing the full project structure, naming conventions, and current state. Hand this file to an AI assistant when adding new lectures to continue work without prior conversation history.

---

## Disclaimer

These notes are personal study material created for academic purposes. They are based on lecture content from the CFCCA course. They are not official course documents and should not be cited as primary sources.
