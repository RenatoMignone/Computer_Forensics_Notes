# Chapter 5 – The 10 Rules for a Perfect Digital Forensic Report
**Professor:** Vaciago
**Reference Slides:** [`Slides/Vaciago/5_Rules_Digital_Forensics.pdf`](Slides/Vaciago/5_Rules_Digital_Forensics.pdf)
**Covered in Lectures:** [Lecture 20](Lectures_MD/Lecture_20_Vaciago.md), [Lecture 23](Lectures_MD/Lecture_23_Vaciago.md)

---

## Introduction

The forensic expert report is not merely a technical document. It enters legal proceedings as evidence and must therefore be verifiable, replicable, understandable, and resistant to cross-examination.

---

## 1. Scope, Limits, and Replicability

The first rules establish the report's boundaries:
- define what was analysed;
- define what was not analysed;
- explain the rationale for exclusions;
- state constraints and limitations;
- document a procedure another expert can reproduce.

Limitations should be declared directly. Vaciago presents transparency as a credibility tool, not a weakness.

---

## 2. Evidence Integrity

The report must manage chain of custody and uniquely identify every evidence item.

Required elements include serial numbers, cryptographic hashes, image format, tool details, acquisition timestamps, examiner identity, and storage/transfer records.

---

## 3. Methodology and Interpretation

Experts must declare tools, versions, configurations, and parameters. They must also separate:
- raw facts;
- technical analysis;
- interpretive conclusions.

Timelines should correlate technical and real-world events, identify gaps, and document time-zone normalisation.

---

## 4. Communication

The report must be written for the judge. It should use:
- an executive summary;
- clear section structure;
- short definitions;
- a glossary where needed;
- probabilistic language rather than unsupported certainty.

The lab presentations reinforced this: good forensic reports begin with the thesis and then connect each item of evidence to that thesis.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Cross-Examination Proof** | Capable of surviving adversarial legal questioning. |
| **Evidence Item Registry** | Formal mapping of items to identifiers, hashes, and acquisition details. |
| **Probabilistic Language** | Language calibrated to evidentiary confidence, such as "consistent with" or "probable". |
| **Executive Summary** | Initial non-technical summary of thesis, evidence, and conclusions. |

---

## Summary
- Forensic reports are evidence and must stand alone.
- Scope and exclusions prevent later procedural attacks.
- Constraints strengthen credibility when explained honestly.
- Replicability requires forensic copies, documented steps, and verifiable results.
- Chain of custody links the seized item to the analysed evidence.
- Tool versions and parameters are part of the evidentiary foundation.
- Clear timelines and probabilistic conclusions are essential.
- The judge is the final audience.
