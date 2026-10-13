# Method: NBT Cache, Eviction und Play-Intent

```yaml
slug: nbt-cache-eviction-play-intent
title: NBT Cache, Eviction und Play-Intent
status: active
tags: [usb-msc, cache, automotive, preregistered]
```

## Zweck

Cache-Hit, Resume, Prefetch und echten Wiedergabewunsch trennen sowie
Kapazität, Eviction und Metadatenbindung reproduzierbar bestimmen. Die Methode
deckt HU-A1, HU-A3, HU-A4, HU-A6 und die Read-Anteile von HU-A8 ab. Alle noch
nicht ausgeführten Varianten sind `UNKNOWN`.

## Voraussetzungen

- definierter Cold-/Warm-Zustand nach
  [`hu-media-lifecycle`](hu-media-lifecycle.md)
- LBA→Datei-/Offset-Map und
  [`msc-trace-correlation`](msc-trace-correlation.md)
- je Slot unterscheidbare Audio-, Stille-, ID3- und APIC-Marker
- unveränderte Kontrollläufe; pro Isolationslauf genau eine Variable

## Ablauf

1. Baseline mit dokumentierter Medium-Identity, Dateiliste und Lifecycle
   erfassen.
2. Slot A live spielen, Slot B nur non-live lesen lassen, dann B auswählen.
   Auswahl als **kein Read**, **Head-Read** oder **Body-/Mid-Read**
   klassifizieren; gelieferten Inhalt und hörbaren Marker getrennt notieren.
3. Manuell, Auto-Next, Resume und Index-Prefetch mit demselben Korpus
   wiederholen. Klassifikator zunächst ausschließlich observe-only auswerten.
4. Kapazitätsleiter getrennt fahren: zuerst Dateigröße bei konstanter
   Dateianzahl, danach Dateianzahl bei konstanter Gesamtgröße.
5. FIFO gegen LRU prüfen: A/B/C füllen, A gezielt berühren, D einbringen und
   A/B erneut auswählen. Positionsabhängige Verdrängung separat prüfen.
6. Metadatenmatrix fahren: gleiche Audioframes mit geändertem ID3/APIC; danach
   gleiche Metadaten mit neuer Datei- oder Volume-Identity. Bild- und
   Audioreaktion getrennt bewerten.
7. Plug→erste stabile Auswahl als Timeline erfassen und Reads als
   Index/Prefetch/Play-Guess/BUSY-arm klassifizieren. Nicht klassifizierbare
   Phasen bleiben `UNKNOWN`.
8. Jede beobachtete Klasse mindestens einmal identisch wiederholen; erst dann
   eine Policy-Änderung erwägen.

## Artefakte

- Run-Matrix mit Identity, Lifecycle, Intent, Größen-/Anzahlstufe und genau
  einer geänderten Variable
- Command-/LBA-Timeline plus Device-Inhalt und AV-Marker
- Cache-Hit-/Miss-/Eviction-Tabelle; Audio und APIC/ID3 getrennt
- Evidence erst im ausführenden Audit; diese Note erzeugt keine Evidence-ID

## Präregistrierte Gates

| Gate | Pass | Fail | Kill / Stop |
|------|------|------|-------------|
| C1 Prefetch-Kausalität | Auswahlklasse und gelieferter Marker sind in Wiederholung gleich | Klasse oder Marker widersprechen sich | keine Policy-Änderung bei uneindeutiger Klasse |
| C2 Play-Intent | manuell/Auto-Next/Resume/Prefetch haben reproduzierbar trennbare Signaturen | Signaturen überlappen | Play-Guess bleibt observe-only |
| C3 Kapazität | kleinste reproduzierbare Hit→Miss-Grenze bestimmt | nur einzelne Misses | Leiter stoppen, wenn Lifecycle driftet |
| C4 Eviction | FIFO, LRU oder positionsabhängige Regel durch Gegenprobe unterscheidbar | Gegenprobe widerspricht | keine globale Eviction-Regel claimen |
| C5 Metadaten | Audio- und Metadatenbindung jeweils isoliert | mehrere Identities zugleich geändert | keine Cache-Identity-Aussage |
| C6 Menüphase | dominante Read-Klassen erklären die Zeitspanne reproduzierbar | Rest nicht zuordenbar | Ursache bleibt `UNKNOWN` |

## Fallstricke

- Kein Read ist kein Beleg für Decoderposition oder konkreten Cache-Inhalt.
- Ein Body-Read kann Prefetch, Resume oder Play sein; Ohrbeobachtung allein
  entscheidet das nicht.
- Cache-Kapazität nicht über Zündung, Replug oder Sleep hinweg mitteln.
- Head-Force und Identity-Rotation nie im selben Isolationslauf.
- Vorhandene Methode
  [`nbt-medium-identity-resume`](nbt-medium-identity-resume.md) für HU-A2
  wiederverwenden, nicht hier duplizieren.

## Beispiel-Einsatz

[`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/) — HU-A1/A3/A4/A6/A8,
präregistriert; neue Messwerte derzeit `UNKNOWN`.
