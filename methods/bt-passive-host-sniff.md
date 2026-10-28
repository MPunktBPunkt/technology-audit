# Method: BT Passive Host Sniff (nRF / HCI snoop)

```yaml
slug: bt-passive-host-sniff
title: BT Passive Host Sniff (nRF Sniffer / HCI snoop)
status: active
tags: [tracing, bluetooth, analysis]
```

## Zweck

Passiv erfassen, was Telefon↔Peripherie austauschen, **ohne** ESP im Datenpfad — besonders wenn Bonding/Encryption Transparent-Relais blockiert oder Classic-Audio beobachtet werden soll.

## Voraussetzungen

- **Android HCI snoop:** Entwickleroptionen → Bluetooth HCI snoop log; Bugreport/`btsnoop_hci.log` → Wireshark
- **nRF Sniffer:** nRF52 Dongle + Wireshark Plugin; BLE Adv/Data (mit Limits bei Encryption)
- Optional: Linux `btmon` / BlueZ Monitor am Host-Adapter
- Kein Anspruch auf Entschlüsselung fremder Bonds ohne Keys

## Ablauf

1. Geräteklasse und Frage festlegen (GATT UUID? HFP AT? A2DP Metadata?).
2. **Passiv** capturen (Phone snoop und/oder nRF), Zeitstempel notieren.
3. Parallel optional ESP-**Endpoint** oder Observe-Proxy — Captures korrelieren, nicht vermischen.
4. In Wireshark Filter nach ATT/RFCOMM/AVDTP/AVCTP setzen; Evidence-IDs nur für belegte Frames.
5. Encryption: wenn ATT encrypted und Keys fehlen → Endpoint-Re-Pair oder Analyse stoppen (`UNKNOWN`).

## Artefakte

| Artefakt | Naming |
|----------|--------|
| `btsnoop_hci.log` / pcapng | `YYYY-MM-DD-<device>-hci.pcapng` |
| Notiz Bonding/Keys | Session-YAML: bonded=yes/no, role |
| Korrelation ESP-UART | gleiche Session-ID |

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Frage beantwortbar aus Capture | relevante PDUs sichtbar | nur leere Adv / encrypted ohne Key |
| Epistemik | Desk/Lab getrennt | ESP-Log als „Phone↔Original“ verkauft |

## Fallstricke

- nRF sieht nicht alles unter Encryption; HCI snoop ist **Phone-seitig**, nicht magisch Full-MITM.
- A2DP-Medieninhalt ≠ Metadata/AVRCP-Steuerung — getrennt auswerten.
- Bettercap/GATTacker: Host-MITM-Kontrast — keine Attack-How-tos in der KB.

## Beispiel-Einsätze

- Soundbar: Phone HCI snoop + ESP A2DP-Sink Endpoint (`bt-analysis-endpoint`)
- Uhr: nRF + optional `ble-gatt-observe-proxy` nach Re-Pair
- Auto: HCI snoop für HFP AT; ESP als HF-Endpoint zum Nachstellen

## Abgrenzung Capture-Pipelines

| Pfad | Sicht | Wann |
|------|-------|------|
| **nRF OTA** (diese Method) | Link-Layer / Adv / ggf. Follow | fremde Connection, keine ESP-Rolle |
| **HCI snoop** (Phone/BlueZ) | Stack am Endgerät | Encryption oft lesbar am Phone |
| **ESP Endpoint Event Stream** | App-Events (GATT/HFP/AVRCP) | ESP ist Gerät; → Sheet `bt-endpoint-event-stream` |
| **ESP Dual-Role Observe** | Phone↔Sensor Proxy | nur wenn transparent/pairbar |

**Regel:** ESP fängt auf Anwendungsebene; nRF/HCI für Funk- bzw. Stack-Sicht; Debian wertet aus (JSONL oder PCAP).

## Verwandt

- Sheets: `ble-gatt-observe-proxy`, `bt-analysis-endpoint`, `bt-endpoint-event-stream`, `bluetooth-hfp`, `bluetooth-a2dp`
- Kampagnen: `bt-analysis-relay-2026-foreign`, `bt-sniffing-capture-2026-foreign`
