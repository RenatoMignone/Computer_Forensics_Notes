# Chapter 13 – Digital Forensics in the TOR Network
**Professor:** Atzeni
**Reference Slides:** [`Slides/Atzeni/13_Digital-Forensics-in-the-TOR-Network.pdf`](../../Slides/Atzeni/13_Digital-Forensics-in-the-TOR-Network.pdf)
**Covered in Lectures:** [Lecture 25](../../Lectures_MD/Lecture_25_Atzeni.md)

---

## Introduction

TOR is an anonymity network designed for privacy and free expression, but it is also relevant to anti-forensics because it can conceal the relationship between source and destination. Forensic analysis must therefore distinguish legitimate privacy use from investigative concealment.

---

## 1. Architecture and Daemon

> 📎 *Slide reference: `13_Digital-Forensics-in-the-TOR-Network.pdf` — The Tor Background Daemon*

TOR separates application behaviour from anonymity infrastructure. Applications route traffic through a local proxy-like daemon, while the daemon manages circuits, cryptography, relay selection, and directory consensus.

---

## 2. Onion Routing and Cryptography

Traffic is routed through three relays: guard, middle, and exit. The client negotiates separate keys and encrypts data in layers. Each relay removes only one layer.

| Relay | Knows |
|-------|-------|
| **Guard** | Client IP and next relay. |
| **Middle** | Previous and next relay only. |
| **Exit** | Destination and previous relay, but not client IP. |

End-to-end application encryption remains important because the TOR exit node can see plaintext destination traffic if the application layer is not encrypted.

---

## 3. Guard Nodes

Persistent guard nodes reduce the chance that an adversary eventually becomes the first relay. The user has exposure if the selected guard is malicious, but the probability does not grow with every circuit.

Guard persistence mitigates relay-level attacks but not a broad adversary observing both entry and exit traffic.

---

## 4. Forensic Detection and Evasion

Known TOR relays can be detected by cross-referencing captured IPs with public TOR node lists. This approach becomes weaker when traffic uses non-public TOR nodes that are not available in ordinary public lists.

The lecture also discusses traffic correlation, relay jurisdiction, and guard discovery attacks as possible investigative approaches.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Onion Routing** | Layered encryption and relay routing so each relay knows only a limited part of the path. |
| **TOR Daemon Proxy** | Local component used by applications to send traffic through the TOR daemon. |
| **Directory Authorities** | Trusted TOR infrastructure that signs relay consensus information. |
| **Non-Public TOR Node** | TOR node not available through ordinary public relay lists, making simple relay-list detection weaker. |
| **Guard Discovery Attack** | Attempt to identify a hidden service or user's guard relay through traffic behaviour. |

---

## Summary
- TOR is privacy infrastructure with forensic and anti-forensic relevance.
- The daemon manages circuits and hides complexity from applications.
- Three-hop circuits separate origin and destination knowledge.
- Persistent guards reduce repeated exposure to malicious entry relays.
- Public relay lists can identify ordinary TOR use, but not bridge use.
- Traffic correlation remains a major weakness against powerful adversaries.
