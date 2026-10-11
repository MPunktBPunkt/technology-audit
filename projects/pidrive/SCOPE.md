# Project Scope: PiDrive

```yaml
project_id: pidrive
title: PiDrive
updated: 2026-10-11
reviewed_commit: b61df4d
reviewed_commit_note: Radio/BT-Vertiefung gegen pidrive@b61df4d; MSC/HU-Evidence weiter multi-Artefakt (docs/betrieb)
repos:
  - https://github.com/MPunktBPunkt/pidrive
  - https://github.com/MPunktBPunkt/esp32.pidrive
status: active
profile_hint: ops-field
```

## Zweck

Infotainment-Stack (Quellen, Audio, Steuerung, Metadaten) für den Betrieb an BMW iDrive (u. a. NBT Evo), inkl. ESP32-Pfaden (USB-MSC-Medienquelle, perspektivisch BT-Gateway).

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| Raspberry Pi / PiDrive-Userspace | Quellen, Routing, Trigger, UI | ja |
| ESP32 (`esp32.pidrive`) | MSC-Bridge / Gerätepfad zur HU | ja |
| BMW NBT Evo (USB/BT-Host) | Verhalten als Host/Sink | ja (beobachtend) |
| BlueZ / A2DP / AVRCP auf dem Pi | bestehender BT-Pfad | ja |
| esp32.bt-gateway (Planung) | ausgelagerte BT-Hardware | angrenzend (Transfer) |
| Fahrzeug-CAN / Diagnose | — | nein |

## Nicht-Ziele

- Vollständige Kopie der Betriebs-/Feldberichte aus `pidrive`/`docs/betrieb`
- Reverse Engineering fremder Firmware jenseits des eigenen Stacks
- Produktisierung / Serienreife

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code Pi | `pidrive/`, `systemd/`, `pipewire-config/` | Upstream-Repo |
| Firmware ESP | `esp32.pidrive` | separates Repo |
| Betrieb / Feld | `docs/betrieb/` in pidrive | Artefakte verlinken, nicht spiegeln |
| Planung BT-Gateway | `esp32.bt-gateway` | Transfer-Kandidat |

## Prioritäten für die Analyse

1. USB-MSC / SCSI / FAT / LBA und HU-Leseverhalten  
2. Empfang/Funk: DAB+, RTL-SDR, PMR446, Airband, Spektrum-FFT (`pidrive-2026-radio-bt`)  
3. Audio-Pipeline und Bluetooth (A2DP/AVRCP) — Pi BlueZ vs. ESP-Gateway  
4. Metadaten (MPRIS) und Systemintegration (systemd, Trigger, ESP↔Pi)

## Offene Scope-Fragen

- Wie weit `esp32.bt-gateway` als eigenes Projekt vs. PiDrive-Application geführt wird
- Ob Lab-only-Tools als Methods oder als Tech-Sheets erfasst werden
