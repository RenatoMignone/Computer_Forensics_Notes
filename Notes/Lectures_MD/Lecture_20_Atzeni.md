# Lecture 20 – NTFS, Forensic Copying, and Low-Level Acquisition Tools
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/09_FS_forensics.pdf`

---

## Overview
This lecture extends file system forensics from FAT to NTFS and explains why forensic copying differs from ordinary user-level copying. It also introduces slack space, data carving, sanitisation previews, low-level acquisition commands, hashing, file signatures, and the first SSD-related complications.

---

## 1. Lab Requirements and Reports

The lecture starts with clarifications about lab participation, optional bonus points, group organisation, deadlines, and report submission. The mandatory deliverable is the end-of-lab draft; the refined version is optional but can improve evaluation.

---

## 2. Why NTFS Was Needed

FAT is portable and simple, but it lacks robustness, security, and performance features. NTFS was introduced for business and server scenarios where the file system needed to behave more like a structured database.

> 📎 *Slide reference: `09_FS_forensics.pdf` — Modern file system metadata*

NTFS improves on FAT through:
- richer metadata;
- an attribute-oriented organisation;
- journaling and rollback mechanisms;
- access control support;
- better performance on large volumes and large file sets.

---

## 3. NTFS as a Modern File System Example

Atzeni refers to NTFS as an example of a modern, complex file system whose structures must be understood before analysis. The transcript does not go into a full NTFS field-by-field description, but it stresses the investigative approach:
- understand where the file system stores allocation, logging, and metadata information;
- compare normal OS-visible metadata with lower-level file-system information;
- treat richer metadata as useful evidence, but still subject to manipulation, corruption, and misinterpretation.

The general point is portable beyond NTFS: modern file systems increasingly embed reliability, performance, access-control, and sometimes security mechanisms that affect what evidence remains and how it should be interpreted.

---

## 4. System-Level vs Forensic-Level Views

Atzeni stresses that investigators should compare OS-mediated outputs with direct file system inspection.

System-level examples:
```bash
stat file.txt
Get-Item file.txt
```

Forensic-level examples:
```bash
istat image.dd <inode-or-record>
```

Discrepancies between these views can indicate corruption, manipulation, or anti-forensic behaviour.

---

## 5. Forensic Copying and Hashing

An ordinary copy preserves the payload but not necessarily original metadata. A forensic acquisition must preserve all bytes and allow later verification.

> 📎 *Slide reference: `09_FS_forensics.pdf` — Forensic imaging and bitstream copies*

The core command pattern is:
```bash
dd if=/dev/sda of=image.dd
```

Variants such as `dc3dd` and `dcfldd` add useful forensic features, especially hashing during acquisition. Performing acquisition and hashing together is more defensible because it reduces the gap between copying and integrity verification.

---

## 6. File Signatures and Data Carving

Investigators should not rely only on file extensions. **Magic numbers** and file signatures reveal actual file type.

Deleted or hidden files can be recovered by scanning the raw device for known headers and reconstructing the content. Atzeni connects this to the practice of searching not-in-use areas for signatures of previous data.

---

## 7. First SSD Complications

The lecture closes by explaining that SSDs complicate assumptions built around magnetic disks.

Key differences include:
- **Flash Translation Layer (FTL):** a firmware layer translates OS-visible addresses into physical NAND locations, so the operating system does not directly control the real storage position.
- **Wear levelling:** the controller may move data to distribute cell usage, even when the OS-level file appears unchanged.
- **TRIM and garbage collection:** after deletion, the controller may make data unavailable quickly, and some activity may continue after power-off.
- **Different TRIM behaviours:** depending on implementation, reads after TRIM may return old content, deterministic values, or zeros rather than the real physical content.
- **Write-blocker limits:** a write blocker cannot bypass the SSD controller, so it may not guarantee stability of SSD contents in the same way as with magnetic disks.
- **Hashing still matters:** the firmware mapping should still return consistent logical content for allocated data, so hashes remain meaningful for integrity checks.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **NTFS** | Modern Windows file system used here as an example of richer metadata, reliability, and access-control mechanisms. |
| **Bitstream Copy** | A bit-for-bit forensic image of a device or partition. |
| **Magic Number** | Initial byte sequence used to identify a file type independently of its extension. |
| **Slack Space** | Unused bytes inside an allocated storage unit that may preserve remnants of previous data. |
| **FTL** | Flash Translation Layer; SSD firmware mapping between OS-visible addresses and physical NAND cells. |
| **TRIM** | Command informing the SSD controller that certain logical blocks are no longer needed. |

---

## Summary
- NTFS was designed to overcome FAT's lack of robustness, metadata richness, and access control.
- NTFS is used as an example of a modern file system with richer internal structures that require specific investigative understanding.
- Modern file systems may include reliability, rollback, metadata, indexing, access-control, and security mechanisms.
- A forensic copy must preserve the complete byte structure, not only visible file contents.
- `dd`, `dc3dd`, and `dcfldd` support bit-level acquisition workflows.
- File signatures and carving help recover data outside ordinary file system views.
- Slack space and byte-level analysis can reveal remnants that file-system metadata does not expose.
- SSDs introduce firmware-level behaviour that changes classic recovery assumptions, especially around deletion and write blocking.
