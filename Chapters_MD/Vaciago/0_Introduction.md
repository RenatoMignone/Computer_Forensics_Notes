# Chapter 0 – Introduction: Technology, Law & Digital Forensics
**Professor:** Vaciago  
**Reference Slides:** [`Slides/Vaciago/0_Introduction.pdf`]  
**Covered in Lectures:** Lecture 3

---

## Introduction
This introductory chapter establishes the legal perspective of the course. It examines how the relationship between technology and law has evolved, introduces the concept of legal design, analyses dark patterns as an example of the technology-law gap, and situates digital forensics within three distinct legal domains. The chapter also presents two key case studies in automated decision-making — Lex Machina and COMPAS — to frame the dangers of AI in forensic and legal contexts. Together, these topics provide the conceptual foundation for all subsequent legal chapters.

---

## 1. Course Structure – Legal Component

Prof. Vaciago's component of the course comprises:
- **~15 hours of theoretical lessons** — covering international conventions, Italian law, jurisdiction, and case law
- **~25 hours of laboratory simulation** — a procedural trial simulation

### Laboratory Simulation Format
- Students are divided into **prosecutors** and **defence lawyers**
- Prof. Vaciago acts as judge (an AI judge may be trialled as an experiment)
- Focus is on **legal argumentation**, not technical analysis
- Goal: develop oral advocacy skills and understand how digital evidence is presented and challenged in court

### Upcoming Topics
| Topic | Description |
|-------|-------------|
| **Cybercrime Convention** | Budapest Convention — primary international framework for cybercrime |
| **UN Convention** | Brief overview of UN-level cybercrime instruments |
| **Italian law** | Primary focus given the predominantly Italian student population |
| **Garlasco case** | Famous Italian digital forensics case — focus on digital evidence issues |
| **IoT & Digital Forensics** | Forensic principles applied to IoT devices |
| **Territorial principle** | Jurisdiction and the Hackington case |
| **AI & Digital Forensics** | Emerging questions about AI-generated and AI-analysed evidence |
| **Case study / lab** | Full laboratory simulation |

> 📎 *Slide reference: `0_Introduction.pdf` — Course Overview*

---

## 2. The Evolution of Technology and Its Legal Implications

Technology's relationship with society — and therefore with law — has undergone three distinct paradigm shifts:

| Era | Paradigm | Description |
|-----|----------|-------------|
| Pre-2000 | **Technology between us** | Communication tools (telephone, email) that people use to exchange information *with each other* |
| 2008+ | **Technology about us** | Social media (Facebook/Meta) — technology that collects and creates data *about* us; generates psychological and social data as a by-product |
| Present / Future | **Technology in us** | AI — technology embedded in our decision-making processes; influences cognition and behaviour, not just communication |

### Why This Framework Matters for Digital Forensics

- **Technology about us** (social media) generates vast, persistent **evidence trails** — location data, social graphs, behavioural patterns, content. This evidence is legally complex: it crosses borders, is controlled by third parties, and reflects intimate personal information.
- **Technology in us** (AI) raises entirely new questions: when an AI system makes a consequential decision, who is legally accountable? Can the decision be explained? Can it be challenged? These questions directly affect forensic admissibility.
- The **speed of technological evolution** consistently outpaces legal frameworks, creating gaps that forensic practitioners — both technical and legal — must navigate.

> 📎 *Slide reference: `0_Introduction.pdf` — Technology Evolution (3 Paradigms)*

---

## 3. The Jurisdiction Problem

A recurring and fundamental theme throughout the course:

> *"When you go to Instagram, from a virtual standpoint, you are going to the United States. You are not in Italy."*

### The Core Tension

| User Perception | Legal Reality |
|----------------|---------------|
| I am physically in Italy, so Italian law applies to my online activity | The service is hosted by a US company; the platform is governed primarily by US law |
| My data is "on my phone" | Your data is stored in data centres subject to US law, regardless of your nationality |

### Practical Consequences

- **Criminal investigation**: Italian authorities cannot unilaterally compel a US platform to disclose data. They must rely on formal legal mechanisms (Mutual Legal Assistance Treaties, GDPR transfer provisions, or the US CLOUD Act).
- **Content moderation**: defamation is a criminal offence in Italy (Article 595 Penal Code) but is broadly protected speech in the US under the First Amendment. A US platform may lawfully host content that is criminal under Italian law.
- **Data retention**: an Italian court order to preserve data with a US provider may not be legally enforceable without going through MLAT procedures — which can take months.

### Mechanisms Addressing the Jurisdiction Gap
These will be covered in detail in later chapters:
- **Budapest Convention, Article 32** — trans-border access to stored computer data
- **EU Data Retention Directive (and its national implementations)**
- **MLAT (Mutual Legal Assistance Treaty)** system — formal bilateral/multilateral cooperation framework
- **US CLOUD Act (2018)** — allows US law enforcement to compel US companies to produce data stored anywhere globally

> 📎 *Slide reference: `0_Introduction.pdf` — Jurisdiction Problem*

