# Project Inventory: esp32-hci-controller-refs

```yaml
project_id: esp32-hci-controller-refs
updated: 2026-11-12
reviewed_commit: "multi-2026-11-12"
profile: lab-tool
pilot_order: [esp-hci-uart-controller, bt-hci-host-attach]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel | Aktion |
|--------|------|--------|
| ESP32 Controller-only + UART H4 → BlueZ | `esp-hci-uart-controller` | **neu** |
| `btattach`/`hciattach` Host-Attach Prozedur | Method `bt-hci-host-attach` | **neu** |
| Dual-Mode Controller (BTDM) | `bt-dual-mode-coex` | reused (Kontrast: Host off-chip) |
| HCI Capture / Observe am Host | `bt-usb-hci-observe-baseline`, `bt-passive-host-sniff` | reused Kontrast |
| Eigener HCI-over-TCP + VHCI Analyzer | `esp32-bt-analyzer` | Cross-Ref — **nicht** dieses Sheet |
| Classic Profile Endpoint auf ESP | `bt-analysis-endpoint` / A2DP/HFP Sheets | Abgrenzung: hier Host = Linux |

Kampagne: [esp32-hci-controller-2026-foreign](../../audits/esp32-hci-controller-2026-foreign/).

## Muster × Quelle

| Quelle | Transport | Host-Attach | Controller-Scope | Besonderheit |
|--------|-----------|-------------|------------------|--------------|
| redchenjs @ ef5d792 | UART1 H4 + HWFC (TX5/RX18/RTS19/CTS23), 921600 | `btattach -B … -P h4 -S 921600` | BTDM; UHCI+UART dann `esp_bt_controller_enable(BTDM)` | `CONFIG_BTDM_CTRL_BR_EDR_SCO_DATA_PATH_HCI=y` |
| dakhnod @ 4ebcbc1 | UART H4 921600 (USB-UART Dongle) | `hciattach -s 921600 … any 921600 noflow` | CONTROLLER_ONLY, Bluedroid off, BTDM | SCO MTU `255:4` in `hciconfig`-Beispiel; Reset-Tangle Note |
| IDF `controller_hci_uart` @ ~827cc62 | H4; ESP32 Defaults = gleiche Pins/921600+HWFC | BlueZ / third-party Host | Controller Example (unified; alt ESP32-only removed IDF v6.1) | **VS HCI OFF** für Third-Party-Hosts; SCO-Pfad in Community-Forks |
| Zephyr hci_uart Docs | UART + **HWFC required** | `btattach -B … -S 1000000`; `-R` QEMU proxy | Host/Controller Split Referenz | Architektur, nicht ESP-IDF Port |

## Übersicht Sheets / Methods

| Slug | Name | Primary | Status | Coverage | Sheet / Note | Application |
|------|------|---------|--------|----------|--------------|-------------|
| `esp-hci-uart-controller` | ESP HCI UART Controller | D | applied | partial | [SHEET](../../technologies/esp-hci-uart-controller/SHEET.md) | [app](applications/esp-hci-uart-controller.md) |

**Method (kein Inventar-Status):** [`bt-hci-host-attach`](../../methods/bt-hci-host-attach.md) — `btattach`/`hciattach` an ESP32 H4.
