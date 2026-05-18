# Lecture 19 – The 10 Rules for a Digital Forensic Report
**Professor:** Vaciago
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Vaciago/5_Rules_Digital_Forensics.pdf`

---

## Overview
This lecture is a lab-oriented legal session on how to write a forensic expert report that can survive adversarial scrutiny. Vaciago distinguishes ordinary technical reports from forensic expert reports and explains that the latter become evidence in legal proceedings.

---

## 1. Technical Report vs Forensic Expert Report

> 📎 *Slide reference: `5_Rules_Digital_Forensics.pdf` — Why a forensic report is different*

A technical report is normally written for peers, can assume shared context, and may be revised iteratively. A forensic expert report must stand alone in court.

A forensic report must be:
- **verifiable**, with every assertion traceable to objective data;
- **replicable**, so another expert can reproduce the same results;
- **cross-examination proof**, with logic strong enough to survive hostile questioning.

---

## 2. Scope, Constraints, and Replicability

The first rules concern the foundations of credibility.

| Rule | Practical Meaning |
|------|-------------------|
| **Define the scope** | State what was analysed, what was excluded, and why. |
| **Declare limitations** | Do not hide missing, encrypted, overwritten, or unavailable data. |
| **Guarantee replicability** | Analyse forensic copies, document each step, and provide verifiable results. |

Vaciago stresses that admitting limits strengthens credibility. Hidden limitations become powerful attack points for the opposing party.

---

## 3. Chain of Custody and Evidence Identification

> 📎 *Slide reference: `5_Rules_Digital_Forensics.pdf` — Chain of custody and evidence items*

The report must document seizure, acquisition, storage, analysis, and court presentation. Every evidence item must be uniquely identified through serial numbers, hashes, image format, acquisition timestamps, and examiner identity.

Even clerical errors in hash values or serial numbers can create serious procedural problems, because the court may no longer be able to link the analysed item to the seized item.

---

## 4. Tools, Methodology, and Transparency

A report must declare:
- software names;
- exact versions;
- configuration parameters;
- custom scripts;
- keyword searches;
- non-default settings.

This matters because tool output can vary across versions and configurations. The expert must be prepared to explain tool validation and known limitations.

---

## 5. Facts, Interpretations, Timelines, and Probability

Vaciago emphasises a strict separation:

| Layer | Example |
|-------|---------|
| **Raw fact** | A timestamp is present in a log or MFT record. |
| **Analysis** | The timestamp is correlated with other artifacts. |
| **Conclusion** | The activity is consistent with a specific user action. |

The report should build a coherent timeline and use calibrated language such as "consistent with", "likely", "probable", or "cannot be excluded" rather than unsupported certainty.

---

## 6. Writing for the Judge

The ultimate audience is not the forensic expert community but the judge. A good report uses a clear structure, a readable executive summary, a glossary for technical terms, and accessible language.

The lab then asks students to apply these rules to a digital alibi scenario inspired by the Garlasco case, with one side defending the alibi and the other challenging it as artificial.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Forensic Expert Report** | A technical-legal document that becomes evidence and must be verifiable, replicable, and defensible. |
| **Scope** | The precise boundary of what the expert analysed and did not analyse. |
| **Replicability** | The ability of another qualified expert to repeat the procedure and obtain the same result. |
| **Probabilistic Language** | Carefully calibrated language expressing the strength of a forensic conclusion without overstating certainty. |

---

## Summary
- A forensic expert report is evidence, not just a technical document.
- Scope and exclusions must be explicit from the beginning.
- Limitations should be admitted and explained, not hidden.
- Chain of custody and unique evidence identification are essential.
- Tools, versions, and parameters must be declared.
- Facts must be separated from interpretation and conclusions.
- Timelines should combine technical and real-world events.
- Reports must be understandable to judges and robust under cross-examination.
