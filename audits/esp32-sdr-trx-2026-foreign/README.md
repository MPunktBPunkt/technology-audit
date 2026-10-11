# Audit Campaign: esp32-sdr-trx-2026-foreign

```yaml
id: esp32-sdr-trx-2026-foreign
project_id: esp32-sdr-trx
started: 2026-10-11
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "esp32-sdr-trx@e1aebbf eSpDR@f279bf8"
reuse_outcomes:
  reused: [esp32-undoc-iq-rx, esp32-apll-fm-tx, hw-path-gate]
  new: [esp32-polar-phy-tx]
  not_helped: []
  process: "Desk foreign; author measurements INFERRED; no antenna"
```

## Ziel

Kandidaten **jochenhammes/esp32-sdr-trx** (+ eSpDR-Provenance) als S3 RX+polar-TX-Pfad in die KB: eigener TX-Slug, RX an Chip-Matrix, klarer Kontrast zu Classic APLL.

## Scope

[SCOPE](../../projects/esp32-sdr-trx/SCOPE.md) — Desk; keine Feldaussendung; keine Übernahme ungeprüfter Messwerte als `MEASURED`.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Sheet `esp32-polar-phy-tx` + Application | erfüllt |
| 3 | RX an `esp32-undoc-iq-rx` gematcht | erfüllt |
| 4 | Performance-Claims epistemisch getrennt | erfüllt |
| 5 | Abgrenzung APLL / raw I/Q research | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-11) |
| 7 | Eigene Lab-Remessung | offen (FOLLOW-ON) |

## Lessons → Transfer

- Polar PHY-TX ≠ APLL-Clock-FM — getrennte Slugs (wie Pi vs. ESP).
- AI-assistierter Upstream: Architektur-FACT ok; Hz/dB erst nach Remessung.
- jochenhammes/eSpDR ist Historie — kanonisch esp32-sdr-trx.

## Bezug

[INVENTORY](../../projects/esp32-sdr-trx/INVENTORY.md) · [evidence](evidence.md) · [`espargos-espsdr-2026-foreign`](../espargos-espsdr-2026-foreign/) · [`esp-fm-tx-2026-foreign`](../esp-fm-tx-2026-foreign/)
