# Project Scope: esp32-marauder (Fremd)

```yaml
project_id: esp32-marauder
title: ESP32 Marauder — WiFi/BLE Lab Toolkit (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "9386f3c0348c171eb58ef2e1ce1f0c2f555ba30c"
repos:
  - https://github.com/justcallmekoko/ESP32Marauder
status: active
```

## Zweck

Fremdrepo als Desk-Quelle für **ESP WiFi-Promiscuous-Capture + PCAP** (hohe Paketraten, Double-Buffer→SD), BLE-Scan-Nebenrolle und Chip-/Board-Matrix (Classic / S3 / C5 Dual-Band). Wissen in wiederverwendbare Sheets überführen.

**Rechtlicher Rahmen (Audit):** Nur dokumentieren, was für Lab-/Defensive-Analyse und Hardware-Limits relevant ist. Keine Anleitungen für unautorisierte Angriffe auf fremde Netze.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `WiFiScan` + Promiscuous-Callbacks | Sniff / Monitor / Packet-Rate | ja (Desk, Architektur) |
| `Buffer` + `PcapHeader` + SD | PCAP-Double-Buffer | ja |
| NimBLE Scan (`HAS_BT`) | BLE Adv-Scan / Listen | ja (Kontrast zu GATT-Sheets) |
| Board-`configs.h` Matrix | Chip-/Feature-Gates | ja |
| Offensive TX-Modi (Deauth, Beacon Spam, …) | Produkt-Feature-Signale | **nur Inventar-Name**, kein Sheet/How-to |
| Evil Portal / Credential UX | — | **nein** (kein KB-Inhalt) |
| Eigene Feldangriffe / Remessung pps | — | FOLLOW-ON Lab (authorized only) |

## Nicht-Ziele

- Angriffsverfahren, Payloads, Timing-Rezepte oder „wie Deauth senden“
- Evil-Portal / Captive-Phishing-Inhalte spiegeln
- Marauder als Ersatz für `rf-environment-monitor` (Scan-Score ≠ Packet-Sniff)
- Alle Board-Targets 1:1 als eigene Sheets

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code | https://github.com/justcallmekoko/ESP32Marauder @ `9386f3c` | Fremd, Desk |
| Wiki | https://github.com/justcallmekoko/ESP32Marauder/wiki | sekundär; nicht spiegeln |
| Version | `configs.h` `MARAUDER_VERSION` | `v1.19.2` |

## Prioritäten für die Analyse

1. Neues Sheet `esp-wifi-promiscuous-pcap` (A) + Application
2. Kontrast-Reuse: `rf-environment-monitor`, `lan-device-inventory` (Abgrenzung)
3. Offensive TX nur als observed Signals ohne Sheet
4. Chip-Gate Classic ≠ S3 ≠ C5 Dual-Band

## Offene Scope-Fragen

- „Dual-Core“ (Community) vs. belegtem Double-Buffer/`portMUX` — separates Lab?
- Dual-Band-C5: eigenes Sheet später oder nur Chip-Gate in diesem Sheet?
