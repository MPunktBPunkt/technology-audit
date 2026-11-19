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
  field_evidence: R2   # F20 DEEP_FORENSIC 2026-11-16/18 via esp32-bt-analyzer
  reusability: W2
updated: 2026-11-19
standard_version: "0.7.1"
related_audits:
  - ../../../audits/bmw-connected-sas-auth-2026-11-06/
  - ../../../audits/idriveconnectkit-securityaccess-2026-11-19/
```

## Rolle

Desk-Rekonstruktion der **SAS-Schicht** auf Basis BimmerGestalt-Quellen + Crosswalk zum
F20-Feld. Implementiert **keine** Auth und speichert **keine** Secrets. Blocker = OEM
`signChallenge`, nicht BCL-HS/KNOCK.

## Evidenz (Kurz)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| IDL sas_* | `EVID-SAS-2026-11-06-001` | FACT |
| AAIdrive Call-Graph | `EVID-SAS-2026-11-06-003` | FACT |
| Crypto MD5withRSA+XOR | `EVID-SAS-2026-11-06-009` | FACT (Phone recon) |
| Digests / RHMI whitelist | `EVID-SAS-2026-11-06-010`/`012` | FACT Doc + Narrative |
| Simulator open stub | `EVID-SAS-2026-11-06-017` | FACT |
| SecurityAccess / CertMangling / Packages | `EVID-SASACC-001`…`014` | FACT |
| F20 16-B Challenge + 512-B Sig / 559-B Frame | `EVID-SASACC-F01`/`F02` | FIELD MEASURED |
| Lab-sim Cert Auth REJECT am F20 | `EVID-SASACC-F04` | FIELD MEASURED |

## Gates (Audit-Definition)

| Gate | Dieses Projekt liefert |
|------|------------------------|
| G3 Desk | vollständiger Report |
| G3 Field | Follow-on → hu-probe FX-G3-01 |
| G4 Desk | RHMI Digests + App-Code Pfade |

Details: [`AUDIT-REPORT.md`](../../../audits/bmw-connected-sas-auth-2026-11-06/AUDIT-REPORT.md).
