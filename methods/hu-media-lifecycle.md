# Method: HU Media Lifecycle Isolation

```yaml
slug: hu-media-lifecycle
title: HU Media Lifecycle Isolation
status: active
tags: [usb-msc, automotive, lifecycle, cache, preregistered]
```

## Zweck

Media-Hide, Soft-Detach und physischen Replug als verschiedene Ereignisse
behandeln und ihre Wirkung auf HU-Medienzustand, Index, Auswahl- und
Startklasse reproduzierbar bestimmen. Die Methode deckt HU-A9 ab und liefert
definierte Warm-/Cold-Bedingungen für nachgelagerte Cache-, Resume- und
AV-Tests. Nicht ausgeführte Klassen bleiben `UNKNOWN`.

Die Methode beobachtet Device-/Stack- und HU-nahe Artefakte. Sie erzeugt ohne
separaten, validierten USB-Capture keine Wire-Claims.

## Ereignis- und Zustandsklassen

| Klasse | Operative Definition | Typische Grenze | Nicht automatisch belegt |
|--------|----------------------|----------------|--------------------------|
| `MH` Media-Hide | Medium/Inhalt wird logisch verborgen und wieder sichtbar; USB-Attach, Device-Boot und Versorgung bleiben nach Instrumentierung unverändert | neue Media-Visibility-Epoch | USB-Re-Enumeration, HU-Cache-Löschung |
| `SD` Soft-Detach | Device-Stack löst softwareseitig Detach/Attach aus; kein physischer Steckvorgang und kein Device-Boot | neue USB-Mount-/Attach-Epoch | elektrische Trennung, HU-Cold-State |
| `PR` physischer Replug | Stecker oder definierter Datenpfad wird physisch getrennt und wieder verbunden | neue Physical-Plug-Epoch; weitere Grenzen messen | Device-Reset, Power-Cycle oder Cache-Löschung |

**Warm/Cold sind Ergebnisbedingungen, keine Synonyme für ein Ereignis:**

- `W0` — gleiche HU-Session, gleiche USB-Mount-Epoch; nur `MH`.
- `W1` — gleiche HU-Session und gleicher Device-Boot, aber neue
  USB-Mount-/Attach-Epoch durch `SD`.
- `C-USB` — physische Plug-Grenze belegt; Device-Boot/Versorgung können gleich
  oder neu sein und werden separat angegeben.
- `C-DEV` — neuer Device-Boot oder belegter Device-Power-Cycle.
- `C-HU` — vorab definierte HU-Cold-Precondition erfüllt, etwa ein unabhängig
  beobachtetes Ende der HU-Session. Zündung aus oder eine Wartezeit allein
  belegt `C-HU` nicht.

Jeder Lauf führt getrennte Epoch-Zähler für `media_visibility`,
`usb_mount_attach`, `device_boot`, `physical_plug` und `hu_session`. Eine
Grenze setzt die anderen Zähler nicht implizit zurück.

## Voraussetzungen

- stabile Baseline mit fester Medium-Identity, identischem Testkorpus und
  reproduzierbarer Auswahl-/Startklasse
- monotone gemeinsame Zeitbasis und Operator-/Autotest-Marker
- Device-Telemetrie für Media-Hide, Soft-Detach/Attach, Mountstatus und
  Boot-ID/Resetreason
- unabhängige Beobachtung des physischen Steckereignisses; für Strom- oder
  Resetfragen zusätzlich
  [`plug-power-reset-isolation`](plug-power-reset-isolation.md)
- HU-nahe Beobachtung mindestens für Medium sichtbar/fehlend, Auswahl,
  Startklasse sowie hör-/sichtbaren Inhaltsmarker
- präregistrierte Wartefenster und ein operatives Kriterium für `C-HU`
- unveränderter Kontrolllauf vor und nach der Ereignisserie

Fehlt eine erforderliche Beobachtung, wird die betroffene Dimension
`UNKNOWN`; sie wird nicht aus Zeitabstand oder Nachbarereignissen abgeleitet.

## Isolierte Dimensionen

Pro Isolationslauf wird genau **eine** Ereignisdimension geändert:

1. `MH`: Sichtbarkeit aus/an, ohne Soft-Detach, Replug, Boot oder
   Identity-Wechsel.
