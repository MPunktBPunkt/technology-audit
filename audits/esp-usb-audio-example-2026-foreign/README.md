# Audit Campaign: esp-usb-audio-example-2026-foreign

```yaml
id: esp-usb-audio-example-2026-foreign
project_id: esp-usb-audio-example
started: 2026-10-13
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "662f2c0"
reuse_outcomes:
  reused: [esp-usb-audio-uac, esp-i2s-audio]
  new: []
  not_helped: []
  process: "Desk community UAC headset; confirms official UAC sheet"
```

## Ziel

Community-Headset-Beispiel (S3-BOX) als zweite Upstream-Quelle für `esp-usb-audio-uac` und als I2S-Codec-Application — Kontrast zu Espressif Official Component.

## Scope

[SCOPE](../../projects/esp-usb-audio-example/SCOPE.md) — Desk only.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.7.1 + lab-tool | erfüllt |
| 2 | Apps UAC + I2S; kein Sheet-Fork | erfüllt |
| 3 | Evidence `662f2c0` | erfüllt |
| 4 | C11/C12 gesetzt | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-13) |
| 6 | Host-OS Lab | offen (bewusst) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neues UAC-Sheet? | Official schon vorhanden? | parallel esp-iot-solution | Nein — reuse `esp-usb-audio-uac` | KNOWN BEFORE TEST |
| I2S als eigenes Sheet? | Codec-Pfad generalisierbar? | `EVID-USBAUD-EX-2026-10-13-004` | reuse `esp-i2s-audio` | KNOWN BEFORE TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-USBAUD-EX-2026-10-13-002` | Vor Port: Target S2/S3 Device-OTG? Classic = Gate | KNOWN BEFORE TEST |
| `EVID-USBAUD-EX-2026-10-13-003` | Sample-Rate USB ↔ I2S synchron halten | KNOWN BEFORE TEST |
| `EVID-USBAUD-EX-2026-10-13-001` | Board-HAL (BOX vs. generisch) nicht als A-FACT | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** Example bestätigt Device-UAC+I2S-Bridge auf S3-BOX.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Example targetet Classic ESP32 ohne USB Device | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Bestätigung ohne Host-Lab. UNKNOWN Host-Enumeration ≠ automatisches STOP.
```

## Knowledge Feedback

Desk only — C13 n/a.

## Bezug

[INVENTORY](../../projects/esp-usb-audio-example/INVENTORY.md) · [evidence](evidence.md) · Official [`esp-iot-solution-2026-foreign`](../esp-iot-solution-2026-foreign/)
