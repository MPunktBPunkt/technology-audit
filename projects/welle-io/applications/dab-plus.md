# Project Application: dab-plus in welle-io

```yaml
project_id: welle-io
tech_slug: dab-plus
status: active
sheet: ../../../technologies/dab-plus/SHEET.md
audit: ../../../audits/welle-io-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R0
  reusability: W3
```

## Rolle

Upstream-Implementierung von DAB/DAB+-Empfang: Backend (OFDM, FIC/MSC, Decoder) + **welle-cli** (ALSA/Web) und **welle-gui** (Qt). PiDrive nutzt typisch nur die CLI-Seite — hier der Quellcode dazu.

## Architektur / Datenfluss

```text
SDR/RAW → OFDM/FIC/MSC → DAB/DAB+ Decode → PCM (ALSA) | HTTP (mp3/flac) | DLS/MOT
                              └─ Web: /mux.json, /spectrum (kanalgebunden)
```

## Pfade

| Pfad (Upstream) | Rolle |
|-----------------|-------|
| `src/backend/` | OFDM, FIB/FIC, MSC, DAB/DAB+-Decoder, PAD/MOT, TII |
| `src/various/channels.cpp` | Band-III- + L-Band-Kanal → Frequenz |
| `src/welle-cli/welle-cli.cpp` | CLI: `-c`/`-p`/`-w`/`-D`/`-C`/`-g`/`-F` |
| `src/welle-cli/webradiointerface.cpp` | `/mux.json`, `/spectrum`, Carousel |
| `src/welle-gui/` | Qt-GUI (nicht vertieft) |
| `CMakeLists.txt` | `BUILD_WELLE_CLI` ohne Qt möglich |
| `README.md` | Hardware, Examples, Limits |

## Konfiguration (CLI, Auswahl)

| Option | Bedeutung | Status |
|--------|-----------|--------|
| `-c channel` | DAB-Kanalname (z. B. `12A`) | `FACT` |
| `-p programme` | Service/Programm | `FACT` |
| `-w port` | Webserver | `FACT` |
| `-C N` | Carousel N Decoder | `FACT` |
| `-g gain` | Gain-**Index** oder `-1` Auto | `FACT` |
| `-O mp3\|flac` | Web-Audio-Codec | `FACT` (README) |

## Ebene C

Desk-Upstream, kein Feld:

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| v2.7 @ `512558d`; GPL-2 | `EVID-WELLE-2026-10-11-001` | `FACT` |
| Kanäle Band III + L-Band; Start `5A` | `EVID-WELLE-2026-10-11-005` | `FACT` |
| `/spectrum` = FFT über `T_u` Samples des laufenden Kanals | `EVID-WELLE-2026-10-11-007` | `FACT` |
| Web: `/mux.json`, Carousel `-C`/`-w` | `EVID-WELLE-2026-10-11-008` | `FACT` |
| Airspy HF+ nicht unterstützt | `EVID-WELLE-2026-10-11-009` | `FACT` |

PiDrive-Feldclaims bleiben in [`pidrive/applications/dab-plus.md`](../../pidrive/applications/dab-plus.md).

## Kontrast PiDrive

| | welle-io (dieses Repo) | PiDrive |
|--|------------------------|---------|
| Rolle | Upstream-Tool | Ops-Facade um `welle-cli` |
| Gain | Index + Software-AGC im Input | Index-Tabelle in Python-Helpers |
| Spektrum | DAB-Web `/spectrum` | extra `sdr-spectrum-fft` für andere Bänder |
| Audio | ALSA / HTTP-Stream | Route vs. BT/PipeWire (Feld) |
