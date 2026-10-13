# Method: Plug Power / Reset Isolation

```yaml
slug: plug-power-reset-isolation
title: Plug Power / Reset Isolation
status: active
tags: [power, reset, usb, hardware, preregistered]
```

## Zweck

Brownout, VBUS-Umschaltung, Masseausgleich, externen Reset und
Software-Watchdog beim Stecken unterscheiden. Verhindert, dass ein Device-
Reset fälschlich als HU-Cache- oder MediaStore-Verhalten gewertet wird.

## Voraussetzungen

- UART-/Bootreason-Capture ohne automatische DTR/RTS-Resetwirkung
- geeignetes Oszilloskop oder Min/Max-Erfassung für VBUS und lokale Rail
- gemeinsamer Plug-Marker; definierte Masse- und Versorgungsführung
- alternative Versorgung und geeigneter VBUS-Blocker/Power-Isolator

## Ablauf

1. Instrumentierung ohne Stecken verifizieren; insbesondere ausschließen,
   dass der UART-Adapter selbst Reset auslöst.
2. Baseline mit nur einer Versorgung und dokumentierter Kabel-/Masseführung
   erfassen.
3. Plug-Matrix einzeln fahren: Busversorgung, alternative Versorgung,
   gemeinsame Versorgung mit VBUS blockiert sowie kontrollierte
   Masse-Reihenfolge.
4. Je Lauf VBUS/lokale Rail, Resetleitung, UART-Bootreason, USB-
   Disconnect/Reconnect und Watchdogmarker auf einer Zeitachse erfassen.
5. Jede Resetklasse reproduzieren und mit einem absichtlich ausgelösten
   Brownout-/Watchdog-/External-Reset-Kontrast vergleichen, sofern sicher.
6. Erst nach elektrischem Gate einen getrennten HU-Lifecycle-Lauf bewerten.

## Artefakte

- Plug-Matrix mit Verdrahtung, Versorgung, Kabel und Bootreason
- Scope-/MinMax-Capture mit Zeitbezug zu UART und USB
- Klassifikation `brownout`, `watchdog`, `external`, `power-on` oder `UNKNOWN`
- Evidence erst im ausführenden Audit

## Präregistrierte Gates

| Gate | Pass | Fail | Kill / Stop |
|------|------|------|-------------|
| P1 Instrumentierung | UART/Probe verändert Resetpfad nachweislich nicht | DTR/RTS oder Probe löst Reset aus | keine Fahrzeuginterpretation |
| P2 Elektrische Korrelation | Rail-Ereignis und Bootreason stimmen reproduzierbar überein | Marker fehlen/widersprechen | Ursache `UNKNOWN` |
| P3 Isolationsmatrix | genau eine Versorgungs-/VBUS-Bedingung geändert | Verdrahtung und Software zugleich geändert | Lauf verwerfen |
| P4 HU-Abgrenzung | HU-Cachetest erfolgt ohne Device-Reset | Reset im Cachelauf | Cache-/Lifecycle-Claim stoppen |

## Sicherheit / Fallstricke

- Keine Fahrzeugleitungen kurzschließen; geeignete Isolation und
  Messkategorie verwenden.
- VBUS-Blocker darf Datenmasse/-leitungen nicht unkontrolliert referenzlos
  machen.
- Ein Bootlog ohne Rail-Capture unterscheidet Ursache und Folge oft nicht.
- Kein Code-, Flash- oder RF-Schritt ist Bestandteil dieser Methode.

## Beispiel-Einsatz

[`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/) — HU-A11,
präregistriert und noch `UNKNOWN`.
