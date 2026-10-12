# Audit Campaign: esp32sdr-2026-foreign

```yaml
id: esp32sdr-2026-foreign
project_id: esp32sdr
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "dbff7bb"
reuse_outcomes:
  reused: [esp32-undoc-iq-rx, hw-path-gate, esp32-polar-phy-tx]
  new: [esp32-wifi-tone-tx]
  not_helped: []
  process: "Desk foreign; no antenna; author BER INFERRED"
```

## Ziel

[lozaning/ESP32SDR](https://github.com/lozaning/ESP32SDR): S3 burst RX + Wi-Fi tone TX; Raw-I/Q-DAC als S3-Falsifikation; Kontrast polar/APLL.

## Scope

[SCOPE](../../projects/esp32sdr/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Sheet `esp32-wifi-tone-tx` + Apps | erfüllt |
| 3 | RX an `esp32-undoc-iq-rx` | erfüllt |
| 4 | DAC-TX `REJECTED` dokumentiert | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |

## Lessons → Transfer

- S3 hat **mindestens zwei** TX-Contracts (polar vs. Wi-Fi-tone) plus einen totgelaufenen DAC-Pfad.
- Burst-RX-Registerwissen vertieft die Undoc-Matrix, ersetzt aber nicht IQS-Bridge-Messungen.

## Bezug

[INVENTORY](../../projects/esp32sdr/INVENTORY.md) · [evidence](evidence.md) · [`esp32-sdr-trx-2026-foreign`](../esp32-sdr-trx-2026-foreign/) · [`espargos-espsdr-2026-foreign`](../espargos-espsdr-2026-foreign/)
