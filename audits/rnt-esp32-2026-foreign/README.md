# Audit Campaign: rnt-esp32-2026-foreign

```yaml
id: rnt-esp32-2026-foreign
project_id: rnt-esp32
started: 2026-10-11
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
source_kind: secondary-web-catalog
reviewed_snapshot: "2026-10-11"
source_url: "https://randomnerdtutorials.com/projects-esp32/"
reuse_outcomes:
  reused_signals: [esp-embedded-web-sse, esp-now-messaging, mqtt-node-telemetry, esp-lab-bus-tools, ssd1306-oled-ui]
  partial: [ble-hrm-gatt, esp-hub-telemetry, bluetooth-a2dp]
  new_sheets: []
  not_created: [esp32-cyd-ui, freertos-esp, lora-radio, firebase-iot]
  process: "catalog match only; no tutorial text; no seen_in without Application"
```

## Ziel

Den RNT-ESP32-Tutorial-**Index** wie einen Fremd-Upstream behandeln: Signale sammeln, gegen `technologies/index.yaml` matchen, Lücken als observed/candidate belassen. Wissensbasis wächst durch **Match-Qualität**, nicht durch gespiegelte Guides.

## Scope

[SCOPE](../../projects/rnt-esp32/SCOPE.md) — Desk Index-Scan; keine Tutorial-Bodies; keine Feldversuche.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | `standard_version` 0.6.6 + Profil `lab-tool` + Snapshot-Datum | erfüllt |
| 2 | Match-Tabelle Index → bestehende Slugs (Reuse vor neu) | erfüllt |
| 3 | Kein neues Sheet; G19 für CYD/FreeRTOS/… | erfüllt |
| 4 | Keine Tutorial-Texte/Code in der KB | erfüllt |
| 5 | Evidence: Snapshot + URL + Katalog-FACTs | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 7 | Gezielte Artikel-Vertiefung (optional) | offen (FOLLOW-ON) |

## Lessons → Transfer

- Website ≠ GitHub: Snapshot-Datum statt Commit-SHA; Inhalt driftet.
- Sekundärquelle: nicht `FACT` für Peripherie ohne TRM/Code (G17).
- „ESP32“ in Arduino-Tutorials ≠ Chip-Familie S3/C3 automatisch.
- `seen_in` erst mit Application — Katalog allein erzeugt keine Implementierungs-Spur.

## Bezug

[INVENTORY](../../projects/rnt-esp32/INVENTORY.md) · [evidence](evidence.md) · Familie ESP-Hub / Lab-Fremd