2. `SD`: genau ein Detach/Attach-Zyklus, ohne Replug, Boot, Media-Inhalt- oder
   Identity-Wechsel.
3. `PR`: genau ein physischer Replug; Versorgung und Device-Boot werden nur
   beobachtet, nicht still vorausgesetzt.
4. Warm/Cold-Kontrast: dasselbe Ereignis einmal in präregistriertem `W*` und
   einmal in belegtem `C-HU`; keine weitere Dimension ändern.

Konstant bleiben insbesondere USB-Serial/Product-Revision, FAT/BPB- und
Root-Label, Volume-ID, Dateiliste/-größe/-pfad/-cluster, Inhalt, ausgewählter
Track, Firmware, Kabel und HU-Bedienfolge. Identity-Tests gehören zu
[`nbt-medium-identity-resume`](nbt-medium-identity-resume.md), nicht in diesen
Lauf.

## Ablauf

1. Run-ID, erwartete Ereignisklasse, Ausgangs-Epochs, HU-/Device-Zustand,
   Medium-Identity, Testkorpus und präregistriertes Nachbeobachtungsfenster
   erfassen.
2. Kontrollauswahl ohne Lifecycle-Ereignis ausführen. Auswahlklasse als
   **kein Read**, **Head-Read** oder **Body-/Mid-Read** und den tatsächlich
   gelieferten/hörbaren Marker getrennt festhalten.
3. Genau ein Ereignis `MH`, `SD` oder `PR` auslösen. Marker für Request,
   beobachteten Zustandswechsel und Rückkehr setzen; nicht beobachtete
   Zwischenstufen bleiben `UNKNOWN`.
4. Epoch-Zähler nur anhand ihrer eigenen Marker fortschreiben. Bei `PR`
   Bootreason/Rail-Klasse erfassen; bei `SD` unveränderte Boot-ID prüfen.
5. Nach Rückkehr dieselbe Auswahl und Bedienfolge ausführen. Sichtbarkeit,
   Auswahl, Startklasse, ausgelieferten Marker und relevante
   Device-/MSC-Telemetrie erfassen.
6. Den Lauf identisch wiederholen. Danach unveränderten Kontrolllauf fahren,
   um Baseline-Drift zu erkennen.
7. Erst bei stabiler Einzelklasse den Warm/Cold-Kontrast oder die nächste
   Ereignisklasse starten. Cache-/Resume-Deutungen werden an die ermittelte
   Lifecycle-Klasse gebunden, nicht klassenübergreifend gemittelt.

## Epistemischer Vertrag

| Aussage | Zulässiger Status |
|---------|-------------------|
| protokollierter Hide-/Detach-Request, Device-Boot-ID, Mountcallback, Operator-Replugmarker, beobachtete HU-Anzeige oder AV-Marker | `FACT` des jeweiligen Instruments/Laufs |
| „Nachklasse folgt reproduzierbar auf genau dieses isolierte Ereignis“ | `INFERENCE`, bis Wiederholung und Kontrolllauf die Zuordnung tragen |
| „HU löscht/persistiert MediaStore oder Cache intern“ | `HYPOTHESIS`, solange kein unabhängiger interner Beleg existiert |
| USB-Pakete, Busreset, elektrische Trennung oder Wire-Timing | ohne validierten separaten Capture `UNKNOWN`; kein Wire-Claim |

Ein Stack-Mountcallback ist kein Beleg für eine konkrete Wire-Sequenz. Ebenso
belegt ein physischer Replug allein weder Device-Power-Cycle noch `C-HU`.

## Messvertrag und Artefakte

Jeder Lauf liefert:

- Run-Manifest mit Firmware, Medium-/Korpus-Hashes, Identity, Kabel/
  Versorgung, Ereignisklasse, Warm/Cold-Klasse und präregistrierten Fenstern
- normalisierte Timeline mit `t`, Quelle, Marker, Epoch-Zählern, Boot-ID,
  Mountstatus, HU-Sichtbarkeit, Auswahl-/Startklasse und Inhaltsmarker
- Vorher/Nachher-Snapshot der HU-nahen Beobachtungen und Device-Telemetrie
- Kontrolllauf-Diff und Wiederholungsmatrix je Ereignis-/Zustandsklasse
- Klassifikation `FACT` / `INFERENCE` / `HYPOTHESIS` / `UNKNOWN` pro Aussage
- Rohlogs unverändert plus Parser-/Toolversion; Evidence erst im ausführenden
  Audit, diese Note vergibt keine Evidence-ID

