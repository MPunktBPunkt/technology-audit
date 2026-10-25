# Project Application: lms-squeezelite in squeezelite-esp32

```yaml
project_id: squeezelite-esp32
tech_slug: lms-squeezelite
status: active
sheet: ../../../technologies/lms-squeezelite/SHEET.md
audit: ../../../audits/squeezelite-esp32-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle

Primärer LMS/Squeezelite-Player auf ESP32/S3; Multi-Room-Sync; Web-UI/NVS-Konfig; AirPlay/BT/Spotify als Add-ons.

| Repo | Commit | Rolle |
|------|--------|-------|
| [sle118/squeezelite-esp32](https://github.com/sle118/squeezelite-esp32) | `ee1720c` (`master-v4.3`) | Firmware suite |

## Architektur / Datenfluss

```text
LMS (LAN)
  → squeezelite core + codecs
  → optional resample/EQ (16-bit mode)
  → I2S DAC | SPDIF | BT speaker
[+ AirPlay / BT sink / Spotify Connect stitched on]
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `components/squeezelite/` | Player core |
| `components/codecs/` | Decoders |
| `components/raop/` | AirPlay |
| `components/spotify/` | Spotify Connect (cspot) |
| `components/driver_bt/` | Bluetooth |
| `README.md` | Performances, Hardware gates |

## Konfiguration (Desk)

| Parameter | Upstream | Status |
|-----------|----------|--------|
| Min HW | 4 MB Flash + 4 MB PSRAM; WROOM rejected | `FACT` |
| CPU | 240 MHz recommended | `FACT` |
| Core | default 16-bit internal; 32-bit compile option | `FACT` |
| Max rate guidance | limit report ~96 kHz advised | `FACT` |
| Version file | `local.500.cmake-master` | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| LMS-first design; Add-ons have shortcomings | `EVID-SQZ-2026-10-25-001` | `FACT` |
| PSRAM required; performance table 16/32-bit | `EVID-SQZ-2026-10-25-002` | `FACT` |
| Multi-room sync capability claimed | `EVID-SQZ-2026-10-25-003` | `FACT` |
| Eigenes Sync-Lab | — | `UNKNOWN` |

## Offene Fragen

- Welches Named-Build (SqueezeAMP/Muse/I2S) für eigenes Lab?
