# Project Inventory: iobroker.freeair100

```yaml
project_id: iobroker-freeair100
updated: 2026-10-09
reviewed_commit: 501f344
profile: adapter
pilot_order: [freeair-connect-portal]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), 0.6.3):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| freeair-connect.de HTML/API Poll + Parsing | `freeair-connect-portal` | **neu** |
| WebUI :8096 / Control-Placeholder | — | Application B |
| AES-CBC Minutenwerte (`values.php`) | `freeair-connect-portal` | Coverage-Lücke |

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `freeair-connect-portal` | freeAir Connect Portal | F | `iot`,`cloud` | applied | partial | [SHEET](../../technologies/freeair-connect-portal/SHEET.md) | [app](applications/freeair-connect-portal.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| AES-Key aus freeair.js | README: noch nicht extrahiert | Key → vollständige values.php |
| Control POST | Placeholder | Endpoint klären |
