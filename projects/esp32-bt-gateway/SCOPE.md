# Project Scope: esp32.bt-gateway

```yaml
project_id: esp32-bt-gateway
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.bt-gateway
reviewed_commit: 7a7e8a4
profile: planning
```

## Grenzen

| | |
|--|--|
| **In scope** | `README.md`, `STATE.md`, `docs/planung/*` (Konzept, Pflichtenheft V2, Hub, AVRCP, Messplan, Flash-Budget, Reviews) |
| **Nicht in scope** | Nicht existierende Firmware; Hub-Internals; PiDrive-Geschäftslogik; medizinische Claims |
| **Hardware (geplant)** | klassischer ESP32 WROOM-32 (Plan B WROVER); Dual-OTA ~1,9 MB Slots |
| **Firmware** | **nicht gestartet** (A17 Host-Stack offen; Q12 Build-Host) |

## Systeme

```text
Client (PiDrive) ──PDAP (PCM+Meta+Cmd+Menu)──▶ ESP32 Gateway
                                                │ A2DP Source + AVRCP Target
                                                ▼
                                             Sink (BMW NBT Evo / …)
                     ▲
ESP-Hub (Heim) ──────┘ USB-Flash / OTA-Pull
```

## Ziel dieses Audit-Laufs

Planungsstand in die Wissensbasis: bestehende Slugs matchen (`esp-hub-telemetry`, `bmw-nbt-evo`), Spec-/Muster-Sheets für A2DP/AVRCP/PDAP anlegen, offene Gates (A17, Phase −1, Flash-Budget) als Exit führen — **ohne** Mess-Claims zu erfinden.
