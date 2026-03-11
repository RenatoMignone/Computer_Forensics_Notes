# Chapter 1 – Definitions, Standards, and the Evidence Location Model
**Professor:** Vaciago  
**Reference Slides:** [`Slides/Vaciago/1_Definition.pdf`]  
**Covered in Lectures:** Lecture 6

---

## Introduction
This chapter provides the definitional and normative foundation for digital forensics from a legal perspective. It distinguishes the three domains in which forensic work occurs, maps the key international standards governing each phase of a forensic investigation, and introduces the model forensic practitioners use to locate digital evidence across physical devices and cloud infrastructure. It concludes with a comparative study of the US and EU prosecution models and how they shape the demand for forensic expertise.

> 📝 *For the introductory framing of the legal challenges surrounding technology and jurisdiction, see [0_Introduction.md](../Vaciago/0_Introduction.md).*

---

## 1. Three Domains of Digital Forensics

Digital forensics is not a monolithic discipline. It operates across three substantially different legal and operational contexts:

| Domain | Context | Primary Legal Framework | Typical Commissioning Party |
|--------|---------|------------------------|---------------------------|
| **Criminal Forensics** | State prosecution of crimes | Criminal procedure law (varies by jurisdiction); evidence statutes; Convention on Cybercrime | Police; prosecutor's office |
| **Civil Forensics** | Disputes between private parties; employment matters; IP litigation | Civil procedure; rules of evidence; employment law | Law firms; corporate legal departments |
| **Corporate / Internal Forensics** | Incident response; insider threat; regulatory compliance | Employment contracts; internal policies; data protection law (GDPR) | CISO; HR; Compliance |

### Key Differences in Practice
- **Criminal forensics** has the most stringent chain of custody requirements and the strictest admissibility rules — evidence must meet criminal procedure standards. Results must be repeatable by a defence expert.
- **Civil forensics** operates under a lower evidential standard (balance of probabilities vs. beyond reasonable doubt); European civil procedure generally requires forensic evidence to be produced by a court-appointed expert.
- **Corporate forensics** is the most flexible but also the most ethically complex — employees have privacy rights even in a corporate environment; GDPR directly constrains how employee data may be collected and examined.

> 📎 *Slide reference: `1_Definition.pdf` — Three Domains*

---

## 2. International Forensic Standards

Standardisation in digital forensics defines what constitutes a technically valid and legally acceptable investigation procedure.

| Standard | Issuing Body | Scope |
|----------|-------------|-------|
| **ISO/IEC 27037:2012** | ISO/IEC JTC 1/SC 27 | Guidelines for identification, collection, acquisition, and preservation of digital evidence |
| **ISO/IEC 27001** | ISO/IEC JTC 1/SC 27 | Information security management system (ISMS) standard; forms the basis for cybersecurity compliance certification |
| **NIST SP 800-86** | US National Institute of Standards & Technology | Guide to integrating forensic techniques into incident response; four-phase model |
| **ACPO Guidelines** | UK Association of Chief Police Officers | Four forensic principles; heavily influential in UK courts and beyond |

### The Standardisation Challenge
International standards in digital forensics face a structural tension:
- **Technology evolves faster than standards**: A cloud forensics standard published today may be obsolete when a new cloud architecture is adopted in 18 months
- **Jurisdiction fragmentation**: What is acceptable evidence procedure in Italy may not satisfy a US federal court; cross-border investigations require simultaneous compliance with multiple frameworks
- **Certification gaps**: Unlike established professions, there is no universal mandatory certification for digital forensic practitioners; multiple competing frameworks exist without a single globally recognised accreditor

> *This fragmentation creates a perverse incentive: an investigator who follows best practice in one jurisdiction may inadvertently violate another jurisdiction's rules, leading to evidence exclusion.*

> 📎 *Slide reference: `1_Definition.pdf` — Standards & Challenges*

---

## 3. Suspect Identification: OSINT and IP Address Tracing

Before physical evidence can be collected, investigators must identify the suspect. In digital investigations, suspect identification typically begins with the IP address.

### OSINT in Suspect Identification

OSINT (Open Source Intelligence) — gathering intelligence from publicly available sources — is generally lawful and forms an early part of many investigations. Investigators must be aware of the limits: any form of interaction that generates logs on systems the subject controls may require formal authorisation in many jurisdictions.

