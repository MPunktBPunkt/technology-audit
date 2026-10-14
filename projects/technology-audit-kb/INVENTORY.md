# Project Inventory: technology-audit KB (Meta)

```yaml
project_id: technology-audit-kb
updated: 2026-10-14
reviewed_commit: "5fab7f5"
profile: ops-field
pilot_order: [epistemic-status, evidence-ids, measured-clusters]
```

**Reuse / Match:** Kein neuer Tech-Slug. Die „Technologien“ dieser Meta-Kampagne
sind Verfahrensartefakte der KB selbst.

## Übersicht

| Signal | Ort | Status | Coverage | Hinweis |
|--------|-----|--------|----------|---------|
| Epistemic-Status | [`docs/DOCUMENT-STANDARD.md`](../../docs/DOCUMENT-STANDARD.md) | applied | partial | FACT/MEASURED/… definiert |
| Evidence-IDs | `audits/*/evidence.md` | observed | partial | ~439 unique IDs; ~28 unique `MEASURED` |
| Desk≠Lab≠Field | Methodology + Kampagnen | applied | partial | durchgängig zitiert |
| MEASURED-Cluster PiDrive | `pidrive-2026-*`, Apps | applied | partial | stärkster Messblock |
| MEASURED-Cluster Ergo/FTMS/HR | `esp32-ergo/ftmsprobe/heartrate` | applied | partial | Geräte-/Lab-Messungen |
| MEASURED-Index (zentral) | — | candidate | none | fehlt — Follow-on |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Zentraler MEASURED-Ledger | nur verstreut in Evidence-Dateien | Index/Report pflegen |
| Stale active Desk-Kampagnen | ~50 active vs. 7 closed | Batch-Close desk-complete |
| Schwache MEASURED-Quellen | z. B. README-„getestet“ | auf Artefakt-Tiefe prüfen |
| Sheet `field_evidence` | 49× R0 (korrekt für A) | Navigation über Apps, nicht Sheets |
