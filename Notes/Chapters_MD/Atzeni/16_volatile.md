# Chapter 16 – Volatile Memory Forensics
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/16_volatile.pdf`](../../Slides/Atzeni/16_volatile.pdf)
**Covered in Lectures:** [Lecture 28](../../Lectures_MD/Lecture_28_Atzeni.md)

---

## Introduction

Volatile memory forensics examines RAM to recover evidence that may never be written to disk or may disappear after shutdown. It is especially important for fileless malware, injected code, encryption keys, credentials, active network sessions, and runtime-only artifacts.

The workflow has two major phases:
1. acquire a memory dump;
2. analyze that dump with tools such as Volatility or Rekall.

---

## 1. Memory Dumps

> 📎 *Slide reference: `15_OS.pdf` — Memory dump*

A memory dump is a point-in-time capture of RAM. It may contain process state, open files, network connections, decrypted data, and traces of malware.

The acquisition is delicate because RAM changes continuously. Installing and running an acquisition tool can itself modify memory. This must be documented because it can be challenged in court.

---

## 2. Acquisition Tools

Atzeni discusses several acquisition approaches:
- **LiME**, a Linux kernel module for live memory extraction;
- **Fmem**, which exposes physical memory as a raw device file;
- **AVML**, which can acquire memory and transfer it to local or remote destinations;
- crash dump tools such as `kdump`, which are primarily designed for debugging but may preserve useful forensic state.

The investigator should prefer tools and workflows that reduce interaction with the target system and immediately preserve integrity through hashing and documented transfer.

---

## 3. LiME

LiME can acquire the full contents of Linux RAM and save it locally or stream it over the network. Network streaming can be useful because it avoids writing large evidence files onto the target disk.

LiME must be compiled for the target kernel and architecture. This is not cosmetic: memory structures depend on the exact operating-system version, so a mismatch can prevent correct acquisition or analysis.

---

## 4. Volatility Requirements

> 📎 *Slide reference: `16_volatile.pdf` — Volatility technical requirements*

Volatility parses memory dumps by understanding the target operating system's internal structures.

Volatility 2 uses profiles, such as Windows build profiles. Volatility 3 uses symbol tables:
- Windows symbols can be obtained through Microsoft's symbol infrastructure;
- Linux and macOS analysis may require building an ISF file from target debug symbols.

Without the correct symbols or profile, offsets are wrong and plugin output becomes unreliable.

---

## 5. Process Analysis

The Volatility workflow uses multiple process views:
- `pslist`, which walks the ordinary active process list;
- `pstree`, which reconstructs parent-child relationships;
- `psscan`, which scans raw memory for process structures.

Comparing these views is important. A process found by `psscan` but absent from `pslist` may indicate unlinking or hiding behavior typical of rootkits.

---

## 6. DLLs, Handles, and Injection

Memory analysis can inspect loaded libraries, handles, mutexes, registry keys, and suspicious memory regions.

Key techniques include:
- comparing loader lists against VAD regions;
- looking for DLLs present in memory but absent from normal loader structures;
- using `malfind` to locate executable, non-file-backed, suspicious memory areas;
- dumping suspicious regions for reverse engineering.

These techniques help detect process hollowing, reflective DLL injection, and shellcode injection.

---

## 7. Network and Timeline Analysis

Memory may retain active or recently closed network connections. By linking connections to owning PIDs, the examiner can pivot from a suspicious network endpoint to a concrete process.

Volatility timelines can aggregate timestamps from processes, DLLs, registry keys, and file handles. The resulting timeline should be correlated with:
- Windows Event Logs or Sysmon;
- filesystem MAC times;
- packet captures;
- proxy and DNS logs;
- other host artifacts.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **RAM** | Volatile memory holding active runtime state. |
| **LiME** | Linux Memory Extractor, used for live memory acquisition. |
| **VAD** | Windows Virtual Address Descriptor tree describing a process's virtual memory regions. |
| **psscan** | Volatility process scanner that can find hidden or unlinked process structures. |
| **malfind** | Volatility plugin for suspicious executable memory regions and injection indicators. |
| **ISF** | Intermediate Symbol Format used by Volatility 3 to describe kernel structures. |

---

## Summary
- Memory can contain evidence unavailable on disk.
- Acquisition must be fast, documented, and integrity-preserving.
- LiME, Fmem, AVML, and crash dumps represent different acquisition paths.
- Volatility requires correct target profiles or symbols.
- Comparing multiple process views can reveal hidden processes.
- DLL, handle, VAD, and network analysis can expose injection and malware behavior.
- Memory timelines must be correlated with external logs and filesystem evidence.
