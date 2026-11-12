# Project Application: esp-hci-uart-controller in esp32-hci-controller-refs

```yaml
project_id: esp32-hci-controller-refs
tech_slug: esp-hci-uart-controller
status: active
sheet: ../../../technologies/esp-hci-uart-controller/SHEET.md
audit: ../../../audits/esp32-hci-controller-2026-foreign/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| redchenjs: H4 UART HCI, Pins TX5/RX18/RTS19/CTS23, 921600, BTDM | `EVID-HCICTRL-2026-11-12-001` | `FACT` |
| redchenjs: UHCI+UART1 enable → `esp_bt_controller_enable(BTDM)`; `btattach -P h4 -S 921600` | `EVID-HCICTRL-2026-11-12-002` | `FACT` |
| redchenjs: `CONFIG_BTDM_CTRL_BR_EDR_SCO_DATA_PATH_HCI=y` | `EVID-HCICTRL-2026-11-12-003` | `FACT` |
| dakhnod: CONTROLLER_ONLY, Bluedroid off, BTDM, UART H4 921600 | `EVID-HCICTRL-2026-11-12-010` | `FACT` |
| dakhnod: `hciattach -s 921600 … any 921600 noflow`; SCO MTU 255:4 Example; Reset-Tangle Note | `EVID-HCICTRL-2026-11-12-011` | `FACT` |
| IDF `controller_hci_uart`: H4, ESP32 Default-Pins/921600+HWFC; VS HCI OFF für Third-Party; unified (alt ESP32 example removed v6.1) | `EVID-HCICTRL-2026-11-12-020` | `FACT` |
| Zephyr hci_uart Docs: `btattach -S 1000000`, HWFC required, `-R` QEMU | `EVID-HCICTRL-2026-11-12-030` | `FACT` |
| UART/USB-UART = Escape aus WiFi-Coex-Bottleneck vs Analyzer HCI_TCP | `EVID-HCICTRL-2026-11-12-040` | `INFERENCE` |
| UART-HCI Lab-Throughput dieser Repos | — | `UNKNOWN` (kein MEASURED in dieser Kampagne) |

## Abgrenzung zu esp32-bt-analyzer

Eigener Analyzer: HCI-over-TCP + `/dev/vhci`. ACL/WiFi-Pfad-Zahlen (~41–45 kB/s Gate in [`STATUS`](../../esp32-bt-analyzer/STATUS.md)) sind **dessen** WiFi-MEASURED — **nicht** auf UART-Repos übertragen.
