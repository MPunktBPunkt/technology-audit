# Evidence — pi-fm-tx-2026-foreign

Desk 2026-10-10 · **standard_version 0.6.3** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/rm-hull/pifm | `6c30d00` |
| https://github.com/F5OEO/PiFmRds | `2707ecc` |
| https://github.com/markondej/fm_transmitter | `322500e` |
| https://github.com/F5OEO/rpitx | `ee7ff57` |
| https://github.com/zoroxide/Pi-Fm_transmitter | `552f955` |
| https://github.com/cdzombak/pi-fm-player | `f602f42` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-PIFM-2026-10-10-001` | pifm `/dev/mem` + mmap | `FACT` | `pifm.cpp` |
| `EVID-PIFM-2026-10-10-002` | DMA-Exit-Risiko dokumentiert | `FACT` | PiFmRds `pi_fm_rds.c` Header |
| `EVID-PIFM-2026-10-10-003` | GPIO4 Emissionspin (Klassiker) | `FACT` | READMEs pifm/PiFmRds |
| `EVID-PIFM-2026-10-10-004` | PLL statt Divider; Harmonische bleiben | `FACT` | PiFmRds README |
| `EVID-PIFM-2026-10-10-005` | Unlizenzierte Aussendung illegal / keine Antenne | `FACT` | PiFmRds Warning |
| `EVID-RDS-2026-10-10-001` | RDS CRC/Gruppen | `FACT` | PiFmRds `rds.c` |
| `EVID-RDS-2026-10-10-002` | ~228 kHz für 57 kHz RDS | `FACT` | `pi_fm_rds.c` Header |
| `EVID-RDS-2026-10-10-003` | Control-Pipe PS/RT | `FACT` | `control_pipe.c` |
| `EVID-RDS-2026-10-10-004` | Getestete RDS-Empfänger gelistet | `FACT` | PiFmRds README Tests |
| `EVID-MATCH-2026-10-10-001` | Vor Audit kein TX-Sheet; RX ≠ TX | `FACT` | technologies Index |
| `EVID-FMTX-2026-10-10-001` | markondej: bis Pi4, nicht Pi5; `GPIO21=1` | `FACT` | fm_transmitter README |
| `EVID-FMTX-2026-10-10-002` | `-d` DMA-Kanal / 255 = CPU | `FACT` | fm_transmitter README |
| `EVID-FMTX-2026-10-10-003` | zoroxide: gleiche CLI/WAV-Probe + install_rpi*.sh | `FACT` | Pi-Fm_transmitter Tree/README |
| `EVID-FMTX-2026-10-10-004` | pi-fm-player: systemd + ffmpeg S16LE → pifm | `FACT` | `pifm-player.sh` / `.service` |
| `EVID-FMTX-2026-10-10-005` | pi-fm-player vendored Mattos/Weigl `pifm/` | `FACT` | `pifm/pifm.cpp` Header |
| `EVID-RPITX-2026-10-10-001` | 5 kHz–1500 MHz + Legal-Disclaimer | `FACT` | rpitx README |
| `EVID-RPITX-2026-10-10-002` | BPF/Filter-Warnung | `FACT` | README Hardware + `doc/bpf-warning.png` |
| `EVID-RPITX-2026-10-10-003` | install.sh setzt `gpu_freq=250` | `FACT` | `install.sh` |
| `EVID-RPITX-2026-10-10-004` | Pi4 „In beta mode“ | `FACT` | README Matrix |
| `EVID-RPITX-2026-10-10-005` | FM-RDS via `src/pifmrds` / `testfmrds.sh` | `FACT` | Tree + README |
| `EVID-RPITX-2026-10-10-006` | GPIO4 Antennenpin | `FACT` | rpitx README Hardware |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Harmonic-Pegel gemessen | `UNKNOWN` | kein Lab |
| Pi5-Nachfolger-Pfad | `UNKNOWN` | markondej: anderer Chip |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-10 | Bootstrap pifm + PiFmRds; Sheets `rpi-gpio-fm-tx`, `fm-rds` |
| 2026-10-10 | + markondej, rpitx, zoroxide, pi-fm-player; Sheet `rpitx` |
