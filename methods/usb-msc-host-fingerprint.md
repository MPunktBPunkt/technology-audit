# Method: USB MSC Host Fingerprint

```yaml
slug: usb-msc-host-fingerprint
title: USB MSC Host Fingerprint (Device-Gadget Observation)
status: active
tags: [usb, msc, field, fingerprinting]
```

## Zweck

Am **MSC-Device-Gadget** beobachtbare Host-Muster erfassen (Opcode-Sequenz, READ/WRITE,
Mount/Remount, Recovery, AOA-Nebenkanal) — ohne Wire-PHY und ohne Host-Klassen aus n=1
abzuleiten.

## Voraussetzungen

- Stabiles MSC-Gadget (bekannte Identity VID:PID, Kapazität, Pattern/FAT klar dokumentiert)
- Class-Hook oder äquivalente CBW-Sichtbarkeit (`source` taggen)
- Status-Zähler: reads/bytes/writes/mounts/unmounts + `aoa51/52/53`
- Optional: Soft-Reenum / fault stimulus für Recovery
- Topology-Zeile: welches Kabel, welcher Host, welche Identity/Content

## Ablauf

1. **Baseline:** Gadget Identity + Content festhalten (z. B. `303a:1001` + `lab_sector_v1` vs. FAT).
2. **Connect:** Host stecken; Mount/Unmount und erste CBW-Sequenz loggen.
3. **Slice:** Timed delta (reads/bytes/writes + AOA-Zähler) + SCSI-Ring / Aggregate.
4. **Stimulus (optional):** Soft-Reenum, Replug, Format/Write — eine Variable pro Lauf.
5. **Negativ:** Non-Host-Port (keine Aktivität) und AOA=0 unter MSC-Identity explizit notieren.
6. **Claim-Grenze:** Host-Profil = C / HOST-SPECIFIC; keine GENERAL-Klassen ohne Wiederholung.

## Artefakte

| Artefakt | Inhalt |
|----------|--------|
| `MATRIX_SUMMARY.json` / Host-Zeile | usb_host?, mount, aoa51, delta_reads, notes |
| Capture / scsi_ops | Opcode-Counts; READ10 transfer_length hist |
| Watch / fault_phases | remount nach Soft-Reenum |
| Evidence-ID | `EVID-…` mit Upstream-Link, nicht Rohdump in KB |

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Identity/Content dokumentiert | Topology-Zeile vorhanden | „Stick“ ohne VID/PID/Pattern |
| Dimensionen getrennt | Opcode ≠ Rate ≠ UI | UI-Stille als „kein USB“ |
| AOA-Nebenkanal | aoa51/52/53 gezählt (auch 0) | AOA weggelassen |
| Write-Cache | Bytes/Ops MEASURED; Eviction nur mit Audit | „Datenloch“ ohne LBA-Audit |
| Generalisierung | n=1 = Project Evidence | „TVs machen X“ als Tech-FACT |

## Fallstricke

- Ring-Overflow verliert frühe Mount-Opcodes (z. B. INQUIRY) — Aggregate Counters prioritär.
- MSC-Mount + AOA-respond ≠ AOA-Initiation durch den Host.
- Windows Write-Bytes > Cache-Slots ist **Test Gap**, kein FACT-Loch.
- Consumer-Hosts ohne FAT/Media erscheinen „still“ trotz Mount.

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| esp32-usb-analyzer Feldmatrix 2026-11-06 | [`esp32-usb-analyzer-2026-field-host-matrix`](../audits/esp32-usb-analyzer-2026-field-host-matrix/) |
| Kontrast BOT observation | [`usb-bot-command-observation`](usb-bot-command-observation.md) |
