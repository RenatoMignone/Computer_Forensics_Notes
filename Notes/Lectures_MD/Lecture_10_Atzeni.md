# Lecture 10 – Untrusted Domains and Malware Infection Vectors
**Professor:** Atzeni
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Atzeni/07_untrusted_domain.pdf`, `Slides/Atzeni/07a_HTTPS-Session-Hijacking.pdf`, `Slides/Atzeni/07b_Man-in-the-Disk-MitD-Vulnerability.pdf`

---

## Overview
This lecture explores the importance of trusted environments for conducting forensic investigations. It examines various high-level and low-level compromise possibilities that can disrupt or alter forensic analysis, categorizing them into node-level and network-level infections. A specific focus is placed on the extensive "Man-in-the-Middle" family of attacks, including variations such as Man-in-the-Cloud, Man-in-the-Mobile, and Man-in-the-Disk.

---

## 1. Compromise in Untrusted Environments

For a forensic investigation to be structurally sound and legally admissible, it must take place in a trusted environment. However, investigators frequently encounter environments that have been compromised either intentionally by an attacker or inadvertently due to systemic weaknesses.

### 1.1 Node-Level Infection
Infection occurs directly on the device or host. It severely expands the attack surface, potentially bypassing network firewalls and access controls.
- **Malware & Trojans:** Legitimate-looking software embedding malicious functionalities (e.g., credential theft, installing backdoors, or concealing folders).
- **Social Engineering:** Manipulating human users via urgent phishing emails or chat messages (e.g., requesting fraudulent bank transfers or cloud credentials).
- **Physical Compromise:** Acquiring physical access to a poorly hardened device.
- **Bugs and Misconfigurations:** Unintended vulnerabilities within applications. Forensic investigators must rely on certified or well-tested tools (e.g., hardware write blockers) to avoid erroneous analysis derived from bugs.
- **Willing Misbehavior:** A malicious system administrator with root access can alter OS calls or device drivers (e.g., storage drivers modified to conceal specific folders) down to the firmware or BIOS level.

### 1.2 Network-Level Infection
The nodes themselves might remain uninfected, but an attacker compromises the traffic flowing between them.
- **Sniffing and Injection:** Monitoring or altering traffic to acquire credentials or fool legitimate nodes.
- **Denial of Service:** Disrupting network availability.

> 📎 *Slide reference: `07_untrusted_domain.pdf` — Untrusted Environments & Node/Network Compromise*

---

## 2. The "Man-in-the-Something" Attack Family

The lecture detailed how attackers position themselves to intercept, modify, or exploit data transit and storage.

### 2.1 Man-in-the-Middle (MitM)
An attacker sits between two legitimate parties to intercept and potentially alter communications.
- **ARP Poisoning (Network Layer 2):** Since the ARP protocol (mapping IP addresses to MAC addresses) is unauthenticated, an attacker on the same LAN can broadcast forged ARP messages. The victim is tricked into sending traffic to the attacker's MAC address instead of the legitimate gateway or node.
- **HTTP Session Hijacking & Cross-Site Scripting (XSS):** At the application layer, an attacker exploits lack of input sanitization to inject malicious scripts (like JavaScript) into a web session. If a session cookie lacks proper protections (e.g., `HttpOnly` flag), the script can steal the session ID and send it to an evil domain, effectively hijacking an HTTPS-secured session.

> 📎 *Slide reference: `07a_HTTPS-Session-Hijacking.pdf` — HTTP Session Hijacking & XSS*

### 2.2 Variations of MitM
- **Man-in-the-Browser:** Malware infects the browser directly, seamlessly altering data input by the user on legitimate websites (e.g., changing the destination account in a banking transfer) to harvest credentials.
- **Man-in-the-Cloud:** Acquiring and reusing an OAuth token to access cloud services (e.g., Google Drive) unnoticed. Often worsened when tokens violate the principle of least privilege by granting overly broad access for extended periods.
- **Man-in-the-Mobile:** Bypassing two-factor authentication (2FA). Malware like *Zipmode* intercepts SMS MFA codes and forwards them continuously. AI agents are increasingly used to rapidly exploit these access points before the user realizes.

### 2.3 Man-in-the-Disk (MitD)
An often-overlooked vector where attackers target shared storage locations rather than network transit. If a location is unprotected, attackers can silently alter files before the legitimate application uses them.
- **Multi-user Temp Folders (`/tmp` in Linux):** If an application creates intermediate files here unsafely, an attacker can replace them or use *symbolic links* to trick the application into overwriting sensitive files (like the password file) or exporting sensitive data.
- **Desktop Apps & Steganography:** Documents temporarily stored on disk can be modified to include malicious macros or code hidden within figures (e.g., SVG or PDF execution layers).
- **Continuous Integration (CI) Pipelines:** If the shared file system of an automated CI/CD pipeline is accessible, attackers can swap legitimate artifacts for malicious ones midway through the build.
- **Log File Poisoning:** Attackers can inject crafted executable instructions into shared log files (like `/var/log`). Vulnerable downstream parsing tools may inadvertently execute this code when generating reports.
- **Temporary Installers:** Modifying installer components placed in a temp folder before the execution completes.
- **Network File Systems (SMB/NFS) & SQLite:** Swapping or altering SQLite database columns or roles before the database is initialized.
- **DLL Hijacking:** Placing a malicious DLL in a directory that a Windows application searches *before* it finds the legitimate system library.

> 📎 *Slide reference: `07b_Man-in-the-Disk-MitD-Vulnerability.pdf` — Storage vulnerabilities and MitD*

---

## 3. Mitigating Storage and Context Vulnerabilities

Investigators and system administrators can defend against MitD and similar attacks through defensive programming and system hardening:
- **Input Sanitization:** Strictly validating all user inputs to mitigate XSS and injection attacks.
- **Secure File Creation:** Using system calls like `mkstemp` (which creates temporary files atomically) or applying the `O_EXCL` flag when opening files to ensure exclusivity.
- **Strict Access Controls:** Configuring fine-grained permissions (e.g., `0600` in Linux) and Access Control Lists (ACLs) so that only authorized users can read/write specific storage points.
- **Atomic Operations:** Performing critical reads and writes without interruption to block race-condition exploits.
- **Integrity Checks:** Applying hash verification before and after file storage/transfer to spot silent modifications.

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Man-in-the-Disk (MitD)** | A class of attacks exploiting insecure, shared physical or networked storage (like `/tmp` folders) to modify files or insert malware before legitimate applications read them. |
| **ARP Poisoning** | A Layer-2 local network attack that sends forged unauthenticated ARP messages to associate the attacker's MAC address with a legitimate IP address, intercepting traffic. |
| **Cross-Site Scripting (XSS)** | An application-layer vulnerability where unsanitized user input allows an attacker to execute malicious client-side scripts, often used for HTTP session hijacking. |
| **Symbolic Link Attack** | Exploiting a program's insecure file writing in a shared folder by creating a symlink that redirects the program to inadvertently overwrite or reveal sensitive files. |
| **Atomic Operation** | A system operation that runs completely independently of any other processes and cannot be interrupted, crucial for avoiding race conditions in file handling. |

---

## Summary
- Forensic investigations rely heavily on the integrity of the environment; identifying potential node or network-level compromises is a fundamental first step.
- An attacker with root privileges can cleanly forge operating system calls and device drivers to conceal deeply embedded malware.
- The Man-in-the-Middle umbrella covers attacks intercepting data at various layers, from Layer 2 (ARP poisoning) to Application Layer (XSS session hijacking).
- Man-in-the-Cloud and Man-in-the-Mobile attack authentication tokens and MFA codes directly, bypassing initial perimeter security.
- Man-in-the-Disk leverages incorrectly configured shared storage (e.g., multi-user `/tmp` folders, CI pipelines, update installers) to manipulate files without directly attacking application memory.
- Effective countermeasures against these attacks involve meticulous input sanitization, atomic system operations, hash integrity checks, and enforced least-privilege configurations.
