# Lecture 15 – Fundamentals of File System Forensics
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/09_FS_forensics.pdf`

---

## Overview
This lecture introduces file system forensics by explaining the file system abstraction, the forensic implications of mounting and unmounting devices, and the main device types seen in Unix/Linux environments. The focus is on understanding how file systems mediate access to evidence and where traces of activity can persist.

---

## 1. The File System Abstraction

Operating systems interact with storage through an **abstraction layer** called the File System.
- **Middleware:** The FS hides the physical complexity (sectors, magnetic fields) and provides a common "File/Folder" metaphor using a set of standard system calls.
- **Diversity:** There is no single FS. Windows uses NTFS; Linux uses ext4, Btrfs, and hundreds of others; macOS uses APFS.
- **Hiding Data:** Different FS architectures provide different ways of "hiding" information (e.g., Slack Space, Alternate Data Streams), which investigators must understand.

---

## 2. Mounting and Unmounting

### 2.1 The Mounting Process
Mounting incorporates a storage device (local disk, USB, or Network FS like NFS/SMB) into the existing directory tree at a **Mount Point**.
- **Forensic Risk:** Standard mounting is NOT just a label. It often involves **checking for errors** and attempting corrections. This can modify metadata (e.g., last mount time, journal entries), which may erase relevant forensic evidence.
- **Investigator Rule:** Ideally, never mount original evidence directly. Use bit-by-bit images or specialized forensic mounting tools.

### 2.2 Unmounting and Buffering
- **Optimization Problems:** To improve performance, OSs use **Write-Behind Caching**. When you "save" a file, it might stay in a RAM buffer for seconds or minutes before being flushed to the disk.
- **Inconsistencies:** Suddenly unplugging a device prevents buffers from flushing, leading to "Inconsistent Integrity" between the actual file content and the metadata describing it.
- **Forensic Trace:** Mount/Unmount events leave traces in the OS (e.g., Windows Registry, Prefetch, Linux dmesg).

---

## 3. Device Types in Unix/Linux

Everything in Unix is a file, represented by nodes in `/dev/`.

| Device Type | Description | Example |
|-------------|-------------|---------|
| **Block Device** | Supports random access; data is handled in atomic blocks (sectors). | Hard Drives, SSDs (`/dev/sda1`) |
| **Character Device** | Provides a continuous stream of data; no random access. | Terminals, pseudo-devices (`/dev/null`) |
| **Network Device** | Mediates packets through a socket abstraction. | WiFi/Ethernet cards (`wlo1`) |
| **Special Devices** | Pseudofiles for system interaction. | `/dev/zero`, `/dev/random`, `/dev/loop` |
| **Memory Devices** | Allow direct access to physical/kernel memory. | `/dev/mem`, `/dev/kmem` |

---

## 4. Forensic Precautions and Interaction

### 4.1 Maintaining Read-Only Status
- **OS-Level Read-Only:** Mounting with the flag `-o ro`.
- **Device-Level Read-Only:** Forcing the block device itself into read-only mode using `blockdev --setro`. This is more secure as it overrides file system write requests.
- **Hardware Write Blockers:** The ultimate forensic standard; physical hardware that prevents any write signal from reaching the storage.

### 4.2 Imaging (Bit-by-Bit Copy)
Using tools like `dd`, an investigator creates a file (e.g., `evidence.dd`) that is an exact replica of the original.
- **Structural Integrity:** Every element (Master File Table, Journals, Indexes) remains at the exact same byte offset in the image as it was on the original disk.
- **Image Mounting:** Specialized tools like `i-mount` or `disk-image-mounter` can "loop-mount" these images, allowing the investigator to explore them as if they were real disks without risking the original media.

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Mounting** | The process of making a file system accessible by attaching it to a specific point in the directory tree. |
| **Write-Behind Cache** | A performance optimization where data is written to RAM and only later "flushed" to the persistent storage. |
| **Loop Device** | A pseudo-device that allows a file to be treated as a block device (essential for mounting forensic images). |
| **/dev/mem** | A specialized device file that provides access to the computer's physical memory, often used for memory dumps. |

---

## Summary
- The File System is a middle layer that translates user "File" operations into physical disk operations.
- Mounting a device can accidentally alter its metadata; investigators must use read-only flags or hardware write blockers.
- Modern OS performance features (caching, buffering) mean that "saving" a file is not instantaneous, and improper removal can cause data loss or forensic inconsistencies.
- Linux/Unix treats hardware as files in `/dev/`, allowing tools like `dd` to copy bytes directly from the device.
- Direct memory access files (`/dev/mem`) are critical for snapshotting RAM for volatility analysis.
- Forensic images preserve the exact spatial organization of data, enabling remote or offline analysis on a trusted workstation.
- Investigators should verify the status of a mounted device (ReadOnly vs. ReadWrite) to ensure evidence integrity.
