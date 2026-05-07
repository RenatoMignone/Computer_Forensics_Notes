# Lecture 18 – File System Forensics: Slack Space and FAT Recovery
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/09_FS_forensics.pdf`

---

## Overview
This lecture continues the file system forensics discussion by moving from the user-visible file abstraction to hidden and residual storage areas. The main focus is how deleted files, metadata, slack space, and FAT structures can preserve evidence even when the operating system no longer presents that evidence to the user.

---

## 1. Lab Organisation and Evaluation

The lecture begins with practical information for the forensic labs. Groups should contain four to six students, submit one report per group, and provide both an end-of-lab draft and, optionally, a more refined version during the following week.

The reports must also include self-evaluation, describing each member's contribution to tool usage, reporting, creativity, and other relevant dimensions.

---

## 2. Hidden Data Below the File Abstraction

Operating systems expose only a simplified **file metaphor**. A forensic examiner must reason about the much larger set of data managed by the device and the file system.

> 📎 *Slide reference: `09_FS_forensics.pdf` — File system metadata and deleted data*

Important sources include:
- **Deleted data**, which may be marked as unavailable by the file system but still physically present.
- **Slack space**, created when the physical allocation unit is larger than the logical file content.
- **Metadata**, produced by the operating system and applications without direct user manipulation.
- **Registry and configuration data**, which reconstruct OS and application state.

---

## 3. Metadata and Low-Level Tools

**Metadata** is data about data. It may describe file creation time, size, permissions, document authorship, EXIF camera information, and many other properties.

Atzeni distinguishes two levels of tooling:
- **System-level tools**, such as `stat`, which query information through the operating system abstraction.
- **Forensic-level tools**, such as `istat` from The Sleuth Kit, which inspect lower-level file system structures directly.

High-level tools such as **Autopsy** can aggregate multiple low-level analyses and help build timelines, but investigators must understand their limitations, performance costs, and possible tool behaviour.

---

## 4. Partitioning and File System Choice

The lecture revisits the relationship between physical storage, partition tables, and file systems.

> 📎 *Slide reference: `09_FS_forensics.pdf` — MBR, GPT, and volume boot records*

| Structure | Forensic Importance |
|-----------|--------------------|
| **MBR** | Historical first-sector structure containing boot code and a partition table; fragile and limited. |
| **GPT** | Modern UEFI partitioning structure with redundancy, CRC checks, and a protective MBR. |
| **Volume Boot Record** | First sector of a partition, containing information about the file system used there. |

The operating system strongly influences the file system used: NTFS for Windows, APFS for macOS, and ext4 commonly for Linux.

---

## 5. FAT as a Didactic File System

FAT remains useful because its simple structure makes forensic principles easy to see.

> 📎 *Slide reference: `09_FS_forensics.pdf` — FAT allocation table*

FAT uses:
- a **volume boot sector**;
- reserved space;
- two copies of the **File Allocation Table**;
- a root directory;
- the data area containing files and subdirectories.

A FAT directory entry stores the file name, attributes, size, and first cluster. The FAT table then acts as a linked list that points from one cluster to the next until the end-of-file marker.

---

## 6. Deletion and Recovery in FAT

In FAT, deletion is mainly a metadata operation. The system marks clusters as available and changes the directory entry, but it does not immediately overwrite the stored bytes.

This makes recovery possible if:
- the clusters have not been overwritten;
- the FAT chain can be reconstructed;
- slack space or unallocated space still contains meaningful fragments.

The lecture uses this as the conceptual basis for understanding direct recovery of data that remains on the device below the operating-system view.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Slack Space** | Unused bytes inside an allocated storage unit that may contain remnants of previous data. |
| **Metadata** | Information about a file or artifact, such as timestamps, permissions, size, or application-level properties. |
| **FAT** | File Allocation Table; a simple file system that stores file cluster chains in a table. |

---

## Summary
- User-visible files are only one layer of storage evidence.
- Deleted files may remain recoverable because file deletion often modifies metadata rather than bytes.
- Slack space can preserve fragments of older files.
- Metadata exists at file system and application level and is central to timeline reconstruction.
- `stat` and `istat` show the difference between OS-mediated and forensic-level inspection.
- FAT is still useful pedagogically because its linked-list allocation model is simple and recoverable.
- MBR and GPT define storage organisation before the file system is even interpreted.
