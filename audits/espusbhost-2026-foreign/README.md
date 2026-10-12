# Audit Campaign: espusbhost-2026-foreign

```yaml
id: espusbhost-2026-foreign
project_id: espusbhost
started: 2026-10-12
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "6386f2a"
reuse_outcomes:
  reused: [usb-msc]
  new: [esp-usb-host]
  not_helped: []
  process: "Desk foreign; device matrix as Upstream FACT not KB MEASURED"
```

## Ziel

EspUsbHost v2 als USB-Host-Sheet; Rollen-Trennung zu Device-MSC.

## Scope

[SCOPE](../../projects/espusbhost/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 | erfüllt |
| 2 | Sheet `esp-usb-host` + Application | erfüllt |
| 3 | Abgrenzung `usb-msc` | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (2026-10-12) |

## Lessons → Transfer

- Host ≠ Device trotz gleichem MSC-Klassenwort.
- VBUS und FS/HS sind die ersten Gates — vor Klassen-Features.

## Bezug

[INVENTORY](../../projects/espusbhost/INVENTORY.md) · [evidence](evidence.md) · [`esp32-pidrive-2026-pilot`](../esp32-pidrive-2026-pilot/)
