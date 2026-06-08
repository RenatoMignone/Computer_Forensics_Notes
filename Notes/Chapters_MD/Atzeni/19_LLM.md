# Chapter 19 – Digital Forensics and Generative AI
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/19_LLM.pdf`](../../Slides/Atzeni/19_LLM.pdf)  
**Covered in Lectures:** [Lecture 33](../../Lectures_MD/Lecture_33_Atzeni.md)

---

## Introduction

This chapter summarizes Atzeni's final discussion on large language models in digital investigations. LLMs can help with triage, search, summarization, automation, and report drafting, but their probabilistic nature creates serious forensic risks.

The central lesson is that LLMs may generate investigative leads, but they cannot replace repeatable, explainable forensic analysis.

---

## 1. Large Language Models

> 📎 *Slide reference: `19_LLM.pdf` — Large Language Models*

LLMs are advanced AI systems designed to process and generate language-like output. They rely on neural networks with many parameters, trained on extensive datasets, often using transformer architectures and self-attention mechanisms.

Atzeni introduces them only to the extent needed for forensic reasoning: their strength is processing large bodies of text and context; their weakness is that they generate probable outputs rather than deterministic truth.

---

## 2. Possible Investigative Uses

> 📎 *Slide reference: `19_LLM.pdf` — Using LLMs in investigative processes*

LLMs may support:
- analysis of textual and visual data;
- parsing large volumes of unstructured or semi-structured logs;
- suspicious-activity flagging;
- organization of evidence during collection;
- script generation for acquisition and preservation workflows;
- contextual keyword search;
- connecting related evidence across large datasets;
- retrieval-augmented generation over evidence corpora;
- drafting summaries, evidence analyses, and reports.

These uses may improve speed and coverage, especially where human review would be slow.

---

## 3. Reliability and Adversarial Robustness

LLMs may be vulnerable to adversarial conditions. Attackers may change file extensions, embed data through steganography, or craft perturbations that confuse AI classifiers.

For forensic use, the model must be tested against adversarial robustness. A defence attorney can challenge AI-assisted findings if the system is vulnerable to simple manipulation.

---

## 4. Repeatability

> 📎 *Slide reference: `19_LLM.pdf` — Risks using LLMs*

Digital forensics requires repeatability and determinism. LLMs and agentic frameworks are probabilistic, so the same prompt may produce different answers or execution traces.

This is a central admissibility problem. If a result cannot be reproduced and explained, it is weak as evidence.

---

## 5. Recoverability and Semantic Carving

Atzeni distinguishes traditional data carving from **semantic carving**. Traditional tools search for file signatures, headers, footers, and file structures. LLM-style reconstruction may stitch fragments together based on linguistic or contextual plausibility.

Even if the output is coherent, it may be wrong. A plausible reconstruction is not the same thing as recovered evidence.

---

## 6. Scalability and RAG Limits

Forensic datasets may include terabytes of logs, registry hives, captures, and file systems. Retrieval-augmented generation can lose rare but important events during chunking.

Atzeni suggests that hybrid approaches may be required, combining rule-based security tools such as SIEMs or YARA with knowledge graphs and LLM summaries.

---

## 7. Training Data, Confidentiality, and Legal Viability

General-purpose models may be biased or inaccurate for forensic contexts because they are not trained on domain-specific evidence. Fine-tuning would require forensic logs, legal documents, and cybercrime case studies, but real forensic data is often confidential.

A major warning is evidence leakage. Pasting logs or compromised-system data into a commercial model can expose confidential evidence, create privacy violations, and give the defence a strong admissibility challenge.

For sensitive work, Atzeni frames local and controlled models as more viable. Even then, they should be used as lead generators rather than expert witnesses.

---

## 8. Black-Box Admissibility

The **black-box admissibility problem** arises because AI-generated outputs may be false, misleading, or impossible to attribute clearly. Accountability becomes complex when AI-generated insights influence investigative decisions.

Legal and ethical standards must require transparency, oversight, and human responsibility.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **LLM** | Large language model, a probabilistic AI system for language-like processing and generation. |
| **RAG** | Retrieval-augmented generation, combining model output with retrieved external evidence. |
| **Semantic Carving** | Reconstruction based on contextual plausibility rather than physical file-structure recovery. |
| **Adversarial Robustness** | Ability to resist intentionally crafted inputs that mislead the model. |
| **Black-Box Admissibility Problem** | Legal problem created when a model's internal reasoning cannot be fully explained or reproduced. |
| **Lead Generator** | Tool that suggests investigative directions without being treated as decisive evidence. |

---

## Summary
- LLMs can support triage, log analysis, evidence organization, search, summaries, and reports.
- Their outputs are probabilistic and may not be repeatable.
- Adversarial manipulation can undermine AI-assisted findings.
- Semantic carving may produce plausible but false reconstructions.
- RAG can miss rare but critical events in large forensic datasets.
- Confidential evidence must not be sent to uncontrolled commercial models.
- LLMs are safest when treated as investigative lead generators, not expert witnesses.
