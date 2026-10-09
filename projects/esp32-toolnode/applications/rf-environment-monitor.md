# Project Application: rf-environment-monitor in esp32.toolnode

```yaml
project_id: esp32-toolnode
tech_slug: rf-environment-monitor
status: active
sheet: ../../../technologies/rf-environment-monitor/SHEET.md
audit: ../../../audits/esp32-toolnode-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

**Geschwister** zu rfmonitor: RF als **Modul** (`ScannerModule`, `RfHealthModule`), nicht Einzweck-Firmware. WLAN-Scan + RF-Score/History; BLE default **aus** (`TOOLNODE_ENABLE_BLE=0` auf Mini).

## Architektur / Datenfluss

```text
WiFi.scanNetworks(async) ──▶ ScannerModule ──▶ HistoryStore / RfHealth score ──▶ Hub IO + Web Charts
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/modules/ScannerModule.*` | WLAN-Scan |
| `src/modules/RfHealthModule.*` | Score |
| `src/core/HistoryStore.*` | RSSI/Score/AP |
| `docs/ARCHITECTURE.md` | Hub-IO `rf_score` |

## Abweichungen zu rfmonitor

| Aspekt | rfmonitor | toolnode |
|--------|-----------|----------|
| Produktzuschnitt | Einzweck | Modul im Host |
| BLE Adv-Scan | ja (sequentiell) | default aus |
| `fwType` | `rfmonitor` | `toolnode` (+ enabledModules) |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| WLAN-Scan + RF-Health Module | `EVID-RF-2026-10-09-010` | `FACT` |
| BLE default disabled Mini | `EVID-RF-2026-10-09-011` | `FACT` |
| Score-Formel = rfmonitor v1 | — | `UNKNOWN` |

## Verwandte

- Sheet [rf-environment-monitor](../../../technologies/rf-environment-monitor/SHEET.md) · App rfmonitor
