# Project Application: esp32-undoc-iq-rx in c5vrx

```yaml
project_id: c5vrx
tech_slug: esp32-undoc-iq-rx
status: active
sheet: ../../../technologies/esp32-undoc-iq-rx/SHEET.md
audit: ../../../audits/c5vrx-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

**C5 continuous Analog-FPV-Pfad:** MODEM_DIAG I/Q (~40 MS/s Q4/I4-Klasse laut Docs) → PARLIO/GDMA → BitScrambler FM-Demod → 6‑bit Widerstands-DAC **CVBS**. Zeigt Matrix-Zelle „C5 continuous“, nicht den ESPARGOS-Burst/Host-SDR-Pfad.

| Repo | Commit | Rolle |
|------|--------|-------|
| [Twotoz/C5VRX](https://github.com/Twotoz/C5VRX) | `6887fb3` | main + `v5/` |

## Architektur / Datenfluss

```text
5.8 GHz analog FM (VTX)
  → ESP32-C5 MODEM_DIAG I/Q
  → PARLIO RX / GDMA
  → BitScrambler WBFM (phase path)
  → PARLIO TX → R-DAC → CVBS NTSC
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `main/` / `v5/` | Live- bzw. C5VRX-5 Firmware |
| `docs/native-agc-v2.md` | Native AGC vs. continuous carrier |
| `docs/direct-gain-v3-core.md` u. a. | Gain-Control Research |
| `*.bsasm` (BitScrambler) | On-device Demod |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Target ESP32-C5; 5.8 GHz FPV → CVBS | `EVID-C5VRX-2026-10-11-001` | `FACT` |
| Undocumented MODEM_DIAG I/Q path in architecture | `EVID-C5VRX-2026-10-11-002` | `FACT` |
| Native packet AGC poorly fits continuous FM video | `EVID-C5VRX-2026-10-11-003` | `INFERRED` (author measurements in docs) |
| Range/quality at all distances | — | `UNKNOWN` |

## Verwandte Applications

- [`espargos-espsdr`](../../espargos-espsdr/applications/esp32-undoc-iq-rx.md) — C5 in Multi-Chip-Tabelle (Burst/Host)
