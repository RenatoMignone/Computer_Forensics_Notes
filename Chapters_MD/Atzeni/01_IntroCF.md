# Chapter 1 – Introduction to Computer Forensics
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/01_introCF.pdf`]  
**Covered in Lectures:** Lecture 1

---

## Introduction
Computer forensics is the discipline of applying scientific methodology to the collection, examination, and presentation of digital evidence for legal or investigative purposes. Its roots lie in classical forensic science dating back thousands of years; its modern form emerged from the necessity of investigating incidents on early networked computers. This chapter covers the definition of the field, its historical lineage, key institutional milestones, and contemporary challenges.

> 📝 *The Morris Worm foundational case study is covered in [`01b_MorrisWorm.md`](01b_MorrisWorm.md).*

---

## 1. What is Forensics Analysis?

**Forensics Analysis** is the application of scientific knowledge — primarily in terms of methodology — to legal problems, criminal investigations, or internal organisational investigations.

While *computer forensics* focuses specifically on digital artefacts and systems, the underlying methodology is the same as any other forensic discipline: **gather evidence rigorously, analyse it systematically, and present conclusions clearly**.

The scope is broader than criminal law:
- A system administrator diagnosing unexplained server behaviour is applying forensic methodology.
- A corporate investigator tracing an insider threat is performing forensic analysis without initiating criminal proceedings.

### Core Activities of Computer Forensics

| Activity | Description |
|----------|-------------|
| **Acquisition** | Obtaining digital artefacts without introducing modifications; preserving the original state |
| **Examination** | Carefully inspecting all details of the acquired evidence |
| **Presentation** | Communicating findings clearly to non-technical audiences — judges, attorneys, executives |

Presentation is often underestimated. A forensically sound investigation is worthless if a jury or judge cannot understand the conclusions.

> 📎 *Slide reference: `01_introCF.pdf` — Forensics Analysis Definition*

---

## 2. Historical Evolution of Forensic Science

### Ancient Origins
Forensic investigation is approximately **4,000 years old**:
- **Babylon (~2000 BCE)**: fingerprints used to identify individuals in business transactions.
- **Xi Yuan Ji Lu** (China, Song Dynasty): a physician provided a structured methodology to distinguish between drowning and strangulation, used to resolve a murder investigation. The title translates as *"Washing Away of Wrongs"*.

These examples show that the idea of applying systematic, reproducible methods to legal disputes is ancient — digital forensics is the latest expression of an enduring need.

### 19th Century Milestones

| Year | Event |
|------|-------|
| 1835 | Henry Goddard (British police) — first documented comparison of bullets to solve a murder |
| Late 1800s | Henry Faulds — proposed using fingerprints for identification |
| Late 1800s | Sir Francis Galton — collected and classified thousands of fingerprints (spirals, loops, arches) |
| Early 1900s | Dedicated crime laboratories began to emerge, combining legal, technical, and field expertise |

### 20th Century Developments
- **Fingerprints are not unique**: false positives and false negatives are possible; fingerprints can be affected by injuries. This limitation opened the search for more precise identification methods.
- **DNA profiling** introduced — far more precise than fingerprints; essentially unique per individual.
- Growth of **specialised forensic units** within police agencies, military organisations, and large corporations.
- Integration of **artificial intelligence** for rapid sample analysis — always with mandatory human counter-check.

> 📎 *Slide reference: `01_introCF.pdf` — History of Forensics*

---

## 3. Digital Forensics – Key Milestones

| Milestone | Significance |
|-----------|--------------|
| **Morris Worm (1988)** | First major computer forensic case; analysis of logs, network traffic, and email |
| **IACIS founding** | International Association of Computer Investigative Specialists — early body establishing investigative guidelines |
| **IOCE** | International Organisation on Computer Evidence — developed foundational standards for digital evidence handling |
| **EnCase tool** | First widely-usable forensic platform providing acquisition, storage, and analysis in one tool; very expensive, but still available in newer versions |
| **Early 2000s** | Digital forensics became standard in legal proceedings; country-specific legislation enacted |
| **Mobile & cloud era** | Dramatically changed acquisition methods and expanded the scope of evidence |
| **Present** | Blockchain, LLMs, quantum cryptography, and highly organised cybercrime add new layers of complexity |

### Challenges Introduced by Mobile & Cloud Computing

**Mobile devices:**
- Always carried by suspects — contain enormous volumes of personal, location, and communication data
- Modern operating systems protect data even with user cooperation (full-disk encryption by default)
- Highly fragmented device ecosystem (hundreds of models, firmware variants)

**Cloud computing:**
- Data is **off-device** — cannot be physically seized from the subject's premises
- Access requires cooperation from cloud providers, often governed by foreign law
- Data may be distributed across multiple jurisdictions
- Provider records (audit logs, timestamps) are the primary evidence source

> 📎 *Slide reference: `01_introCF.pdf` — Digital Forensics Milestones*

> 📝 *The Morris Worm foundational case study is covered in [`01b_MorrisWorm.md`](01b_MorrisWorm.md).*

---

## 4. Modern Challenges and Future Outlook

The field of computer forensics continues to evolve alongside emergent technologies:

| Challenge | Description |
|-----------|-------------|
| **Cloud forensics** | Evidence distributed across multi-tenant infrastructure in multiple jurisdictions; provider cooperation required |
| **Mobile forensics** | Fragmented ecosystem; operating systems protect data even with user cooperation |
| **Generative AI** | New AI technologies are having a large impact on computer forensics |
| **Organised cybercrime** | Highly structured groups and criminal organisations with billions in income; units working for states, terrorist organisations, and gangs with tens or hundreds of members |
| **Blockchain** | Emerging complication for forensic analysis |
| **Quantum cryptography** | May break existing cryptographic assumptions in the next 10–15 years |

> 📎 *Slide reference: `01_introCF.pdf` — Digital Forensics: Modern Challenges [inferred]*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Forensics Analysis** | Application of scientific methodology to legal or investigative problems |
| **Computer Forensics** | Discipline focused on identifying, acquiring, examining, and presenting digital evidence |
| **Digital Evidence** | Any digital data that can be used to reach conclusions in an investigation or legal proceeding |
| **Acquisition** | The forensically sound process of obtaining digital artefacts without modifying the original |
| **Monoculture Risk** | The danger that systems sharing the same architecture can all be compromised by a single exploit |
| **IACIS** | International Association of Computer Investigative Specialists — early forensics standards body |
| **IOCE** | International Organisation on Computer Evidence — developed foundational digital evidence standards |
| **EnCase** | First widely-used commercial forensic platform for acquisition, storage, and analysis |

---

## Summary

- **Computer forensics** applies scientific methodology — acquisition, examination, presentation — to digital artefacts for legal or investigative purposes.
- The discipline descends from a tradition of forensic science dating back 4,000 years, with structured modern practices emerging in the 19th century through fingerprinting and crime laboratories.
- **DNA profiling**, crime labs, and AI-assisted analysis represent the evolutionary arc from physical to biological to digital evidence.
- Key institutional milestones — IACIS, IOCE, EnCase, the mobile and cloud eras — each reshaped how digital evidence is gathered and processed.
- **Mobile and cloud** computing present the most significant current forensic challenges: data is encrypted, off-device, multi-jurisdictional, and legally complex to obtain.
- Emerging challenges — AI-generated evidence, blockchain forensics, quantum threats — will define the next generation of the discipline.
- The foundational case study (Morris Worm, 1988) is covered in [`01b_MorrisWorm.md`](01b_MorrisWorm.md).
