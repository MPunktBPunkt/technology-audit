# Technology Sheet: Semantic GATT Bridge

```yaml
slug: ble-gatt-semantic-bridge
title: Semantic GATT Bridge (Profile A → B)
primary: C
tags: [esp-idf, nimble]
type: pattern
status: active
seen_in: [ble-gatt-bridge-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Konkrete Profile (FTMS, CPS, HID, Custom) → eigene Protokoll-Sheets / Applications.

## Kurzfassung

Bridge **re-encodiert** oder mappt zwischen zwei GATT-Profilen bzw. Protokoll-Semantiken (z. B. FTMS Indoor Bike Data → CPS Measurement; Custom Vendor → FTMS; proprietäres HID → Standard-HID). Downstream sieht ein **erwartetes** Profil — nicht die Upstream-Bytes. Optional: Control-Point-Transaktionen und Exclusive Control.

## Abgrenzung

- **Ist:** Profilwechsel / semantisches Mapping + ggf. CP-Routing.
- **Ist nicht:** Byte-Passthrough (`ble-gatt-transparent-bridge`); reines HR-Fanout desselben Service (`ble-hr-relay`); Trainingsregler-Logik (sitzt darüber).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| Upstream | Quell-Profil (Central) | Notify und/oder Poll-Read |
| Downstream | Ziel-Profil (Peripheral) | Notify/Indicate + optionale Writes |
| lateral | Control Point | Request → Indicate Result → Wirkung Upstream |

## Interaktionsmodelle

| Modell | Kennzeichen | Beispiel-Signal |
|--------|-------------|-----------------|
| Notify Fan-Out (gleiches Profil) | gleiche UUID/Payload | → eher `ble-hr-relay` |
| Semantic Notify Map | Flags/Felder neu packen | FTMS→CPS |
| Control-Point Proxy | Write + Indicate Result | FTMS CP / HOGP CP |
| Exclusive Control | ein Controller „besitzt“ Upstream | App vs Coach Lock |
| Poll-instead-of-Notify | Upstream ohne Notify | periodisches Read→Notify |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Gleiche Physik-Größe ⇒ byte-identische Characteristic | `REJECTED` | Flags/optionale Felder profilabhängig |
| Control-Point Success = Wirkung am Gerät | `REJECTED` | siehe `bluetooth-ftms` |
| Multi-Client + Exclusive ohne Lock-Policy | `REJECTED` | Bridge Exclusive vs Observer |
| Upstream-Notify immer vorhanden | `HYPOTHESIS` | ggf. Poll-Loop |
| Semantic Bridge braucht Transparent-Clone | `REJECTED` | oft nur Ziel-Services exposen |
| CPS/CSC-Felder „einfach weglassen“ | `HYPOTHESIS` | Consumer (Watch/App) können hart filtern |

## Transfer

Folgeprojekt: zuerst **Ziel-Profil der App** und **Upstream-Fähigkeit** klären, dann Mapping-Tabelle (Felder, Einheiten, synthetische Felder wie Crank-Revs). Dual-Role → `ble-gatt-dual-role`. FTMS-Details → `bluetooth-ftms`.

### Projektstart-Checkliste

- [ ] Upstream-Profil + Downstream-Profil spezifiziert
- [ ] Feld-Mapping inkl. synthetischer Ableitungen
- [ ] Control Point? Indicate-Pfad + Fehlercodes
- [ ] Exclusive vs Multi-Client Policy
- [ ] Notify vs Poll Upstream
- [ ] Dual-Role-Checkliste
- [ ] Application + `seen_in`

## Referenzen

- iFitnessProxy FTMS→CPS
- ifit Custom→FTMS + CP handlers
- BleRemoteBrideg HID semantic + FSM
- esp32.ergo FTMS Peripheral Bridge

## Offene Fragen

- Einheitliches Exclusive-Control-Muster über Profile hinweg?
- Wann synthetische CPS-Crank-Felder Watch-tauglich genug?
