# Audit Campaign: pidrive-2026-radio-bt

```yaml
id: pidrive-2026-radio-bt
project_id: pidrive
started: 2026-10-09
ended: null
status: active
profile: ops-field
standard_version: "0.6.6"
revalidated_from: "0.6.3"
revalidated: 2026-10-11
reviewed_commit: b61df4d
reuse_outcomes:
  - new: [dab-plus, rtl-sdr, pmr446, airband-am, sdr-spectrum-fft]
  - grown: [bluetooth-a2dp, avrcp]
  - sharpened: "0.6.6 RX≠TX + stack-scope Pi BlueZ ≠ ESP; tuner family"
  - process: "parity 0.6.3 → 0.6.6; DELTA"
  - not_created: [freenet, lpd, cb, ukw-wbfm]
  - contrast: [pi-fm-tx, esp-fm-tx, welle-io, esp32-bt-gateway]
```

## Ziel

Vertiefung **Empfang/Funk/FFT** und **Bluetooth A2DP/AVRCP** in PiDrive — Wissen aus welle-cli, Scanner/PMR/Airband, Spektrum und BlueZ/PipeWire in Sheets + Applications; Querverweis ESP-BT-Gateway.

**Revalidation 2026-10-11:** Commit `b61df4d` unter **0.6.6** — RX≠TX, Stack-/Tuner-Scope, Gaps. Historie: Git + [DELTA](DELTA.md).

## Scope

Siehe [SCOPE](../../projects/pidrive/SCOPE.md) · Inventar-Reuse Radio/BT. Revalidation = gleicher Commit, keine neue Feldserie.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.3 + ops-field (Original) | erfüllt (2026-10-09) |
| 2 | Sheets DAB / RTL-SDR / PMR / Airband / Spectrum-FFT | erfüllt |
| 3 | Applications + A2DP/AVRCP applied (Pi vs ESP kontrastiert) | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 5 | Feldserie Antenne/Ohr vollständig verdichtet | offen |
| 6 | Revalidation 0.6.6: RX≠TX + Stack-Scope + DELTA | erfüllt (2026-10-11) |

## Lessons (Revalidation)

- Empfangs-Sheets dürfen TX-Verträge nicht absorbieren (G17/Transfer zu `rpi-gpio-fm-tx` / `esp32-apll-fm-tx`).
- A2DP/AVRCP auf Pi ≠ ESP-Gateway — gleicher Slug, getrennte Stack-Evidence.
- Observed Scanner-Raster (Freenet/…) bleiben ohne Sheet (G19).

## Bezug

[INVENTORY](../../projects/pidrive/INVENTORY.md) · [evidence](evidence.md) · **[DELTA](DELTA.md)** · Gateway [`esp32-bt-gateway`](../../projects/esp32-bt-gateway/) · TX [`pi-fm-tx`](../pi-fm-tx-2026-foreign/) · RX-Upstream [`welle-io`](../welle-io-2026-foreign/)
