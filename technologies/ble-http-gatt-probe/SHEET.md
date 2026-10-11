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
pilot: audits/esp32-ftmsprobe-2026-pilot
```

Nur Ebene **A**. Konkrete API-Routen und Scan-Ordner → Application.  
**Chip-Scope:** Pattern ist spezseitig chip-neutral (HTTP↔BLE-Central). **Connection-Budget** (z. B. Bike+HR parallel) und Firmware-Familien (`probe` Classic vs `probe-s3`) sind **build-/chip-gebunden** — nicht still von einem Env auf alle ESP32 übertragen (G17).

## Kurzfassung

Lab-Muster: ein ESP (oder gleichwertig) exponiert BLE-Central-Operationen (Scan, Connect, GATT-Dump, Read/Write/Subscribe, Log-Export) über HTTP/SSE, damit Analyse und Automatisierung aus einem Container/CLI laufen können, ohne Host-HCI im Namespace.

## Abgrenzung

- **Ist:** Fernsteuerbarer GATT-Explorer / Probe am Produkt-Funkstack.
- **Ist nicht:** Produkt-Coach-UI; dauerhafter Peripheral-Service; Ersatz für Spec-Kenntnis; Annahme gleiches Dual-Link-Budget auf jedem ESP32-Env.

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
| Dual-Link-Budget eines Envs gilt für alle ESP32 | `REJECTED` (als FACT) | Classic vs S3 / `MAX_CONNECTIONS` pro Build belegen |
| Probe-Peripheral „wie Ergo-Bridge“ ohne Umbau | `REJECTED` | typisch Central-only; Bridge = anderes Chip-/Rollen-Budget |

## Transfer

Einsetzen wenn: (1) Lab-Automatisierung ohne Desktop-nRF, (2) gleicher BLE-Stack wie Produktion, (3) wiederholbare Capability-/Wirkungsläufe. Verfahren: Method `ftms-capability-probe` (FTMS) oder analoge Checkliste für andere GATT-Profile. Geschwister: Evidence → `esp32-ergo` Host/FTMS-Sheets.

### Projektstart-Checkliste

- [ ] Zielprofil (FTMS, HR, …) und Method Note gewählt
- [ ] Chip/Env + Connection-Budget wie Produkt testen (Classic vs S3)
- [ ] Exportformat für Evidence festgelegt (JSON/NDJSON + Bericht)
- [ ] Panic/Not-Stop und Deadman spezifizieren
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Method: [`ftms-capability-probe`](../../methods/ftms-capability-probe.md)
- Beispielrepo: [esp32.ftmsprobe](https://github.com/MPunktBPunkt/esp32.ftmsprobe)

## Offene Fragen

- Wie generisch lässt sich die Probe-API über FTMS hinaus halten (Profil-Plugins)?
