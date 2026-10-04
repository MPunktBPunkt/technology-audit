# Evidence — pidrive-2026-msc

Rohdaten bleiben in `pidrive` / `esp32.pidrive`. Hier nur IDs, Claims, Links, Epistemic-Status.

Basis-URL pidrive Docs: `https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/`

| ID | Claim (Kurz) | Layer | Status | Quelle |
|----|--------------|-------|--------|--------|
| `EVID-USBMSC-2026-10-04-001` | HU liest Slots per MSC-Block-I/O; Prefetch/Burst beobachtbar | C | `MEASURED` | Feldtraces unter `artifacts-2026-10-04-feld/` · Einstieg [MSC-AKTUELL.md](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) |
| `EVID-USBMSC-2026-10-04-002` | Auto-Next triggert Cold-Body-Burst nächsten Slot (LBA-Fenster) | C | `MEASURED` | [GESAMTBERICHT-FELD-Q3B-1732](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-feld/feld-q3b-next-1732/GESAMTBERICHT-FELD-Q3B-1732.md) · Analog 1738 |
| `EVID-USBMSC-2026-10-04-003` | Türöffnen → zusätzlicher Cold-Body/Re-Read (17:55) | C | `MEASURED` | MSC-AKTUELL Ampel / Feldbericht 1738-Kontext |
| `EVID-USBMSC-2026-10-04-004` | Seed an HU: `bytesServed` ≈ +8 MiB, C′ PASS 17:32 | B/C | `MEASURED` | GESAMTBERICHT 1732 |
| `EVID-USBMSC-2026-10-04-005` | Seed inactive bei GO → C′ FAIL 17:38 | B | `MEASURED` | [GESAMTBERICHT-FELD-Q3B-1738](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-feld/feld-q3b-next-1738/GESAMTBERICHT-FELD-Q3B-1738.md) |
| `EVID-USBMSC-2026-10-04-006` | Lab AV A+B: MPEG am Host-dd im Live-Fenster; ≠ Feld-Ohr | B | `MEASURED` | [GESAMTBERICHT-AV-MPEG-AT-HOST](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-04-lab/lab88-av-mpeg-2035/GESAMTBERICHT-AV-MPEG-AT-HOST.md) |
| `EVID-USBMSC-2026-10-04-007` | Frühere Deutung „Sequenz tot wegen warm-konfundierter Trace“ | — | `REJECTED` | Trace-Korrektur / Gesamtbericht M3SEQ 2026-10-04 (pidrive docs/betrieb) |

## Wissens-Chronik (Auszug)

| Datum | Ereignis |
|-------|----------|
| 2026-09-28 | Frühe Feldtests ESP-MSC am BMW (Repo-Feldbericht) |
| 2026-10-02–03 | Lab-Geometrie L0, Prefill/Oracle-Arbeit |
| 2026-10-04 | Feld Q3b 17:32 PASS Seed · 17:38 FAIL Seed · Lab AV A+B PASS · Feld-Ohr offen |
| 2026-10-04 | Dieser Pilot: Wissen nach A/B/C + Evidence-IDs strukturiert |
