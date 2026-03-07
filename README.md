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
├── Lectures_MD/          # Structured markdown lecture notes (primary study material)
│   ├── Lecture_1_Atzeni.md
│   ├── Lecture_2_Atzeni.md
│   ├── Lecture_3_Vaciago.md
│   ├── Lecture_4_Atzeni.md
│   ├── Lecture_5_Atzeni.md
│   └── Lecture_6_Vaciago.md
│
├── Lectures_txt/         # Raw transcriptions of lectures (source material)
│   ├── Lecture_1_Atzeni.txt
│   ├── Lecture_2_Atzeni.txt
│   ├── Lecture_3_Vaciago.txt
│   ├── Lecture_4_Atzeni.txt
│   ├── Lecture_5_Atzeni.txt
│   └── Lecture_6_Vaciago.txt
│
├── Slides/               # Official course slide decks
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

- **Markdown notes** in `Lectures_MD/` are synthesised from lecture transcriptions and official slides. They are structured with section headings, tables, key concept definitions, and bullet-point summaries.
- **Raw transcriptions** in `Lectures_txt/` are unedited audio-to-text outputs. They are provided as a reference but may contain transcription artefacts.
- **Slides** are the official material distributed by the professors.

---

## Disclaimer

These notes are personal study material created for academic purposes. They are based on lecture content from the CFCCA course. They are not official course documents and should not be cited as primary sources.
