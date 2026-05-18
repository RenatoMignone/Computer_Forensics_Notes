# Lecture 25 – TOR and Cloud Forensics
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/13_Digital-Forensics-in-the-TOR-Network.pdf`, `Slides/Atzeni/14_Cloud.pdf`

---

## Overview
The lecture covers TOR as both privacy infrastructure and anti-forensic tool, then introduces the peculiarities of cloud forensics.

---

## 1. TOR as Privacy Tool and Anti-Forensic Infrastructure

> 📎 *Slide reference: `13_Digital-Forensics-in-the-TOR-Network.pdf` — TOR key characteristics*

TOR is an open-source anonymity network based on onion routing. It routes traffic through relays so that no single relay knows both the user's origin and the final destination.

The lecture emphasises the dual nature of TOR:
- legitimate privacy protection for free speech and safety;
- possible concealment infrastructure for illegal activity.

---

## 2. Onion Routing and the TOR Daemon

The **TOR daemon** runs locally as a proxy-like component. Applications such as Tor Browser send traffic to the daemon, which handles routing, cryptography, relay selection, and circuit management.

TOR circuits usually involve:
1. **Guard node**, which sees the user's IP but not the destination.
2. **Middle relay**, which forwards encrypted cells.
3. **Exit node**, which connects to the destination and sees destination traffic not protected by end-to-end encryption.

Each layer is encrypted with a different symmetric key, and relays peel only their own layer.

---

## 3. Guard Nodes and Traffic Correlation

> 📎 *Slide reference: `13_Digital-Forensics-in-the-TOR-Network.pdf` — Guard nodes*

Persistent guard nodes reduce the probability that an adversary eventually becomes the entry relay. Instead of choosing a new entry relay for every circuit, the client keeps a small guard set for an extended period.

This mitigates cumulative intersection attacks but does not defeat:
- malicious guards selected at the beginning;
- adversaries observing both ends of the traffic;
- network-level adversaries with broad visibility.

---

## 4. Detecting TOR and Its Limits

Forensic analysts can identify TOR use by cross-referencing captured IPs against known TOR relay lists. This approach becomes weaker when traffic uses non-public TOR nodes that do not appear in the ordinary public lists.

The lecture also discusses international traffic-correlation concerns, especially where many relays fall within cooperative intelligence jurisdictions.

---

## 5. Cloud Forensics Peculiarities

> 📎 *Slide reference: `14_Cloud.pdf` — Cloud forensics peculiarities*

Cloud forensics applies digital forensics to cloud environments, where traditional assumptions about physical access and stable devices often fail.

Key peculiarities include:
- **multi-tenancy**, where multiple customers share physical resources;
- **ephemeral resources**, such as containers, VMs, and serverless functions;
- **provider dependency**, especially in SaaS and PaaS;
- **jurisdictional fragmentation** across countries and legal regimes;
- **log completeness and integrity** problems.

---

## 6. Cloud Models and Evidence Access

| Model | Investigator Visibility |
|-------|-------------------------|
| **SaaS** | Mostly user-level and application-level logs; strong provider dependency. |
| **PaaS** | Application-level visibility and some platform logs; no hardware control. |
| **IaaS** | Better VM, storage, and network control, but still no physical hardware access. |

Cloud storage such as **Amazon S3** can be very valuable because it may provide versioning, WORM-like retention options, long-term storage classes, and provider-mediated access to stored data. However, the investigator often relies on the provider's APIs and trustworthiness.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **TOR Daemon** | Local process that manages TOR circuits, cryptography, relay state, and proxy-like routing for applications. |
| **Guard Node** | First relay in a TOR circuit; it knows the client IP but not the destination. |
| **Non-Public TOR Node** | TOR node not available through ordinary public relay lists, making simple relay-list detection weaker. |
| **Cloud Forensics** | Application of digital forensic methods to cloud environments. |
| **Multi-Tenancy** | Cloud property where multiple users share physical or virtual infrastructure. |
| **WORM-like Cloud Retention** | Contractual storage property that can prevent even the customer from deleting or modifying retained data for a configured period. |

---

## Summary
- TOR provides privacy but can also obstruct network attribution.
- Onion routing separates knowledge of origin, path, and destination across relays.
- Persistent guards reduce long-term exposure to malicious entry relays.
- Relay-list detection works only against public relays, not non-public TOR nodes.
- Cloud forensics breaks classic assumptions about physical seizure and direct imaging.
- SaaS, PaaS, and IaaS provide different evidence visibility.
- Cloud logs may be incomplete unless configured for the relevant data-plane events.
- Provider trust, jurisdiction, and API-mediated access must be documented in any cloud investigation.
