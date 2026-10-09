# Project Application: freeair-connect-portal in iobroker.freeair100

```yaml
project_id: iobroker-freeair100
tech_slug: freeair-connect-portal
status: active
sheet: ../../../technologies/freeair-connect-portal/SHEET.md
audit: ../../../audits/iobroker-freeair100-2026-pilot/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R1
  reusability: W1
```

## Rolle

Poll per Seriennummer gegen freeair-connect.de; HTML-Parsing (nav4/nav1); WebUI :8096. Minuten-AES noch blockiert.

## Pfade

| Pfad | Rolle |
|------|-------|
| `main.js` | Poll/Parse/States/Web |
| `Schnittstellen.md` | Portal + REST |
| `io-package.json` | native serialnumber, webPort 8096 |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Portal GET ohne Auth, Serial in HTML | `EVID-FA-2026-10-09-001` | `FACT` |
| values.php AES 267 kB — Key offen | `EVID-FA-2026-10-09-002` | `FACT` |
| WebPort 8096 | `EVID-FA-2026-10-09-003` | `FACT` |
