# Follow-on ideas (aus bt-sniffing-capture-refs)

```yaml
reuse_outcomes:
  reused: [bt-analysis-endpoint, ble-gatt-observe-proxy, bt-passive-host-sniff, bluetooth-hfp, bluetooth-a2dp]
  new: [bt-endpoint-event-stream]
  not_helped: ["ESP OTA connection-follow statt nRF", "Eidolon als HFP-TCP-Vorbild — nicht gefunden", "PCAP-Pflicht für App-Events"]
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| ESP Firmware: GATT/HFP Events → TCP JSONL | event-stream | Lab-Collector |
| Debian: `nc -l` / Python JSONL Writer + Filter | event-stream | Capture-Repo |
| AVRCP/HFP Event-Taxonomie festnageln | analysis-endpoint | Schema v1 |
