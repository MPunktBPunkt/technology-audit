# Evidence — pidrive-2026-bmw-hu

Rohdaten in `pidrive` / `esp32.pidrive`. Register für **Ebene C** (BMW NBT Evo als USB-MSC-Host). IDs aus Pilot 1 beibehalten; Quellen unverändert.

Basis-URL: `https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/`

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBMSC-2026-10-04-001` | HU liest Slots per MSC-Block-I/O; Prefetch/Burst | `MEASURED` | Feldtraces `artifacts-2026-10-04-feld/` · [MSC-AKTUELL.md](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) |
| `EVID-USBMSC-2026-10-04-002` | Auto-Next → Cold-Body-Burst nächster Slot | `MEASURED` | [GESAMTBERICHT-FELD-Q3B-1732](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-feld/feld-q3b-next-1732/GESAMTBERICHT-FELD-Q3B-1732.md) · 1738 |
| `EVID-USBMSC-2026-10-04-003` | Türöffnen → zusätzlicher Re-Read (17:55) | `MEASURED` | MSC-AKTUELL / Feld 1738-Kontext |
| `EVID-USBMSC-2026-10-04-004` | Seed an HU: `bytesServed` ≈ +8 MiB (17:32) | `MEASURED` | GESAMTBERICHT 1732 |
| `EVID-USBMSC-2026-10-04-005` | Seed inactive bei GO (17:38) — HU sieht keinen Seed-Fortschritt | `MEASURED` | [GESAMTBERICHT-FELD-Q3B-1738](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-feld/feld-q3b-next-1738/GESAMTBERICHT-FELD-Q3B-1738.md) |
| `EVID-USBMSC-2026-10-04-006` | Lab AV A+B am Host-dd ≠ Feld-Ohr | `MEASURED` | [GESAMTBERICHT-AV-MPEG-AT-HOST](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-lab/lab88-av-mpeg-2035/GESAMTBERICHT-AV-MPEG-AT-HOST.md) |
| `EVID-USBMSC-2026-10-04-007` | Deutung „Sequenz tot (warm Trace)“ | `REJECTED` | Trace-Korrektur M3SEQ 2026-10-04 |

## Offene Claims (noch ohne ID)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Feld-AV / hörbarer Ton über MSC | `UNKNOWN` | [MSC-AKTUELL](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) Ampel FAIL · Stand 2026-10-04 upstream |

## Wissens-Chronik (Auszug)

| Datum | Ereignis |
|-------|----------|
| 2026-10-04 | C-Claims in MSC-Pilot dokumentiert |
| 2026-10-05 | C-Register → Kampagne `pidrive-2026-bmw-hu`; upstream unverändert (kein Feld-AV PASS) |
