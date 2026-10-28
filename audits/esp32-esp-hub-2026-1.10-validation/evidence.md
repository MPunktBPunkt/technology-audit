# Evidence — esp32-esp-hub-2026-1.10-validation

Desk-Revalidation 2026-10-28 @ `eebbcd9` (FW **1.10.5**) · Upstream Lab A/B 2026-10-27 zitiert · **standard_version 0.7.1**.

Basis: `https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-BASE-2026-10-28-001` | Vorlage = Ordner `esp-hub-base/`; anpassen: `ProjectConfig.h` + `.ino`-Zonen; `src/core/` Plattform | `FACT` | [README Sketch-Struktur](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/README.md) · [`ProjectConfig.h`](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/esp-hub-base/ProjectConfig.h) · [`esp-hub-base.ino`](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/esp-hub-base/esp-hub-base.ino) |
| `EVID-BASE-2026-10-28-002` | M0–M11 abgeschlossen; Erweiterung über BaseModule (M10) | `FACT` | [docs/update/README](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/docs/update/README.md) · [M10_BASEMODULE](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/docs/update/M10_BASEMODULE.md) · `src/core/BaseModule.h` |
| `EVID-BASE-2026-10-28-003` | Derived A/B-Rollout (≥8 Nodes) laborgeprüft; HI/CpuLoad byte-identisch (außer Ergo-HwInfo) | `FACT` (Lab, Upstream) | [ROLLOUT_DERIVED](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/docs/update/ROLLOUT_DERIVED.md) · [AUDIT_BASE_A-B](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/docs/update/AUDIT_BASE_A-B_2026-10-27.md) |
| `EVID-BASE-2026-10-28-004` | Diag/Recovery/ProgressWatch/Checkpoint = Base-only; nicht A/B-Pflicht | `FACT` | AUDIT_BASE_A-B §Urteil / §1 Diag-APIs |
| `EVID-HUB-2026-10-28-001` | Heartbeat schlank: Basis + `freePsram`/`psramSize`; Diag nicht im Register | `FACT` | [README Heartbeat](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/README.md) · [`HubClient.cpp`](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/esp-hub-base/src/core/HubClient.cpp) · ADR/AUDIT |
| `EVID-HUB-2026-10-28-002` | Hub-Reply Keys: `interval`, `otaUrl`, `name` (Rename→NVS) | `FACT` | HubClient.cpp Reply-Parser · AUDIT_BASE_A-B §Hub-Reply · VERIFICATION_CHECKLIST |
| `EVID-HUB-2026-10-28-003` | Additive Status/HB: `hwSummary` / `module` / `cpu*` erlaubt, schlank | `FACT` | HardwareInfo Status-JSON · AUDIT_BASE_A-B · WebUi `/api/status` |
| `EVID-WEB-2026-10-28-001` | Web-UI: `web/index.html` → `pack_ui.py` → gzip PROGMEM (`UiPagesGz.h`), `Content-Encoding: gzip` | `FACT` | [WEBUI_GZ](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/docs/update/WEBUI_GZ.md) · [`WebUi.cpp`](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/esp-hub-base/src/core/WebUi.cpp) |
| `EVID-WEB-2026-10-28-002` | SSE `/events` (`text/event-stream`) weiter Teil der Status-UI | `FACT` | WebUi.cpp SSE-Header · VERIFICATION_CHECKLIST |
| `EVID-BASE-2026-10-09-001` | Änderungszonen-Idee (Pilot) | `FACT` | Prior — strukturell ersetzt/ konkretisiert durch `EVID-BASE-2026-10-28-001` |
| `EVID-BASE-2026-10-09-002` | Bin-Namen `{projekt}.{ver}.esp32[.s3].bin` | `FACT` | Prior + README 1.10.5 |
| `EVID-HUB-2026-10-09-070` | Heartbeat-Basisfelder | `FACT` | Prior — bestätigt/ erweitert durch `EVID-HUB-2026-10-28-001` |
| `EVID-HUB-2026-10-09-071` | Identity ohne fwType-Pflicht | `FACT` | Prior — weiter gültig |
| `EVID-WEB-2026-10-09-050` | SSE Status | `FACT` | Prior — bestätigt durch `EVID-WEB-2026-10-28-002` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| BOOT 3 s WLAN-Reset im Feld | `UNKNOWN` | physisch; Upstream Verification offen |
| Hub-`interval` Config-Wechsel End-to-End (Admin→Gerät) | `HYPOTHESIS` / Teil-PASS Upstream | Default 30 s beobachtet; expliziter Wechsel nicht gefahren |
| Adapter spiegelt alle additiven Keys | `UNKNOWN` | eigene Adapter-Kampagne |
| Partition Minimal SPIFFS Feldbestätigung | `UNKNOWN` | Pilot-Rest |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-09 | Pilot Desk @ `a03400a` / FW 1.7.0 · Standard 0.6.3 |
| 2026-10-27 | Upstream Base 1.10.5 + Derived A/B Freeze (Lab) |
| 2026-10-28 | KB-Revalidation unter Standard 0.7.1 @ `eebbcd9` |
