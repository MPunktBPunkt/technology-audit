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
  field_evidence: R2   # F20 DEEP_FORENSIC_ETCH_SAS_20261116 + AUTH_REJECT_20261118
  reusability: W2
  evidence_scope: [desk-bg, f20-field-2026-11]
```

Ebene **A** + F20-Feld. Desk: [`audits/bmw-connected-sas-auth-2026-11-06/`](../../audits/bmw-connected-sas-auth-2026-11-06/).  
SecurityAccess/CertMangling-Deep-Dive: [`audits/idriveconnectkit-securityaccess-2026-11-19/`](../../audits/idriveconnectkit-securityaccess-2026-11-19/).  
**Gate lokalisiert ≠ Response gelöst** — Schlüsselort A–D: [`audits/signchallenge-pipeline-localize-2026-11-19/`](../../audits/signchallenge-pipeline-localize-2026-11-19/).

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

## Sequenz (Desk-FACT)

```
sas_certificate(p7b) → challenge[]
signChallenge (Phone Security) → response[]
sas_login(response) → void | SecurityException
```

**Zwei Phone-Pfade:** AAIdrive/Kit = eigener Etch-Client; CarAPI = Connected führt `sas_*`
stellvertretend aus (ContentProvider-Cert). Analysis Doc: Tunnel **nicht verschlüsselt**.

## Fallstricke

| Claim | Status |
|-------|--------|
| Simulator/Mock login = echte HU-Verifikation | `REJECTED` |
| AOA/BCL Capture = SAS Erfolg | `REJECTED` |
| Challenge immer 16 B auf allen HUs | `MEASURED` auf diesem F20 (`DEEP_FORENSIC_ETCH_SAS_20261116`); andere HUs `UNKNOWN` |
| Response-Signatur 512 B (RSA-4096); Wire-Frame größer | `MEASURED` F20: 512-B Sig in 559-B `sas_login`-Frame |
| HS/KNOCK/ACK10 = SAS-Challenge | `REJECTED` — BCL-Transport ≠ Etch-SAS ([SecurityAccess-Audit](../../audits/idriveconnectkit-securityaccess-2026-11-19/)) |
| Lab/`f20_sim` Login = echte HU-Auth | `REJECTED` — FIELD AUTH REJECT 2026-11-18 |
| USB und BT teilen SAS | `INFERENCE` (gleiche Etch-API) |

## Transfer

- Feld: FX-G3-01 in Audit-Report — Etch-Trace oder korrelierte Logs.
- ESP32: Framing sichtbar; Signaturerzeugung auf dem Phone unsichtbar.
- Keine Bypass-/Key-Extraktion in Sheets.

### Projektstart-Checkliste

- [ ] Gates G1–G4 nicht vermischen (Identity ≠ Transport ≠ SAS ≠ RHMI)
- [ ] SecurityService vs SecurityModule (Classic Binder vs MyBMW Module) klären
- [ ] Fake-HU-Erfolge nicht als Crypto-FACT werten
