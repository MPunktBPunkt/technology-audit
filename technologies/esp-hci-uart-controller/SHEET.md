# Technology Sheet: ESP HCI UART Controller

```yaml
slug: esp-hci-uart-controller
title: ESP HCI UART Controller (H4 → Linux Host)
primary: D
tags: [esp-idf, bluetooth, hci, bluez]
type: pattern
status: active
seen_in: [esp32-hci-controller-refs]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-hci-controller-2026-foreign
```

Nur Ebene **A**. Pinouts, Baud, Attach-Kommandos → Application / Method.
Dual-Mode Budget on-chip → [`bt-dual-mode-coex`](../bt-dual-mode-coex/SHEET.md).
Eigener TCP/VHCI-Analyzer → [`esp32-bt-analyzer`](../../projects/esp32-bt-analyzer/) (Kontrast, nicht dieses Muster).

## Kurzfassung

Muster: ESP32 (oder kompatibler Controller) läuft **nur als Bluetooth-Controller**; der Host-Stack (BlueZ, Zephyr Host, …) sitzt auf dem Linux-Host und spricht **HCI H4** über UART bzw. USB-UART. UART/USB-UART ist der pragmatische Escape aus WiFi-Coex-/TCP-Brücken-Engpässen — im Gegensatz zum seltenen HCI-over-TCP-Pfad des eigenen Analyzers.

## Abgrenzung

- **Ist:** Controller-only + H4 Transport + Host-Attach (`btattach`/`hciattach`); SCO-über-HCI-Option; VS-HCI-Gate für Third-Party-Hosts.
- **Ist nicht:** Bluedroid/NimBLE Host auf dem ESP; Profil-Endpoint (`bt-analysis-endpoint`); HCI-over-TCP/`/dev/vhci` Analyzer-Pipeline; USB-HCI Observe eines fremden Dongles (`bt-usb-hci-observe-baseline`).
- **Grenzt an:** Chip Classic+BLE (BTDM) vs BLE-only SoC; HWFC vs `noflow`; Reset-Reihenfolge Host↔Controller.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | `esp_bt_controller` BTDM / CONTROLLER_ONLY | Bluedroid oft bewusst aus |
| lateral | UART1 + UHCI (H4), optional HWFC | Defaults häufig TX5/RX18/RTS19/CTS23 @ 921600 |
| oben | BlueZ `btattach -P h4` / `hciattach` | Baud und Flow müssen matchen |
| optional | SCO data path → HCI | HFP Audio auf dem Host |
| parallel | Vendor-Specific HCI | für Third-Party-Hosts typ. **OFF** |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| ESP32 kann Dual-Mode Controller für BlueZ sein (UART H4) | `FACT` | redchenjs / IDF example / dakhnod Pins |
| Default ESP32 HCI UART = Pins 5/18/19/23 @ 921600 + HWFC | `FACT` | redchenjs README + IDF defaults |
| VS HCI muss für Third-Party-Hosts aus | `FACT` | IDF `controller_hci_uart` Docs/Kconfig |
| `hciattach … noflow` = immer gleich gut wie HWFC | `REJECTED` / Gate | dakhnod noflow vs IDF/Zephyr HWFC-Pflicht |
| UART-HCI-Throughput = Analyzer HCI_TCP ~41–45 kB/s | `REJECTED` | andere Physik; Analyzer-WiFi-MEASURED nicht übertragen |
| SCO ohne `SCO_DATA_PATH_HCI` läuft über Host | `REJECTED` / Gate | redchenjs setzt HCI-Pfad; sonst lokal/PCM |
| Reset Host vor Controller stabil | `UNKNOWN` | dakhnod Reset-Tangle Note — Lab |
| BLE-only Chip = Classic HCI Controller | `REJECTED` | Chip-Gate |
| Zephyr `btattach -S 1000000` = ESP-IDF Default 921600 | `REJECTED` | Baud pro Port; nicht mischen |

### Projektstart-Checkliste

- [ ] Chip Classic+BLE (BTDM) bestätigt
- [ ] CONTROLLER_ONLY / Bluedroid off verifiziert
- [ ] UART Pins, Baud, HWFC vs noflow dokumentiert
- [ ] VS HCI für BlueZ/Third-Party OFF
- [ ] SCO-Pfad (HCI vs PCM) bewusst gewählt
- [ ] Attach-Kommando: Method `bt-hci-host-attach`
- [ ] Nicht mit HCI_TCP/VHCI-Analyzer-Zahlen vermischen
- [ ] Application + `seen_in`

## Transfer

Für Lab-Dongles und günstige Dual-Mode-Adapter an Debian/BlueZ: UART H4 Controller-Firmware + Host-Attach. Für Instrumentierung mit WiFi-Sink bleibt der eigene Analyzer-Pfad eigenständig — Sheet nicht als „gleicher Transport“ verkaufen.

## Referenzen

- redchenjs/uart_hci_bluetooth_module_esp32 @ ef5d792
- dakhnod/ESP32-Bluetooth-USB-dongle @ 4ebcbc1
- espressif/esp-idf `examples/bluetooth/controller/controller_hci_uart` @ ~827cc62
- Zephyr `samples/bluetooth/hci_uart` README
- Audit: [`esp32-hci-controller-2026-foreign`](../../audits/esp32-hci-controller-2026-foreign/)

## Offene Fragen

- Lab MEASURED: HCI ACL Throughput UART@921600+HWFC vs USB-UART noflow?
- Stabilste Reset-Reihenfolge BlueZ ↔ ESP Controllers?
- SCO MTU 255:4 (dakhnod Example) vs moderne BlueZ Defaults?
