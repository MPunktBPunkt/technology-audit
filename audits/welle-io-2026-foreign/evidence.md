# Evidence — welle-io-2026-foreign

Desk 2026-10-11 · Original **0.6.5** · Revalidation **0.6.6** · Profile `lab-tool`.

| Repo | Commit | Version |
|------|--------|---------|
| https://github.com/AlbrechtL/welle.io | `512558d` | 2.7 (`src/welle-gui/_current_version`) |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-WELLE-2026-10-11-001` | DAB/DAB+ SDR; v2.7; GPL-2 | `FACT` | README, `_current_version`, `COPYING` |
| `EVID-WELLE-2026-10-11-002` | Inputs: RTL_SDR, RTL_TCP, AIRSPY, SOAPYSDR, RAW, LIMESDR, NULL | `FACT` | `src/input/input_factory.cpp` |
| `EVID-WELLE-2026-10-11-003` | `setGain(gain_index)` wählt Eintrag aus `rtlsdr_get_tuner_gains` | `FACT` | `src/input/rtl_sdr.cpp` |
| `EVID-WELLE-2026-10-11-004` | Immer manual gain mode; Software-AGC über Index ±1 | `FACT` | `rtl_sdr.cpp` Open + AGC-Pfad |
| `EVID-WELLE-2026-10-11-005` | Kanalmap Band III (`5A`…) + L-Band (`LA`…); `firstChannel = "5A"` | `FACT` | `src/various/channels.cpp` |
| `EVID-WELLE-2026-10-11-006` | `INPUT_RATE` 2048000; RTL setzt diese Sample-Rate | `FACT` | `dab-constants.h`, `rtl_sdr.cpp` |
| `EVID-WELLE-2026-10-11-007` | `/spectrum` FFT über `T_u` Samples des laufenden Inputs | `FACT` | `webradiointerface.cpp` `send_spectrum` |
| `EVID-WELLE-2026-10-11-008` | Web `/mux.json`, `/spectrum`; Carousel `-C`/`-w` | `FACT` | `webradiointerface.cpp`, README |
| `EVID-WELLE-2026-10-11-009` | Airspy HF+ nicht unterstützt (Bandbreite) | `FACT` | README Supported Hardware |
| `EVID-WELLE-2026-10-11-010` | CLI `-g` Index oder `-1` auto; `-F rtl_tcp,host:port` | `FACT` | `welle-cli.cpp` help/getopt |
| `EVID-WELLE-2026-10-11-011` | Fork-Historie qt-dab (Acknowledgement) | `FACT` | README Acknowledgement |
| `EVID-WELLE-2026-10-11-012` | CMake kann `welle-cli` ohne Qt bauen | `FACT` | README CMake / `BUILD_WELLE_IO=OFF` |
| `EVID-SCOPE-2026-10-11-003` | RTL Gain-Index-Contract gilt nicht still für Soapy/Airspy/Lime | `FACT` | input_factory + rtl_sdr vs. andere Treiber; Revalidation |
| `EVID-MATCH-2026-10-11-002` | RX≠TX zu `rpi-gpio-fm-tx`/`esp32-apll-fm-tx`; kein Input-Sheet aus Factory-Liste | `FACT` | Inventar G19 + Sheet-Abgrenzung; Revalidation |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Empfangsqualität Band III vor Ort | `UNKNOWN` | kein Feld |
| Soapy-Gain-Semantik == RTL-Index | `REJECTED` (Annahme) | getrennte Treiber; nicht vertieft gemessen |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-11 | Bootstrap + Kampagne; Apps `dab-plus`/`rtl-sdr`; Sheets gewachsen |
| 2026-10-11 | Revalidation **0.6.6**: Input-Scope, RX≠TX, [DELTA](DELTA.md) |
