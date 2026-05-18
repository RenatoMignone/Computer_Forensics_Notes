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
4. Add the desired output filename (e.g., `Lecture_09_Vaciago_13-03_.txt`) to the `File_Names` list, ensuring the lengths of both lists match

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
   - Attach the new `Lectures_txt/Lecture_[NN]_[Professor]_[DD-MM]_.txt` file
   - Attach the corresponding slide PDFs from `Notes/Slides/[Professor]/`
   - Attach any related existing chapter notes from `Notes/Chapters_MD/[Professor]/` for consistency
   - Provide this prompt to the AI:
     > Based on the attached `AI_Context.md`, transcription file, and slides as structural references, generate:
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
    │   ├── ...
    │   └── Lecture_28_Atzeni.md
    │
    ├── Chapters_MD/          # Per-chapter notes grouped by topic and professor
    │   ├── Atzeni/
    │   └── Vaciago/
    │
    ├── Side_Events_MD/       # Dedicated notes for guest/non-slide side events
    │   └── Lecture_16_Guest_Paolo_Dal_Checco_Garlasco.md
    │
    ├── Side_Events_Index.txt # Index of presentations, labs, guest sessions, and admin material
    │
    ├── Lectures_txt/         # Raw audio transcriptions (source material only)
    │   ├── Lecture_01_Atzeni_24-02_.txt
    │   ├── ...
    │   └── Lecture_28_Atzeni_13-05_.txt
    │
    └── Slides/               # Official course slide PDFs (organized by professor)
        ├── Atzeni/
        └── Vaciago/
