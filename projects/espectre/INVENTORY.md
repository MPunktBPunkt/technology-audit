# Project Inventory: espectre (Fremd)

```yaml
project_id: espectre
updated: 2026-10-25
reviewed_commit: "5866bff6aa3a8ac41ed70d2476c115ea6285b277"
profile: lab-tool
pilot_order: [wifi-csi-motion, esp-wifi-promiscuous-pcap, rf-environment-monitor, mqtt-node-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Wi-Fi CSI Amplitudes → Motion / Score, on-device | `wifi-csi-motion` | **neu** + App |
| Temporal admission @ `csi_target_pps` (default 100) | `wifi-csi-motion` | A-Fallstrick |
| Lightweight vs High-Accuracy (MLP) Detectors | `wifi-csi-motion` | A + App |
| Managed CSI traffic (ping/dns/wifi_raw/external) | `wifi-csi-motion` | A (Traffic ≠ Sniff) |
| Promiscuous PCAP / Frame dump | `esp-wifi-promiscuous-pcap` | **Kontrast** |
| AP/BLE Environment-Score | `rf-environment-monitor` | **Kontrast** |
| MQTT / HA Discovery (Native) | `mqtt-node-telemetry` | observed / partial |
| Direct HTTP + SSE | `esp-embedded-web-sse` | observed / partial |
| Marauder CSI Motion modules | `wifi-csi-motion` | Kontrast (Marauder Inventar) |
| On-device LLM / PLE | `mcu-ple-inference` | **≠** — anderes ML |

Kampagne: [`espectre-2026-foreign`](../../audits/espectre-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `wifi-csi-motion` | Wi-Fi CSI Motion Sensing | H | applied | partial | [SHEET](../../technologies/wifi-csi-motion/SHEET.md) | [app](applications/wifi-csi-motion.md) |
| `esp-wifi-promiscuous-pcap` | Promiscuous + PCAP | H | observed | none | [SHEET](../../technologies/esp-wifi-promiscuous-pcap/SHEET.md) | — (Kontrast) |
| `rf-environment-monitor` | RF Environment Monitor | H | observed | none | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | — (Kontrast) |
| `mqtt-node-telemetry` | MQTT Node Telemetry | F | observed | none | [SHEET](../../technologies/mqtt-node-telemetry/SHEET.md) | — |
| `esp-embedded-web-sse` | Embedded Web REST + SSE | G | observed | none | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Eigene Raum-Lab-Messung | Desk only | FOLLOW-ON authorized |
| Matter Controller Matrix | Upstream limited | observed |
| Marauder CSI Code-Tiefe | nur Signal | optional App-Kontrast |

## Signale ohne Eintrag

- Browser Flash Tooling / docs/web — Ops UX
- Dataset NPZ Corpus — Research, nicht spiegeln
- MicroPython CSI Mainline-PR — angrenzend, Link only
