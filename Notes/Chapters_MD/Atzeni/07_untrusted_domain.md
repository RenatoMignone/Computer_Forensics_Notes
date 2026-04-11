# Chapter 7 – Untrusted Domains, Malware Constraints, and Advanced Threats
**Professor:** Atzeni  
**Reference Slides:** `Slides/Atzeni/07_untrusted_domain.pdf`, `Slides/Atzeni/07a_HTTPS-Session-Hijacking.pdf`, `Slides/Atzeni/07b_Man-in-the-Disk-MitD-Vulnerability.pdf`  
**Covered in Lectures:** Lecture 10, Lecture 11

---

## Introduction
For a digital forensics investigation to be scientifically sound and legally admissible, the analysis must be conducted within a **Trusted Environment**. However, the vast majority of environments investigators examine are **Untrusted Domains**—systems potentially compromised by targeted malware, misconfigurations, or physical attacks. This chapter explores the myriad of ways a system can be compromised, detailing the expansive "Man-in-the-Something" attack family, supply chain vulnerabilities, and the advanced operational capabilities of Advanced Persistent Threats (APTs). 

---

## 1. Compromise in Untrusted Environments

Attacks generally target one of two levels:
1. **Node-Level Infection:** Directly compromises the physical device or the operating system. Node infections can bypass border firewalls, providing the attacker with lateral movement capabilities internally. Vulnerabilities include trojans, social engineering (e.g., fraudulent transfers), poor hardware protections, or even intentional misbehavior by a system administrator (e.g., hiding critical folders at the OS level).
2. **Network-Level Infection:** The nodes may remain clean, but the traffic flowing between them is intercepted, injected, or modified en route (e.g., traffic injection, unauthenticated DNS/ARP alterations).

> 📎 *Slide reference: `07_untrusted_domain.pdf` — Untrusted Environments & Node/Network Compromise*

---

## 2. The "Man-in-the-Something" Attack Family

Attackers position themselves advantageously to intercept or manipulate data. This extends far beyond traditional network interception, deeply integrating into modern host storage and memory arrays.

### 2.1 Man-in-the-Middle (MitM) & HTTP Session Hijacking
- **ARP Poisoning (Network Layer 2):** Because the ARP protocol is unauthenticated, an attacker on the same local area network can emit forged ARP messages. This forces a victim node to send traffic to the attacker’s MAC address rather than the legitimate gateway.
- **Cross-Site Scripting (XSS) Session Hijacking:** At the application layer, if an application fails to sanitize user input, an attacker can load malicious JavaScript. If session cookies lack proper security flags (like `HttpOnly`), this script can extract the session ID and transmit it to an attacker’s domain, hijacking fully encrypted HTTPS sessions.

### 2.2 Advanced Man Variants
- **Man-in-the-Browser:** Malware residing directly in the browser. It waits for the user to visit sensitive domains (like online banking) and seamlessly modifies the form data *before* it is submitted, allowing it to harvest credentials or bypass TLS encryption entirely.
- **Man-in-the-Cloud:** Acquiring and reusing authentication tokens (like OAuth tokens) to autonomously access cloud storage (e.g., Google Drive) unnoticed. These tokens frequently violate the principle of least privilege, providing prolonged and far-reaching access.
- **Man-in-the-Mobile:** Bypassing Multi-Factor Authentication (MFA). Malware like *Zipmode* continuously intercepts 2FA SMS codes to forward them to an attacker. AI agents are increasingly used to scale and automate this exploitation immediately.
- **Man-in-the-Memory:** A "file-less" malware execution technique that operates entirely in RAM. Because data and encryption keys must eventually be decrypted into memory to be utilized by the operating system, this malware reads sensitive data prior to encryption. It is famously leveraged by both intelligence/police agencies and advanced attackers.
- **Man-on-the-Side:** A passive observation technique paired with brief injections (like statistical perturbations or overwhelming bandwidth usage) designed to blind or evade Intrusion Detection Systems (IDS).

> 📎 *Slide reference: `07a_HTTPS-Session-Hijacking.pdf` — MitM Extentions*

### 2.3 Man-in-the-Disk (MitD)
An often-overlooked vector focusing entirely on insecure shared storage instead of network transit. Attackers silently manipulate files temporarily stored by legitimate applications.
- **Multi-user Temp Folders (`/tmp` in Linux):** If applications create temporary files unsafely, an attacker can replace them or use *symbolic link attacks* to trick the application into overwriting sensitive system files (such as erasing password databases).
- **Log File Poisoning:** Attackers can write crafted executable payloads into open log files (like `/var/log`). If downstream analytical parsers (like SIEM reporting tools) lack strict input sanitization, they may execute the payload upon parsing the log.
- **Desktop Apps & Steganography:** Documents temporarily stored on disk can be modified to embed malicious macros. SVG graphics or PDF files can embed executable JavaScript triggered when subsequently opened by the victim.
- **CI/CD Pipelines and Installers:** Malicious actors may access shared storage locations used by Continuous Integration pipelines to quietly swap clean deployment artifacts with infected ones; or modify temporary installer packages before an OS update completes.

