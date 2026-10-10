# Technology Sheet: Raspberry Pi GPIO / Clock FM Transmit

```yaml
slug: rpi-gpio-fm-tx
title: Raspberry Pi GPIO / Clock FM Transmit
primary: D
tags: [radio-tx, lab-only, fragile, linux-userspace]
type: implementation
status: active
seen_in: [pi-fm-tx]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/pi-fm-tx-2026-foreign
```

Nur Ebene **A**. Repo-Pfade, WAV-Pipelines und Ops-Wrapper → Application.  
**Recht:** unlizenzierter Sendebetrieb mit Antenne ist in den meisten Ländern illegal — Sheet beschreibt Technik/Risiken, keinen Sendebetrieb.

## Kurzfassung

Muster: VHF-FM-Träger aus dem **BCM-Clock-/PLL-Pfad** auf einem GPIO (klassisch **GPIO 4**, auf Pi 4 oft **GPIO 21**), Modulation über Teiler-/Frac-Updates, typisch **DMA** + Mailbox. Linie Mattos/Weigl → Hirst → Jacquet/F5OEO PiFmRds → markondej `fm_transmitter` (+ Ableger). Rechteckträger → **Harmonische**. Multi-Mode-RF jenseits UKW-FM → `rpitx`.

## Abgrenzung

- **Ist:** SoC-Clock/GPIO als **UKW-FM**-Träger + Audio (WAV/stdin).
- **Ist nicht:** Empfang (`rtl-sdr`, `dab-plus`); allgemeine RF-Plattform (`rpitx`); RDS allein (`fm-rds`); Pi 5/RP1 (anderer Peripheral-Chip — Upstream markondej); legale Sendestation.

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | PCM / WAV / stdin / sox|ffmpeg-Pipe | oft 22.05 kHz S16 |
| unten | GPIO4 oder GPIO21 + DMA/Mailbox | Root; Pi4-Interferenz |
| lateral | CPU-Governor / feste ARM-Freq | Pi4-Workaround Upstream |
| lateral | systemd / Playlist-Loop | Ops-Wrapper, nicht Teil des RF-Contracts |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Antenne am GPIO = harmloses Experiment | `REJECTED` | oft illegal; geschirmte Direktverbindung RX↔Pi |
| Spektrum ist „sauberes FM“ | `REJECTED` | starke ungerade Harmonische ohne Filter |
| DMA-Stop fehlt beim Exit → harmlos | `REJECTED` | DMA kann fremdem Speicher folgen |
| Ein Binary / ein GPIO für alle Pi | `REJECTED` | Pi1≠2/3; Pi4 oft GPIO21 + Governor; Pi5 unsupported (markondej) |
| Empfangs-Sheets decken TX ab | `REJECTED` | RX≠TX |
| PLL-Modulation löst Harmonic-Problem | `REJECTED` | Reinheit ≠ Filterpflicht |
| Fork mit Install-Script = neue Tech | `REJECTED` | oft derselbe Clock-TX-Contract (zoroxide ≈ markondej) |
| systemd-Player ändert RF-Recht | `REJECTED` | nur Ops um denselben TX |

### Projektstart-Checkliste

- [ ] Rechtliche Grenze: kein Antennen-TX ohne Lizenz/Filter
- [ ] Pi-Modell: GPIO4 vs GPIO21; Pi5 aussortieren
- [ ] DMA/Mailbox vs. CPU-Fallback (`-d 255` bei markondej)
- [ ] Audio-Pipeline (WAV vs. sox/ffmpeg → stdin)
- [ ] RDS nötig? → `fm-rds` / PiFmRds / rpitx-Untermenge
- [ ] Multi-Mode / andere Bänder? → `rpitx`
- [ ] Application + `seen_in`

## Transfer

Kontrast zu PiDrive-Empfang; Warnkatalog „Pi = Sender“. Produkt-Audio eher A2DP/Kabel. Ops-Muster (systemd + Decode-Cache) ist wiederverwendbar **ohne** den RF-Pfad zu empfehlen.

## Referenzen

- Mattos/Weigl · Hirst · Jacquet PiFmRds · [markondej/fm_transmitter](https://github.com/markondej/fm_transmitter) · [rm-hull/pifm](https://github.com/rm-hull/pifm) · [F5OEO/PiFmRds](https://github.com/F5OEO/PiFmRds) · [cdzombak/pi-fm-player](https://github.com/cdzombak/pi-fm-player) · [zoroxide/Pi-Fm_transmitter](https://github.com/zoroxide/Pi-Fm_transmitter)

## Offene Fragen

- Pi5/RP1: gibt es einen gepflegten Nachfolger-Pfad?
- Wann BPF Pflicht auch bei geschirmtem Lab-Kabel?
