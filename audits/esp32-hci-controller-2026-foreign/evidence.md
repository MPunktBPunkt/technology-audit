# Evidence — esp32-hci-controller-2026-foreign

Desk 2026-11-12 · **standard_version 0.7.1**. Keine UART-Throughput-MEASURED erfunden.

## redchenjs / uart_hci_bluetooth_module_esp32 @ ef5d792

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-HCICTRL-2026-11-12-001` | H4 UART HCI; Pinmap HOST↔ESP TX/RX/CTS/RTS → ESP pins **5 / 18 / 19 / 23**; Baud **921600**; BTDM Controller | `FACT` | README Pinmap + sdkconfig @ ef5d792 |
| `EVID-HCICTRL-2026-11-12-002` | App: UHCI + UART1 enable, dann `esp_bt_controller_enable(BTDM)`; Host: `btattach -B … -P h4 -S 921600` | `FACT` | `main` + README @ ef5d792 |
| `EVID-HCICTRL-2026-11-12-003` | `CONFIG_BTDM_CTRL_BR_EDR_SCO_DATA_PATH_HCI=y` (SCO über HCI) | `FACT` | sdkconfig.defaults / Kconfig @ ef5d792 |

## dakhnod / ESP32-Bluetooth-USB-dongle @ 4ebcbc1

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-HCICTRL-2026-11-12-010` | CONTROLLER_ONLY; Bluedroid off; BTDM; UART H4 **921600** | `FACT` | sdkconfig / README @ 4ebcbc1 |
| `EVID-HCICTRL-2026-11-12-011` | Host-Beispiel: `hciattach -s 921600 … any 921600 noflow`; SCO MTU **255:4** via `hciconfig`; Reset-Tangle dokumentiert | `FACT` | README @ 4ebcbc1 |

## espressif / esp-idf controller_hci_uart @ ~827cc62

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-HCICTRL-2026-11-12-020` | Unified `controller_hci_uart` (alt `controller_hci_uart_esp32` removed IDF **v6.1**); H4; ESP32 Defaults = gleiche Pins / 921600 + HWFC; **VS HCI must be OFF** for third-party hosts; SCO-Pfad-Config in Community-Forks vorhanden | `FACT` | example README / Kconfig @ idf master ~827cc62 |

## Zephyr hci_uart (Docs)

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-HCICTRL-2026-11-12-030` | Docs: `btattach -B … -S 1000000`; **HWFC required**; `-R` for QEMU proxy; Host/Controller-Split Architektur-Referenz | `FACT` | Zephyr `samples/bluetooth/hci_uart` README |

## Kontrast / Epistemik

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-HCICTRL-2026-11-12-040` | UART/USB-UART HCI ist Community-Standard-Escape aus WiFi-Coex-Bottleneck; HCI-over-TCP + `/dev/vhci` (eigener Analyzer) ist selten/unique | `INFERENCE` | Desk Contrast vs [`esp32-bt-analyzer`](../../projects/esp32-bt-analyzer/) |
| — | UART-HCI Throughput dieser Upstream-Repos | `UNKNOWN` | keine Lab-Messung in dieser Kampagne |
| — | Analyzer ACL/WiFi ~41–45 kB/s (`none` Gate) | own `MEASURED` **nur** in Analyzer-STATUS | [`STATUS.md`](../../projects/esp32-bt-analyzer/STATUS.md) — **nicht** UART-Evidence |
| Transfer Analyzer-kB/s → UART-Repos | — | `REJECTED` | andere Physik / anderer Pfad |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Lab `btattach` Smoke 921600+HWFC auf Debian | `UNKNOWN` | FOLLOW-ON |
| Reset-Reihenfolge Host vs ESP stabil | `UNKNOWN` | dakhnod Tangle |
| SCO Audio End-to-End über BlueZ mit HCI-Pfad | `UNKNOWN` | Config FACT ≠ Feld |
| USB-UART Latency vs native UART | `UNKNOWN` | Lab |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-12 | Foreign Desk: redchenjs + dakhnod + IDF + Zephyr Docs → Sheet/Method + Kontrast Analyzer |
