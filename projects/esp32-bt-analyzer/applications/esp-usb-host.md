# Project Application: esp-usb-host in esp32.bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: esp-usb-host
status: draft
sheet: ../../../technologies/esp-usb-host/SHEET.md
maturity:
  technology: R0
  implementation: R0
  field_evidence: R0
  reusability: W0
```

## Rolle im Projekt

ESP32-S3 enumeriert einen USB-Bluetooth-Dongle und liefert Descriptors/Interfaces/Endpoints als Grundlage für USB-HCI-Capture (Gate BT1+).

## Architektur / Datenfluss

```text
BT Dongle USB  →  ESP32-S3 USB Host  →  descriptor/state  →  (later) HCI endpoints → TCP
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `firmware/analyzer-node/` | Host node (BT1+) |
| `docs/HARDWARE.md` | N8R2 / Hub |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| — | — | noch kein Lab |
