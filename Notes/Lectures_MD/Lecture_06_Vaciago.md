# Lecture 6 – Legal Frameworks: Data Retention, Jurisdiction & Digital Evidence
**Professor:** Vaciago  
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)  
**Reference Slides:**  
- `Slides/Vaciago/1_Definition.pdf`  
- `Slides/Vaciago/2_Cybercrime_Convention.pdf`

---

## Overview
This lecture resumes the legal perspective on digital forensics introduced in Lecture 3. It covers **international and national forensic standards**, explores how suspects are **identified through digital traces** (with emphasis on data retention obligations and OSINT), and examines the **jurisdiction problem** arising when data is stored across national borders. The lecture also compares US and EU/Italian investigative models and discusses the erosion of the IP address as reliable evidence.

---

## 1. Recap & Standards Context

### Three Forensics Domains (Review from Lecture 3)
Digital forensics operates across three distinct legal contexts:

| Domain | Legal Framework | Typical Actor |
|--------|----------------|---------------|
| **Criminal forensics** | Criminal procedural law; state-led prosecution | Police, prosecutors, court-appointed experts |
| **Civil forensics** | Civil litigation; burden of proof on claimant | Private forensic experts, court-appointed consultants |
| **Corporate / incident response** | Internal investigation; labour law; compliance | Corporate security teams, external consultants |

Each domain has different evidence admissibility standards, privacy constraints, and investigative powers.

### Forensic Standards

| Standard | Origin | Scope |
|----------|--------|-------|
| **ISO/IEC 27037** | International | Identification, collection, acquisition, and preservation of digital evidence |
| **ISO/IEC 27001** | International | Information security management system (ISMS) standard; compulsory for cybersecurity compliance activities |
| **NIST SP 800-86** | US (freely accessible) | Guide to integrating forensic techniques into incident response; preferred in US practice |
| **ACPO Guidelines** | UK | Historically influential; principled approach to evidence handling |

**Standardisation challenge**: because digital forensics intersects with both criminal law and computer science — which are themselves moving rapidly — achieving a single universally accepted standard is extremely difficult. Different jurisdictions, courts, and organisations apply different frameworks.

> 📎 *Slide reference: `Slides/Vaciago/1_Definition.pdf`*

---

## 2. Identifying a Suspect

Before acquiring and examining evidence, investigators must identify the suspect. This involves tracing **digital identifiers** back to a physical person.

### 2.1 OSINT and Suspect Identification

**OSINT** (Open Source Intelligence) can reveal significant information about a suspect from publicly available sources — social media profiles, public registration records, and other open data.

**Legality of OSINT**: collecting publicly available information is generally lawful in Italy and most EU jurisdictions. However, investigators must be aware of the legal limits, particularly where any form of interaction with sources or systems the subject controls may require formal authorisation.

### 2.2 IP Addresses and ISP Data

The most common initial identifier in a cybercrime investigation is an **IP address**, which must then be traced to a subscriber:

**Step 1**: Collect the IP address and timestamp from the victim system's logs  
**Step 2**: Determine which ISP/operator owns that IP block (RIPE/ARIN/APNIC WHOIS)  
**Step 3**: Submit a formal **legal request** (court order or warrant) to the ISP to identify the subscriber associated with that IP at that time  
**Step 4**: The ISP provides subscriber identity from its **data retention records**

**Italian legal framework**: obtaining IP address data from a network or hosting provider requires the authorisation of both a prosecutor and a judge, pursuant to **Article 132 of Legislative Decree 196/2003** (the Privacy Code), and is only available for serious crimes.

> 📎 *Slide reference: `Slides/Vaciago/1_Definition.pdf`*

---

## 3. Data Retention

**Data retention** is the legal obligation imposed on network and internet service providers to store certain traffic data for a prescribed period so that it can be provided to law enforcement upon request.

### 3.1 Historical Origins

