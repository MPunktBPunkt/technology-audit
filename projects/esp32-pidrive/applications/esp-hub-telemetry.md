# Project Application: esp-hub-telemetry in esp32.pidrive

```yaml
project_id: esp32-pidrive
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-pidrive-2026-pilot/
maturity:
  technology: R4
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

Dünner Arduino-`HubClient`: `POST /api/register` mit `fwType=pidrive`, `chipModel=esp32s3`, `ios` (USB/PUMP/OTA). OTA aus Heartbeat-`otaUrl` sowie lokales SoftAP `/ota-upload`. Dist: `pidrive.<ver>.{usb,ota}.esp32s3.bin`.

## Architektur / Datenfluss

```text
buildHeartbeat ──POST /api/register──▶ hub :8093
Response interval / otaUrl ──▶ HubClient::performOta (HTTP GET + Update)
SoftAP POST /ota-upload ──▶ lokaler OTA-Pfad (Stufe 2)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `src/core/HubClient.*` | Register + otaUrl-Konsum |
| `src/app/App.cpp` `buildHeartbeat` | Identity + ios |
| `include/BuildFlags.h` | `FW_TYPE`, Hub-Defaults |
| `docs/planung/HUB-INTEGRATION.md` | Planung (teilweise veraltet: IDF vs. Arduino) |
| `dist/pidrive.*.esp32s3.bin` | usb/ota Artefakte |

## Konfiguration und Parameter

| Feld | Wert | Epistemic |
|------|------|-----------|
| `hwType` | `esp32` | `FACT` |
| `chipModel` | `esp32s3` | `FACT` |
| `fwType` | `pidrive` (`FW_TYPE`) | `FACT` |
| Hub-Default | `192.168.178.113:8093` | `FACT` (Build-Default) |
| ios (Auszug) | `usbEnumerated`, `pumpState`, `bufferMs`, `otaState`, SoftAP | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Heartbeat enthält fwType + chipModel esp32s3 | `EVID-HUB-2026-10-09-080` | `FACT` |
| otaUrl aus Register-Response triggert Update | `EVID-HUB-2026-10-09-081` | `FACT` |
| Planungsdoc nennt ESP-IDF; Ist = Arduino/PIO | `EVID-HUB-2026-10-09-082` | `FACT` (Doc-Drift) |

## Verwandte

- Sheet: [`esp-hub-telemetry`](../../../technologies/esp-hub-telemetry/SHEET.md)
- Adapter: [`iobroker-esp-hub`](../../iobroker-esp-hub/)
