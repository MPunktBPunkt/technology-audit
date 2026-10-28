# Follow-on ideas (aus ble-gatt-bridge-refs)

```yaml
reuse_outcomes:
  reused: [ble-hr-relay, bluetooth-ftms, ble-http-gatt-probe]
  new: [ble-gatt-dual-role, ble-gatt-transparent-bridge, ble-gatt-semantic-bridge]
  not_helped: ["esp32-ble2mqtt als BLE↔BLE-Vorbild — nur Central↔MQTT"]
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Folgeprojekt: Profil zuerst wählen (HR Fanout vs Semantic vs Transparent) | alle drei neuen Sheets | Sheet-Wahl steuert Interaktionsmodell |
| Exclusive-Control Lab an ergo/MyWhoosh | `bluetooth-ftms`, `ble-gatt-semantic-bridge` | Exit noch offen |
| `ble-cps-gatt` Sheet wenn CPS Produktpfad | iFitnessProxy Evidence | Candidate → Sheet |
| Classic Dual-Role Gate | `ble-gatt-dual-role` | eigene Messung |
| heartrate: CCCD dest≠source dokumentieren | `ble-hr-relay` + transparent | Fallstrick schon A |
