# Audit Campaign: esp32-pidrive-2026-pilot

```yaml
id: esp32-pidrive-2026-pilot
project_id: esp32-pidrive
started: 2026-10-09
ended: null
status: active
profile: firmware
standard_version: "0.6.3"
reviewed_commit: b00e453
```

## Ziel

Desk-Audit von `esp32.pidrive` unter **0.6.3** — MSC-Gadget-Firmware, neuer PUMP-Sheet, Hub-Client; Ops/Host-C bleiben bei `pidrive`.

## Scope

Siehe [SCOPE](../../projects/esp32-pidrive/SCOPE.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.3 + profile firmware | erfüllt |
| 2 | Reuse `usb-msc` + neu `pump-control-link` + Hub | erfüllt |
| 3 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 4 | Host-C / Feld-AV nicht verdoppelt | erfüllt (Verweis `pidrive`) |
| 5 | Sheets `scsi`/`fat` oder bewusst observed | teilweise (observed) |

## Bezug

[INVENTORY](../../projects/esp32-pidrive/INVENTORY.md) · [evidence](evidence.md) · [`pidrive`](../../projects/pidrive/) · [`VERSION`](../../VERSION)
