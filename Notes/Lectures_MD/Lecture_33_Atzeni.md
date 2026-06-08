# Lecture 33 – Autopsy, Timelines, and LLMs in Digital Forensics
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/18_autopsy.pdf`, `Slides/Atzeni/19_LLM.pdf`

---

## Overview
The final Atzeni lecture introduces Autopsy as a didactic example of an integrated forensic platform and then briefly surveys the possible role of large language models in digital investigations. The lecture stresses both the usefulness of automation and the limits of relying on tools whose output must remain explainable, repeatable, and admissible.

---

## 1. Autopsy as an Integrated Forensic Platform

> 📎 *Slide reference: `18_autopsy.pdf` — Autopsy overview*

Atzeni presents **Autopsy** as an open-source, multiplatform, multi-user digital-forensics platform. It is extensible through plugins and connects many open-source tools through a Java graphical interface.

Many underlying operations are performed by **The Sleuth Kit**, which remains central to Autopsy's file-system and evidence-analysis capabilities.

Atzeni notes an important practical limitation: Autopsy is useful didactically because it shows the steps of an investigation, but in real cases it may be slow, unstable, or unsuitable for very large evidence sets.

---

## 2. Autopsy Workflow

> 📎 *Slide reference: `18_autopsy.pdf` — Autopsy workflow*

The workflow includes:
- creating a case with name and investigator metadata;
- selecting data sources such as files, disk images, or virtual-machine images;
- importing data;
- running ingest modules such as keyword search, hash analysis, or file-type identification;
- using viewers to inspect text, images, metadata, analytics, and other artifacts;
- generating reports.

Because analysis can take days on large evidence sets, investigators may choose which modules to run first and may prioritize folders or data sources.

---

## 3. Autopsy Modules and Correlation

Autopsy supports modules for:
- recent activity extraction;
- hash calculation and lookup;
- file-type identification and extension-mismatch detection;
- embedded file extraction;
- EXIF parsing;
- keyword and regular-expression search;
- email parsing;
- encryption detection through entropy;
- interesting-file identification;
- correlation across cases;
- PhotoRec carving;
- virtual-machine extraction;
- data-source integrity checks;
- Android analysis.

Atzeni emphasizes correlation and inconsistency detection. A forensic tool should help the examiner find candidate anomalies, but the human analyst still has to evaluate whether they are meaningful.

---

## 4. NSRL and Known-File Filtering

> 📎 *Slide reference: `18_autopsy.pdf` — NIST NSRL*

The **National Software Reference Library** is described as a NIST initiative that collects reference hashes for known software. Autopsy can use such datasets to recognize ordinary operating-system or application files and reduce the amount of material an investigator must manually inspect.

This is valuable because a forensic image may contain huge numbers of legitimate files. Filtering known software helps focus analysis on unknown, suspicious, or case-relevant artifacts.

---

## 5. Timeline Reconstruction

> 📎 *Slide reference: `18_autopsy.pdf` — Timeline*

Atzeni returns to a recurring course theme: the timeline is one of the most important final outcomes of a forensic investigation.

Autopsy can gather timestamps from files, web artifacts, EXIF/GPS metadata, and other sources, then present them in a navigable visual timeline. The final timeline still requires explanation and refinement by the investigator, because the report must justify why the reconstruction is sound.

---

## 6. LLMs in Forensic Investigation

> 📎 *Slide reference: `19_LLM.pdf` — LLM use in investigative processes*

The lecture then introduces **large language models** as possible assistants in digital investigations. LLMs may help:
- parse large volumes of unstructured or semi-structured logs;
- flag suspicious activity;
- organize textual or visual evidence;
- generate acquisition or preservation scripts;
- assist keyword search with contextual understanding;
- connect disparate evidence through retrieval-augmented generation;
- draft summaries and reports for different audiences.

Atzeni frames these uses as investigative support, not as a replacement for forensic expertise.

---

## 7. Risks of LLM Use

> 📎 *Slide reference: `19_LLM.pdf` — Risks using LLMs*

The main risks are:
- reliability under anti-forensic or adversarial conditions;
- lack of determinism and repeatability;
- semantic carving that may produce plausible but false reconstructions;
- loss of important rare events during RAG chunking;
- bias or poor performance caused by non-forensic training data;
- inability to replicate investigator intuition;
- cost and resource requirements;
- privacy and confidentiality risks when evidence is sent to external services;
- the black-box admissibility problem.

Atzeni gives a strong warning: pasting logs from a compromised system into a commercial model may create an evidence leak and a legal weakness. In sensitive forensic contexts, only local, controlled, air-gapped or otherwise appropriate models may be viable, and even then they should be framed as lead generators rather than expert witnesses.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Autopsy** | Open-source digital-forensics platform integrating multiple analysis modules and The Sleuth Kit. |
| **The Sleuth Kit** | Underlying open-source toolkit used for many file-system and forensic operations. |
| **NSRL** | NIST National Software Reference Library, a collection of hashes for known software files. |
| **Timeline Reconstruction** | Building a chronological account from file, system, web, metadata, and other timestamps. |
| **LLM** | Large language model, a probabilistic AI system capable of generating and analyzing language-like outputs. |
| **RAG** | Retrieval-augmented generation, combining a model with external evidence or document retrieval. |
| **Semantic Carving** | LLM-style reconstruction based on contextual plausibility rather than physical file-structure recovery. |

---

## Summary
- Autopsy is useful for teaching integrated forensic workflow, but may be limited in large real investigations.
- Its workflow covers case creation, source selection, ingest modules, analysis, and reporting.
- Hash lookup and NSRL filtering reduce the volume of known-good files.
- Timeline reconstruction remains a central forensic outcome.
- LLMs can support triage, search, summarization, workflow automation, and report drafting.
- LLM output is probabilistic and may be challenged for reliability, repeatability, bias, and explainability.
- Sensitive evidence should not be pasted into uncontrolled commercial AI services.
- LLMs are best treated as investigative lead generators, not expert witnesses.
