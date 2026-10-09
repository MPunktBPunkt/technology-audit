# Project Application: kostal-piko-http in iobroker.kostalpiko

```yaml
project_id: iobroker-kostalpiko
tech_slug: kostal-piko-http
status: active
sheet: ../../../technologies/kostal-piko-http/SHEET.md
audit: ../../../audits/iobroker-kostalpiko-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

Adapter pollt den **lokalen PIKO-Webserver** (Basic Auth), parst `index.fhtml` / `Inf.fhtml`, optional `LogDaten.dat` für 15‑min-Historie. States unter `kostalpiko.N.*`; Engineer-Dashboard auf `webPort` (Default 8092).

## Architektur / Datenfluss

```text
_fetchPage(/index.fhtml) ──latin1──▶ Zellen-Parser (2 vs 3 Strings)
_fetchPage(/LogDaten.dat) ──Tab-CSV──▶ History/Influx (Catch-up)
Serialisierung: Live-Poll und LogDaten nicht parallel (ein HTTP-Client am Gerät)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `main.js` | Poll, Parser, WebUI, Influx |
| `Schnittstellen.md` | Device- + ioBroker-Contract |
| `admin/jsonConfig.json` | IP/Auth/Modell/webPort |
| `docs/README.de.md` | DE-Doku |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| Auth Default | `pvserver` / `pvwr` | `FACT` (Schnittstellen) |
| Encoding | windows-1252 → `latin1` | `FACT` |
| Modelle | 3.0–10.1; auto via cells.length | `FACT` |
| webPort | 8092 (+1 / Instanz) | `FACT` |
| pollInterval | Default 30 s | `FACT` (Config) |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Interleaved String/L-Zellenordnung | `EVID-PIKO-2026-10-09-001` | `FACT` |
| LogDaten nur serialisiert / nachts oft skip | `EVID-PIKO-2026-10-09-002` | `FACT` |
| ≠ Catalog-Eintrag `kostal-piko-ba` | `EVID-PIKO-2026-10-09-003` | `FACT` |

## Verwandte

- Sheet: [`kostal-piko-http`](../../../technologies/kostal-piko-http/SHEET.md)
- Catalog-Ops: [`iobroker-repositories`](../../iobroker-repositories/)
