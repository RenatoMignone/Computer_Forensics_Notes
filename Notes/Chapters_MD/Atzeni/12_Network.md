# Chapter 12 – Network Forensics
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/12_Network.pdf`](../../Slides/Atzeni/12_Network.pdf)
**Covered in Lectures:** [Lecture 21](../../Lectures_MD/Lecture_21_Atzeni.md), [Lecture 23](../../Lectures_MD/Lecture_23_Atzeni.md), [Lecture 24](../../Lectures_MD/Lecture_24_Atzeni.md)

---

## Introduction

Network forensics captures, records, and analyses network traffic and related artifacts to support incident and legal investigations. It is usually complementary to host, file system, malware, and legal evidence.

---

## 1. Evidence Identification and Collection

Network investigations identify digital footprints such as IP addresses, domains, accounts, repositories, social profiles, and public communications.

> 📎 *Slide reference: `12_Network.pdf` — Evidence identification*

Collection can include PCAPs, logs, screenshots, web archives, metadata exports, and OSINT snapshots. Preservation must include timestamps, source information, and defensible capture methods.

Because online evidence can change outside the investigator's control, Atzeni stresses snapshot-style preservation. A screenshot, downloaded page, metadata export, or archived web resource should be timestamped, signed where appropriate, and put into the chain of custody.

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
| **Wayback Machine / web archives** | Historical versions of pages or deleted online material. |

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

Analysis often becomes graph-oriented: accounts, domains, IP addresses, repositories, organisations, posts, timestamps, and service providers are correlated to reconstruct relationships and timelines. Third-party cooperation may be required when useful metadata is held by a network administrator, email provider, social platform, or other service provider.

---

## 4. Anti-Forensics

> 📎 *Slide reference: `12_Network.pdf` — Anti-forensics for network forensics*

Attackers may use encryption, tunnelling, packet manipulation, traffic shaping, decoys, polymorphic malware, or anonymisation. The goal is to hide payload, intent, origin, destination, or the pattern of behaviour.

Examples discussed in the lectures include:
- **encrypted protocols** such as TLS, SSH, IPsec, and VPNs;
- **tunnelling**, where one protocol or full packet stack is carried inside another encrypted channel;
- **covert channels**, such as data hidden in DNS queries or unused protocol fields;
- **IP spoofing** and packet manipulation to obscure the origin of traffic;
- **traffic shaping**, delays, slow scans, and decoy traffic to defeat real-time detection and later forensic reconstruction;
- **honeypots and honeynets**, which can be useful for defenders but may also complicate interpretation of attacker behaviour;
- **polymorphic or metamorphic malware**, which may change payloads or rewrite itself to resist signature-based detection.

Countermeasures include deep packet inspection where possible, encrypted traffic analysis, behavioural analytics, comprehensive logging, WORM storage, and threat intelligence. Atzeni emphasises that no single countermeasure is sufficient; investigators usually combine traffic inspection, anomaly detection, whitelisting, tamper-resistant logs, and shared indicators of compromise.

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
