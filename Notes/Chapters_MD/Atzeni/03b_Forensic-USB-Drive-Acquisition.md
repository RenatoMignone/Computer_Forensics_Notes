# Chapter 3b – Forensic USB Drive Acquisition: Tools and Procedure
**Professor:** Atzeni  
**Reference Slides:** [`Slides/Atzeni/03b_Forensic-USB-Drive-Acquisition.pdf`]  
**Covered in Lectures:** Lecture 5

---

## Introduction
This chapter provides a hands-on, tool-level walkthrough of acquiring a forensic image from a USB drive. It covers the primary command-line acquisition tools (`dd`, `dc3dd`) and FTK Imager as a GUI alternative, the lab setup required, an eight-step acquisition procedure with annotated commands, chain of custody documentation at the point of acquisition, and a table of common pitfalls.

> 📝 *For the broader context of where acquisition fits within the five investigation phases, see [03_investigation_phases.md](03_investigation_phases.md).*

---

## 1. `dd` — The Standard Unix Copy Utility

`dd` is the foundational Unix bit-copy tool. It is present on every Linux and macOS system with no installation required, making it a universal fallback when specialised tools are unavailable.

### Key Parameters

| Parameter | Meaning | Example Value |
|-----------|---------|--------------|
| `if=` | Input file — the source device or file | `if=/dev/sdb` |
| `of=` | Output file — the destination image file | `of=/media/evidence/usb_image.dd` |
| `bs=` | Block size — bytes read and written per I/O operation; larger = faster | `bs=512` |

### Basic Acquisition Command

```bash
dd if=/dev/sdb of=/media/evidence/usb_image.dd bs=512
```

### Limitations of bare `dd`

| Limitation | Impact |
|------------|--------|
| No built-in hashing | Must run `sha256sum` **before** and **after** separately; the two operations are not atomic |
| No log output | No per-block error record; errors are counted but not located |
| No verification pass | Does not automatically compare source and destination after imaging |

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — `dd` and Forensic Copy Tools*

---

## 2. `dc3dd` — Enhanced Forensic Copy Tool

`dc3dd` was created to address `dd`'s forensic shortcomings. It is open-source and available in standard Linux forensic distributions (Kali, CAINE).

| Feature | `dd` | `dc3dd` |
|---------|------|----------|
| Simultaneous hashing during copy | ❌ | ✅ (source + dest, multiple algorithms) |
| Hash log file output | ❌ | ✅ |
| Per-block error logging | ❌ | ✅ |
| Split output files | ❌ | ✅ |
| Progress display | Partial | ✅ |
| Scrubbing (wipe destination before write) | ❌ | ✅ |

### `dc3dd` Example Command

```bash
dc3dd if=/dev/sdb hof=/media/evidence/usb_image.dd \
  hash=sha256 \
  hash=sha512 \
  log=/media/evidence/acquisition_log.txt \
  verb=on
```

| Argument | Meaning |
|----------|---------|
| `hof=` | Hashed output file — destination image; hashes are computed during the copy |
| `hash=sha256` | Compute SHA-256 of both source and destination simultaneously |
| `hash=sha512` | Also compute SHA-512 simultaneously (dual-algorithm best practice) |
| `log=` | Write all operational output, hash values, and error counts to a log file |
| `verb=on` | Verbose output: percentage complete, bytes processed |

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — dc3dd*

---

## 3. FTK Imager

**FTK Imager** is a widely-used GUI-based forensic acquisition and preview tool. It is widely accepted in courts and used by law enforcement agencies worldwide.

### Key Features

