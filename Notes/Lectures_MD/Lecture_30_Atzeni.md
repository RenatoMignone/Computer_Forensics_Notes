# Lecture 30 – Memory Forensics, LiME, Volatility, and Malware Indicators
**Professor:** Atzeni  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Atzeni/15_OS.pdf`, `Slides/Atzeni/16_volatile.pdf`

---

## Overview
This lecture continues the memory-forensics material introduced at the end of Lecture 28. Atzeni distinguishes informal debugging or crash-dump sources from forensic acquisition, explains why full RAM snapshots are needed, and introduces LiME, Volatility, profiles, symbol tables, plugins, and memory-based malware indicators.

---

## 1. From Debugging Access to Forensic Acquisition

> 📎 *Slide reference: `15_OS.pdf` — Volatile memory acquisition*

Atzeni begins by clarifying that many tools can interact with memory, but not all of them are suitable as forensic evidence. Debuggers such as `gdb` can inspect or stop processes and capture limited portions of memory, but they are primarily development tools.

For forensic work, they have limits:
- they usually affect the running system;
- they provide partial access rather than a full evidentiary image;
- they may lack certification or robustness for court use;
- the defence can challenge admissibility because the tool was not designed for forensic acquisition.

Crash dumps may be more useful than debugger snapshots, but they are still sparse and originally intended for system diagnosis.

---

## 2. Full RAM Snapshots

Forensic memory acquisition aims to capture the full content of central memory quickly and with minimal interaction with the target operating system.

The snapshot should be stored in a safe location. If possible, the examiner should avoid writing the dump onto storage controlled by the suspect or by an untrusted system.

This matters because RAM changes continuously. Any acquisition tool necessarily changes some memory state, so the examiner must choose tools that minimize that impact and document the acquisition process.

---

## 3. LiME Acquisition

> 📎 *Slide reference: `15_OS.pdf` — LiME*

**LiME** is presented as one of the most famous Linux memory acquisition tools. It is a kernel module, so it can interact directly with the running kernel and acquire the contents of RAM.

Atzeni highlights a useful client-server acquisition setup:
- a forensic workstation waits for the memory dump;
- the target host loads a LiME module compiled for its kernel;
- the module acquires RAM and sends it through a socket or tunnel to the forensic workstation.

This avoids writing the dump onto the target disk and helps preserve evidence integrity. LiME stores memory content in its own format with minimal additional structure, making it suitable for later analysis by compatible tools.

---

## 4. Volatility as the Analysis Framework

> 📎 *Slide reference: `16_volatile.pdf` — Volatility workflow*

After acquisition, a tool such as **Volatility** performs the analysis. Volatility is an open-source framework built around plugins. It can be used for forensic analysis, debugging, malware investigation, cryptographic analysis, and system-behaviour understanding.

Atzeni emphasizes that Volatility works on the acquired memory image, not on the live target, so analysis is repeatable and does not further modify the original system state.

Typical analysis goals include:
- listing processes;
- reconstructing process trees;
- inspecting loaded libraries and modules;
- checking network connections;
- finding hidden processes or injected code;
- locating information that was nominally deleted but not yet overwritten in RAM.

---

## 5. Profiles, Symbol Tables, and Operating-System Knowledge

Memory is organized differently by each operating system, kernel version, architecture, and configuration. Volatility must know how to interpret those structures.

Atzeni distinguishes:
- **Volatility 2**, which uses profiles;
- **Volatility 3**, which uses symbol tables.

For Windows, symbols can often be downloaded for the relevant version. For Unix-like systems, the analyst may need to build the symbol table from the specific kernel installation. This can be one of the most difficult and time-consuming steps of a real memory investigation.

If the wrong profile or symbol table is used, the analysis may miss objects or interpret memory incorrectly.

---

## 6. Plugin-Based Analysis and Process Views

Volatility plugins analyze different internal memory structures. Atzeni explains that this redundancy is useful: different plugins may see different views of the same system state.

For example:
- a process-list plugin may walk the normal linked list of processes;
- a process-tree plugin may reconstruct parent-child relationships;
- a scan plugin may search memory for process structures even if they are unlinked.

Differences between these outputs can be indicators of compromise. A rootkit may hide a process from one OS-maintained list while leaving traces elsewhere in memory.

---

## 7. Malware Indicators in Memory

Memory forensics is especially useful for malware because every running program must exist in memory at some point.

Atzeni lists several suspicious conditions:
- a child process whose parent has already disappeared;
- a process running from an unexpected user directory while pretending to be a system service;
- unusual loaded modules or libraries;
- code injection into legitimate processes;
- high-entropy memory regions suggesting encrypted or packed content;
- open connections inconsistent with ordinary process behaviour.

Loader-style malware is a typical example: a small initial process downloads or activates the main malicious component, then terminates itself. Memory analysis may reveal the surviving child process and reconstruct the chain.

---

## 8. Rekall and Alternative Tools

Atzeni also mentions **Rekall**, a memory-analysis framework related to Volatility. It was respected and interesting for some time, but today Volatility has the stronger community and remains the more prominent tool in the course discussion.

The broader lesson is not that one tool is enough. Memory analysis often requires comparing multiple views and understanding the operating system deeply enough to explain why one plugin finds something another plugin misses.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Memory Forensics** | Acquisition and analysis of RAM to recover volatile runtime evidence. |
| **LiME** | Linux Memory Extractor, a kernel module used to acquire live RAM. |
| **Volatility** | Open-source memory-analysis framework built around plugins. |
| **Profile** | Volatility 2 description of operating-system memory structures. |
| **Symbol Table** | Volatility 3 mapping used to interpret kernel and memory structures. |
| **Plugin** | Volatility component that performs a specific analysis task. |
| **Rekall** | Memory-forensics framework related to Volatility, mentioned as a less common alternative. |
| **Hidden Process** | Process concealed from ordinary OS views, often by rootkit-style manipulation. |

---

## Summary
- Debugging tools and crash dumps may help investigations, but they are not the same as forensic RAM acquisition.
- A forensic RAM snapshot should be fast, documented, and minimally invasive.
- LiME can acquire Linux memory locally or stream it to a forensic workstation.
- Volatility analyzes memory images through plugins rather than modifying the live system.
- Correct profiles or symbol tables are essential for reliable interpretation.
- Comparing different plugin outputs helps reveal hidden processes and rootkit activity.
- Memory analysis can expose fileless malware, injected code, credentials, keys, and active network state.
- Tool output must be explained through operating-system structure, not treated as magic.
