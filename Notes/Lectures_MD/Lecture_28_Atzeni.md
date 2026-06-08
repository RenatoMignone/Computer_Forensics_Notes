# Lecture 28 – Video Carving, OS Forensics, and Memory Acquisition
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/15_OS.pdf`

---

## Overview
This lecture combines two student presentations with Atzeni's theoretical introduction to operating system and memory forensics. The first presentation examines file carving for video recovery. The theoretical part then explains OS-level artifacts, rootkit investigation, and volatile memory acquisition. The final presentation surveys several digital forensics case studies and emerging evidence domains.

---

## 1. Student Presentation: File Carving for Video Recovery

The lecture opens with a presentation on video file carving. The presenter compares signature-based carving and structure-aware carving for video formats such as MP4 and AVI.

Video recovery is harder than simple file recovery because video containers separate metadata from encoded media data. MP4 files, for example, rely on atoms such as:
- **FTYP**, identifying the file type;
- **MOOV**, containing metadata, sample tables, codecs, and timing;
- **MDAT**, containing encoded media data.

If the metadata is missing or corrupted, the raw data may exist but remain unplayable.

---

## 2. Carving Approaches and Experimental Results

The presentation distinguishes:
- **signature-based carving**, which scans for known headers and reads sequentially until a footer or size threshold;
- **structure-aware carving**, which understands container hierarchy and may recover playable fragments even when the file is fragmented or partially corrupted.

Tools discussed include PhotoRec, Scalpel, and Planet Carver. The experiment used videos with different containers, codecs, resolutions, frame rates, sizes, and GOP values, then introduced mild, moderate, and severe corruption.

The main forensic lesson is that the tool choice depends on the case:
- PhotoRec performed poorly in the presented dataset;
- Scalpel was fast and configurable, but over-carved and produced files with unrelated data appended;
- Planet Carver recovered more useful fragments in severe corruption, but required much more time and memory.

The presenter also notes that GOP size affects recovery: more frequent keyframes can improve the chance of playable recovery after corruption.

---

## 3. Operating System Forensics

> 📎 *Slide reference: `15_OS.pdf` — Operating System Forensics*

Atzeni defines OS forensics as analysis of data stored or processed by an operating system. It includes:
- file system structures and metadata;
- allocated and unallocated space;
- event logs and configuration files;
- Windows artifacts such as Prefetch and LNK files;
- Unix-like artifacts such as shell histories, `/var/log/auth.log`, and `/proc`;
- memory dumps and volatile system state.

The operating system is important because it connects user activity, application execution, storage, processes, memory, and network activity.

Atzeni also mentions integrated forensic suites such as Autopsy as useful teaching examples: they combine modules for different evidence types and help reconstruct unified timelines, although he notes that performance and stability may limit their use in real investigations.

---

## 4. Rootkit Investigation

For a rootkit investigation, Atzeni highlights several evidence families:
- centralized logs such as `/var/log/syslog`, `/var/log/auth.log`, and Windows Event Viewer;
- kernel activity, because rootkits often operate at kernel level;
- kernel modules and system call behavior;
- process listings, process statistics, and parent-child relationships;
- memory dumps;
- local socket and network analysis.

Missing logs can be meaningful: a rootkit may suppress, modify, or delete logs, so absence or inconsistency can itself be an indicator.

---

## 5. Memory Forensics

> 📎 *Slide reference: `15_OS.pdf` — Memory Forensics*

Memory forensics examines RAM to recover volatile data such as:
- running processes;
- injected code;
- decrypted data;
- encryption keys;
- passwords and tokens;
- open files;
- active network connections;
- in-memory malware.

Atzeni stresses that every process must use memory. Fileless malware can avoid persistent storage, but it cannot avoid leaving some execution traces in RAM while it runs.

---

## 6. Memory Dumps and Forensic Soundness

A memory dump is a snapshot of RAM at a specific moment. It is valuable but fragile: the system continues to change while the examiner installs or runs the acquisition tool.

This creates admissibility issues. The defence can question:
- whether the acquisition tool modified memory;
- whether the dump is complete;
- whether the tool was compiled or configured for the target system;
- whether the storage and transfer process preserved integrity.

Atzeni distinguishes ordinary debugging access from forensic acquisition. Debuggers and crash dumps can be informative, but forensic tools aim to acquire memory quickly and defensibly.

---

## 7. Memory Acquisition Tools

The lecture introduces several tools and approaches:
- **LiME**, a Linux kernel module for live memory acquisition;
- **Fmem**, which exposes physical memory through a special device file such as `/dev/fmem`;
- **AVML**, which can acquire Linux memory and transfer it to external locations, including cloud storage;
- crash dump utilities, originally intended for debugging but sometimes useful for forensic analysis.

LiME can write memory to a local file or stream it over the network to a forensic workstation. This can reduce direct interaction with the target storage. However, LiME must be compiled for the target kernel and system context, because memory structures depend on the operating system version.

---

## 8. Volatility and Rekall

> 📎 *Slide reference: `15_OS.pdf` — Volatility workflow*

Once a dump is acquired, analysis tools parse the memory image. Volatility is presented as the main framework, with Rekall mentioned as another memory forensics framework.

Volatility can analyze memory images from major operating systems when it is configured with the correct knowledge of the target system. Atzeni notes that Volatility 3 is current, while Volatility 2 is still used in some legacy contexts. Rekall is described as a fork or related framework that is also used for memory analysis.

Common analysis goals include:
- listing processes;
- detecting hidden processes;
- checking loaded libraries or modules against expected state;
- identifying code injection;
- recovering credentials, keys, or plaintext that only exists in memory;
- reconstructing network connections;
- cross-checking memory structures against logs, configuration files, and storage artifacts.

---

## 9. Student Presentation: Case Studies and Emerging Evidence

The final presentation surveys several domains:
- the Garlasco case, focusing on weak chain of custody and forensic procedure;
- the Meredith Kercher / Raffaele Sollecito laptop analysis, focusing on metadata interpretation and last-access artifacts;
- EncroChat, framed as real-time interception rather than ordinary post-mortem forensics;
- automotive forensics, including infotainment, GPS, CAN bus signals, paired phones, and correlation with physical evidence;
- AI-assisted forensics, useful for triage and classification but risky if used as the decisive basis for accusations.

The discussion reinforces a recurring course point: digital artifacts gain evidentiary value through correlation, context, and defensible procedure.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **File Carving** | Recovery of files from raw data without relying on file-system metadata. |
| **MOOV Atom** | MP4 metadata structure needed to interpret media samples and playback timing. |
| **GOP** | Group of pictures; the interval between keyframes affects video recovery resilience. |
| **OS Forensics** | Analysis of operating-system artifacts such as logs, processes, registries, file metadata, and memory. |
| **Memory Dump** | Snapshot of RAM acquired for post-mortem analysis. |
| **LiME** | Linux Memory Extractor, a live memory acquisition kernel module. |
| **Volatility** | Memory forensics framework for analyzing dumps from multiple operating systems. |
| **Malfind** | Volatility plugin used to identify suspicious executable memory regions and possible injection. |

---

## Summary
- Video carving is difficult because playable recovery requires both media data and metadata.
- Structure-aware carving can recover more useful fragments than simple signature scanning, at higher resource cost.
- OS forensics links logs, processes, file systems, registry/configuration data, and memory.
- Rootkit investigations require cross-checking logs, kernel behavior, process structures, memory, and network activity.
- Memory forensics is powerful because fileless and encrypted activity must still appear in RAM at some point.
- Memory acquisition is fragile and can be challenged in court if tool effects and integrity are not documented.
- LiME, Fmem, AVML, Volatility, and Rekall represent the acquisition and analysis workflow.
- Case-study presentations show that digital evidence must be correlated with physical, legal, and procedural context.
