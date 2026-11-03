# Follow-on ideas (aus esp32.bt-analyzer)

Ideen aus dem Bootstrap — noch keine neuen Repos.

```yaml
reuse_outcomes:
  reused: [esp-usb-host, esp-hub-telemetry, esp32-s3-silicon, bt-passive-host-sniff]
  new: []
  not_helped: []
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Erste VID/PID USB-BT Enum | `esp-usb-host` | BT1 Gate |
| HCI raw → btsnoop/PCAPNG | Method HCI snoop | BT3–BT8 |
| BLE vs Classic Dongle Matrix | Capture family | BT9/BT10 getrennt claimen |
| WiFi↔USB Host Coex unter Last | `esp32-s3-usb-wifi-coex` | vor lossless BT6 |
| Stimulus ESP (kein MITM-Label) | Dual-ESP Pattern | BT11 |
| RF/Air Capability | nRF / externe Sniffer | **BT15 separat** |
