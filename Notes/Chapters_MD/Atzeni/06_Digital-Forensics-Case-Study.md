# Chapter 6 – Digital Forensics Case Study: Insider IP Exfiltration
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/06_Digital-Forensics-Case-Study.pdf`](../../Slides/Atzeni/06_Digital-Forensics-Case-Study.pdf)  
**Covered in Lectures:** [Lecture 5](../../Lectures_MD/Lecture_05_Atzeni.md), [Lecture 8](../../Lectures_MD/Lecture_08_Atzeni.md)

---

## Introduction

This chapter summarizes the case-study exercise introduced in Lecture 5 and debriefed in Lecture 8. The scenario concerns a suspected insider exfiltration at **Shockwave Analytics**, after a competitor, **Basal Core System**, announced a product with strong similarities to Shockwave's **Project Triton** machine-learning engine.

The case is used to apply the forensic investigation questions and to show how a timeline can be reconstructed by correlating file-system traces, prefetch artifacts, browser history, USB activity, firewall logs, and other logs discussed during the lecture.

---

## 1. Scenario

| Element | Transcript-supported detail |
|---------|-----------------------------|
| **Victim organisation** | Shockwave Analytics, a company working on predictive threat-detection tools for the finance sector. |
| **Central asset** | Project Triton, a machine-learning engine treated as a relevant competitive advantage. |
| **Triggering event** | Basal Core System announced a product with similarities considered too strong to be simple coincidence. |
| **Main suspect** | John Matthews, a senior software engineer identified by the internal review as a relevant suspect. |

The exercise asks students to reason from evidence rather than from a single predetermined theory. During the debrief, Atzeni explicitly noted that some student hypotheses involved a larger role for Basal Core, but the timeline presented in class supported John acting alone.

---

## 2. Relevant Evidence Sources

The lecture mentions or relies on several classes of evidence:

| Evidence source | Forensic role in the case |
|-----------------|---------------------------|
| **File server / laptop artifacts** | Used to reconstruct operations on Project Triton and the creation of a staging folder. |
| **Windows Prefetch** | Shows execution of tools even after those tools are removed. |
| **NTFS Master File Table / file-system traces** | Supports reconstruction of file operations, archive creation, and deleted artifacts. |
| **Windows Registry** | Contains traces of operations and connected devices. |
| **USB traces** | Show insertion and use of a large pen drive. |
| **Browser history** | Shows searches related to job opportunities, exfiltration, large Gmail attachments, and deletion of traces. |
| **Firewall logs** | Show an unusual large outbound transfer after midnight. |
| **Other logs** | Used to rule out malware, strange IP connections, and compromise by another agent. |

---

## 3. Windows Prefetch Files

Atzeni paused on Windows Prefetch because not everyone knew it well.

Prefetch files are useful because they can record that an executable was run and may persist even after the executable itself has been removed. In this case, prefetch artifacts help show tool execution and support the timeline of archive creation and attempted trace deletion.

Forensic value discussed in the lecture:
- execution of specific programs;
- timestamps useful for timeline reconstruction;
- possible evidence that a program was run from an external drive;
- persistence of traces after attempted deletion.

---

## 4. Timeline Reconstruction

### 4.1 Pre-Exfiltration Context

| Event | Interpretation |
|-------|----------------|
| John searches for better work opportunities and income. | Establishes a possible motive and context for the later actions. |
| Students discuss whether Basal Core may have had deeper involvement. | Atzeni's reconstruction does not support this broader hypothesis. |

### 4.2 Testing and Preparation

| Event | Interpretation |
|-------|----------------|
| A first test attempt occurs around 10 March. | Traces show insertion of a reasonably large pen drive and operations on Project Triton. |
| A folder related to the operation is created. | The folder itself becomes a forensic artifact. |
| Archive tooling is used. | Prefetch, MFT, and registry traces support the interpretation that John compressed and encrypted Project Triton data before exfiltration. |

### 4.3 Exfiltration and Anti-Forensics

| Event | Interpretation |
|-------|----------------|
| Archive copied to USB. | One exfiltration channel. |
| Archive sent through personal Gmail. | Second exfiltration channel; Atzeni interprets this as redundancy from John's perspective. |
| Firewall detects a large encrypted transfer shortly after midnight. | The content may be encrypted, but the volume and timing remain suspicious. |
| `eraser.exe` is run after searches about deleting traces. | Attempted anti-forensics; the attempt itself becomes evidence of awareness and intent. |

---

## 5. Investigative Conclusions

| Question | Conclusion from the lecture reconstruction |
|----------|--------------------------------------------|
| **Who** | John Matthews. The artifacts point to his user profile. |
| **Where** | Atzeni's reconstruction places the relevant activity in the company environment, with no support for a remote proxy or outside actor. |
| **When** | Around the final work period, with a relevant two-day window and preparatory actions before exfiltration. |
| **How** | Project Triton data was staged, compressed/encrypted, copied through USB, and also sent through Gmail. |
| **Why** | Atzeni interprets the actions as linked to personal benefit, job/income motivation, and a move toward a competitor. |

The lecture also explicitly rules out several alternative explanations based on the presented logs:
- no evidence of malware action;
- no strange command-and-control connection;
- no signs that another agent used John as a proxy;
- no log evidence supporting direct Basal Core involvement in the exfiltration.

---

## 6. Presentation and Reporting Lessons

The case connects back to the general reporting principle introduced in Lecture 5: a forensic report must be adapted to its audience while preserving technical correctness.

Atzeni stresses that the investigator should be ready to handle alternative explanations. For example, John might claim that the archive was made for backup or for the organization's interest. The forensic narrative must therefore connect artifacts, timing, and intent carefully rather than merely listing technical traces.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Insider threat** | A risk or incident involving someone inside the organization or with legitimate access. |
| **Project Triton** | The Shockwave Analytics machine-learning project at the center of the case scenario. |
| **Prefetch file** | Windows artifact that can record program execution and remain useful even after the executable has been removed. |
| **MFT** | NTFS Master File Table; relevant because it can preserve traces of file operations. |
| **Staging folder** | A folder used to collect target data before compression or transfer. |
| **Anti-forensics** | Attempts to hide, erase, or confuse traces; in this case, the use of `eraser.exe` is treated as an unsuccessful attempt. |

---

## Summary

- The case-study scenario involves Shockwave Analytics, Project Triton, Basal Core System, and the suspect John Matthews.
- The lecture reconstruction is based on timeline correlation across multiple artifacts and logs.
- Prefetch, MFT traces, registry traces, browser history, USB traces, firewall logs, and other logs are used together rather than in isolation.
- Atzeni's reconstruction supports John acting alone and rules out malware compromise, proxy use, and direct Basal Core involvement based on the available logs.
- The attempted deletion of traces does not erase the case; instead, it strengthens the interpretation that John knew the action was improper.
