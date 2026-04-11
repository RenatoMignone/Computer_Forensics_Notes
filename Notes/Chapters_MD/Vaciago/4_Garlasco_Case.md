# Chapter 4 – Case Study: The Garlasco Murder (Digital Evidence)
**Professor:** Vaciago  
**Guest Expert:** Paolo Dal Checco  
**Covered in Lectures:** [Lecture 16](Lectures_MD/Lecture_16_Vaciago.md)

---

## 1. Introduction to the Garlasco Case

The murder of Chiara Poggi in Garlasco (2007) is a quintessential example of the transition from traditional to digital investigative paradigms in Italy. It serves as a warning on how **procedural errors** in the handling of digital evidence can permanently obscure the truth.

---

## 2. The Fragility of the "Digital Alibi"

A digital alibi consists of traces (logs, metadata, activity sessions) that prove a suspect was interacting with a device at a specific time. In this case, the suspect (Alberto Stasi) claimed to be working on his university thesis at the time of the murder.

### 2.1 Technical Errors and Metadata Destruction
The investigation suffered from massive "top-down" incompetence regarding digital evidence:
- **Untrained First Responders:** The local Carabinieri accessed the computer repeatedly (14–29 August) without **Hardware Write Blockers**.
- **The "Saving" Mistake:** Officers opened the thesis document and manually saved it. 
- **Impact:** This action changed the "Last Modified" and "Last Accessed" timestamps. By altering the metadata, they destroyed the technical certainty required to confirm if the suspect was actually typing during the murder window.
- **Probabilistic Reasoning:** Because the original metadata was destroyed, the court had to rely on "Digital Archaeology" (reconstructing evidence from temporary files and degraded artifacts), leading to conflicting technical opinions.

---

## 3. Legal and Procedural Challenges

### 3.1 The 348 vs 359/360 Controversy
A core legal conflict in Garlasco was the classification of forensic activity:
- **Art. 348 CPP:** General discovery/collection by police.
- **Art. 359/360 CPP:** Irrepeatable technical examinations requiring experts.
- **The Error:** The police treated the laptop as a simple "useful element" (348). However, since turning on a computer or browsing files *alters* the evidence (metadata, cache), it should have been treated as an irrepeatable technical act (360). This lead to the landmark "Vitelli Decision," where the judge ordered a super-expert review due to the "intrinsic fragility" of the initial findings.

---

## 4. Advanced Forensics: VMs and Super Timelines

To resolve the inconsistencies, modern experts used:
- **Virtualization:** Creating an exact digital twin of the suspect's computer to test how specific user actions (e.g., clicking 'Save') affected systemic timestamps.
- **Super Timelines:** Using tools like **Plaso** (Log2Timeline) to aggregate file system events with browser history and OS journals. This allowed for a millisecond-level reconstruction of the "Scene of Digital Life."

---

## 5. Professional Ethics for Experts

The case also serves as a study in expert behavior:
- **Verification over Authority:** Experts must not trust tools or colleagues blindly. 
- **The "April Fool's" Lesson:** Paolo Dal Checco's fake "hash converter" showed that even professionals can be fooled by reputable figures. Experts must maintain a radical curiosity and test every step of their process.
- **Interaction with Judges:** Experts must "put themselves in the judge's shoes," explaining complex technicalities (like unallocated sectors or sectors) using simple metaphors (a ledger or a timeline).

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Digital Archaeology** | The process of recovering and reconstructing meaningful data from damaged, degraded, or non-obvious digital sources. |
| **Vitelli Decision** | A judicial ruling emphasizing that when a life is at stake, the court must require the "maximum effort" and a super-expert review if initial evidence collection was sloppy. |
| **Epistemic Damage** | Damage to our ability to "know" the truth caused by the improper handling of evidence (e.g., metadata alteration). |

---

> 📓 *Related Chapters:*
> - [3_Law_48_08.md](3_Law_48_08.md) – The legal framework created partly as a response to errors in cases like Garlasco.
> - [01_IntroCF.md](../Atzeni/01_IntroCF.md) – The basic principles of Chain of Custody that were violated here.
