# Project Application: bluetooth-ftms in esp32.ftmsprobe

```yaml
project_id: esp32-ftmsprobe
tech_slug: bluetooth-ftms
status: active
sheet: ../../../technologies/bluetooth-ftms/SHEET.md
audit: ../../../audits/esp32-ftmsprobe-2026-pilot/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R3
  reusability: W3
```

## Rolle im Projekt

Sonde liest/schreibt FTMS zur **Charakterisierung**, nicht zur Trainingsregelung. Ergebnis speist Sheet-Fallstricke und Ergo-Capability-Design. `tools/ftms.py` = ausführbare Codec-Referenz.

## Architektur / Datenfluss

```text
read/subscribe/write ──▶ 0x2ACC/2AD6/2AD8/2AD2/2AD9 ──▶ scan-<datum>/ + ERGEBNISBERICHT
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `src/ble/FtmsLive.*` | Live-IBD-Decode |
| `tools/ftms.py` | Codec-Selbsttest |
| `docs/ergometer/ERGEBNISBERICHT.md` | verdichtete Caps |
| `docs/ergometer/scan-20260910/` | Rohartefakte |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Ausgang 1: Standard-FTMS, Control offen | `EVID-FTMS-2026-10-09-001` (geteilt mit ergo) | `MEASURED` |
| Resistance sint16 Zehntel wirkt; uint8-Lesart nicht | `EVID-VARON-2026-10-09-001` | `MEASURED` |
| Power Target Feature nein; Success ohne Beleg | `EVID-FTMS-2026-10-09-002` | `MEASURED` |

## Abweichungen vom Ergo-Projekt

- Kein Limiter/PowerController — nur Messung.
- Bericht ist Input für Ergo, nicht Produktverhalten.

## Offene Fragen

- Simulation `0x11` Wirkung systematisch nachziehen?

## Verwandte

- [hammer-varon-xtr](hammer-varon-xtr.md)
- Ergo-Application [bluetooth-ftms](../../esp32-ergo/applications/bluetooth-ftms.md)
