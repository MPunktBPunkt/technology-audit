# Audit Campaign: pidrive-2026-radio-bt

```yaml
id: pidrive-2026-radio-bt
project_id: pidrive
started: 2026-10-09
ended: null
status: active
profile: ops-field
standard_version: "0.6.3"
reviewed_commit: b61df4d
```

## Ziel

Vertiefung **Empfang/Funk/FFT** und **Bluetooth A2DP/AVRCP** in PiDrive unter **0.6.3** — Wissen aus welle-cli, Scanner/PMR/Airband, Spektrum und BlueZ/PipeWire in Sheets + Applications; Querverweis ESP-BT-Gateway.

## Scope

Siehe [SCOPE](../../projects/pidrive/SCOPE.md) · Inventar-Reuse Radio/BT.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.3 + ops-field | erfüllt |
| 2 | Sheets DAB / RTL-SDR / PMR / Airband / Spectrum-FFT | erfüllt |
| 3 | Applications + A2DP/AVRCP applied (Pi vs ESP kontrastiert) | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 5 | Feldserie Antenne/Ohr vollständig verdichtet | offen |

## Bezug

[INVENTORY](../../projects/pidrive/INVENTORY.md) · [evidence](evidence.md) · Gateway [`esp32-bt-gateway`](../../projects/esp32-bt-gateway/) · [`VERSION`](../../VERSION)
