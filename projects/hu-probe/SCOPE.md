# Project Scope: hu-probe

```yaml
project_id: hu-probe
title: hu-probe — ESP32-S3 USB-MSC Head-Unit Messsonde
updated: 2026-10-21
profile_hint: lab-tool
status: active
repos:
  - /home/martin/projects/hu-probe
reviewed_commit: "f985459"
fw_pin: "0.3.1"
```

## Zweck

Audit-Kontext für die eigene USB-MSC-Messsonde (ESP32-S3, Arduino/PlatformIO):
Instrumentierung, Capture-Pfad, **USB↔WiFi-Coexistenz unter Host-Last**, und
**Host-Read-Semantik** (Messplan + Feld-Transport S0/S2 + free Offline Grammar).
Dieses Repo (`technology-audit`) speichert Desk-/Feldwissen und Kampagnen — nicht den
Firmware-Quellbaum.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP32-S3 OTG Device MSC | TinyUSB Bulk, Demo-FAT / SynthFat | ja (Desk + Lab + Feld) |
| YD-ESP32-S3 Board (N8R2, Dual-USB-C) | Hardware-Pin, PSRAM, Versorgung | ja |
| WiFi STA + TCP JSONL Collector | Telemetrie-Pfad | ja |
| RAM/PSRAM Offline-Capture (+ TripStore 0.3.x) | WIFI_OFF → Replay / Drive-Home | ja (Instrument); Drive-Home Census offen |
| Stack-Pin PlatformIO/Arduino | Defaults Task/PHY / PSRAM Flags | ja |
| Fremd: esp-idf / esp-usb / arduino-esp32 | Coex-Evidence | ja, Desk |
| BMW NBT / Mazda HU | Host-Verhalten | Transport + demo_v1 free Grammar ja; Prefetch große Dateien / Cache-Key nur nach Formal; kein Wire; kein Mazda-Default |
| Root-Cause WiFi-Death | — | **nein** als Desk-FACT (eigene Coex-Kampagne; PSRAM ≠ Heilung) |
| Fix-Implementierung in FW | — | **nein** (Desk-Audits) |
| Upstream-Profil-Edit | `bmw_nbt_evo.json` | beobachtet / zitiert; Edit liegt im Quellrepo |

## Nicht-Ziele

- „USB-Bulk verursacht WiFi-Tod“ als FACT aus Repos ableiten
- IDF-Issue = Sonde-Ursache
- PiDrive-Zahlen als hu-probe-Semantik-`FACT` / Linux-Read-Ahead als NBT-Prefetch
- Gap/4096 blind als HU-Scheduler-Pace
- Burst-39 / Prefetch~15 s als Profil-Konstante ohne Formal (15 s auf demo_v1 **REJECTED**)
- Capture-Flush-Architektur ersetzen
- HARDWARE.md Upstream-Edit in diesem Repo

## Quellen für das Audit

| Quelle | Snapshot / Pin | Bemerkung |
|--------|----------------|-----------|
| Lokal hu-probe | **`f985459`** · FW **0.3.1**; Feldkern free **0.2.40** | Sessions + `docs/feld/` + `profiles/` |
| Board-Doku | `docs/HARDWARE-YD-ESP32-S3.md` | Foto/Pinout; §2.3 PSRAM-Text driftet |
| espressif/esp-idf | Issues + Pins | PHY/WiFi/USB |
| Arduino-ESP32 2.0.11 | PIO `espressif32@6.4.0` | hu-probe-Pfad |

## Prioritäten für die Analyse

1. Coex-unter-Last-Karte — Desk erledigt; Lab Recovery 0.2.37–39 PASS; Root-Cause offen
2. S1–S3 + Transport S0/S2 + CBW-Atom 240+69 — erledigt
3. free Offline Grammar demo_v1 — **erledigt 2026-10-20/21**
4. PSRAM/Board — **erledigt 2026-10-21** (Doc-Drift FOLLOW-ON)
5. Größenleiter / Elevator-Test / audible — **offen**
6. Drive-Home 0.3.x Integrity — **offen**

## Offene Scope-Fragen

- Gehört Drive-Mode/TripStore als eigener Pilot-Slug, oder bleibt er unter `usb-msc` Instrument?
