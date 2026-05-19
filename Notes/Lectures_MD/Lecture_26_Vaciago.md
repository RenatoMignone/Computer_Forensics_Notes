# Lecture 26 – Malware Production, Mens Rea, and Criminal Liability
**Professor:** Vaciago
**Course:** Computer Forensics and Cybercrime Analysis (CFCCA)
**Reference Slides:** `Slides/Vaciago/Articoli_Codice_Penale.pdf`

---

## Overview
This laboratory lecture reframes the Hacking Team discussion as a legal exercise about companies that produce malware or lawful-interception tooling. Vaciago asks students to argue either for the prosecution or the defence of a company accused under Articles 615-ter and 615-quater of the Italian Criminal Code.

The lecture also contains methodological feedback on student homework and a broader reflection on media pressure in criminal cases, using the Garlasco case as an example of how public attention can distort justice.

---

## 1. Homework Feedback and Use of AI

Vaciago begins by commenting on the first homework submissions. He accepts the use of generative AI, but insists that a forensic or legal analysis must show the student's own reasoning.

The key warning is qualitative rather than formal: producing many pages does not improve the work if the reasoning is weak or if the text contains unsupported claims. For later assignments, the evaluation will be stricter, and work done during class laboratories must normally be individual unless the professor gives prior approval.

---

## 2. Criminal Cases, Privacy, and Media Pressure

The lecture then discusses recent public attention around the Garlasco case. Vaciago distinguishes between public-interest political debate and criminal cases involving private persons.

In his view, criminal proceedings should be judged through trial evidence and judicial decisions, not through newspapers, television anticipations, or social-media pressure. Media pressure can harm both suspects and the quality of justice because prosecutors, judges, lawyers, and experts may be forced to operate under external expectations rather than only on the evidence.

The forensic lesson is that digital evidence must be handled in a disciplined procedural setting. Public curiosity is understandable, but it is not a substitute for evidentiary method.

---

## 3. The Laboratory Scenario: Malware Producers

> 📎 *Slide reference: `Articoli_Codice_Penale.pdf` — Articles 615-ter and 615-quater*

Vaciago changes the Hacking Team laboratory perspective from a mainly technical analysis to a legal analysis. Students must imagine a company that produces malware or a broader interception platform, similar in role to tools such as RCS Galileo.

The scenario distinguishes:
- companies that produce malware as a standalone artifact;
- companies that produce a broader operational package for remote access, interception, or surveillance;
- companies that sell only to government agencies or public authorities;
- companies whose research and development may require contact with vulnerability brokers, ethical hackers, or cybercriminal environments.

The central legal problem is whether the production, possession, distribution, or use of these tools is criminal, and under what subjective conditions.

---

## 4. Article 615-ter: Unauthorized Access

In the lecture, Article 615-ter is introduced as the unauthorized-access offence relevant to protected computer systems.

In the laboratory scenario, the prosecution can argue that a spyware platform is designed precisely to enter protected systems. The defence can argue that the company sells a tool, often to public authorities, and that the legality of a concrete access depends on authorization, purpose, and operational use.

The article is therefore not only a technical question of whether access occurred. It also requires attention to authorization, role, context, and the will of the system owner.

---

## 5. Article 615-quater: Access Codes and Means of Access

In Vaciago's framing, Article 615-quater raises the risk that producing, importing, possessing, or distributing malware-like access tools may itself be treated as criminally relevant.

Vaciago connects this to the possession and distribution of malware or access-enabling tools. A company producing such tools may be accused not only of technical development but also of creating or distributing means suitable for unlawful access.

For the defence, the difficult point is to show that the tool's production and delivery are framed by lawful purposes, lawful customers, and a lack of criminal intent.

---

## 6. Mens Rea

The most important concept for the assignment is **mens rea**, the subjective element of the offence.

Vaciago stresses that mens rea is not simply a bad moral purpose. The relevant question is awareness and will with respect to the criminal conduct. In the malware scenario, this means asking whether the accused was aware of producing or distributing a tool suitable for the prohibited activity, and whether the legal elements of the offence are satisfied.

This creates a subtle distinction:
- producing malware to attack a bank may involve both malware-related offences and the later offence against the bank;
- producing malware for a law-enforcement investigation may have a legitimate declared purpose, but the legal analysis still must address awareness of producing the tool;
- selling only to governments may be relevant for defence, but it does not automatically remove every legal risk.

---

## 7. Participation in a Crime

The second major concept is **participation in a crime** (`concorso`).

Even a researcher or company with cybersecurity aims can create legal risk by entering into operational contact with actors who commit crimes. If a malware producer obtains vulnerabilities, infrastructure, or access from a cybercriminal environment, the question becomes whether the producer participates in the criminal activity of others.

For the laboratory, students must therefore discuss not only the tool itself but also the surrounding relationships:
- who supplied vulnerabilities or access;
- whether the company knew the supplier's illicit activity;
- whether the company helped another actor commit an offence;
- whether the company's customers were legitimate public bodies or illegitimate private actors.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Article 615-ter c.p.** | Unauthorized-access offence used in the lab scenario against the malware-producing company. |
| **Article 615-quater c.p.** | Offence Vaciago connects to production, import, possession, or distribution of malware-like access tools. |
| **Mens rea** | Subjective element: awareness and will regarding the conduct that constitutes the offence. |
| **Participation in a crime** | Liability risk arising from contribution to another actor's criminal conduct. |
| **Lawful-interception tool** | A technical system intended to support authorized investigative interception or remote access. |

---

## Summary
- Vaciago warns that homework must show human reasoning, not only AI-generated volume.
- Media pressure in criminal cases can damage justice and distort the evidentiary process.
- The Hacking Team-style laboratory is reframed around legal liability for malware production.
- Articles 615-ter and 615-quater are the main statutory references.
- The assignment can be argued from either prosecution or defence.
- The core analytical point is mens rea: awareness of the legally relevant conduct.
- Contact with cybercriminal environments can raise participation-in-a-crime issues.
- Selling only to public authorities is legally relevant but not a complete answer by itself.
