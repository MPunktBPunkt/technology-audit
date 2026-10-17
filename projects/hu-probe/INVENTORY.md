# Project Inventory: hu-probe

```yaml
project_id: hu-probe
updated: 2026-10-15
reviewed_commit: "FW 0.2.23 / hu-probe@5dbec43 (S0 0.2.17 + S2 Feld + Lab offline); Coex-Pin 0.2.15"
profile: lab-tool
pilot_order: [esp32-s3-usb-wifi-coex, usb-msc, bmw-nbt-evo]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| USB MSC TinyUSB Device | `usb-msc` | applied (BOT/Control + Feld-Transport) |
| S3 USB OTG + WiFi STA unter Last | `esp32-s3-usb-wifi-coex` | applied (Coex-Desk; Feld-Symptom bestätigt) |
| BMW NBT Host | `bmw-nbt-evo` | applied (hu-probe C: Transport; Semantik INFERENCE) |
| Virtual FAT Demo | `virtual-fat` | reuse (Medium/Slots S1) |

Kampagnen: [`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/) ·
[`msc-host-read-semantics-s1s2s3-2026`](../../audits/msc-host-read-semantics-s1s2s3-2026/) ·
[`hu-probe-bmw-s0s2-field-2026`](../../audits/hu-probe-bmw-s0s2-field-2026/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `esp32-s3-usb-wifi-coex` | S3 USB↔WiFi Coex | D | `esp32s3`, `wifi`, `usb-device` | applied | partial | [SHEET](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) | [app](applications/esp32-s3-usb-wifi-coex.md) |
| `usb-msc` | USB MSC Device | C | `usb-device` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `bmw-nbt-evo` | BMW NBT Evo Host | I | `automotive`, `usb-host` | applied | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | [app](applications/bmw-nbt-evo.md) |

## Nach Kategorie

### C — Protokolle

- `usb-msc` — applied / partial (Instrument + Feld-Transport)

### D — Embedded

- `esp32-s3-usb-wifi-coex` — applied / partial

### I — Plattformen / Hosts

- `bmw-nbt-evo` — applied / partial (Transport MEASURED; Prefetch/Eager/Cache offen)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Lab Power/Starve/RF | Desk only | Method `usb-wifi-coex-discrimination` |
| S1/S3 Semantik-Formal | S2 Transport ja; LBA/Marker-Formal nein | Method + P0b |
| Profil P1c Upstream | **done 2026-10-17** schema 3 / `hu_probe_field` Transport | hu-probe `bmw_nbt_evo.json` |
| Auto Offline | Lab PASS / BMW FAIL | P0c Diagnose |
| GATE-01 unbroken Timeline | fragmentiert | Burst-Epistemik / Offline |

## Signale ohne Eintrag

- StatusLed / EventBus / TcpStreamer — App-Schicht, kein neuer Slug
- WiFiManager Portal — observed
- Virtual FAT — reuse ohne eigene Application (Medium über usb-msc)