| Feature | Description |
|---------|-------------|
| **Multiple image formats** | Supports `.dd` (raw), `.E01` (EnCase evidence format), `.AFF` (Advanced Forensic Format), `.L01` |
| **Integrated hash verification** | Computes MD5 and SHA-256 of source and image simultaneously; produces a hash report |
| **Drive preview** | Browse the file system and view files in the source device **without mounting** it — no atime modification |
| **Physical and logical acquisition** | Can acquire an entire physical drive, a single partition, or selected folders |
| **Memory acquisition** | Can capture a RAM dump of a running Windows system |
| **Chain of custody fields** | GUI prompts for examiner details, case number, and evidence item description before acquisition begins |
| **Export hash report** | Produces a signed hash report document suitable for court submission |

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — FTK Imager*

---

## 4. Lab Setup

The following components constitute a minimal forensic USB acquisition lab:

| Component | Specification / Purpose |
|-----------|------------------------|
| **Forensic workstation** | A clean, investigator-controlled machine booted from a trusted forensic OS (e.g., CAINE, Tsuruji) or a verified, imaged Windows installation |
| **Hardware write blocker** | Interposed between the target USB drive and the workstation to prevent any write commands reaching the source |
| **Target USB drive** | The evidence item; must NOT be connected to any machine before the write blocker is in place |
| **Destination storage** | A separate drive or network share with capacity at least equal to the target; pre-wiped and hashed to prove it was blank before acquisition; stored under the same evidentiary controls as the target after acquisition |

> ⚠️ *Do not connect the target USB directly to the OS without a write blocker. USB mass storage drivers on Linux, Windows, and macOS all write metadata (Last Mount, NTFS journal replay, device registration) on connection, even in read-only mode unless explicitly blocked at the kernel level.*

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — Lab Setup*

---

## 5. Step-by-Step Acquisition Procedure

### Pre-Acquisition
**Step 1: Prepare and verify the destination drive**
```bash
# Confirm destination device identifier
lsblk

# Wipe destination to zeros (proves no prior data)
# Use dedicated forensic wipe utility or dd with /dev/zero

# Record hash of blank destination
sha256sum /dev/sdc > /media/logs/destination_pre_hash.txt
```

**Step 2: Connect the write blocker and attach the source USB**
> *Physical action*: Attach the hardware write blocker to the forensic workstation; plug the target USB into the write blocker's "evidence" port.

**Step 3: Identify the source device**
```bash
lsblk                 # List all block devices
dmesg | tail -20      # Confirm device assignment (e.g., /dev/sdb)
```
> *Confirm the size matches the known capacity of the target USB. Avoid any assumptions.*

**Step 4: Record the pre-acquisition hash of the source**
```bash
sha256sum /dev/sdb > /media/logs/source_pre_hash.txt
cat /media/logs/source_pre_hash.txt
```

### Acquisition
**Step 5: Run the forensic imaging tool**
```bash
dc3dd if=/dev/sdb hof=/media/evidence/usb_CASE042_ITEM003.dd \
  hash=sha256 \
  hash=sha512 \
  log=/media/logs/acquisition_log_CASE042_ITEM003.txt \
  verb=on
```
> *Monitor output for read errors. In `dc3dd` these are reported as bad sectors; note them in the chain of custody record.*

### Post-Acquisition Verification
**Step 6: Verify the image hash**
```bash
sha256sum /media/evidence/usb_CASE042_ITEM003.dd
# This hash MUST match the pre-acquisition source hash recorded in Step 4
```

**Step 7: Compute and record the hash of the sealed original**
```bash
sha256sum /dev/sdb > /media/logs/source_post_hash.txt
diff /media/logs/source_pre_hash.txt /media/logs/source_post_hash.txt
# Output should be empty (no differences) — confirming write blocker worked
```

**Step 8: Seal and label the original; document in the chain of custody**
> *Physical action*: Disconnect the USB from the write blocker; place in a tamper-evident evidence bag; apply a label with the item number, hash value, acquisition date/time, examiner name; seal the bag; sign across the seal.

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — Acquisition Procedure*

---

## 6. Chain of Custody Documentation at Acquisition

