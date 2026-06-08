# Lecture 29 – Malware-Production Homework Feedback and Professional Digital Forensics
**Professor:** Vaciago  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** N/A

---

## Overview
This lecture is mainly a homework-presentation and feedback session on legal scenarios involving malware production, red-team tools, dual-use cybersecurity products, and corporate liability. Vaciago and Gianluca discuss the students' arguments from a defence perspective, then the lecture continues with professional guidance from Stefano Fattepietro on career paths, open-source digital forensics, and the practical limits of consulting work.

---

## 1. Homework Format and Evaluation Context

Vaciago explains that the session simulates what would normally happen in person: each group presents its case, the lecturers provide legal comments, and the class discusses the strengths and weaknesses of the defence strategy.

The scenario is deliberately legal rather than purely technical. Students are expected to reason about criminal liability, evidence, mens rea, causation, and company procedures, even though they are not law students.

---

## 2. Sentinel Case: Stolen Defensive Tool Used Against a Hospital

The first presentation concerns a company whose proprietary tool, Sentinel, was stolen and later used in an attack against a healthcare entity. The tool was described by the student as a high-criticality dual-use tool capable of simulating malware-like behaviour and, under authorized conditions, altering or destroying digital assets.

The defence argument focuses on the theft of Sentinel and on the absence of involvement by the company in the later attack. Gianluca comments that the simplest defence for **Article 615-ter c.p.** is the broken causal link: if the tool was stolen and used by third parties, there is no evidence that the company itself accessed the victim system.

### Legal Feedback
The lecturers warn that **dual use** has a specific legal meaning in export-control and cyber-tool regulation. It should not be used casually to mean "usable for good and bad purposes."

They also identify a recurring blind spot: students often assume that a cybersecurity company lawfully owns every exploit or malware component it uses. The difficult question is how those tools were developed, purchased, or obtained. If a researcher had to circumvent security measures or buy a zero-day from an unlawful source, the origin of the tool may itself create legal risk.

---

## 3. Company A / Company B: Software Sold to a Bank and Misused

Another group presents a scenario involving a cybersecurity company that sells software to a bank. The software is formally requested for anti-money-laundering, deep-packet inspection, threat modelling, and compliance purposes, but the bank allegedly uses it for insider-trading-related monitoring.

The defence focuses on the contract and on the fact that the vendor was misled by the customer. The key issue is whether the vendor knew or should have known that the tool would be used outside the declared lawful purpose.

---

## 4. Malware Vendor Defence and Article 615-quater

Several presentations deal with companies accused under **Article 615-quater c.p.** because they develop, possess, or distribute tools suitable for accessing protected systems.

The lecturers stress two separate defence questions:
- whether the company was allowed to possess and develop the tool at all;
- whether the tool was used, distributed, or supplied in an unlawful way.

Mixing these questions makes the defence unclear. A company cannot merely say that the tool was not misused if the accusation also challenges the legitimacy of possessing the tool in the first place.

---

## 5. Red-Team Engagement and Out-of-Scope Activity

One presentation concerns a red-team operation for a banking customer. A red teamer allegedly reaches an out-of-scope asset controlled by a third-party provider and deploys a demonstrative payload with malware-like behaviour.

The defence relies on:
- the written **statement of work**;
- excluded assets and rules of engagement;
- the need for written approval before scope changes;
- the company's immediate preservation of logs, payload hashes, and test-machine images;
- the argument that any unauthorized action was an individual deviation, not corporate policy.

The feedback focuses on consistency: the defence must decide whether it is arguing lawful ownership of tools, lawful use of tools, lack of causation for the denial-of-service effect, or absence of corporate liability.

---

## 6. Professional Digital Forensics Discussion

The lecture includes a professional discussion with Stefano Fattepietro, who presents practical observations about working in cybersecurity and digital forensics.

The discussion compares large consulting firms, specialized forensic work, offensive security, market demand, and career development. Fattepietro notes that offensive security attracts more market investment than digital forensics, so tooling and automation may advance faster there, although digital forensics will also be affected by the same technological trends.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Dual Use** | In the lecture feedback, a term with a specific regulatory meaning; it should not be used loosely as a synonym for "usable for good and bad purposes." |
| **Causal Link** | Connection between the defendant's conduct and the harmful event; theft and later misuse by third parties may break this link. |
| **Article 615-ter c.p.** | Italian offence concerning unauthorized access to a protected computer or telecommunication system. |
| **Article 615-quater c.p.** | Italian offence concerning unlawful procurement, possession, diffusion, or delivery of access codes or means suitable for access. |
| **Rules of Engagement** | Contractual and operational limits defining what a red-team or security-testing activity may do. |
| **Mens Rea** | Subjective element required to connect technical conduct to criminal liability. |

---

## Summary
- Lecture 29 is mainly a homework-presentation and feedback session, not a slide-backed doctrinal lecture.
- The lecturers repeatedly distinguish technical capability from criminal responsibility.
- The origin of malware, exploits, and red-team tools matters as much as their later use.
- The term dual use must be used carefully because it has a specific legal-regulatory meaning.
- For Article 615-ter, a stolen tool used by third parties may break the causal link to the original developer.
- For Article 615-quater, possession and unlawful use are distinct defence problems.
- Red-team cases turn on authorization, written scope, rules of engagement, and documentation.
- Professional digital forensics work requires both technical competence and awareness of market, legal, and evidentiary constraints.
