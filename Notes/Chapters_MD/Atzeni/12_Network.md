# Chapter 12 – Network Forensics
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/12_Network.pdf`](Slides/Atzeni/12_Network.pdf)
**Covered in Lectures:** [Lecture 22](Lectures_MD/Lecture_22_Vaciago.md), [Lecture 24](Lectures_MD/Lecture_24_Atzeni.md), [Lecture 25](Lectures_MD/Lecture_25_Atzeni.md)

---

## Introduction

Network forensics captures, records, and analyses network traffic and related artifacts to support incident and legal investigations. It is usually complementary to host, file system, malware, and legal evidence.

---

## 1. Evidence Identification and Collection

Network investigations identify digital footprints such as IP addresses, domains, accounts, repositories, social profiles, and public communications.

> 📎 *Slide reference: `12_Network.pdf` — Evidence identification*

Collection can include PCAPs, logs, screenshots, web archives, metadata exports, and OSINT snapshots. Preservation must include timestamps, source information, and defensible capture methods.

---

## 2. Tools and Sources

| Tool / Source | Use |
|---------------|-----|
| **Wireshark / PCAP** | Packet capture and protocol analysis. |
| **Nmap** | Service and port discovery. |
| **Xplico / NetworkMiner** | Application-layer reconstruction and file extraction. |
| **IPinfo / Whois / RIPE** | IP ownership, geolocation, ASN, and abuse contacts. |
| **DNSDumpster / Shodan / Censys** | Domain topology and exposed services. |
| **VirusTotal** | Threat intelligence and malicious infrastructure correlation. |

---

## 3. OSINT and Social Media Forensics

OSINT supports attribution, timeline construction, and relationship analysis.

Social media evidence may include:
- public posts;
- account relationships;
- timing and behaviour;
- image metadata;
- reverse image search;
- fake profile detection;
- emotional or motivational signals.

---

## 4. Anti-Forensics

> 📎 *Slide reference: `12_Network.pdf` — Anti-forensics for network forensics*

Attackers may use encryption, tunnelling, packet manipulation, traffic shaping, decoys, polymorphic malware, or anonymisation. The goal is to hide payload, intent, origin, destination, or the pattern of behaviour.

Countermeasures include deep packet inspection where possible, encrypted traffic analysis, behavioural analytics, comprehensive logging, WORM storage, and threat intelligence.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **PCAP** | Standard file format for captured network packets. |
| **OSINT** | Investigation using publicly available sources. |
| **DNS Tunnelling** | Covert channel that uses DNS queries/responses to move data. |
| **Threat Intelligence** | Shared knowledge about malicious infrastructure, indicators, and campaigns. |
| **Traffic Correlation** | Analysis of timing, volume, and route relationships across flows. |

---

## Summary
- Network forensics is strongest when correlated with endpoint evidence.
- PCAPs preserve useful metadata even when payloads are encrypted.
- OSINT can reveal domains, services, leaks, relationships, and suspicious campaigns.
- Social media traces may support attribution and timeline reconstruction.
- Anti-forensics can target payloads, flows, logs, or investigator attention.
- Behavioural and threat-intelligence approaches are needed when signatures fail.
