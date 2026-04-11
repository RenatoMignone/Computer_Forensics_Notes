# Lecture 09 – Jurisdiction and the Cybercrime Convention
**Professor:** Vaciago
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Vaciago/2_Cybercrime_Convention.pdf`

---

## Overview
This lecture delves deeper into the complexities of jurisdiction in the digital age, comparing US and European approaches to digital evidence. It also heavily explores the Budapest Cybercrime Convention (Council of Europe, 2001), outlining the primary mutual assistance tools and highlighting why Article 32b severely compromised the treaty's ability to facilitate international cooperation.

---

## 1. Principles of Jurisdiction

### 1.1 The Four Main Principles
- **Territorial Principle:** The court in the place where the data is located has jurisdiction. In a democratic society, this is considered the most important and fundamental principle, despite the operational difficulties caused by the "loss of location" (e.g., cloud computing).
- **Nationality Principle:** Jurisdiction is established based on the nationality of the perpetrator.
- **Flag Principle:** Primarily used for airplanes and ships.
- **Power of Disposal Approach:** A newer principle asserting that jurisdiction is granted if the state has the availability (physical possession) of the device. From a legal standpoint, this principle is highly criticized because the value lies in the data, not the physical device. However, this approach provides the necessary legal justification for hacking a computer to obtain evidence across borders.

> 📎 *Slide reference: `2_Cybercrime_Convention.pdf` — Jurisdiction*

### 1.2 US vs. Europe Investigation Cultures
- **European/Italian Model:** Relies heavily on the judiciary system, conducting formal wiretapping (intercettazioni) authorized by a judge. This ensures transparency, giving citizens the right to know what investigations are being conducted regarding their data.
- **US Model:** Formally respects the territorial principle and has practical advantages as most data resides within US companies. Crucially, it employs a culture of agency (e.g., CIA, NSA) conducting secret investigations for national security, often operating outside the transparent judiciary system.

---

## 2. Presentation of Evidence in Court

### 2.1 The Challenge of Scientific Evidence
- 90–95% of judges lack the technical background to independently understand digital forensics concepts (e.g., in cases like the Garlasco timeline or IT incident root cause analyses).
- Experts bear an ethical responsibility. Presenting the evidence poorly strips the judge of the ability to make an informed decision, forcing them to rely merely on the concluding "yes or no" of the report.

### 2.2 Role of AI and Rehearsal
- **Rehearsal:** A technique learned from the US system where experts participate in trial simulations to prepare their delivery and extract the right points for the judge.
- **Artificial Intelligence:** Generative AI allows experts to simplify complex concepts or use role-playing to practice. AI can also create visual reconstructions (e.g., deepfakes or 3D simulations) to persuade the judge. However, this power also introduces the risk of manipulating court decisions.

---

## 3. The Budapest Cybercrime Convention (2001)

### 3.1 Background and Council of Europe
- **Council of Europe:** Unrelated to the European Union, the Council (based in Strasbourg) can create conventions inviting non-European countries, with the goal of creating rules adopted globally.
- **The Budapest Convention:** Adopted by the Committee of Ministers in Nov 2001. Though proposed before the cloud computing revolution, it aimed to harmonize national laws, improve investigative techniques, and increase international cooperation regarding cybercrime.

> 📎 *Slide reference: `2_Cybercrime_Convention.pdf` — Purpose of the Convention*

### 3.2 Key Investigative Tools and Articles
Various articles attempt to streamline the sharing of evidence between parties, bypassing traditional, slow "rogatory" procedures (which require moving from judicial to executive powers like the Minister of Justice):
- **Mutual Legal Assistance Treaty (MLAT):** Simplifies the process of evidence exchange compared to a traditional international rogatory procedure.
- **Article 16 - Expedited Preservation of Stored Computer Data:** Authorities can mandate a provider to preserve specific vulnerable data for up to 90 days. This is critical because normal retention policies (e.g., US providers) often delete data after 6 months.
- **Article 17:** Expedited preservation of traffic data.
- **Article 18 - Production Order:** Requires a person or service provider to submit specified computer data or subscriber information. (Subscriber information refers to registration details like name, phone, email, not browsing history or IP addresses).
- **Article 19 - Search and Seizure:** Empowers authorities to search and seize computer data.
- **Real-Time Data (Articles 20 & 21):** The capacity to collect traffic data and intercept content data in real time.

> 📎 *Slide reference: `2_Cybercrime_Convention.pdf` — Mutual Assistance Provisions*

### 3.3 The Russian Intervention and Article 32b
- **China:** Abandoned the Budapest negotiations early to maintain complete control ("balkanization") over its web jurisdiction.
- **Russia:** Stayed in the negotiations to alter a key article before ultimately refusing to ratify the convention.
- **Article 32a:** Allows a party to access openly available data (e.g., public social media posts) located in another state without authorization.
- **Article 32b (The Fatal Flaw):** Allows a state to access data located in another party's territory only if it obtains the "lawful and voluntary consent" of the person who has the lawful authority to disclose the data (the service provider).
  - The insertion of the word **"voluntary"** by the Russian delegation means providers (like Meta or Google) can legally refuse to cooperate based on their own corporate guidelines or ethical decisions.
  - This effectively destroyed the binding power of the convention, leaving law enforcement frustrated and increasingly pushing prosecutors toward state-sponsored "legal hacking" to acquire evidence when providers do not voluntarily cooperate.

> 📎 *Slide reference: `2_Cybercrime_Convention.pdf` — Article 32*

---

## 4. Unintended Consequences of the Digital Age

### 4.1 Defamation and the "Omnipotent System"
- Moving from a "synopticum" (television: many watch the few) to an omnipotent system (many watch the many).
- Reputation is now a critical, fragile asset. Due to the internet, defamation charges in Italy grew phenomenally (e.g., from 500 cases in 1995 to roughly 500,000 cases today).

### 4.2 EU Level Directives
- To counter the failures of MLATs and Article 32b, the EU established new regulations in 2023 for exchanging digital evidence. This works well purely within European borders but fails to solve the broader issue that mostly the requested data resides with US companies.

---

## Key Concepts & Definitions
| Term | Definition |
|------|------------|
| **Power of Disposal Approach** | The legal principle granting jurisdiction over digital data based on physical possession of the device, often used to justify legal hacking. |
| **Rogatory Procedure (Rogatoria)** | The traditional, time-consuming process of requesting evidence across international borders, requiring the involvement of both nations' executive branches (Ministers of Justice). |
| **MLAT** | Mutual Legal Assistance Treaty; a framework that attempts to expedite international evidence requests compared to traditional rogatory channels. |
| **Subscriber Information** | Data provided during registration (name, phone, billing), distinct from traffic data or browsing history. |
| **Balkanization** | The fragmentation of the global open internet into localized, state-controlled networks (e.g., China's approach). |
| **Article 32b** | A clause in the Budapest Convention allowing cross-border data access only with the "voluntary" consent of the service provider, crippling the treaty's enforcement power. |

---

## Summary
- The territorial principle is ideal but struggled to adapt to the cloud, giving rise to the flawed but necessary "power of disposal" approach to justify legal hacking.
- Experts fail their ethical duty if they do not adequately present scientific evidence to judges, a challenge increasingly aided or complicated by AI and technical rehearsal.
- The 2001 Budapest Convention aimed to harmonize global cybercrime laws and establish rapid evidence-sharing mechanisms (like 90-day data preservation).
- Introducing the word "voluntary" into Article 32b gave tech providers the ultimate power to deny data requests, fundamentally fracturing the convention's purpose.
- Frustrated by slow MLATs and uncooperative providers, law enforcement has increasingly resorted to infecting devices with malware to bypass physical jurisdiction.
- Within the EU, recent 2023 regulations improved local evidence exchange, but acquiring data from dominant US-based tech companies remains the field's foremost hurdle.
