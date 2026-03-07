# Digital Forensics Case Study – Insider IP Exfiltration
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/Digital-Forensics-Case-Study.pdf`]  
**Covered in Lectures:** Lecture 5

---

## Introduction
This case study applies the five forensic investigation phases to a realistic scenario: an insider threat at a technology company involving intellectual property (IP) exfiltration. It is designed to show how the abstract procedures described in [03_investigation_phases.md](03_investigation_phases.md) and [03b_Forensic-USB-Drive-Acquisition.md](03b_Forensic-USB-Drive-Acquisition.md) translate into concrete investigative steps, decisions, and outcomes.

---

## Scenario Setup

**Organisation**: A mid-sized software development company (approx. 350 employees).  
**Incident trigger**: The IT security team detects an anomalously large transfer of files from an internal R&D file server to a personal email account.  
**Suspect**: A senior software engineer (referred to as Subject A) who has announced resignation and is serving their notice period.  
**Scope of potential theft**: Proprietary source code, design specifications, and unreleased product roadmap documents.  
**Regulatory context**: The company is subject to standard IP law; no special sector-specific regulation (not healthcare, not finance, not government).

---

## Phase 1: Identification

### Initial Alert
The **corporate IT monitoring** system flagged:
- Outbound email from Subject A's corporate account to a Gmail address containing a 240 MB ZIP attachment
- The ZIP was attached at 22:47 on a Tuesday — outside normal working hours
- Subject A's access badge records show they were **not in the building** at that time — the email was sent remotely via VPN

### OSINT Reconnaissance
Before any device seizure:
- **LinkedIn**: Subject A's profile updated with a new employer — a direct competitor — effective the following Monday
- **Pastebin / GitHub search (passive)**: No public postings of suspected stolen code identified, but the investigation notes this as a persistent monitoring objective
- **Internal HR records**: Subject A submitted formal resignation 3 weeks prior; standard practice for departing employees should have included access restriction — this had not been applied

### Endpoint and Infrastructure Review
- **Email server logs**: Confirm the outbound message, its size, recipient, and timestamp
- **VPN logs**: Confirm Subject A authenticated via VPN at 22:35 using a corporate laptop (asset tag recorded)
- **Windows Event Logs on the corporate laptop**: Show the laptop was active from 22:35; `Security` log records user authentication; `PowerShell` log shows a script was run at 22:41
- **`usbstor` registry key** (Windows USB device history): Records that a USB drive with a specific device serial number was inserted into the corporate laptop at **08:15 two days prior**, on the day Subject A had an in-person meeting to begin handover

### Scope Definition
The legal team confirms the investigation scope includes:
- Subject A's **corporate laptop** (company-owned asset; employee agreement covers forensic inspection)
- **Email server logs** (infrastructure asset)
- **VPN logs** (infrastructure asset)
- Subject A's **corporate email account** contents
- The USB drive, if it can be located and seized with appropriate authority

---

## Phase 2: Collection

### Isolation
- Subject A's **VPN access is revoked** remotely to prevent further access
- The **corporate email account is suspended** and its content archived under legal hold
- IT confirms the **corporate laptop is currently in Subject A's possession** at home — a seizure must be arranged

### Seizure and Physical Collection
- Legal counsel confirms that the employee agreement and company property policy provide the basis for demanding return of the corporate laptop before end of notice period
- Subject A is contacted; the laptop is returned to the HR manager the following morning
- **Before collection**: IT security photographs the laptop in the HR manager's office; the laptop is in sleep mode with the lid closed
- **Decision on power state**: Rather than forcing a cold shutdown, the investigation team decides to perform **live acquisition** because BitLocker **full-disk encryption** is active and the laptop is in a BitLocker-unlocked sleep state from which the Volume Master Key (VMK) may be recoverable from RAM

### Chain of Custody Initiated
A formal chain of custody record is started:
- Item 001: Corporate laptop, asset tag LP-0342, Make/Model Dell Latitude 7420, Serial No. [recorded]
- Condition: Lid closed, sleep indicator light active, battery partially charged
- Date/time of collection: [recorded]
- Collected by: Senior forensic examiner; witnessed by HR Director

---

## Phase 3: Acquisition

### RAM Acquisition (Live)
- The laptop lid is opened; the screen resumes without requesting a BitLocker PIN (indicating the VMK is loaded in memory)
- The forensic examiner plugs a **forensic USB drive** (containing the investigator's trusted Linux live environment and static binaries) into the USB port
- A live RAM dump is captured using a trusted acquisition tool run from the forensic USB drive, written to the forensic destination drive
- The RAM dump is completed and its SHA-256 hash is recorded

### Disk Acquisition
- After RAM capture, the laptop is **shut down using the Windows shutdown command** (not a forced power-off, to allow the OS to complete the clean shutdown sequence)
- The BitLocker VMK, identified within the RAM dump during forensic RAM analysis, is extracted and documented
- The SSD is removed from the laptop; a **hardware write blocker is attached**; `dc3dd` is used to image the encrypted SSD:

```bash
dc3dd if=/dev/sdb hof=/media/forensic_drive/LP0342_disk.dd \
  hash=sha256 hash=sha512 \
  log=/media/forensic_drive/LP0342_acquisition_log.txt \
  verb=on
