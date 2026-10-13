# Evidence — esp32-audioi2s-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/schreibfaul1/ESP32-audioI2S | `45db753` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-AUDIOI2S-2026-10-13-001` | Nur multi-core (S3/S31/P4); Classic limited; S2/C3 nein | `FACT` | README Warning |
| `EVID-AUDIOI2S-2026-10-13-002` | I2S Out oft 48 kHz unabhängig von Quelle; DAC-Beispiele MAX98357A/PCM5102/… | `FACT` | README |
| `EVID-AUDIOI2S-2026-10-13-003` | v4.0.0; PSRAM + external DAC/I2S-BT laut library.properties | `FACT` | library.properties |
| `EVID-AUDIOI2S-2026-10-13-004` | Codecs wav/mp3/aac/flac/opus/vorbis; 16–48 kHz; 8–32 bit | `FACT` | README |
| `EVID-AUDIOI2S-2026-10-13-005` | Example „I2S Bluetooth Transmitter“ nutzt pschatzmann ESP32-A2DP Source | `FACT` | examples/I2S Bluetooth Transmitter/ |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | Desk I2S-Player Audit 0.7.1 |
