# Audit Campaign: esp-idf-classic-bt-2026-foreign

```yaml
id: esp-idf-classic-bt-2026-foreign
project_id: esp-idf-classic-bt
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "86f72d0"
reuse_outcomes:
  reused: ['bluetooth-a2dp', 'avrcp']
  new: []
  not_helped: []
  process: "Desk foreign A2DP/AVRCP catalog batch"
```

## Ziel

Vendor-SoT für Bluedroid Classic: a2dp_sink_stream*, avrcp_ct_metadata, avrcp_ct_cover_art (1.6), avrcp_absolute_volume — Targets ESP32 (+ S31 Flag).

## Scope

[SCOPE](../../projects/esp-idf-classic-bt/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Applications A2DP/AVRCP (soweit Signal) | erfüllt |
| 3 | Sheets um Kontrast/Community-Gates gewachsen | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |

## Lessons → Transfer

- Cover Art (1.6) und Abs Volume sind Vendor-belegte Stufen — Libraries darunter oft dünner.
- `a2dp_sink` wurde zu `a2dp_sink_stream*` umbenannt — Docs nicht an alten Pfad koppeln.
- Community: Abs Volume nur wenn Peer es anbietet.

## Bezug

[INVENTORY](../../projects/esp-idf-classic-bt/INVENTORY.md) · [evidence](evidence.md) · [`esp32-a2dp-2026-foreign`](../esp32-a2dp-2026-foreign/) · [`esp32-bt-gateway-2026-planning`](../esp32-bt-gateway-2026-planning/)