Data retention law has roots in the **post-9/11 counterterrorism response**:
- The US established extensive data retention requirements following the 2001 attacks
- The **EU Data Retention Directive (2006/24/EC)** followed, requiring member states to implement data retention obligations for electronic communications providers

The core requirement: providers must store **who communicated with whom, when, from where, and for how long** — not the content of communications.

### 3.2 Who Is Obligated?

The obligation applies differently depending on the type of provider.  
**Key distinction — three provider types:**

| Provider Type | Description | Example |
|---------------|-------------|---------|
| **Network/Access provider** | Provides physical/logical access to the internet via infrastructure | Telecom Italia (TIM), Vodafone, mobile operators |
| **Internet Service Provider (ISP) / Application layer** | Provides internet-based services (email, websites) | Gmail, Outlook, web hosting companies |
| **Hosting provider** | Stores or hosts data on behalf of third parties | AWS, Google Cloud, OVH |

**Important note**: a single company may occupy multiple roles (e.g., TIM provides both physical access and email hosting).

**What network/access providers must retain:**
- All **IP addresses** assigned to subscribers
- Source and destination IP addresses for all connections (in some jurisdictions)
- **Start and end timestamps** of each connection/session

### 3.3 Retention Periods Across Jurisdictions

| Jurisdiction | Required Retention Period |
|--------------|--------------------------|
| **EU minimum (2006/24/EC)** | 6 months |
| **EU maximum (2006/24/EC)** | 24 months |
| **Italy** | Up to **5 years** (one of the longest in the world) |
| **Germany** | Directive declared **unconstitutional** |
| **Ireland** | Directive declared **unconstitutional** |
| **Romania** | Directive declared **unconstitutional** |

Italy's 5-year retention period is exceptional: investigators can, in theory, obtain **5 years of connection history** for a given subscriber — who connected to what, when, for how long.

### 3.4 The Freezing Procedure

When investigators identify a device/IP involved in an offence early in an investigation:
1. A **formal freezing request** is submitted immediately to the provider (before the data retention period expires)
2. The provider is ordered to **immediately preserve** the data pending a formal warrant
3. The formal warrant is then obtained (which may take longer than the data retention period would allow)

Without freezing, data that lies just within the retention window may be deleted before the warrant arrives.

### 3.5 The 2012 Interpol and Tor Problem

The **Tor anonymisation network** (and similar tools) fundamentally undermines the reliability of IP addresses as evidence:
- Tor routing passes traffic through multiple relays in multiple countries, masking the originating IP
- The **exit node's IP** is what the victim's server sees — this may be a volunteer's connection in a different country
- Following the growing prevalence of Tor, a **2012 Convention** (referenced in the lecture as an Interpol-level agreement) effectively acknowledged the **technical impossibility** of consistently tracing IP addresses to individuals when anonymisation tools are used

**Consequence**: IP address alone has been significantly **devalued as evidence** in many jurisdictions. A successful prosecution built on IP address alone is increasingly untenable.

### 3.6 The Identity-Verified Internet Debate

A recurring policy debate follows from this:
> *"Should all internet access require identity verification — as physical access to a country requires a passport?"*

**For**:
- Eliminates anonymous cybercrime
- Enables reliable attribution

**Against**:
- Destroys anonymous dissent and whistleblowing (critical in authoritarian contexts)
- Privacy rights
- Technically difficult to enforce at scale

The debate has not been resolved; most democracies have not moved in this direction.

> 📎 *Slide reference: `Slides/Vaciago/2_Cybercrime_Convention.pdf`*

---

## 4. Jurisdiction – The Cross-Border Problem

### 4.1 The Core Tension

Digital evidence is frequently stored in a **different country** from the one where the crime occurred or where the victim is located. This creates a **jurisdictional gap**: the investigating authorities of Country A cannot unilaterally compel providers in Country B to disclose data.

### 4.2 GDPR and Big Tech

