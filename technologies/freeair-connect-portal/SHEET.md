# Technology Sheet: freeAir Connect Portal

```yaml
slug: freeair-connect-portal
title: bluMartin freeAir Connect Portal
primary: F
tags: [iot, cloud]
type: protocol
status: active
seen_in: [iobroker-freeair100]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W1
pilot: audits/iobroker-freeair100-2026-pilot
```

Nur Ebene **A**.

## Kurzfassung

Cloud-Portal **freeair-connect.de** für bluMartin freeAir-Lüftung: SSR-HTML mit Live-Kennzahlen; zusätzliche Minutenreihen können **AES-verschlüsselt** geliefert werden. Integration = Poll + Parse (+ ggf. Decrypt), kein lokales Geräte-API-Pflicht.

## Abgrenzung

- **Ist:** Portal-HTTP/HTML (und optionale encrypted values).
- **Ist nicht:** lokales Modbus/BACnet am Gerät; generisches Lüftungs-Sheet; Adapter-UI.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Portal braucht Login-Token | `REJECTED` | Serial-URL oft öffentlich scrape-bar |
| HTML-Keys sind stabil über Firmware | `HYPOTHESIS` | Regex-Parser brüchig |
| AES-Payload ohne Key nutzbar | `REJECTED` | Decrypt nötig |
| Cloud-Poll = lokales LAN-Gerät | `REJECTED` | Abhängigkeit Portal/Internet |

### Projektstart-Checkliste

- [ ] Serial/Auth-Modell klären
- [ ] HTML vs. encrypted values trennen
- [ ] Rate-Limits / UA-Policy
- [ ] Application + `seen_in`

## Referenzen

- https://www.freeair-connect.de · Adapter iobroker.freeair100
