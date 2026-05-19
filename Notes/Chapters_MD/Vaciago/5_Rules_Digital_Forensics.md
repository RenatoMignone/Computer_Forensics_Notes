# Chapter 5 – The 10 Rules for a Perfect Digital Forensic Report
**Professor:** Vaciago
**Reference Slides:** [`Slides/Vaciago/5_Rules_Digital_Forensics.pdf`](../../Slides/Vaciago/5_Rules_Digital_Forensics.pdf)
**Covered in Lectures:** [Lecture 19](../../Lectures_MD/Lecture_19_Vaciago.md), [Lecture 22](../../Lectures_MD/Lecture_22_Vaciago.md)

---

## Introduction

The forensic expert report is not merely a technical document. It enters legal proceedings as evidence and must therefore be verifiable, replicable, understandable, and resistant to cross-examination.

---

## 1. Define the Scope

The first rule is to state the scope of work: what was analysed, what was not analysed, and why. Vaciago stresses that even apparently obvious exclusions must be written down, because an adversarial party can attack anything left implicit.

The expert must remain inside the mandate. If the question from the court, prosecutor, attorney, or company is badly framed, the correct reaction is to ask for clarification or modification of the mandate, not to silently expand the work.

---

## 2. Declare Constraints and Limitations

Limitations should be admitted directly. They may come from:
- the mandate;
- missing or unavailable data;
- encryption;
- damaged or overwritten data;
- technical impossibility;
- lack of access to some devices or data sets.

Vaciago presents transparency as a credibility tool, not a weakness. If an important limitation is hidden, the judge or counterpart may interpret the omission as dishonesty.

---

## 3. Guarantee Replicability

The report must describe a procedure that another expert can reproduce. This includes working on forensic copies rather than originals, documenting the steps taken, and presenting results in a way that can be verified.

Generative AI may help draft or organise reports, but it does not remove the duty to describe the forensic process precisely and synthetically.

---

## 4. Document the Chain of Custody

The report must explain the path of the evidence through seizure, acquisition, storage, analysis, and presentation in court.

Vaciago notes that a perfect chain of custody is difficult in practice, which is why hashing is central: once an item is hashed, later modifications can be detected. Weaknesses in the chain should be acknowledged and explained instead of hidden.

---

## 5. Identify Every Evidence Item

Each item must be uniquely identifiable. Required elements include serial numbers, cryptographic hash values, image format or container, acquisition timestamps, examiner identity, and storage or transfer records.

Small transcription or copying errors in hashes and identifiers can become decisive in court, so the report must check these values carefully.

---

## 6. Declare Tools and Methodology

Experts must declare software, version numbers, configurations, and parameters. The lecture links this to the historic debate over open-source and closed-source forensic tools: transparency matters because the counterpart may challenge how a tool works.

Closed-source tools may be practically necessary, especially in mobile forensics, but the report should still be as transparent as possible about the methodology used.

---

## 7. Separate Facts, Analysis, and Opinion

The report must distinguish:
- raw facts;
- technical analysis;
- interpretive conclusions.

The final opinion must flow logically from the data and analysis presented. Vaciago warns against starting from facts and then drifting into interpretations that are not actually supported by those facts.

---

## 8. Build a Coherent Timeline

Timelines are one of the most important parts of a forensic report. They should connect real-world events with technical events, identify gaps or conflicts, and make the sequence understandable for the judge.

Vaciago recommends using both a synthetic timeline with the most important events and a detailed timeline for readers who need to follow the full evidentiary path.

---

## 9. Use Probabilistic Language

Digital evidence rarely permits absolute certainty. The expert should use calibrated language such as "consistent with", "probable", or "cannot be excluded" when certainty is not justified.

This is not the same as being vague. The expert should still take a reasoned position, but the strength of the conclusion must match the strength of the evidence.

---

## 10. Write for the Judge

The final audience is the judge, not only other technicians. The report should use clear structure, accessible language, definitions, and a glossary where needed.

The lab presentations reinforced this: good forensic reports begin with the thesis and then connect each item of evidence to that thesis. AI can help rewrite or test clarity, but the human expert must still add judgement, focus, and legal relevance.

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
