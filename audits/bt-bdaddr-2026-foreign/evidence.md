# Evidence — bt-bdaddr-2026-foreign

Desk 2026-11-12 · **standard_version 0.7.1** · Pin: thxomas/bdaddr @ `53dae3f`.

Keine Attack-/Spoofing-Schritte.

## bdaddr @ `53dae3f`

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-BDADDR-2026-11-12-001` | Write BD_ADDR über **vendor-specific** HCI: u. a. Ericsson (`compid` 0/57), Intel (2), CSR (10), TI (13), Broadcom (15), Zeevo (18), ST (48), Cypress (305) | `FACT` | [`bdaddr.c`](https://github.com/thxomas/bdaddr/blob/53dae3f/bdaddr.c) `vendor[]` · [`README.md`](https://github.com/thxomas/bdaddr/blob/53dae3f/README.md) supported manufacturers |
| `EVID-BDADDR-2026-11-12-002` | **Kein Espressif** in `vendor[]` (Tabelle endet mit Cypress 305 + Sentinel 65535) | `FACT` | `bdaddr.c` `vendor[]` Zeilen ~357–367 |
| `EVID-BDADDR-2026-11-12-003` | ESP-Adresse über Stack/Controller-APIs (`esp_base_mac_addr_set` u. ä.), **nicht** über Host-Tool `bdaddr` | `FACT` (Abgrenzung) | Kontrast zu 002; ESP-IDF API-Namen — kein Deep-Pin dieses Audits |
| `EVID-BDADDR-2026-11-12-004` | Link-Keys nach Address Change ungültig / Re-Pair nötig | `INFERENCE` | übliche Stack-Erwartung; `bdaddr` belegt es nicht |
| `EVID-BDADDR-2026-11-12-005` | HU / Peer-Reaktion auf BD_ADDR-Wechsel am Analyse-Adapter | `UNKNOWN` | keine Messung |

## CROSSREF

| Thema | Ort |
|-------|-----|
| BluetoothInterceptor MAC clone out-of-scope / DESIGN Q2 | [`ble-gatt-bluez-relay-2026-foreign`](../ble-gatt-bluez-relay-2026-foreign/) · DESIGN.md @ `4a10bcf` |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-12 | Minimal desk; Sheet `bt-bdaddr-rewrite` angelegt |
