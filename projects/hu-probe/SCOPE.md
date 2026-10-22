# Project Scope: hu-probe

```yaml
project_id: hu-probe
title: hu-probe — ESP32-S3 USB-MSC Head-Unit Messsonde
updated: 2026-10-22
profile_hint: lab-tool
status: active
repos:
  - /home/martin/projects/hu-probe
reviewed_commit: "8234982"
fw_pin: "0.3.17"
```

## Zweck

Audit-Kontext für die eigene USB-MSC-Messsonde (ESP32-S3, Arduino/PlatformIO):
Instrumentierung, Capture-Pfad, **USB↔WiFi-Coexistenz unter Host-Last**, und
**Host-Read-Semantik** (Transport S0/S2, free Offline Grammar, Media-Leiter Phasen).
Dieses Repo (`technology-audit`) speichert Desk-/Feldwissen und Kampagnen — nicht den
Firmware-Quellbaum.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP32-S3 OTG Device MSC | TinyUSB Bulk, Demo-FAT / SynthFat | ja (Desk + Lab + Feld) |
| YD-ESP32-S3 Board (N8R2, Dual-USB-C) | Hardware-Pin, PSRAM, Versorgung | ja |
| WiFi STA + TCP JSONL Collector | Telemetrie-Pfad | ja |
| RAM/PSRAM Offline-Capture (+ TripStore 0.3.x) | WIFI_OFF → Replay / Drive-Home | ja (Instrument); Lab Replay B50 offen |
| Stack-Pin PlatformIO/Arduino | Defaults Task/PHY / PSRAM Flags | ja |
| Fremd: esp-idf / esp-usb / arduino-esp32 | Coex-Evidence | ja, Desk |
| BMW NBT / Mazda HU | Host-Verhalten | Transport + free + Media-Leiter Phasen ja; A8/Cache-Key nur nach Formal; kein Wire; kein Mazda-Default |
| Root-Cause WiFi-Death | — | **nein** als Desk-FACT (eigene Coex-Kampagne; PSRAM ≠ Heilung) |
| Fix-Implementierung in FW | — | **nein** (Desk-Audits) |
| Upstream-Profil-Edit | `bmw_nbt_evo.json` | beobachtet / zitiert; Edit liegt im Quellrepo |

## Nicht-Ziele

- „USB-Bulk verursacht WiFi-Tod“ als FACT aus Repos ableiten
- IDF-Issue = Sonde-Ursache
- PiDrive-Zahlen als hu-probe-Semantik-`FACT` / Linux-Read-Ahead als NBT-Prefetch
- Gap/4096 blind als HU-Scheduler-Pace
- Burst-39 / Prefetch~15 s / Prefetch~8 s als Profil-Konstante ohne Formal
- „Nur Ordnerstruktur“ als Host-FACT
- Capture-Flush-Architektur ersetzen
- HARDWARE.md Upstream-Edit in diesem Repo

## Quellen für das Audit

| Quelle | Snapshot / Pin | Bemerkung |
|--------|----------------|-----------|
| Lokal hu-probe | **`8234982`** · FW **0.3.17**; Media-Leiter + Trip-Replay | Sessions + `docs/feld/` + `profiles/` |
| Prior Pin | `f985459` · FW 0.3.1 / free 0.2.40 | PSRAM/Board/free Grammar |
| Board-Doku | `docs/HARDWARE-YD-ESP32-S3.md` | Foto/Pinout; §2.3 PSRAM-Text driftet |
| espressif/esp-idf | Issues + Pins | PHY/WiFi/USB |
| Arduino-ESP32 2.0.11 | PIO `espressif32@6.4.0` | hu-probe-Pfad |

## Prioritäten für die Analyse

1. Coex-unter-Last-Karte — Desk erledigt; Lab Recovery 0.2.37–39 PASS; Root-Cause offen
2. S1–S3 + Transport S0/S2 + CBW-Atom 240+69 — erledigt
3. free Offline Grammar demo_v1 — **erledigt 2026-10-20/21**
4. PSRAM/Board — **erledigt 2026-10-21** (Doc-Drift FOLLOW-ON)
5. Media-Leiter Head/Tail/Bulk/Elevator/PiDrive-Vertrag — **erledigt 2026-10-22**
6. Trip-Replay 0.3.17 Upload — **erledigt**; Lab B50 / A8 formal / audible — **offen**

## Offene Scope-Fragen

- Gehört Drive-Mode/TripStore als eigener Pilot-Slug, oder bleibt er unter `usb-msc` Instrument?
