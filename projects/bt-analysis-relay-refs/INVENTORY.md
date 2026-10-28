# Project Inventory: bt-analysis-relay-refs

```yaml
project_id: bt-analysis-relay-refs
updated: 2026-10-28
reviewed_commit: "multi-2026-10-28"
profile: lab-tool
pilot_order: [ble-gatt-observe-proxy, bt-analysis-endpoint, bt-passive-host-sniff]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel | Aktion |
|--------|------|--------|
| Transparent Dual-Role + Logging | `ble-gatt-observe-proxy` | **neu** (Analyse-Dach über transparent-bridge) |
| ESP = A2DP/HFP/GATT-Server zum Lernen | `bt-analysis-endpoint` | **neu** |
| Passiv nRF / HCI snoop | Method `bt-passive-host-sniff` | **neu** |
| Transparent Clone-Mechanik | `ble-gatt-transparent-bridge` | reused |
| Dual-Role Budget | `ble-gatt-dual-role` | reused |
| HFP/A2DP/HID Cross | `bluetooth-hfp`, `bluetooth-a2dp`, `hid-cross-transport-bridge` | reused |
| MQTT GATT Sink | ble2mqtt → Observe-Proxy Transfer | Evidence |

Kampagne: [bt-analysis-relay-2026-foreign](../../audits/bt-analysis-relay-2026-foreign/).

## Muster × Quelle

| Quelle | Muster | Beobachtbarkeit | Encryption-Grenze |
|--------|--------|-----------------|-------------------|
| ChimeraBLE | Transparent Dual-Role | UART JSON/hex (`log.cpp`) | Bonding/Keys; aktiver MITM-Pfad Inventar only |
| ble2mqtt | Central→MQTT (kein Peripheral-Mirror) | MQTT Topics = Analyse-Sink | Bonding am Central; kein Phone↔Device MITM |
| uart-mx | Custom GATT Dual + Multi-Peer | Serial protocol | App-Bond |
| btlejuice | 2-HCI Host Proxy | UI Hex/Hooks | Architektur-Referenz; nicht ESP |
| a2dpSinkHfpClient | **Endpoint** A2DP+HFP | ESP_LOG Call/Audio/AVRC | Pairing als Sink/HF — sieht Phone→Endpoint |
| EspBle | Endpoint + Dual-Host | Profile-APIs/Tests | ESP32 Classic Gate |
| bthidbridge | Cross-Transport | Forward-Logs | BTDM; Bond NVS |
| IDF examples | Endpoint-Rollen | Example logs | BR/EDR-only Defaults |

## Geräteklassen-Empfehlung

| Klasse | Primär | Sekundär | ESP-Relais? |
|--------|--------|----------|-------------|
| Fitness-Uhr / BLE-Sensor | Observe-Proxy **oder** GATT-Central-Log (ble2mqtt) | nRF Sniffer | ja, wenn unverschlüsselt/mit Pairing beider Seiten |
| Soundbar | **A2DP-Sink Endpoint** | HCI snoop am Phone | kein transparentes Audio-MITM |
| Auto / HU | **HFP-HF + A2DP-Sink Endpoint** | Phone HCI snoop | Endpoint; proprietäre Erweiterungen UNKNOWN |
| HID Gamepad/Keyboard | HOGP Endpoint oder Cross-Transport | nRF / HCI | Bridge nur Legacy-Host |
| Beliebig verschlüsselt | Host-Sniffer + Endpoint | — | Transparent MITM oft unmöglich |

## Übersicht Sheets

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `ble-gatt-observe-proxy` | BLE GATT Observe Proxy | C | applied | partial | [SHEET](../../technologies/ble-gatt-observe-proxy/SHEET.md) | [app](applications/ble-gatt-observe-proxy.md) |
| `bt-analysis-endpoint` | BT Analysis Endpoint | C | applied | partial | [SHEET](../../technologies/bt-analysis-endpoint/SHEET.md) | [app](applications/bt-analysis-endpoint.md) |

**Method (kein Inventar-Status):** [`bt-passive-host-sniff`](../../methods/bt-passive-host-sniff.md) — nRF / HCI snoop.
