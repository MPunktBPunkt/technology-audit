# Project Application: bmw-bcl RFCOMM role (delta)

```yaml
project_id: bimmergestalt-idrive-refs
tech_slug: bmw-bcl
focus: rfcomm-client-server-roles
status: active
sheet: ../../../technologies/bmw-bcl/SHEET.md
audit: ../../../audits/bmw-bcl-rfcomm-role-2026-desk/
related_audits:
  - ../../../audits/bimmergestalt-idrive-2026-foreign/
  - ../../../audits/bmw-connected-sas-auth-2026-11-06/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

Focused follow-up (gap 4/5): **RFCOMM client/server roles** between phone app and HU.
Does **not** re-audit BCL framing, Etch, or SAS — see prior campaigns.

## Evidenz (Desk)

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Phone app opens RFCOMM **client** via `createRfcommSocketToServiceRecord(SDP_BCL)` | `EVID-BCLRF-2026-11-12-001` | `FACT` |
| `SDP_BCL` = generic SPP UUID `00001101-0000-1000-8000-00805F9B34FB` | `EVID-BCLRF-2026-11-12-002` | `FACT` |
| HU is SDP provider / RFCOMM **server** (inferred from client connect pattern) | `EVID-BCLRF-2026-11-12-003` | `INFERENCE` |
| Watchdog dest 5001; ping `0x13371337` every 5s; timeout 20s | `EVID-BCLRF-2026-11-12-004` | `FACT` |
| A2DP-connected devices used as discovery hint in `BtClientService` | `EVID-BCLRF-2026-11-12-005` | `FACT` |

## CROSSREF (nicht duplizieren)

| Thema | Audit |
|-------|-------|
| BCL framing / Handshake / Init `12 34 56 78` | [`bimmergestalt-idrive-2026-foreign`](../../../audits/bimmergestalt-idrive-2026-foreign/) · [`bmw-bcl.md`](bmw-bcl.md) · [`bmw-bcl-handshake.md`](bmw-bcl-handshake.md) |
| SAS challenge/response über Etch | [`bmw-connected-sas-auth-2026-11-06`](../../../audits/bmw-connected-sas-auth-2026-11-06/) · [`bmw-sas-auth.md`](bmw-sas-auth.md) |

## Abgrenzung

RFCOMM-Rolle war die verbleibende Gap nach SAS/Etch Desk. Keine Secrets, keine Bypass-Schritte.