### IP Address Tracing: The 4-Step Process

| Step | Actor | Action | Legal Instrument Required |
|------|-------|--------|--------------------------|
| **1. Identify the IP** | Investigator | An IP address is associated with a specific crime event (log, timestamp) | None — IP is in an existing log |
| **2. Identify the ISP** | Investigator | WHOIS/ARIN/RIPE database lookup resolves the IP to its owning ISP | None — databases are public |
| **3. Identify the subscriber** | ISP (compelled) | ISP's customer records map the IP + timestamp to an account holder (name, address) | **Court order / data preservation order** — ISPs cannot disclose subscriber data without legal basis |
| **4. Identify the individual** | Police / investigator | Account holder may not be the suspect (e.g., shared Wi-Fi, compromised router) — further investigation required | Physical search, seizure, digital forensics |

> ⚠️ *An IP address identifies an internet connection, not a person. Step 4 is always required and is often where cases become complex.*

> 📎 *Slide reference: `1_Definition.pdf` — Suspect Identification*

---

## 4. The Digital Evidence Location Model

Where might the relevant evidence reside? Vaciago presents a **four-level hierarchical model** of evidence location that guides the forensic examiner's search strategy.

| Level | Location | Typical Evidence | Access Mechanism |
|-------|---------|-----------------|-----------------|
| **Level 1** | Personal computer / laptop (suspect's device) | Files, browsing history, email client data, installed software, registry, RAM | Physical seizure and forensic imaging |
| **Level 2** | Mobile phone / tablet | Call logs, messages (WhatsApp, Signal, iMessage), location data, app data, cloud sync artefacts | Physical seizure; mobile forensic tools (UFED/Cellebrite) |
| **Level 3** | ISP / network provider logs | Connection logs, IP assignment records, DNS queries, traffic metadata | Formal legal request (court order, data preservation notice); subject to retention law |
| **Level 3b** | Bank and digital payment providers (Stripe, PayPal) | Transaction records, linked accounts, device/IP metadata | Formal legal request; "follow the money" — financial data can corroborate device and IP evidence |
| **Level 4** | Cloud services | Email (Gmail, Outlook 365), cloud storage (Drive, OneDrive, iCloud), social media, collaborative tools | Formal cross-border legal procedures or compelled production via US parent company; complex and time-consuming |

### Progression Implications
- Level 1 and Level 2 evidence is **directly accessible** once a seizure warrant is obtained — the investigator has physical custody
- Level 3 evidence depends on **data retention policy** in the relevant jurisdiction; if the investigation begins after the retention window, the data is gone
- Level 4 evidence is subject to **cross-border legal procedures** which can take months to years; cloud providers may also challenge requests or provide only partial responses

> 📎 *Slide reference: `1_Definition.pdf` — Evidence Location Model*

---

## 5. Mobile Forensics

Mobile devices represent one of the richest sources of digital evidence and one of the most challenging acquisition targets.

### Challenges Specific to Mobile Forensics

| Challenge | Description |
|-----------|-------------|
| **Encryption** | Modern smartphones (iOS and Android) are encrypted at rest by default; without the passcode, the physical image is largely unreadable |
| **Remote wipe** | Remote wipe capability is standard; device must be placed in a Faraday bag immediately upon seizure to prevent the command |
| **Multiple connectivity interfaces** | Bluetooth, Wi-Fi, cellular, and NFC must all be blocked simultaneously |
| **Storage architecture** | Internal flash storage architecture differs from conventional hard drives; standard acquisition tools may not apply directly |

### UFED (Universal Forensic Extraction Device)
Cellebrite's UFED is the leading mobile forensic extraction platform used by law enforcement worldwide:

| Feature | Detail |
|---------|--------|
| **Extraction** | Requires physical connection for full extraction; continuously updated to support new phone models |
| **Cost** | Extremely expensive: hardware unit, software licences, and annual update subscriptions required |

> *Cost is a significant barrier: only well-funded law enforcement agencies and large forensic firms can afford to maintain current UFED capability. This creates a two-tier forensic landscape.*

> 📎 *Slide reference: `1_Definition.pdf` — Mobile Forensics*

---

## 6. US vs. EU Prosecution Models

The approach to criminal prosecution differs fundamentally between the United States and the European Union (taking Italy as the representative EU example).

| Dimension | United States | Italy / EU |
|-----------|--------------|-----------|
| **Prosecution model** | **Discretionary / adversarial** | **Compulsory / inquisitorial** |
| **Filing decision** | Prosecutor has **wide discretion** to decide whether to bring charges; decisions shaped by resource availability, strategic priority, likelihood of conviction | Prosecutor is **obligated by law to open a preliminary investigation** for any notified crime; greater constraint on prosecutorial discretion |
| **Who investigates** | Law enforcement with prosecutorial guidance; forensic work largely in-house | Judicial police under direction of the prosecutor; independent court-appointed forensic expert for major contested issues |
| **Forensic investment driver** | **Commercial and civil litigation**: major technology and IP disputes drive demand for private-sector forensic firms | **Criminal justice system** drives most forensic demand; private forensic firms also active in corporate and civil matters |

### Why the Model Affects Forensic Practice
- In the **US adversarial model**, forensic experts are retained by one side; their role is to support the retaining party's case. Expert credibility is tested through cross-examination.
- In the **Italian inquisitorial model**, the court-appointed expert is formally neutral; their report goes to the judge without being filtered through adversarial advocacy. Party-retained experts can challenge the court expert's findings.
- **This creates different quality pressures**: US forensic reports must withstand aggressive cross-examination; Italian court-appointed reports must satisfy the technical judge and survive scrutiny from party experts.

> 📎 *Slide reference: `1_Definition.pdf` — Prosecution Models*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Criminal Forensics** | Forensic investigation supporting state criminal prosecution; highest evidentiary standards |
| **Civil Forensics** | Forensic investigation in civil or employment disputes; lower standard of proof |
| **Corporate Forensics** | Internal forensic investigation; subject to employment law and GDPR constraints |
| **ISO/IEC 27037** | International standard for identification, collection, acquisition, and preservation of digital evidence |
| **ISO/IEC 27001** | International standard for information security management systems (ISMS); key for cybersecurity compliance |
| **OSINT** | Open Source Intelligence — intelligence gathered from publicly available sources |
| **IP Tracing** | 4-step process: identify IP → resolve to ISP → obtain subscriber data (via court order) → identify individual |
| **Evidence Location Model** | Multi-level hierarchy: personal device → mobile → ISP logs + financial providers → cloud; defines escalating access complexity |
| **UFED** | Universal Forensic Extraction Device (Cellebrite); leading mobile forensic hardware platform |
| **Remote Wipe** | Command sent over network to wipe a device's storage; requires immediate Faraday isolation on seizure |
| **Follow the money** | Investigative principle: bank accounts and digital payment providers (Stripe, PayPal) often hold corroborating evidence |
| **Compulsory Prosecution** | Legal system (e.g., Italy) in which prosecutors are obligated by law to open investigations for all reported crimes |
| **Discretionary Prosecution** | Legal system (e.g., US) in which prosecutors have broad discretion to decide whether to bring charges |

---

## Summary

- Digital forensics operates in three distinct domains — **criminal, civil, and corporate** — each with different legal standards, procedural constraints, and evidentiary requirements.
- International standards (ISO/IEC 27037, **ISO/IEC 27001**, NIST SP 800-86, ACPO) provide the normative framework, but **standardisation is structurally challenged** by rapid technological change and jurisdictional fragmentation.
- **Suspect identification** in digital investigations typically proceeds through OSINT + IP address tracing (4 steps), with a court order required at step 3 to compel ISP subscriber disclosure.
- The **digital evidence location model** maps evidence across device → mobile → ISP/financial providers → cloud. **Bank and payment providers** (Stripe, PayPal) are important evidence sources: "follow the money" is a core investigative principle. Level 4 (cloud) requires formal cross-border procedures.
- **Mobile forensics** is technically demanding: encryption, remote wipe risk, and cloud-only storage require immediate Faraday isolation and tools like UFED — at significant cost.
- The **US adversarial model** and **EU inquisitorial model** create different forensic quality pressures: US experts must withstand cross-examination; Italian court-appointed experts must satisfy the formal judicial expert role.
