# Technology Sheet: BT Endpoint Event Stream (ESP → Host)

```yaml
slug: bt-endpoint-event-stream
title: BT Endpoint Event Stream (ESP → Host Export)
primary: H
tags: [esp-idf, analysis, streaming]
type: pattern
status: active
seen_in: [bt-sniffing-capture-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Endpoint-Rollen → `bt-analysis-endpoint`; Observe-Proxy → `ble-gatt-observe-proxy`; Passiv Funk → Method `bt-passive-host-sniff`.

## Kurzfassung

Capture-Muster: ESP empfängt auf **Anwendungsebene** (Scan/GATT/HFP/AVRCP/…) und streamt **strukturierte Events** an einen Host (Debian). Bevorzugt **TCP + JSONL**; MQTT/Serial sind verwandte Egress-Pfade. Das ist **kein** OTA-Connection-Follower und kein PCAP-Zwang — PCAP nur wo Link-Layer-Mehrwert besteht.

## Abgrenzung

- **Ist:** App-Level Event-Export, Queues/Drops, Host-Collector.
- **Ist nicht:** nRF LE Sniffer; Android HCI snoop; Classic active piconet-join (BrakTooth-Klasse); Universal-MITM; synthetisches Adv-PCAP als Analyse-SoT.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | BT Stack / Endpoint-Rolle | Scan, GATT, HFP, A2DP-Sig |
| oben | Host | TCP Socket, MQTT Broker, oder UART |
| lateral | Speicherung | SD optional; Host-Datei SoT |

## Transport-Eignung

| Transport | Stärken | Schwächen |
|-----------|---------|-----------|
| **TCP JSONL** | einfach auf Debian (`nc`/Python), zeilenweise | eigener Server nötig |
| MQTT | Queue-Ökosystem, Topics | Broker-Abhängigkeit |
| Serial JSONL | Lab ohne WiFi | Bandbreite/USB |
| SD PCAP | Wireshark offline | kein Live-Stream; Synth-PCAP ≠ RF |

## Minimales Event-Schema (v0)

Pflicht: `ts_ms`, `layer`, `dir`, `op`, Payload (`payload_hex` und/oder `data`).  
Optional: `uuid`/`handle`, `conn`, `seq`, `drop`, `rssi`, `src`.

Beispiel GATT Notify:

```json
{"ts_ms":12345,"src":"esp","dir":"rx","layer":"gatt","op":"notify","uuid":"2a37","payload_hex":"0064","conn":"...","seq":9,"drop":0}
```

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| ESP ersetzt nRF Connection-Follow | `REJECTED` | anderer Mechanismus |
| PCAP immer besser als JSONL für App-Events | `REJECTED` | App-Semantik in JSON oft klarer |
| MQTT ohne Drop-Zähler ist verlustfrei | `REJECTED` | Fremd: Queue16 + dropped_* |
| Endpoint-Events = Phone↔Original Traffic | `REJECTED` | siehe analysis-endpoint |
| OTA ohne Keys liest GATT-Payloads | `REJECTED` | Ciphertext; Endpoint/HCI priorisieren |

## Debian-Collector (Skizze)

```bash
# ESP verbindet sich zu Debian:PORT und sendet JSONL
nc -lk 9000 | tee capture.jsonl
# oder Python: socket → validate → filter layer==hfp → file
```

Backpressure: Host langsam ⇒ ESP braucht Drop-Zähler/`seq`-Lücken sichtbar machen.

## Transfer

Heim-Lab: Endpoint-Rolle wählen → Events mappen → TCP JSONL → Debian. Parallel Method Host-Sniff für Stack-Sicht. Geräteklasse steuert layer-Felder (gatt vs hfp vs avrcp).

### Projektstart-Checkliste

- [ ] Capture-Pfad: Endpoint-Stream vs nRF vs HCI (Matrix)
- [ ] Egress: TCP JSONL (Default) vs MQTT vs Serial
- [ ] Schema v0 Felder + Drop/Seq
- [ ] Rolle aus `bt-analysis-endpoint` / Observe-Proxy
- [ ] Encryption-Gate geklärt
- [ ] Application + `seen_in`

## Referenzen

- wiredlab/esp32-ble-scan-mqtt (JSON + Queues + drops)
- esp32-ble2mqtt (GATT→MQTT)
- ChimeraBLE Serial hex (Kontrast)
- CapibaraZero BLESniffer / BrakTooth / bsniffhub (PCAP/Host-Kontrast)

## Offene Fragen

- Einheitliche `layer`/`op` Enum für HFP AT + AVRCP?
- TLS/Auth für TCP im Heimnetz nötig?
