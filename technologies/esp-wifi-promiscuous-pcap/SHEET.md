# Technology Sheet: ESP WiFi Promiscuous + PCAP

```yaml
slug: esp-wifi-promiscuous-pcap
title: ESP WiFi Promiscuous Sniff + PCAP Capture
primary: H
tags: [esp-idf, arduino, lab-only, fragile]
type: pattern
status: active
seen_in: [esp32-marauder]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/esp32-marauder-2026-foreign
```

Nur Ebene **A**. Board-Pins, Menü-CLI, Produktnamen → Application.  
**Policy:** Sheet beschreibt **Capture-/Analyse-Pipeline** (Promiscuous → Buffer → PCAP). Keine Anleitung für unautorisierte Stör-/Angriffssender.

## Kurzfassung

ESP32-Familie im **WiFi-Promiscuous-Modus**: Management-/Data-Frames per Callback empfangen, oft in einen **Double-Buffer** legen und als **PCAP** (SD/Serial) persistieren. Hohe Paketraten erzwingen RAM-Budget (`BUF_SIZE`/`SNAP_LEN`) und kritische Abschnitte zwischen Callback und Flush.

## Abgrenzung

- **Ist:** Promiscuous RX, Filter-Masken, Packet-Monitor/Rate, PCAP-Header/Records, Double-Buffer→FS.
- **Ist nicht:** Periodischer AP/BLE-**Environment-Score** (`rf-environment-monitor`); Wi-Fi-**CSI-Motion** (`wifi-csi-motion`); LAN-Port-Inventur (`lan-device-inventory`); GATT-Central (`ble-hrm-gatt`); Angriffs-TX-Rezepte.
- **Grenzt an:** ESP-IDF `esp_wifi` Promiscuous API; SD/FS; optional GPS/Wigle-Export (App).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | `esp_wifi_set_promiscuous` + RX-Callback | oft MGMT\|DATA Filter |
| lateral | Double-Buffer + `portMUX` / Critical | Callback vs. Flush |
| oben | PCAP-Datei / Serial / UI Packet-Count | Analyse off-device |
| parallel | BLE Adv-Scan | shared radio → sequentiell planen |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Promiscuous-Sniff ≡ RF-Environment-Monitor | `REJECTED` | anderer Contract (Frames vs. Score-Scan) |
| Promiscuous-Sniff ≡ CSI-Motion-Sensing | `REJECTED` | Frame-Dump ≠ Subcarrier-Amplituden-Detektor (`wifi-csi-motion`) |
| Unbegrenzte Capture-Rate ohne Drop | `REJECTED` | Buffer voll → Drop; Budget messen |
| Double-Buffer = immer `xTaskCreatePinnedToCore` | `REJECTED` | Concurrency oft Callback↔Loop + Mux; Worker separat prüfen |
| Classic / S3 / C5 gleiche Kanal-/Band-Fähigkeit | `REJECTED` | Dual-Band (5 GHz) Chip-Gate (z. B. C5) |
| WLAN+BLE Sniff parallel ohne Qualitätseinbuße | `HYPOTHESIS` | shared radio |
| Sheet deckt Deauth/Beacon-Spam ab | `REJECTED` | Offensive TX ≠ dieses Capture-Muster; kein How-to hier |

### Projektstart-Checkliste

- [ ] Chip-Familie + Band (2.4 only vs Dual-Band)
- [ ] `BUF_SIZE` / `SNAP_LEN` vs. RAM/PSRAM
- [ ] PCAP-Ziel: SD vs Serial; Flush-Pfad unter Last
- [ ] Filter-Maske (MGMT/DATA) dokumentieren
- [ ] BLE parallel? → Zeitbudget
- [ ] Application + `seen_in`; keine Attack-A

## Transfer

Nützlich für Lab-Capture, Wardrive-PCAP, Packet-Rate-Monitore. Nicht still auf Hub-RF-Score-Nodes oder Offensive-TX übertragen.

## Referenzen

- ESP-IDF WiFi Sniffer / Promiscuous
- PCAP Global Header (libpcap-kompatibel)
- Pilot: [ESP32Marauder](https://github.com/justcallmekoko/ESP32Marauder) (`Buffer`, `PcapHeader`, `WiFiScan`)

## Offene Fragen

- Welche Drop-Raten typisch bei 8 KiB×2 ohne PSRAM?
- C5 Dual-Band Channel-Walk vs. Classic 1–13 Budget?
