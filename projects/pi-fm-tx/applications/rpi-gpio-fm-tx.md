# Project Application: rpi-gpio-fm-tx in pi-fm-tx

```yaml
project_id: pi-fm-tx
tech_slug: rpi-gpio-fm-tx
status: active
sheet: ../../../technologies/rpi-gpio-fm-tx/SHEET.md
audit: ../../../audits/pi-fm-tx-2026-foreign/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R0
  reusability: W3
```

## Rolle

UKW-FM über Pi-GPIO/Clock — **eine** Tech, mehrere Repos (Linie + Ableger + Ops-Wrapper). Multi-Mode → Application `rpitx`.

| Repo | Commit | Rolle |
|------|--------|-------|
| [rm-hull/pifm](https://github.com/rm-hull/pifm) | `6c30d00` | Klassiker Mattos/Weigl+DMA; unmaintained Mirror |
| [F5OEO/PiFmRds](https://github.com/F5OEO/PiFmRds) | `2707ecc` | PLL/RDS-Linie (siehe auch `fm-rds`) |
| [markondej/fm_transmitter](https://github.com/markondej/fm_transmitter) | `322500e` | aktiv gepflegt; Mailbox/DMA; Pi4 GPIO21; **kein Pi5** |
| [zoroxide/Pi-Fm_transmitter](https://github.com/zoroxide/Pi-Fm_transmitter) | `552f955` | markondej-nahe Ableitung + Install-Scripts Pi1–3/4 |
| [cdzombak/pi-fm-player](https://github.com/cdzombak/pi-fm-player) | `f602f42` | systemd + ffmpeg-Cache + **vendortes** klassisches `pifm/` |

GPIO klassisch **4**; markondej Pi4-Workaround: `make GPIO21=1` + Governor/feste ARM-Freq / Frequenzen &lt;93 MHz.

## Pfade (Auswahl)

| Repo / Pfad | Rolle |
|-------------|-------|
| `pifm/pifm.cpp` | DMA + `/dev/mem` |
| `fm_transmitter/transmitter.cpp` | Clock-TX, `#ifndef GPIO21` |
| `fm_transmitter/mailbox.*` | Contiguous DMA mem |
| `Pi-Fm_transmitter/install_rpi*.sh` | Build-Wrapper-Ableger |
| `pi-fm-player/pifm/` | vendortes Mattos/Weigl inkl. Binary |
| `pi-fm-player/pifm-player.sh` | Shuffle MP3 → ffmpeg S16LE → pifm stdin |
| `pi-fm-player/pifm-player.service` | systemd root, `Restart=always` |

## Kontrast

| | Empfang (PiDrive) | Diese Apps |
|--|-------------------|------------|
| Richtung | RX SDR | TX SoC-Clock |
| Meta | DLS / AVRCP | optional RDS (andere App) |
| Ops | PipeWire/BlueZ | systemd-Loop um pifm |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Klassiker `/dev/mem`+DMA (pifm) | `EVID-PIFM-2026-10-10-001` | `FACT` |
| GPIO4 Default; Legal warnings | `EVID-PIFM-2026-10-10-003` / `-005` | `FACT` |
| markondej: bis Pi4, nicht Pi5; GPIO21-Option | `EVID-FMTX-2026-10-10-001` | `FACT` |
| markondej: DMA-Kanal wählbar / CPU-Fallback | `EVID-FMTX-2026-10-10-002` | `FACT` |
| zoroxide ≈ markondej-Struktur + Install-Scripts | `EVID-FMTX-2026-10-10-003` | `FACT` |
| pi-fm-player: systemd + ffmpeg→pifm stdin | `EVID-FMTX-2026-10-10-004` | `FACT` |
| pi-fm-player vendored classic pifm | `EVID-FMTX-2026-10-10-005` | `FACT` |
