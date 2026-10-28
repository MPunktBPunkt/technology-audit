# Project Scope: ble-gatt-bridge-refs (Fremd)

```yaml
project_id: ble-gatt-bridge-refs
title: BLE GATT Bridge / Dual-Role References (Fremd)
updated: 2026-10-28
profile_hint: lab-tool
reviewed_commit: "ChimeraBLE@2330423 iFitnessProxy@1c24f58 ifit@d29ca88 esp32-ble2mqtt@e66ec5a BleRemoteBrideg@958da7c esp32-ble-uart-mx@3451904 btlejuice@981b2e3"
repos:
  - https://github.com/MatthewKuKanich/ChimeraBLE
  - https://github.com/jesusbotella/iFitnessProxy
  - https://github.com/ianchi/ifit
  - https://github.com/shmuelzon/esp32-ble2mqtt
  - https://github.com/QYHHHH/BleRemoteBrideg
  - https://github.com/olegv142/esp32-ble-uart-mx
  - https://github.com/DigitalSecurity/btlejuice
status: active
```

## Zweck

Desk-Extraktion wiederverwendbarer **BLE GATT Bridge**- und **Dual-Role**-Mechanismen. Taxonomie-Lücken schließen gegenüber `ble-hr-relay` (Notify-Fanout) und `bluetooth-ftms` (bidirektional + Control Point) — **nicht** „noch ein HR-Relay“.

## Systeme und Grenzen

| Repo | Rolle im Audit | Im Scope? |
|------|----------------|-----------|
| ChimeraBLE | Dual-Role + transparentes GATT-Clone/Relay (Architektur) | ja — **keine** MITM-/Attack-How-tos |
| iFitnessProxy | Semantic Bridge FTMS→CPS, Dual-Role ESP | ja |
| ifit | Custom↔FTMS Relay + Control-Point; Interceptor nur Architektur | ja — Activation-Capture = Inventar, kein How-to |
| esp32-ble2mqtt | Transparenter GATT↔MQTT Central-Gateway (Kontrast: kein BLE Peripheral) | ja |
| BleRemoteBrideg | Dual-Role HID Semantic Bridge + FSM + Event-Queue | ja |
| esp32-ble-uart-mx | Explizites Dual-Role + Multi-Connection UART-GATT | ja |
| btlejuice | Klassisches GATT Proxy/Clone-Framework (Architektur) | ja — **keine** Exploit-Anleitungen |
| esp32.heartrate / ergo / ftmsprobe | Reuse-Ziel | Querverweis, kein Umbau hier |

## Nicht-Ziele

- Attack-/MITM-Rezepte, Impersonation-Anleitungen, Unauthorized Access
- Neues Produkt-Firmware-Repo
- Classic-vs-S3 Lab-Messung (Chip-Scope bleibt Gate)
- Vollständige CSC/CPS-Spec-Sheets (Kandidat / FOLLOW-ON)

## Prioritäten

1. Neue Pattern-Sheets: Dual-Role, Transparent Bridge, Semantic Bridge  
2. Wachstum `ble-hr-relay` / `bluetooth-ftms` (Cross-Refs, Exclusive Control)  
3. Reuse-Hinweise → heartrate / ergo / ftmsprobe  
4. CCCD-Sync und Control-Point-Routing als Fallstricke, nicht Feature-Liste  
