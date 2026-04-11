# Lecture 17 – Advanced Metadata and File System Structures
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/09_FS_forensics.pdf`

---

## Overview
This lecture extends file system forensics into metadata, partitioning, and FAT internals. It highlights how EXIF data, magic numbers, MBR/GPT structures, and FAT allocation logic can all provide evidence or reveal attempts to conceal data.

---

## 1. Advanced Metadata Analysis

### 1.1 EXIF Correlation and Integrity
Metadata is often handled differently by various communication layers:
- **Preservation:** Email clients usually preserve original metadata (EXIF).
- **Destruction/Stripping:** Social media and messaging apps (WhatsApp, Instagram, Telegram) strip or modify EXIF to protect privacy or save bandwidth.
- **Forensic Value:** Finding original EXIF (GPS, Altitude, Speed) can uniquely situate a suspect in 3D space during a crime.

### 1.2 Magic Numbers and File Integrity
- **Extension Spoofing:** Changing `.exe` to `.txt` is a common tactic to hide malware.
- **The "Magic Number" Defense:** Forensic tools ignore the extension and check the first few bytes (e.g., `89 50 4E 47` for a PNG). 
- **Caution:** A sophisticated attacker can manipulate magic numbers for specific payloads, though this often prevents the file from opening normally.

---

## 2. Partitioning Standards: MBR vs. GPT

### 2.1 Master Boot Record (MBR)
- **Sector Zero:** The first 512 bytes contain the boot code and partition table.
- **Limits:** Max 4 primary partitions and 2TB capacity limit.
- **Fragility:** If sector zero is corrupted, the entire disk's logical structure is lost.

### 2.2 GUID Partition Table (GPT)
- **Modern Standard:** Part of the UEFI specification.
- **Redundancy:** GPT mirrors the partition header (LBA 1 and the last sector of the disk). If the primary header fails, the system auto-restores from the backup.
- **Integrity:** Uses CRC32 checksums to detect and reject corrupted headers.
- **Compatibility:** Includes a "Protective MBR" in sector zero so legacy tools don't assume the disk is empty and overwrite it.

---

## 3. The FAT File System (Deep Dive)

### 3.1 Allocation Logic
FAT (File Allocation Table) uses a **Linked List** metaphor.
1.  **Directory Entry:** Contains the file name, basic attributes, and a pointer to the **First Cluster**.
2.  **The Table:** The FAT table contains a value for every cluster on the disk. Each entry tells you where the "Next Cluster" is.
3.  **The Chain:** The OS follows this chain (e.g., Cluster 29 → 30 → 33) until it hits an **EOF (End of File)** marker.

### 3.2 Forensic Deletion
- **Process:** When a file is deleted in FAT, the OS simply marks the clusters as "available" in the table and changes the first character of the filename to a special hex value.
- **Data Persistence:** The actual bytes on the disk (the clusters) are **not erased**. They remain until a new file overwrites them.
- **Recovery:** Forensic tools can "relink" these chains to recover deleted documents.

---

## 4. Practical Lab Preparation
- **Groups:** 4–6 members.
- **Deliverables:** Two reports for each lab. A draft at the end of the 3-hour session and a finalized, "more sophisticated" version a week later.
- **Evaluation:** Includes self-evaluation of contribution across dimensions (tool usage, creativity, reporting).

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Protective MBR** | A placeholder MBR at the start of a GPT disk to prevent legacy partitioning tools from seeing the disk as empty. |
| **FAT Linked List** | The structural method of the FAT file system where each table entry points to the successor cluster. |
| **CRC32** | Cyclic Redundancy Check; a checksum algorithm used by GPT to ensure the partition table has not been altered or corrupted. |
| **Cluster** | The smallest logical unit of space that can be allocated to hold a file in the data area of a volume. |

---

## Summary
- EXIF metadata is a primary source for spatial/temporal attribution, but investigators must know which apps strip it.
- GPT is significantly more robust than MBR due to header mirroring and CRC checksums.
- Magic numbers are the primary way forensic tools identify file types, regardless of user-defined extensions.
- In FAT, deletion is a metadata-only event; file contents remain in "unallocated space" until new data is written over them.
- Forensic imaging must be bit-by-bit to preserve the "slack space" and fragmented chains in filesystems like FAT.
- Multi-source correlation (e.g., matching FS timestamps with Application XML timestamps) is essential to detect timestamp manipulation.
