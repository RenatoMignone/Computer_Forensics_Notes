# Lecture 3 – Legal Introduction: Technology, Law & Digital Forensics
**Professor:** Vaciago  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Vaciago/0_Introduction.pdf`

---

## Overview
This is the first lecture delivered by Prof. Vaciago, introducing the legal perspective of the course. The lecture covers the evolution of technology and its relationship with law and society, introduces the concept of legal design, discusses dark patterns, examines GDPR Article 22 on automated decision-making, and presents practical examples of AI-driven automated decisions in legal contexts. It also outlines the course structure and upcoming laboratory simulation.

---

## 1. Course Structure – Legal Component

Prof. Vaciago's part of the course consists of:
- **~15 hours of theoretical lessons** (covering legal concepts, standards, and case law)
- **~25 hours of laboratory simulation** (procedural trial simulation)

### Laboratory Format
The laboratory will simulate a **trial proceeding**:
- Students divided into **prosecutors and defence lawyers**
- Prof. Vaciago will act as judge (or an AI judge may be used as an experiment)
- Focus on **legal, not technical** analysis of a forensic case
- Goal: develop oral argumentation skills and understand how evidence is presented and challenged in court

### Exam
- All exam-related questions should be directed to **Prof. Atzeni**, not Prof. Vaciago
- The legal portion of the course is equally important for the exam

### Upcoming Topics (Vaciago's Part)
1. **Cybercrime Convention (Budapest Convention)**
2. **UN Convention** (brief overview)
3. **Italian law** (focus, given the predominantly Italian student population)
4. **Garlasco case** – famous Italian digital forensics case (focus on initial phase and digital issues)
5. **IoT and Digital Forensics** principles
6. **Territorial principle** and the Hackington case
7. **Digital Forensics and Artificial Intelligence**
8. **Case study / laboratory simulation**

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Course Overview*

---

## 2. The Evolution of Technology and Law

### Three Paradigms of Technology

| Era | Paradigm | Description |
|-----|----------|-------------|
| Pre-2000 | **Technology between us** | Communication tools (telephone, email) that people use to exchange information *with each other* |
| 2008+ | **Technology about us** | Social media (Facebook/Meta) — technology that collects and creates data *about* us; generates psychological and social consequences |
| Present/Future | **Technology in us** | AI — technology that is embedded in our decision-making; not just robotisation but AI influence on cognition and behaviour |

### Why This Matters for Digital Forensics
- Technology *about us* (social media) generates vast amounts of **evidence** — digital traces of behaviour, location, relationships, and content
- Technology *in us* (AI) raises questions about **automated decision-making** and its legal admissibility
- The speed of technological evolution has outpaced legal frameworks, creating gaps that forensic practitioners must navigate

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slides: Technology Evolution*

---

## 3. The Jurisdiction Problem

A recurring theme throughout the course is the **jurisdiction problem**: when you go online, you cross digital borders.

> *"When you go to Instagram, from a virtual standpoint, you are going to the United States. You are not in Italy."*

### Key insight:
- Physical presence = Italian law applies
- But digital interactions = you are connecting to US-based platforms governed largely by US law
- The **user's perception** (that Italian rules apply because they are literally in Italy) conflicts with the **legal reality** (the service is governed by the law of the platform's jurisdiction)

This creates fundamental problems for:
- Criminal investigation (jurisdiction over evidence)
- Data access (ISP compelled disclosure across borders)
- Content moderation (freedom of speech varies by country)

The jurisdiction problem will be addressed in depth through:
- **Article 32 of the Cybercrime Convention** (trans-border access to stored data)
- **Data retention directive**
- **Formal legal cooperation frameworks** (bilateral and multilateral mechanisms for cross-border evidence access)

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Jurisdiction Problem*

---

## 4. Legal Design

**Legal design** is the intersection of law, technology, and design — a framework developed by **Margaret Hagan** — aimed at making legal information more accessible and reducing information overload.

### Two Core Problems in Legal Communication

| Problem | Description |
|---------|-------------|
| **Information overload** | Legal documents (e.g., the EU AI Act) run to hundreds of pages; the complexity exceeds what any individual can absorb |
| **Written by experts, for experts** | Legal texts are written assuming legal expertise; but legal documents affect all citizens, not just lawyers |

### Why This Affects Computer Forensics
- A digitally forensic evidence report must be **understood by a judge or jury** — not just a technical colleague
- Forensic experts must develop the capability to explain complex technical findings in plain language
- Failure to communicate clearly can undermine an otherwise technically sound investigation

### The Engineer's Triangle at Google
Google's company structure historically placed **engineers at the top** of the decision-making triangle (with marketing and legal subordinate). This enabled rapid innovation, but also produced cases like the **Google Street View WiFi wiretapping incident**:
- Google Street View cars mapped streets AND captured payload data from **open (unencrypted) WiFi networks**
- The responsible engineer applied the "open WiFi = public" logic without legal consultation
- This triggered **140 criminal proceedings in 140 states worldwide**
- The engineer went into hiding to avoid being called as a witness across jurisdictions

**Lesson**: Even highly skilled engineers must understand the legal implications of their technical decisions.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Legal Design*

---

## 5. Dark Patterns

**Dark patterns** are user interface design choices that deliberately mislead users into actions they would not otherwise choose — typically benefiting the business at the user's expense.

### Example: Deleting an Amazon Account
The lecture walkthrough demonstrated that deleting an Amazon account requires:
1. Navigating to the Account page (no deletion option visible)
2. Scrolling to the bottom footer → "Let us help you"
3. "Need more help?" → "Contact us"
4. Selecting "Prime or something else" → "Login and security" → "Close my account"
5. Initiating a **chat with a human agent** who will try to discourage deletion

This pattern is referred to as a **"roach motel"** — easy to enter, nearly impossible to leave.

### Relevance to Digital Forensics
- When the law and technology are not combined properly, systems can create dark patterns that disadvantage **users without technical or legal literacy**
- Forensic experts and digital lawyers must be able to identify when technical complexity is a design choice that manipulates behaviour

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Dark Patterns*

---

## 6. GDPR Article 22 – Automated Decision-Making

> **Article 22 GDPR**: *"The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significant effects."*

### Why This Matters
As AI systems become capable of making (or strongly influencing) consequential decisions, Article 22 provides a right to **human oversight** in legal, employment, and other significant contexts.

### Case Studies in Automated Legal Decisions

#### Lex Machina (USA)
A software platform that predicts the probability of winning a case by analysing a specific judge's historical decisions. It was **banned in France in 2019** because:
- It creates a **bias effect on judges** (judges knowing they are being profiled may change behaviour)
- It allows clients to game the system by judge-shopping
- It produces an unfair metric for evaluating lawyers (outcome depends on client quality, not legal skill)

#### COMPAS System (USA, ~2016)
*Correctional Offender Management Profiling for Alternative Sanctions* — a risk assessment tool predicting recidivism likelihood.

ProPublica found that:
- White defendants who re-offended were disproportionately labelled **low risk**
- Black defendants who did not re-offend were disproportionately labelled **high risk**

This is a classic **garbage in, garbage out** problem — the algorithm absorbed historical bias in the training data.

### The Core Risk in Digital Forensics
A **false positive** in a digital forensics analysis can destroy a person's life. AI-assisted forensic analysis tools must be:
- Transparent (explainable)
- Subject to human verification
- Documented with a clear methodology (SHAP, LIME, or equivalent explainability frameworks)

**Key principle**: current generative AI tools are prohibited in formal legal proceedings (criminal, civil, labour law) because their outputs cannot be sufficiently explained and verified under current standards.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: GDPR Article 22 & Automated Decisions*

---

## 7. Natural Language vs. Mathematical Rules

Prof. Vaciago introduced a recurring philosophical theme:

> *Math exercise posed: Is "eleven plus two" = 11 or 14?*

In natural language, ambiguity is inherent. In mathematics, the result is unambiguous. Legal systems have traditionally relied on **natural language** → open to interpretation.

As digital systems (AI) increasingly make decisions using **mathematical rules**, engineers play a critical role: they can **encode legal reasoning** into systems that operate with precision. This creates both:
- **Opportunity**: more consistent and scalable enforcement
- **Risk**: if the rules are wrong, errors are systematic and large-scale

### Implication for Engineers
Future engineers will need a basic understanding of law — not to write legal documents, but to **translate legal intent into machine-readable logic**, avoiding systematic errors at scale.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Natural Language & Legal Interpretation*

---

## 8. Digital Forensics in Context – Three Domains

Prof. Vaciago distinguishes three major application domains for digital forensics:

| Domain | Description |
|--------|-------------|
| **Criminal forensics** | Forensic evidence used in criminal proceedings; highest standards; strong competence exists |
| **Civil forensics** | Family law disputes, contract disputes; extremely variable scope and complexity |
| **Corporate forensics** | Internal investigations within companies; no immediate court involvement; governed by labour law and internal policy |

Corporate forensics is growing rapidly because:
- Companies prefer to resolve issues internally (avoid public criminal or civil proceedings)
- Insider threats, data exfiltration, and policy violations are handled through internal investigation and HR processes

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Domains of Digital Forensics*

---

## 9. Terminology – "Digital" vs "Computer" Forensics

Prof. Vaciago uses **"digital forensics"** rather than "computer forensics" because the term *computer* refers to only one type of device that can carry digital evidence. The course is titled "Computer Forensics" for historical reasons; both terms are used interchangeably with no conceptual distinction intended.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Terminology [inferred]*

---

## 10. AI in Digital Forensics – Preliminary Assumption

A key clarification from Prof. Vaciago before proceeding to formal definitions:

> AI **cannot be used exclusively** in digital forensics. Both GDPR Article 22 and the EU AI Act, together with Italian law, require **human oversight** for any automated decision with significant legal effects.

### The Human Oversight Challenge
The practical difficulty is defining what "meaningful" oversight means:
- If every AI output must be reviewed in full, the efficiency advantage is eliminated
- But if oversight is reduced to a single confirmation click, it is meaningless

Finding a verifiable, proportionate oversight methodology — using explainability frameworks such as **SHAP** or **LIME** — is an open problem in digital forensics. This is particularly acute when handling very large datasets (e.g., 45 GB of WhatsApp messages, or 2 TB of emails), where automation is necessary but must be rigorously controlled to avoid life-altering false positives.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: AI & Digital Forensics [inferred]*

---

## 11. Definitions of Digital Evidence

Three widely-used definitions presented in the lecture:

| Definition | Source |
|------------|--------|
| *"Any information of evidential value, whether memorized or sent in a digital format"* | **SWGDE** (Scientific Working Group for Digital Evidence) — Prof. Vaciago's preferred definition |
| *"Any probative information stored or transmitted in a digital form that a party to a court case may use at trial"* | **Eugene Casey** |
| *"Information generated, stored or transmitted using electronic devices that may be relied upon in court"* | General *electronic evidence* definition |

The SWGDE definition is preferred because it is broader — it does not limit digital evidence to court use, acknowledging that digital evidence is also used in corporate and non-trial contexts. All three definitions convey the same core concept.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Digital Evidence – Definitions [inferred]*

---

## 12. Characteristics and Legal Requirements of Digital Evidence

### Key Characteristics

| Characteristic | Description |
|---------------|-------------|
| **Invisible** | Cannot be directly perceived — requires specialist tools and interpretation |
| **Alterable through normal use** | Normal interaction with a device (opening a file, starting a system) can modify or destroy evidence |
| **Infinitely copyable** | Can be copied without limit and without degradation; both a forensic opportunity and a challenge for containment |

### Legal Requirements

For evidence to be usable in legal proceedings it must satisfy:

| Requirement | Meaning |
|-------------|---------|
| **Admissible** | Gathered lawfully with appropriate legal grounds (e.g., a prosecutor or court order); without legal grounds, evidence gathered from a device is inadmissible even if it clearly incriminates the subject. Italian **Law 48/2008** explicitly provides that evidence gathered in violation of digital forensics procedure is inadmissible in court |
| **Authentic** | Free from tampering; every handling step must guarantee the evidence has not been altered |
| **Reliable and believable** | Must be understandable to the judge; the forensic expert's duty is to explain technical findings in plain, credible language — *"you must be able to explain the case to my mother"* |
| **Proportional** | The investigation must be limited to what is relevant to the case; personal information outside the scope must be excluded and protected |

### Proportionality – Practical Implications

| Scenario | Rule |
|---------|-----|
| **Extramarital affair discovered during fraud investigation** | Unrelated to the case; must not be disclosed to the court |
| **Social media screening in hiring** | Under **Article 8 of Law 300/1970** (the Workers' Statute), checking a job candidate's social media is a criminal offence (six months to one year); only CV information may be assessed |
| **Credit scoring via social media** | Since 2023, a **CCD directive** (Consumer Credit Directive) prohibits banks from using social media or web-based information to assess creditworthiness |
| **Social scoring risk** | Unchecked digital profiling leads to social scoring systems — threatening freedom of expression and democratic rights |
| **Excessive evidence strategy** | US courts prohibit flooding proceedings with unnecessary digital evidence; in Italy, submitting terabytes of marginally relevant evidence to cause delays and reach prescription (prescrizione) is a known, if problematic, strategy |

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Legal Requirements of Digital Evidence [inferred]*

---

## 13. Categories of Digital Evidence (Stephen Mason)

| Category | Description | Examples |
|----------|-------------|---------|
| **Human to human** | Created by a person for communication with another person | Emails, chat messages |
| **Human to PC** | Created by a person using a computer | Word documents |
| **Created by computer** | Automatically generated by a machine without human authorship | System logs, network flow records, IoT sensor data |
| **Mixed (human + computer)** | Data entered by human; result calculated by machine | Electronic spreadsheet |

The **computer-created evidence** category (logs) is the most important growing area of digital forensics — especially in complex systems such as autonomous vehicles, where multiple AI and software providers are involved and liability must be attributed based on log reconstruction. The **EU AI Act** requires AI providers to maintain clear log retention policies for this reason.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Categories of Digital Evidence [inferred]*

---

## 14. Definition of Digital Forensics & The Big Five (Council of Europe)

### Council of Europe Definition of Digital Forensics
1. Get hold of evidence **without modifying** the IT system in which it is found
2. Ensure evidence acquired in another medium is **identical to the original**
3. **Analyse data without modifying it**

### The Big Five – Council of Europe Principles

| Principle | Description |
|-----------|-------------|
| **Data integrity** | Evidence must not be altered at any stage |
| **Chain of custody** | Full, documented record of all evidence handling |
| **Specialist support** | A digital forensics expert must be involved |
| **Training** | First responders must be appropriately trained; an untrained person first on the scene (e.g., a bank employee or IT administrator) can inadvertently destroy evidence — some banks have begun providing basic digital forensics training to frontline staff |
| **Legality** | The person or agency in charge is responsible for ensuring the law and the above principles are adhered to |

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: Big Five – Council of Europe [inferred]*

---

## 15. NIST Standard and ISO 27037

Two key certification references for professional digital forensics practice:

### NIST – Four Phases

| Phase | Description |
|-------|-------------|
| **Collection** | Gather relevant data while maintaining forensic soundness |
| **Examination** | Extract and assess information from the collected data |
| **Analysis** | Interpret findings to draw conclusions about the incident |
| **Reporting** | Document results with a clear chain of custody and integrity verification |

The **reporting phase** is particularly important in NIST: presenting evidence clearly — in court or in a corporate context — is a core competency, not an afterthought.

NIST also incorporates a **risk management approach** (absent from ISO 27037): forensic experts working under a court-imposed deadline (e.g., two weeks) must make risk-based decisions about what to analyse in depth. Documenting the trade-off and its rationale is part of NIST compliance.

### ISO 27037
The primary European/international standard for digital evidence handling. For those wishing to work professionally in digital forensics, certification against ISO 27037 is recommended. Standards serve as "soft law" enabling cross-border professional recognition when formal legal frameworks are insufficient.

*ISO 27037 was not covered in this lecture due to time — to be addressed in subsequent sessions.*

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: NIST & ISO 27037 [inferred]*

---

## 16. CFI – Computer Forensics Italy

The **CFI (Computer Forensics Italy)** newsletter is a community of approximately 1,000–1,500 digital forensics professionals in Italy. Prof. Vaciago recommends following it as a resource for staying current in the Italian digital forensics landscape.

Two well-known Italian practitioners mentioned as examples of effective forensic communication:
- **Paolo Dalchecco** — works with Mediaset; appears as a forensic commentator
- **Stefano De Fratepietro** — also publicly known

Their public profiles stem from their ability to explain complex forensic concepts clearly to non-expert audiences — demonstrating that communication skills are as important as technical ones in this field.

> 📎 *Slide reference: `Slides/Vaciago/0_Introduction.pdf`, slide: CFI Community [inferred]*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Legal Design** | Framework combining law, technology, and design to make legal documents and processes more accessible |
| **Dark Pattern** | UI/UX design that deliberately misleads users into choices that benefit the platform |
| **GDPR Article 22** | EU regulation giving individuals the right not to be subject to solely automated consequential decisions |
| **COMPAS** | Risk assessment algorithm for recidivism prediction; found to exhibit racial bias |
| **Lex Machina** | AI tool predicting litigation outcomes by profiling judges; banned in France |
| **Jurisdiction** | The authority of a legal system over a person, entity, or digital activity |
| **Budapest Convention** | The primary international framework for cybercrime law (to be covered in depth) |
| **Corporate Forensics** | Digital forensic investigations conducted within organisations without formal legal proceedings |
| **OSINT** | Open Source Intelligence — gathering information from publicly available sources |
| **Digital Evidence** | Any information of evidential value, whether memorised or sent in digital format (SWGDE definition) |
| **SWGDE** | Scientific Working Group for Digital Evidence — body that produced the preferred definition of digital evidence |
| **Admissibility** | Legal requirement that evidence be gathered lawfully with appropriate legal authority; violated evidence may be excluded under Italian Law 48/2008 |
| **Proportionality** | Legal requirement that a forensic investigation use only information relevant to the case |
| **Big Five** | Council of Europe's five principles for digital forensics: data integrity, chain of custody, specialist support, training, legality |
| **NIST** | US national standard defining the four phases of digital forensics: collection, examination, analysis, reporting |
| **ISO 27037** | International standard for digital evidence handling; key certification for professional digital forensic practitioners |
| **CFI** | Computer Forensics Italy — professional community of ~1,000–1,500 Italian digital forensics experts |

---

## Summary

- Prof. Vaciago's part of the course focuses on the **legal dimension** of digital forensics, including international frameworks and Italian case studies.
- Technology evolution (Tools → Data Collection → AI Decision-making) brings new legal challenges at each stage, especially regarding jurisdiction.
- **Legal design** and engineers play a critical role in translating complex legal intent into machine-readable, accessible logic.
- **Dark patterns** illustrate how UI/UX can be intentionally designed to disadvantage users, requiring forensic and legal scrutiny.
- **GDPR Article 22** and Italian law mandate **meaningful human oversight** for automated decisions to avoid life-altering false positives.
- Digital evidence must satisfy the "Big Four": **admissible** (lawful), **authentic** (untampered), **reliable** (credible), and **proportional** (relevant).
- The **Big Five** principles (Council of Europe) and **NIST phases** provide the technical and procedural foundation for sound forensic practice.
- **NIST** uniquely includes a risk management dimension, essential for making documented trade-offs under court-imposed deadlines.
- Corporate forensics is a rapidly growing domain where companies resolve issues (insider threats, data exfiltration) internally through HR and policy.
- AI-assisted tools must be transparent and verifiable; current generative AI is generally prohibited from formal legal outputs due to explainability gaps.
