# Project Scope: esp32-hci-controller-refs (Fremd)

```yaml
project_id: esp32-hci-controller-refs
title: ESP32 as Bluetooth HCI Controller for Linux Hosts (Fremd)
updated: 2026-11-12
profile_hint: lab-tool
reviewed_commit: "redchenjs@ef5d792 dakhnod@4ebcbc1 esp-idf@827cc62 zephyr-hci_uart-docs"
repos:
  - https://github.com/redchenjs/uart_hci_bluetooth_module_esp32
  - https://github.com/dakhnod/ESP32-Bluetooth-USB-dongle
  - https://github.com/espressif/esp-idf/tree/master/examples/bluetooth/controller/controller_hci_uart
  - https://docs.zephyrproject.org/latest/samples/bluetooth/hci_uart/README.html
status: active
```

## Zweck

Desk: ESP32 (Classic + BLE Controller) als **HCI-Transport-Endpunkt** für einen Linux-Host-Stack (BlueZ/`btattach`/`hciattach`) — UART H4 mit optional HWFC, bzw. USB-UART-Brücke. Kontrast zum eigenen [`esp32-bt-analyzer`](../esp32-bt-analyzer/) (HCI-over-TCP + `/dev/vhci`).

## Systeme und Grenzen

| Quelle | Rolle | Im Scope? |
|--------|-------|-----------|
| redchenjs/uart_hci_bluetooth_module_esp32 @ ef5d792 | H4 UART HCI Module, Pinmap, SCO→HCI, `btattach` | ja |
| dakhnod/ESP32-Bluetooth-USB-dongle @ 4ebcbc1 | CONTROLLER_ONLY USB-UART Dongle, `hciattach`, SCO MTU note | ja |
| espressif/esp-idf `controller_hci_uart` @ ~827cc62 | Offizielles unified Example (IDF; alt `controller_hci_uart_esp32` entfernt ab v6.1) | ja |
| Zephyr `samples/bluetooth/hci_uart` Docs | Host/Controller-Split + `btattach` Architektur-Referenz | ja — Docs/Architektur |
| BlueZ `btattach` / `hciattach` / `hciconfig` | Host-Attach-Pfad | Method + Evidence |
| esp32-bt-analyzer HCI-over-TCP / VHCI | Kontrast eigener WiFi-Pfad | Cross-Ref only |

## Nicht-Ziele

- Feldmessungen an UART/USB-UART-Throughput (keine erfundenen kB/s)
- Attack-/Exploit-How-tos für HCI Inject
- Host-Stack-Implementierung (BTstack/NimBLE Host auf dem ESP) als Primärziel
- WiFi-Coex-Messung des eigenen TCP-Bridges als Evidence für diese UART-Repos

## Prioritäten

1. Sheet `esp-hci-uart-controller` (primary D — Embedded Controller-Transport)
2. Method `bt-hci-host-attach`
3. Kontrast UART/USB-UART vs. HCI-over-TCP (Analyzer)
4. SCO-Pfad / VS-HCI / Reset-Tangle als Fallstricke
