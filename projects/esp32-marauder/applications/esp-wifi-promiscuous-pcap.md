# Project Application: esp-wifi-promiscuous-pcap in esp32-marauder

```yaml
project_id: esp32-marauder
tech_slug: esp-wifi-promiscuous-pcap
status: active
sheet: ../../../technologies/esp-wifi-promiscuous-pcap/SHEET.md
audit: ../../../audits/esp32-marauder-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt

Kern der **defensiven/analytischen** Marauder-Seite: Promiscuous-Sniff-Modi, Packet-Monitor/Rate, Raw-Capture → Double-Buffer → PCAP auf SD/Serial. CLI u. a. `sniffraw`, `sniffbeacon`, `packetcount`, `wardrive`.

| Repo | Commit | Rolle |
|------|--------|-------|
| [justcallmekoko/ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder) | `9386f3c` | Firmware `esp32_marauder/` · Tag im Code `v1.19.2` |

## Architektur / Datenfluss

```text
esp_wifi promiscuous RX callback
  → filter (MGMT|DATA typisch)
  → Buffer.append(wifi_promiscuous_pkt_t)
       bufA|bufB + portMUX
  → PCAP global/record header
  → SD / Serial flush (save)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `esp32_marauder/WiFiScan.cpp` / `.h` | Modi, `esp_wifi_set_promiscuous`, Callbacks |
| `esp32_marauder/Buffer.cpp` / `.h` | Double-Buffer, PCAP append/save |
| `esp32_marauder/PcapHeader.*` | Global Header Builder |
| `esp32_marauder/SDInterface.*` | SD Persistenz |
| `esp32_marauder/configs.h` | `BUF_SIZE`/`SNAP_LEN`, Boards, `DUAL_BAND_CHANNELS` |
| `esp32_marauder/CommandLine.h` | Sniff-CLI-Namen (Desk-Signal) |

## Konfiguration und Parameter

| Parameter | Upstream (Desk) | Status |
|-----------|-----------------|--------|
| Version | `MARAUDER_VERSION` `v1.19.2` | `FACT` |
| PSRAM-Profil | `BUF_SIZE` 8 KiB, `SNAP_LEN` 4096 | `FACT` |
| Default (kein PSRAM) | `BUF_SIZE` 3 KiB, `SNAP_LEN` 2324 | `FACT` |
| Low-RAM Profil | 2 KiB / 1514 | `FACT` |
| Dual-Band Kanäle | `DUAL_BAND_CHANNELS` 51 | `FACT` |
| Filter (Header) | MGMT \| DATA Mask | `FACT` |
| Concurrency | `portMUX` Double-Buffer; kein `xTaskCreatePinnedToCore` im Desk-Scan | `FACT` / `UNKNOWN` für „Dual-Core-Worker“ |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Suite WiFi/BT offensive+defensive Tools (README) | `EVID-MARAUDER-2026-10-25-001` | `FACT` |
| Promiscuous + diverse Sniff-Callbacks + Packet-Rate-Mode | `EVID-MARAUDER-2026-10-25-002` | `FACT` |
| PCAP Double-Buffer → SD/Serial | `EVID-MARAUDER-2026-10-25-003` | `FACT` |
| Dual-Band Channel-Index (C5-Klasse) ≠ pinned Dual-Core-LLM-Muster | `EVID-MARAUDER-2026-10-25-004` | `FACT` |
| Offensive TX-Modi existieren als Produkt-Signale | `EVID-MARAUDER-2026-10-25-005` | `FACT` (Existenz only) |
| Eigene pps/Drop Lab-Zahlen | — | `UNKNOWN` |

## Abweichungen / Policy

Offensive TX und Evil-Portal werden **nicht** als Application-How-to vertieft — nur Existenz-Evidence für Inventar-Transparenz.

## Offene Fragen

- Drop-Verhalten wenn beide Buffer voll (authorized Lab)?