Zeitwerte werden als Instrumentmessung mit Auflösung/Unsicherheit geführt.
Fehlende Marker dürfen nicht aus Logreihenfolge synthetisiert werden.

## Soft-Cycle-Autotest

Ein Autotest darf `MH` oder `SD` deterministisch auslösen, Run-/Epoch-Marker
setzen und die Rückkehr der Device-Instrumentierung prüfen. Der bestehende
Lab-Lauf mit `auto_soft_detach` belegt einen vollständigen
`ram_offline`-Instrumentpfad, nicht dieselbe Wirkung am BMW-HU:
[`hu-probe-bmw-s0s2-field-2026`, Evidence `007`](../audits/hu-probe-bmw-s0s2-field-2026/evidence.md).

Vor HU-Einsatz muss der Autotest offenlegen, ob „Soft Cycle“ `MH`, `SD` oder
eine Sequenz aus beiden bedeutet. Kombiniert er beide, ist er ein
Funktions-/Regressionstest, aber kein kausal interpretierbarer
Isolationslauf. Autotest-PASS bedeutet nur: die präregistrierte Aktion und
ihre Instrumentmarker wurden vollständig ausgeführt.

## Präregistrierte Gates

| Gate | Pass | Fail | Kill / Stop |
|------|------|------|-------------|
| L1 Baseline | Kontrollläufe liefern gleiche Sichtbarkeit, Auswahl- und Startklasse | Baseline driftet | Ereignisserie stoppen; Läufe nicht vergleichen |
| L2 Einzelereignis | genau eine Ereignisdimension geändert; übrige Epochs wie erwartet stabil | erwartete Klasse tritt nicht ein | mehrere Ereignisse, Boot-/Identity-Drift oder unklare Epochgrenze → Lauf verwerfen |
| L3 Nachklasse | dasselbe Ereignis ergibt in Wiederholung dieselbe HU-nahe Nachklasse und denselben Inhaltsmarker | Persistenz-/Reset-Hypothese widerspricht der Nachklasse | Marker oder Rückkehrfenster unvollständig → keine Kausalitätsaussage |
| L4 Warm/Cold | `W*` und `C-HU` sind operativ belegt und bei sonst identischem Lauf unterscheidbar oder gleich | erwarteter Warm/Cold-Kontrast tritt nicht ein | `C-HU` nur aus Wartezeit/Zündung angenommen → Kontrast verwerfen |
| L5 Soft-Cycle-Autotest | Aktion, Klasse und Epoch-Marker vollständig; keine gekoppelte Dimension | Autotest erreicht Zielklasse nicht | Sammelbegriff „Soft Cycle“ ohne aufgelöste Aktion → nur Regression, keine Isolation |
| L6 Claim-Grenze | Aussagen bleiben auf beobachteter Instrument-/HU-Ebene | interne Cache-/MediaStore-Hypothese widersprochen | Wire- oder Powerclaim ohne eigenes Instrument → Claim stoppen |

`FAIL` verwirft die jeweilige Hypothese. `KILL` stoppt nur den abhängigen
Interpretationspfad oder verwirft den Lauf; `UNKNOWN` allein ist kein
automatischer Stop.

## Fallstricke

- Media-Hide, Soft-Detach und Replug sind nicht austauschbare „Remounts“.
- Ein neues Mountcallback kann bei gleicher HU-Session weiterhin warm sein.
- Ein langer Schlaf, Zündung aus oder Türverriegelung ist ohne operatives
  Kriterium kein `C-HU`.
- Physischer Replug kann Power-, Reset- und Masseeffekte koppeln; A11 zuerst
  auswerten, sobald Boot-ID oder Rail abweicht.
- Kein Read nach Rückkehr belegt weder Cache-Inhalt noch Decoderposition.
- Lifecycle-, Identity- und Content-Änderung nie im selben Isolationslauf.
- Ergebnisse nicht über Firmware, Fahrzeugprofil oder HU-Variante übertragen,
  ohne die Preconditions erneut zu belegen.

## Beispiel-Einsatz

[`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/) — HU-A9,
präregistriert und derzeit `UNKNOWN`.
