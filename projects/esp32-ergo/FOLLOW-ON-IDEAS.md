# Folgeprojekte (aus esp32.ergo)

```yaml
reuse_outcomes:
  - sheets: [bluetooth-ftms, hammer-varon-xtr]
    note: 0.6.6 Revalidation — S3 product scope; sibling relay deploy
  - process: "parity 0.6.0 → 0.6.6; DELTA in audits/esp32-ergo-2026-pilot/"
```

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Zweites Ergometer nur per Capability-Scan | `bluetooth-ftms` + Method | neues Host-Sheet, nicht Varon verbiegen |
| Bridge MyWhoosh Lab-PASS | `bluetooth-ftms` | Evidence-IDs (Exit 5) |
| Gemeinsame Hub-IO-Doku heartrate+ergo | `esp-hub-telemetry` | Schema-Freeze |
| Classic Dual-Role Ergo | Chip-Scope Gate | nicht Produkt — nur bei Bedarf messen |
| SIM-Passthrough (§11) | Bridge / `bluetooth-ftms` | Code laut STATE fehlt |
| `ftms-erg-control` Sheet | observed Slug | nur bei Transferbedarf + Gate (G19) |
