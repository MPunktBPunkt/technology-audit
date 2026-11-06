# Project Inventory: esp32.usb-analyzer

```yaml
project_id: esp32-usb-analyzer
updated: 2026-11-06
reviewed_commit: 688a40b
profile: lab-tool
pilot_order: [usb-dual-esp-observe-proxy, usb-msc, usb-msc-host-behaviour, esp-usb-host, usb-aoa]
```

**Evidence-Update** 2026-11-06 @ `688a40b` (FW **0.0.52** Feld Host-Matrix).  
Prior Soft-Lab 2026-11-02 @ `60244b3` (FW **0.0.50**, Controller **0.0.41**).  
Prior Pilot 2026-10-31 @ `b2c9987` (0.0.35).  
Ursprungsrepo: [esp32.usb-analyzer](https://github.com/MPunktBPunkt/esp32.usb-analyzer) (read-only).  
Kampagnen: [field-host-matrix](../../audits/esp32-usb-analyzer-2026-field-host-matrix/) · [0.0.50](../../audits/esp32-usb-analyzer-2026-0.0.50/) · [pilot](../../audits/esp32-usb-analyzer-2026-pilot/).  
Methods: [usb-otg-loop-baseline](../../methods/usb-otg-loop-baseline.md) · [usb-msc-host-fingerprint](../../methods/usb-msc-host-fingerprint.md).  
Reuse: [docs/REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md).

**Match (Signal → Slug):**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Dual-ESP Host+Device + Debian Control / Capture | `usb-dual-esp-observe-proxy` | wachsen (Path-A kill, Observer, Harness) |
| MSC Device gadget + BOT class-hook | `usb-msc` | wachsen (Lab rates + Feld WRITE gap) |
| Fremd-Host MSC Fingerprints (HU/Windows/…) | `usb-msc-host-behaviour` | **neu** (Evidence-Update 2026-11-06) |
| BMW NBT Evo als MSC-Host (P-MOUNT) | `bmw-nbt-evo` | wachsen (Feld App Analyzer) |
| ESP OTG Host enum / MSC / HID / AOA Host | `esp-usb-host` | wachsen (Capability Enum) |
| AOA 51→52→53 + MSC-Identity-Gate | `usb-aoa` | wachsen (Feld Negativ `303a:1001`) |
| BCL 8-byte BE Framing über AOA-Bulk | `bmw-bcl` | unverändert — **Lab Rohr**, nicht HU-Wire |
| USB↔WiFi Datenrate Mode A / Pipeline | `esp32-s3-usb-wifi-coex` | Application (Bottleneck + Pipeline) |
| YD-ESP32-S3 N8R2 / OTG PHY / GPIO19-20 | `esp32-s3-silicon` | Application light (Path-A PHY note) |
| Hub register / OTA Stufe A | `esp-hub-telemetry` | Application light |
| Node Web UI / SSE | `esp-embedded-web-sse` | observed |
| HID interrupt inject/observe | — | Signal unter Host/Device Apps |
| Debian Lab UI `:8080` | — | Teil von `usb-dual-esp-observe-proxy` (B) |

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `usb-dual-esp-observe-proxy` | Dual-ESP USB Observe/Proxy Lab | H | `lab-only`, `usb`, `esp32s3` | applied | partial | [SHEET](../../technologies/usb-dual-esp-observe-proxy/SHEET.md) | [app](applications/usb-dual-esp-observe-proxy.md) |
| `usb-msc` | USB Mass Storage Class | C | `usb-device`, `lab-only` | applied | partial | [SHEET](../../technologies/usb-msc/SHEET.md) | [app](applications/usb-msc.md) |
| `usb-msc-host-behaviour` | USB MSC Host Behaviour / Fingerprinting | C | `usb-host`, `field-verified` | applied | partial | [SHEET](../../technologies/usb-msc-host-behaviour/SHEET.md) | [app](applications/usb-msc-host-behaviour.md) |
| `bmw-nbt-evo` | BMW NBT Evo Host | I | `automotive`, `usb-host` | applied | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | [app](applications/bmw-nbt-evo.md) |
| `esp-usb-host` | ESP32 USB Host OTG | C | `usb-host`, `esp32s3` | applied | partial | [SHEET](../../technologies/esp-usb-host/SHEET.md) | [app](applications/esp-usb-host.md) |
| `usb-aoa` | USB AOA | C | `usb-host`, `lab-only` | applied | partial | [SHEET](../../technologies/usb-aoa/SHEET.md) | [app](applications/usb-aoa.md) |
| `bmw-bcl` | BMW BCL Framing | H | `automotive`, `lab-only` | applied | partial | [SHEET](../../technologies/bmw-bcl/SHEET.md) | [app](applications/bmw-bcl.md) |
| `esp32-s3-usb-wifi-coex` | S3 USB↔WiFi Coex | D | `wifi`, `usb` | applied | partial | [SHEET](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md) | [app](applications/esp32-s3-usb-wifi-coex.md) |
| `esp32-s3-silicon` | S3 Silicon / Board | D | `esp32s3` | applied | partial | [SHEET](../../technologies/esp32-s3-silicon/SHEET.md) | [app](applications/esp32-s3-silicon.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `iobroker` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | observed | none | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | — |

## Nach Kategorie

### C — Protokolle

- `usb-msc`, `usb-msc-host-behaviour`, `esp-usb-host`, `usb-aoa` — applied / partial (Lab + Feldmatrix)

### I — Plattform / Host

- `bmw-nbt-evo` — applied / partial (P-MOUNT Feld am Analyzer)

### D — Embedded

- `esp32-s3-usb-wifi-coex`, `esp32-s3-silicon` — applied / partial

### F / G — Integration / UI

- `esp-hub-telemetry` — applied light · `esp-embedded-web-sse` — observed

### H — Test / Analyse

- `usb-dual-esp-observe-proxy`, `bmw-bcl` (Lab-Framing only)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Transparent MITM | Observer-Loop MEASURED ≠ Transparenz | Kontroll-Host Baseline Method |
| Hard Sync µs | nur Offset-Estimate | Gate 8 / REJECT hard-lock |
| Live L0 D+/D− | Path A REJECTED; Path-B HW offen | Hardware Path-B, kein Sheet-Inflation |
| HU AOA positiv / BCL Wire | MSC-Identity Negativ; Trigger `UNKNOWN` | **C1** phone-like Identity |
| C0 FAT Content | Pattern-Stick ≠ Media-UI | FAT/Media unter gleicher Identity |
| Write-Cache Eviction | 106 Sektoren vs 64 Slots | Write-LBA-Audit (Upstream P0-F) |
| Store-and-Forward | TCP≪USB bleibt | `STORE_FORWARD.md` Upstream wenn Proxy-Last |
| Host-Klassen GENERAL | n=1 TV/Soundbar/FRITZ | Wiederholung; bis dahin Project Evidence |
| Debian Web UI Application | observed Pattern | App nur bei Transferbedarf |

## Signale ohne Eintrag

- RGB/WS2812 Identify — Board-UI, kein Slug
- Soft-composite MSC+Vendor+HID — Implementation unter Device-Apps
- Capture schema `docs/schemas/` — Teil des Observe-Proxy Sheets
- Foreign-DUT Visibility (pidrive/hu-probe) — Cross-Repo Lab; kein neuer Slug
- Soft Path-B / L0-Sim Pipeline — unter Observe-Proxy, kein Live-Wire-Claim
- TV/Soundbar/FRITZ Rohprofile — Project Evidence under `usb-msc-host-behaviour`, kein eigener Slug
