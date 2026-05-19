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

> 📎 *Slide reference: `16_volatile.pdf` — Memory dump*

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

## 4. Volatility and Memory Analysis

> 📎 *Slide reference: `16_volatile.pdf` — Volatility technical requirements*

Volatility is the main example used in the lecture for memory-dump analysis. It can analyze memory snapshots from Linux, Windows, and macOS systems, but only when the analysis context is configured for the operating system being examined.

Atzeni mentions both Volatility 2 and Volatility 3, and also mentions Rekall as a less common fork of Volatility. The important forensic point is that memory structures depend on the OS and kernel version; if the tool interprets those structures incorrectly, the analysis can become unreliable.

---

## 5. Process Analysis

Memory forensics can reconstruct process state and compare process relationships. A suspicious case is a process without a plausible parent, or process structures that do not match the expected hierarchy of the operating system.

This is useful for both accidental malfunction and malware investigation: inconsistencies in process trees, runtime state, memory use, or kernel structures can indicate corruption, concealment, or injected behaviour.

---

## 6. Code, Data, and Injection

Memory analysis can inspect code and data that may not exist on disk. This matters because modern malware may be fileless, may hide persistence outside normal storage artifacts, or may decrypt only selected parts of itself during execution.

Key techniques include:
- comparing in-memory state with files, logs, and configuration stored on disk;
- identifying modified libraries or unexpected executable content;
- using Volatility plugins such as `malfind` to locate suspicious memory regions;
- checking for high-entropy encrypted regions that should not normally be encrypted.

These techniques help detect code injection or concealed malware behaviour, especially when the disk view alone looks clean.

---

## 7. Network and Timeline Analysis

Memory may retain active network connections, decrypted network content, session keys, credentials, passwords, passphrases, or tokens. By linking connections and decrypted material to a process, the examiner can pivot from a suspicious network endpoint to concrete runtime evidence.

The resulting timeline should be correlated with:
- Windows Event Logs;
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
| **malfind** | Volatility plugin for suspicious executable memory regions and injection indicators. |
| **Rekall** | Memory-analysis framework derived from Volatility and mentioned as a less common alternative. |
| **Crash Dump** | Memory snapshot produced after a system crash, primarily for debugging but sometimes useful in investigations. |
| **Entropy Analysis** | Technique for flagging unusually encrypted or compressed memory regions that may hide malware content. |

---

## Summary
- Memory can contain evidence unavailable on disk.
- Acquisition must be fast, documented, and integrity-preserving.
- LiME, Fmem, AVML, and crash dumps represent different acquisition paths.
- Volatility-style analysis requires correct interpretation of the target OS and kernel memory structures.
- Process relationships and inconsistent runtime structures can reveal concealed or abnormal behaviour.
- Process, memory-region, entropy, and network analysis can expose injection and malware behavior.
- Memory timelines must be correlated with external logs and filesystem evidence.
