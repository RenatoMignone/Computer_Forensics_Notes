# Chapter 16 – Volatility and Volatile Memory Analysis
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/16_volatile.pdf`](../../Slides/Atzeni/16_volatile.pdf)  
**Covered in Lectures:** [Lecture 30](../../Lectures_MD/Lecture_30_Atzeni.md)

---

## Introduction

This chapter contains the real Chapter 16 material: analysis of acquired memory images, especially through Volatility. Chapter 15 covers OS forensics and the acquisition of volatile memory; Chapter 16 begins after the dump exists and the investigator must interpret it.

Volatile memory analysis is valuable because RAM may contain evidence that never appears on disk or disappears after shutdown, including fileless malware, injected code, credentials, keys, plaintext, and active network state.

---

## 1. Volatility Workflow

> 📎 *Slide reference: `16_volatile.pdf` — Volatility workflow*

After acquisition, tools such as **Volatility** analyze the memory image. Volatility is an open-source framework built around plugins. It can analyze memory snapshots from different platforms when configured with correct knowledge of the target operating system.

Because Volatility works on the acquired image rather than the live system, analysis can be repeated without further modifying the evidence source.

---

## 2. Profiles and Symbol Tables

Memory is organized differently by each operating system, kernel version, architecture, and configuration. Volatility must know how to interpret those structures.

Atzeni distinguishes:
- **Volatility 2**, which uses profiles;
- **Volatility 3**, which uses symbol tables.

For Windows, symbols can often be downloaded for the relevant version. For Unix-like systems, the analyst may need to build the symbol table from the specific kernel installation. This can take significant time in real investigations.

If the wrong profile or symbol table is used, the analysis may miss objects or interpret memory incorrectly.

---

## 3. Initial Examination

The first step is triage: understand what kind of memory image is being analyzed and what system produced it.

Atzeni describes using plugins to identify:
- operating-system family and version;
- architecture;
- memory-image metadata;
- acquisition time;
- registry hives or equivalent system configuration artifacts;
- signs of virtualization or nested environments.

This initial picture informs every later query. A virtualized artifact may even require separate analysis with different assumptions.

---

## 4. Process Analysis

> 📎 *Slide reference: `16_volatile.pdf` — Process analysis*

Volatility provides different plugins that examine different memory structures. This redundancy is useful because each view may reveal or miss different objects.

Examples include:
- process-list style views that walk the normal linked list of processes;
- process-tree views that reconstruct parent-child relationships;
- scan-based views that search memory for process structures even if they are no longer linked.

The differences between these outputs can be evidence. A rootkit may hide a process from ordinary OS-maintained lists, while raw memory scanning still finds it.

---

## 5. Malware Indicators

Memory forensics can reveal malware indicators that storage analysis may miss:
- a child process whose parent has terminated;
- a process pretending to be a system service but running from a user folder;
- unexpected modules or DLLs;
- suspicious virtual address descriptor regions;
- code injection into legitimate processes;
- high-entropy regions suggesting packed or encrypted content;
- open network connections inconsistent with process behaviour.

Atzeni gives loader-style malware as an example: a small loader downloads or activates the main malicious component, then terminates itself. Memory analysis may reveal the surviving child process and reconstruct the relationship.

---

## 6. Deleted and Residual Memory Content

RAM behaves similarly to storage in one important sense: when information is no longer logically active, it is not necessarily overwritten immediately.

A process may unload a module or free a memory area, but the previous content may remain until reused. A memory snapshot can therefore contain traces of data that should no longer be accessible through normal OS abstractions.

This is one reason memory forensics can recover passwords, keys, tokens, plaintext fragments, and malware remnants.

---

## 7. Network and Runtime State

Memory may retain information about active connections, sockets, ports, and process ownership. Linking network state to process state lets the investigator pivot from an endpoint or command-and-control indicator to the executable context that produced it.

The memory timeline should be correlated with:
- filesystem MAC times;
- Windows Event Logs;
- shell history;
- proxy, DNS, and firewall logs;
- packet captures;
- malware indicators.

---

## 8. Rekall and Multi-Tool Reasoning

Atzeni mentions **Rekall** as a memory-analysis framework related to Volatility. It is less prominent today, but it illustrates the broader point that memory analysis should not rely blindly on one tool or one plugin.

The examiner must understand why one view finds an object and another view does not. That explanation is part of the evidentiary value of the analysis.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Volatility** | Open-source memory-analysis framework built around plugins. |
| **Profile** | Volatility 2 description of operating-system memory structures. |
| **Symbol Table** | Volatility 3 mapping used to interpret kernel and memory structures. |
| **Plugin** | Component that performs one specific memory-analysis task. |
| **pslist** | Process-list style analysis based on ordinary OS process structures. |
| **psscan** | Scan-style process discovery that can reveal structures missing from normal lists. |
| **malfind** | Volatility plugin for suspicious executable memory regions and injection indicators. |
| **Rekall** | Memory-analysis framework related to Volatility. |
| **Hidden Process** | Process concealed from ordinary OS views, often through rootkit-style manipulation. |

---

## Summary
- Chapter 16 is now focused on Volatility and memory analysis, not acquisition.
- Volatility analyzes acquired memory images through plugins.
- Correct profiles or symbol tables are essential for reliable interpretation.
- Initial triage identifies OS, architecture, metadata, and configuration context.
- Comparing process-list, tree, and scan outputs helps detect hidden processes.
- Malware indicators include unusual parents, path mismatches, injected code, suspicious modules, and high-entropy regions.
- Memory may retain residual data after logical deletion or unloading.
- Network state in RAM should be correlated with logs, packet captures, and filesystem timelines.
