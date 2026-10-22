# Project Inventory: hu-probe

```yaml
project_id: hu-probe
updated: 2026-10-22
reviewed_commit: "FW 0.3.17 / hu-probe@4fdf519 (Heimfahrt + Media-Leiter); prior PSRAM f985459 / free 0.2.40 retained"
profile: lab-tool
pilot_order: [esp32-s3-usb-wifi-coex, usb-msc, bmw-nbt-evo, esp32-s3-silicon]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| USB MSC TinyUSB Device | `usb-msc` | applied (BOT/Control + Feld-Transport + 1 MiB Offline + Trip-Replay 0.3.17) |
| S3 USB OTG + WiFi STA unter Last | `esp32-s3-usb-wifi-coex` | applied (Coex-Desk; Lab Recovery; PSRAM ≠ Heilung; Live-Leiter OBSERVED) |
| BMW NBT Host | `bmw-nbt-evo` | applied (Transport + free + Media-Leiter + Heimfahrt Remount/Scheduler MEASURED; Audible/Identity/A8 OPEN) |
| S3 Board / PSRAM / Flash | `esp32-s3-silicon` | documented → applied light (N8R2 field pin) |
| Virtual FAT Demo | `virtual-fat` | reuse (Medium/Slots) |

Kampagnen: [`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/) ·
[`msc-host-read-semantics-s1s2s3-2026`](../../audits/msc-host-read-semantics-s1s2s3-2026/) ·
[`hu-probe-bmw-s0s2-field-2026`](../../audits/hu-probe-bmw-s0s2-field-2026/) ·
[`hu-probe-bmw-s2-abend-offline-2026-10-18`](../../audits/hu-probe-bmw-s2-abend-offline-2026-10-18/) ·
[`hu-probe-psram-board-free-2026-10-21`](../../audits/hu-probe-psram-board-free-2026-10-21/) ·
[`hu-probe-media-ladder-2026-10-22`](../../audits/hu-probe-media-ladder-2026-10-22/) ·
[`hu-probe-heimfahrt-2026-10-22`](../../audits/hu-probe-heimfahrt-2026-10-22/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp32-s3-usb-wifi-coex` | S3 USB↔WiFi Coex | D | `esp32s3`, `wifi`, `usb-device` | applied | partial | [SHEET](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) | [app](applications/esp32-s3-usb-wifi-coex.md) |
| `esp32-s3-silicon` | S3 Silicon / Board / PSRAM | D | `esp32s3`, `errata`, `psram` | applied | partial | [SHEET](../../technologies/esp32-s3-silicon/SHEET.md) | [app](applications/esp32-s3-silicon.md) |
| `usb-msc` | USB MSC Device | C | `usb-device` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `bmw-nbt-evo` | BMW NBT Evo Host | I | `automotive`, `usb-host` | applied | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | [app](applications/bmw-nbt-evo.md) |

## Nach Kategorie

### C — Protokolle

- `usb-msc` — applied / partial (Instrument + Feld-Transport + PSRAM Offline + Trip-Replay)

### D — Embedded

- `esp32-s3-usb-wifi-coex` — applied / partial
- `esp32-s3-silicon` — applied / partial (N8R2 + PSRAM Build/Feld)

### I — Plattformen / Hosts

- `bmw-nbt-evo` — applied / partial (Transport + free + Media-Leiter Phasen; A8/Cache-Key offen)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Lab Power/Starve/RF | Desk/Lab Recovery only | Method `usb-wifi-coex-discrimination` |
| Formal A8 / `seq_size` | Leiter ≠ Formal | H-A/B/C auswerten |
| audible / GATE-01 Lead | kein Anker | Operator-Tap |
| Analyzer B47 | Scan in Prefetch-Stats | Fenster markieren |
| Cache-Key Replug | n=1 Resume | `ident_b` |
| Lab Offline Replay B50 | FAIL trotz Records | `.88` vs `.89` |
| HARDWARE.md §2.3 | Doc-Drift | Upstream-Fix |

## Signale ohne Eintrag

- StatusLed / EventBus / TcpStreamer — App-Schicht, kein neuer Slug
- WiFiManager Portal — observed
- TripStore / DriveMode 0.3.x — unter `usb-msc` Instrument (0.3.17 Upload PASS)
- Virtual FAT — reuse ohne eigene Application (Medium über usb-msc)
