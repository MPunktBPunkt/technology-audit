# Technology Sheet: ioBroker Simple-API Client

```yaml
slug: iobroker-simple-api
title: ioBroker Simple-API Client
primary: F
tags: []
type: protocol
status: active
seen_in: [esp32-metermaster]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

HTTP-Client-Muster: ESP liest (und ggf. schreibt) ioBroker-States über die **Simple-API** (`getPlainValue` / verwandte Routen). Gut für bestehende States — ungeeignet, um State-Bäume erst anzulegen (Henne-Ei).

## Abgrenzung

- **Ist:** Lesen/Schreiben bereits existierender States per HTTP.
- **Ist nicht:** Adapter-eigenes Register/Config-API; MQTT; ESP-Hub `/api/register`.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Simple-API kann nodes.* vor Registrierung anlegen | `REJECTED` | Adapter-Register zuerst |
| Ein Port für alles (Werte + Config + Hub) | `REJECTED` | oft 8087 / adapter / 8093 getrennt |
| ESP ist HTTP-Server für ioBroker | `HYPOTHESIS` | typisch ESP = Client, pollt |

### Projektstart-Checkliste

- [ ] Welche States schon existieren?
- [ ] Separater Adapter-HTTP für Register/Config?
- [ ] Poll-Intervalle / Fehlerpfade
- [ ] Application + `seen_in`

## Referenzen

- ioBroker simple-api Adapter
- Beispiel: MeterMaster `docs/DATENAUSTAUSCH.md`

## Offene Fragen

- Auth-Varianten der Simple-API in LAN-only Setups?