Prior to GDPR (2018), major US technology companies (Google, Meta, etc.) processed EU users' data under **US law**:
- Data of EU residents stored in US data centres
- Requests for that data governed by **US law** (a different legal regime from EU law)

**GDPR's response** (indirect): under GDPR, companies established entities in Ireland (within the EU) — **Google Ireland, Meta Platforms Ireland** — as the data controllers for EU users' data.

**What this achieved — very little:**
- Google Ireland is a wholly owned subsidiary of **Google LLC (US)**
- US law still applies at the parent company level
- US law gives its law enforcement authorities the ability to compel US companies to produce data stored anywhere in the world, including data of EU users held by European subsidiaries

**Ireland's position**: Ireland declared the EU Data Retention Directive unconstitutional domestically. However, this does not prevent US law from reaching Google Ireland's data via the US parent company.

> 📎 *Slide reference: `Slides/Vaciago/2_Cybercrime_Convention.pdf`*

### 4.3 Freedom of Speech: US vs Italy

A concrete consequence of US-EU jurisdiction divergence:

| Jurisdiction | Defamation | Legal treatment |
|--------------|------------|----------------|
| **Italy** | Criminal offence | Article 595 of the Italian Penal Code; punishable with imprisonment |
| **USA** | Generally a **civil** matter | First Amendment protects freedom of speech broadly; criminal defamation is rare and narrow |

**Practical implication**: when an Italian is defamed on Google, Facebook, or YouTube:
- The content is hosted by a US company governed primarily by US law
- Under US law, the content may be **entirely lawful** (protected speech)
- Italian authorities may request removal but the company may decline
- Cross-border enforcement is slow and complex

### 4.4 Transparency Reports

Major platforms publish **transparency reports** disclosing how they respond to government requests:

**Google** (as representative example):
- Receives **over 1 million government requests per year** globally
- The vast majority of requests relate to **freedom of speech** (content removal) rather than criminal investigation
- Compliance rates vary significantly by request type and jurisdiction

**The policy spectrum** for platform cooperation:
- **Meta (Facebook/Instagram)**: generally cooperative with law enforcement; detailed transparency reports
- **X (formerly Twitter)**: significantly reduced cooperation with law enforcement after a change in ownership; reduced trust and safety team; transparency reports show declining compliance
- **Telegram**: operated under a strong non-cooperation policy; CEO Pavel Durov was **arrested in France** in 2024, which led to a policy shift toward greater cooperation with authorities

### 4.5 The China/Yahoo Case (2005–2008)

A landmark case in the tension between platform cooperation and human rights:
- **Yahoo** had operations in China and stored email data of Chinese users within China
- Chinese authorities demanded the IP addresses and account information of **political bloggers** who had posted critically about the government
- Yahoo complied under Chinese law
- Chinese authorities **identified, prosecuted, and in some cases executed** the bloggers
- The case triggered global debate about the responsibility of technology companies operating in authoritarian jurisdictions
- **Google** subsequently declined to continue operating a censored version of its search engine in China (`google.cn`) and withdrew from the Chinese market

---

### 4.6 The Four Jurisdiction Principles

> ⚠️ *Prof. Vaciago explicitly flagged these four principles as exam content.*

When digital evidence is located outside the investigating authority's borders, the applicable legal principle determines which country's courts have authority:

| Principle | Definition | Notes |
|-----------|-----------|-------|
| **Territorial** | Jurisdiction of the country where the data is physically located — or, in a more generous interpretation, where the managing company is incorporated | Most common principle; undermined by cloud computing, where data moves and replicates across jurisdictions |
| **Nationality** | Criminal jurisdiction follows the nationality of the perpetrator | Creates conflicts when perpetrator's and victim's nationalities differ; generally applied as a secondary principle |
| **Flag** | On aircraft or ships, the law of the flag state applies regardless of geographic position | Limited to those specific physical contexts |
| **Power of disposal** | If a device is physically present in the investigating country, authorities can access data on it regardless of where that data is actually hosted | Controversial: some jurisdictions use this to justify hacking a suspect's device even when the data resides on servers abroad; Vaciago describes it as dubious from a fundamental legal standpoint |

