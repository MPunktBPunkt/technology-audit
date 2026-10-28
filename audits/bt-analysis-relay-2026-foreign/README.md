# Audit Campaign: bt-analysis-relay-2026-foreign

```yaml
id: bt-analysis-relay-2026-foreign
project_id: bt-analysis-relay-refs
started: 2026-10-28
ended: 2026-10-28
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "multi-2026-10-28"
upstream_pins:
  ChimeraBLE: "2330423"
  esp32-ble2mqtt: "e66ec5a"
  esp32-ble-uart-mx: "3451904"
  btlejuice: "981b2e3"
  a2dpSinkHfpClient: "df6c5f4"
  EspBle: "ef09bed"
  esp32-bthidbridge: "5d3a563"
  esp-idf: "4d80c1b"
reuse_outcomes:
  reused:
    - ble-gatt-transparent-bridge
    - ble-gatt-dual-role
    - bluetooth-hfp
    - bluetooth-a2dp
    - bluetooth-hid
    - hid-cross-transport-bridge
    - bt-dual-mode-coex
  new:
    - ble-gatt-observe-proxy
    - bt-analysis-endpoint
    - bt-passive-host-sniff
  not_helped:
    - "A2DP audio MITM als Analyseziel"
    - "ESP-Relais bei LE Secure Connections ohne Keys"
  process: "Desk Analyse-Muster; Relais nur wo transparent; sonst Endpoint + Host-Sniffer."
  decisions_touched:
    - fact-observe-proxy-vs-endpoint
    - reject-universal-esp-mitm
    - fact-mqtt-as-analysis-sink
    - fact-device-class-tooling-matrix
```

## Ziel

Phone↔Peripherie **verstehen** (Uhr/Sensor/Soundbar/Auto/HID): Observe-Proxy vs Endpoint vs Host-Sniffer — geräteklassenbezogen, beobachtbarkeitszentriert.

## Scope

[SCOPE](../../projects/bt-analysis-relay-refs/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + pins | erfüllt |
| 2 | Muster-Matrix + Geräteklassen-Empfehlung | erfüllt |
| 3 | Sheets observe-proxy + analysis-endpoint | erfüllt |
| 4 | Method bt-passive-host-sniff | erfüllt |
| 5 | Encryption/Bonding-Grenzen dokumentiert | erfüllt |
| 6 | C10–C12 | erfüllt |
| 7 | `ta-assist check` 0 errors | erfüllt |
| 8 | Lab Captures Phone↔Uhr/Soundbar | FOLLOW-ON |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Zwei Analyse-Sheets | Relais = Endpoint? | Matrix | Observe vs Endpoint | KNOWN BEFORE |
| ble2mqtt = Observe-Familie | Peripheral Mirror? | `…-010` | Central-Sink, kein MITM | DISCOVERED |
| Soundbar → Endpoint | Audio-MITM? | `…-031` | `REJECTED` Relais | KNOWN BEFORE |
| Method für nRF/HCI | Sheet? | — | Method Note | KNOWN BEFORE |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-002` | CCCD beide Seiten tracen |
| `…-010` | MQTT-Sink nicht als Phone↔Device Relais verkaufen |
| `…-030` | HFP/A2DP Endpoint-Logs ≠ Original-Peer Traffic |
| Encryption | ohne Keys → Endpoint/Sniffer Gate |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Generisches ble-relay ohne Analyse-Unterscheidung | `REJECTED` |
| 2 | Attack-How-tos in Sheets | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk schließt Tooling-Wahl; Lab-Captures FOLLOW-ON.
```

## Empfehlung kurz

| Geräteklasse | Tooling |
|--------------|---------|
| BLE Uhr/Sensor | Observe-Proxy **oder** ble2mqtt Central-Log; sonst nRF |
| Soundbar | A2DP-Sink Endpoint + Phone HCI snoop |
| Auto | HFP-HF + A2DP-Sink Endpoint + HCI snoop |
| HID Legacy-PC | Cross-Transport / HID Endpoint |
| Encrypted unknown | Host-Sniffer zuerst |

**Regel:** Relais nur wo transparent möglich; sonst Endpoint + Host-Sniffer.

## Lessons → Transfer

- Analyse ≠ Produktions-Bridge: Observe-Proxy und Endpoint haben getrennte Sheets.
- MQTT-Central-Gateway ist Analyse-Sink, kein Phone↔Device-MITM.
- Encryption/Classic-Audio: Host-Sniffer + Endpoint statt Universal-Relais.
- Geräteklasse steuert Tooling — nicht „noch ein ble-relay“.

## Bezug

[INVENTORY](../../projects/bt-analysis-relay-refs/INVENTORY.md) · [evidence](evidence.md) · [method](../../methods/bt-passive-host-sniff.md) · Prior: [`ble-gatt-bridge-refs-2026-foreign`](../ble-gatt-bridge-refs-2026-foreign/) · [`bt-classic-gaps-2026-foreign`](../bt-classic-gaps-2026-foreign/)
