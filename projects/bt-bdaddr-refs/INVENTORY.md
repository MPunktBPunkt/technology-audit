# Project Inventory: bt-bdaddr-refs

```yaml
project_id: bt-bdaddr-refs
updated: 2026-11-12
reviewed_commit: "bdaddr@53dae3f"
profile: lab-tool
pilot_order: [bt-bdaddr-rewrite]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Vendor HCI Write BD_ADDR (CSR/TI/Intel/Cypress/…) | `bt-bdaddr-rewrite` | **neu** |
| Kein Espressif in Vendor-Tabelle | `bt-bdaddr-rewrite` | FACT / Fallstrick |
| ESP MAC via IDF APIs | `bt-bdaddr-rewrite` | Abgrenzung |

Kampagne: [bt-bdaddr-2026-foreign](../../audits/bt-bdaddr-2026-foreign/).

## Übersicht Sheets

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `bt-bdaddr-rewrite` | BT BD_ADDR Rewrite | C | applied | partial | [SHEET](../../technologies/bt-bdaddr-rewrite/SHEET.md) | [app](applications/bt-bdaddr-rewrite.md) |