> *In practice, when traditional cooperation methods (requests to providers, formal cross-border legal cooperation) fail, investigators sometimes assert the power of disposal approach to justify accessing data via the suspect's device — bypassing the usual provider route entirely.*

> 📎 *Slide reference: `Slides/Vaciago/2_Cybercrime_Convention.pdf` — Jurisdiction Principles*

---

### 4.7 Emergency Disclosure Procedure

For situations involving **imminent risk to life**, major platforms operate a **24/7 Emergency Disclosure Procedure (EDP)**:
- Allows law enforcement to receive data without a formal court order when there is an immediate, credible risk to life (terrorism, kidnapping)
- Available even from platforms that do not routinely cooperate with government requests
- The platform evaluates the request and determines whether the emergency threshold is met
- Requires precise articulation of the emergency: a generic claim that "a person may be in danger" is not sufficient; specific facts and a credible timeframe must be provided

> *Vaciago worked directly on these procedures with Google from 2007 to 2014, facilitating law enforcement requests from multiple countries. He noted that for major crimes (terrorism, kidnapping where life is at risk within hours) this mechanism works. For lesser crimes (ransomware, fraud, defamation), it does not apply.*

> 📎 *Slide reference: `Slides/Vaciago/2_Cybercrime_Convention.pdf` — Emergency Disclosure*

---

## 5. Digital Evidence Location – A Practical Model

When beginning an investigation, evidence is most likely to be found in the following locations, ordered from most accessible to hardest to obtain:

```
[ Level 1 ] Suspect's personal computer / workstation
     ↓
[ Level 2 ] Suspect's mobile device(s)
     ↓
[ Level 3 ] ISP / Network provider logs (data retention)
            Bank accounts + digital payment providers (Stripe, PayPal, etc.)
            → "follow the money" applies here
     ↓
[ Level 4 ] Cloud-hosted data (Google Drive, iCloud, OneDrive, etc.)
```

Each level requires a progressively more complex legal process (search warrant → domestic court order → formal cross-border legal cooperation or compelled production via the US parent company chain).

> *Note: 90% of data ownership is concentrated in US companies. The jurisdiction of the legal entity that owns the data determines the rules that apply.*

> 📎 *Slide reference: `Slides/Vaciago/1_Definition.pdf`*

---

## 6. Mobile Forensics

Mobile devices present unique forensic challenges:
- **Full-disk encryption** is on by default on modern iOS and Android devices
- Remote wipe capability is standard (Faraday bag required — see Lecture 4)
- Multiple connectivity interfaces (BlueTooth, WiFi, cellular, NFC) must all be blocked
- Internal flash storage architecture differs from conventional hard drives

### UFED (Universal Forensic Extraction Device)
**Cellebrite UFED** is the industry-leading mobile forensics tool:
- Hardware device + companion software
- Requires physical connection (and sometimes physically opening the device) for full extraction
- Continuously updated to support new phone models
- **Extremely expensive**: hardware kit, software licences, and update subscriptions
- Primarily used by law enforcement agencies

**Budget implication**: the high cost of mobile forensics tools (particularly UFED) means that only well-funded agencies or large corporate security teams can perform comprehensive mobile investigations.

---

## 7. US vs EU/Italian Investigation Models

### Compulsory vs Discretionary Prosecution

| Feature | European Union (Italy) | United States |
|---------|----------------------|---------------|
| **Prosecution model** | **Compulsory prosecution**: police/prosecutors *must* investigate any formally filed complaint | **Prosecutorial discretion**: the District Attorney may decline to investigate or prosecute based on likelihood of success, available resources, political factors |
| **Implication for forensics** | High volume of investigations; many small/medium-complexity cases require forensic analysis | Selective prosecution; DA focuses resources on high-value cases; private civil litigation heavy |
| **Digital forensics investment** | Moderate; constrained by state budgets | High; driven by both prosecution and deep-pocketed civil litigation |

