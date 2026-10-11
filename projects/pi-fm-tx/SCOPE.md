# Project Scope: Pi FM / RF Transmit (Fremdrepos)

```yaml
project_id: pi-fm-tx
title: Pi FM / RF Transmit (Fremd)
updated: 2026-10-11
profile_hint: lab-tool
reviewed_commit: "pifm@6c30d00 PiFmRds@2707ecc fm_transmitter@322500e rpitx@ee7ff57 Pi-Fm_transmitter@552f955 pi-fm-player@f602f42"
reviewed_commit_note: Sechs Upstream-Repos; Desk-Audit ohne Feldaussendung
repos:
  - https://github.com/rm-hull/pifm
  - https://github.com/F5OEO/PiFmRds
  - https://github.com/markondej/fm_transmitter
  - https://github.com/F5OEO/rpitx
  - https://github.com/zoroxide/Pi-Fm_transmitter
  - https://github.com/cdzombak/pi-fm-player
status: active
```

## Zweck

KB-Test / Transferwissen: Raspberry-Pi-**Software-TX** (UKW-FM-Linie + rpitx Multi-Mode) als Kontrast zu PiDrive-**Empfang**. Wissen und Fallstricke — **kein** Sendebetrieb.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| pifm / PiFmRds / fm_transmitter / Pi-Fm_transmitter / pi-fm-player | UKW-FM GPIO-Clock-Linie | ja (Desk) |
| rpitx | Multi-Mode RF-Plattform | ja (Desk, Überblick) |
| PiDrive Empfang | Kontrast RX | angrenzend |
| Antennen-Feld-TX | — | **nein** |

## Nicht-Ziele

- Anleitung zu unlizenzierter Aussendung
- Vollständige Mode-für-Mode-Laborserie rpitx
- Produkt-Infotainment-Sendepfad

## Prioritäten

1. Match: FM-Linie vs. `rpitx`-Sheet  
2. Forks/Wrapper ohne Sheet-Explosion (zoroxide, pi-fm-player)  
3. Recht / Filter / Pi-Modell-Fallen (Chip-Scope BCM ≠ RP1)  
4. Evidence auf Commits  
5. Revalidation 0.6.6: Signalpfad + Gate vor Pi5-Sheet ([DELTA](../../audits/pi-fm-tx-2026-foreign/DELTA.md))
