# Technology Sheet: BMW SAS Authentication (Connected Apps)

```yaml
slug: bmw-sas-auth
title: BMW SAS — Connected Apps Security Authentication
primary: H
tags: [automotive, protocol, security, foreign-desk]
type: technology
status: active
seen_in: [bimmergestalt-idrive-refs, hu-probe, esp32-bt-analyzer]
maturity:
  technology: R2
  implementation: R2
  field_evidence: R3   # + FIELD_B3_GATEB_20261121 (Gate B CLOSED live APP_AUTH)
  reusability: W2
  evidence_scope: [LAB, FIELD]
```

Ebene **A** + F20-Feld. Desk: [`audits/bmw-connected-sas-auth-2026-11-06/`](../../audits/bmw-connected-sas-auth-2026-11-06/).  
SecurityAccess/CertMangling-Deep-Dive: [`audits/idriveconnectkit-securityaccess-2026-11-19/`](../../audits/idriveconnectkit-securityaccess-2026-11-19/).  
**Crypto CLOSED (2026-11-20):** Pad `0x02000000` · PKCS#1 v1.5 DigestInfo-MD5 · Wire Cert↔Sig 8/8.  
CASE A Signer: [`audits/libaudio-signchallenge-pipeline-2026-11-19/`](../../audits/libaudio-signchallenge-pipeline-2026-11-19/).  
**Gate B CLOSED (2026-11-21):** B3 profile relay — live MyBMW/AAIdrive Cert+Sig → `_result_sas_login` → RHMI/AM/CDS/AV (**FIELD FACT**; product `FIELD_B3_GATEB_20261121T112446Z`, commit `4d05169`).  
**Field Crypto CLOSED (2026-11-22):** **18/18** HU-akzeptierte Logins RSA-VERIFY gegen Wire-Leaf
`a4a_app_BMWTouchCommand_Connection_00.00.10` — Audit
[`bmw-sas-auth-field-crypto-2026-11-21`](../../audits/bmw-sas-auth-field-crypto-2026-11-21/)
(`SAS_CRYPTO_VERIFY.json`).  
**Standalone / reproduzierter Credential-Kontext** bleibt **OPEN** (nicht „Protokoll unbekannt“).  
Closure: [`docs/analysis/F20_BT_CONTROL_PLANE_CLOSURE_20261121.md`](../../docs/analysis/F20_BT_CONTROL_PLANE_CLOSURE_20261121.md) ·  
[`audits/nbt-evo-bt-control-plane-closure-2026-11-21/`](../../audits/nbt-evo-bt-control-plane-closure-2026-11-21/).  
Historisches Delta (pre-B3): [`docs/analysis/F20_CONNECTED_GAP_AUDIT_20261120.md`](../../docs/analysis/F20_CONNECTED_GAP_AUDIT_20261120.md).

## Kurzfassung

Nach BCL-Tunnel und Etch-Connect authentifiziert sich eine Connected App beim HU-Dienst
`BMWRemoting` über **SAS**: PKCS#7-Zertifikat bündeln → `sas_certificate` → Challenge →
Phone-seitige Signatur (`CarSecurityService` / SecurityModule) → `sas_login`.  
Danach erst RHMI/AV/CDS (**Authorization** und Resource-Hashes sind getrennt).

## Abgrenzung

- **Ist:** Auth-API, Cert-Rollen APP/APP_AUTH, Challenge/Response-Rollen, Phone Security.
- **Ist nicht:** BCL-Framing; AOA; RHMI-Widget-Semantik; USB-MSC.
- **Grenzt an:** [`bmw-etch-rpc`](../bmw-etch-rpc/SHEET.md), [`bmw-bcl`](../bmw-bcl/SHEET.md),
  [`bmw-rhmi`](../bmw-rhmi/SHEET.md), [`usb-aoa`](../usb-aoa/SHEET.md).

## Sequenz (Desk-FACT + Field)

```
sas_certificate(p7b) → challenge[16]
signChallenge (Phone Security) → response[512]   # RSA-4096 sig
sas_login(response) → void | SecurityException
```

**Zwei Phone-Pfade:** AAIdrive/Kit = eigener Etch-Client; CarAPI = Connected führt `sas_*`
stellvertretend aus (ContentProvider-Cert). Analysis Doc: Tunnel **nicht verschlüsselt**.

### Crypto (FIELD FACT — B3)

```
Pad16    = MD5(02 00 00 00)          # CertificateType APP_AUTH; ≠ serial 0x0AA9
X        = Challenge16 XOR Pad16
Digest16 = MD5(X)
Sig512   = RSA-4096-PKCS#1-v1.5(DigestInfo-MD5 || Digest16)
Verify   = Leaf CN=a4a_app_BMWTouchCommand_Connection_00.00.10
```

B3 counts: 12× cert · 19× challenge · **18× login / 18× accept / 18× VERIFY VALID**.  
Multi-Channel: parallele BCL `src`→dest 4004 mit unabhängigen Cert/Login-Sequenzen (**FIELD FACT**).

## Fallstricke

| Claim | Status |
|-------|--------|
| Simulator/Mock login = echte HU-Verifikation | `REJECTED` |
| AOA/BCL Capture = SAS Erfolg | `REJECTED` |
| Challenge immer 16 B auf allen HUs | `MEASURED` auf diesem F20 (`DEEP_FORENSIC_ETCH_SAS_20261116` + B3); andere HUs `UNKNOWN` |
| Response-Signatur 512 B (RSA-4096); Wire-Frame größer | `MEASURED` F20: 512-B Sig; B3 18× bestätigt |
| HS/KNOCK/ACK10 = SAS-Challenge | `REJECTED` — BCL-Transport ≠ Etch-SAS ([SecurityAccess-Audit](../../audits/idriveconnectkit-securityaccess-2026-11-19/)) |
| Lab/`f20_sim` Login = echte HU-Auth | `REJECTED` — FIELD AUTH REJECT 2026-11-18 = Standalone OPEN; ≠ „F20 kann kein SAS“ (Gate B CLOSED 2026-11-21) |
| Pad-u32 APP_AUTH = X509-Serial | `REJECTED` — Wire FACT `0x02000000` |
| MyBMW nötig für SAS-Protokollmathematik | `REJECTED` — Formel Wire-geschlossen; MyBMW bleibt Signer-Träger bis Standalone |
| RSA-VERIFY dieses B3-Captures pending | `SUPERSEDED` — 18/18 CLOSED (`bmw-sas-auth-field-crypto-2026-11-21`) |
| Ein Cert/Login genügt immer (Single-Channel Suffizienz) | `UNKNOWN` — B3 zeigt Multi-Channel; Minimum unbewiesen |
| USB und BT teilen SAS | `INFERENCE` (gleiche Etch-API) |

## Transfer

- Feld: FX-G3-01 in Audit-Report — Etch-Trace oder korrelierte Logs.
- ESP32: Framing sichtbar; Signaturerzeugung auf dem Phone unsichtbar.
- Keine Bypass-/Key-Extraktion in Sheets.

### Projektstart-Checkliste

- [ ] Gates G1–G4 nicht vermischen (Identity ≠ Transport ≠ SAS ≠ RHMI)
- [ ] SecurityService vs SecurityModule (Classic Binder vs MyBMW Module) klären
- [ ] Fake-HU-Erfolge nicht als Crypto-FACT werten
