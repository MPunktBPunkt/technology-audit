# Project Application: bmw-sas-auth in hu-probe

```yaml
project_id: hu-probe
tech_slug: bmw-sas-auth
status: active
sheet: ../../../technologies/bmw-sas-auth/SHEET.md
audit: ../../../audits/bmw-connected-sas-auth-2026-11-06/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R2   # FX-G3-01 proven on F20 over BT (esp32-bt-analyzer DEEP_FORENSIC_ETCH_SAS_20261116)
  reusability: W2
updated: 2026-11-16
standard_version: "0.7.1"
```

## Rolle im Projekt

**Beobachtungsziel G3**, nicht Firmware-Feature. hu-probe / ESP32-Analyzer können
SAS nur indirekt sehen (Etch in BCL DATA nach Tunnel). Phone + Connected/MyBMW +
AAIdrive bleiben die Signing-Seite.

## Abgrenzung zu bestehenden Gates

| Messart | Beweist |
|---------|---------|
| AOA Enum / 51–53 / Bulk | G1 / Ansatz G2 — **nicht** G3 |
| BCL Framer Lab | G2 Lab — **nicht** G3 |
| Etch `DEADBEEF` + sas_* decode oder korrelierte AAIdrive Logs | **G3** |

Siehe Run-Sheet FX-G3-01 in
[`AUDIT-REPORT.md` §22](../../../audits/bmw-connected-sas-auth-2026-11-06/AUDIT-REPORT.md).
**Update 2026-11-16:** FX-G3-01 ist am F20 über Bluetooth (`SCN 6`) vollständig bewiesen (`esp32-bt-analyzer` `DEEP_FORENSIC_ETCH_SAS_20261116.md`: `_result_sas_certificate` 16-B-Challenge + `559 B` RSA-4096 `MD5withRSA` XOR-Signatur aus MyBMWs JNI-`SecurityModule` via `BMWTouchCommand_Connection_00.00.10` + `_result_sas_login`).

## Nicht tun

- SAS in ESP32 „nachbauen“ aus diesem Desk-Audit
- Simulator-Erfolg als HU-Auth werten
- Private Keys in Repo legen
