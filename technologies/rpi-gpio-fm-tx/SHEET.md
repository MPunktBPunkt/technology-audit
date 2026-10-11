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
**Chip-Scope:** **BCM283x / BCM2711** (Raspberry Pi 1–4) mit **GPCLK-/PLL-/DMA-Userspace-Pfad**. **Raspberry Pi 5 / RP1:** **nicht** im Scope dieses Sheets (anderer Peripheral-Chip; Upstream markondej: unsupported). Keine automatische Übertragung BCM → RP1.

## Kurzfassung

Muster: VHF-FM-Träger aus dem **BCM-Clock-/PLL-Pfad** auf einem GPIO (klassisch **GPIO 4**, auf Pi 4 oft **GPIO 21**), Modulation über Teiler-/Frac-Updates, typisch **DMA** + Mailbox. Linie Mattos/Weigl → Hirst → Jacquet/F5OEO PiFmRds → markondej `fm_transmitter` (+ Ableger). Rechteckträger → **Harmonische**. Multi-Mode-RF jenseits UKW-FM → `rpitx`.

## Abgrenzung

- **Ist:** BCM-SoC-Clock/GPIO als **UKW-FM**-Träger + Audio (WAV/stdin) auf Pi 1–4.
- **Ist nicht:** Empfang (`rtl-sdr`, `dab-plus`); allgemeine RF-Plattform (`rpitx`); RDS allein (`fm-rds`); Pi 5/RP1 (Gate nötig — kein Sheet-Ausweiten); ESP32 APLL/MCLK-FM (`esp32-apll-fm-tx` — Analogie nur im Muster, anderer Chip-Contract); legale Sendestation.

## Signalpfad-Kette

| Stufe | Claim | Status | Evidence |
|-------|-------|--------|----------|
| BCM osc / PLL | Clock-Quelle für GPCLK-Pfad | `FACT` | pifm / PiFmRds / markondej Docs+Code |
| PLL / Frac-Divider | Trägerfrequenz + FM-Nudges | `FACT` | PiFmRds PLL-README; markondej transmitter |
| DMA + Mailbox mem | Sample-/Frac-Updates ohne reinen CPU-Pfad (optional CPU-Fallback) | `FACT` | `EVID-PIFM-…-001`, `EVID-FMTX-…-002` |
| GPCLK → GPIO pad | klassisch GPIO4; Pi4 oft GPIO21 | `FACT` | `EVID-PIFM-…-003`, `EVID-FMTX-…-001` |
| Physical pad / Draht | Emissionspunkt; Legal/Filter | `FACT` | Upstream Warnings |
| Measured RF / Harmonics | Pegel, Spurious | `UNKNOWN` | kein Lab in dieser KB |
| RP1 (Pi5) gleicher Pfad | BCM-GPCLK-Äquivalent | `UNKNOWN` | markondej unsupported; Gate E-0/E-1 |

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
| Pi4-GPIO21-Pfad gilt auf Pi5/RP1 | `UNKNOWN` / Gate | anderer Chip; `hw-path-gate` E-0/E-1; kein Sheet vor Evidence |
| „Pi kann Software-FM“ ohne SoC-Angabe | `REJECTED` (als FACT) | Chip-Scope Pflicht (G17); sonst höchstens `HYPOTHESIS` |
| Empfangs-Sheets decken TX ab | `REJECTED` | RX≠TX |
| PLL-Modulation löst Harmonic-Problem | `REJECTED` | Reinheit ≠ Filterpflicht |
| Fork mit Install-Script = neue Tech | `REJECTED` | oft derselbe Clock-TX-Contract (zoroxide ≈ markondej) |
| systemd-Player ändert RF-Recht | `REJECTED` | nur Ops um denselben TX |
| ESP32-APLL-Evidence überträgt sich auf BCM-GPCLK | `REJECTED` | getrennte Slugs; nur Muster-Analogie |

### Projektstart-Checkliste

- [ ] Rechtliche Grenze: kein Antennen-TX ohne Lizenz/Filter
- [ ] Pi-Modell / Chip: BCM Pi1–4 (GPIO4 vs GPIO21); Pi5/RP1 → Stop / Gate, nicht dieses Sheet verbiegen
- [ ] DMA/Mailbox vs. CPU-Fallback (`-d 255` bei markondej)
- [ ] Audio-Pipeline (WAV vs. sox/ffmpeg → stdin)
- [ ] RDS nötig? → `fm-rds` / PiFmRds / rpitx-Untermenge
- [ ] Multi-Mode / andere Bänder? → `rpitx`
- [ ] Application + `seen_in`

## Transfer

Kontrast zu PiDrive-Empfang; Warnkatalog „Pi = Sender“. Produkt-Audio eher A2DP/Kabel. Ops-Muster (systemd + Decode-Cache) ist wiederverwendbar **ohne** den RF-Pfad zu empfehlen.

- Kontrast zu `esp32-apll-fm-tx`: gleiches *Muster* (PLL/Clock-FM), anderer Peripheral-Contract; Pi-DMA-Exit-Risiko nicht als ESP-FACT übernehmen.
- Pi5/RP1: FOLLOW-ON + `hw-path-gate` — analog ESP32-S3-Gate auf der ESP-Seite.

## Referenzen

- Mattos/Weigl · Hirst · Jacquet PiFmRds · [markondej/fm_transmitter](https://github.com/markondej/fm_transmitter) · [rm-hull/pifm](https://github.com/rm-hull/pifm) · [F5OEO/PiFmRds](https://github.com/F5OEO/PiFmRds) · [cdzombak/pi-fm-player](https://github.com/cdzombak/pi-fm-player) · [zoroxide/Pi-Fm_transmitter](https://github.com/zoroxide/Pi-Fm_transmitter)
- Revalidation: [`audits/pi-fm-tx-2026-foreign/DELTA.md`](../../audits/pi-fm-tx-2026-foreign/DELTA.md)

## Offene Fragen

- Pi5/RP1: konkretisierbarer Clock→Pad-Pfad (E-0) und messbarer Träger (E-1)?
- Wann BPF Pflicht auch bei geschirmtem Lab-Kabel?
