# Evidence — esp32sdr-2026-foreign

Desk 2026-10-12 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/lozaning/ESP32SDR | `dbff7bb` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-TONE-2026-10-12-001` | `esp_phy_wifi_tx_tone` / rftest keyed TX; 5 MHz grid | `FACT` | README transmit chain |
| `EVID-TONE-2026-10-12-002` | OOK/ASK/2-FSK 0 % BER board-to-board | `INFERRED` | README author Lab |
| `EVID-TONE-2026-10-12-003` | DAC replay completes but no commanded RF on S3 | `FACT` | README + `docs/FINDINGS.md` |
| `EVID-TONE-2026-10-12-004` | BPSK/QPSK need phase → DAC path | `FACT` | README conclusion |
| `EVID-ESPSDR-RX-2026-10-12-001` | Capture regs `0x60033d5c`, SRAM `0x3fcd0000` | `FACT` | README |
| `EVID-ESPSDR-RX-2026-10-12-002` | 10-bit I/Q packing / CAP16 | `FACT` | README |
| `EVID-ESPSDR-RX-2026-10-12-003` | Mirrored spectrum / −3 MHz spur | `INFERRED` | README quirks |
| `EVID-ESPSDR-S3-ONLY-2026-10-12` | CMake FATAL unless ESP32-S3 | `FACT` | `main/CMakeLists.txt` |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Absolute TX power | `UNKNOWN` | ~49 dB @ RX author-relative |
| Tone-TX auf C5 | `UNKNOWN` | Gate |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | Desk; neuer Slug `esp32-wifi-tone-tx` |
