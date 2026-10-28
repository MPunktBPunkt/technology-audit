# Audit Campaign: bt-sniffing-capture-2026-foreign

```yaml
id: bt-sniffing-capture-2026-foreign
project_id: bt-sniffing-capture-refs
started: 2026-10-28
ended: 2026-10-28
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "multi-2026-10-28"
upstream_pins:
  esp32-ble-scan-mqtt: "ee096de"
  BLESniffer: "1bea2e8"
  esp32_bluetooth_classic_sniffer: "0e174ca"
  bsniffhub: "29049d7"
  esp32-ble2mqtt: "e66ec5a"
  ChimeraBLE: "2330423"
  a2dpSinkHfpClient: "df6c5f4"
reuse_outcomes:
  reused:
    - bt-analysis-endpoint
    - ble-gatt-observe-proxy
    - bt-passive-host-sniff
    - bluetooth-hfp
    - bluetooth-a2dp
  new:
    - bt-endpoint-event-stream
  not_helped:
    - "ESP als nRF-Connection-Follower"
    - "Eidolon als HFP-TCP-Vorbild (nicht gefunden)"
    - "PCAP als Default für App-Events"
  process: "Desk Capture-Pipelines; JSONL/TCP priorisiert; OTA vs Endpoint vs HCI getrennt."
  decisions_touched:
    - fact-jsonl-over-pcap-for-app-events
    - fact-mqtt-queues-need-drop-counters
    - reject-esp-ota-follow
    - fact-device-class-capture-path
```

## Ziel

ESP fängt auf **Anwendungsebene**, streamt Events (TCP/JSONL) an Debian; nRF/HCI für Funk-/Stack-Sicht. Geräteklassenbezogene Capture-Pfade.

## Scope

[SCOPE](../../projects/bt-sniffing-capture-refs/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + multi-pin | erfüllt |
| 2 | Capture-Muster-Matrix + Transport-Eignung | erfüllt |
| 3 | Sheet `bt-endpoint-event-stream` + JSONL-Schema v0 | erfüllt |
| 4 | Method Host-Sniff Pipeline-Vergleich | erfüllt |
| 5 | Geräteklasse → Capture-Pfad | erfüllt |
| 6 | C10–C12 + Lessons | erfüllt |
| 7 | `ta-assist check` 0 errors | erfüllt |
| 8 | Lab ESP→TCP→Debian Capture | FOLLOW-ON |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Event-Stream Sheet | Endpoint-Sheet genug? | scan-mqtt Queues | Neu Primary H | DISCOVERED |
| JSONL > PCAP für App | Wireshark Pflicht? | BLESniffer synth | PCAP optional | DISCOVERED |
| ESP ≠ nRF Follow | OTA Follow auf ESP? | bsniffhub/nRF | `REJECTED` | KNOWN BEFORE |
| Eidolon | HFP TCP Repo? | Search | UNKNOWN / absent | DISCOVERED |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-001` | Drop/Seq bei Queue-Export |
| `…-020` | Synth-PCAP nicht als RF-Truth |
| `…-030` | Classic active sniffer ≠ Endpoint-JSONL |
| Schema | `layer`/`op` pro Geräteklasse |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Generisches ble-sniffer Sheet ohne Transport | `REJECTED` |
| 2 | ESP-OTA-Follow als Empfehlung | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk schließt Pipeline-Wahl; Lab-TCP-Capture FOLLOW-ON.
```

## Regel

**ESP = Application-Level Capture → Event-Stream; nRF = Passive OTA; HCI-Snoop = Stack am Phone/Host; Debian wertet aus.**

| Klasse | Pfad |
|--------|------|
| Uhr/Sensor | Endpoint/Central + TCP JSONL \| HCI \| nRF |
| Soundbar | A2DP-Sink Events TCP \| HCI |
| Auto | HFP-HF Events TCP \| HCI |
| Encrypted fremd | Host-Sniffer zuerst |

## Lessons → Transfer

- scan-mqtt liefert Queue/Drop/JSON-Muster für TCP-JSONL-Port.
- PCAP-Pipelines (BLESniffer/BrakTooth/bsniffhub) sind Kontrast, nicht Default für App-Events.
- a2dpSink zeigt Endpoint-Logs — TCP-Export noch bauen (FOLLOW-ON).

## Bezug

[INVENTORY](../../projects/bt-sniffing-capture-refs/INVENTORY.md) · [evidence](evidence.md) · Prior: [`bt-analysis-relay-2026-foreign`](../bt-analysis-relay-2026-foreign/) · [`bt-classic-gaps-2026-foreign`](../bt-classic-gaps-2026-foreign/)
