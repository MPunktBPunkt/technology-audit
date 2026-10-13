# Method: Field AV Offset Correlation

```yaml
slug: field-av-offset-correlation
title: Field AV Offset Correlation
status: active
tags: [audio, usb-msc, correlation, field, preregistered]
```

## Zweck

Gelieferte Dateibytes mit Cache-, Decoder- und hörbarer Timeline verbinden,
ohne USB-Read-Offset mit Decoderposition gleichzusetzen. Geeignet für HU-A5
und vergleichbare gepufferte Audiopfade. Ungemessene Offsetbeziehungen bleiben
`UNKNOWN`.

## Voraussetzungen

- grünes Startgate: Auswahl und Startklasse sind reproduzierbar
- LBA→Dateioffset-Map und synchronisierte MSC-/Device-Zeitbasis
- Testfiles mit maschinenlesbaren Offsetmarkern und hör-/sichtbaren Markern
- unabhängiger Parser/Decoder zur Prüfung der erzeugten MPEG-/ID3-Struktur
- Feldaufzeichnung mit monotonic Zeit oder gemeinsamem Klapp-/Lichtmarker

## Ablauf

1. Kontrollfile mit konstantem MPEG-Profil und Markern in bekannten
   Dateioffset-/Samplepositionen erzeugen; Hash und Parserausgabe sichern.
2. Plug, Auswahl, erste Datenlieferung, Head-/Body-Reads, Device-Bytes und
   hör-/sichtbare Marker auf eine Zeitachse bringen.
3. Kette `Dateioffset → ausgelieferte Bytes → Cache/Read-Lücke →
   hörbarer Marker` auswerten. Unbeobachtete Cache-/Decoderstufen nicht
   erfinden.
4. Baseline identisch wiederholen. Erst danach jeweils **eine** Dimension
   variieren: MPEG-Version, Sample-Rate, Kanalzahl, Bitrate oder ID3/APIC-Länge.
5. Formatwechsel innerhalb einer Datei nur nach stabiler Baseline testen;
   Position, Resync-Dauer und Folgeframes dokumentieren.
6. Rechnerischen Samplezeitpunkt und beobachteten Marker mit vorab definierter
   Toleranz vergleichen; Ausreißer einzeln klassifizieren.

## Artefakte

- Manifest der Testfiles mit Hash, Frame-/ID3-Map und Markerpositionen
- synchronisierte Offset-/Read-/AV-Timeline
- Abweichungsbudget für Capture, Puffer und Markerauflösung
- Evidence erst im ausführenden Audit; keine ID aus dieser Präregistrierung

## Präregistrierte Gates

| Gate | Pass | Fail | Kill / Stop |
|------|------|------|-------------|
| AV1 Baseline | zwei Läufe liefern gleiche Markerreihenfolge innerhalb deklarierter Toleranz | Reihenfolge oder Startklasse weicht ab | keine Formatmatrix starten |
| AV2 Offsetbindung | gelieferter Offset sagt Markerfenster reproduzierbar voraus | Marker widerspricht der Offsethypothese | Hypothese verwerfen; Decoderposition `UNKNOWN` |
| AV3 Einzelfaktor | genau ein Formatparameter geändert und File valide | mehrere Parameter oder Parserfehler | Lauf nicht interpretieren |
| AV4 Resync | Formatwechsel und Resync-Grenze reproduzierbar | sporadisches Verhalten | kein allgemeiner Decoderclaim |

## Fallstricke

- Dateioffset, physischer Read, Decoder-P und Ohrzeit sind vier verschiedene
  Größen.
- Variable Bitrate und große ID3/APIC-Blöcke machen Byte→Zeit-Rechnung ohne
  Frame-Map unzulässig.
- Lab-Audio ist kein Feld-Ohr-PASS.
- Diese Methode blockiert den Hauptpfad nicht, solange das Startgate offen ist.

## Beispiel-Einsatz

[`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/) — HU-A5,
präregistriert und noch `UNKNOWN`.
