# Evidence — pidrive-2026-bmw-hu

Rohdaten in `pidrive` / `esp32.pidrive`. Register für **Ebene C** (BMW NBT Evo als USB-MSC-Host). Pilot-1-IDs mit Präfix `USBMSC`; ab 2026-10-05 HU-Claims mit Präfix `BMWHU`. Revalidation **0.6.6** 2026-10-11 = Prozess-Parität. Feld **2026-10-12** E7/S6 Busy-Pacing: `EVID-BMWHU-2026-10-12-*` (Upstream-Artefakt nachziehen).

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
| `EVID-SCOPE-2026-10-11-001` | Host-Scope: C-Claims gelten für NBT Evo in PiDrive — nicht still andere BMW-HU | `FACT` | Sheet-Abgrenzung; Revalidation 0.6.6 |
| `EVID-MATCH-2026-10-11-001` | Prozess-Parität: Profile/Reuse/Checklisten/`standard_version` nachgezogen; Gaps 0.5.1 geschlossen | `FACT` | Kampagnen-YAML + DELTA |
| `EVID-BMWHU-2026-10-12-001` | NBT akzeptiert Busy-Pacing (`return 0` + Delay); READ10 läuft weiter | `MEASURED` | Session E7/S6 2026-10-12 · Desk-Basis [`tinyusb-msc-busy-retry-2026`](../tinyusb-msc-busy-retry-2026/) · **Upstream-Artefakt: nachziehen** |
| `EVID-BMWHU-2026-10-12-002` | Mit Busy-Pacing: ~65 s Wiedergabe bis Dateiende (512‑KiB-Datei) | `MEASURED` | Session E7/S6 2026-10-12 · **Upstream-Artefakt: nachziehen** |
| `EVID-BMWHU-2026-10-12-003` | Stall-off Gegenexperiment: wieder ~6 s Tonfenster | `MEASURED` | Session E7/S6 2026-10-12 · A/B zu 001/002 · **Upstream-Artefakt: nachziehen** |
| `EVID-BMWHU-2026-10-12-004` | Busy-Pacing kausaler Faktor für langes Tonfenster (A/B Stall-on vs. off) | `INFERRED` | aus 001–003 |
| `EVID-BMWHU-2026-10-12-005` | Annahme „kleiner Ring + kurze Tonphase als technische Grenze“ | `REJECTED` | widerlegt durch 002 vs. 003 |

## Offene Claims (noch ohne ID)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Feld-AV / hörbarer Ton (Exit „Ohr“ — Sender-Slots / Meta-Menü-Gate) | `UNKNOWN` (teilweise) | Busy-Pacing-Ton bis Dateiende belegt (`EVID-BMWHU-2026-10-12-002`); Exit #6 (Rock/Bayern/BOB + Menü-Gate) bleibt getrennt — [FELD-ABEND-EAR-2026-10-05](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-05-feld/FELD-ABEND-EAR-2026-10-05.md) |

## Wissens-Chronik (Auszug)

| Datum | Ereignis |
|-------|----------|
| 2026-10-04 | C-Claims in MSC-Pilot dokumentiert |
| 2026-10-05 | C-Register → Kampagne `pidrive-2026-bmw-hu` |
| 2026-10-05 | Nachzug upstream: C′ Feld PASS; AV-Gate/Menü-Lock Lab; Feld-AV noch offen |
| 2026-10-11 | Revalidation **0.6.6**: Framework-Parität + Host-Scope, [DELTA](DELTA.md); kein neuer Feld-Lauf |
| 2026-10-12 | E7/S6 Busy-Pacing Feld: ~65 s bis Dateiende vs. ~6 s Stall-off; IDs `EVID-BMWHU-2026-10-12-*`; Upstream-Artefakt nachziehen |