```

- Pre- and post-acquisition hashes are recorded; Source pre-hash and image post-hash confirmed to match
- SSD sealed in tamper-evident bag; hash recorded on bag label

### Infrastructure Log Preservation
- Email server logs and VPN logs are exported by the IT team and provided to the forensic examiner in read-only format
- SHA-256 hashes of both log exports are computed and recorded
- Copies are placed under the same chain of custody as the physical device

---

## Phase 4: Examination and Analysis

### BitLocker Decryption
- The BitLocker VMK is used to decrypt the SSD image, which is then mounted read-only for examination with `Autopsy`

### File System Examination

**Key artefacts identified:**

| Artefact | Location | Finding |
|---------|---------|---------|
| PowerShell history | `C:\Users\SubjectA\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt` | Contains commands that enumerate R&D share contents, copy files to a local staging directory, and compress the staging directory into a ZIP |
| Staging directory | `C:\Users\SubjectA\Documents\HandoverDocs\` | Directory created 2 days before resignation; MFT record shows it contained 847 files over 230 MB; directory contents deleted after email was sent |
| MFT entry for deleted staging directory | MFT journal (NTFS change journal) | Full record of file creation, modification, and deletion in the staging directory; files recovered from unallocated clusters |
| Email client artefacts | Outlook `.pst` file | Shows the outbound email with attachment composed at 22:42, sent at 22:47 |
| ZIP file | Recovered from unallocated clusters via `Autopsy` | Contents match the R&D source code repository structure; 847 source files, build configurations, design specs |

### USB Device Examination
- The `usbstor` registry entry identifies the USB by device serial number
- A warrant is prepared to compel Subject A to produce the USB device

### Portal and Remote Access Correlation
- VPN log timestamp (22:35) → PowerShell command execution (22:41) → email composition (22:42) → email sent (22:47) → VPN disconnect (22:55)
- Timeline is **internally consistent** and cross-corroborated across three independent evidence sources (endpoint logs, VPN logs, email server logs)

### Clock Skew Check
- VPN server and corporate email server are both synchronised to the same NTP source — **no clock delta**
- Laptop clock is confirmed to match NTP time via Windows Time Service log — **clock skew: <1 second**

### Anti-Forensics Indicators
- **File deletion** of the staging directory was performed; files recovered from unallocated clusters — standard deletion does not securely erase
- **MFT journal** (NTFS change journal) was not cleared by the suspect — full file operation history preserved
- No evidence of timestamp manipulation detected

---

## Phase 5: Presentation

### Three-Version Report Structure

| Version | Audience | Focus |
|---------|---------|-------|
| **Technical Report** | IT security team, forensic reviewers | Full technical methodology; tool names and versions; raw hash values; command-line output excerpts; complete artefact list with file system paths |
| **Legal Brief Supplement** | Prosecution counsel; HR/legal department | Findings re-stated in terms of legal elements (access, intent, exfiltration, competitor link); technical detail in appendices; timeline diagram |
| Executive Summary | Board; CISO | Business impact (IP at risk); scope of data exfiltrated; current status (criminal referral made); recommended remediation (offboarding controls, IT monitoring, BitLocker key escrow) |

### Outcome
- The matter was referred to police on the basis of the forensic evidence
- Subject A's employment was terminated for cause during the notice period
- The company implemented immediate remediation: departing employees' access is now restricted to email-only during their notice period, with monitoring elevated

### Quality Assurance
- A second forensic examiner independently verified the timeline by re-examining the same forensic images and produced the same hash matches and artefact identifications
- All three report drafts were preserved; legal counsel confirmed conclusions were appropriately scoped

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Insider Threat** | Security risk originating from within the organisation — current or former employees, contractors, or partners with authorised access |
| **BitLocker VMK** | Volume Master Key — the symmetric encryption key that BitLocker uses to encrypt the drive; held in RAM while the drive is unlocked |
| **MFT Journal** | NTFS file system structure that records file and directory change operations; persists after deletion and is a primary anti-deletion artefact |
| **Staging Directory** | A temporary local directory used by the suspect to gather files before exfiltration; its creation and use is itself forensic evidence |
| **`usbstor` Registry Key** | Windows registry path that records every USB storage device ever connected, including device serial number and timestamps |
| **Legal Hold** | Preservation order directing that data be retained without modification or deletion pending litigation or investigation |

---

## Summary

- The case illustrates how **multiple independent evidence sources** (endpoint logs, VPN logs, email server logs, file system artefacts, registry entries) must be corroborated to build a credible forensic narrative.
- **Live acquisition** was the correct decision because BitLocker encryption made the disk unreadable after shutdown — the BitLocker VMK was only available while the device was in its live state.
- Standard **file deletion did not erase the evidence**: the MFT journal and unallocated cluster recovery provided a complete picture of the staging directory operations.
- The **timeline was internally consistent** across three independent evidence sources with negligible clock skew, making it robust against legal challenge.
- The **three-version report structure** (technical / legal / executive) is essential for ensuring findings are communicated appropriately to each stakeholder.
- **Remediation** (departing employee access controls, elevated IT monitoring, BitLocker key escrow) was derived directly from the investigation's findings — forensic investigations should always inform defensive improvements.
