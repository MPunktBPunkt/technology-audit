# Project Application: iobroker-esp-hub-adapter in iobroker-esp-hub

```yaml
project_id: iobroker-esp-hub
tech_slug: iobroker-esp-hub-adapter
status: active
sheet: ../../../technologies/iobroker-esp-hub-adapter/SHEET.md
audit: ../../../audits/iobroker-esp-hub-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

**Node.js**-Implementierung der Zentrale: Dashboard :8093, State-Baum, Firmware-Depot, OTA-Push, esptool/arduino-cli, WebRTC-Signaling.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `main.js` | Adapter-Kern |
| `Schnittstellen.md` | API-Spec |
| `admin/` | UI |
| `firmware/` | gebündelte Bins |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Port 8093 Register+Firmware+OTA | `EVID-ADP-2026-10-09-001` | `FACT` |
| otaUrl nach Versand geleert | `EVID-ADP-2026-10-09-002` | `FACT` |
| WebRTC POST/GET /api/webrtc | `EVID-ADP-2026-10-09-003` | `FACT` |
| USB/LXC Hinweise | `EVID-ADP-2026-10-09-004` | `FACT` |
