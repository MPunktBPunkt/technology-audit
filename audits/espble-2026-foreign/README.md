# Audit Campaign: espble-2026-foreign

```yaml
id: espble-2026-foreign
project_id: espble
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "56e288d"
reuse_outcomes:
  reused: ['bluetooth-a2dp', 'avrcp']
  new: []
  not_helped: []
  process: "Desk foreign A2DP/AVRCP catalog batch"
```

## Ziel

Unified BLE (NimBLE) + Classic Bluedroid (namespaced) mit explizitem AVRCP CT/TG und A2DP Sink/Source — Dual-Host-Koexistenz experimental.

## Scope

[SCOPE](../../projects/espble/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Applications A2DP/AVRCP (soweit Signal) | erfüllt |
| 3 | Sheets um Kontrast/Community-Gates gewachsen | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |

## Lessons → Transfer

- Eine der wenigen Libraries mit bewusst getrennten AVRCP-CT/TG-APIs.
- Dual-Host BLE+Classic bleibt experimental — Coex-Gate.
- Target-Notification-Limits sind Host-Build-Sache, nicht Spec-Sache.

## Bezug

[INVENTORY](../../projects/espble/INVENTORY.md) · [evidence](evidence.md) · [`esp32-a2dp-2026-foreign`](../esp32-a2dp-2026-foreign/) · [`esp32-bt-gateway-2026-planning`](../esp32-bt-gateway-2026-planning/)
