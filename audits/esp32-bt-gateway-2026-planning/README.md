# Audit Campaign: esp32-bt-gateway-2026-planning

```yaml
id: esp32-bt-gateway-2026-planning
project_id: esp32-bt-gateway
started: 2026-10-09
ended: null
status: active
profile: planning
standard_version: "0.6.0"
standard_gaps: ["0.6.1 Geschwister-Reuse / G9–G11 / Arduino-Layout — Kampagne vor Regelstand"]
reviewed_commit: 7a7e8a4
```

## Ziel

Planungsrepo in die Wissensbasis; Parität/Reuse schärfen (`AUDIT-PROFILES`); A2DP/AVRCP/PDAP Sheets für späteren Firmware-Start; Hub-Sheet um IDF-Contract wachsen.

## Scope

Siehe [SCOPE](../../projects/esp32-bt-gateway/SCOPE.md). Keine erfundenen Lab-Messungen.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE + INVENTORY mit Reuse-Match, Status ≤ documented | erfüllt |
| 2 | Sheets `bluetooth-a2dp`, `avrcp`, `pdap` + Checklisten | erfüllt |
| 3 | Hub-Sheet A-Delta (IDF / otaUrl) | erfüllt |
| 4 | Offene Gates A17 / Phase −1 / Q12 als Exit geführt | erfüllt (offen) |
| 5 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 6 | Host-Stack A17 entschieden **oder** deferred dokumentiert | offen |
| 7 | Phase −1 Messartefakte verlinkt | offen |

## Bezug

[INVENTORY](../../projects/esp32-bt-gateway/INVENTORY.md) · [evidence](evidence.md) · Nachbar [pidrive](../../projects/pidrive/)

## Prozess-Schärfung dieses Laufs

- Profil `planning` eingeführt
- Parität alter Projekte nachgezogen (Checklisten, Reuse-Hinweise)
- Checker G6/G7 aktiv

## Offene Punkte

- A17, Q12, Phase −1 (siehe STATE.md Upstream)
