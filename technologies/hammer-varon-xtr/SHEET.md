# Technology Sheet: Hammer Varon XTR II (FTMS Host)

```yaml
slug: hammer-varon-xtr
title: Hammer Varon XTR II (FTMS Host)
primary: I
tags: [field-verified]
type: technology
status: active
seen_in: [esp32-ftmsprobe, esp32-ergo]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
  evidence_scope: [LAB, FIELD, DEVICE-SPECIFIC]
```

Ebene **A nur soweit geräteklasse-übergreifend nutzbar**; die meisten Aussagen sind **gerätetypisch** und gehören primär in die Project Application / Evidence. Dieses Sheet hält die verdichteten, wiederkehrenden Quirks des Varon-Profils, damit sie nicht in `bluetooth-ftms` als Spec wandern.

## Kurzfassung

Indoor-Bike „Hammer Varon XTR II“ (BLE-Name oft `TC174`, Hersteller `ASR`): FTMS mit Resistance Target und Simulation, **ohne** Set Target Power / ohne `0x2AD8`. Wattsteuerung nur über Stufen-Emulation.

## Abgrenzung

- **Ist:** Konkretes Geräteprofil / Host-Verhalten unter FTMS.
- **Ist nicht:** Die FTMS-Spec selbst (`bluetooth-ftms`); Coach-/Regellogik.

## Typische Fallstricke (gerätetypisch)

| Claim | Status | Hinweis |
|-------|--------|---------|
| Marketing-Stufen/Watt = FTMS-Raster | `REJECTED` | Über FTMS ~16 Stufen (0,1er), nicht 41 / 20–400 W-Marketing |
| Opcode `0x05` Success ⇒ Wattziel aktiv | `REJECTED` | Success ohne Feature; produktiv sperren |
| Advertising allein reicht zum Wiederfinden | `REJECTED` | MAC + AddrType merken; Scan oft ohne Name/Services |
| Resistance-Feld in IBD spiegelt Ist-Stufe | `REJECTED` | Feature-Bit ja, IBD-Feld typisch nein |

## Transfer

Nützlich als Negativ-/Positivbeispiel für Capability-first-Clients. Andere ASR/ähnliche Konsolen ggf. vergleichen — nicht pauschal auf alle Indoor-Bikes übertragen. Zweites Gerät = Method erneut fahren, **kein** Ausweiten dieses Sheets zum Universal-Trainer (G19).

### Projektstart-Checkliste

- [ ] Als Host-Sheet nutzen, nicht FTMS-Spec erweitern
- [ ] Caps/Wirkung aus Method `ftms-capability-probe` oder Evidence zitieren
- [ ] Marketing-Watt/Stufen ≠ FTMS-Raster
- [ ] Neues Bike ≠ dieses Sheet verbiegen — neues Host-Sheet oder Application-C
- [ ] Application + `seen_in` nachziehen

## Referenzen

- Messungen: `esp32.ftmsprobe` Scan-Artefakte; `esp32.ergo` `docs/ergometer/GERAETEPROFIL.md`

## Offene Fragen

- Weitere Firmware-Revisions des gleichen Gehäuses mit abweichendem `2ACC`?
