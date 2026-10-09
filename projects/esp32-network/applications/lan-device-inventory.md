# Project Application: lan-device-inventory in esp32.network

```yaml
project_id: esp32-network
tech_slug: lan-device-inventory
status: active
sheet: ../../../technologies/lan-device-inventory/SHEET.md
audit: ../../../audits/esp32-network-2026-pilot/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

Multi-Port-TCP-Scan, persistentes Inventar (Label/Notiz/Uptime), SSE-Progress. **Nicht** RF-Monitor.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Multi-Port Subnetz-Scan | `EVID-LAN-2026-10-09-001` | `FACT` |
| Inventar NVS + Hub devices/online | `EVID-LAN-2026-10-09-002` | `FACT` |
