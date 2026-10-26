# Project Scope: esp32.rfmonitor

```yaml
project_id: esp32-rfmonitor
updated: 2026-10-26
source_repo: https://github.com/MPunktBPunkt/esp32.rfmonitor
reviewed_commit: afcd137
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `src/` (RfScanner, BleTracker, RfAnalyzer/RfScore, Location/Session/Motion, History, Hub, Web), `docs/RF_SCORE.md`, `docs/OBSERVATION_MODEL.md`, `docs/HUB_CONTRACT.md`, `docs/LOCATION_PROFILE.md`, `docs/MOTION_SENSITIVITY.md`, `docs/SCORE_CHARACTERIZATION.md`, Lab-/Küchen-Evidence, `platformio.ini`, Host-Tools (`rf-characterize`, `rf-motion-characterize`, Replay) |
| **Nicht in scope** | Spektrumanalyse; CSI; Promiscuous/PCAP; toolnode-Module; Presence-Genauigkeit; ioBroker-Adapter-Internals (nur Contract-Spiegel als Exit) |
| **Hardware** | `rfmonitor-mini` (D1 Mini, kein PSRAM) · `rfmonitor-s3` (PSRAM wenn vorhanden) |
| **Version** | `FW_VERSION` **1.10.2** (`RFMON_SCORE_VERSION` 2) |

## Systeme

```text
WLAN APs / BLE Adv ──Scan (sequentiell)──▶ ESP32 RF-Monitor
        │                                      │
        │     observation → derived(proxy) → assessment (score v1∥v2 + DQ)
        │                                      │
        ├── Location Profile / Session Profiles / Snapshot
        ├── Channel + multi-res History / AP Lifetime / Alerts
        └── Own-Link fein (always-on) + Motion-Session (CAL/W1/W2)
                                              │
                                    WebUI/SSE + Hub (Contract v2)
```

## Ziel dieses Audit-Laufs

Delta **1.5.0 → 1.10.2** unter Audit-Standard 0.7.1: Motion Own-Link, Characterization, History/AP-Events; Presence-Drift verhindern. Kampagne: [`esp32-rfmonitor-2026-motion-delta`](../../audits/esp32-rfmonitor-2026-motion-delta/).