---

## 4. Legal Design

**Legal design** is a framework developed by **Margaret Hagan** at the intersection of law, technology, and design. Its goal is to make legal information and processes accessible to non-experts, reducing information overload and improving comprehension.

### Two Core Problems in Legal Communication

| Problem | Manifestation |
|---------|---------------|
| **Information overload** | Legal documents (e.g., the EU AI Act) span hundreds of pages; complexity exceeds individual absorption |
| **Written by experts, for experts** | Legal texts assume legal expertise but affect all citizens |

### Relevance to Computer Forensics
A digital forensic expert report must be understood by a **judge or jury** — not just a peer reviewer. The ability to translate complex technical findings into plain, legally actionable language is a core competency for forensic practitioners.

### Case Study: Google Street View WiFi Incident
Google's historical engineering culture placed **engineers at the apex** of internal decision-making (with marketing and legal subordinate). This enabled rapid innovation but created the following incident:

- Google Street View cars, while photographing streets, also captured **payload data from unencrypted (open) WiFi networks**.
- The responsible engineer applied the technical logic: *open WiFi = public = no privacy expectation*.
- This was done **without legal review**.
- Outcome: **140 criminal proceedings in 140 states worldwide**.
- The engineer went into hiding to avoid being called as a witness across multiple jurisdictions.

**Lesson**: even highly skilled engineers must understand the legal implications of technical decisions. The technical validity of an action does not determine its legality.

> 📎 *Slide reference: `0_Introduction.pdf` — Legal Design*

---

## 5. Dark Patterns

**Dark patterns** are user interface and user experience design choices that **deliberately mislead users** into actions they would not otherwise take — typically to the benefit of the business and the detriment of the user.

### Example: Deleting an Amazon Account

The lecture walkthrough demonstrated that deleting an Amazon account requires navigating through multiple obfuscating layers:

1. Account page — no deletion option visible
2. Footer → "Let us help you"
3. "Need more help?" → "Contact us"
4. "Prime or something else" → "Login and security" → "Close my account"
5. Initiation of a **live chat with a human agent** trained to discourage deletion

This pattern is known as a **"roach motel"**: easy to enter, deliberately difficult to leave.

### Classification of Dark Patterns
Dark patterns include (but are not limited to):
- **Roach motel**: easy sign-up, deliberately obfuscated cancellation
- **Hidden costs**: fees revealed only at the final checkout step
- **Confirmshaming**: opt-out language designed to make refusal feel negative (e.g., "No thanks, I don't want to save money")
- **Misdirection**: visually directing attention away from the option the user would prefer

### Relevance to Digital Forensics
- Dark patterns create a **technology-law gap** that disadvantages users without technical or legal literacy.
- In investigations, identifying whether a platform used dark patterns to obtain "consent" can affect the admissibility of data obtained under that consent.
- Dark patterns may constitute **unfair commercial practices** under EU consumer protection law — forensic documentation of UI flows is sometimes required as evidence.

> 📎 *Slide reference: `0_Introduction.pdf` — Dark Patterns*

---

## 6. GDPR Article 22 – Automated Decision-Making

> **Article 22 GDPR**: *"The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significant effects."*

This provision establishes a right to **human oversight** wherever automated processing produces consequential outcomes.

### Case Study 1: Lex Machina (USA)
Lex Machina is a software platform that predicts the probability of winning a legal case by analysing a specific judge's historical decisions.

**Banned in France (2019)** because:
- It creates a **behavioural bias effect** on judges (awareness of being profiled may alter judicial behaviour, undermining independence)
- It enables **judge shopping** — routing cases to judges statistically favourable to a client's position
- It produces a **distorted performance metric** for lawyers — outcomes depend on client quality and judge assignment, not legal skill

### Case Study 2: COMPAS (USA, ~2016)
*Correctional Offender Management Profiling for Alternative Sanctions* — an algorithmic risk assessment tool predicting the likelihood of recidivism, used in sentencing decisions.

**ProPublica investigation findings**:
- White defendants who subsequently re-offended were disproportionately labelled **low risk**
- Black defendants who did not re-offend were disproportionately labelled **high risk**

This is a textbook **garbage in, garbage out** problem: the algorithm absorbed historical biases present in the training data (racially unequal historical enforcement patterns) and reproduced them systematically at scale.

### Implications for Digital Forensics

| Risk | Consequence |
|------|-------------|
| **False positive** in forensic analysis | An innocent person may be convicted; AI-assisted forensic tools that produce unexplainable results are dangerous |
| **Lack of explainability** | Forensic tools must be transparent; SHAP, LIME, or equivalent frameworks provide partial explanation |
| **Current prohibition** | Generative AI outputs are currently **prohibited in formal legal proceedings** (criminal, civil, labour) because they cannot be sufficiently explained and verified under existing evidentiary standards |

> 📎 *Slide reference: `0_Introduction.pdf` — GDPR Article 22 & Automated Decision-Making*

---

## 7. Natural Language vs. Mathematical Rules

