# Technology Sheet: BT Analysis Endpoint (Impersonation)

```yaml
slug: bt-analysis-endpoint
title: BT Analysis Endpoint (Role Impersonation)
primary: C
tags: [esp-idf, classic-bt, ble, analysis]
type: pattern
status: active
seen_in: [bt-analysis-relay-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Profil-Details → `bluetooth-a2dp` / `bluetooth-hfp` / `bluetooth-hid` / GATT-Sheets.

## Kurzfassung

Analyse-Muster: ESP (oder Host-Stack) **spielt das Peripherie-Gerät** (A2DP Sink, HFP HF, GATT Server, HID Device) und loggt, was das **Telefon wirklich sendet**. Kein MITM zwischen Phone und Original-Gerät — das Original ist ersetzt oder parallel. Pflicht, wenn Transparent-Relais an Encryption/Classic-Audio scheitert.

## Abgrenzung

- **Ist:** Endpoint-Rolle + Logging für Device-Understanding.
- **Ist nicht:** Transparent Phone↔Original Relais; Produktions-Gateway; Audio-Passthrough zum echten Gerät.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Phone → ESP | Profil-Link | A2DP/HFP/GATT/HID |
| ESP → Log / Stream | UART / MQTT / **TCP JSONL** | Events, Metadata, AT, Reports — Export-Muster → `bt-endpoint-event-stream` |
| lateral | Original-Gerät | oft **nicht** im Pfad |

## Geräteklassen (Empfehlung)

| Klasse | Endpoint-Rolle | Log-Fokus |
|--------|----------------|-----------|
| Soundbar | A2DP Sink (+ AVRCP) | Codec, Metadata, Abs Volume |
| Auto / HU | HFP HF + A2DP Sink | Call AT/Indikatoren, SCO start, Media |
| BLE Sensor (wenn Relais nein) | GATT Server Clone oder Central | Services nach Pairing |
| HID | HID Device / HOGP | Report Map, Output |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Endpoint sieht denselben Traffic wie Phone↔Original | `REJECTED` | anderes Peer; Timing/Features können abweichen |
| A2DP-MITM = Endpoint | `REJECTED` | MITM bräuchte zwei Links + Audio-Mux |
| HFP AT ohne SCO-Pfad vollständig | `HYPOTHESIS` | Audio-State separat loggen |
| Ein Endpoint deckt proprietäre Auto-Erweiterungen | `UNKNOWN` | oft Vendor UUID/SDP |
| Classic Endpoint auf BLE-only SoC | `REJECTED` | Chip-Gate |

## Transfer

Soundbar/Auto: Endpoint zuerst; Host-Sniffer am Phone ergänzen. BLE: Endpoint nur wenn Observe-Proxy unmöglich. Immer Profil-Sheet + Dual-Mode-Checkliste mitlesen.

### Projektstart-Checkliste

- [ ] Geräteklasse → Endpoint-Rolle gewählt
- [ ] Profil-Sheets gelesen (A2DP/HFP/HID/GATT)
- [ ] Log-Felder spezifiziert (Events ≠ Audio-Rohdump Pflicht)
- [ ] Export: TCP/JSONL via `bt-endpoint-event-stream` (nicht nur ESP_LOG)
- [ ] Bonding/Name/COD wie Zielgerät (soweit nötig)
- [ ] Parallel: Method `bt-passive-host-sniff`?
- [ ] Application + `seen_in`

## Referenzen

- a2dpSinkHfpClient; EspBle Classic; IDF a2dp_sink / hfp_hf; pschatzmann ESP32-A2DP (Kontrast)

## Offene Fragen

- Minimale AVRCP/HFP Event-Taxonomie für Captures?