```

### Directory Roles

| Folder | Purpose | Editable? | Source |
|--------|---------|-----------|--------|
| `Script/` | automated Python script for GPU transcription | No | Provided |
| `Notes/Lectures_MD/` | Per-lecture chronological notes | **Yes** | Generated from transcriptions; slides are structural references only |
| `Notes/Chapters_MD/` | Per-topic thematic chapter notes | **Yes** | Aggregated & synthesized from lecture transcriptions |
| `Notes/Side_Events_MD/` | Full notes for guest sessions and non-slide side events | **Yes** | Isolated from slide-backed chapter notes |
| `Notes/Side_Events_Index.txt` | Quick map of presentations, labs, homework feedback, and admin material | **Yes** | Maintained during audits |
| `Notes/Lectures_txt/` | Raw lecture transcriptions | **Yes** | Transcribed from video audio |
| `Notes/Slides/` | Official course slide PDFs | No | Downloaded from Portale della Didattica |
| `Notes/AI_Context.md` | Project metadata and conventions | **Yes** | Updated as lectures are added |

---

## Lecture Index

### Prof. Atzeni – Technical Track

| # | File | Topic | Key Slides |
|---|------|-------|------------|
| 1 | [Lecture_01_Atzeni.md](Notes/Lectures_MD/Lecture_01_Atzeni.md) | Intro to CompForensics & Morris Worm | `01_introCF.pdf`, `01b_Cybersecurity-History-MorrisWorm.pdf` |
| 2 | [Lecture_02_Atzeni.md](Notes/Lectures_MD/Lecture_02_Atzeni.md) | Evidence, Chain of Custody & Acquisition | `02_terms.pdf` |
| 4 | [Lecture_04_Atzeni.md](Notes/Lectures_MD/Lecture_04_Atzeni.md) | Investigation Phases I: Identification | `03_investigation_phases.pdf` |
| 5 | [Lecture_05_Atzeni.md](Notes/Lectures_MD/Lecture_05_Atzeni.md) | Investigation Phases II: Acquisition | `03_investigation_phases.pdf`, `03b_Forensic-USB-Drive-Acquisition.pdf` |
| 7 | [Lecture_07_Atzeni.md](Notes/Lectures_MD/Lecture_07_Atzeni.md) | Write Blockers & Scene Assessment | `04_Write-Blocker-Tools.pdf` |
| 8 | [Lecture_08_Atzeni.md](Notes/Lectures_MD/Lecture_08_Atzeni.md) | Case Study: Prefetch & Timeline Analysis | `06_Digital-Forensics-Case-Study.pdf` |
| 10 | [Lecture_10_Atzeni.md](Notes/Lectures_MD/Lecture_10_Atzeni.md) | Untrusted Domains & Malware Vectors | `07_untrusted_domain.pdf` |
| 11 | [Lecture_11_Atzeni.md](Notes/Lectures_MD/Lecture_11_Atzeni.md) | Memory Exploitation & Supply Chain Attacks | `07_untrusted_domain.pdf` |
| 13 | [Lecture_13_Atzeni.md](Notes/Lectures_MD/Lecture_13_Atzeni.md) | Forensic Lab Setup & Principles | `08_tools_and_labs.pdf` |
| 14 | [Lecture_14_Atzeni.md](Notes/Lectures_MD/Lecture_14_Atzeni.md) | Advanced Lab Resilience & UFED | `08_tools_and_labs.pdf` |
| 15 | [Lecture_15_Atzeni.md](Notes/Lectures_MD/Lecture_15_Atzeni.md) | File System Forensics: Device Types | `09_FS_forensics.pdf` |
| 17 | [Lecture_17_Atzeni.md](Notes/Lectures_MD/Lecture_17_Atzeni.md) | File System Forensics: Metadata & FAT | `09_FS_forensics.pdf` |
| 18 | [Lecture_18_Atzeni.md](Notes/Lectures_MD/Lecture_18_Atzeni.md) | File System Forensics: Slack Space & FAT Recovery | `09_FS_forensics.pdf` |
| 20 | [Lecture_20_Atzeni.md](Notes/Lectures_MD/Lecture_20_Atzeni.md) | NTFS, Forensic Copying, Slack Space & SSD Intro | `09_FS_forensics.pdf`, `10_HDD-vs-SSD...pdf` |
| 21 | [Lecture_21_Atzeni.md](Notes/Lectures_MD/Lecture_21_Atzeni.md) | SSD Acquisition, Sanitisation & Network Intro | `10_HDD-vs-SSD...pdf`, `11_Data-Sanitisation...pdf`, `12_Network.pdf` |
| 23 | [Lecture_23_Atzeni.md](Notes/Lectures_MD/Lecture_23_Atzeni.md) | Network Forensics, OSINT & Social Media | `12_Network.pdf` |
| 24 | [Lecture_24_Atzeni.md](Notes/Lectures_MD/Lecture_24_Atzeni.md) | Network Anti-Forensics & Attack Obfuscation | `12_Network.pdf` |
| 25 | [Lecture_25_Atzeni.md](Notes/Lectures_MD/Lecture_25_Atzeni.md) | TOR & Cloud Forensics | `13_Digital-Forensics-in-the-TOR-Network.pdf`, `14_Cloud.pdf` |
| 27 | [Lecture_27_Atzeni.md](Notes/Lectures_MD/Lecture_27_Atzeni.md) | Cloud Forensics: Effects & Acquisition Strategy | `14_Cloud.pdf` |
| 28 | [Lecture_28_Atzeni.md](Notes/Lectures_MD/Lecture_28_Atzeni.md) | Video Carving, OS Forensics & Memory Acquisition | `15_OS.pdf`, `16_volatile.pdf` |

### Prof. Vaciago – Legal Track

| # | File | Topic | Key Slides |
|---|------|-------|------------|
| 3 | [Lecture_03_Vaciago.md](Notes/Lectures_MD/Lecture_03_Vaciago.md) | Legal Intro: Technology & Digital Forensics | `0_Introduction.pdf` |
| 6 | [Lecture_06_Vaciago.md](Notes/Lectures_MD/Lecture_06_Vaciago.md) | Frameworks: Retention & Jurisdiction | `1_Definition.pdf`, `2_Cybercrime_Convention.pdf` |
| 9 | [Lecture_09_Vaciago.md](Notes/Lectures_MD/Lecture_09_Vaciago.md) | International Cooperation & Budapest Conv. | `2_Cybercrime_Convention.pdf` |
| 12 | [Lecture_12_Vaciago.md](Notes/Lectures_MD/Lecture_12_Vaciago.md) | Italian Law 48/2008 & Corporate Liability | `3_Law_48_08.pdf` |
| 16 | [Lecture_16_Vaciago.md](Notes/Lectures_MD/Lecture_16_Vaciago.md) | Guest Expert Insights & Garlasco Case Study | N/A (side event) |
| 19 | [Lecture_19_Vaciago.md](Notes/Lectures_MD/Lecture_19_Vaciago.md) | The 10 Rules for a Digital Forensic Report | `5_Rules_Digital_Forensics.pdf` |
| 22 | [Lecture_22_Vaciago.md](Notes/Lectures_MD/Lecture_22_Vaciago.md) | Digital Alibi Feedback & Hacking Team Case | `5_Rules_Digital_Forensics.pdf`, `6_Hacking_Team_Case.pdf` |
| 26 | [Lecture_26_Vaciago.md](Notes/Lectures_MD/Lecture_26_Vaciago.md) | Malware Production, Mens Rea & Criminal Liability | `Articoli_Codice_Penale.pdf` |

---

## Chapter Index

Chapter notes aggregate content **across multiple lectures** per topic, using the slide deck as the structural backbone. They are the recommended starting point for exam revision.

### Prof. Atzeni – Technical Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Atzeni/01_IntroCF.md](Notes/Chapters_MD/Atzeni/01_IntroCF.md) | ✅ Complete | Introduction to Computer Forensics | Lecture 01 |
| [Chapters_MD/Atzeni/01b_MorrisWorm.md](Notes/Chapters_MD/Atzeni/01b_MorrisWorm.md) | ✅ Complete | The Morris Worm – Case Study | Lecture 01 |
| [Chapters_MD/Atzeni/02_terms.md](Notes/Chapters_MD/Atzeni/02_terms.md) | ✅ Complete | Evidence & Chain of Custody | Lecture 02 |
| [Chapters_MD/Atzeni/03_investigation_phases.md](Notes/Chapters_MD/Atzeni/03_investigation_phases.md) | ✅ Complete | Forensic Investigation Phases | Lectures 4 & 5 |
| [Chapters_MD/Atzeni/06_Digital-Forensics-Case-Study.md](Notes/Chapters_MD/Atzeni/06_Digital-Forensics-Case-Study.md) | ✅ Complete | Insider IP Exfiltration Case Study | Lectures 5 & 8 |
| [Chapters_MD/Atzeni/04_Write-Blocker-Tools.md](Notes/Chapters_MD/Atzeni/04_Write-Blocker-Tools.md) | ✅ Complete | Write Blocker Tools | Lecture 07 |
| [Chapters_MD/Atzeni/05_Scene-Assessment...md](Notes/Chapters_MD/Atzeni/05_Scene-Assessment-and-Data-Source-Identification.md) | ✅ Complete | Scene Assessment & OSINT | Lecture 07 |
| [Chapters_MD/Atzeni/07_untrusted_domain.md](Notes/Chapters_MD/Atzeni/07_untrusted_domain.md) | ✅ Complete | Untrusted Domains & Malware | Lectures 10 & 11 |
| [Chapters_MD/Atzeni/08_tools_and_labs.md](Notes/Chapters_MD/Atzeni/08_tools_and_labs.md) | ✅ Complete | Forensic Lab Setup & UFED | Lectures 13 & 14 |
| [Chapters_MD/Atzeni/09_FS_forensics.md](Notes/Chapters_MD/Atzeni/09_FS_forensics.md) | ✅ Complete | File System Forensics | Lectures 15, 17, 18 & 20 |
| [Chapters_MD/Atzeni/10_HDD-vs-SSD-in-Digital-Forensics.md](Notes/Chapters_MD/Atzeni/10_HDD-vs-SSD-in-Digital-Forensics.md) | ✅ Complete | HDD vs SSD Forensics | Lectures 20 & 21 |
| [Chapters_MD/Atzeni/11_Data-Sanitisation-Techniques.md](Notes/Chapters_MD/Atzeni/11_Data-Sanitisation-Techniques.md) | ✅ Complete | Data Sanitisation Techniques | Lecture 21 |
| [Chapters_MD/Atzeni/12_Network.md](Notes/Chapters_MD/Atzeni/12_Network.md) | ✅ Complete | Network Forensics | Lectures 21, 23 & 24 |
| [Chapters_MD/Atzeni/13_Digital-Forensics-in-the-TOR-Network.md](Notes/Chapters_MD/Atzeni/13_Digital-Forensics-in-the-TOR-Network.md) | ✅ Complete | TOR Network Forensics | Lecture 25 |
| [Chapters_MD/Atzeni/14_Cloud.md](Notes/Chapters_MD/Atzeni/14_Cloud.md) | ✅ Complete | Cloud Forensics | Lectures 25 & 27 |
| [Chapters_MD/Atzeni/15_OS.md](Notes/Chapters_MD/Atzeni/15_OS.md) | ✅ Complete | Operating System Forensics | Lecture 28 |
| [Chapters_MD/Atzeni/16_volatile.md](Notes/Chapters_MD/Atzeni/16_volatile.md) | ✅ Complete | Volatile Memory Forensics | Lecture 28 |

### Prof. Vaciago – Legal Track

| File | Status | Topic | Source Lectures |
|------|--------|-------|------------------|
| [Chapters_MD/Vaciago/0_Introduction.md](Notes/Chapters_MD/Vaciago/0_Introduction.md) | ✅ Complete | Technology, Law & Forensics | Lecture 03 |
| [Chapters_MD/Vaciago/1_Definition.md](Notes/Chapters_MD/Vaciago/1_Definition.md) | ✅ Complete | Definitions & Standards | Lecture 06 |
| [Chapters_MD/Vaciago/2_Cybercrime_Convention.md](Notes/Chapters_MD/Vaciago/2_Cybercrime_Convention.md) | ✅ Complete | Budapest Conv. & Jurisdiction | Lectures 06 & 09 |
| [Chapters_MD/Vaciago/3_Law_48_08.md](Notes/Chapters_MD/Vaciago/3_Law_48_08.md) | ✅ Complete | Italian Law 48/2008 | Lecture 12 |
| [Chapters_MD/Vaciago/5_Rules_Digital_Forensics.md](Notes/Chapters_MD/Vaciago/5_Rules_Digital_Forensics.md) | ✅ Complete | Forensic Report Writing Rules | Lectures 19 & 22 |
| [Chapters_MD/Vaciago/6_Hacking_Team_Case.md](Notes/Chapters_MD/Vaciago/6_Hacking_Team_Case.md) | ✅ Complete | Hacking Team Case | Lecture 22 |
| [Chapters_MD/Vaciago/Articoli_Codice_Penale.md](Notes/Chapters_MD/Vaciago/Articoli_Codice_Penale.md) | ✅ Complete | Articles 615-ter/615-quater & Malware Liability | Lecture 26 |

### Side Events and Presentations

These are indexed separately from chapter notes so that student presentations, homework feedback, lab logistics, guest sessions, and non-slide discussions remain traceable without polluting the slide-backed chapter structure.

| File | Purpose |
|------|---------|
| [Side_Events_Index.txt](Notes/Side_Events_Index.txt) | Master list of side events and where they appear in lecture notes |
| [Side_Events_MD/Lecture_16_Guest_Paolo_Dal_Checco_Garlasco.md](Notes/Side_Events_MD/Lecture_16_Guest_Paolo_Dal_Checco_Garlasco.md) | Dedicated note for the Paolo Dal Checco / Garlasco guest session |

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
- Cloud forensics: provider dependency, snapshots, redundancy, volatile resources
- Operating system and volatile memory forensics
- Video carving and structure-aware recovery
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
- Malware-production liability under Articles 615-ter and 615-quater
- Mens rea and participation in a crime
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

- **`Notes/Lectures_MD/`** — Per-lecture notes synthesised from transcriptions, with slides used only as structural references. Structured with section headings, tables, key concept definitions, and bullet-point summaries. One file per lecture session.
- **`Notes/Chapters_MD/`** — Thematic chapter notes that aggregate content from all relevant lectures per topic. Organised by professor. These are the primary revision resource.
- **`Notes/Lectures_txt/`** — Unedited audio-to-text transcriptions. Provided as source material only; may contain transcription artefacts.
- **`Notes/Slides/`** — Official slide PDFs distributed by the professors. Used as the structural skeleton for all notes.
- **`Notes/AI_Context.md`** — Persistent context file describing the full project structure, naming conventions, and current state. Hand this file to an AI assistant when adding new lectures to continue work without prior conversation history.

---

## Disclaimer

These notes are personal study material created for academic purposes. They are based on lecture content from the CFCCA course. They are not official course documents and should not be cited as primary sources.
