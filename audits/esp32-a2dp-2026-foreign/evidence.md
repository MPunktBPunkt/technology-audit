# Evidence — esp32-a2dp-2026-foreign

Desk 2026-10-12 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/pschatzmann/ESP32-A2DP | `a9e946a` |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-A2DP-LIB-2026-10-12-001` | `IS_VALID_PLATFORM` nur `CONFIG_IDF_TARGET_ESP32` oder `ESP32S31` | `FACT` | `src/config.h` |
| `EVID-A2DP-LIB-2026-10-12-002` | Getrennte Klassen `BluetoothA2DPSink` / `BluetoothA2DPSource` | `FACT` | `src/*.h`, Examples |
| `EVID-A2DP-LIB-2026-10-12-003` | HFP/HSP und standalone AVRCP nicht supported | `FACT` | README |
| `EVID-AVRCP-LIB-2026-10-12-001` | AVRCP nur zusammen mit A2DP | `FACT` | README |
| `EVID-AVRCP-LIB-2026-10-12-002` | Metadata-Attribute-Mask + Callback (Sink) | `FACT` | `bt_music_receiver_with_metadata` |
| `EVID-AVRCP-LIB-2026-10-12-003` | Pass-Through Callback (Source) | `FACT` | `bt_music_sender_avrc` |
| `EVID-A2DP-LIB-2026-10-12-004` | Legacy I2S nur IDF &lt; 5; AudioTools empfohlen | `FACT` | README + `A2DP_LEGACY_I2S_SUPPORT` |
| `EVID-A2DP-LIB-2026-10-12-005` | Managed multi-codec SEP ab IDF 5.5; AAC runtime oft 6.1+ | `FACT` | `src/config.h`, codec examples |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| ESP32-S31 Classic-A2DP im Feld | `UNKNOWN` | Compile-Flag; Caps nicht lab-belegt |
| NBT-Evo Sink mit dieser Source | `UNKNOWN` | Gateway FOLLOW-ON |
| WiFi+BTDM Coex stabil | `HYPOTHESIS` | Beispiel `bt_music_receiver_and_BLE` |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | Desk-Bootstrap + Sheet-Wachstum A2DP/AVRCP |
