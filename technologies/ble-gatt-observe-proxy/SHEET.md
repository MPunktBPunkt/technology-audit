# Technology Sheet: BLE GATT Observe Proxy (Analyse)

```yaml
slug: ble-gatt-observe-proxy
title: BLE GATT Observe Proxy (Analysis Dual-Role)
primary: C
tags: [esp-idf, nimble, analysis]
type: pattern
status: active
seen_in: [bt-analysis-relay-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Mechanik Transparent Bridge → `ble-gatt-transparent-bridge`; Dual-Role → `ble-gatt-dual-role`. Offensive MITM-Rezepte **nicht** in der KB.

## Kurzfassung

Analyse-Muster: Dual-Role **GATT Observe/Proxy** mit strukturiertem Logging (UART/MQTT/…), um Phone↔Sensor/Uhr-Traffic zu verstehen. CCCD Source≠Dest; Payloads byte-transparent. Ziel ist **Beobachtbarkeit**, nicht Produkt-Bridge. Bei Bonding/LE Secure Connections ohne Keys → Endpoint oder Host-Sniffer statt Relais.

## Abgrenzung

- **Ist:** Observability-Schicht auf Transparent Dual-Role / Central-Gateway (MQTT).
- **Ist nicht:** Semantic A→B; Classic Audio-MITM; universelles MITM; Endpoint-Impersonation (`bt-analysis-endpoint`).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Upstream | Target GATT (Central) | Discover, Subscribe, optional Encrypt |
| Downstream | Phone/App als Peripheral-Client | Mirror-GATT |
| lateral | Log-Sink | UART hex/JSON, MQTT Topics, File |
| lateral | Dual-Role Budget | `ble-gatt-dual-role` |

## Beobachtbarkeit (A)

| Sichtbar typisch | Oft unsichtbar ohne Keys/Host |
|------------------|-------------------------------|
| UUID/Handle-Map, Notify/Indicate Bytes | Link-Key-Inhalt / verschlüsselte ATT |
| Write/Read Requests (wenn Proxy aktiv) | Phone↔Device ohne ESP im Pfad |
| CCCD Subscribe Events (lokal) | Fremde Bonds ohne Re-Pair |
| MQTT Topic-Tree (ble2mqtt-Stil) | SCO/A2DP Audio-Frames |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Transparent Relais knackt jedes Bonding | `REJECTED` | ohne Keys/Re-Pair oft tot |
| CCCD Downstream steuert Upstream automatisch | `REJECTED` | Source≠Dest — Trace beide |
| MQTT-Gateway = Phone↔Device Relais | `REJECTED` | ble2mqtt = Central-only Analyse-Sink |
| Notify-Congestion egal bei Analyse | `REJECTED` | Drops verfälschen Verständnis |
| Analyse-Proxy = Produktions-Bridge | `REJECTED` | andere Exit-Kriterien |

## Transfer

Fitness-Uhr/Sensor: zuerst Pairing-Modell klären. Logging-Hooks an Transparent-Bridge oder Central-Gateway hängen. Encryption-Gate → `bt-analysis-endpoint` + Method `bt-passive-host-sniff`.

### Projektstart-Checkliste

- [ ] Geräteklasse = BLE GATT (nicht Soundbar/Auto-Audio)
- [ ] Bonding: Re-Pair beider Seiten möglich?
- [ ] Log-Sink gewählt (UART vs MQTT)
- [ ] Dual-Role Budget + CCCD-Trace
- [ ] Fallback Host-Sniffer geplant?
- [ ] Application + `seen_in`

## Referenzen

- ChimeraBLE log/mitm Architektur; esp32-ble2mqtt MQTT sink
- Sheets: `ble-gatt-transparent-bridge`, `ble-gatt-dual-role`

## Offene Fragen

- Minimales Capture-Schema (JSONL) für KB-Evidence?
