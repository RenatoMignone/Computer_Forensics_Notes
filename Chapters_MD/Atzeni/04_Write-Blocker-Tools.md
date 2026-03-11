# Chapter 4 – Write Blocker Tools

**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/04_Write-Blocker-Tools.pdf`]  
**Covered in Lectures:** Lecture 7

---

## Introduction

A **write blocker** is one of the most fundamental tools in the digital forensics toolkit. Its function is deceptively simple — prevent any write operation from reaching an evidence storage device — yet its importance spans the full scope of a forensic investigation: from the moment an investigator first touches an original drive to the moment the report is challenged in court. Without a write blocker in place, even a momentary OS-level interaction with an evidence drive can silently modify metadata and render weeks of subsequent analysis legally inadmissible.

This chapter covers the rationale for write blocker use, the taxonomy of hardware and software solutions, the leading commercial hardware products, the subtleties of software-based blocking (including common Linux misconfiguration pitfalls), and the documentation requirements that transform physical use of a write blocker device into a legally defensible act.

> 📝 *The broader context of write blocker use within the acquisition phase of a forensic investigation is covered in [03_investigation_phases.md](03_investigation_phases.md).*  
> 📝 *Practical hands-on acquisition commands and the chain-of-custody walkthrough are in [03b_Forensic-USB-Drive-Acquisition.md](03b_Forensic-USB-Drive-Acquisition.md).*

---

## 1. Why Write Blockers Are Required

### 1.1 Three Non-Negotiable Properties

| Requirement | Explanation |
|-------------|-------------|
| **Technical soundness** | No bit on the original evidence may be altered during acquisition or subsequent handling. This extends beyond file content to metadata: access times (`atime`), modification times (`mtime`), and internal file-system journal state. |
| **Legal admissibility** | The investigation must demonstrate to the court — including opposing counsel — that the entire manipulation chain was controlled and predictable. A write blocker provides a certified, independently verifiable mechanism for this guarantee. |
| **Repeatability** | A forensically sound acquisition is one that, when performed again on the same evidence under the same documented conditions, produces a **bit-for-bit identical result**. Even one unintended write can break this property permanently. |

### 1.2 The Single-Bit Problem

The evidentiary chain is not "mostly valid" if only a small portion of the data was altered. A single bit flip is enough to:

- Break the cryptographic hash, causing the hash verification step to fail.
- Render the acquired image inadmissible as evidence — regardless of how trivial the modification is in semantic terms.
- Require the entire acquisition to be repeated, which may not be possible if the original evidence has been affected.

> *"The modification of just one bit that might be completely fine from the perspective of the semantic content of my file is nonetheless no longer admissible at the end of the chain — this might be very frustrating."*

### 1.3 Metadata as Evidence

The problem is particularly acute with **metadata**, because normal OS operations modify file-system metadata as a side effect of merely reading a device:

- Mounting a file system without a write blocker updates `atime` on every file touched by the kernel.
- The ext3/ext4 journal may be replayed or extended on a simple mount operation, writing journal-commit records to the device.
- OS indexing services (e.g., `mlocate`, Windows Search) may begin cataloguing immediately upon device attachment.

Metadata is frequently the primary substrate for **timeline construction** — one of the most critical outputs of a forensic examination. Corrupting it forecloses this investigative avenue.

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Why Write Blockers Are Required*

---

## 2. Hardware Write Blockers

### 2.1 Taxonomy: Pure vs Standalone

| Category | Description | Typical Use Case |
|----------|-------------|-----------------|
| **Pure (dependent) write blocker** | A passive hardware device that intercepts the bus between the evidence drive and the forensic workstation. Has no internal OS or intelligence; requires an external laptop or workstation to initiate and manage the acquisition. | Field work with laptop-based acquisition toolchain; lower unit cost. |
| **Standalone write blocker** | A self-contained unit with an embedded, hardened Linux OS (minimal kernel, no known bugs, minimal functionality to reduce attack surface). Can manage and execute the full acquisition with no external computer needed. Simply attach source and destination drives and start. | Lab environments; high-volume acquisition; situations where no analyst workstation should be exposed to the evidence. |

Standalone units are physically larger owing to their embedded compute hardware. Their internal Linux build is deliberately stripped to the minimum required kernel version with no unnecessary services, reducing the probability of undiscovered bugs affecting the acquisition.

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Hardware Write Blockers: Pure vs Standalone*

---

### 2.2 Leading Commercial Products

#### Tableau (Guidance Software / OpenText)

| Aspect | Detail |
|--------|--------|
| **Industry standing** | De facto standard in litigation environments; routinely cited by name in investigation reports as a mark of professional credibility. |
| **Legal standing** | Certified under specific forensic standards; courts recognise the brand by name. |
| **Product range** | T8i, T35, and many others — each model supports a defined set of interface types (SATA, IDE, USB, SAS, PCIe/NVMe, FireWire, Fibre Channel, Ethernet). Model selection depends on the drive interfaces present in the investigation. |
| **Quality standard** | Highest among commercial hardware write blockers. |

#### WiebeTech / RealTech

| Aspect | Detail |
|--------|--------|
| **Product type** | Predominantly pure (non-standalone) hardware write blockers. |
| **Price** | Generally lower than Tableau equivalents. |
| **Target audience** | Private labs; smaller forensic operations. |
| **Quality standard** | Very high; the slight quality differential with Tableau does not render them technically unreliable — the gap relates mainly to certification breadth and brand recognition in court settings. |

#### Logicube

| Aspect | Detail |
|--------|--------|
| **Known for** | Duplicator series; end-to-end forensic duplication units (standalone). |
| **Standing** | Well-known and widely deployed; considered one of the three leading brands in forensic duplication. |

#### Interface Coverage Table (Illustration — Tableau Example)

Different models cover different physical interfaces. The exact model used, not just the brand, must be documented because models differ in interface support. Example discrepancy:

| Tableau Model | SATA | IDE/PATA | USB | SAS | PCIe/NVMe |
|---------------|------|----------|-----|-----|-----------|
| T8i | ✅ | ❌ | ✅ | ❌ | ❌ |
| T35 | ✅ | ✅ | ✅ | ✅ | ❌ |
| (full list per official Tableau datasheets) | — | — | — | — | — |

If the investigation report cites "T8i" but the opposing expert has an IDE drive to re-test with, the acquisition cannot be reproduced with the documented tool — breaking the chain.

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Hardware Write Blockers: Products and Interface Table*

---

## 3. Software Write Blockers

### 3.1 Definition and Forms

A **software write blocker** is an OS configuration or privileged application that enforces read-only access to an attached evidence device at the kernel or driver level. Two forms:

1. **OS-level configuration**: appropriate mount options, udev rules, or registry settings that block write-path kernel calls for the target device.
2. **Forensic application with root/admin privileges**: a purpose-built program that intercepts all I/O to the target device and enforces read-only semantics, regardless of what the OS would otherwise permit.

### 3.2 Linux: Mount Options

Mounting with read-only (`-o ro`) is the first-order control, but is **insufficient on its own** for journalled file systems:

```bash
# Minimal read-only mount — may still trigger journal replay:
mount -o ro /dev/sdb1 /mnt/evidence

