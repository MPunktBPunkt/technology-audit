# Project Application: esp-hub-telemetry in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R4
  implementation: R1
  field_evidence: R0
  reusability: W4
```

## Rolle im Projekt

Analyzer-Nodes nutzen **esp-hub Stufe A** Web/OTA/Register (Port 80, Hub `:8093`) — Convenience für Flash/Identify, **keine** harte Abhängigkeit für USB-Messclaims.

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `docs/HUB-BASELINE.md` | Reuse notes |
| `tools/flash_lab_ota.sh` | OTA flash |
| Node `/api/status`, `/events`, `/ota-upload` | Hub-kompatible Oberfläche |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Hub register | `192.168.178.113:8093` (lab note) | `FACT` (B lab) |
| Web UI tabs | Analyzer / Status / OTA | `FACT` (B) |

## Ebene C — Host- / Feld-Evidenz

Keine Feld-Hub-Kampagne. Hub = Ops-Pfad für Lab-Boards.

## Verwandte Applications / Methods

- Andere Hub-Client Applications in ESP-Hub-Familie
