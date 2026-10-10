# Technology Sheet: BMW NBT Evo (Host-Plattform)

```yaml
slug: bmw-nbt-evo
title: BMW NBT Evo Head Unit — Host-Plattform
primary: I
tags: [automotive, field-verified, usb-host]
type: technology
status: active
seen_in: [pidrive, esp32-bt-gateway]
maturity:
  technology: R2          # Plattform-Rolle verstanden; kein vollständiges HU-Reverse-Engineering
  implementation: R0      # PiDrive spricht HU an — siehe usb-msc Application (B)
  field_evidence: R3      # USB-MSC-Host-Reads/Prefetch vielfach gemessen (PiDrive-Kontext)
  reusability: W1         # stark BMW-/NBT-spezifisch
pilot: audits/pidrive-2026-bmw-hu
```

Ebene **A** (Plattform-Kontext und Abgrenzung). Empirisches **Host-Verhalten** (Reads, Prefetch, Auto-Next, …) → [`applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) (**C**). MSC-Device-Seite → [`applications/usb-msc.md`](../../projects/pidrive/applications/usb-msc.md) (**B**).

## Kurzfassung

**NBT Evo** ist eine BMW-Headunit-Generation mit USB-Host für Massenspeicher (MSC), Bluetooth (A2DP/AVRCP u. a.) und interner Medienwiedergabe. In PiDrive ist sie der **USB-Host**, der den ESP32-MSC-Gadget liest und MP3 dekodiert. Dieses Sheet beschreibt die Plattformrolle — nicht USB-MSC-Spezifikation und nicht PiDrive-Firmware-Details.

## Abgrenzung

- **Ist:** Ziel-Host in PiDrive; USB-MSC-Consumer; Decoder/UI/Playlist-Logik auf HU-Seite (black box mit beobachtbaren I/O-Mustern).
- **Ist nicht:** Allgemeines USB-MSC-Verhalten aller Hosts; SCSI/FAT-Spec; ESP32-Implementierung.
- **Grenzt an:** [`usb-msc`](../usb-msc/SHEET.md) (Protokoll), [`avrcp`](../avrcp/SHEET.md) (paralleler BT-Pfad, später Pilot 3).

## Schnittstellen (PiDrive-relevant)

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| PiDrive → HU | USB OTG (MSC BOT) | virtuelles FAT, on-the-fly Sektoren |
| PiDrive → HU | Bluetooth Classic | A2DP/AVRCP — anderer Stack, nicht gleichzeitig mit MSC-Zielbild |
| Beobachtung | Traces, LED, Korrelation | Host-Reads, Fenster, `bytesServed` — siehe Application C |

## Typische Fallstricke (A — Plattform)

| Claim | Status | Hinweis |
|-------|--------|---------|
| „NBT liest wie jeder PC-Stick“ | `REJECTED` | Prefetch/Burst/Cold-Body-Muster sind empirisch (**C**) |
| Lab-Host-Replay ersetzt HU-Beweis | `REJECTED` | Lab AV ≠ Feld-Ohr (PiDrive 2026-10-04) |
| Erfolg = nur SCSI-konforme Antworten | `REJECTED` | HU-Decode + hörbarer Ton ist Projektkriterium |
| MSC und BT können parallel als PiDrive-Ziel laufen | `INFERRED` | Architekturwahl PiDrive; nicht „NBT-Spec“ |

## Transfer

Wiederverwendbar als **Vorlage „automotive HU als MSC-Host“**: Trace-Korrelation, Claim-Trennung C vs. MSC-A. Konkrete LBA-/Timing-Profile **nur** mit Evidence aus diesem Host — nicht auf andere Fahrzeuge übertragen.

### Projektstart-Checkliste

- [ ] Nur Host-/Feldclaims (C); keine stillen Spec-Transfers nach `usb-msc`/`avrcp`
- [ ] Evidence-IDs aus Betrieb/Lab verlinken
- [ ] Ampel/Exit (Ohr/AV) von Lab-PASS unterscheiden
- [ ] Application + `seen_in` nachziehen

## Referenzen

- PiDrive Betrieb: [`MSC-AKTUELL.md`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md)
- Lab/Feld-Artefakte: `pidrive/docs/betrieb/artifacts-2026-10-04-*`

## Offene Fragen (A)

- Welche NBT-Varianten (Evo vs. Evo2, iDrive-Generation) teilen dasselbe USB-Read-Profil?
- Wann reicht Korrelation (Fenster × Bytes) vs. zwingend Ohr-Beweis für „AV PASS“?

## Lessons (Pilot 2 — Zwischenstand)

- Host-Sheet hält Spec sauber: MSC-Sheet bleibt ohne HU-Timing.
- C-Claims leben in Application + Audit, nicht hier.
