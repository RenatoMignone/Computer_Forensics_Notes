# Lecture 21 – SSD Acquisition, Data Sanitisation, and Network Forensics Introduction
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/10_HDD-vs-SSD-in-Digital-Forensics.pdf`, `Slides/Atzeni/11_Data-Sanitisation-Techniques.pdf`, `Slides/Atzeni/12_Network.pdf`

---

## Overview
The lecture closes the SSD discussion, introduces sanitisation standards and techniques, and starts the network forensics topic.

---

## 1. Advanced SSD Acquisition

Atzeni completes the SSD discussion by explaining that some acquisition approaches try to bypass ordinary controller behaviour.

> 📎 *Slide reference: `10_HDD-vs-SSD-in-Digital-Forensics.pdf` — Advanced SSD acquisition*

The lecture mentions:
- **factory access mode**, which may reduce or disable mechanisms such as garbage collection, wear levelling, deletion, and remapping;
- **chip-off forensics**, where NAND chips are physically extracted and read directly;
- **over-provisioning**, where the device contains more physical memory than it exposes to the operating system.

These approaches are risky, device-dependent, and may fail when self-encryption is active.

---

## 2. Sanitisation Levels

Atzeni introduces data sanitisation as the legally and technically sound deletion of information from a file, storage device, or managed endpoint. He presents the NIST categories as a practical reference.

> 📎 *Slide reference: `11_Data-Sanitisation-Techniques.pdf` — Sanitisation levels*

| Level | Meaning |
|-------|---------|
| **Clear** | Logical techniques that defeat ordinary, non-invasive recovery. |
| **Purge** | Stronger techniques intended to defeat laboratory-level recovery. |
| **Destroy** | Physical destruction of the device when reuse is not intended. |

---

## 3. Sanitisation Techniques

The lecture compares several ways to remove recoverable data:
- **overwriting**, including multi-pass procedures with zeros, ones, and random data;
- **firmware-level erase commands**, preferred when the device supports them;
- **degaussing**, useful for magnetic devices such as hard disks, floppy disks, and tapes;
- **crypto-erase**, which deletes or changes the encryption key of a self-encrypting drive;
- **remote wipe** through mobile-device-management systems;
- **physical destruction**, such as shredding, incineration, or disintegration.

Atzeni stresses that sanitisation must be verified. A procedure that writes data or issues an erase command must check that the expected operation succeeded.

Verification may include statistical checking of a percentage of the device, full verification for high-security contexts, or hash-based checking against expected values for a fully overwritten device. Controller status and logs are useful to monitor failures, but they may not be sufficient alone. In litigation, a trusted third party may certify the operation, and the report should preserve who performed it, when, with which equipment, and with what result.

---

## 4. Important Terms

Several technical terms shape the sanitisation discussion:
- **Data Encryption Key (DEK)**: the key protecting data at rest.
- **Self-Encrypting Drive (SED)**: a drive that encrypts and decrypts internally at hardware or firmware level.
- **Coercivity**: magnetic resistance relevant to degaussing.
- **NVMe**: a protocol for non-volatile memories that may expose low-level sanitisation commands.
- **FIPS-approved random number generator**: relevant when crypto-erase depends on a key that must not be recomputable.

---

## 5. Network Forensics Introduction

The lecture then begins network forensics. Atzeni defines the strict field as acquisition and analysis of network traffic, but also uses a broader sense that includes network traces, public online artifacts, and OSINT/SOCMINT-style information about people, organisations, domains, and services.

> 📎 *Slide reference: `12_Network.pdf` — Network forensics*

Modern network investigation must consider encryption through TLS, SSH, IPsec, and VPNs. Even when payload inspection is unavailable, packet captures may preserve useful lower-layer information, timing, addresses, and encrypted sessions that could become readable if keys are later recovered.

Public network traces can also support an investigation: social media activity, forum posts, job ads, domain-registration history, public repositories, old website snapshots, and IP-address metadata may help reconstruct behaviour, identify possible tools or infrastructure, and refine hypotheses.

---

## 6. Network Tools and Artifacts

The lecture mentions practical tools and formats:
- **PCAP** as a packet-capture format;
- **Wireshark** for packet acquisition and analysis;
- **Nmap** for service and port investigation;
- **Xplico** and **NetworkMiner** for extracting application-level content from traffic.

Network evidence can be correlated with host logs, file system artifacts, and service-provider information to refine investigative hypotheses.

Because online information can change outside the investigator's control, acquisition must preserve the observed state. Examples include timestamped screenshots, digitally signed captures, downloaded pages or metadata, and a documented chain of custody. The analysis phase may then build graphs linking accounts, IP addresses, domains, organisations, services, and events, sometimes requiring cooperation from network administrators, social platforms, email providers, or other third parties.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Factory Access Mode** | SSD mode that may bypass or reduce ordinary controller mechanisms. |
| **Crypto-Erase** | Sanitisation by deleting or replacing encryption key material. |
| **Degaussing** | Use of a strong magnetic field to destroy data on magnetic media. |
| **PCAP** | Packet capture format used to store network traffic. |
| **Deep Packet Inspection** | Inspection of packet contents, limited when payloads are encrypted. |
| **OSINT** | Use of publicly available online information to support investigative hypotheses. |

---

## Summary
- SSD acquisition may require factory mode, chip-off, or over-provisioning analysis, but all are risky and device-dependent.
- Self-encrypting drives can make chip-off recovery ineffective.
- NIST distinguishes Clear, Purge, and Destroy levels of sanitisation.
- Overwriting, degaussing, crypto-erase, firmware commands, remote wipe, and physical destruction apply to different media and assurance levels.
- Sanitisation must be verified to be forensically defensible.
- Network forensics starts from traffic captures, logs, public traces, and related network artifacts.
- Encryption limits payload inspection but does not make network captures useless.
- Network evidence should be captured with timestamps, signatures, and chain-of-custody documentation because online content can change quickly.
