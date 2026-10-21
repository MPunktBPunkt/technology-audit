# Technology Sheet: ESP32-S3 Silicon / Hardware Limits

```yaml
slug: esp32-s3-silicon
title: ESP32-S3 Silicon Errata & Hardware Limits
primary: D
tags: [esp32s3, silicon, errata, usb-otg, cache, sleep, psram]
type: technology
status: active
seen_in: [esp32-pidrive, hu-probe, pidrive]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-s3-hw-limits-2026
```

Ebene **A**. Projekt-FW-Pins und Session-Politik → Application. Desk:
[`esp32-s3-hw-limits-2026`](../../audits/esp32-s3-hw-limits-2026/).
USB↔WiFi Coex → [`esp32-s3-usb-wifi-coex`](../esp32-s3-usb-wifi-coex/SHEET.md).
MSC-Protokoll → [`usb-msc`](../usb-msc/SHEET.md).

## Kurzfassung

Offizielle Espressif-Errata und begleitende Hardware-Dokumente beschreiben
bekannte ESP32-S3-Silicon-Fehler (Cache, Sleep/Analog, USB-OTG Download, RTC,
LCD, RMT, Touch, ADC2-DMA) inklusive betroffener Revisionen und Software-
Workarounds. Community-Issues (PSRAM, GDMA, USB-Disconnect) sind **Signale**,
keine Ersatz-Errata.

## Abgrenzung

- **Ist:** Chip-Errata-Karte, Revision/Date-Code-Hinweise, IDF-Bypass-Versionen,
  Verweis auf Datasheet/TRM/HW-Design-Guidelines.
- **Ist nicht:** Task-/PHY-Coex-Navigationskarte (→ `esp32-s3-usb-wifi-coex`);
  MSC/BOT-Protokoll; Root-Cause eines konkreten Gadgets; Forums-Thermik ohne Pin;
  „USB Light-Sleep Freeze“ als Silicon-FACT ohne Errata-Eintrag.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | App / FW (USB Device, Sleep, PSRAM) | Workarounds oft in IDF |
| seitlich | USB-Serial-JTAG vs USB-OTG | eFuse / PHY-Select |
| unten | Silicon Rev v0.0 / v0.1 / v0.2 | Summary-Spalten |
| parallel | Datasheet, TRM, HW Design Guidelines | elektrische/Timing-Limits |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| CACHE-126 Write-Back Hit-Fehler; No fix; IDF-Bypass | `FACT` | Errata |
| ANALOG-160 kann Chip zerstören (BIAS_SLEEP∧PD_CUR) | `FACT` | Errata; Safety-Gate |
| RTC-126 nach Light-Sleep; RTC nicht power-down | `FACT` | Errata |
| USBOTG-4289: alte Batches ohne OTG Download | `FACT` | Date Code / PW |
| Light-Sleep + USB-MSC Freeze = Silicon-Erratum | `REJECTED` | nicht in S3-Summary |
| GDMA I2S→AES = Silicon-Erratum | `REJECTED` | IDF Issue Won't Do / Driver |
| 16 MB Octal-PSRAM offiziell supported | `REJECTED` | jumbo PoC + Timing-Warnung |
| Verbautes PSRAM = automatisch genutzt | `REJECTED` | braucht `BOARD_HAS_PSRAM` + passendes `memory_type` (qio_qspi vs qio_opi); sonst `getPsramSize()==0` |
| Issue-Tracker-Titel = Root-Cause Projekt X | `REJECTED` | Epistemik |

## Errata-Orientierung (S3)

| ID | Thema | Fix | Typischer Bypass |
|----|-------|-----|------------------|
| CACHE-126 | Cache Write-Back | No fix | IDF ≥ v5.2 / gelistete LTS |
| RTC-126 | RTC-Read nach Light-Sleep | No fix | IDF ≥ v4.4 |
| ANALOG-160 | Sleep-Analog zerstört Chip | No fix | IDF ≥ v5.0 / v4.4.2 |
| USBOTG-4289 | OTG Download eFuse | Teil-Batches v0.2 | USB-Serial-JTAG |
| LCD-239 / RMT-176 / TOUCH-100 / ADC-183 | Peripheral | No fix | siehe Errata |

Vollständige Texte: [ESP32-S3 Chip Errata](https://docs.espressif.com/projects/esp-chip-errata/en/latest/esp32s3/) · Repo-Pin in Audit-Evidence.

## Transfer

- Jedes S3-Projekt mit **Sleep**, **USB-OTG** oder **Dual-Core+Cache**: Errata-Karte
  und IDF-Mindestversion vor Optimismus aus Issues.
- USB-Device + WiFi unter Last: zusätzlich `esp32-s3-usb-wifi-coex`.
- PSRAM/Octal: Issue-Signale beobachten; DMA-Buffer bevorzugt internal RAM.
  Modulvariante (R2 quad vs R8 octal) muss zum Build passen — hu-probe Feld **N8R2**
  (`qio_qspi`, 1 MiB Offline-Capture): Audit
  [`hu-probe-psram-board-free-2026-10-21`](../../audits/hu-probe-psram-board-free-2026-10-21/).

### Projektstart-Checkliste

- [ ] Sheet gelesen (Abgrenzung + Fallstricke)
- [ ] Chip-Revision / Date Code der Hardware notiert
- [ ] IDF/Arduino-Version gegen CACHE/ANALOG/RTC-Bypass geprüft
- [ ] Sleep-Politik (an/aus) für USB-Sessions entschieden
- [ ] Application mit Projekt-Pin; keine Issue→FACT-Kurzschlüsse
- [ ] `seen_in` ergänzt

## Quellen / Evidence

Pilot: [`esp32-s3-hw-limits-2026`](../../audits/esp32-s3-hw-limits-2026/) ·
`EVID-S3HW-2026-10-18-001` … `015`.
