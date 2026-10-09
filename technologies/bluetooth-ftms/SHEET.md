# Technology Sheet: Bluetooth FTMS (Fitness Machine)

```yaml
slug: bluetooth-ftms
title: Bluetooth FTMS (Fitness Machine)
primary: C
tags: [esp-idf, streaming]
type: protocol
status: active
seen_in: [esp32-ergo]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
```

Nur Ebene **A**. Konkrete Trainer (z. B. Varon) und App-Bridges → Applications / Host-Sheets.

## Kurzfassung

Bluetooth LE Fitness Machine Service (`0x1826`): Features (`0x2ACC`), Indoor Bike Data (`0x2AD2`), Control Point (`0x2AD9`), optionale Ranges (`0x2AD6` Resistance, `0x2AD8` Power). Clients steuern Trainer; Peripherals können FTMS nach außen spiegeln (Bridge zu Zwift/MyWhoosh o. Ä.).

## Abgrenzung

- **Ist:** GATT-Profil für Indoor-Trainer / Fitnessgeräte (Messwerte + Sollwerte).
- **Ist nicht:** Heart Rate Service (`0x180D`); herstellerspezifische Vendor-UUIDs; Trainingslogik (ERG-Regler, Zonen) — die sitzt darüber.

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

## Steuerstrategien (A)

| Strategie | Voraussetzung | Typischer Fallback |
|-----------|---------------|--------------------|
| Direktes Wattziel | Target Power + belastbare Power Range | — |
| Emulation über Resistance | Resistance Target wirkt; Power Target fehlt/ungut | Kennfläche Stufe→Watt, Regler im Client |
| Nur Dashboard | Keine belastbare Stellgröße | Lesen von IBD, keine Last |

Capabilities zur Connect-Zeit ableiten — nicht als Firmware-Konstanten „dieses eine Bike“ hardcoden, wenn Transferziel mehrere Geräte sind.

## Transfer

Wiederverwendbar für ESP-Central (Bike) und ESP-Peripheral (App-Bridge). Probe-/Scan-Repos (Capability-Messung) vor Coach-Logik trennen. Host-Quirks (konkretes Bike) nicht still als Spec behandeln.

## Referenzen

- Bluetooth Fitness Machine Service / Indoor Bike Profile (SIG)
- Projektmessungen als Evidence in Ursprungsrepos (nicht hier roh spiegeln)

## Offene Fragen

- Wie häufig ist Notify-statt-Indicate auf `0x2AD9` außerhalb einzelner ASR/Varon-Geräte?
- Gute Defaults für ERG-Slew bei Resistance-Emulation (zyklusübergreifend)?
