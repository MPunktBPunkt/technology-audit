# Project Application: rtl-sdr in welle-io

```yaml
project_id: welle-io
tech_slug: rtl-sdr
status: active
sheet: ../../../technologies/rtl-sdr/SHEET.md
audit: ../../../audits/welle-io-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R0
  reusability: W3
```

## Rolle

RTL2832U als eine von mehreren Sample-Quellen hinter `CInputFactory`. welle setzt **immer** manuellen Tuner-Gain-Mode und steuert Gain über **Indizes** der von `rtlsdr_get_tuner_gains` gelieferten Tabelle; AGC ist Software (Amplituden-Fenster).

## Datenfluss

```text
USB RTL-SDR → librtlsdr @ INPUT_RATE 2.048 MHz → Backend
     oder rtl_tcp (Host:Port) → CRTL_TCP_Client
```

## Pfade

| Pfad | Rolle |
|------|-------|
| `src/input/input_factory.cpp` | auto/manual Device-Wahl; Fallback Null-Device |
| `src/input/rtl_sdr.cpp` | Open, Sample-Rate, Gain-Index, Software-AGC |
| `src/input/rtl_tcp.cpp` | Remote IQ |
| `src/backend/dab-constants.h` | `INPUT_RATE 2048000` |
| `CMakeLists.txt` | `-DRTLSDR=1` |

## Parameter

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `setGain(int gain_index)` auf Tuner-Gain-Tabelle | `EVID-WELLE-2026-10-11-003` | `FACT` |
| Immer `rtlsdr_set_tuner_gain_mode(device, 1)`; AGC in Software | `EVID-WELLE-2026-10-11-004` | `FACT` |
| Sample-Rate = `INPUT_RATE` 2048000 | `EVID-WELLE-2026-10-11-006` | `FACT` |
| CLI `-g` Index / `-1` auto; `-F rtl_tcp,host:port` | `EVID-WELLE-2026-10-11-010` | `FACT` |
| Factory: RTL_SDR, RTL_TCP, AIRSPY, SOAPYSDR, RAW, … | `EVID-WELLE-2026-10-11-002` | `FACT` |

## Kontrast

Andere Inputs (Airspy, Soapy) teilen die Virtual-Input-API, haben aber **eigene** Gain-Semantik — nicht mit RTL-Index verwechseln. Stick-Exklusivität / DVB-Blacklist bleibt Host-Ops (PiDrive), nicht in diesem Upstream gelöst.