# Correct for journalled file systems (ext3, ext4, XFS):
mount -o ro,noload /dev/sdb1 /mnt/evidence
```

**Why `noload` matters:**

| Without `noload` | With `noload` |
|-----------------|---------------|
| Kernel replays the ext3/ext4 journal on mount | Journal replay is suppressed |
| Journal-commit metadata may be written to the device | No writes occur |
| `ro` flag does not prevent all journal-related writes | Evidence integrity preserved |

The `noload` option (also accessible as `norecovery` on XFS) is the forensically correct choice. This is just one example of the depth of OS knowledge required to use a software write blocker correctly — which is why courts are sceptical of software-only approaches.

### 3.3 Legal Standing of Software Write Blockers

Software write blockers are significantly harder to defend in court for the following reasons:

- There is no independently certifiable physical device whose design can be inspected.
- The examiner must demonstrate mastery of every edge case in the OS kernel and driver stack that might have led to a write.
- Different OS versions and patch levels may behave differently for the same configuration.
- The opposing party cannot replicate the exact software environment without knowing the full OS patch history.

> *"In a court of justice, it is very appreciated that you use something that all parties, including the counterpart, know as error-free and reliable."*

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Software Write Blockers and Their Limitations*

---

## 4. Common Errors

| Error | Description | Consequence |
|-------|-------------|-------------|
| **Direct device connection** | Evidence drive connected to any workstation without a write blocker in place, even briefly | OS immediately interacts with device on plug-in, modifying metadata; even immediate disconnection may not prevent the modification |
| **`ro` mount without `noload`** | Journalled file system mounted read-only but journal replay not suppressed | Journal metadata written to device; hash no longer matches |
| **Wrong model documented** | Investigation report names a Tableau T8i; drive to be replicated requires an IDE interface not present on the T8i | Opposing expert cannot replicate acquisition; legal chain broken |
| **Missing device documentation** | Evidence drive type noted as "USB pen drive" but it is actually an older interface type | Same reproducibility failure |
| **No photographs** | Steps and connections not photographically documented | No visual proof the write blocker was used as claimed; Standard Operating Procedure compliance failure |
| **Hash computed late** | Hash computed a significant time after acquisition completes, not atomically | Window of opportunity for undetected modification between imaging and hashing |

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Common Errors in Write Blocker Use*

---

## 5. Documentation Requirements

Rigorous documentation of write blocker use is not optional — it is the mechanism by which technical actions become legally durable. Required documentation:

### 5.1 Device Identification Fields

| Field | Example | Purpose |
|-------|---------|---------|
| Write blocker make and model | Tableau T35 | Identifies exact interface support and capability |
| Serial number | WB-20230412-001 | Uniquely identifies this specific physical unit |
| Firmware version | 3.1.4 | Different firmware may have different bug profiles |
| Firmware update history | Last updated 2025-01-10 | Identifies whether known bugs apply to this unit |
| Connection type used | SATA III (6 Gbit/s) | Establishes the acquisition pathway |
| Evidence device make, model, S/N | Samsung 870 EVO 1TB — S/N: S4XXXXXX | Uniquely identifies the evidence storage medium |

### 5.2 Standard Operating Procedure (SOP) Citation

Most forensic standards require the examiner to reference the SOP under which the acquisition was conducted. An example citation from investigation documentation:

> *"Digital evidence was acquired using a Tableau T35 write blocker (S/N: XXXX, firmware v3.1.4) in accordance with Lab SOP-ACQ-004, compliant with ISO/IEC 27037:2012."*

This single sentence accomplishes three goals: it identifies the tool (with enough specificity to reproduce the acquisition); it ties the action to a documented, auditable procedure; and it cites the governing standard.

### 5.3 Photographic Evidence

Photographs (and where possible, video) must document:
- Each device before connection
- The write blocker with evidence drive connected and running
- The acquisition progress screen or terminal output
- The hash verification output

These images form part of the investigation's **Standard Operating Procedure evidence package** and are typically appended to the legal documentation alongside the written chain-of-custody record.

> 📎 *Slide reference: `04_Write-Blocker-Tools.pdf` — Documentation and Standard Operating Procedures*

---

## 6. Hashing in Combination with Write Blockers

The write blocker and the hash verification step are **complementary and inseparable**:

| Step | Tool | Purpose |
|------|------|---------|
| Write-blocked acquisition | Hardware write blocker | Prevents modification of original evidence during copying |
| Hash of original (pre-acquisition, if accessible) | `dc3dd` or hash tool | Establishes a reference baseline |
| Hash of acquired image (immediately post-imaging) | `dc3dd` (integrated) | Confirms the copy is bit-for-bit identical to original |
| Dual-algorithm hash (high-stakes cases) | Two independent hash algorithms | Defence against hash collision arguments |

`dc3dd` (the forensic extension of `dd`) integrates hashing atomically with the imaging process, eliminating the gap between completing the image and computing its hash:

```bash
dc3dd if=/dev/sdb of=/mnt/forensic/evidence.dd hash=sha256 log=/mnt/forensic/acquisition.log
```

> 📝 *Full `dc3dd` and `dd` parameter reference and a step-by-step practical acquisition walkthrough are in [03b_Forensic-USB-Drive-Acquisition.md](03b_Forensic-USB-Drive-Acquisition.md).*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **Write blocker** | A hardware device or software configuration that prevents all write operations from reaching an evidence storage medium |
| **Pure write blocker** | Hardware write blocker without its own OS; depends on an external workstation to manage the acquisition |
| **Standalone write blocker** | Self-contained hardware write blocker with an embedded minimal OS; can perform the full acquisition independently |
| **`noload` / `norecovery`** | Linux `mount` options that suppress ext3/ext4 or XFS journal replay during a read-only mount, preventing silent metadata writes |
| **`dc3dd`** | Forensic extension of the Unix `dd` utility; integrates hashing and logging atomically with the imaging process |
| **SOP (Standard Operating Procedure)** | A documented step-by-step procedure derived from a recognised forensic standard, defining how investigations must proceed to remain court-compliant |
| **Technical soundness** | The property that evidence has not been altered in any way since seizure; verifiable only if a write blocker was used |
| **Repeatability** | The property that re-running the documented acquisition steps produces a bit-for-bit identical copy; broken by any unintended write |
| **Hash verification** | Comparing cryptographic hash values before and after a step to confirm no modification occurred; two independent hash algorithms recommended for high-stakes cases |
| **Interface type** | The physical connector standard used by a storage device (SATA, IDE/PATA, USB, SAS, PCIe/NVMe, etc.); must match the write blocker's supported interfaces |

---

## Summary

- A write blocker is mandatory before any forensic interaction with original evidence; the threshold for metadata corruption is a single OS-level interaction on plug-in.
- Three properties that write blockers protect: **technical soundness**, **legal admissibility**, and **repeatability**.
- **Hardware write blockers** are preferred over software solutions in both technical rigour and court acceptance.
- **Pure write blockers** require an external workstation; **standalone write blockers** operate independently with an embedded OS.
- **Tableau** is the de facto legal standard; **WiebeTech** and **Logicube** are trusted alternatives routinely used in private labs.
- Document the exact model (not just the brand) of every write blocker used — different models support different interfaces and a model mismatch breaks reproducibility.
- Under Linux, `mount -o ro` alone is insufficient for journalled file systems; `noload`/`norecovery` must be added to suppress journal replay.
- Software write blockers are technically viable but legally weak: they depend on the examiner's ability to prove mastery of every OS edge case, which is impossible to certify externally.
- Hashing (run atomically via `dc3dd`) must be performed immediately after write-blocked imaging; dual-algorithm hashing is recommended for high-stakes cases.
- Comprehensive documentation (model, serial number, firmware, connection method, photographs) is required to transform a well-executed acquisition into a court-defensible one.
