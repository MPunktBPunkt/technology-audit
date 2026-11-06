# Technology Sheet: USB MSC Host Behaviour / Host Fingerprinting

```yaml
slug: usb-msc-host-behaviour
title: USB MSC Host Behaviour / Host Fingerprinting
primary: C
tags: [usb-host, fingerprinting, field-verified]
type: pattern
status: active
seen_in: [esp32-usb-analyzer]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0   # Profile leben in Applications; Sheet hält nur Dimensionen + Claim-Grenzen
  reusability: W2
  evidence_scope: [FIELD, HOST-SPECIFIC]
pilot: audits/esp32-usb-analyzer-2026-field-host-matrix
```

Ebene **A** (wiederverwendbare Host-Beobachtungsdimensionen). Konkrete Host-Profile →
Project Applications / Audit-Evidence. Device-Protokoll → [`usb-msc`](../usb-msc/SHEET.md).
BMW-Plattform → [`bmw-nbt-evo`](../bmw-nbt-evo/SHEET.md). AOA-Identity-Gate → [`usb-aoa`](../usb-aoa/SHEET.md).

## Kurzfassung

Unterschiedliche USB-MSC-**Hosts** initialisieren und nutzen denselben Device-Endpunkt mit
beobachtbaren Mustern: SCSI-Opcode-Sequenz, READ-Cadence/-Größen, Mount/Remount,
WRITE-Verhalten, Recovery. Das ergibt eine **Fingerprint-Dimension**, keine universelle
Host-Klassifikation. Ein Nachmittag mit n=1 Gerät pro Klasse reicht **nicht** für
Allgemeinaussagen wie „TVs lesen nur einmal“.

## Abgrenzung

- **Ist:** Beobachtungsachsen und Claim-Grenzen für MSC-Host-Verhalten am Device-Gadget.
- **Ist nicht:** USB-MSC/BOT Spec ([`usb-msc`](../usb-msc/SHEET.md)); Prefetch/Audio-Semantik
  am NBT ([`bmw-nbt-evo`](../bmw-nbt-evo/SHEET.md)); AOA/Connected-Apps ([`usb-aoa`](../usb-aoa/SHEET.md)).
- **Grenzt an:** Instrumentierung ([`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md),
  [`usb-msc-host-fingerprint`](../../methods/usb-msc-host-fingerprint.md)).

## Fingerprint-Dimensionen (A)

| Dimension | Was beobachten | Typischer Nutzen |
|-----------|----------------|------------------|
| SCSI opcode sequence | CBW-Opcodes am Mount / Idle | Init-Signatur (P-MOUNT vs. Scan vs. OS) |
| READ cadence | Inter-Arrival / Burst vs. Idle | Aktivitätsklasse |
| READ sizes | `transfer_length` Histogramm | Host-Chunking |
| Mount / remount | mount/unmount counts, Soft-Reenum | Session-/Recovery-Verhalten |
| WRITE behaviour | writeOps / writeBytes / LBA | Format/OS vs. Read-only Hosts |
| Recovery | CLEAR_HALT, PREVENT/ALLOW, remount after fault | Robustheit / Host-FSM |

**Status:** Dimensionen `FACT` (als Messachsen) · A.  
**Konkrete Zahlen / Host-Namen:** nur Application/Evidence · C.

## Typische Fallstricke (A)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Ein Host-Muster gilt für alle Hosts | `REJECTED` | Fingerprint ist host-spezifisch |
| n=1 Gerät ⇒ Host-Klasse („TVs…“) | `REJECTED` | Project Evidence ja; GENERAL nein |
| AOA=0 an MSC-Identity ⇒ Host kann kein AOA | `REJECTED` | Identity-Gate; siehe `usb-aoa` |
| UI-Stille ⇒ kein USB-Mount | `REJECTED` | oft stiller Mount ohne FAT/Media |
| Capture-Ring-Overflow = vollständige Opcode-Historie | `REJECTED` | Aggregate/Counters nötig |
| Windows Write-Bytes > Cache-Slots ⇒ Datenloch | `UNKNOWN` | Test Gap; Eviction erst mit Write-LBA-Audit |

## Transfer

Übernehmbar als **Messrahmen** für jeden MSC-Device-Probe (Analyzer, hu-probe, pidrive):
gleiche Dimensionen, eigene Evidence-IDs, kein stiller Host-Transfer. Host-Klassen
(minimal / scanner / filesystem / interactive OS) erst nach wiederholten Messungen.

### Projektstart-Checkliste

- [ ] Dimensionen vs. Host-Profil trennen (A vs. C)
- [ ] Identity (VID/PID/Descriptors) und Content (FAT/Media) getrennt claimen
- [ ] AOA-Zähler parallel führen — MSC-Mount ≠ AOA-Initiation
- [ ] Ring-Overflow: Aggregate Counters, nicht nur Event-Ring
- [ ] Write-Cache/Eviction nicht ohne LBA-Audit claimen
- [ ] Application + Evidence; `seen_in` nachziehen

## Referenzen

- Pilot-Feldmatrix: [`esp32-usb-analyzer-2026-field-host-matrix`](../../audits/esp32-usb-analyzer-2026-field-host-matrix/)
- Upstream: [LAB_FIELD_HOST_MATRIX_2026-11-06_MEASURED](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/LAB_FIELD_HOST_MATRIX_2026-11-06_MEASURED.md) @ `688a40b`
- Method: [`usb-msc-host-fingerprint`](../../methods/usb-msc-host-fingerprint.md)

## Offene Fragen (A)

- Welche stabilen Host-Klassen ergeben sich bei n≥3 Geräten pro Klasse?
- Welche Aggregate (Opcode-Hist, READ-size-Hist, remount count) reichen trotz Ring-Overflow?
- Ab wann ist WRITE-Eviction MEASURED vs. HYPOTHESIS?

## Lessons

- Feldmatrix 2026-11-06 erhöht **Evidence-Reife** der Dimensionen, nicht automatisch die
  Allgemeinheit der Host-Klassen.
- BMW NBT Evo und Windows sind die derzeit stärksten Referenzprofile; Consumer-Media/NAS
  bleiben Project Evidence bis zur Wiederholung.
