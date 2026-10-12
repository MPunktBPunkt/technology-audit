# Project Application: esp32-undoc-iq-rx in esp-sdr-bridge

```yaml
project_id: esp-sdr-bridge
tech_slug: esp32-undoc-iq-rx
status: active
sheet: ../../../technologies/esp32-undoc-iq-rx/SHEET.md
audit: ../../../audits/esp-sdr-bridge-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

Host-seitige **IQS1**-Brücke: S3 firmware streamt decimated I/Q über USB Serial/JTAG; Python-Prozess prüft CRC/Continuity, entfernt DC, serviert **SpyServer** (:5555) und **rtl_tcp** (:1234).

| Repo | Commit | Rolle |
|------|--------|-------|
| [z2labs/esp-sdr-bridge](https://github.com/z2labs/esp-sdr-bridge) | `7da8aea` | Bridge |
| ESP-SDR `s3-iq-stream` (zodoczi / ESPARGOS#4) | angrenzend | Firmware IQS |

## Architektur / Datenfluss

```text
RF 2.2–2.8 GHz
  → S3 capture @16 MS/s + 2-stage FIR DDC (core1, PIE)
  → IQS1 frames (USB Serial/JTAG, ~0.65 MB/s)
  → esp-sdr-bridge
  → SpyServer and/or rtl_tcp clients (SDR++/gqrx/…)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/esp_sdr_bridge/bridge.py` | Serial IQS, servers |
| `docs/MEASUREMENTS.md` | Soak / sweep (author) |
| `tools/ss_client.py` | SpyServer test client |
| `README.md` | Rates 250/125/62.5 kS/s |

## Konfiguration (Desk)

| Parameter | Wert (Upstream) |
|-----------|-----------------|
| Tune | 2204–2804 MHz, 1 kHz |
| Default rates | 250 kS/s 8-bit; 125/62.5 16-bit |
| LO offset | fs/4 (4 MHz) IF shift |
| Ports | SpyServer 5555, rtl_tcp 1234 |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| IQS command + IQS1 framing in bridge | `EVID-BRIDGE-2026-10-12-001` | `FACT` |
| USB bandwidth ~0.65 MB/s limits rate | `EVID-BRIDGE-2026-10-12-002` | `FACT` (claim) |
| Soak 87 min 0 CRC / 0 seq gaps | `EVID-BRIDGE-2026-10-12-003` | `INFERRED` (author MEASUREMENTS) |
| PLL spur on 20 MHz LO grid | `EVID-BRIDGE-2026-10-12-004` | `INFERRED` |
| Absolute RF cal | — | `UNKNOWN` ohne Remessung |

## Abweichungen

- rtl_tcp-API ≠ physischer RTL2832U (`rtl-sdr` Sheet) — Backend-Kompatibilität, andere RF-Hardware.
- Burst-Waterfall (ESP32SDR) ≠ gapless IQS FIR stream.
