# Lecture 1 – Introduction to Computer Forensics & the Morris Worm
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/01_introCF.pdf`, `Slides/Atzeni/01b_Cybersecurity-History-MorrisWorm.pdf`

---

## Overview
This lecture introduces the course structure, grading scheme, and expected prerequisites. The main content covers the historical roots of forensic science and its evolution into digital forensics, culminating in a detailed case study of the Morris Worm (1988) as a foundational milestone in the field.

---

## 1. Course Structure & Organisation

The course is worth **8 credits** and is divided into two coordinated but separate parts:

- **Computer Science perspective** – Prof. Atzeni (Tuesday, Wednesday, and ~4 lab sessions)
- **Law perspective** – Prof. Vaciago (Friday sessions)

The two parts are thematically linked and reflect the entanglement of technical knowledge, legal compliance, and cybersecurity that practitioners must navigate in the real world.

### Lab Sessions
- Groups of **4–6 students** complete practical tasks and submit them for evaluation.
- Labs are **optional** but contribute fractional bonus points (approx. 2–3 decimal points per lab, up to ~1 point total).

### Exam
- **30 points total**, 90-minute written exam.
- Composed of **10–12 closed questions** (multiple choice) + **1 open question per professor**.
- The open question requires extensive, detailed answers covering tools, theory, and applied knowledge.

### Optional Homework
- Maximum **1 homework per student**, individually assigned.
- Output: a **10–20 page report** + **10–15 minute presentation** during lecture hours.
- Earns **0–2 bonus points** added to the written exam result.
- Topics must be agreed upon with Prof. Atzeni.
- Presentation must occur *after* the course covers the relevant topic.

> 📎 *Slide reference: `Slides/Atzeni/01_introCF.pdf`, slide: Course Introduction*

---

## 2. Course Topics Overview

The technical part of the course will cover:

- **Fundamentals**: phases, procedures, and implications of digital forensics
- **Cybercrime overview**: essentials of cybercrime organisation and structure
- **Case studies**: specific examples of cybercrime and forensic investigations
- **Best practices and standards**: distillation of key principles from major forensic standards (ACPO, NIST, ISO, etc.)
- **Domain-specific forensics**: file systems, memory, email, mobile, cloud
- **Future outlook**: impact of generative AI on computer forensics

### Expected Prerequisites
Students are expected to have solid understanding of:
- Network security protocols and cyber security building blocks (firewalls, VPNs, digital certificates)
- Hash functions, digital signatures, and encryption
- Common attack types and techniques
- Operating system internals, computer networks, and system architecture

> 📎 *Slide reference: `Slides/Atzeni/01_introCF.pdf`, slide: Course Content*

---

## 3. What is Forensics Analysis?

**Forensics Analysis** is the application of scientific methodology to legal problems, criminal investigations, or internal organisational investigations.

> *"The application of scientific knowledge in terms mostly of methodology on legal problems."*

While the term "computer forensics" focuses specifically on digital artefacts, the broader field of forensics analysis can be applied in non-criminal contexts, e.g., by a system administrator diagnosing system misbehaviour.

### Computer Forensics – Core Activities
Computer forensics involves several key phases applied to **digital evidence**:

1. **Acquisition** – Obtaining digital artefacts without introducing modifications.
2. **Examination** – Carefully inspecting all details of the evidence.
3. **Presentation** – Communicating findings clearly to non-technical audiences (judges, attorneys, juries).

> 📎 *Slide reference: `Slides/Atzeni/01_introCF.pdf`, slide: Forensics Analysis Definition*

---

## 4. Historical Evolution of Forensic Science

### Ancient Origins
The concept of forensic investigation is approximately **4,000 years old**:
- **Babylon** (~2000 BCE): fingerprints used to identify individuals in business transactions.
- **Xi Yuan Ji Lu** (China, Song Dynasty): a physician provided a structured methodology to distinguish between drowning and strangulation, used to resolve a murder case. The title translates poetically as *"Washing Away of Wrongs."*

### 19th Century Milestones
| Year | Event |
|------|-------|
| 1835 | Henry Goddard (British police) – first documented comparison of bullets to solve a murder |
| Late 1800s | Henry Faulds – proposed using fingerprints for identification |
| Late 1800s | Sir Francis Galton – collected thousands of fingerprints; classified patterns as spirals, loops, and arches |
| Early 1900s | Crime labs began to emerge, combining legal, technical, and field expertise |

### 20th Century Developments
- **DNA profiling** introduced – far more precise than fingerprints (essentially unique per individual)
- Growth of **specialised forensic units** within police, military, and large organisations
- Integration of **artificial intelligence** for rapid sample analysis (with mandatory human counter-check)

> 📎 *Slide reference: `Slides/Atzeni/01_introCF.pdf`, slides: History of Forensics*

---

## 5. Digital Forensics – Key Milestones

| Milestone | Significance |
|-----------|-------------|
| **Morris Worm (1988/1989)** | First major computer forensic case; involved analysis of logs, network traffic, and email |
| **IACIS founding** | International Association of Computer Investigative Specialists – early body establishing guidelines |
| **IOCE** | International Organisation on Computer Evidence – developed foundational standards |
| **EnCase tool** | First widely-usable forensic tool providing acquisition, storage, and analysis in one platform |
| **Early 2000s** | Digital forensics became standard in legal proceedings; country-specific laws were enacted |
| **Mobile & cloud era** | Dramatically changed acquisition methods and evidence scope |
| **Present** | Blockchain, LLMs, quantum cryptography, and highly organised cybercrime add new complexity |

### Challenges Introduced by Mobile & Cloud
- **Mobile devices**: always carried, collect enormous personal data; but many OS protect data even with user cooperation; highly fragmented device ecosystem
- **Cloud computing**: data is off-device and cannot be accessed without cloud provider cooperation or user consent; provider data are not physically seized-able

> 📎 *Slide reference: `Slides/Atzeni/01_introCF.pdf`, slides: Digital Forensics Milestones*

---

## 6. The Morris Worm – Case Study

> 📎 *Slide reference: `Slides/Atzeni/01b_Cybersecurity-History-MorrisWorm.pdf`*

### Context
The Morris Worm (November 1988) is considered the **first major cybersecurity attack** and the **first significant computer forensic case**. It was created by **Robert Tappan Morris**, a graduate student at Cornell University and son of NSA cryptographer Robert Morris Sr.

Morris's stated intent was to *test* whether a self-propagating network worm was feasible — not to cause damage. The worm was released onto the ARPANET (the precursor to the internet), which at the time primarily connected US universities.

### Technical Details
- Target system: **Unix BSD 4** (written in C)
- Architecture: a small "grappling hook" downloader deployed the main worm binary
- Total binary size: a few kilobytes (fits on a single floppy disk; original preserved at the Computer History Museum)

### Vulnerabilities Exploited
| Vulnerability | Description |
|---------------|-------------|
| **sendmail debug mode** | Daemon left with remote debug mode enabled, allowing remote instruction injection |
| **finger daemon buffer overflow** | Overflow allowed arbitrary code execution on the target host |
| **rexec / rsh trust** | Remote execution commands authenticated only by IP address |
| **Weak passwords** | Many accounts used trivial passwords (e.g., username = password, reversed username) |

### The Propagation Bug
Morris included a self-limiting mechanism: the worm checked if it was already running on a target and, if so, would not propagate again. However, anticipating that system admins could fake a "already infected" response, Morris hard-coded a **1-in-7 chance (≈14%) of replication even on an already-infected host**.

This small probability, combined with exponential propagation across a densely connected network, caused:
- Machines to become infected multiple times
- Resource exhaustion (a **fork bomb** effect)
- Mass system crashes

> *"They were like dead in the water."* — Clifford Stoll

### Damage Assessment
- **~6,000 machines infected** (approximately 2,000 in the first 15 hours)
- **Internet backbone disconnected for days** to prevent recontamination
- **Estimated damage: ~$10 million USD**
- Later infected machines rendered completely unusable

> *"He should have tried it on a simulator first."* — Michael Rabin (whose randomisation concept inspired the 14% replication probability)

### Legal Outcome
Robert Tappan Morris was convicted under the **Computer Fraud and Abuse Act (CFAA)** — one of its earliest federal applications in US history:
- 3 years' probation
- 400 hours community service
- $10,050 fine

### Lasting Impact
1. **First CERT** (Computer Emergency Response Team) established at Carnegie Mellon University, funded by DARPA
2. **Computer Fraud and Abuse Act** applied in a digital context for one of the first times
3. **Popular culture**: referenced in several books; inspired the TV series *Mr. Robot*
4. **Monoculture risk**: because all infected systems shared the same architecture and vulnerabilities, a single exploit could cascade globally — a lesson still relevant today

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Forensics Analysis** | Application of scientific methodology to legal or investigative problems |
| **Computer Forensics** | Discipline focused on identifying, acquiring, examining, and presenting digital evidence |
| **Digital Evidence** | Any digital data that can be used to reach conclusions in an investigation or legal proceeding |
| **Monoculture Risk** | The danger that systems sharing the same architecture can all be compromised by a single weakness |
| **ARPANET** | The predecessor to the internet, primarily connecting US universities and some foreign institutions |
| **CERT** | Computer Emergency Response Team – a coordinated body for responding to cybersecurity incidents |
| **CFAA** | Computer Fraud and Abuse Act – US federal law specifically addressing computer-related crimes |
| **Buffer Overflow** | A vulnerability in which input data exceeds allocated memory and overwrites adjacent memory, potentially executing attacker-controlled code |
| **rexec / rsh** | Remote execution commands that authenticate solely via IP address – considered insecure today |

---

## Summary

- The CFCCA course integrates **legal and technical perspectives** on digital forensics, reflecting the real-world entanglement of cybersecurity, compliance, and law.
- Forensic science has roots dating back **4,000 years**, with structured approaches emerging in the 19th century (fingerprinting, crime labs).
- Computer forensics emerged as a distinct discipline through key events like the **Morris Worm (1988)**, the growth of networked computing, and the digitisation of everyday life.
- The Morris Worm illustrates foundational concepts: **vulnerability exploitation**, **unintended consequences of probabilistic self-replication**, **coordinated incident response**, and the **monoculture risk**.
- Modern challenges include **mobile forensics**, **cloud storage**, **encryption**, **AI-generated evidence**, and the rise of **highly organised cybercrime** with state-level resources.
