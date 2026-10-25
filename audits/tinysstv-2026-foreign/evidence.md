# Evidence — tinysstv-2026-foreign

Desk 2026-10-25 · **0.7.1** · `lab-tool`

| Repo | Commit |
|------|--------|
| https://github.com/JO3ALT/TinySSTV | `b9977a62d45dbd459d6bbec6e971383e721ddcf4` |

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-SSTV-2026-10-25-001` | Hardware-verified Martin M1; off-air demod 256/256 syncs, 0.022 ms RMS timing residual | `FACT` | README |
| `EVID-SSTV-2026-10-25-002` | 40 kHz DDS → 1 MHz sigma-delta GPIO; LPF required; AF to radio; ~115 s; VIS/Martin M1 | `FACT` | README, config.rs |
| `EVID-SSTV-2026-10-25-003` | PTT_GPIO reserved; firmware does not drive PTT | `FACT` | README, config.rs |
| `EVID-SSTV-2026-10-25-004` | ESP32-C3; Rust/ESP-IDF; open AP; RGB333 RAM or SD BMP; no on-chip JPEG decoder | `FACT` | README, src/ |
| `EVID-SSTV-2026-10-25-005` | Related Cardputer fork exists (out of this audit depth) | `FACT` | README |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-25 | Desk-Bootstrap SSTV Sheet |
