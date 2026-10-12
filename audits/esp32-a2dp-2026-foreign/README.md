# Audit Campaign: esp32-a2dp-2026-foreign

```yaml
id: esp32-a2dp-2026-foreign
project_id: esp32-a2dp
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "a9e946a"
reuse_outcomes:
  reused: [bluetooth-a2dp, avrcp]
  new: []
  not_helped: []
  process: "Desk foreign; Bluedroid ESP Classic reference for gateway"
```

## Ziel

[pschatzmann/ESP32-A2DP](https://github.com/pschatzmann/ESP32-A2DP) als ESP-Bluedroid-Referenz für A2DP/AVRCP in die KB — Chip-Gate Classic vs. S3, Sink/Source-Rollen, Kontrast zu Pi BlueZ.

## Scope

[SCOPE](../../projects/esp32-a2dp/SCOPE.md) — Desk; keine Feld-Paarung.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Applications A2DP + AVRCP | erfüllt |
| 3 | Sheets um ESP-Stack-Zelle gewachsen | erfüllt |
| 4 | S3 Classic-Transfer `REJECTED` im Sheet | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |
| 6 | NBT-Evo Lab | offen (FOLLOW-ON) |

## Lessons → Transfer

- A2DP-Profil-Slug bleibt stack-neutral; Evidence muss Bluedroid vs. BlueZ trennen.
- Library-Compile-Gate bestätigt: S2/S3/C3 ≠ Classic-A2DP-Host.
- Gateway braucht **Source** + AVRCP-Pass-Through — nicht nur Sink-Beispiele.

## Bezug

[INVENTORY](../../projects/esp32-a2dp/INVENTORY.md) · [evidence](evidence.md) · [`esp32-bt-gateway-2026-planning`](../esp32-bt-gateway-2026-planning/) · [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/)
