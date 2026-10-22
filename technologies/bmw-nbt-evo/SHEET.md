# Technology Sheet: BMW NBT Evo (Host-Plattform)

```yaml
slug: bmw-nbt-evo
title: BMW NBT Evo Head Unit — Host-Plattform
primary: I
tags: [automotive, field-verified, usb-host]
type: technology
status: active
seen_in: [pidrive, esp32-bt-gateway, bmw-nbt-media-index, hu-probe]
maturity:
  technology: R2          # Plattform-Rolle verstanden; kein vollständiges HU-Reverse-Engineering
  implementation: R0      # PiDrive spricht HU an — siehe usb-msc Application (B)
  field_evidence: R3      # USB-MSC-Host-Reads/Prefetch vielfach gemessen (PiDrive-Kontext)
  reusability: W1         # stark BMW-/NBT-spezifisch
pilot: audits/pidrive-2026-bmw-hu
```

Ebene **A** (Plattform-Kontext und Abgrenzung). Empirisches **Host-Verhalten** (Reads, Prefetch, Auto-Next, …) → [`applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) (**C**, PiDrive) und [`hu-probe/applications/bmw-nbt-evo.md`](../../projects/hu-probe/applications/bmw-nbt-evo.md) (**C**, unabhängige Sonde: Transport S0/S2 + free + Media-Leiter + Heimfahrt Remount/Scheduler `MEASURED`; Audible/Intent/A8/`seq_size`/Cache-Key weiter offen). MSC-Device-Seite → [`applications/usb-msc.md`](../../projects/pidrive/applications/usb-msc.md) (**B**) / [`hu-probe/…/usb-msc.md`](../../projects/hu-probe/applications/usb-msc.md).  
**Host-Scope:** belegte Plattform = **BMW NBT Evo** (PiDrive-Feld/Lab + hu-probe-Feld 2026-10-15…22). Andere Generationen (Evo2, …) / andere OEMs = `UNKNOWN` bis eigene Evidence — kein stiller Transfer (G17-analog).

## Kurzfassung

**NBT Evo** ist eine BMW-Headunit-Generation mit USB-Host für Massenspeicher (MSC), Bluetooth (A2DP/AVRCP u. a.) und interner Medienwiedergabe. In PiDrive ist sie der **USB-Host**, der den ESP32-MSC-Gadget liest und MP3 dekodiert. Dieses Sheet beschreibt die Plattformrolle — nicht USB-MSC-Spezifikation und nicht PiDrive-Firmware-Details.

## Abgrenzung

- **Ist:** Ziel-Host in PiDrive; USB-MSC-Consumer; Decoder/UI/Playlist-Logik auf HU-Seite (black box mit beobachtbaren I/O-Mustern).
- **Ist nicht:** Allgemeines USB-MSC-Verhalten aller Hosts; SCSI/FAT-Spec; ESP32-Implementierung; Universal-„BMW HU“-Profil.
- **Grenzt an:** [`usb-msc`](../usb-msc/SHEET.md) (Protokoll), [`avrcp`](../avrcp/SHEET.md) / [`pidrive-2026-radio-bt`](../../audits/pidrive-2026-radio-bt/) (BT-Pfad, nicht USB-C duplizieren).

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
| „NBT scannt nur Ordnerstruktur, nie Dateiinhalt“ | `REJECTED` (als FACT) | hu-probe Media-Leiter: Head ~80 KiB typisch; Eager/Neighbor zusätzlich (Heimfahrt) — siehe Application C |
| „Remount = Cold Start / Cache-Flush“ | `REJECTED` (als FACT) | hu-probe Heimfahrt: Kontext-Resume + 395xxx-Probe |
| „Prefetch-Lead = 8 s“ / „globaler Elevator“ | `REJECTED` (als Konstante/Modell) | Lead kontextabhängig; LBA-Scheduler interleaved |
| Lab-Host-Replay ersetzt HU-Beweis | `REJECTED` | Lab AV ≠ Feld-Ohr (PiDrive 2026-10-04) |
| Erfolg = nur SCSI-konforme Antworten | `REJECTED` | HU-Decode + hörbarer Ton ist Projektkriterium |
| MSC und BT können parallel als PiDrive-Ziel laufen | `INFERRED` | Architekturwahl PiDrive; nicht „NBT-Spec“ |
| NBT-Evo-Timing gilt für alle BMW-HU | `REJECTED` (als FACT) | Host-Scope; andere Varianten = Gate/Evidence |
| Lab-Menü-PASS = Feld-Ohr-PASS | `REJECTED` | Exit Ohr bleibt getrennt (siehe Application) |
| Host-BUSY-Toleranz aus MSC-/TinyUSB-Spec ableiten | `REJECTED` | Spec erlaubt Busy; NBT-Akzeptanz ist nur **C** (`EVID-BMWHU-2026-10-12-*`) |
| Dynamische Datei ohne stabile Geometrie/Index | `REJECTED` (als Strategie) | HU erwartet indexierbares, statisch wirkendes Medium — Live-Body muss Read-Muster bedienen (**C**) |

## Community / SIB-Muster (nicht PiDrive-MEASURED)

Öffentliche Foren/SIBs (keine eigenen Lab-IDs) — in Applications nur als `HYPOTHESIS`/`INFERRED` führen, bis gemessen:

| Muster | Epistemic | Hinweis |
|--------|-----------|---------|
| Starkes Caching über Volume-Label + Serial | `HYPOTHESIS` | Änderungen oft erst nach Label-/Stick-Wechsel sichtbar |
| Re-Index durch mehrere unterschiedliche Sticks | `HYPOTHESIS` | Cache-Flush-Ritual |
| FAT32 am zuverlässigsten auf älteren NBT/NBT Evo | `HYPOTHESIS` | exFAT/NTFS problematisch berichtet; PiDrive Lab nutzt FAT12/16 — Gate |
| Track-/Datei-Limits ~6k–26k | `HYPOTHESIS` | generation- und namensabhängig |
| „Reading data“-Hänger bei großen Libs / langsamen Sticks | `HYPOTHESIS` | passt zu Burst/Latenz-These |
| SIB 65 08 07 u. a.: Sync großer Sticks Minuten; HDD-USB abraten | `INFERRED` (secondary) | offizielle Service-Hinweise, nicht KB-remeasured |

## Transfer

Wiederverwendbar als **Vorlage „automotive HU als MSC-Host“**: Trace-Korrelation, Claim-Trennung C vs. MSC-A. Konkrete LBA-/Timing-Profile **nur** mit Evidence aus diesem Host — nicht auf andere Fahrzeuge übertragen. Busy-Pacing am NBT Evo ist **C** belegt (2026-10-12) — keine ms-/Timeout-Zahlen als A-FACT. Revalidation: [`DELTA`](../../audits/pidrive-2026-bmw-hu/DELTA.md).

### Projektstart-Checkliste

- [ ] Host-Variante benennen (NBT Evo vs. andere) — kein stiller Transfer
- [ ] Nur Host-/Feldclaims (C); keine stillen Spec-Transfers nach `usb-msc`/`avrcp`
- [ ] Evidence-IDs aus Betrieb/Lab verlinken
- [ ] Ampel/Exit (Ohr/AV) von Lab-PASS unterscheiden
- [ ] BT/AVRCP nicht als USB-C-Duplikat führen
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
- Busy-Pacing-Feld (2026-10-12) bestätigt: Desk-Semantik ermöglicht den Versuch; Host-Akzeptanz bleibt Field-Fact.
