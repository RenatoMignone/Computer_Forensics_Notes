# Chapter 11 – Data Sanitisation Techniques
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/11_Data-Sanitisation-Techniques.pdf`](Slides/Atzeni/11_Data-Sanitisation-Techniques.pdf)
**Covered in Lectures:** [Lecture 22](Lectures_MD/Lecture_22_Vaciago.md)

---

## Introduction

Data sanitisation is the legally and technically sound destruction of recoverable information. The correct method depends on the medium, the required assurance level, and whether the device will be reused, transferred, or destroyed.

---

## 1. NIST Sanitisation Levels

> 📎 *Slide reference: `11_Data-Sanitisation-Techniques.pdf` — Key definitions*

| Level | Meaning |
|-------|---------|
| **Clear** | Logical techniques protecting against simple non-invasive recovery. |
| **Purge** | Stronger techniques protecting against laboratory-grade recovery. |
| **Destroy** | Physical destruction rendering media unusable and unrecoverable. |

---

## 2. Main Techniques

> 📎 *Slide reference: `11_Data-Sanitisation-Techniques.pdf` — Technique comparison by media type*

| Technique | Suitable Media | Notes |
|-----------|----------------|-------|
| **Overwriting** | HDDs, some tapes | A single modern HDD pass may be enough for many NIST cases; SSDs require caution. |
| **Degaussing** | Magnetic HDDs, LTO tapes, floppy disks | Ineffective against SSDs and optical media. |
| **Cryptographic Erasure** | SEDs and encrypted SSDs | Destroys or replaces the DEK. |
| **Physical Destruction** | HDDs, SSDs, optical, mobile | Required when reuse is not permitted. |
| **Firmware Commands** | ATA/NVMe devices | More reliable than OS-level overwriting for modern drives. |
| **Remote Wipe / MDM** | Mobile and managed endpoints | Depends on reachability and command acknowledgement. |

---

## 3. Firmware and NVMe Commands

Some ATA and NVMe devices expose low-level sanitisation mechanisms. Atzeni specifically notes that firmware-level commands are preferable when available because they operate below ordinary file-system writes and are mediated by the controller itself.

Investigators and administrators must verify that the command completed successfully and that the expected sanitisation effect was achieved.

---

## 4. Verification and Audit Trail

Sanitisation is incomplete without verification and documentation. The lecture stresses the use of appropriate procedures, certified tools where required, and checks during or after the sanitisation steps to confirm that writes or erasures succeeded.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **DEK** | Data Encryption Key used to encrypt data at rest. |
| **Crypto-Erase** | Sanitisation by destroying or replacing key material. |
| **Coercivity** | Resistance of magnetic media to demagnetisation, relevant for degaussing. |
| **MDM** | Mobile Device Management system capable of remote administrative actions. |
| **FIPS-approved RNG** | Random generator validated for cryptographic key generation. |

---

## Summary
- Sanitisation must match media type and assurance goal.
- NIST distinguishes Clear, Purge, and Destroy.
- Overwriting is reliable for HDDs but not for SSDs affected by wear levelling.
- Degaussing applies only to magnetic media.
- Crypto-Erase is fast and strong when encryption was correctly implemented.
- Firmware-level ATA/NVMe commands are preferred over ordinary OS writes.
- Verification and audit trails are mandatory for defensibility.
