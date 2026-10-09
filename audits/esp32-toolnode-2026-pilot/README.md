# Audit Campaign: esp32-toolnode-2026-pilot

```yaml
id: esp32-toolnode-2026-pilot
project_id: esp32-toolnode
started: 2026-10-09
ended: null
status: active
profile: firmware
standard_version: "0.6.1"
standard_gaps: ["0.6.2 Hub-ohne-fwType / Scan-Schichten / G12–G14"]
reviewed_commit: af4d973
```

## Ziel

Desk-Audit von `esp32.toolnode` unter **Audit-Standard 0.6.1** — Geschwister-Reuse RF (kein Fork), neue Sheets Modular-Host + MQTT, Hub/Web wachsen.

## Scope

Siehe [SCOPE](../../projects/esp32-toolnode/SCOPE.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | YAML `standard_version: "0.6.1"
standard_gaps: ["0.6.2 Hub-ohne-fwType / Scan-Schichten / G12–G14"]` + profile | erfüllt |
| 2 | Reuse-Match: RF → gleicher Slug wie rfmonitor | erfüllt |
| 3 | Sheets `esp-module-host`, `mqtt-node-telemetry` + Apps Hub/Web/RF | erfüllt |
| 4 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 5 | RF-Score-Parität zu rfmonitor belegt | offen |

## Bezug

[INVENTORY](../../projects/esp32-toolnode/INVENTORY.md) · [evidence](evidence.md) · Standard: [`STANDARD-CHANGELOG`](../../docs/STANDARD-CHANGELOG.md) · [`VERSION`](../../VERSION)

## Offene Punkte

- Exit 4/5
- Lab-Bus-Tools Sheet wenn zweites Projekt
