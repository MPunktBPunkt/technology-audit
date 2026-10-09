# Audit Campaign: esp32-heartrate-2026-pilot

```yaml
id: esp32-heartrate-2026-pilot
project_id: esp32-heartrate
started: 2026-10-08
ended: null
status: active
reviewed_commit: 72acae4
profile: firmware
```

## Ziel

Desk-Inventar und priorisierte Sheets/Applications für die Kerntechnologien von `esp32.heartrate` (HR-Central, HR-Relay, Embedded-Web/SSE, Hub-Telemetrie). Wissen liegt in diesem Repo; das Ursprungsrepo ist nur Evidence-Quelle.

## Scope

- Im Scope: siehe [SCOPE.md](../../projects/esp32-heartrate/SCOPE.md)
- Nicht im Scope: Hub-Internals, medizinische Claims, volle HRV-Analyse

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE + INVENTORY mit Status/Coverage und Taxonomie A–J | erfüllt |
| 2 | ≥4 Technology Sheets (Ebene A) für Pilot-Slugs | erfüllt |
| 3 | Applications (B/C) + Evidence-Register für Pilot-Slugs | erfüllt |
| 4 | `python3 tools/ta-assist check` grün | erfüllt (lokal / structure-check) |
| 5 | Mind. ein dokumentierter Lab-PASS zu Relay-Abnahme 1–15 | offen |
| 6 | Feldnotiz Polar H9 + optional Radcomputer verlinkt | offen |

Kampagne bleibt `active`, bis 5–6 geschlossen oder bewusst verworfen sind.

## Bezug Inventar

Priorität: `ble-hrm-gatt` → `ble-hr-relay` → `esp-embedded-web-sse` → `esp-hub-telemetry`  
Details: [INVENTORY.md](../../projects/esp32-heartrate/INVENTORY.md) · Evidence: [evidence.md](evidence.md)

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Sheets | [technologies/](../../technologies/) (Pilot-Slugs) |
| Applications | [applications/](../../projects/esp32-heartrate/applications/) |
| Follow-on | [FOLLOW-ON-IDEAS.md](../../projects/esp32-heartrate/FOLLOW-ON-IDEAS.md) |

## Lokal prüfen

```bash
# in technology-audit
python3 tools/ta-assist check
python3 tools/ta-assist prepare bootstrap https://github.com/MPunktBPunkt/esp32.heartrate
```

Quelle bleibt read-only: [esp32.heartrate](https://github.com/MPunktBPunkt/esp32.heartrate).

## Offene Punkte nach diesem Stand

- Lab-Protokoll Relay-Abnahme mit Evidence-IDs
- Continuity-KPIs vs. PFLICHTENHEFT
- Optional: Sheets für `rr-quality-pipeline` / `littlefs-session-archive`
