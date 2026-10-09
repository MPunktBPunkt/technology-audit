# Project Application: esp-hub-telemetry in esp32.MeterMaster

```yaml
project_id: esp32-metermaster
tech_slug: esp-hub-telemetry
status: active
sheet: ../../../technologies/esp-hub-telemetry/SHEET.md
audit: ../../../audits/esp32-metermaster-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R1
  reusability: W3
```

## Rolle im Projekt

**Zusätzlicher** Heartbeat an ESP-Hub Port **8093** (Dashboard). Fachfunktionen (Config, cmd, Zähler) laufen über MeterMaster-Adapter **8089** — Dual-Backend.

## Architektur

```text
registerNode()     → :8089 /api/register   (Adapter)
sendEspHubHeartbeat() → :8093 /api/register (Hub, optional hubPort>0)
```

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Drei Ports 8087/8089/8093 | `EVID-HUB-2026-10-09-020` | `FACT` |
| Hub-Heartbeat separat von Adapter | `EVID-HUB-2026-10-09-021` | `FACT` |

## Abweichungen

- Kein `esp-hub-base`-Stack; dünner HTTP-Client im `.ino`
- Produkt-Register ≠ Hub-Register (Sheet-Fallstrick)