**Defenses against MitD**: Implementing strict ACLs, forcing Atomic System Operations (ensuring reads and writes cannot be interrupted via race conditions), creating files safely (e.g., `mkstemp`), and enforcing rigorous, repeated input sanitization.

> 📎 *Slide reference: `07b_Man-in-the-Disk-MitD-Vulnerability.pdf` — Storage constraints*

---

## 3. Advanced Persistent Threats (APTs) & Supply Chain Attacks

### 3.1 Supply Chain Compromise
When organizations are heavily fortified, attackers target their less-secure partners or dependencies.
- **Software:** Infiltrating development pipelines to patch malicious code into trusted vendor software updates (e.g., the SolarWinds Orion breach).
- **Firmware/Hardware:** Manipulating devices physically during shipping (e.g., Israeli explosive implants in Hezbollah pagers).

### 3.2 Advanced Persistent Threats (APTs)
APTs are heavily funded, exceedingly patient cyber-espionage state or criminal groups. Typical campaigns span months to years without detection.
- **Phase 0: Reconnaissance:** Extensive open-source intelligence gathering to learn employee habits and technology infrastructure (like observing job postings to infer which IDS the company uses).
- **Phase 1: Initial Intrusion:** Utilizing tailored Spear-Phishing or purchasing expensive zero-day exploits. Phishing often uses misdirection domains (e.g., `qov.hu.com` passing for `gov.hu`).
- **Phase 2: Foothold Establishment:** Imbedding backdoors and multi-platform rootkits (like APT28’s *X-Agent*).
- **Phase 3: Privilege Escalation & Lateral Movement:** Waiting passively (using keyloggers) to harvest administrative credentials before bouncing to other nodes using legitimate tools like RDP or SSH.
- **Phase 4: Evasion and Exfiltration:** Slowly extracting data while evading detection by diluting traffic loads, encrypting communication (through custom C2 servers like Zebra C2), stealing signed certificates, or altering execution metadata (timestamps).

> *APT28 (Fancy Bear): A famous Russian state-sponsored group responsible for the 2016 US election interference and attacks against Ukrainian infrastructure (e.g., NotPetya Wiper campaigns).*

---

## 4. Kernel-Level System Call Manipulation

To truly control a system and remain hidden, advanced attackers load malicious modifications strictly into the OS Kernel.

### 4.1 Loadable Kernel Modules (LKMs)
Modern environments dynamically load kernel functions to remain memory efficient. High-privilege attackers can inject a malicious LKM to tamper with the **Syscall Table** (the array correlating system calls with their backend routines). By redirecting a standard system call like `open()` to a malicious one, the application's read operation behaves completely normally, while seamlessly running a malicious background task.

### 4.2 Altering Inter-Process Communication (`kill`)
The `kill` system call sends critical instruction signals between processes. An investigator must realize that `kill` can easily be modified:
- By hijacking it, an attacker could instruct that whenever signal *64* or *63* is sent, the system provides automatic root access or wakes a dormant backdoor. 
- **Forensic Traceability:** Administrators and investigators can search `dmesg` (the kernel logging utility) for anomalies utilizing log severity tags (e.g., `KERN_WARNING`, `KERN_ERROR`) to track unapproved module loads.

> 📎 *Slide reference: `07_untrusted_domain.pdf` — LKMs and kernel-level manipulation*

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Man-in-the-Disk (MitD)** | Modifying files written to shared storage folders before legitimate actions use them, bypassing network security layers. |
| **Atomic Operation** | A process that completes execution instantaneously without being interrupted by other scheduling tasks. |
| **Supply Chain Attack** | Infiltrating an organization by compromising trusted external vendor software, libraries, or physical shipments. |
| **APT28 (Fancy Bear)** | A prominent Russian state-sponsored espionage group identified by tools like the *X-Agent* rootkit and specific geopolitical targets. |
| **Loadable Kernel Module (LKM)** | Executable code built into the Linux kernel upon demand; frequently targeted to overwrite Syscall Tables with backdoors. |
| **dmesg** | Linux utility tracing the kernel ring buffer, utilized to audit hardware connections and module events. |

---

## Summary
- A trusted environment is paramount to forensics; discovering the method of compromise directly influences whether evidence is considered unadulterated.
- The "Man-in-the-Something" suite highlights the expansion of interception. Man-in-the-Memory bypasses at-rest encryption; Man-in-the-Mobile circumvents MFA; Man-in-the-Disk turns benign temporary folders (or log files) into weaponized execution vectors.
- Effective defenses prioritize input sanitization, Atomic System Operations, and robustly mapped Access Control Lists applied directly over shared storage.
- APT agents exploit Supply Chain channels and play the "long game," executing highly patient reconnaissance and lateral movement rather than immediate destruction.
- A sophisticated attacker with root privileges will manipulate the Kernel's Syscall Table through LKMs to hijack fundamentally necessary functions like `open` or `kill`, ensuring stealthy operation that bypasses traditional anti-virus logging.
- `dmesg` serves as a vital investigative tracking tool for kernel-level anomalies and component initialization tracing.