A philosophical theme that recurs throughout the legal component of the course:

> *Math exercise: Is "eleven plus two" equal to 11 or 14?*

- In **natural language**, the sentence is ambiguous ("eleven" could be parsed as a numeral or as part of "eleventh plus two", etc.).
- In **mathematics**, the result is unambiguous: $11 + 2 = 13$.

Legal systems have traditionally relied on **natural language** → which is inherently open to interpretation, subject to evolving meaning, and dependent on context.

As AI systems encode legal rules as **mathematical logic**, the properties of that encoding become critical:
- Errors become **systematic** rather than individual (a biased algorithm produces biased decisions at scale)
- Rules lose the **interpretive flexibility** that allows natural language law to adapt to edge cases
- **Engineers** are increasingly the people who translate legal intent into executable logic — a significant responsibility

### Implication for Engineers
Future engineers working in legal-adjacent fields must understand **enough law** to translate legal intent into machine-readable logic without introducing systematic legal errors. They do not need to write legal documents — but they must understand the legal consequences of their technical choices.

> 📎 *Slide reference: `0_Introduction.pdf` — Natural Language & Legal Interpretation*

---

## 8. Three Domains of Digital Forensics

Digital forensics is applied across three distinct legal contexts, each governed by different rules, standards, and investigative powers:

| Domain | Legal Framework | Typical Actor | Key Characteristics |
|--------|----------------|---------------|---------------------|
| **Criminal forensics** | Criminal procedural law; state-led prosecution | Police, court-appointed forensic experts, prosecutors | Highest evidence standards; strong institutional competence; governed by criminal procedure codes |
| **Civil forensics** | Civil litigation; burden of proof on claimant | Private forensic experts, court-appointed consultants | Extremely variable scope and complexity; family law, contract disputes, IP theft |
| **Corporate / incident response** | Labour law, internal HR policy, compliance frameworks | Corporate security teams, external consultants | No immediate court involvement; governed by employment contracts and internal policy; growing rapidly |

### Why Corporate Forensics is Growing
- Companies prefer to resolve issues **internally** rather than through public criminal or civil proceedings (reputational risk, cost, speed)
- Insider threats, data exfiltration, policy violations, and fraud are often handled through **internal investigation → HR action → quiet dismissal**
- Even where evidence is later handed to law enforcement, the initial investigation is typically corporate

> 📎 *Slide reference: `0_Introduction.pdf` — Three Domains of Digital Forensics*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Legal Design** | Framework combining law, technology, and design to make legal processes accessible to non-experts |
| **Dark Pattern** | UI/UX design that deliberately misleads users into choices that benefit the platform at the user's expense |
| **GDPR Article 22** | EU regulation giving individuals the right not to be subject to solely automated consequential decisions |
| **COMPAS** | Algorithmic recidivism-prediction tool found to exhibit racial bias; foundational case for AI fairness in law |
| **Lex Machina** | AI tool predicting litigation outcomes by profiling judges; banned in France for undermining judicial independence |
| **Jurisdiction** | The authority of a legal system over a person, entity, or digital activity |
| **Budapest Convention** | Principal international framework for cybercrime law and cross-border digital evidence cooperation |
| **MLAT** | Mutual Legal Assistance Treaty — bilateral/multilateral mechanism enabling cross-border legal cooperation |
| **CLOUD Act** | US Clarifying Lawful Overseas Use of Data Act (2018) — allows US authorities to compel US companies to produce data stored anywhere in the world |
| **Corporate Forensics** | Digital forensic investigations conducted within organisations prior to or instead of formal legal proceedings |
| **Roach Motel** | Dark pattern where signing up is easy but cancellation is deliberately obfuscated |
| **COMPAS bias** | Systematic error in which a risk-assessment algorithm reproduces historical racial inequities from training data |
| **Garbage in, garbage out** | Principle that a biased or flawed training dataset produces biased or flawed model outputs regardless of methodological rigour |

---

## Summary

- Technology has evolved through three paradigms — *between us* (tools) → *about us* (data collection) → *in us* (AI decision-making) — each generating new forensic challenges and legal gaps.
- The **jurisdiction problem** is the central unresolved tension of digital forensics: users are physically in one country while their digital activity falls under the law of another.
- **Legal design** addresses the gap between technical/legal complexity and user comprehension; forensic practitioners must communicate findings clearly to non-expert audiences.
- **Dark patterns** demonstrate how technology deliberately exploits the technology-law gap to the detriment of users — relevant both to evidence gathering and GDPR compliance enforcement.
- **GDPR Article 22** establishes a right to human oversight of automated consequential decisions; its application to forensic AI tools means such tools must be explainable and verifiable.
- The **COMPAS** case shows that algorithmic bias at scale is more dangerous than individual human bias — it is reproducible, systematic, and laundered through the apparent objectivity of mathematics.
- Current generative AI tools are **prohibited in formal legal proceedings** due to insufficient explainability.
- Digital forensics operates across three domains — criminal, civil, corporate — each with distinct rules, actors, and evidentiary standards.
