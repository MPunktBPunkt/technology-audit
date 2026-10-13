# Technology Sheet: FM-RDS (Radio Data System)

```yaml
slug: fm-rds
title: FM-RDS (Radio Data System)
primary: C
tags: [radio-tx, metadata, lab-only]
type: protocol
status: active
seen_in: [pi-fm-tx, esp-fm-rds-node]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/pi-fm-tx-2026-foreign
```

Nur Ebene **A**. Encoder-Pfade und PS/RT-Strings → Application.

## Kurzfassung

**RDS** auf UKW-FM: digitale Nebeninformation auf ~57 kHz-Unterträger (BPSK), typisch Gruppen mit PI, PS (8 Zeichen), RT (bis 64), optional TA u. a. Unabhängig vom Träger-Generator — braucht aber ein Multiplex, das den Unterträger trägt.

## Abgrenzung

- **Ist:** Protokoll/Baseband-RDS (Gruppen, CRC, Felder PI/PS/RT…).
- **Ist nicht:** FM-Trägererzeugung (`rpi-gpio-fm-tx`); DAB-DLS; AVRCP/MPRIS-Metadaten; Empfangs-Demod allein.

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Station-Meta (PI, PS, RT, …) | Laufzeit-Update oft per Control-Pipe |
| unten | MPX/Baseband @ ausreichend hoher Rate | z. B. ~228 kHz Samplepfad für 57 kHz |
| lateral | FM-Stereo-Pilot 19 kHz | gemeinsames MPX mit Audio |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| PS/RT ändern = A2DP/AVRCP-Titel | `REJECTED` | anderes Medium, andere Senke |
| RDS ohne sauberes MPX „einfach anhängen“ | `REJECTED` | Unterträger/Timing Teil der Modulation |
| Jeder FM-RX zeigt RDS | `REJECTED` | Chip/Firmware/Antenne; Upstream listet getestete Geräte |
| RDS macht unlizenzierte Aussendung legal | `REJECTED` | Meta ändert Lizenzpflicht nicht |

### Projektstart-Checkliste

- [ ] Felder (PI/PS/RT/…) und Update-Kanal (CLI vs. Pipe) festlegen
- [ ] MPX-/Sample-Rate-Contract mit TX-Pfad klären
- [ ] Empfänger-Testraum (welche Geräte RDS wirklich zeigen)
- [ ] Nicht mit DAB-DLS/AVRCP vermischen
- [ ] Application + `seen_in`

## Transfer

Für Lab-Meta auf FM-Loopback oder spezifizierte RDS-Encoder. In PiDrive eher DAB-DLS / MPRIS / AVRCP — gleicher *Zweck* (Text am Empfänger), anderes Protokoll.

## Referenzen

- IEC/EN RDS · PiFmRds `rds.c` / Control-Pipe · rpitx `src/pifmrds` · Christophe Jacquet / F5OEO-Linie

## Offene Fragen

- Welche Gruppen außer 0A/2A braucht ein gezielter Lab-Empfänger minimal?
