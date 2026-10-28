# Technology Sheet: Bluetooth SPP (Serial Port Profile)

```yaml
slug: bluetooth-spp
title: Bluetooth SPP (Serial Port Profile)
primary: C
tags: [esp-idf, classic-bt]
type: protocol
status: active
seen_in: [bt-classic-profile-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. BLE-UART/Custom-GATT → Kontrast `ble-gatt-transparent-bridge` / feste `FFE0`-Muster.

## Kurzfassung

Classic **Serial Port Profile** über **RFCOMM**: Server (Acceptor) und/oder Client (Initiator) exponieren einen Byte-Stream. Typisch für Legacy-Tools, Diagnostics und Hosts ohne BLE-GATT. Channel (SCN) oft 0 = dynamisch; Bonding/Security sind Produktentscheidungen, nicht „SPP default open“.

## Abgrenzung

- **Ist:** RFCOMM-Serial Classic; Server/Client-Rollen; Congestion/Write-Chunking.
- **Ist nicht:** BLE Nordic UART / `FFE0` GATT; HFP-RFCOMM (AT+SCO); TCP/IP; SPP als generisches „Classic Relay“.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | App-Stream / VFS | Read/Write, Congestion-Wait |
| unten | Bluedroid `esp_spp_*` / BTstack RFCOMM | SDP Record |
| lateral | GAP Discovery | Name/COD → Client Connect |
| lateral | Security | `SEC_NONE` vs Bonding/SSP |

## Wann Classic SPP vs BLE Serial

| Bedarf | Tendenz |
|--------|---------|
| Legacy Host erwartet SPP/RFCOMM | **SPP** |
| Mobile App modern, niedriger Energie | **BLE GATT** |
| Dual-Mode ESP32 + BLE schon aktiv | BLE oft einfacher; SPP braucht Classic-Budget |
| Multi-Client Fanout | beides begrenzt — Budget prüfen |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| SPP = BLE-UART mit anderem Namen | `REJECTED` | anderer Transport/Stack |
| SCN 0 ist immer Kanal 1 | `REJECTED` | dynamische Vergabe üblich |
| `ESP_SPP_SEC_NONE` + PIN 1234 produktionsreif | `REJECTED` | Demo-Defaults |
| Unbegrenzte parallele SPP-Clients | `REJECTED` | oft Single-Client Disconnect |
| SPP auf BLE-only SoCs | `REJECTED` | Classic nötig |

## Transfer

Diagnostics/Legacy-Bridges: Minimal-Pattern Acceptor + Congestion. Produkt: Security und Reconnect-Policy explizit. Parallel zu A2DP/HFP: Connection-Budget.

### Projektstart-Checkliste

- [ ] Server vs Client (oder beides)
- [ ] Security/Bonding vs Demo-`SEC_NONE`
- [ ] Single- vs Multi-Client Policy
- [ ] Reconnect/Discovery-Loop
- [ ] Alternative BLE-Serial erwogen? (Abgrenzung)
- [ ] Application + `seen_in`

## Referenzen

- ESP-IDF `bt_spp_acceptor` / `bt_spp_initiator` (+ VFS)
- BTClassicSPP; EspBle `EspBleClassicSppStream`
- btstack `spp_server.c` + `rfcomm.c`

## Offene Fragen

- VFS-SPP vs Raw-Callback: wann welcher Pfad auf ESP-IDF?
