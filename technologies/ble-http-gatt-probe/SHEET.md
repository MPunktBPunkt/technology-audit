# Technology Sheet: HTTP-gesteuerte BLE-GATT-Sonde

```yaml
slug: ble-http-gatt-probe
title: HTTP-gesteuerte BLE-GATT-Sonde
primary: H
tags: [esp-idf, lab-only]
type: pattern
status: active
seen_in: [esp32-ftmsprobe]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
```

Nur Ebene **A**. Konkrete API-Routen und Scan-Ordner → Application.

## Kurzfassung

Lab-Muster: ein ESP (oder gleichwertig) exponiert BLE-Central-Operationen (Scan, Connect, GATT-Dump, Read/Write/Subscribe, Log-Export) über HTTP/SSE, damit Analyse und Automatisierung aus einem Container/CLI laufen können, ohne Host-HCI im Namespace.

## Abgrenzung

- **Ist:** Fernsteuerbarer GATT-Explorer / Probe am Produkt-Funkstack.
- **Ist nicht:** Produkt-Coach-UI; dauerhafter Peripheral-Service; Ersatz für Spec-Kenntnis.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | CLI / Cursor / Hub-OTA | HTTP JSON, Artefakt-Export |
| unten | NimBLE (o. Ä.) Central | Scan, Links, CCCD |
| lateral | Deadman / Panic | Messung nicht „hängen“ lassen |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| BlueZ im LXC reicht für Geräte-Lab | `REJECTED` | oft kein HCI; Standort der Antenne falsch |
| OTA während offener Links ist harmlos | `REJECTED` | Lauf ungültig; Guard/Ablehnung sinnvoll |
| Subjektives „zieht an“ ersetzt Wirkungsmessung | `REJECTED` | IBD vor/nach + Rohbytes |
| Probe-Code darf beliebige Product-API brechen | `HYPOTHESIS` | Pin gleiche BLE-Lib-Major wie Produktlinie |

## Transfer

Einsetzen wenn: (1) Lab-Automatisierung ohne Desktop-nRF, (2) gleicher BLE-Stack wie Produktion, (3) wiederholbare Capability-/Wirkungsläufe. Verfahren: Method `ftms-capability-probe` (FTMS) oder analoge Checkliste für andere GATT-Profile.

### Projektstart-Checkliste

- [ ] Zielprofil (FTMS, HR, …) und Method Note gewählt
- [ ] Connection-Budget wie Produkt testen
- [ ] Exportformat für Evidence festgelegt (JSON/NDJSON + Bericht)
- [ ] Panic/Not-Stop und Deadman spezifizieren
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Method: [`ftms-capability-probe`](../../methods/ftms-capability-probe.md)
- Beispielrepo: [esp32.ftmsprobe](https://github.com/MPunktBPunkt/esp32.ftmsprobe)

## Offene Fragen

- Wie generisch lässt sich die Probe-API über FTMS hinaus halten (Profil-Plugins)?
