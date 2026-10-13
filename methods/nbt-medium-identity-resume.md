# Method: NBT Medium Identity / Resume Isolation

```yaml
slug: nbt-medium-identity-resume
title: NBT Medium Identity / Resume Isolation
status: active
tags: [usb-msc, fat, cache, automotive, field-verified-input]
```

## Zweck

Bei stummem Start eines großen festen MSC-Files drei Zustände getrennt
bestimmen: Decoderposition **P**, physischer MSC-Read-Offset und bereits
gecachter Dateiinhalt. Erst danach eine Resume- oder Identity-Abwehr wählen.

## Voraussetzungen

- LBA→Slot/File-Offset-Map und MSC-Trace
- Status vor/nach Auswahl (`playingUid`, Stream-Slot, Head/Mid-Zähler)
- Blockdevice-Zugriff auf Boot- und Root-Sektoren
- definierter Live- und non-live-Inhalt je Slot

## Ablauf A — Prefetch vor Resume

1. Cold/definierte Identity erfassen.
2. Slot A live spielen, Slot B non-live durch den Host vorlesen lassen.
3. Vor Auswahl von B Marker und Status sichern.
4. B auswählen und klassifizieren:
   - kein Read: cache-hit-like;
   - Mid-File-Read: möglicher Resume/Intent ohne Head;
   - Head-Read: Play-Detect/Gate prüfen.
5. Audio/ID3 nicht allein aus dem ersten Read-Offset ableiten; den tatsächlich
   ausgelieferten Inhalt und die Decode-Beobachtung separat korrelieren.

## Ablauf B — Identity-Matrix bei P≫0

Pro Lauf genau eine Dimension ändern:

1. USB-Serial/Product-Revision,
2. FAT12/16 BPB Volume-ID,
3. BPB-Label + Root-Label (konsistent),
4. Dateiname,
5. Dateigröße,
6. Pfad,
7. Startcluster.

Vor und nach jedem Lauf Status, Bootsektor und Root-Directory sichern. Bereits
negativ getestete Kombinationen nicht als neue Isolation wiederholen.

## Pass / Fail

| Gate | Pass | Fail / nicht interpretierbar |
|------|------|-----------------------------|
| Identity isoliert | genau eine Dimension geändert | mehrere Dimensionen gekoppelt |
| Medium belegt | API = tatsächlicher BPB/Root-Sektor | nur API-/Config-Wert |
| Startklasse | kein/Mid/Head eindeutig | nur Ohrbeobachtung |
| Kausalität | Wiederholung mit gleicher Klasse | Head-Force + Rotation zusammen |

## Fallstricke

- `fromHead`/`midFile` beschreibt physische Reads, nicht Decoder-P.
- Kein Read bei Auswahl kann vom Device nicht mit Head-Force beeinflusst werden.
- Ein Root-Volume-Label ist nicht dasselbe wie BPB-Label oder BPB Volume-ID.
- Trace-Tags können abgeschnitten sein; Slot über LBA-Bereich zuordnen.
- Neue Evidence-ID erst aus einem neuen Messlauf, nicht aus Reinterpretation.

## Beispiel-Einsatz

`pidrive-2026-bmw-hu`: S6 `fav0` 8 MiB, D-Startgate vor D1–D3.