**Prof. Vaciago's observation**: the US "pay-to-play" (highly adversarial, privately funded) legal system drives far larger investment in digital forensics capabilities than the Italian compulsory prosecution model, where state agencies have limited budgets.

**Secondary driver**: in the US, **civil litigation** (not just criminal prosecution) requires digital forensics extensively — e-discovery, intellectual property theft, employment disputes — creating a large and well-funded commercial forensics sector.

---

## 8. Key Mandatory Law, Remote Forensics, and the Encryption Problem

### The Password Compulsion Debate

The most direct solution to the encryption problem — legally compelling a suspect to reveal their password — is unconstitutional in democratic systems.

- **Right against self-incrimination**: a *suspected person* has the right not to cooperate with an investigation, including the right not to reveal encryption keys or passwords. This is the **Miranda principle** — the right to silence, the right not to be compelled to speak.
- **Boucher case (US/Canada)**: one of the most prominent legal battles over password compulsion. After prolonged proceedings across the two countries, the conclusion was that no democratic legal system can validly force a suspect to produce a decryption key.
- **Australia, Belgium, and France** each introduced mandatory key disclosure laws; all were ultimately declared unconstitutional.

> *Vaciago described a procedural workaround used in practice: inviting a suspect to attend informally as a "person informed of the facts" — effectively a witness, who must tell the truth — asking for passwords, and only formally charging them afterward. He described this as constitutionally impermissible but difficult to challenge once consent has been given.*

### Remote Forensics and State-Sponsored Hacking

With password compulsion ruled out, investigators turned to **remote forensics** — covertly installing spyware (Trojan/keylogger) on a suspect's device to gain access.

**German Constitutional Court (2008)**: The landmark decision on a **North Rhine-Westphalia (NordWestfalia)** law authorising covert hacking of suspects' computers. The Court declared it unconstitutional, recognising three violated rights:
1. Privacy of **correspondence**
2. Inviolability of the **home** (extended to digital spaces)
3. A newly articulated **right to informational self-determination** — specifically, the *right to confidentiality and integrity of information technology systems*

Despite this ruling, covert device access continued in Germany, Italy, and other countries via unofficial channels.

**Hacking Team / RCS Galileo**: Milan-based company *Hacking Team* was one of the world's most widely-used commercial producers of law enforcement spyware. Their product *RCS Galileo* was sold to law enforcement agencies globally. In **2015**, Hacking Team suffered a major data breach, exposing the full scale of state-sponsored hacking operations.

**Bossetti / Yara Gambirasio case**: The Carabinieri used Hacking Team's tools to covertly access the email account of Massimo Bossetti (defendant, ultimately convicted of the murder of Yara Gambirasio). His defence challenged whether the emails presented as prosecution evidence had been planted by investigators who had had unlogged covert access to the device — a challenge that highlights the fundamental forensic integrity problem of any remote forensics operation.

### Italian Remote Forensics Law (2017–2018)

Italy eventually legalised a limited form of remote forensics under wiretapping law:
- Law enforcement may covertly **activate a device's microphone and camera** for audio/video interception
- Authorised **only for organised crime investigations**
- Does **not** legally authorise reading emails, files, or other stored data — but once inside a device, technical access to everything is available

### Fruit of the Poisonous Tree

In common law systems (**US and UK**), evidence obtained in violation of a suspect's rights — and any evidence derived from it — is inadmissible under the **"fruit of the poisonous tree"** doctrine.

In civil law systems (**Italy and most of Europe**), the equivalent principle is weaker. Italian judges do not automatically exclude evidence because of procedural irregularities in its collection. A video proving guilt tends to be admitted even if obtained improperly — making admissibility challenges harder to sustain and far less central to the defence strategy.

