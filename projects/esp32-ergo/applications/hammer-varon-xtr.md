# Project Application: hammer-varon-xtr in esp32.ergo

```yaml
project_id: esp32-ergo
tech_slug: hammer-varon-xtr
status: active
sheet: ../../../technologies/hammer-varon-xtr/SHEET.md
audit: ../../../audits/esp32-ergo-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R3
  reusability: W1
```

## Rolle im Projekt

Referenz-Bike für Coach und Bridge. Alle Quirks (kein Power Target, Success-Lüge, Advertising) sind **C** — speisen Capability-Ableitung und Kennfläche, gehören nicht still in `bluetooth-ftms` Spec-Claims.

## Architektur / Beobachtungsebene

```text
Probe (ftmsprobe) → GERAETEPROFIL → FtmsCapabilities + PowerMap (Kalibrierung)
Live: MAC/AddrType remember, IBD 0x2AD2, Resistance 0x04 sint16
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `docs/ergometer/GERAETEPROFIL.md` | verdichtete Messung |
| `docs/ergometer/KALIBRIERUNG.md` | Kennfläche |
| `docs/ergometer/scan-*` in ftmsprobe | Rohscan (extern) |
| `STATE.md` | offene Nachtests |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| `2ACC` ohne Power Target; `2AD8` fehlt | `EVID-FTMS-2026-10-09-001` | `MEASURED` |
| Success auf untrusted `0x05` | `EVID-FTMS-2026-10-09-002` | `MEASURED` |
| ~16 Stufen 1,0–16,0 Zehntel wirkend | `EVID-VARON-2026-10-09-001` | `MEASURED` |
| Advertising oft ohne Name/Services | `EVID-VARON-2026-10-09-002` | `MEASURED` |
| Nachtest 6 Crash unter Last | — | `UNKNOWN` |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-09-10 probe | GATT-Tabelle, Caps-Rohwerte |
| 2026-09-12/13 | Stufenwirkung, Sim ab ~3 % |

## Offene Fragen

- Firmware-Updates am Bike ändern Caps?
- Kadenzbänder dichter kalibrieren?

## Verwandte

- [bluetooth-ftms](bluetooth-ftms.md)
