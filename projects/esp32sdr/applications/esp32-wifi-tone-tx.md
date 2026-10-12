# Project Application: esp32-wifi-tone-tx in esp32sdr

```yaml
project_id: esp32sdr
tech_slug: esp32-wifi-tone-tx
status: active
sheet: ../../../technologies/esp32-wifi-tone-tx/SHEET.md
audit: ../../../audits/esp32sdr-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Arbeitender TX-Pfad: `TXTONE` / `esp_phy_wifi_tx_tone` keyed für OOK/ASK/2-FSK-Messaging board-to-board. DAC-Replay-Pfade bleiben im Repo als Lab-Toteis.

| Repo | Commit | Rolle |
|------|--------|-------|
| [lozaning/ESP32SDR](https://github.com/lozaning/ESP32SDR) | `dbff7bb` | Firmware + GUI link |

## Architektur / Datenfluss

```text
Host gui/link.py
  → serial commands TXTONE / channel retune
  → esp_phy_rftest_* + esp_phy_wifi_tx_tone
  → CW on 5 MHz Wi-Fi grid
  → OOK/FSK bits → peer RX power/energy decide
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `README.md` — The transmit chain | Tone vs DAC falsification |
| `docs/FINDINGS.md` | Register map / DAC dead ends |
| `gui/link.py` / `gui/modulation.py` | Host bit framing |
| `main/Kconfig.projbuild` | Experimental raw-I/Q feeder flag |
| `main/CMakeLists.txt` | `FATAL_ERROR` unless ESP32-S3 |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Tone-TX API + channel grid | `EVID-TONE-2026-10-12-001` | `FACT` |
| OOK/ASK/2-FSK claimed working | `EVID-TONE-2026-10-12-002` | `INFERRED` (author BER) |
| DAC replay does not radiate I/Q on S3 | `EVID-TONE-2026-10-12-003` | `FACT` (Upstream Lab narrative + FINDINGS) |
| BPSK/QPSK impossible without phase path | `EVID-TONE-2026-10-12-004` | `FACT` (as Upstream conclusion) |

## Offene Fragen

- Eigene Spurs/Power bei TXTONE?
- Vergleich SNR zu polar-TX auf anderem Band?
