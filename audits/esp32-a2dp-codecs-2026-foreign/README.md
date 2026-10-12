# Audit Campaign: esp32-a2dp-codecs-2026-foreign

```yaml
id: esp32-a2dp-codecs-2026-foreign
project_id: esp32-a2dp-codecs
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "cfint@bf8b482 WillyBilly06@f4eb125"
reuse_outcomes:
  reused: [bluetooth-a2dp, avrcp]
  new: []
  not_helped: []
  process: "Desk foreign multi-codec sinks"
```

## Ziel

Codec-Forks als A2DP-Varianten mit klaren Gates (PSRAM, IDF-Fork, BlueZ-Cache).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 | erfüllt |
| 2 | Applications + Sheet-Fallstricke | erfüllt |
| 3 | `ta-assist check` | erfüllt (2026-10-12) |

## Lessons → Transfer

- Multi-Codec ≠ Standard-Gateway-Pfad.
- Peer/OS-Cache kann Codec-Liste „einfrieren“.

## Bezug

[INVENTORY](../../projects/esp32-a2dp-codecs/INVENTORY.md) · [evidence](evidence.md)
