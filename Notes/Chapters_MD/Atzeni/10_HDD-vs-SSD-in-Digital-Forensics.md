# Chapter 10 – HDD vs SSD in Digital Forensics
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/10_HDD-vs-SSD-in-Digital-Forensics.pdf`](../../Slides/Atzeni/10_HDD-vs-SSD-in-Digital-Forensics.pdf)
**Covered in Lectures:** [Lecture 20](../../Lectures_MD/Lecture_20_Atzeni.md), [Lecture 21](../../Lectures_MD/Lecture_21_Atzeni.md)

---

## Introduction

SSD forensics changes the assumptions built around magnetic disks. In HDDs, logical block addresses map to stable physical locations; in SSDs, the controller continuously remaps data through firmware mechanisms invisible to the operating system.

---

## 1. Architectural Principles

> 📎 *Slide reference: `10_HDD-vs-SSD-in-Digital-Forensics.pdf` — Architectural principles*

An **HDD** has stable physical addressing: a given logical block generally corresponds to a persistent platter location until the OS overwrites it.

An **SSD** uses a **Flash Translation Layer (FTL)**. The FTL maps logical addresses to NAND cells and may move data internally for performance and durability, breaking the classic relationship between file system address and physical evidence location.

---

## 2. TRIM, Garbage Collection, and Wear Levelling

| Mechanism | Forensic Impact |
|-----------|-----------------|
| **TRIM** | Tells the SSD that logical blocks are no longer needed; deleted data may become inaccessible almost immediately. |
| **Garbage Collection** | Controller-level background process that reorganises and erases NAND blocks independently of host commands. |
| **Wear Levelling** | Spreads writes across cells to avoid premature failure, moving data without OS-level visibility. |

Write blockers cannot stop internal controller processes. They protect against host writes, but not against firmware-level activity.

---

## 3. Logical Hash Stability vs Physical Flux

Hashing remains useful, but only at the logical layer. The OS-visible content may hash consistently even if the physical NAND locations change underneath.

This distinction matters for courtroom explanation: a matching hash supports logical integrity, not physical immutability.

---

## 4. Deleted Data Recovery

On HDDs, deleted data often remains at the same physical location until overwritten. On SSDs, recovery is highly variable:
- with TRIM enabled, deleted recovery may be effectively zero;
- with TRIM disabled, recovery may be much closer to HDD-like behaviour;
- controller behaviour can make the real erasure time differ from the operating system's deletion request.

---

## 5. Advanced Techniques and Chain of Custody

Advanced acquisition may involve **factory access mode**, **chip-off forensics**, or attempts to inspect **over-provisioning areas**. These techniques are controller-specific, risky, and often ineffective when self-encrypting drives are involved.

Documentation should record the SSD model or manufacturer-specific behaviour, TRIM behaviour, encryption state, and any relevant over-provisioning considerations where possible.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **FTL** | Flash Translation Layer; SSD firmware layer that maps logical addresses to physical NAND cells. |
| **TRIM** | Command indicating that logical blocks no longer contain needed data. |
| **Garbage Collection** | SSD internal process that erases and reorganises flash blocks. |
| **Over-Provisioning** | Extra NAND capacity not exposed to the OS, used for wear management and replacement blocks. |
| **SED** | Self-Encrypting Drive with hardware-level encryption. |

---

## Summary
- HDDs preserve a stable logical-to-physical mapping; SSDs do not.
- The FTL is invisible to the OS and forensic tools using ordinary interfaces.
- TRIM and garbage collection can make deleted data unrecoverable.
- Write blockers remain necessary but insufficient for SSDs.
- Hashes confirm logical consistency, not NAND-level stability.
- Chip-off and factory mode are advanced, risky, and model-dependent.
- Encryption can make SSD evidence destruction nearly instantaneous through crypto-erase.
