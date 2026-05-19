# Lecture 24 – Network Anti-Forensics and Attack Obfuscation
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/12_Network.pdf`

---

## Overview
This lecture completes the network forensics discussion by focusing on anti-forensic techniques. The central theme is that the same technologies that protect privacy or ordinary security can also be used to hide malicious activity.

---

## 1. Student Homework Continuation

The lecture begins with the conclusion of a homework presentation on an Ubuntu local privilege escalation attack involving `snap-confine` and `systemd-tmpfiles`. The presentation highlights the importance of live acquisition, process inspection, socket analysis, and kernel audit logs.

---

## 2. Goals of Network Anti-Forensics

> 📎 *Slide reference: `12_Network.pdf` — Anti-forensics for network forensics*

Network anti-forensics aims to:
- obscure the truth of network flows;
- hide intent and payload;
- wipe or alter logs;
- create decoys and false flags;
- make real-time detection and post-mortem reconstruction harder.

Atzeni stresses that these techniques are not inherently illegitimate: encryption, VPNs, and anonymisation can be privacy-preserving tools as well as attacker tools.

---

## 3. Encryption, VPNs, and Tunnelling

**Encryption** hides payload content through protocols such as TLS, SSH, VPNs, and IPsec.

**Tunnelling** can encapsulate one protocol inside another, hiding not only the content but sometimes the nature of the communication. Examples include SSH tunnelling and DNS tunnelling.

DNS tunnelling is especially relevant because DNS messages can carry enough data in fields that appear legitimate, enabling covert communication or exfiltration.

---

## 4. Packet Manipulation and Traffic Shaping

Attackers may manipulate packet metadata or timing.

| Technique | Purpose |
|-----------|---------|
| **IP spoofing** | Hide or falsify the apparent origin. |
| **Slow scanning** | Spread reconnaissance over long time windows to avoid detection. |
| **Noise generation** | Blend malicious packets into large volumes of benign traffic. |
| **Decoy traffic** | Overload analyst attention and monitoring systems. |

---

## 5. Malware, Anonymisation, and Countermeasures

Polymorphic and metamorphic malware can alter its payload or code structure, weakening signature-based detection. Anonymisation infrastructures such as TOR can hide source and destination relationships by routing traffic through multiple nodes.

Countermeasures include:
- deep packet inspection where legally and technically possible;
- encrypted traffic analysis;
- behavioural analytics;
- tamper-resistant logging such as WORM storage;
- threat intelligence feeds;
- honeypots or honeynets to study current attacker behaviour;
- whitelisting and careful network shaping where the defender controls the infrastructure;
- expert review supported by automated or AI-based detection;
- correlation across host, network, and malware artifacts.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Tunnelling** | Encapsulation of one protocol or flow inside another protocol. |
| **DNS Tunnelling** | Use of DNS queries/responses as a covert data channel. |
| **Polymorphic Malware** | Malware that changes its appearance, often encryption or payload representation, to evade signatures. |
| **Metamorphic Malware** | Malware that rewrites its own code structure while preserving behaviour. |
| **WORM Storage** | Write-once-read-many storage used to make logs resistant to later alteration. |

---

## Summary
- Anti-forensics can target payload, flow metadata, logs, timing, and analyst attention.
- Legitimate privacy technologies can also be abused for concealment.
- Encryption prevents direct payload inspection unless endpoint evidence or keys are recovered.
- Tunnelling can hide protocols and exfiltrate data through apparently legitimate traffic.
- Slow, distributed activity is harder to detect than obvious high-volume attacks.
- Decoy traffic can conceal a more important intrusion.
- Behavioural analytics and threat intelligence are needed when signatures are insufficient.
- Honeypots, whitelisting, tamper-resistant logs, and expert review can help counter network anti-forensics.
