# Lecture 23 – Network Forensics, OSINT, and Social Media Evidence
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/12_Network.pdf`

---

## Overview
This lecture continues network forensics with a focus on OSINT, domain and IP investigation, social media traces, and the forensic value of public online activity. It also includes a short student homework presentation on a Linux local privilege escalation vulnerability.

---

## 1. Network Forensics as Complementary Evidence

Network forensics is often not sufficient by itself, but it is powerful when correlated with file system evidence, host logs, social media traces, and organisational context.

> 📎 *Slide reference: `12_Network.pdf` — Evidence identification and collection*

Atzeni stresses that online traces can help reconstruct motivation, behaviour, relationships, and timelines.

---

## 2. OSINT Sources for Network Investigation

Publicly available sources can support identification and collection.

| Source | Forensic Use |
|--------|--------------|
| **IP info services** | Geolocation, ASN, hosting/provider information, abuse contacts. |
| **Whois / RIPE** | Ownership, route, registry, creation and modification dates. |
| **DNSDumpster** | Domain topology, subdomains, mail servers, DNS records. |
| **Shodan / Censys / SpiderFoot** | Host exposure, services, scanned device metadata. |
| **Pastebin / search dorks** | Leaked credentials, alerts, or incident mentions. |
| **VirusTotal** | Threat intelligence and malicious infrastructure correlation. |

> 📎 *Slide reference: `12_Network.pdf` — Network Forensics OSINT*

---

## 3. Domain and Service Analysis

Investigators can use DNS and service data to identify unusual behaviour:
- freshly registered domains;
- missing or inconsistent DNS records;
- unexpected services on exposed hosts;
- vulnerable versions;
- infrastructure historically associated with suspicious campaigns.

These are not final proof by themselves, but they are useful flags for deeper investigation.

---

## 4. Social Media Forensics

> 📎 *Slide reference: `12_Network.pdf` — Social Media Forensics*

Social media analysis may reveal:
- public profiles and aliases;
- timing of activity;
- relationships and recurring interactions;
- GPS/EXIF metadata in images;
- reverse-image-search clues;
- emotional state, motivation, or affiliation;
- fake profiles or coordinated activity.

Atzeni connects this back to earlier case studies: online activity can reveal relationships, motivations, and links to competing organisations or other suspects.

---

## 5. Homework Presentation: Linux Privilege Escalation

The final part begins a student presentation about a local privilege escalation attack involving `snap-confine`, `systemd-tmpfiles`, `/tmp`, sockets, and ephemeral artifacts.

The forensic lesson is that volatile artifacts require live acquisition:
- RAM state;
- `/tmp` filesystem entries;
- active sockets;
- process metadata under `/proc`;
- system logs.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **OSINT** | Open Source Intelligence; use of publicly available information for investigation. |
| **Whois** | Registry lookup method for domain and IP ownership information. |
| **Threat Intelligence Feed** | Shared database or service describing known malicious infrastructure, malware, or indicators. |
| **Live Acquisition** | Collection of evidence while a system is running, needed for volatile artifacts. |

---

## Summary
- Network forensics is strongest when correlated with host and timeline evidence.
- OSINT can reveal IP ownership, domains, services, leaks, and suspicious infrastructure.
- DNS records and registration history can expose campaign-like behaviour.
- Social media evidence can support attribution, geolocation, motivation, and relationship mapping.
- Public tools remain useful even though commercial OSINT services are now often stronger.
- Reverse image search and EXIF data can identify places or device behaviour.
- Volatile attack artifacts must be collected live before they disappear.
