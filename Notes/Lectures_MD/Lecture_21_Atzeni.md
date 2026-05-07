# Lecture 21 – SSD Forensics and Deleted Data Recovery
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/10_HDD-vs-SSD-in-Digital-Forensics.pdf`

---

## Overview
This lecture explains why SSDs change the forensic assumptions developed for magnetic disks. The central issue is that the operating system no longer has direct control over where data physically resides, because SSD firmware mediates access through controller-level mechanisms.

---

## 1. SSD Firmware and Indirection

SSDs introduce a controller layer between the operating system and the physical NAND cells. Atzeni describes this as a compatibility layer that lets operating systems keep using disk-like commands while the SSD internally translates and reorganises data.

> 📎 *Slide reference: `10_HDD-vs-SSD-in-Digital-Forensics.pdf` — HDD vs SSD forensic assumptions*

The same logical address may correspond to different physical cells over time. This breaks the older assumption that a deleted sector remains in one stable physical place until overwritten.

---

## 2. Flash Translation Layer and Wear Levelling

The **Flash Translation Layer (FTL)** maps operating-system requests to real physical cells. The controller also performs **wear levelling**, distributing writes across the SSD so that some cells do not fail much earlier than others.

This means that data can be moved even when the user and operating system did not explicitly rewrite the file. The physical evidence state can therefore change below the normal forensic interface.

---

## 3. TRIM and Garbage Collection

The **TRIM** command tells the SSD that some logical blocks are no longer needed. Depending on the implementation, later reads may return old content, deterministic content, or zeros, even if the physical cells have not yet been erased.

Atzeni distinguishes this from the older HDD model: with SSDs, deleted data recovery can become extremely difficult as soon as TRIM and controller-level cleanup are active.

Garbage collection may also continue the controller's internal work independently from the user's visible actions, and this affects the volatility of SSD evidence.

---

## 4. Write Blockers and Hashing

Traditional write blockers cannot fully freeze an SSD, because the firmware can continue internal operations below the interface protected by the write blocker.

Hashing still remains meaningful at the logical level. Even if physical NAND locations change, the firmware should return the same logical data to the operating system, so a hash can still verify the acquired logical content.

---

## 5. Recovery Limits

Atzeni concludes that SSD deleted-file recovery is highly variable and often very hard when TRIM is enabled. The investigator must understand the specific device behaviour and should not automatically apply HDD recovery assumptions to SSDs.

The key practical point is that storage technology changes the correct forensic procedure: evidence can be more volatile than expected, even after the device is switched off.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **FTL** | Flash Translation Layer; controller mechanism that maps logical addresses to physical NAND cells. |
| **TRIM** | Command informing the SSD that logical blocks are no longer needed. |
| **Wear Levelling** | SSD strategy that distributes writes across cells to prolong device life. |
| **Garbage Collection** | Controller-level cleanup and reorganisation of NAND storage. |
| **Write Blocker Limitation** | A write blocker can prevent host writes but cannot necessarily stop SSD firmware activity. |

---

## Summary
- SSDs use firmware-level indirection that hides physical NAND placement from the operating system.
- Wear levelling may move data even without an explicit host-level rewrite.
- TRIM changes deleted-data recovery assumptions and can make recovery effectively impossible.
- SSD evidence can be volatile in ways closer to memory than to old magnetic disks.
- Write blockers remain useful but cannot guarantee that internal SSD state is frozen.
- Hashes remain meaningful for logical content even if physical placement changes.
