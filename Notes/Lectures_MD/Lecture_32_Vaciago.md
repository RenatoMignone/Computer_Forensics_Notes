# Lecture 32 – Corporate Forensics and the TechMed Data Breach Laboratory
**Professor:** Vaciago  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Vaciago/07_TechMed_Forensics_Law.pdf`

---

## Overview
This lecture introduces the final legal-track laboratory on corporate forensics through the TechMed case. Vaciago explains why most digital-forensics work in companies never reaches trial, why Italian labour-law limits matter when investigating employee devices, and how the TechMed incident combines malware, business email compromise, data breach obligations, criminal offences, and organisational failures.

---

## 1. Course Administration and Bonus Points

The lecture opens with an administrative check of homework and laboratory bonus points. Vaciago asks students to verify whether their names and scores have been correctly recorded before the exam.

This material is administrative and is indexed as a side event rather than absorbed into chapter notes.

---

## 2. Corporate Forensics

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — Corporate forensics laboratory*

Vaciago describes **corporate forensics** as digital-forensics work carried out inside a company, often after an incident, where the matter may never become a criminal, civil, or labour trial.

He estimates that most corporate forensic analyses remain internal. Even so, the same procedural discipline matters, because evidence may later need to support:
- a criminal complaint;
- a labour dispute;
- a civil claim;
- a regulatory notification;
- an insurance or contractual dispute;
- an internal decision about responsibility and remediation.

---

## 3. Employee Devices, Company Data, and Labour-Law Limits

Vaciago stresses that managers often make a dangerous assumption: because the company owns the hardware, it can inspect all data on it. The hardware may belong to the company, but the data may include employee personal data, communications, opinions, or protected private material.

Italian labour-law rules, especially the **Statuto dei Lavoratori**, restrict employee monitoring. Vaciago highlights two recurring risks:
- pressure from the CEO to inspect immediately;
- pressure to reduce cost by skipping proper forensic and legal procedure.

The forensic examiner must resist both pressures. If the procedure is not respected, the examiner may personally become the weak point in a later dispute.

---

## 4. AI Monitoring and Workplace Control

The lecture includes a discussion of AI-enabled employee monitoring. Vaciago uses examples involving employer attempts to control employee behaviour, AI prompts, or AI outputs.

The point is not a full AI-law lesson. The forensic relevance is that corporate investigations increasingly involve systems that can monitor employees at scale, making the boundary between security control and unlawful workplace surveillance harder to maintain.

---

## 5. TechMed Case Scenario

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — The TechMed case and timeline*

TechMed S.r.l. is presented as an 85-employee company with patient-management software, employee records, hospital/clinic contacts, and a cloud testing database containing patient-related data.

The incident timeline is:
- 15 April 2026, 08:45: phishing email sent to Giovanni Martini;
- 08:50: Martini opens `Payroll_Form_2026.docx`;
- 08:52: first command-and-control connection, with 450 KB exfiltrated;
- 09:15: second C2 connection, with 12.3 MB exfiltrated;
- 10:30: the finance manager receives a spoofed CEO email requesting a EUR 95,000 transfer;
- 11:15: the finance manager authorizes the wire transfer;
- 16 April 2026, 09:00: the CEO denies sending the email;
- 10:00: the IT manager discovers exfiltration;
- 14:30: the DPO is informed;
- 15:00: the workstation is isolated without shutdown and Forensics Italia is engaged;
- 17 April 2026: disk, RAM, firewall logs, and email server logs are acquired;
- 18 April 2026: a criminal complaint is filed in Turin.

---

## 6. Evidence Collection Priority

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — Digital evidence collection priority*

The case requires a priority order:

| Priority | Evidence | Reason |
|----------|----------|--------|
| 1 | RAM dump | Most volatile; may contain processes, connections, keys, and malware traces. |
| 2 | Disk image | Workstation is isolated but still running; acquire bit-for-bit image and preserve hashes. |
| 3 | Firewall logs | Active-system evidence useful for exfiltration reconstruction. |
| 4 | Email server logs | Structured logs and headers useful for phishing and spoofing reconstruction. |

Vaciago connects this to the broader course rule: urgency does not remove the need for chain of custody, hashing, documentation, and proper acquisition.

---

## 7. Criminal, GDPR, and Organisational Analysis

The laboratory asks students to analyze:
- **Article 615-ter c.p.**, unauthorized access to TechMed systems;
- the possible fraud offence connected to the EUR 95,000 transfer;
- whether the facts fit computer fraud or another form of fraud;
- GDPR notification deadlines and communication to data subjects;
- organisational failures and remedies.

The organisational failures include:
- no SPF, DKIM, or DMARC protection against spoofed CEO email;
- no emergency payment verification procedure;
- insufficient antivirus detection against polymorphic or zero-day malware;
- lack of anti-phishing training.

---

## 8. Laboratory Questions

The final assignment asks students to:
- describe the correct evidence-collection order and integrity hashes;
- infer likely exfiltrated content from firewall logs and transfer sizes;
- reconstruct the malware infection chain and identify disk artifacts;
- analyze criminal offences and their factual elements;
- identify organisational failures and remediation measures;
- draft a simple payment-verification policy for transfers above EUR 50,000.

Vaciago notes that the legal analysis may go beyond the articles suggested in the slides if students can justify the alternative view.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Corporate Forensics** | Internal digital-forensics work performed for a company, often after an incident and often before any trial exists. |
| **Business Email Compromise** | Fraud pattern where an attacker impersonates a trusted business actor to induce payment or disclosure. |
| **DPO** | Data Protection Officer, the organisational contact for GDPR breach handling. |
| **SPF** | Email authentication mechanism listing authorized sending servers for a domain. |
| **DKIM** | Email authentication mechanism using cryptographic signatures in message headers. |
| **DMARC** | Policy mechanism combining SPF and DKIM results to reject or quarantine spoofed mail. |
| **Chain of Custody** | Documentation proving who handled evidence, when, how, and under what integrity controls. |

---

## Summary
- Corporate forensics often stays inside the company, but it must still be procedurally defensible.
- Owning the device does not mean the company can freely inspect all employee data.
- Italian labour-law limits and employee-monitoring rules are central in corporate investigations.
- The TechMed case combines phishing, malware, C2 exfiltration, BEC fraud, GDPR breach analysis, and criminal-law reasoning.
- RAM is collected first because it is volatile; disk, firewall logs, and email logs follow.
- Firewall volumes help infer likely exfiltrated content.
- The case requires both technical forensic reconstruction and legal analysis.
- Organisational controls such as SPF, DKIM, DMARC, EDR, anti-phishing training, and payment verification are part of the remediation analysis.
