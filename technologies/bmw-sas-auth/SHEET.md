# Technology Sheet: BMW SAS Authentication (Connected Apps)

```yaml
slug: bmw-sas-auth
title: BMW SAS — Connected Apps Security Authentication
primary: H
tags: [automotive, protocol, security, foreign-desk]
type: technology
status: active
seen_in: [bimmergestalt-idrive-refs, hu-probe]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
  evidence_scope: []
```

Ebene **A** (Desk aus Fremdquellen). **Keine** eigenen SAS-Wire-Captures.
Vollaudit: [`audits/bmw-connected-sas-auth-2026-11-06/`](../../audits/bmw-connected-sas-auth-2026-11-06/).

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

## Fallstricke

| Claim | Status |
|-------|--------|
| Simulator/Mock login = echte HU-Verifikation | `REJECTED` |
| AOA/BCL Capture = SAS Erfolg | `REJECTED` |
| Challenge immer 16 B auf allen HUs | `INFERENCE` (observed) |
| Response immer 512 B | `INFERENCE` (Classic path); Dev-Key Tests 192 B |
| USB und BT teilen SAS | `INFERENCE` (gleiche Etch-API) |

## Transfer

- Feld: FX-G3-01 in Audit-Report — Etch-Trace oder korrelierte Logs.
- ESP32: Framing sichtbar; Signaturerzeugung auf dem Phone unsichtbar.
- Keine Bypass-/Key-Extraktion in Sheets.

### Projektstart-Checkliste

- [ ] Gates G1–G4 nicht vermischen (Identity ≠ Transport ≠ SAS ≠ RHMI)
- [ ] SecurityService vs SecurityModule (Classic Binder vs MyBMW Module) klären
- [ ] Fake-HU-Erfolge nicht als Crypto-FACT werten
