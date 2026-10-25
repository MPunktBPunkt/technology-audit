# Project Scope: esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
updated: 2026-10-25
source_repo: https://github.com/MPunktBPunkt/esp32.rfmonitor
reviewed_commit: 739c67a
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `src/` (RfScanner, BleTracker, RfAnalyzer/RfScore, Location/Session, Hub, Web), `docs/RF_SCORE.md`, `docs/OBSERVATION_MODEL.md`, `docs/HUB_CONTRACT.md`, `docs/LOCATION_PROFILE.md`, Lab-Evidence, `platformio.ini` |
| **Nicht in scope** | Spektrumanalyse; toolnode-Module; Presence-Genauigkeit; ioBroker-Adapter-Internals (nur Contract-Spiegel als Exit) |
| **Hardware** | `rfmonitor-mini` (D1 Mini, kein PSRAM) · `rfmonitor-s3` (PSRAM wenn vorhanden) |
| **Version** | `FW_VERSION` **1.5.0** (`RFMON_SCORE_VERSION` 2) |

## Systeme

```text
WLAN APs / BLE Adv ──Scan (sequentiell)──▶ ESP32 RF-Monitor
        │                                      │
        │     observation → derived(proxy) → assessment (score v1∥v2 + DQ)
        │                                      │
        └── Location Profile / Session / Snapshot ──▶ WebUI/SSE + Hub (Contract v2)
```

## Ziel dieses Audit-Laufs

Revalidation unter **Audit-Standard 0.7.1** nach Upstream 1.1→1.5: Observation Model, Score v2, Location/Session, Hub-Contract v2, Lab-Baseline. Kampagne: [`esp32-rfmonitor-2026-v2-validation`](../../audits/esp32-rfmonitor-2026-v2-validation/).
