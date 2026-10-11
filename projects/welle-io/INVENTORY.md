# Project Inventory: welle.io (Fremd)

```yaml
project_id: welle-io
updated: 2026-10-11
reviewed_commit: "512558d"
profile: lab-tool
pilot_order: [dab-plus, rtl-sdr]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md); Revalidation von 0.6.5):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| DAB/DAB+ Empfänger, Ensemble/Service, DLS, AAC/MP2 | `dab-plus` | Sheet wachsen + App |
| welle-cli `-c`/`-p`/`-w`/`-D`/`-C` Web | `dab-plus` | App-Pfade |
| `/spectrum`, `/mux.json` kanalgebunden | `dab-plus` (+ Abgrenzung `sdr-spectrum-fft`) | Fallstrick A |
| RTL2832U, librtlsdr, Gain-Index, Software-AGC | `rtl-sdr` | Tuner-Scope + App |
| rtl_tcp Host:Port (`-F`) | `rtl-sdr` | App |
| Airspy / SoapySDR / LimeSDR / RAW | — | observed, **kein Sheet** (G19) |
| Qt6 GUI / Flatpak / Docker-RPi | — | observed |
| Pi/ESP GPIO-Clock FM-TX | `rpi-gpio-fm-tx` / `esp32-apll-fm-tx` | **RX≠TX** |
| Allzweck-FFT über MHz | `sdr-spectrum-fft` | **Abgrenzung** |

Kampagne: [`welle-io-2026-foreign`](../../audits/welle-io-2026-foreign/) · [DELTA](../../audits/welle-io-2026-foreign/DELTA.md).  
Nachbar Ops: [`pidrive`](../pidrive/) · TX: [`pi-fm-tx`](../pi-fm-tx/) · [`esp-fm-tx`](../esp-fm-tx/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `dab-plus` | DAB+ Digital Audio Broadcasting | A | `sdr`, `streaming` | applied | partial | [SHEET](../../technologies/dab-plus/SHEET.md) | [app](applications/dab-plus.md) |
| `rtl-sdr` | RTL-SDR Host Stack | A | `sdr`, `usb-host` | applied | partial | [SHEET](../../technologies/rtl-sdr/SHEET.md) | [app](applications/rtl-sdr.md) |
| `sdr-spectrum-fft` | SDR Spectrum / FFT | H | `sdr`, `lab-only` | observed | none | [SHEET](../../technologies/sdr-spectrum-fft/SHEET.md) | — (nur Abgrenzung) |
| `airspy-sdr` | Airspy Input | A | `sdr` | observed | none | — | — |
| `soapysdr` | SoapySDR Input | A | `sdr` | observed | none | — | — |
| `alsa-audio-out` | ALSA Playback (cli) | B | `streaming` | observed | none | — | — |
| `qt6-gui` | Qt 6 Desktop GUI | G | `linux-userspace` | observed | none | — | — |
| `flatpak` | Flatpak Packaging | F | `linux-userspace` | observed | none | — | — |

## Nach Kategorie

### A — Empfang

`dab-plus`, `rtl-sdr` (+ observed Airspy/Soapy)

### B — Audio

`alsa-audio-out` (observed)

### F — Systemintegration

`flatpak` (observed)

### G — Steuerung / UI

`qt6-gui` (observed)

### H — Test / Analyse

`sdr-spectrum-fft` nur als Abgrenzung zu welle `/spectrum`

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Feldempfang / SNR | Desk only | bei Bedarf PiDrive-Kampagne |
| Soapy/Airspy Quirks | nicht priorisiert | observed belassen; Gain ≠ RTL-Index |
| Android/macOS Builds | Upstream unmaintained | ignorieren |

## Signale ohne Eintrag

- Munin-Plugin `welle-cli-munin.py` (mux.json → Graphen)
- MOT Slideshow / X-PAD dump (`--dump-file`)
- Fork-Historie qt-dab (Acknowledgement)
