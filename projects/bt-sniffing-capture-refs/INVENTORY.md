# Project Inventory: bt-sniffing-capture-refs

```yaml
project_id: bt-sniffing-capture-refs
updated: 2026-10-28
reviewed_commit: "multi-2026-10-28"
profile: lab-tool
pilot_order: [bt-endpoint-event-stream, bt-passive-host-sniff, bt-analysis-endpoint]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel | Aktion |
|--------|------|--------|
| ESP App-Events → Host (MQTT/TCP/Serial/JSON) | `bt-endpoint-event-stream` | **neu** |
| nRF / HCI passiv | Method `bt-passive-host-sniff` | **wachsen** |
| Endpoint-Rollen | `bt-analysis-endpoint` | **wachsen** (Export) |
| Observe Dual-Role | `ble-gatt-observe-proxy` | reused |
| GATT→MQTT | ble2mqtt | Evidence |
| Adv→JSON Queues | esp32-ble-scan-mqtt | Evidence |
| PCAP-Synthese / Classic UART→PCAP | BLESniffer / BrakTooth | Kontrast |
| Host Dongle Hub | bsniffhub | Kontrast |

Kampagne: [bt-sniffing-capture-2026-foreign](../../audits/bt-sniffing-capture-2026-foreign/).

## Muster × Quelle

| Quelle @ pin | Pattern | Sichtbar | Transport |
|--------------|---------|----------|-----------|
| scan-mqtt `ee096de` | App Adv-Scan | Adv JSON | MQTT/TCP, Serial JSONL, SD |
| BLESniffer `1bea2e8` | App Adv→PCAP synth | Adv | SD PCAP DLT251 |
| classic_sniffer `0e174ca` | Classic active follow | LMP/ACL meta | UART binary → Host PCAPNG |
| bsniffhub `29049d7` | Host LE dongle | LL Adv/ACL (+LTK) | Serial→PCAP/pipe |
| ble2mqtt `e66ec5a` | GATT Central | Notify/Read typed | MQTT |
| Chimera `2330423` | Dual-Role / dump | GATT hex | Serial |
| a2dpSink `df6c5f4` | Endpoint HFP/A2DP | AT/Audio-state | ESP_LOG (kein TCP-SoT) |
| Eidolon | — | — | **nicht gefunden** |

## Geräteklasse → Capture-Pfad

| Klasse | Primär | Alternativ |
|--------|--------|------------|
| Uhr/Sensor | ESP GATT Endpoint/Central + **TCP/JSONL** | HCI-Snoop; nRF bei fremder Connection |
| Soundbar | ESP A2DP-Sink + AVRCP Events → TCP | Phone HCI-Snoop |
| Auto | ESP HFP-HF (+A2DP) Events → TCP | Phone HCI-Snoop |
| Encrypted fremd | Host-Sniffer zuerst | kein ESP-OTA-MITM |

## Minimales Event-Schema (v0 JSONL)

```json
{"ts_ms":0,"src":"esp","dir":"rx","layer":"gatt","uuid":"2a37","handle":42,"op":"notify","payload_hex":"...","conn":"aa:bb:...","seq":1,"drop":0}
```

Pflichtfelder: `ts_ms`, `layer` (`adv`|`gatt`|`hfp`|`avrcp`|`a2dp_sig`|`hid`), `dir` (`rx`|`tx`|`evt`), `op`, `payload_hex` oder strukturiertes `data`. Optional: `uuid`/`handle`, `conn`, `seq`, `drop`, `rssi`.

## Übersicht Sheets

| Slug | Status | Coverage | Sheet | Application |
|------|--------|----------|-------|-------------|
| `bt-endpoint-event-stream` | applied | partial | [SHEET](../../technologies/bt-endpoint-event-stream/SHEET.md) | [app](applications/bt-endpoint-event-stream.md) |
| `bt-analysis-endpoint` | documented | partial | [SHEET](../../technologies/bt-analysis-endpoint/SHEET.md) | — |
| `ble-gatt-observe-proxy` | documented | partial | [SHEET](../../technologies/ble-gatt-observe-proxy/SHEET.md) | — |

**Method:** [`bt-passive-host-sniff`](../../methods/bt-passive-host-sniff.md)
