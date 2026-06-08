# Chapter 18 – Autopsy
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/18_autopsy.pdf`](../../Slides/Atzeni/18_autopsy.pdf)  
**Covered in Lectures:** [Lecture 33](../../Lectures_MD/Lecture_33_Atzeni.md)

---

## Introduction

Autopsy is presented as an open-source digital-forensics platform that integrates many analysis functions through a graphical interface. It is especially useful didactically because it shows the steps of an investigation from case creation to reporting, even though performance and reliability can limit its use in large real cases.

---

## 1. Platform Overview

> 📎 *Slide reference: `18_autopsy.pdf` — Autopsy overview*

Autopsy is:
- open source;
- multiplatform;
- multi-user;
- extensible through plugins;
- built around many open-source tools.

Many underlying operations are performed by **The Sleuth Kit**, which remains central to file-system and evidence-analysis operations.

---

## 2. Workflow

> 📎 *Slide reference: `18_autopsy.pdf` — Autopsy workflow*

The workflow includes:
- creating a case;
- recording case name and investigator metadata;
- selecting data sources such as files, hard-disk images, or virtual-machine images;
- importing data;
- running analysis modules;
- viewing text, images, metadata, and analytics;
- generating reports in formats such as HTML or XML.

Atzeni notes that analysis can take days on large data sources. Investigators may therefore choose specific modules first, then run additional analysis based on early results.

---

## 3. Import and Prioritization

Autopsy supports many file systems, including NTFS, FAT, Ext-family file systems, and ISO9660. It can provide partial results as they become available.

Prioritization matters. An investigator may choose to process user folders first or run keyword search before more expensive modules.

---

## 4. Default Modules

Autopsy modules include:
- recent activity extraction;
- hash calculation and lookup;
- file-type identification;
- extension mismatch detection;
- embedded file extraction;
- EXIF parsing;
- keyword and regular-expression search;
- email parsing;
- encryption detection;
- interesting-file identification;
- correlation engine;
- PhotoRec carving;
- virtual-machine extraction;
- data-source integrity verification;
- Android analysis.

These modules help surface candidate evidence and inconsistencies for the human examiner.

---

## 5. NSRL

> 📎 *Slide reference: `18_autopsy.pdf` — NIST NSRL*

The **National Software Reference Library** is a NIST initiative that collects reference data about known software. Its reference datasets include digital signatures of known applications and files.

Autopsy can use known-file hashes to reduce the analysis burden. If a file matches a known legitimate application component, the examiner can often deprioritize it and focus on unknown or case-relevant material.

---

## 6. Timeline

> 📎 *Slide reference: `18_autopsy.pdf` — Timeline*

Autopsy can build timelines from files, web artifacts, EXIF/GPS metadata, and other sources. Atzeni treats the timeline as a central output of forensic work.

The visual timeline helps compare events, but the final evidentiary timeline still requires human explanation: why each event is included, what timestamp it uses, and how conflicts were resolved.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Autopsy** | Open-source digital-forensics platform integrating multiple analysis modules. |
| **The Sleuth Kit** | Forensic toolkit used by Autopsy for many underlying operations. |
| **Ingest Module** | Autopsy module that processes data sources to extract or classify evidence. |
| **NSRL** | NIST National Software Reference Library, a hash and metadata dataset for known software. |
| **Extension Mismatch** | Difference between a file's extension and its internal signature or magic bytes. |
| **Timeline** | Chronological reconstruction of events from multiple artifacts. |

---

## Summary
- Autopsy integrates acquisition, analysis, viewing, and reporting functions.
- It is strong as a didactic platform, though not always ideal for large real cases.
- The workflow begins with case creation and data-source selection.
- Modules support hashes, keywords, file typing, email parsing, carving, VM extraction, and Android artifacts.
- NSRL known-file filtering reduces the amount of material needing manual review.
- Timeline reconstruction remains one of the central outputs of forensic analysis.
