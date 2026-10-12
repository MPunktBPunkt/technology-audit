# Project Application: avrcp in esp32-a2dp

```yaml
project_id: esp32-a2dp
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/esp32-a2dp-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

AVRCP **zusammen mit A2DP**: Sink-Seite Metadata-Callbacks; Source-Seite Pass-Through-Commands (als CT) und Volume/TG-Pfade in der Bluedroid-API. Standalone AVRCP ohne A2DP = Upstream **nicht** supported.

## Architektur / Datenfluss

```text
Sink-Gerät:  Peer CT ──AVRCP Meta/Cmd──▶ ESP TG/CT hooks ──▶ Sketch callbacks
Source-Gerät: HU CT ──Pass-Through──▶ ESP ──▶ set_avrc_passthru_command_callback
              ESP ──A2DP Audio──▶ HU Sink
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `examples/bt_music_receiver_with_metadata/` | Meta Title/Artist/Album/Playing-Time |
| `examples/bt_music_sender_avrc/` | Pass-Through button handler |
| `src/BluetoothA2DPSink.h` | `set_avrc_metadata_*` |
| `src/BluetoothA2DPSource.h` | `set_avrc_passthru_command_callback`, Volume/TG |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| AVRCP nur gekoppelt mit A2DP (README) | `EVID-AVRCP-LIB-2026-10-12-001` | `FACT` |
| Metadata-Attribute-Mask konfigurierbar | `EVID-AVRCP-LIB-2026-10-12-002` | `FACT` |
| Pass-Through auf Source-Beispiel | `EVID-AVRCP-LIB-2026-10-12-003` | `FACT` |
| Browsing vollständig wie BlueZ-Target | — | `UNKNOWN` / Gate |
| NBT-Evo Tastenmapping | — | `UNKNOWN` (Gateway) |

## Offene Fragen

- Welche Pass-Through-IDs NBT Evo wirklich sendet?
- Browse-Kanal in dieser Library vs. Gateway-Pflichtenheft?
