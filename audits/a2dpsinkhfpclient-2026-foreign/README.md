# Audit Campaign: a2dpsinkhfpclient-2026-foreign

```yaml
id: a2dpsinkhfpclient-2026-foreign
project_id: a2dpsinkhfpclient
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "db7ff2f"
reuse_outcomes:
  reused: ['bluetooth-a2dp', 'avrcp']
  new: []
  not_helped: []
  process: "Desk foreign A2DP/AVRCP catalog batch"
```

## Ziel

Kompakte ESP-IDF-Component: A2DP Sink + HFP HF + explizite AVRC-API (play/pause/next/prev + Metadata-Struct) — Vergleich zu reinem A2DP+AVRCP.

## Scope

[SCOPE](../../projects/a2dpsinkhfpclient/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Applications A2DP/AVRCP (soweit Signal) | erfüllt |
| 3 | Sheets um Kontrast/Community-Gates gewachsen | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |

## Lessons → Transfer

- Guter API-Vergleichspunkt zu pschatzmann (explizite C-Funktionen + Metadata-Struct).
- HFP parallel macht Coex/Audio-Routing komplexer als reines A2DP.

## Bezug

[INVENTORY](../../projects/a2dpsinkhfpclient/INVENTORY.md) · [evidence](evidence.md) · [`esp32-a2dp-2026-foreign`](../esp32-a2dp-2026-foreign/) · [`esp32-bt-gateway-2026-planning`](../esp32-bt-gateway-2026-planning/)
