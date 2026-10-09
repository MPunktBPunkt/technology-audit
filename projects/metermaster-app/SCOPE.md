# Project Scope: MeterMaster-App

```yaml
project_id: metermaster-app
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/MeterMaster-App
reviewed_commit: 80e3fe0
profile: ops-field
```

## Grenzen

| | |
|--|--|
| **In scope** | App-Struktur (MAUI), Core/Tests, Submodule-Verdrahtung, Integrationspfade |
| **Nicht in scope** | Adapter-/ESP-Quellpflege (eigene Repos); Play-Store-Marketingtexte im Detail |
| **Nicht dieses Repo** | Öffentliches Landing [`MeterMaster`](https://github.com/MPunktBPunkt/MeterMaster) (Privacy) |
| **Version** | App v2.8.3 (Build 75) laut README |

## Systeme

```text
Android App ──HTTP──▶ ioBroker.metermaster :8089
optional ESP32 OLED ◀── Adapter Node-API
Submodule pinnt Adapter/ESP Release-Tags
```
