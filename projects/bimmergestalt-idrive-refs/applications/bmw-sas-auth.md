# Project Application: bmw-sas-auth in bimmergestalt-idrive-refs

```yaml
project_id: bimmergestalt-idrive-refs
tech_slug: bmw-sas-auth
status: active
sheet: ../../../technologies/bmw-sas-auth/SHEET.md
audit: ../../../audits/bmw-connected-sas-auth-2026-11-06/
related:
  - bmw-etch-rpc
  - bmw-bcl
  - bmw-rhmi
maturity:
  technology: R2
  implementation: R2   # fremd: AAIdrive + KitAndroid
  field_evidence: R0
  reusability: W2
updated: 2026-11-06
standard_version: "0.7.1"
```

## Rolle

Desk-Rekonstruktion der **SAS-Schicht** auf Basis BimmerGestalt-Quellen, als Grundlage
für hu-probe / Analyzer Feldtests. Dieses Application-Dokument implementiert **keine**
Auth und speichert **keine** Secrets.

## Evidenz (Kurz)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| IDL sas_* | `EVID-SAS-2026-11-06-001` | FACT |
| AAIdrive Call-Graph | `EVID-SAS-2026-11-06-003` | FACT |
| Crypto MD5withRSA+XOR | `EVID-SAS-2026-11-06-009` | FACT (Phone recon) |
| Digests / RHMI whitelist | `EVID-SAS-2026-11-06-010`/`012` | FACT Doc + Narrative |
| Simulator open stub | `EVID-SAS-2026-11-06-017` | FACT |
| Eigenes F20 SAS Capture | `EVID-SAS-2026-11-06-022` | UNKNOWN |

## Gates (Audit-Definition)

| Gate | Dieses Projekt liefert |
|------|------------------------|
| G3 Desk | vollständiger Report |
| G3 Field | Follow-on → hu-probe FX-G3-01 |
| G4 Desk | RHMI Digests + App-Code Pfade |

Details: [`AUDIT-REPORT.md`](../../../audits/bmw-connected-sas-auth-2026-11-06/AUDIT-REPORT.md).
