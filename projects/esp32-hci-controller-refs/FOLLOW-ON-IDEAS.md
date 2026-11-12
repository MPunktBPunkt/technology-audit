# Follow-on ideas (aus esp32-hci-controller-refs)

```yaml
reuse_outcomes:
  reused:
    - bt-dual-mode-coex
    - bt-usb-hci-observe-baseline
    - bt-passive-host-sniff
  new:
    - esp-hci-uart-controller
    - bt-hci-host-attach
  not_helped:
    - "HCI-over-TCP /dev/vhci als Ersatz für UART-Dongle-Pfad"
    - "WiFi-Coex-Zahlen aus esp32-bt-analyzer als UART-Throughput"
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Lab: `btattach` H4 921600+HWFC Smoke auf Debian | Method attach, redchenjs/IDF pins | `hciconfig`/`bluetoothctl` up; Evidence MEASURED |
| Lab: USB-UART Dongle vs native UART Latency | dakhnod vs redchenjs | Reset-Tangle + noflow vs HWFC |
| SCO path gate: HCI vs PCM | IDF/community `SCO_DATA_PATH` | HFP Audio über Host vs lokal |
| Kontrast-Messung: UART HCI vs Analyzer HCI_TCP | esp32-bt-analyzer STATUS | getrennte Evidence-IDs; WiFi-Pfad nicht mischen |
| Zephyr Host an ESP Controller | Zephyr hci_uart Docs | Architektur-Transfer, Baud/HWFC Gate |
