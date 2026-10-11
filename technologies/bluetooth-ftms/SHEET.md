# Technology Sheet: Bluetooth FTMS (Fitness Machine)

```yaml
slug: bluetooth-ftms
title: Bluetooth FTMS (Fitness Machine)
primary: C
tags: [esp-idf, streaming]
type: protocol
status: active
seen_in: [esp32-ftmsprobe, esp32-ergo]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Konkrete Trainer (z. B. Varon) und App-Bridges → Applications / Host-Sheets.  
**Chip-Scope:** GATT-Profil ist chip-neutral. **Dual-Role** (Central zum Bike + Peripheral-Bridge zur App) ist controller-/build-abhängig — in der Ergo-Familie belegt auf **ESP32-S3**, nicht still auf Classic übertragen (G17).

## Kurzfassung

Bluetooth LE Fitness Machine Service (`0x1826`): Features (`0x2ACC`), Indoor Bike Data (`0x2AD2`), Control Point (`0x2AD9`), optionale Ranges (`0x2AD6` Resistance, `0x2AD8` Power). Clients steuern Trainer; Peripherals können FTMS nach außen spiegeln (Bridge zu Zwift/MyWhoosh o. Ä.).

## Abgrenzung

- **Ist:** GATT-Profil für Indoor-Trainer / Fitnessgeräte (Messwerte + Sollwerte).
- **Ist nicht:** Heart Rate Service (`0x180D`); herstellerspezifische Vendor-UUIDs; Trainingslogik (ERG-Regler, Zonen) — die sitzt darüber; automatische Dual-Role-Bridge auf jedem ESP32.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Coach-App / Bridge / Regler | Watt, Stufe, Sim, IBD-Metriken |
| unten | BLE Stack | Central und/oder Peripheral |
| lateral | Capability-Ableitung | Strategie aus Features + Ranges + beobachteten Flags |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Jeder „Smart Trainer“ unterstützt Set Target Power (`0x05`) | `REJECTED` | Target-Bits in `0x2ACC` und Präsenz von `0x2AD8` prüfen |
| Control-Point-Success beweist Wirkung | `REJECTED` | Geräte quittieren teils Ops, die sie nicht ausführen |
| Resistance immer 1-Byte | `REJECTED` | Breite (sint16 Zehntel) geräteabhängig; Wirkungstest nötig |
| `0x2AD9` ist immer Indicate | `HYPOTHESIS` | Manche Geräte Notify statt Indicate — CCCD `0x0001` |
| Feature-Bit „Resistance“ ⇒ IBD liefert Resistance-Feld | `REJECTED` | Bits und Payload-Felder können auseinanderlaufen |
| Advertising enthält zuverlässig Name/Services | `HYPOTHESIS` | Manche Bikes nur über gemerkte MAC + AddrType reconnectbar |
| FTMS-Bridge+Central auf Classic wie auf S3 | `UNKNOWN` / Gate | Connection-Budget; Ergo-Produkt = S3 |

## Steuerstrategien (A)

| Strategie | Voraussetzung | Typischer Fallback |
|-----------|---------------|--------------------|
| Direktes Wattziel | Target Power + belastbare Power Range | — |
| Emulation über Resistance | Resistance Target wirkt; Power Target fehlt/ungut | Kennfläche Stufe→Watt, Regler im Client |
| Nur Dashboard | Keine belastbare Stellgröße | Lesen von IBD, keine Last |

Capabilities zur Connect-Zeit ableiten — nicht als Firmware-Konstanten „dieses eine Bike“ hardcoden, wenn Transferziel mehrere Geräte sind.

## Transfer

Wiederverwendbar für ESP-Central (Bike) und ESP-Peripheral (App-Bridge). Probe-/Scan-Repos (Capability-Messung) vor Coach-Logik trennen. Host-Quirks (konkretes Bike) nicht still als Spec behandeln.

### Projektstart-Checkliste

- [ ] Method [`ftms-capability-probe`](../../methods/ftms-capability-probe.md) gelesen (oder gleichwertiger Lab-Lauf)
- [ ] Zur Connect-Zeit: `0x2ACC` / `0x2AD6` / `0x2AD8` / IBD-Flags → Steuerstrategie wählen
- [ ] Success auf Control Point **nicht** als Wirkungsbeweis behandeln
- [ ] Host-Quirks (Advertising, Notify-vs-Indicate, fehlende Felder) in Application C / Host-Sheet, nicht hier als Spec
- [ ] Wenn Resistance-only: Kennfläche/Emulation planen — kein stilles Hardcode „alle Bikes können ERG“
- [ ] Bei Bridge: Chip-Scope / Dual-Role-Budget prüfen (Familie: S3)
- [ ] `seen_in` + Application nachziehen

## Referenzen

- Bluetooth Fitness Machine Service / Indoor Bike Profile (SIG)
- Method: [`ftms-capability-probe`](../../methods/ftms-capability-probe.md)
- Projektmessungen als Evidence in Ursprungsrepos (nicht hier roh spiegeln)

## Offene Fragen

- Wie häufig ist Notify-statt-Indicate auf `0x2AD9` außerhalb einzelner ASR/Varon-Geräte?
- Gute Defaults für ERG-Slew bei Resistance-Emulation (zyklusübergreifend)?
