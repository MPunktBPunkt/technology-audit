# Folgeprojekte (aus esp32.heartrate)

```yaml
reuse_outcomes:
  - sheets: [ble-hrm-gatt, ble-hr-relay, esp-embedded-web-sse, esp-hub-telemetry]
    note: 0.6.6 Revalidation — Chip-Scope Relay S3≠Classic; Geschwister bestätigt
  - process: "parity 0.6.0 → 0.6.6; DELTA in audits/esp32-heartrate-2026-pilot/"
```

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Lab-PASS Relay-Abnahme 1–15 | `ble-hr-relay` (S3) | Evidence-IDs / Protokoll |
| Classic dual-role Gate | `ble-hr-relay`, Chip-Scope | Eigene Messung — kein Claim von S3 |
| HRV-Analyse-Node (LF/HF, Poincaré) | `rr-quality-pipeline`, Session-Export | Analyse-Algo + UI; Sheet erst bei Transferbedarf |
| Multi-Sensor-Hub-Node | `esp-hub-telemetry` | andere GATT-Profile |
| PiDrive-adjacent BLE tooling | NimBLE-Erfahrung aus `ble-hrm-gatt` | AVRCP ≠ HRM |
| Geschwister-Transfer | `esp32-ergo`, `esp32-ftmsprobe` | bereits Slug-Wachstum; weitere Kampagnen gezielt |
