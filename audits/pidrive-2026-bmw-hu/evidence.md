# Evidence — pidrive-2026-bmw-hu

Rohdaten in `pidrive` / `esp32.pidrive`. Register für **Ebene C** (BMW NBT Evo als USB-MSC-Host). Pilot-1-IDs mit Präfix `USBMSC`; ab 2026-10-05 HU-Claims mit Präfix `BMWHU` (siehe Tabelle).

Basis-URL: `https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/`

Normativer Ampel-Stand: [MSC-AKTUELL.md](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) (2026-10-05 Vormittag).

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBMSC-2026-10-04-001` | HU liest Slots per MSC-Block-I/O; Prefetch/Burst | `MEASURED` | Feldtraces `artifacts-2026-10-04-feld/` · MSC-AKTUELL |
| `EVID-USBMSC-2026-10-04-002` | Auto-Next → Cold-Body-Burst nächster Slot | `MEASURED` | [GESAMTBERICHT-FELD-Q3B-1732](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-feld/feld-q3b-next-1732/GESAMTBERICHT-FELD-Q3B-1732.md) |
| `EVID-USBMSC-2026-10-04-003` | Türöffnen → zusätzlicher Re-Read (17:55) | `MEASURED` | MSC-AKTUELL / Feld 1738-Kontext |
| `EVID-USBMSC-2026-10-04-004` | Seed an HU: `bytesServed` ≈ +8 MiB (17:32) | `MEASURED` | GESAMTBERICHT 1732 |
| `EVID-USBMSC-2026-10-04-005` | Seed inactive bei GO (17:38) — HU sieht keinen Seed-Fortschritt | `MEASURED` | [GESAMTBERICHT-FELD-Q3B-1738](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-feld/feld-q3b-next-1738/GESAMTBERICHT-FELD-Q3B-1738.md) |
| `EVID-USBMSC-2026-10-04-006` | Lab AV A+B am Host-dd ≠ Feld-Ohr (2026-10-04) | `MEASURED` | [GESAMTBERICHT-AV-MPEG-AT-HOST](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-lab/lab88-av-mpeg-2035/GESAMTBERICHT-AV-MPEG-AT-HOST.md) |
| `EVID-USBMSC-2026-10-04-007` | Deutung „Sequenz tot (warm Trace)“ | `REJECTED` | Trace-Korrektur M3SEQ 2026-10-04 |
| `EVID-BMWHU-2026-10-05-001` | Feld-Oracle C′ **PASS** (07:45): `bytesServed` +1,5 MiB, Seed überlebte Settle | `MEASURED` | [FELD-SESSION-2026-10-05-MORGEN](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-05-feld/FELD-SESSION-2026-10-05-MORGEN.md) · [`feld-q3b-next-0744/`](https://github.com/MPunktBPunkt/pidrive/tree/main/docs/betrieb/artifacts-2026-10-05-feld/feld-q3b-next-0744) |
| `EVID-BMWHU-2026-10-05-002` | Feld-AV-Versuch blockiert: Meta-Menü, stream off / live=0 (07:50) | `MEASURED` | [`feld-av-0750/`](https://github.com/MPunktBPunkt/pidrive/tree/main/docs/betrieb/artifacts-2026-10-05-feld/feld-av-0750/) · MSC-AKTUELL Ampel |
| `EVID-BMWHU-2026-10-05-003` | Lab Menü-Seite **PASS**: Sender-Slots, Lock, AV-Vorbereitung | `MEASURED` | [GESAMTBERICHT-MENU-PAGE-AV-PREP](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-05-lab/lab88-menu-page-0816/GESAMTBERICHT-MENU-PAGE-AV-PREP.md) |
| `EVID-BMWHU-2026-10-05-004` | Lab Correlate: Meta=Negativ / Sender=Positiv **PASS** | `MEASURED` | [GESAMTBERICHT-CORRELATE-META-SENDER](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-05-lab/lab88-correlate-meta-sender-0855/GESAMTBERICHT-CORRELATE-META-SENDER.md) |
| `EVID-BMWHU-2026-10-05-005` | Lab: Meta-Erstsiegel überlebt Soft-RST; Rock via `frozen_reject` blockiert | `MEASURED` | [GESAMTBERICHT-LOCK-AFTER-RST](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-05-lab/lab88-lock-after-rst-1022/GESAMTBERICHT-LOCK-AFTER-RST.md) |

## Offene Claims (noch ohne ID)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Feld-AV / hörbarer Ton (Exit „Ohr“) | `UNKNOWN` | Lab A+B PASS (Sender-Seite); Feld blockiert bis HU Rock/Bayern/BOB + Gate — [FELD-ABEND-EAR-2026-10-05](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-05-feld/FELD-ABEND-EAR-2026-10-05.md) |

## Wissens-Chronik (Auszug)

| Datum | Ereignis |
|-------|----------|
| 2026-10-04 | C-Claims in MSC-Pilot dokumentiert |
| 2026-10-05 | C-Register → Kampagne `pidrive-2026-bmw-hu` |
| 2026-10-05 | Nachzug upstream: C′ Feld PASS; AV-Gate/Menü-Lock Lab; Feld-AV noch offen |
