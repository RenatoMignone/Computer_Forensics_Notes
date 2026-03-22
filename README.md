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

### Step 2: Obtain Lecture Video
1. In the Portale della Didattica, find the lecture video corresponding to the new material
2. **Before downloading**: check [Notes/Lectures_MD/](Notes/Lectures_MD/) to identify which lectures have already been processed
3. Right-click the lecture video and select *Save link as...*
4. Save the `.mp4` file to the `Script/` folder in this repository

### Step 3: Extract and Split Audio
1. Open a terminal in the `Script/` directory
2. **Make the script executable** (if not already):
   ```bash
   chmod +x script.sh
   ```
3. Run the bash script:
   ```bash
   ./script.sh your_lecture.mp4
   ```
4. The script will:
   - Create a folder named after the lecture
   - Extract the audio and split it into **30-minute segments** as `.m4a` files
   - Save all segments in the created folder

### Step 4: Transcribe Audio
1. Go to **[https://turboscribe.ai/dashboard](https://turboscribe.ai/dashboard)**
   - Free plan: 3 transcriptions per day
   - **Unlimited workaround**: Use Incognito Mode or Tor Browser to bypass daily limits (TurboscribeAI does not track across sessions)
2. Upload each `.m4a` segment and transcribe to text
3. Download all transcribed `.txt` files

### Step 5: Consolidate Transcriptions
1. Create a new file in `Notes/Lectures_txt/` named `Lecture_[N]_[Professor].txt` (e.g., `Lecture_9_Atzeni.txt`)
2. **Remove TurboscribeAI watermarking**:
   - Delete the parenthetical disclaimer at the **start** of the first segment
   - Delete the parenthetical disclaimer at the **end** of the last segment
3. Concatenate all transcribed segments into the single `.txt` file
4. Review for obvious transcription errors (optional)

### Step 6: Generate Structured Notes (with AI Assistance)
1. Prepare your AI assistant context:
   - Use **Claude Haiku 4.5** via VS Code GitHub Copilot, or
   - Use **Claude Sonnet 4.6** via Anthropic's Claude API, or
   - Use **Antigravity** client if available
2. In your AI chat session:
   - Attach [Notes/AI_Context.md](Notes/AI_Context.md) to provide project context
   - Attach the new `Lectures_txt/Lecture_[N]_[Professor].txt` file
   - Attach the corresponding slide PDFs from `Notes/Slides/[Professor]/`
   - Attach any related existing chapter notes from `Notes/Chapters_MD/[Professor]/` for consistency
   - Provide this prompt to the AI:
     > Based on the attached `AI_Context.md`, transcription file, and slides, generate:
     > 1. A per-lecture note file in `Notes/Lectures_MD/Lecture_[N]_[Professor].md`
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
│   └── script.sh             # Bash script to split lecture videos into 30-min audio segments
│
└── Notes/
    ├── AI_Context.md         # Persistent context file for AI assistants working on this project
    │
    ├── Lectures_MD/          # Per-lecture structured Markdown notes (one file per lecture)
    │   ├── Lecture_1_Atzeni.md
    │   ├── Lecture_2_Atzeni.md
    │   ├── Lecture_3_Vaciago.md
    │   ├── Lecture_4_Atzeni.md
    │   ├── Lecture_5_Atzeni.md
    │   ├── Lecture_6_Vaciago.md
    │   ├── Lecture_7_Atzeni.md
    │   └── Lecture_8_Atzeni.md
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
    │   ├── Lecture_1_Atzeni.txt
    │   ├── Lecture_2_Atzeni.txt
    │   ├── Lecture_3_Vaciago.txt
    │   ├── Lecture_4_Atzeni.txt
    │   ├── Lecture_5_Atzeni.txt
    │   ├── Lecture_6_Vaciago.txt
    │   ├── Lecture_7_Atzeni.txt
    │   └── Lecture_8_Atzeni.txt
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
| `Script/` | Utility script for video processing | No | Provided |
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
| 1 | [Lecture_1_Atzeni.md](Notes/Lectures_MD/Lecture_1_Atzeni.md) | Introduction to Computer Forensics & the Morris Worm | `01_introCF.pdf`, `01b_Cybersecurity-History-MorrisWorm.pdf` |
| 2 | [Lecture_2_Atzeni.md](Notes/Lectures_MD/Lecture_2_Atzeni.md) | Digital Evidence, Chain of Custody & Data Acquisition | `02_terms.pdf` |
| 4 | [Lecture_4_Atzeni.md](Notes/Lectures_MD/Lecture_4_Atzeni.md) | Investigation Phases – Part I: Identification & Collection | `03_investigation_phases.pdf` |
| 5 | [Lecture_5_Atzeni.md](Notes/Lectures_MD/Lecture_5_Atzeni.md) | Investigation Phases – Part II: Acquisition & Examination | `03_investigation_phases.pdf`, `03b_Forensic-USB-Drive-Acquisition.pdf`, `Digital-Forensics-Case-Study.pdf` |
| 7 | [Lecture_7_Atzeni.md](Notes/Lectures_MD/Lecture_7_Atzeni.md) | Write Blocker Tools & Scene Assessment | `04_Write-Blocker-Tools.pdf`, `05_Scene-Assessment-and-Data-Source-Identification.pdf` |
| 8 | [Lecture_8_Atzeni.md](Notes/Lectures_MD/Lecture_8_Atzeni.md) | Digital Forensics Case Study: Debrief & Prefetch Analysis | `Digital-Forensics-Case-Study_partial.pdf` |

### Prof. Vaciago – Legal Track

| # | File | Topic | Key Slides |
|---|------|-------|------------|
| 3 | [Lecture_3_Vaciago.md](Notes/Lectures_MD/Lecture_3_Vaciago.md) | Legal Introduction: Technology, Law & Digital Forensics | `0_Introduction.pdf` |
| 6 | [Lecture_6_Vaciago.md](Notes/Lectures_MD/Lecture_6_Vaciago.md) | Legal Frameworks: Data Retention, Jurisdiction & Digital Evidence | `1_Definition.pdf`, `2_Cybercrime_Convention.pdf` |

---

## Chapter Index

Chapter notes aggregate content **across multiple lectures** per topic, using the slide deck as the structural backbone. They are the recommended starting point for exam revision.

### Prof. Atzeni – Technical Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Atzeni/01_IntroCF.md](Notes/Chapters_MD/Atzeni/01_IntroCF.md) | ✅ Complete | Introduction to Computer Forensics | Lecture 1 |
| [Chapters_MD/Atzeni/01b_MorrisWorm.md](Notes/Chapters_MD/Atzeni/01b_MorrisWorm.md) | ✅ Complete | The Morris Worm – Case Study | Lecture 1 |
| [Chapters_MD/Atzeni/02_terms.md](Notes/Chapters_MD/Atzeni/02_terms.md) | ✅ Complete | Digital Evidence, Chain of Custody & Data Acquisition | Lecture 2 |
| [Chapters_MD/Atzeni/03_investigation_phases.md](Notes/Chapters_MD/Atzeni/03_investigation_phases.md) | ✅ Complete | Forensic Investigation Phases (all five) | Lectures 4 & 5 |
| [Chapters_MD/Atzeni/03b_Forensic-USB-Drive-Acquisition.md](Notes/Chapters_MD/Atzeni/03b_Forensic-USB-Drive-Acquisition.md) | ✅ Complete | USB Drive Acquisition – Tools & Procedure | Lecture 5 |
| [Chapters_MD/Atzeni/Digital-Forensics-Case-Study.md](Notes/Chapters_MD/Atzeni/Digital-Forensics-Case-Study.md) | ✅ Complete | Insider IP Exfiltration – End-to-End Case Study | Lecture 5 |
| [Chapters_MD/Atzeni/04_Write-Blocker-Tools.md](Notes/Chapters_MD/Atzeni/04_Write-Blocker-Tools.md) | ✅ Complete | Write Blocker Tools – Hardware, Software & Documentation | Lecture 7 |
| [Chapters_MD/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.md](Notes/Chapters_MD/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.md) | ✅ Complete | Scene Assessment & Data Source Identification | Lecture 7 |

### Prof. Vaciago – Legal Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Vaciago/0_Introduction.md](Notes/Chapters_MD/Vaciago/0_Introduction.md) | ✅ Complete | Technology, Law & Digital Forensics | Lecture 3 |
| [Chapters_MD/Vaciago/1_Definition.md](Notes/Chapters_MD/Vaciago/1_Definition.md) | ✅ Complete | Definitions, Standards & Evidence Location Model | Lecture 6 |
| [Chapters_MD/Vaciago/2_Cybercrime_Convention.md](Notes/Chapters_MD/Vaciago/2_Cybercrime_Convention.md) | ✅ Complete | Data Retention, Jurisdiction & Budapest Convention | Lecture 6 |
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
