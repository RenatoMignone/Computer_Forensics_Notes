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
- **The MLAT (Mutual Legal Assistance Treaty) system**

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

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Legal Design** | Framework combining law, technology, and design to make legal documents and processes more accessible |
| **Dark Pattern** | UI/UX design that deliberately misleads users into choices that benefit the platform |
| **GDPR Article 22** | EU regulation giving individuals the right not to be subject to solely automated consequential decisions |
| **COMPAS** | Risk assessment algorithm for recidivism prediction; found to exhibit racial bias |
| **Lex Machina** | AI tool predicting litigation outcomes by profiling judges; banned in France |
| **Jurisdiction** | The authority of a legal system over a person, entity, or digital activity |
| **Cybercrime Convention** | Budapest Convention — the primary international framework for cybercrime law (to be covered in depth) |
| **Corporate Forensics** | Digital forensic investigations conducted within organisations without formal legal proceedings |
| **MLAT** | Mutual Legal Assistance Treaty — bilateral/multilateral mechanisms for cross-border legal cooperation |
| **OSINT** | Open Source Intelligence — gathering information from publicly available sources |

---

## Summary

- Prof. Vaciago's part of the course focuses on the **legal dimension** of digital forensics, including international frameworks, Italian law, and real case studies.
- Technology has evolved from being *between us* (tools) → *about us* (data collection) → *in us* (AI decision-making), each stage bringing new legal and forensic challenges.
- The **jurisdiction problem** is a fundamental issue: digital activity crosses borders while users remain physically in one country.
- **Legal design** aims to bridge the gap between legal complexity and user comprehension — engineers have a growing role in this process.
- **Dark patterns** illustrate how technology can be intentionally designed to disadvantage users — relevant to evidence gathering and legal compliance analysis.
- **GDPR Article 22** establishes a right to human oversight of automated decisions; this has direct implications for AI-assisted forensic analysis.
- A **false positive** in digital forensics is not just a technical error — it can destroy a person's life; AI tools must be transparent and verifiable.
