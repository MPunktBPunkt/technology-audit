# Project Scope: hu-probe

```yaml
project_id: hu-probe
title: hu-probe — ESP32-S3 USB-MSC Head-Unit Messsonde
updated: 2026-10-15
profile_hint: lab-tool
status: active
repos:
  - /home/martin/projects/hu-probe
```

## Zweck

Audit-Kontext für die eigene USB-MSC-Messsonde (ESP32-S3, Arduino/PlatformIO):
Instrumentierung, Capture-Pfad, **USB↔WiFi-Coexistenz unter Host-Last**, und
**S1–S3 Host-Read-Semantik** (Messplan, keine stillen PiDrive-FACTs).
Dieses Repo (`technology-audit`) speichert Desk-Wissen und Kampagnen — nicht den
Firmware-Quellbaum.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP32-S3 OTG Device MSC | TinyUSB Bulk, Demo-FAT | ja (Desk + Lab-Pläne) |
| WiFi STA + TCP JSONL Collector | Telemetrie-Pfad | ja |
| Stack-Pin PlatformIO/Arduino | Defaults Task/PHY | ja |
| Fremd: esp-idf / esp-usb / arduino-esp32 | Coex-Evidence | ja, Desk |
| BMW NBT / Mazda HU | Host-Verhalten | S1–S3-Messplan ja; Zahlen nur aus Sessions; kein Wire; kein Mazda-Default |
| Root-Cause WiFi-Death | — | **nein** als Desk-FACT (eigene Coex-Kampagne) |
| Fix-Implementierung in FW | — | **nein** (Desk-Audits) |

## Nicht-Ziele

- „USB-Bulk verursacht WiFi-Tod“ als FACT aus Repos ableiten
- IDF-Issue = Sonde-Ursache
- PiDrive-Zahlen als hu-probe-`FACT` / Linux-Read-Ahead als NBT-Prefetch
- Capture-Flush-Architektur ersetzen

## Quellen für das Audit

| Quelle | Snapshot / Pin | Bemerkung |
|--------|----------------|-----------|
| Lokal hu-probe | FW 0.2.15 · `espressif32@6.4.0` | Pin + Symptom-Kontext |
| espressif/esp-idf | Issues + `ab95e707…` / v4.4.5 | PHY/WiFi/USB |
| espressif/esp-usb | `c40b86d…` Device | TinyUSB-Task-API (Kontrast) |
| Arduino-ESP32 2.0.11 | Tag + PIO package `3.20011.230801` | hu-probe-Pfad |
| esp-faq / esp-iot-solution | pinned SHAs | Abgrenzung / Existenz |

## Prioritäten für die Analyse

1. Coex-unter-Last-Karte (Task/Core/Prio + PHY) — Desk erledigt
2. S1–S3 Host-Read-Semantik — Messplan erledigt; Feld offen
3. Diskriminierungs-Messplan Power vs. Starve vs. RF — Lab offen
4. Keine Ursachenbehauptung / keine PiDrive→hu-probe-FACT-Übernahme

## Offene Scope-Fragen

- Gehört ein vollständiges hu-probe Firmware-Pilot-Audit (GATE-01) in dieselbe
  Projekt-ID? (vorerst: Coex + S1–S3-Kampagnen + Verweis auf Lokal-Docs)
