# Technology Sheet: rpitx (Raspberry Pi Software RF TX)

```yaml
slug: rpitx
title: rpitx — Raspberry Pi Software RF Transmit Platform
primary: D
tags: [radio-tx, lab-only, fragile, linux-userspace]
type: implementation
status: active
seen_in: [pi-fm-tx]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/pi-fm-tx-2026-foreign
```

Nur Ebene **A**. Einzelne Modi/Scripts → Application.  
**Recht:** Bildungs-/Experiment-Software; keine Compliance-Tests; Filter/Lizenz lokal klären — KB beschreibt Technik, nicht Sendebetrieb.  
**Chip-Scope:** Claims (Bandbreite, GPIO4, Mode-Demos, Pi4‑beta) gelten für die **von Upstream dokumentierte Pi-Matrix** (BCM-SoC-Generationen). **Pi 5 / RP1:** nicht belegt — `UNKNOWN` bis Gate; kein Sheet-Ausweiten (G19).

## Kurzfassung

**rpitx** (F5OEO): allgemeine Software-RF-Sendeplattform auf dem Raspberry Pi (laut Upstream ca. **5 kHz–1500 MHz**), GPIO‑Draht als Strahler, oft **Filter** nötig. Bündelt Carrier/Chirp/Spektrum, FM+RDS, SSB, SSTV, POCSAG, FreeDV, FT8, … über **librpitx** und Hilfsprogramme — breiter als reines UKW‑FM (`rpi-gpio-fm-tx`).

## Abgrenzung

- **Ist:** Multi-Mode-TX-Stack inkl. Install/Boot-Tuning (`gpu_freq` o. Ä.) auf belegter Pi-Matrix.
- **Ist nicht:** Nur-UKW-WAV-Player (`rpi-gpio-fm-tx`); RDS-Protokoll allein (`fm-rds`); SDR-**Empfang** (`rtl-sdr`); Pi5/RP1-Port ohne Evidence; legale Amateurfunk-Station ohne Filter/Lizenz.

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Mode-Tools / Menüs / IQ (`sendiq`) | viele Demo-Scripts |
| unten | librpitx + GPIO4 Clock/RF | Pi‑Modell-Matrix; Pi4 „beta“ |
| lateral | optional rtl-sdr zum Monitor | Empfang ≠ Teil des TX-Contracts |
| lateral | `/boot/config.txt` | Install fordert stabile GPU-Clock |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Ohne Filter „nur UKW-Problem“ | `REJECTED` | breites Spektrum + Harmonische; BPF-Warnung Upstream |
| Install ohne config.txt-Änderung stabil | `REJECTED` | Upstream: sonst unstable |
| rpitx = markondej/fm_transmitter | `REJECTED` | anderer Scope (Multi-Mode vs. FM-WAV) |
| Easytest auf 434 MHz = überall frei nutzbar | `HYPOTHESIS` | ISM-Hinweis lokal prüfen; kein Freibrief |
| Pi4 „OK“ wie Pi3 | `REJECTED` | Matrix: Pi4 in beta |
| Bandbreite/Modes gelten automatisch auf Pi5/RP1 | `UNKNOWN` / Gate | anderer I/O-Chip; `hw-path-gate` |
| rpitx = ESP32 Multi-Mode-Äquivalent | `REJECTED` | anderer Chip-Contract; siehe `esp32-apll-fm-tx` nur für UKW-Analogie |

### Projektstart-Checkliste

- [ ] Recht + Filterstrategie vor jedem Mode
- [ ] Pi-Modell vs. Upstream-Matrix (Pi5/RP1 → Stop / Gate)
- [ ] librpitx/csdr-Build und Boot-Parameter
- [ ] FM-only? → eher `rpi-gpio-fm-tx` / PiFmRds prüfen
- [ ] RDS-Claims → zusätzlich `fm-rds`
- [ ] Application + `seen_in`

## Transfer

Lab-Plattform für Mode-Vergleiche und Spektrum-Demos (mit RX-Monitor). Nicht als PiDrive-Infotainment-Pfad. FM-RDS-Untermenge kann `fm-rds` speisen.

## Referenzen

- [F5OEO/rpitx](https://github.com/F5OEO/rpitx) · librpitx · groups.io/g/rpitx

## Offene Fragen

- Welche Modes auf Pi5/RP1 überhaupt noch tragfähig sind? (E-0 Desk → E-1 Lab; kein Sheet vorher)
