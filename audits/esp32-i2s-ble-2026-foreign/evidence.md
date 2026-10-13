# Evidence — esp32-i2s-ble-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/iancarscadden/esp32-i2s-BLE | `4d053c4` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-I2SBLE-2026-10-13-001` | Custom GATT: Service/Control/Audio Notify UUIDs; START/STOP; seq+count+PCM16 | `FACT` | `src/main.cpp`, README Protocol |
| `EVID-I2SBLE-2026-10-13-002` | Capture 16 kHz I2S; Wire/Output **8 kHz** (2:1 downsample) | `FACT` | `src/main.cpp` defines; commit message |
| `EVID-I2SBLE-2026-10-13-003` | Ringbuffer + 120 samples/notify/~15 ms gegen iPhone Drops (Upstream-Begründung) | `FACT` | README „Why Ring Buffer“ |
| `EVID-I2SBLE-2026-10-13-004` | Feather S3 Pins 5/6/9; SPH0645 SEL→3V3 RIGHT | `FACT` | README Wiring |
| `EVID-I2SBLE-2026-10-13-005` | I2S STD driver; DMA 8×512; NimBLE MTU 247 | `FACT` | `src/main.cpp`, platformio.ini |
| `EVID-I2SBLE-2026-10-13-006` | README nennt teils 16 kHz BLE-Stream — weicht vom Code ab | `FACT` | README vs. Code (Dokumentationsdrift) |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | Desk BLE-PCM Pattern Audit 0.7.1; Wire-Rate aus Code |
