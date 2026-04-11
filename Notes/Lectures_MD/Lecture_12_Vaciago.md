# Lecture 12 – Italian Law 48/2008 and Corporate Liability
**Professor:** Vaciago  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:** `Slides/Vaciago/3_Law_48_08.pdf`

---

## Overview
This lecture examines the Italian implementation of the Budapest Convention via **Law 48/2008**. It highlights the three-tier innovation of the law: international harmonization, the reorganization of specific cybercrime offenses (including the "domicile" concept in digital systems), and the extension of corporate criminal liability (Legislative Decree 231/2001) to include IT crimes.

---

## 1. Reorganization of Cybercrime Offenses

Law 48/2008 introduced or refined critical articles in the Italian Criminal Code to address the unique nature of digital evidence and systems.

### 1.1 Illegal Access to an IT System (Art. 615-ter)
The core principle is the **"Right to Exclude Others"** (*ius excludendi alios*).
- **Digital Domicile:** A digital system is treated like a physical home. Even if the "door" is left open (e.g., no password or a weak `1234` password), entering without authorization is a crime.
- **Inside Threats:** An employee who has legitimate access to a system but uses it for a purpose unauthorized by the company (e.g., an officer checking a cousin's tax revenue) commits illegal access. The highest courts have ruled that violating internal company policy/classification of data can lead to criminal liability.

### 1.2 Damage to IT Systems and Data (Art. 635-bis to quinquies)
- **Temporary Unavailability:** Unlike physical damage, digital "damage" includes temporary disruption. A **DDoS attack** or **ransomware** that makes data unavailable, even for a limited time, constitutes a crime.
- **Deletion by Employees:** Deleting personal data from a company device can be a crime if the company's internal policy forbids personal use. Deleting evidence of exfiltration using tools like **CCleaner** is treated as destructive intent, even if some data is later recoverable via forensic carving.

### 1.3 Integrity and Falsification
- **Integrity:** Since 2016, falsifying information in private communications (e.g., altering an email before forwarding it) has been largely decriminalized unless it is used to commit **fraud**.
- **Public vs. Private:** Falsifying documents for public institutions (e.g., university grades, public tenders) remains a serious crime (**Falsehood in Public Documents**).

---

## 2. Corporate Criminal Liability (Decree 231/2001)

Traditionally, "Societas delinquere non potes" (a corporation cannot commit a crime) was the rule. This changed with **Legislative Decree 231/2001**, which Law 48/2008 extended to cybercrimes.

### 2.1 The "Death" of the Company
If an employee or executive commits a crime for the **interest or benefit** of the company, the corporation itself faces sanctions:
- **Financial Fines:** Ranging from €1,500 to €1.5 million.
- **Interdictory Sanctions:** The company can be prohibited from operating for up to two years. This is often fatal for a business, as it stops all revenue and prevents paying salaries.

### 2.2 Compliance Programs (Modello 231)
Companies can avoid liability if they demonstrate **Accountability** through a "Compliance Program":
- The company must prove it had internal IT policies, data classification rules, and monitoring systems in place to prevent the crime.
- If an employee bypassed a robust compliance system, only the individual is held liable. This makes **IT Policy** design a critical junction between computer science and law.

---

## 3. Procedural Innovations and Cooperation

### 3.1 Centralization of Investigations
Because cybercrime is technically complex, Law 48/2008 centralized investigations at the **District Court of Appeal** level (e.g., Turin, Milan, Rome). This ensures that specialized units (like the Postal Police) and expert prosecutors handle these cases rather than smaller, local police stations.

### 3.2 Search and Seizure
- **Physical vs. Digital Seizure:** Investigators can physically seize hardware or, more commonly, perform a bitstream copy of the server.
- **Data Centers:** Law enforcement has the power to search and seize data within data centers (e.g., Aruba, AWS Italy), though they typically coordinate with the provider to avoid disrupting thousands of other innocent users.
- **Preservation Orders:** Data can be "frozen" at a provider for 90 days (expandable to 6 months) to prevent deletion before a formal MLAT request is fulfilled.

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Law 48/2008** | The Italian law that ratified the Budapest Convention and introduced digital forensics principles into the criminal procedural code. |
| **Art. 615-ter** | Italian Criminal Code article defining illegal access to an IT system; established the "digital domicile" principle. |
| **Decree 231/2001** | Legislation on the administrative liability of legal entities, allowing companies to be punished for crimes committed in their interest. |
| **Compliance Program** | An internal organizational model (Modello 231) that a company implements to mitigate the risk of crimes and avoid corporate liability. |
| **Bitstream Copy** | A forensic image that captures every bit of a storage device, ensuring the integrity and authenticity of the digital evidence. |

---

## Summary
- Law 48/2008 bridged a 7-year gap between the Budapest Convention and Italian law, modernizing the legal system for the digital age.
- Illegal access is defined by the "intent to exclude," meaning even public-facing systems without passwords can be "violated" if entry is unauthorized.
- Modern "digital damage" includes temporary unavailability and the unauthorized deletion of data from company assets.
- Companies are no longer immune to the crimes of their employees; they must implement thorough "Compliance Programs" involving IT policies and data security.
- Investigations are centralized in specialized district units to ensure technical competence.
- Procedural rules now mandate that digital evidence be acquired without alteration, primarily through hashing and verified bitstream copies.
- International cooperation is streamlined through MLATs and Interpol, though Article 32b remains a hurdle for mandatory cross-border data production.
