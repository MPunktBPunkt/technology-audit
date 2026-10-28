# Project Scope: bt-analysis-relay-refs (Fremd)

```yaml
project_id: bt-analysis-relay-refs
title: Bluetooth Analyse-Relais & Device-Understanding (Fremd)
updated: 2026-10-28
profile_hint: lab-tool
reviewed_commit: "ChimeraBLE@2330423 esp32-ble2mqtt@e66ec5a uart-mx@3451904 btlejuice@981b2e3 a2dpSinkHfpClient@df6c5f4 EspBle@ef09bed esp32-bthidbridge@5d3a563 esp-idf@4d80c1b"
repos:
  - https://github.com/MatthewKuKanich/ChimeraBLE
  - https://github.com/shmuelzon/esp32-ble2mqtt
  - https://github.com/olegv142/esp32-ble-uart-mx
  - https://github.com/DigitalSecurity/btlejuice
  - https://github.com/walinsky/a2dpSinkHfpClient
  - https://github.com/tanakamasayuki/EspBle
  - https://github.com/anarsoul/esp32-bthidbridge
  - https://github.com/espressif/esp-idf/tree/master/examples/bluetooth
status: active
```

## Zweck

Desk: **Beobachtbarkeit** von Phone↔Peripherie-Flows (Uhr/Sensor/Soundbar/Auto/HID) — nicht Produktions-Bridge. Muster: Transparent Observe-Proxy, Endpoint-Impersonation, Cross-Transport nur wo nötig, Host-Sniffer-Grenzen.

## Systeme und Grenzen

| Quelle | Analyse-Muster | Im Scope? |
|--------|----------------|-----------|
| ChimeraBLE | Transparent Dual-Role GATT + UART-Hex-Log (Architektur) | ja — keine Attack-How-tos |
| esp32-ble2mqtt | Transparent GATT→MQTT Analyse-Sink | ja |
| uart-mx | Custom-GATT Multi-Conn Serial | ja |
| btlejuice | Host-HCI MITM-Architektur (Kontrast) | ja — Inventar only |
| a2dpSinkHfpClient | A2DP+HFP **Endpoint** (was Phone sendet) | ja |
| EspBle | Classic Endpoint + Dual-Host | ja |
| esp32-bthidbridge | Cross-Transport HID + BTDM | ja |
| IDF examples | Rollen-SoT | ja |
| nRF Sniffer / Android HCI snoop | Passiv Host | Method Note |
| GATTacker/Bettercap | Host-MITM Kontrast | Inventar-Hinweis only |

## Nicht-Ziele

- Universelles MITM / Key-Extraction-Rezepte
- Produktions-Bridge-Firmware
- A2DP-Passthrough-MITM (Audio) als Anspruch
- Semantic FTMS→CPS außer als Kontrast

## Prioritäten

1. Sheets `ble-gatt-observe-proxy`, `bt-analysis-endpoint`  
2. Method `bt-passive-host-sniff`  
3. Geräteklassen-Empfehlung ESP vs Host-Sniffer  
4. Cross-Refs zu transparent-bridge / hfp / a2dp / hid-cross-transport  