In addition to the general chain of custody fields (see [03_investigation_phases.md](03_investigation_phases.md)), the following fields must be captured **at the point of acquisition**:

| Field | Required Detail |
|-------|----------------|
| Acquisition start time | UTC timestamp when the imaging tool started |
| Acquisition end time | UTC timestamp when the imaging tool completed |
| Source device identifier | OS device path (e.g., `/dev/sdb`), manufacturer, model, serial number |
| Source pre-acquisition hash | Algorithm name + hash value (computed before imaging) |
| Image filename | Full path and filename of the resulting image file |
| Image post-acquisition hash | Algorithm name + hash value (computed after imaging) |
| Tool name and version | e.g., `dc3dd version 7.2.641-osfmount` |
| Write blocker name and model | e.g., `Tableau T8-R2 Forensic USB Bridge` |
| Read errors | Count and sector locations of any bad sectors encountered |
| Examiner name and badge number | The individual who performed the acquisition |

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — Chain of Custody at Acquisition*

---

## 7. Common Pitfalls

| Pitfall | Consequence | Prevention |
|---------|-------------|-----------|
| Connecting the target USB **without a write blocker** | OS writes to the device on mount (metadata, journal replay); original is contaminated | Always attach the write blocker first; verify it is enabled before connecting the source |
| Using the **wrong device path** (e.g., imaging `/dev/sda` instead of `/dev/sdb`) | May overwrite the forensic workstation's own OS drive | Use `lsblk` and `dmesg` to confirm the device identifier; **never assume** |
| Using **MD5 alone** for the acquisition hash | Vulnerable to collision attacks; defence can argue hash was falsified | Always use SHA-256 or higher; use dual algorithms for critical evidence |
| Not recording **pre-acquisition hash of the source** | Cannot prove the image was unmodified at acquisition time | The source hash is recorded **before** the imaging tool runs, not after |
| **Automounting**: OS auto-mounts the USB before the write blocker is in place | Automatic metadata writes contaminate the original | Disable automount in the forensic OS before connecting any evidence device |
| Not hashing or **pre-wiping the destination** | Cannot prove the destination was blank (could argue planted data) | Wipe and hash the destination before use; document the pre-wipe hash |

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — Common Pitfalls*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **`dd`** | Standard Unix bit-copy utility; no built-in hashing or error logging |
| **`dc3dd`** | Enhanced `dd` with integrated hashing, error logging, and split output; open-source |
| **FTK Imager** | Commercial GUI forensic acquisition and preview tool; widely accepted in courts |
| **Hardware write blocker** | Physical device that prevents any write commands from reaching the source evidence drive |
| **`.dd` format** | Raw bit-for-bit image; no metadata container; simplest format; directly mountable |
| **`.E01` format** | EnCase evidence format; includes embedded metadata (hash, case info) and compression |
| **Automount** | OS feature that automatically mounts removable storage on insertion — must be disabled on a forensic workstation |
| **Pre-acquisition hash** | Hash of the source computed **before** imaging begins; the reference value for all subsequent verification |
| **Dual-algorithm hashing** | Computing two different hash algorithms simultaneously to further prevent collision-based challenges |

---

## Summary

- **`dd`** is universal but requires manual, separate hashing steps — not recommended when specialised tools are available.
- **`dc3dd`** performs integrated, simultaneous hashing of source and destination during the copy, making it a significantly stronger forensic tool than plain `dd`.
- **FTK Imager** is the standard GUI tool; its chain of custody form, hash report, and non-mounting file browser make it practical for both field and lab use.
- The **hardware write blocker** is non-negotiable — connecting evidence media directly to the OS without one will modify the source.
- The eight-step procedure ensures: clean destination, confirmed device, pre-acquisition source hash, imaging, post-acquisition verification, source re-hash confirmation, and physical sealing.
- **Pre-wipe and hash the destination** before acquisition; **disable automount** on the forensic workstation; **never assume the device path** — always verify with `lsblk`.
