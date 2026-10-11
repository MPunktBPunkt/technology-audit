# Project Application: esp32-polar-phy-tx in esp32-sdr-trx

```yaml
project_id: esp32-sdr-trx
tech_slug: esp32-polar-phy-tx
status: active
sheet: ../../../technologies/esp32-polar-phy-tx/SHEET.md
audit: ../../../audits/esp32-sdr-trx-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

Release-Transmitter `espdr-tx`: steuert den PHY-Testträger polar (Frequenz + Amplitude) für FM/SSB/RTTY im 13‑cm-Amateurband. **Kein** APLL-GPIO-Pfad, **kein** Sample-I/Q-TX im Release.

| Repo | Commit | Rolle |
|------|--------|-------|
| [jochenhammes/esp32-sdr-trx](https://github.com/jochenhammes/esp32-sdr-trx) | `e1aebbf` | polar TX + Host |
| [h0m3us3r/eSpDR](https://github.com/h0m3us3r/eSpDR) | `f279bf8` | RX-Basis (`NOTICE`) |

## Architektur / Datenfluss

```text
Host (WAV/pipe/sound/text)
  → Mode-Encoder (FM / USB / LSB / RTTY)
  → 4-byte records (freq offset + gain)
  → Firmware ring / update loop
  → PHY test tone (freq + amplitude)
  → RF @ 2.32–2.45 GHz (lab/Amateur)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `firmware/protocol/transmit.h` | TX ops, record layout, LO limits |
| `firmware/src/radio.c` / `radio.h` | Radio bring-up / LO |
| `src/espdr/cli_tx.py` / `txmodes.py` / `txlink.py` | Host `espdr-tx` |
| `docs/transmitter.md` / `docs/internals.md` | Legal, Modes, polar Erklärung |
| `docs/research/TX-RESEARCH.md` | Forschungsprotokoll |
| `NOTICE` | Provenance eSpDR `f279bf8` + Claude-Hinweis |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Chip | ESP32-S3 |
| TX-Band | 2320–2450 MHz |
| Record rate | 8–40 kHz (Default 40 kHz) |
| Modes | FM ±2.5 kHz, USB/LSB, RTTY 170 Hz |
| Thermal | board-spezifisches Modell optional |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Polar TX Protocol + LO limits im Code | `EVID-POLAR-2026-10-11-001` | `FACT` |
| Chip-Scope S3; Herkunft eSpDR | `EVID-POLAR-2026-10-11-002` | `FACT` |
| Release-TX ≠ raw I/Q engine | `EVID-POLAR-2026-10-11-003` | `FACT` |
| Thermal-Drift-Zahlen (Hz) | `EVID-POLAR-2026-10-11-004` | `INFERRED` (author-reported) |
| Absolute TX-Power / Spurs | — | `UNKNOWN` |
| Polar auf Nicht-S3 | — | `UNKNOWN` |

## Abweichungen

- Dokumentation und viel Code mit Claude; Author betont eigene Messungen — KB markiert Performance als nicht revalidiert.
- `research/iq-tx` hält Raw-I/Q/LoRa — nicht mit Release-TX vermischen.

## Offene Fragen

- Fremde Lab-Reproduktion polar SSB/FM?
- Spurious-Budget für Hub-Lab?
