# Project Inventory: hu-probe

```yaml
project_id: hu-probe
updated: 2026-10-15
reviewed_commit: "FW 0.2.17 / hu-probe@463c0f0 (S1–S3 Desk); Coex-Pin 0.2.15"
profile: lab-tool
pilot_order: [esp32-s3-usb-wifi-coex, usb-msc]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| USB MSC TinyUSB Device | `usb-msc` | reuse (BOT/Control + S1–S3 Messplan) |
| S3 USB OTG + WiFi STA unter Last | `esp32-s3-usb-wifi-coex` | applied (Coex-Desk) |
| BMW NBT Host | `bmw-nbt-evo` | observed; Claims via PiDrive-Audits, S1–S3 `needs_field` |
| Virtual FAT Demo | `virtual-fat` | reuse (Medium/Slots S1) |

Kampagnen: [`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/) ·
[`msc-host-read-semantics-s1s2s3-2026`](../../audits/msc-host-read-semantics-s1s2s3-2026/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp32-s3-usb-wifi-coex` | S3 USB↔WiFi Coex | D | `esp32s3`, `wifi`, `usb-device` | applied | partial | [SHEET](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) | [app](applications/esp32-s3-usb-wifi-coex.md) |
| `usb-msc` | USB MSC Device | C | `usb-device` | documented | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | — (BOT/Control + Method S1–S3) |

## Nach Kategorie

### C — Protokolle

- `usb-msc` — documented / partial (BOT/Control-Reuse + S1–S3-Messplan-Method)

### D — Embedded

- `esp32-s3-usb-wifi-coex` — applied / partial

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Lab Power/Starve/RF | Desk only | Method `usb-wifi-coex-discrimination` |
| S1–S3 Feldzahlen | Messplan Desk-only | Method `msc-host-read-semantics` |
| `usb-msc` Application hu-probe | noch kein App-File | nach ersten S1–S3-Sessions |
| Auto-HU WiFi-Kill | Feld nach Lab | Session-Evidence |

## Signale ohne Eintrag

- StatusLed / EventBus / TcpStreamer — App-Schicht, kein neuer Slug
- WiFiManager Portal — observed
