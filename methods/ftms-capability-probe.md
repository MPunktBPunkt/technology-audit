# Method: FTMS Capability Probe

```yaml
slug: ftms-capability-probe
title: FTMS Capability Probe
status: active
tags: [lab, bluetooth, ftms]
```

## Zweck

Vor dem Bau einer Coach-/Bridge-Firmware feststellen, **was** ein Indoor-Bike über FTMS wirklich kann — Features, Ranges, Wirkungsopcodes, Advertising-Tücken — ohne Annahmen aus Marketing oder Spec-Ideal.

## Voraussetzungen

- BLE-Central am gleichen Stack wie die spätere Produktsfirmware (nicht nur Host-BlueZ im Container)
- HTTP-steuerbare Sonde oder gleichwertiges Lab-Setup (Beispielimplementierung: [`esp32.ftmsprobe`](https://github.com/MPunktBPunkt/esp32.ftmsprobe))
- Möglichkeit zu treten (Kadenz) für Wirkungsmessung
- Nur **ein** Central gleichzeitig am Bike (nRF Connect / Trainer-Apps aus)

## Ablauf

1. **Scan** — Advertising erfassen (Name, MAC, AddrType, Services); Lücken dokumentieren.
2. **GATT** — vollständigen Attributbaum speichern (`0x1826` und Nachbarn).
3. **Read** — `0x2ACC`, `0x2AD6`, `0x2AD8` (falls vorhanden), Device Info; Features auswerten.
4. **Bike Data** — Notify `0x2AD2`: Ruhe vs. Trittphase (Nullen ohne Kadenz erwarten).
5. **Control + Wirkung** — Resistance-Varianten (z. B. uint8 vs. sint16 Zehntel) schreiben; vor/nach Mittelwerte aus IBD (Power/Resistance); subjektiv nur Zusatz.
6. **Dual** (optional) — Bike + HR-Gurt parallel; Verbindungsbudget prüfen.
7. **Report** — verdichteter Ergebnisbericht + Rohartefakte verlinken; Steuerstrategie ableiten (direktes Watt / Resistance-Emulation / nur Dashboard).

## Artefakte

| Artefakt | Inhalt |
|----------|--------|
| `adv.json` / Scan-Log | Advertising |
| `gatt.json` | Attributbaum |
| `reads.json` / Feature-Hex | Caps |
| `bike-data.jsonl` | IBD-Notifies |
| `effects.json` / control log | Wirkungsbelege |
| Ergebnisbericht | verdichtete Claims für Evidence-IDs |

Naming-Beispiel: `docs/…/scan-<YYYYMMDD>/` im Sonden-Repo.

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| FTMS vorhanden | `0x1826` im GATT | nur Vendor-UUID ohne brauchbaren Control |
| Steuerstrategie wählbar | aus Caps + Wirkungsmessung begründet | nur „fühlt sich an“ |
| Success ≠ Wirkung | widersprüchliche Success dokumentiert | Success als Beweis übernommen |
| Rohdaten | exportiert und verlinkt | nur UI-Screenshot |

## Fallstricke

- Host-Bluetooth aus LXC oft unbrauchbar — Sonde am Ziel-Funkstack bevorzugen.
- Mitten in Messung OTA/Flash → Lauf ungültig (Deadman/Guard).
- Konsolendisplay am Bike oft aus während Link — UI der Sonde ist die Anzeige.
- Marketing-Watt/Stufen ≠ FTMS-Raster.

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| `esp32-ftmsprobe` | Implementierung + Varon-Lauf 2026-09-10 |
| `esp32-ergo` | Folge: Capability-first `FtmsClient` / GERAETEPROFIL |
| Sheet `bluetooth-ftms` | Fallstricke A speisen |
