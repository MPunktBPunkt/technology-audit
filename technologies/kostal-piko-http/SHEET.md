# Technology Sheet: Kostal PIKO HTTP

```yaml
slug: kostal-piko-http
title: Kostal PIKO Local HTTP Interface
primary: C
tags: [iot, http]
type: protocol
status: active
seen_in: [iobroker-kostalpiko]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/iobroker-kostalpiko-2026-pilot
```

Nur Ebene **A**. Adapter-Pfade → [`applications/kostal-piko-http.md`](../../projects/iobroker-kostalpiko/applications/kostal-piko-http.md).

## Kurzfassung

Kostal **PIKO**-Wechselrichter exponieren einen lokalen HTTP-Webserver mit Basic Auth: HTML-Seiten für Live-Werte und `LogDaten.dat` für 15‑min-Messreihen. Integration ohne Hersteller-Cloud möglich — Parsing muss Zeichensatz und Tabellen-Layout beachten.

## Abgrenzung

- **Ist:** Lokales HTTP-Gerät-Interface (Live HTML + Log-CSV).
- **Ist nicht:** Kostal Portal/Cloud-API; generisches Modbus/SunSpec (andere Produkte); ioBroker-Adapter-UI/Influx (Application B); fremde Adapter-Namen im Catalog.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Client → PIKO | `GET /index.fhtml`, `/Inf.fhtml` | Live; oft Basic Auth |
| Client → PIKO | `GET /LogDaten.dat` | Tab-separierte Historie |
| Encoding | windows-1252 / latin1 | falsch = Müllwerte |
| Gerät | oft nur **eine** HTTP-Verbindung gleichzeitig | Live vs. Log serialisieren |

## Typische Fallstricke (A)

| Claim | Status | Hinweis |
|-------|--------|---------|
| JSON-API ist Standard auf PIKO | `REJECTED` | HTML/CSV-Scraping |
| UTF-8 reicht für alle Seiten | `REJECTED` | latin1/windows-1252 |
| String- und Phasen-Zellen sind getrennte Zeilenblöcke | `REJECTED` | oft interleaved in einer Zeile |
| Parallel Live + LogDaten ist unkritisch | `REJECTED` | Gerät oft single-connection |
| Offline-Zellen (`x x x`) = Energie verloren | `REJECTED` | Energie-Zellen können weiter gültig sein |
| Jeder „kostal*“-Adapter teilt denselben Parser | `REJECTED` | Produkte/Repos trennen |

## Transfer

Für jedes Tool, das PIKO lokal ausliest (Adapter, Script, Grafana-Bridge). Modell-Unterschiede (2 vs. 3 Strings) in Application oder Config, nicht als Spec-Fork.

### Projektstart-Checkliste

- [ ] Auth + Encoding festlegen
- [ ] 2- vs. 3-String-Zellenmap dokumentieren
- [ ] Live/Log serialisieren; Nacht/Timeout-Policy
- [ ] Application + `seen_in`
- [ ] Catalog-Namen nicht mit Fremd-Adaptern vermengen

## Referenzen

- Hersteller: Kostal Solar Electric
- Adapter-Spec: [Schnittstellen.md](https://github.com/MPunktBPunkt/ioBroker.kostalpiko/blob/main/Schnittstellen.md)

## Offene Fragen

- Firmware-Varianten jenseits ver 3.62?
- Ob neuere PIKO-Generationen dasselbe HTML behalten?
