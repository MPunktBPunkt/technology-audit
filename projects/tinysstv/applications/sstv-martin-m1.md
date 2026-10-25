# Project Application: sstv-martin-m1 in tinysstv

```yaml
project_id: tinysstv
tech_slug: sstv-martin-m1
status: active
sheet: ../../../technologies/sstv-martin-m1/SHEET.md
audit: ../../../audits/tinysstv-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle

ESP32-C3 (Rust/ESP-IDF) als Standalone Martin-M1-Sender: Captive-AP Bild-Upload → Tone-Sequenz → Sigma-Delta GPIO → externes Filter → Radio-AF. Hardware-verified Off-Air Demod laut Upstream.

| Repo | Commit | Rolle |
|------|--------|-------|
| [JO3ALT/TinySSTV](https://github.com/JO3ALT/TinySSTV) | `b9977a6` | Firmware |

## Architektur / Datenfluss

```text
Browser (crop 320×240)
  → HTTP POST on open AP
  → RAM RGB333 | SD 24-bit BMP
  → sstv.rs Martin M1 (~115 s)
  → audio.rs 40 kHz DDS ISR + tone queue
  → sigma-delta 1 MHz on AUDIO_GPIO
  → LPF + DC block → AF OUT → radio
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/sstv.rs` | Martin M1 encoder |
| `src/audio.rs` | GPTimer ISR, DDS, SDM |
| `src/config.rs` | GPIO/AP/SD constants |
| `src/web.rs` / `captive.rs` / `wifi.rs` | Upload + captive |
| `README.md` | Timing proof, filter, PTT gap |

## Konfiguration (Desk)

| Parameter | Upstream | Status |
|-----------|----------|--------|
| Target | ESP32-C3, Rust 1.82+, IDF 5.5.3 | `FACT` |
| Sample rate | 40 kHz DDS; SDM 1 MHz | `FACT` |
| Frame | 320×240 + 8 black lines → 320×256 | `FACT` |
| PTT | reserved, not driven | `FACT` |
| AP | open SSID default `SSTV` | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Martin M1 TX end-to-end; off-air 256/256 syncs, 0.022 ms RMS | `EVID-SSTV-2026-10-25-001` | `FACT` (Upstream MEASURED → Desk) |
| PDM≠audio; LPF required; AF to radio | `EVID-SSTV-2026-10-25-002` | `FACT` |
| PTT unimplemented | `EVID-SSTV-2026-10-25-003` | `FACT` |
| Eigenes Lab Demod | — | `UNKNOWN` |

## Offene Fragen

- XIAO C3 Pin-Defaults vs. andere C3-Boards?
