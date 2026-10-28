# Follow-on ideas (aus bt-analysis-relay-refs)

```yaml
reuse_outcomes:
  reused:
    - ble-gatt-transparent-bridge
    - ble-gatt-dual-role
    - bluetooth-hfp
    - bluetooth-a2dp
    - hid-cross-transport-bridge
    - bt-dual-mode-coex
  new:
    - ble-gatt-observe-proxy
    - bt-analysis-endpoint
    - bt-passive-host-sniff
  not_helped:
    - "A2DP-Passthrough-MITM als Analyseziel"
    - "universelles ESP-MITM bei LE Secure Connections ohne Keys"
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Lab: Phone↔Watch mit Observe-Proxy + MQTT Dump | observe-proxy, ble2mqtt | strukturierte Captures |
| Lab: Soundbar via A2DP-Sink Endpoint | analysis-endpoint, a2dp | Metadata/AVRCP |
| Lab: Auto HFP AT-Log | analysis-endpoint, hfp | Call-Setup Trace |
| Bonding-Grenze dokumentieren (eigene Keys) | observe-proxy | Gate |
