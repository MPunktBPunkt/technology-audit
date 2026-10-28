# Project Scope: ESP32.esp-hub

```yaml
project_id: esp32-esp-hub
updated: 2026-10-28
source_repo: https://github.com/MPunktBPunkt/ESP32.esp-hub
reviewed_commit: eebbcd9
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `esp-hub-base/` (ProjectConfig, `.ino`-Ableiten-Zonen, `src/core/` AppCore/Hub/Web/OTA/Lifecycle), README Ableiten, `docs/update/` (M0–M11, A/B-Freeze, ROLLOUT, WEBUI_GZ) |
| **Nicht in scope** | Adapter-Internals; Fachmodule abgeleiteter Repos; Stufe C/D Diag in Derived; pidrive/hu-probe |
| **Hardware / Runtime** | ESP32 / ESP32-S3 (N8R2 u. a.) |
| **Version** | `FW_VERSION` **1.10.5** (Baseline-Freeze-Bins 1.8.0) |

## Systeme

```text
esp-hub-base (AppCore)
  ──WiFiManager──▶ STA
  ──POST /api/register──▶ iobroker.esp-hub :8093
       ◀── interval / otaUrl / name
  ──Web gzip-UI + SSE + /ota──▶ Browser
  ──Base-only: DiagLog / Recovery / Checkpoint──▶ /api/diag/*
```

## Ziel dieses Audit-Laufs

Revalidation unter **Audit-Standard 0.7.1**: Template nach M0–M11, Contract-Additive, gzip-UI, Derived A/B als Reuse-Beweis. Kampagne: [`esp32-esp-hub-2026-1.10-validation`](../../audits/esp32-esp-hub-2026-1.10-validation/).
