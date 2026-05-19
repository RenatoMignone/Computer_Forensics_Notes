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

`dd` is the foundational Unix-style bit-copy tool. It is a common fallback on Unix-like forensic systems when specialised tools are unavailable.

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

`dc3dd` is one of the `dd`-style forensic tools Atzeni mentions as embedding hash calculation into the copy workflow.

| Feature | `dd` | `dc3dd` |
|---------|------|----------|
| Simultaneous hashing during copy | ❌ | ✅ (source + dest, multiple algorithms) |
| Hash log file output | ❌ | ✅ |
| Per-block error logging | ❌ | ✅ |
| Additional forensic logging | ❌ | ✅ |
| Error-related information | Limited | ✅ |

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

**FTK Imager** is presented in the lecture as a famous and widely used GUI-based forensic acquisition tool.

### Key Features

| Feature | Description |
|---------|-------------|
| **Multiple forensic formats** | Supports famous and widespread acquisition formats |
| **Integrated hash support** | Can assist with verifying the image produced |
| **GUI workflow** | Useful when a visual interface is preferred over command-line tools |
| **Practical adoption** | Used in real forensic investigations |

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — FTK Imager*

---

## 4. Lab Setup

The following components constitute a minimal forensic USB acquisition lab:

| Component | Specification / Purpose |
|-----------|------------------------|
| **Forensic workstation** | A clean, investigator-controlled machine, ideally running a forensic distribution such as Kali, Tsurugi, or CAINE |
| **Hardware write blocker** | Interposed between the target USB drive and the workstation to prevent any write commands reaching the source |
| **Target USB drive** | The evidence item; should not be connected to an ordinary machine before the write blocker is in place |
| **Destination storage** | Dedicated forensic storage with adequate capacity, low error rates, good speed, and controlled use |

> ⚠️ *Do not connect the target USB directly to an ordinary OS without a write blocker. Atzeni stresses that normal mounting can modify timestamps and metadata, and even read-only mounting is less defensible than a hardware write blocker in an important case.*

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
| Using non-dedicated destination media | Raises the risk of errors, contamination, or claims that the acquisition device was compromised | Use storage dedicated to forensic work, and ideally dedicated to the specific investigation in important cases |

> 📎 *Slide reference: `03b_Forensic-USB-Drive-Acquisition.pdf` — Common Pitfalls*

---

## Key Concepts & Definitions

| Term | Definition |
|------|------------|
| **`dd`** | Standard Unix bit-copy utility; no built-in hashing or error logging |
| **`dc3dd`** | Enhanced `dd` with integrated hashing, error logging, and split output; open-source |
| **FTK Imager** | GUI forensic acquisition tool described in lecture as famous and widely used |
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
- **FTK Imager** is a famous GUI tool used in real investigations and useful when a visual workflow is preferable.
- The **hardware write blocker** is the preferred protection for an important acquisition — connecting evidence media directly to an ordinary OS can modify the source.
- The eight-step procedure ensures: clean destination, confirmed device, pre-acquisition source hash, imaging, post-acquisition verification, source re-hash confirmation, and physical sealing.
- Use dedicated forensic destination storage; avoid ordinary mounting/automounting of the source; **never assume the device path** — always verify with tools such as `lsblk` and `dmesg`.
