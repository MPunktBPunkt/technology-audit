# Audit Campaign: esp-sdr-bridge-2026-foreign

```yaml
id: esp-sdr-bridge-2026-foreign
project_id: esp-sdr-bridge
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "7da8aea"
reuse_outcomes:
  reused: [esp32-undoc-iq-rx]
  new: []
  not_helped: []
  process: "Desk foreign; author MEASUREMENTS as INFERRED"
```

## Ziel

IQS Host-Bridge als Application auf `esp32-undoc-iq-rx`; SpyServer/rtl_tcp als G7-Backends.

## Scope

[SCOPE](../../projects/esp-sdr-bridge/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 | erfüllt |
| 2 | Application + Sheet `seen_in` | erfüllt |
| 3 | Epistemic: Soak ≠ KB MEASURED | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |

## Lessons → Transfer

- Continuous IQS ≠ burst capture — gleicher Slug, getrennte Apps.
- rtl_tcp-Kompatibilität verführt zu RTL-Dongle-Annahmen — Hardware bleibt ESP-Undoc.

## Bezug

[INVENTORY](../../projects/esp-sdr-bridge/INVENTORY.md) · [evidence](evidence.md) · [`espargos-espsdr-2026-foreign`](../espargos-espsdr-2026-foreign/)
