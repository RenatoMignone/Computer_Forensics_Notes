# Chapter – Articles 615-ter and 615-quater: Malware, Access, and Liability
**Professor:** Vaciago
**Reference Slides:** [`Slides/Vaciago/Articoli_Codice_Penale.pdf`](../../Slides/Vaciago/Articoli_Codice_Penale.pdf)
**Covered in Lectures:** [Lecture 26](../../Lectures_MD/Lecture_26_Vaciago.md)

---

## Introduction

This chapter collects the legal material introduced for the malware-production laboratory. The slides provide the text of Articles 615-ter and 615-quater of the Italian Criminal Code, while the lecture frames them through a Hacking Team-style scenario involving a company that produces malware or lawful-interception tools.

---

## 1. Article 615-ter: Unauthorized Access

Article 615-ter punishes unauthorized access to a protected computer or telecommunication system, or remaining in the system against the will of the person entitled to exclude the actor.

For digital forensics and cybersecurity work, the article matters because many technical actions can look similar at the packet or host level:
- legitimate administrative access;
- authorized penetration testing;
- law-enforcement access under judicial authorization;
- private unauthorized intrusion;
- malware-enabled remote control.

The legal distinction depends on authorization, role, purpose, context, and the actor's subjective element.

---

## 2. Article 615-quater: Codes and Means of Access

Article 615-quater concerns the unlawful procurement, reproduction, diffusion, communication, or delivery of codes, passwords, or other means suitable for accessing protected systems, where the purpose is profit or damage.

In the lecture scenario, malware and access tooling can be discussed as "means suitable for access." This makes the article relevant to companies that produce, sell, or distribute remote-access tools, exploits, credentials, or instructions.

---

## 3. Malware Producers and Lawful-Interception Vendors

Vaciago asks students to analyze a company accused because it produces malware or an interception platform. The scenario is intentionally ambiguous: the company may sell only to government agencies, but it still produces tools capable of unauthorized access.

The prosecution can focus on the intrinsic suitability of the tools for illegal access. The defence can focus on lawful customers, public-authority use, internal compliance, and absence of criminal purpose.

The analysis must avoid the shortcut that "malware is always illegal" or "government customers make everything legal." The legal issue is more precise.

---

## 4. Mens Rea

The key concept is **mens rea**, the subjective element. In this context, the issue is not simply whether the defendant had a morally bad intention. The question is whether the defendant had awareness and will with respect to the conduct that satisfies the offence.

This is why the same technical artifact can create different legal arguments depending on:
- what the producer knew;
- what the tool was designed to do;
- who received it;
- what contractual and operational limits existed;
- whether the company knew about unlawful uses.

---

## 5. Participation in a Crime

The second core concept is participation in a crime. A company or researcher may be exposed to liability if their work contributes to another actor's offence.

Relevant questions include:
- whether R&D required contact with cybercriminal suppliers;
- whether vulnerabilities or access were purchased from illegal markets;
- whether the company knowingly enabled unlawful operations;
- whether the company had procedures to prevent misuse.

For exam purposes, this chapter should be read together with the Hacking Team case material, because both deal with spyware, public authorities, legal authorization, and the boundary between technical capability and criminal responsibility.

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Article 615-ter c.p.** | Unauthorized access to a protected computer or telecommunication system. |
| **Article 615-quater c.p.** | Unauthorized possession or distribution of access codes or other means suitable for access. |
| **Mens rea** | Subjective element: awareness and will regarding the legally relevant conduct. |
| **Participation in a crime** | Liability arising from contribution to another actor's offence. |
| **Lawful interception** | Authorized interception or remote access performed under legal conditions. |

---

## Summary
- Articles 615-ter and 615-quater are central to the malware-production laboratory.
- Malware production is analyzed through authorization, access, distribution, purpose, and subjective element.
- Mens rea is the main analytical target of the assignment.
- Participation in a crime matters when cybersecurity research touches criminal suppliers or unlawful operations.
- The same tool can support different prosecution and defence arguments depending on surrounding facts.
