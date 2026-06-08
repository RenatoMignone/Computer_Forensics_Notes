# Chapter 07 – TechMed: Corporate Forensics, Data Breach, and Criminal Liability
**Professor:** Vaciago  
**Reference Slides:** [`Slides/Vaciago/07_TechMed_Forensics_Law.pdf`](../../Slides/Vaciago/07_TechMed_Forensics_Law.pdf)  
**Covered in Lectures:** [Lecture 32](../../Lectures_MD/Lecture_32_Vaciago.md)

---

## Introduction

The TechMed chapter collects Vaciago's final laboratory on corporate forensics. The case combines malware infection, command-and-control exfiltration, business email compromise, GDPR breach handling, criminal-law classification, and organisational remediation.

The chapter is practical: students are expected to reconstruct evidence, respect forensic order, identify legal issues, and propose proportionate controls for a company of TechMed's size.

---

## 1. Corporate Forensics Context

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — Corporate forensics laboratory*

Corporate forensics is digital-forensics work performed inside a company, often before any trial exists. Most such analyses remain internal, but the examiner must still preserve evidence as if it may later support a criminal complaint, labour dispute, civil claim, or regulatory notification.

Vaciago warns that company urgency and cost pressure do not justify skipping procedure.

---

## 2. Labour-Law and Employee-Control Limits

The lecture stresses a recurring corporate mistake: the company may own the device, but it does not automatically own or freely control every item of employee data on it.

Italian employee-monitoring rules limit how employers can inspect devices, communications, and behaviour. The examiner must respect legal procedure, especially when the CEO asks for immediate access to employee email or activity traces.

AI-enabled monitoring makes this issue more sensitive because it allows broad, automatic control of employee activity.

---

## 3. TechMed Case

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — The case*

TechMed S.r.l. has:
- 85 employees;
- hospital and clinic clients;
- patient-management software;
- employee HR records;
- a cloud testing database containing patient-related data;
- Windows Active Directory and Exchange 2019;
- a Fortinet FortiGate firewall;
- Windows Defender antivirus.

The main people are the CEO, IT manager, finance manager, and DPO.

---

## 4. Incident Timeline

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — Timeline*

| Time | Event |
|------|-------|
| 15/04 08:45 | Phishing email sent to Giovanni Martini. |
| 15/04 08:50 | Martini opens `Payroll_Form_2026.docx`; malware installs. |
| 15/04 08:52 | First C2 connection; 450 KB exfiltrated. |
| 15/04 09:15 | Second C2 connection; 12.3 MB exfiltrated. |
| 15/04 10:30 | Finance manager receives spoofed CEO email requesting EUR 95,000 transfer. |
| 15/04 11:15 | Transfer authorized. |
| 16/04 09:00 | CEO denies sending the email. |
| 16/04 10:00 | IT manager discovers exfiltration. |
| 16/04 14:30 | DPO informed. |
| 16/04 15:00 | Workstation isolated without shutdown; forensic company engaged. |
| 17/04 09:00 | Disk image, RAM dump, firewall logs, and email logs acquired. |
| 18/04 | Criminal complaint filed in Turin. |

---

## 5. Evidence Collection Priority

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — Digital evidence collection*

| Priority | Evidence | Reason |
|----------|----------|--------|
| 1 | RAM dump | Highest volatility; may contain active processes, C2 connections, keys, and malware traces. |
| 2 | Disk image | Workstation is isolated but still running; acquire a bit-for-bit image and preserve hashes. |
| 3 | Firewall logs | Essential for exfiltration reconstruction and C2 timing. |
| 4 | Email server logs | Needed for phishing, spoofing, headers, and message tracking. |

Integrity should be verified with strong hashes such as SHA-256, and acquisition must be documented in the chain of custody.

---

## 6. Exfiltration and Malware Artifacts

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — Firewall log analysis and infection chain*

The 450 KB transfer is consistent with credentials, employee email lists, or system configuration. The 12.3 MB transfer is consistent with HR documents such as ID card copies and employment contracts.

Artifacts to look for include:
- Prefetch entries for Microsoft Word;
- the opened `Payroll_Form_2026.docx`;
- dropped payloads under user profile paths;
- `$MFT` timestamps;
- persistence keys under Windows `Run` locations;
- Windows Event Logs or Sysmon events for process creation, DLL loading, and network connections;
- email headers and message tracking logs;
- firewall logs showing outbound connections to the C2 address.

Windows Defender may have failed because the malware was polymorphic, obfuscated, or previously unknown. Vaciago connects this to the need for EDR and behavioural detection.

---

## 7. Criminal and GDPR Analysis

The laboratory asks students to analyze unauthorized access and fraud. For **Article 615-ter c.p.**, relevant facts include credential theft, access to protected company systems, and targeted exfiltration.

For the fraudulent transfer, Vaciago asks students to read the criminal-code provision carefully and decide whether the facts truly satisfy computer fraud or whether another fraud classification is more precise.

The GDPR analysis focuses on the moment of awareness. In the case, the IT manager discovers exfiltration on 16 April at 10:00, while the DPO is informed at 14:30. Notification timing and communication to data subjects depend on that awareness and on risk level.

---

## 8. Organisational Failures and Remedies

> 📎 *Slide reference: `07_TechMed_Forensics_Law.pdf` — Organisational failures and remedies*

| Failure | Fact | Remedy |
|---------|------|--------|
| No SPF/DKIM/DMARC | CEO spoofing succeeded. | Deploy SPF, DKIM, and DMARC with a reject policy. |
| No payment verification | EUR 95,000 transfer approved by email alone. | Require verbal confirmation for transfers above EUR 50,000. |
| Insufficient antivirus | Defender did not stop the malware. | Deploy EDR with behavioural analysis. |
| Lack of anti-phishing training | User opened suspicious attachment. | Run phishing simulations and mandatory awareness training. |

The remediation analysis must be proportionate to TechMed's size and risk profile.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Corporate Forensics** | Internal forensic work performed for an organisation, often before any litigation exists. |
| **Business Email Compromise** | Fraud where an attacker impersonates a trusted business actor to induce payment. |
| **SPF** | DNS-based control listing servers authorized to send mail for a domain. |
| **DKIM** | Cryptographic signature mechanism for email authenticity and integrity. |
| **DMARC** | Policy layer that combines SPF and DKIM and tells receivers how to handle failures. |
| **EDR** | Endpoint Detection and Response, using behavioural monitoring and response capabilities. |
| **Moment of Awareness** | GDPR breach-analysis point from which notification timing is assessed. |

---

## Summary
- TechMed is a corporate-forensics laboratory combining technical, legal, and organisational analysis.
- Corporate urgency does not remove forensic and labour-law constraints.
- Evidence collection prioritizes RAM, disk image, firewall logs, then email logs.
- Firewall volumes support inference about likely exfiltrated content.
- Malware artifacts include Prefetch, dropped payloads, persistence keys, `$MFT`, Event Logs, Sysmon, headers, and firewall logs.
- The legal analysis covers unauthorized access, fraud classification, and GDPR notification timing.
- SPF, DKIM, DMARC, EDR, phishing training, and payment-verification procedures are the key remedies.
