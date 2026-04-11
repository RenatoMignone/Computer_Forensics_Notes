# Chapter 9 – Fundamentals of File System Forensics
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/09_FS_forensics.pdf`](Slides/Atzeni/09_FS_forensics.pdf)  
**Covered in Lectures:** [Lecture 15](Lectures_MD/Lecture_15_Atzeni.md), [Lecture 17](Lectures_MD/Lecture_17_Atzeni.md)

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
- **Limits:** Max 4 primary partitions and a 2TB capacity limit.
- **Fragility:** If sector zero is physically or logically damaged, the OS cannot identify any partition structure.

### 3.2 GUID Partition Table (GPT)
Part of the modern UEFI standard, designed for reliability and scale.
- **Redundancy:** GPT mirrors its header at both the beginning (LBA 1) and the end of the disk. If the primary header is corrupted, the system restores it from the backup.
- **Integrity (CRC32):** Every header includes a Cyclic Redundancy Check to detect tampering or hardware errors.
- **Scalability:** Supports up to 128 partitions and disks larger than 2TB.
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

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Mount Point** | A directory in the host file system where a new file system is attached. |
| **Abstraction Layer** | The software (Operating System) that translates high-level file requests into low-level hardware commands. |
| **Block Dev** | A Linux command-line utility used to call block device ioctls, such as setting a device to read-only. |
| **Journaling** | A file system feature that logs changes before they are committed, used to prevent corruption after a crash. |

---

> 📓 *Related Chapters:*
> - [08_tools_and_labs.md](08_tools_and_labs.md) — The environment where these file system actions take place.
> - [04_Write-Blocker-Tools.md](04_Write-Blocker-Tools.md) — The physical defense against accidental writes during mounting.
