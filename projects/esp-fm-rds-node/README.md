# Project: ESP FM/RDS Node (Fremdrepos)

Desk-Audit von ESP-basierten FM-Stereo-/RDS-Pfaden. Der zentrale Architekturpfad ist
**ESP32-S3 → I2S-MPX → externer FM-Modulator**; ein I2S-DAC-Ausgang ist noch kein
RF-Sender.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Quellen, Grenzen und Chip-Scope |
| [INVENTORY.md](INVENTORY.md) | Reuse-Matches und Contract-Entscheidungen |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | präregistrierte Desk-/Lab-Gates |
| [applications/fm-rds.md](applications/fm-rds.md) | RDS/MPX in den Fremdrepos |
| [applications/esp-i2s-audio.md](applications/esp-i2s-audio.md) | I2S-Audiopfade nach Chipfamilie |
| Audit | [`esp-fm-rds-node-2026-foreign`](../../audits/esp-fm-rds-node-2026-foreign/) |

## Architekturentscheidung

```text
ESP32-S3: ADC/PCM → I2S-DSP → Stereo/RDS-MPX → I2S-DAC
                                                ↓
                                  externer FM-Modulator erforderlich

Classic ESP32 / ESP32-C3: Audio/Steuerung → QN8027 oder Si4713 → FM/RDS
```

- **ESP32-S3:** PiratESP32 und ESP32-S3-STEREO-DSP belegen einen digitalen
  Audio-/MPX-Pfad, nicht die RF-Modulation.
- **Classic ESP32:** PixelRadio und `esp32_fmdevkit` steuern QN8027; `fm-streamer`
  steuert Si4713/Si47xx und führt Audio über I2S beziehungsweise Analog zum Sender.
- **ESP32-C3:** `ESP32C3_FM_TRANSMITTER` steuert QN8027 über I2C; seine
  Audioeingabe bleibt ein externer Analogpfad. Das ist kein Beleg für Classic-APLL-
  oder S3-MPX-RF.

## Reuse

Die vorhandenen Sheets [`fm-rds`](../../technologies/fm-rds/SHEET.md) und
[`esp-i2s-audio`](../../technologies/esp-i2s-audio/SHEET.md) werden über lokale
Applications wiederverwendet. Es wurden keine Technology Sheets, Methoden oder
Shared Indexe geändert. Ein generischer MPX-Generator- oder integrierter
FM/RDS-Synthesizer-Contract bleibt bis zu den Gates in
[FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) nur ein begründeter Kandidat.

**Gewissheit:** Desk-FACTs stammen aus Code/Dokumentation der fixierten Commits.
Lab- und Field-Verhalten sind `UNKNOWN`; diese Kampagne enthält keine Messung.
