# Chapter 9 – Fundamentals of File System Forensics
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/09_FS_forensics.pdf`](../../Slides/Atzeni/09_FS_forensics.pdf)  
**Covered in Lectures:** [Lecture 15](../../Lectures_MD/Lecture_15_Atzeni.md), [Lecture 17](../../Lectures_MD/Lecture_17_Atzeni.md), [Lecture 18](../../Lectures_MD/Lecture_18_Atzeni.md), [Lecture 20](../../Lectures_MD/Lecture_20_Atzeni.md)

---

## Introduction

This chapter summarizes the file-system forensics material from Lectures 15, 17, 18, and 20. It focuses on how operating systems abstract storage through files and mount points, why that abstraction can modify evidence, and how investigators use low-level access, read-only protections, forensic images, metadata, and file-system structures to reconstruct user activity.

---

## 1. The File System Hierarchy and Abstraction

Digital forensics relies on understanding the layers between raw bits and user information.
- **The File Metaphor:** An abstraction provided by the operating system to simplify interaction with storage. It hides physical geometry (cylinders, sectors, memory cells).
- **Logical vs. Physical:** A single "File" to a user is a **logical** unit. To the disk, it is a sequence of **physical** blocks.
- **FS Diversity:** Investigators must be familiar with multiple file systems (NTFS, ext4, APFS, FAT32) because each handles metadata, deletion, and "hidden" areas (like Slack Space) differently.

---

## 2. Linux Device Types (`/dev/`)

In Unix-like systems, hardware is abstracted as files. Understanding these nodes is critical for direct (low-level) access.

### 2.1 Block vs. Character Devices
- **Block Devices (`b`):** Support random access and atomic unit operations (blocks). Used for hard drives and SSDs.
- **Character Devices (`c`):** Support continuous streams of data. Used for terminals and serial ports.

### 2.2 Specialized Forensic Nodes
- **/dev/mem & /dev/kmem:** Provide direct access to physical and kernel memory. Essential for **Memory Forensics** and creating RAM snapshots.
- **/dev/loop:** Allows a file (like a forensic image) to be treated as a block device, enabling it to be mounted and explored.
- **/dev/zero & /dev/null:** Used for wiping storage or discarding unwanted output during forensic experiments.

---

## 3. Partitioning Standards: MBR vs. GPT

The organization of partitions on a disk is defined by one of two major standards.

### 3.1 Master Boot Record (MBR)
- **Sector Zero:** The first 512 bytes contain the boot code and the partition table.
- **Limits:** Historically limited to 4 primary partitions and roughly 2TB per partition because of the addressing scheme.
- **Fragility:** If sector zero is physically or logically damaged, the OS cannot identify any partition structure.

### 3.2 GUID Partition Table (GPT)
Part of the modern UEFI standard, designed for reliability and scale.
- **Redundancy:** GPT mirrors its header at both the beginning (LBA 1) and the end of the disk. If the primary header is corrupted, the system restores it from the backup.
- **Integrity (CRC32):** Every header includes a Cyclic Redundancy Check to detect tampering or hardware errors.
- **Scalability:** Removes the historical MBR limit of four primary partitions and supports larger modern disks.
- **Retrocompatibility:** Includes a **Protective MBR** in Sector Zero to prevent legacy tools from seeing the disk as empty and overwriting GPT data.

---


## 4. The FAT File System (Inner Workings)

The File Allocation Table (FAT) is a simple but forensically rich system found in almost all portable storage.

### 4.1 The Linked List Metaphor
FAT organizes data through a system of pointers:
1.  **Directory Entry:** A record containing the filename (8+3 format legacy), attributes, and a pointer to the **First Cluster**.
2.  **FAT Table:** A list where each entry corresponds to a cluster. The entry contains the address of the "Next Cluster" in the file.
3.  **End of Chain:** A special value (EOF) marks the final cluster of a file.

### 4.2 Forensic Deletion in FAT
When a file is "deleted" in FAT:
- The OS changes the first character of the filename in the directory entry to a special hex value (e.g., `0xE5`).
- The clusters in the FAT table are marked as "available."
- **CRITICAL:** The actual data in the clusters is **not modified**. Until a new file overwrites those specific clusters, the data remains intact and recoverable.

---

## 5. The Mounting and Unmounting Process

### 5.1 Mounting for Analysis
Mounting attaches a storage device to a **Mount Point** in the directory tree.
- **Forensic Warning:** Standard mounting can auto-correct minor disk errors or update "Last Mount Time" metadata. This **alters the evidence**.
- **The "ReadOnly" Rule:** 
    - Always use the `-o ro` flag.
    - Use `blockdev --setro` to lock the device at the kernel level.
    - When inspecting untrusted file systems, consider mount options such as `noexec`, `nosuid`, and `nodev` to prevent execution, privilege escalation through setuid bits, or special-device interpretation.
    - Preferred: Use a hardware **Write Blocker**.

### 5.2 Unmounting and Buffering
- **Write-Behind Caching:** OS performance optimizations mean data is often held in RAM buffers before being flashed to disk.
- **Evidence Integrity:** Improper removal (unplugging without unmounting) causes metadata/content inconsistencies, which can be interpreted as corruption or intentional tampering.

---

## 6. Working with Forensic Images

A **Bitstream Copy** (using `dd`) creates a bit-for-bit replica of a storage device.
- **Integrity:** Hashing the original and the image ensures they are identical.
- **Structure preservation:** An image file preserves the exact byte-level location of every file system structure (Master File Table, Journal, Inodes).
- **Loop Mounting:** Using `i-mount` or `mount -o loop`, an investigator can interact with the image as if it were a physical disk, allowing analysis without risking the original media.

---

## 7. File System Metadata

Metadata is "data about data" and is the primary target for timeline reconstruction.

| Metadata Type | Forensic Value |
|---------------|----------------|
| **Filename/Extension** | Mnemonic; easily spoofed (e.g., `virus.exe` renamed to `notes.txt`). |
| **MAC Timestamps** | Modified, Accessed, Created. Reveal the history of file interaction. |
| **Permissions** | Reveal which user accounts had access to specific sensitive files. |
| **Location/Size** | Essential for identifying if a file was moved or truncated. |
| **Magic Numbers** | The first few bytes of a file that define its true type, regardless of extension. |

---

## 8. Slack Space and Data Carving

Slack space is created when the file content is smaller than the allocated physical unit. The unused portion of the sector or cluster may still contain fragments of older data.

Forensic tools can inspect below the user-visible file abstraction and recover evidence from:
- deleted-but-not-overwritten clusters;
- unallocated space;
- slack space;
- file signatures or magic numbers;
- residual application or file system metadata.

Tools such as **Foremost** automate this process by scanning raw bytes for known file patterns and reconstructing recoverable content.

Atzeni also mentions **PhotoRec** as another carving tool. Its advantage is that it can work more directly on the storage device, whereas Foremost is historically used more often on a forensic image supplied as input. In practice, using both can be useful because implementations differ.

---

## 9. NTFS and the Master File Table

NTFS is more robust than FAT because it is organised around an attribute-based model and richer metadata. The lecture uses it as the example of a modern file system where reliability, security, indexing, and recovery structures make analysis more powerful but also more complex.

| NTFS Component | Forensic Value |
|----------------|----------------|
| **Attributes and metadata** | Preserve more information about file state than FAT does. |
| **Indexes and recovery structures** | Improve performance and robustness, but require file-system-specific interpretation. |
| **Access-control metadata** | Can preserve richer permission information than simple portable file systems. |
| **Journaling/recovery data** | Can help reconstruct operations or explain inconsistencies after a crash or improper removal. |

As with other file systems, deletion and copying must be interpreted through the file system's own rules. A normal copy may lose or rewrite metadata, while forensic-level inspection tries to preserve and compare the original metadata.

---

## 10. Application-Level Metadata and Metadata Tools

Metadata is not only stored by the file system. Application formats such as Office/OpenDocument archives and image formats can contain internal metadata. The lecture highlights **ExifTool** as a tool originally associated with EXIF image metadata and now useful for many standardised file types.

Forensic analysis should compare multiple views of the same object:
- system-level tools such as `stat`;
- forensic-level tools such as `istat` from The Sleuth Kit;
- hex-level inspection of file signatures and magic numbers;
- application metadata tools such as `exiftool`.

This is useful because metadata can be wrong, incomplete, or deliberately manipulated. Inconsistencies between the extension, magic number, filesystem metadata, and application metadata are red flags for deeper analysis.

---

## 11. Forensic Copying and System vs Forensic Views

An ordinary file copy does not preserve all metadata. A forensic copy must preserve byte-level structure and be verified through hashes.

Typical tools include:
```bash
dd if=/dev/sda of=image.dd
```

DD-like forensic tools may also compute hashes during the same acquisition step, reducing the gap between copying and integrity verification.

Investigators should compare OS-mediated outputs such as `stat` with forensic-level inspection such as `istat`. Inconsistencies can reveal corruption, manipulation, or anti-forensic activity.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Mount Point** | A directory in the host file system where a new file system is attached. |
| **Abstraction Layer** | The software (Operating System) that translates high-level file requests into low-level hardware commands. |
| **Block Dev** | A Linux command-line utility used to call block device ioctls, such as setting a device to read-only. |
| **Journaling** | A file system feature that logs changes before they are committed, used to prevent corruption after a crash. |
| **Slack Space** | Unused bytes inside an allocated storage unit that may contain remnants of previous data. |
| **MFT** | NTFS Master File Table, the main metadata structure describing files and file system objects. |
| **File Carving** | Recovery technique that scans raw bytes for file signatures and reconstructs files outside normal file system metadata. |

---

## Summary

- File systems hide physical storage complexity behind the file/folder metaphor, but forensic analysis often needs to reason below that abstraction.
- Mounting and unmounting can change metadata, so investigators must use read-only protections, write blockers, and controlled procedures.
- Forensic images preserve byte-level layout and allow analysis away from the original evidence.
- Metadata, magic numbers, slack space, unallocated space, FAT structures, and NTFS MFT records all support timeline reconstruction and recovery.
- Ordinary file copying is not equivalent to forensic copying because it does not preserve the full byte-level and metadata context.

---

> 📓 *Related Chapters:*
> - [08_tools_and_labs.md](08_tools_and_labs.md) — The environment where these file system actions take place.
> - [04_Write-Blocker-Tools.md](04_Write-Blocker-Tools.md) — The physical defense against accidental writes during mounting.
