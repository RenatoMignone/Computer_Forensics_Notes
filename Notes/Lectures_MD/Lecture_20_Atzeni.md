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
- attribute-based file records;
- journaling and rollback mechanisms;
- access control support;
- better performance on large volumes and large file sets.

---

## 3. Master File Table and Attribute Model

The **Master File Table (MFT)** is the central NTFS structure. Each file is represented as a record, typically 1 KB, containing a fixed header and a set of attributes.

| NTFS Element | Forensic Meaning |
|--------------|-----------------|
| **MFT Header** | Contains essential record metadata and validity flags. |
| **Resident Attribute** | Attribute value stored inside the MFT record itself. |
| **Non-Resident Attribute** | Attribute value stored elsewhere, with the MFT pointing to its location. |
| **Bitmap** | Tracks which clusters or records are allocated. |
| **Log File** | Supports transaction recovery and may reveal recent file system activity. |

NTFS deletion marks records and clusters as not in use, but the underlying data may remain recoverable until overwritten.

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
fsutil
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

The lecture closes by previewing that SSDs complicate assumptions built around magnetic disks. Atzeni specifically flags **TRIM** and **wear levelling** as concepts to discuss in the following lecture.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **MFT** | NTFS Master File Table; database-like structure containing records for files and metadata. |
| **Resident Attribute** | NTFS attribute stored directly in the MFT record. |
| **Non-Resident Attribute** | NTFS attribute whose content is stored outside the MFT record. |
| **Bitstream Copy** | A bit-for-bit forensic image of a device or partition. |
| **Magic Number** | Initial byte sequence used to identify a file type independently of its extension. |

---

## Summary
- NTFS was designed to overcome FAT's lack of robustness, metadata richness, and access control.
- The MFT organises file information through headers and attributes.
- NTFS supports rollback and journaling concepts similar to database transaction mechanisms.
- Deletion in NTFS still leaves recoverable traces when data has not been overwritten.
- A forensic copy must preserve the complete byte structure, not only visible file contents.
- `dd`, `dc3dd`, and `dcfldd` support bit-level acquisition workflows.
- File signatures and carving help recover data outside ordinary file system views.
- SSDs introduce firmware-level behaviour that changes classic recovery assumptions.
