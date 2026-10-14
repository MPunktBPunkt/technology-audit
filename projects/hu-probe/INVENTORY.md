# Project Inventory: hu-probe

```yaml
project_id: hu-probe
updated: 2026-10-14
reviewed_commit: "FW 0.2.15 / platformio espressif32@6.4.0"
profile: lab-tool
pilot_order: [esp32-s3-usb-wifi-coex, usb-msc]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| USB MSC TinyUSB Device | `usb-msc` | reuse (Control/BOT-Kampagnen) |
| S3 USB OTG + WiFi STA unter Last | `esp32-s3-usb-wifi-coex` | **neu** |
| BMW NBT Host | `bmw-nbt-evo` | observed / nicht vertieft hier |
| Virtual FAT Demo | `virtual-fat` | candidate (nicht dieser Lauf) |

Kampagne: [`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp32-s3-usb-wifi-coex` | S3 USB↔WiFi Coex | D | `esp32s3`, `wifi`, `usb-device` | applied | partial | [SHEET](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) | [app](applications/esp32-s3-usb-wifi-coex.md) |
| `usb-msc` | USB MSC Device | C | `usb-device` | documented | none | [SHEET](../../technologies/usb-msc/SHEET.md) | — (Reuse via BOT/Control) |

## Nach Kategorie

### C — Protokolle

- `usb-msc` — documented / Coverage none in diesem Projektlauf (Wissen in usb-bot-observation)

### D — Embedded

- `esp32-s3-usb-wifi-coex` — applied / partial

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Lab Power/Starve/RF | Desk only | Method `usb-wifi-coex-discrimination` |
| `usb-msc` Application hu-probe | Coex priorisiert | optional nach Lab |
| Auto-HU WiFi-Kill | Feld nach Lab | Session-Evidence |

## Signale ohne Eintrag

- StatusLed / EventBus / TcpStreamer — App-Schicht, kein neuer Slug
- WiFiManager Portal — observed
