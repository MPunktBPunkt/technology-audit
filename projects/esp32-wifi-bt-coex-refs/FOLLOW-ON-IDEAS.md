# Follow-on ideas (aus esp32-wifi-bt-coex-refs)

```yaml
reuse_outcomes:
  reused: [bt-dual-mode-coex, esp32-s3-usb-wifi-coex]
  new: [esp-wifi-bt-coex]
  not_helped:
    - "esp32-s3-usb-wifi-coex — USB-PHY, nicht RF WiFi↔BT"
    - "bt-dual-mode-coex — Classic+BLE, nicht WiFi-TDM"
    - "öffentliche Repos mit systematischer esp_coex_* + Classic-A2DP + WiFi-Throughput-Messung — nicht gefunden"
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Lab: STA+BT Connected vs SoftAP CONNECTED+BT (C1) unter HCI_TCP-Last | Sheet SoftAP/STA-Karte | Diskriminator für bt-analyzer Topology |
| Lab: `esp_coex_status_bit_*` A2DP_STREAMING vs idle; Throughput/ACL-kB/s | Status-Bits + #12434 | misst, ob App-Bits vs Bluedroid Vendor-Pfad wirken |
| Architektur: UART HCI / offload vs same-chip SoftAP/STA Coex-Tuning | Key Decision | Produktentscheid vor Feintuning |
| EXTERNAL PTA wire 1/2/3 nur bei Multi-Chip-RF | Header EXTERNAL | selten für Analyzer-Lab |
| bt-analyzer Application: HCI_TCP ACL-Zahlen nur als Projekt-`MEASURED` zitieren | Application Kontrast | nie als Fremd-Desk-FACT |