> 📎 *Slide reference: `Slides/Vaciago/2_Cybercrime_Convention.pdf` — Remote Forensics & Key Mandatory Law*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Data retention** | Legal obligation on telecommunications/internet providers to retain traffic (metadata) data for a specified period |
| **EU Data Retention Directive (2006/24/EC)** | EU law requiring member states to mandate 6–24 month data retention; declared unconstitutional in Germany, Ireland, and Romania; Italy retains up to 5 years |
| **Network/access provider** | Entity providing physical or logical connectivity to the internet (e.g., ISPs, mobile operators) |
| **Hosting provider** | Entity hosting data or services on behalf of third parties (e.g., cloud providers) |
| **Freezing procedure** | Immediate formal request to an ISP to preserve specific data pending a formal warrant |
| **Article 132 (D.Lgs. 196/2003)** | Italian provision requiring prosecutor and judge authorisation to obtain IP address data from a provider; only for serious crimes |
| **Tor** | Anonymisation network routing traffic through multiple relays, masking the origin IP; 2012 Interpol-level acknowledgment that blocking anonymisation is technically impossible |
| **OSINT** | Open Source Intelligence — intelligence derived from publicly available sources |
| **Transparency report** | Annual disclosure by technology platforms of government requests for data and content removal, and their responses |
| **Emergency Disclosure Procedure (EDP)** | 24/7 fast-track mechanism for law enforcement to obtain data from platforms in imminent-danger situations (terrorism, kidnapping) without a court order |
| **Prosecutorial discretion** | Power of a US prosecutor to decline to pursue a case |
| **Compulsory prosecution** | EU/Italian principle that investigators must formally respond to any properly filed criminal complaint |
| **UFED (Cellebrite)** | Industry-standard mobile forensics extraction device and software; continuously updated; extremely expensive |
| **Territorial principle** | Jurisdiction of the country where the data is physically located (or managed) — most common principle |
| **Power of disposal approach** | Jurisdictional principle: if a device is in your jurisdiction, you can access its data regardless of where that data is hosted; controversial |
| **Key mandatory law** | Law compelling revelation of encryption keys; attempted in Australia, Belgium, France, Boucher (US/Canada); declared unconstitutional in all cases |
| **Remote forensics** | Covert installation of spyware on a suspect's device to gain access; used in absence of legal password compulsion |
| **Right to informational self-determination** | Right articulated by the German Constitutional Court (2008): the right to confidentiality and integrity of one's own IT systems |
| **Fruit of the poisonous tree** | Common law (US/UK): evidence derived from illegally obtained evidence is inadmissible; weaker in civil law systems |
| **Jurisdiction problem** | The conflict arising when digital evidence is stored in a different legal jurisdiction from the investigation |

---

## Summary

- Digital forensics spans criminal, civil, and corporate domains, each governed by different legal frameworks and standards (ISO 27037, NIST).
- Suspect identification relies on digital identifiers (IP addresses), OSINT, and **data retention** records from ISPs.
- In Italy, obtaining IP data requires prosecutor/judge authorization and is only available for serious crimes under **Article 132**.
- Data retention periods vary globally; Italy's 5-year requirement is exceptional compared to the declared unconstitutionality in other EU states.
- The Rise of **Tor and anonymization tools** has significantly devalued the IP address as standalone reliable evidence.
- The **jurisdiction problem** remains central: data of EU users is often held by US companies governed by US law, creating legal conflicts.
- Four jurisdictional principles determine authority: territorial, nationality, flag, and the controversial **power of disposal**.
- **Mobile forensics** requires expensive, specialized equipment like **UFED** to handle encryption and diverse connectivity interfaces.
- US and EU/Italian investigation models differ significantly between **compulsory prosecution** and **prosecutorial discretion**.
- **Remote forensics** and state-sponsored hacking (e.g., Hacking Team) emerged as responses to the unconstitutionality of mandatory password disclosure.
