# Method: PCM Clock Drift / Jitter Buffer

```yaml
slug: pcm-clock-drift-jitter-buffer
title: PCM Clock Drift / Jitter Buffer
status: active
tags: [audio, network, clock, jitter, preregistered]
```

## Zweck

Host-Audioclock, Netzwerkankunft und Playout-/Modulationsclock messbar
koppeln. Die Methode präregistriert Transport-, Drift-, Reconnect- und
Fail-safe-Gates für RF-B2, RF-B6, RF-B7 und den Betriebsanteil von RF-B9,
ohne eine konkrete Firmware oder TCP als einzig zulässigen Transport
vorwegzunehmen.

## Voraussetzungen

- festgelegtes PCM-Format, Framing, Sequenz-/Samplezähler und Session-ID
- Telemetrie für Bufferfüllstand, Under-/Overflow, Playoutsamples,
  Reconnect und Clockkorrektur
- unabhängige Zeit-/Frequenzreferenz für Sender und Empfänger
- RF-Ausgang deaktiviert oder vollständig geschirmt/gedämpft; Audio-/MPX-
  Loopback vor RF

## Ablauf

1. Contract festhalten: Sample-Rate/-breite/-kanäle, Frames pro Paket,
   Sequenz, Samplecounter, Heartbeat, Flow-Control und Linkverlustaktion.
2. Lokale Baseline ohne Netzwerkjitter erfassen; nominale Clockabweichung und
   Messrauschen bestimmen.
3. Jitter-/Burst-/Delay-Leiter mit unverändertem Audiotakt fahren und
   Bufferlevel, Unter-/Überläufe sowie Latenz erfassen.
4. Clockdrift separat in positiven und negativen ppm-Stufen einspeisen.
   Resampler-/Rate-Matching-Korrektur und Buffertrend gemeinsam auswerten.
5. Paketverlust, Duplikat, Reordering, Backpressure, TCP-Stall und Reconnect
   einzeln testen; Transportsemantik explizit benennen.
6. Producer-Neustart, Sessionwechsel und Metadatenausfall prüfen.
   Linkverlust muss in vorab begrenzter Zeit Mute/TX-OFF anfordern.
7. Dauerlauf erst nach bestandenen Einzelgates; Buffertelemetrie mit
   Audio-/MPX-Frequenz und später optional RF-Messung korrelieren.

## Artefakte

- versionierter Transportvertrag und Testprofil
- Zeitreihe für Samplecounter, Ankunft, Bufferlevel, Korrektur-ppm,
  Under-/Overflow, Latenz und Linkzustand
- Gateprotokoll getrennt nach lokalem Audio/MPX und RF
- Evidence erst in einer ausführenden Kampagne

## Präregistrierte Gates

Numerische Grenzwerte müssen vor dem ersten Lauf im Audit eingesetzt werden;
bis dahin sind sie `UNKNOWN`.

| Gate | Pass | Fail | Kill / Stop |
|------|------|------|-------------|
| J1 Contract | jedes Playoutframe einer Session/Sequenz zuordenbar | implizites Framing oder unerkannte Sessionmischung | kein Dauerlauf |
| J2 Buffer | kein Under-/Overflow innerhalb präregistrierter Jitterleiter | Grenzereignis oder monotone Drift | Architektur nicht für RF freigeben |
| J3 Drift | Buffer bleibt um Zielbereich; Korrektur innerhalb Limit | Korrektur sättigt oder hörbare Sprünge | Rate-Matching-Ansatz verwerfen |
| J4 Reconnect | neue Session startet ohne Alt-/Neudatenmischung | stale PCM oder unbeschränkte Lücke | TX bleibt OFF |
| J5 Fail-safe | Linkverlust/Heartbeat-Ausfall führt fristgerecht zu Mute/TX-OFF | unkontrollierter Output | Kampagne sofort stoppen |
| J6 Dauerlauf | Latenz, Buffer und Clock bleiben über festgelegte Dauer begrenzt | Trend oder Grenzwertverletzung | kein MVP-Go |

## Fallstricke

- TCP verhindert Paketverlust auf Stream-Ebene, nicht Head-of-line-Latenz,
  Stalls oder Sessionverwechslung.
- Bufferstabilität allein beweist keine korrekte Modulationsfrequenz.
- Resampling kann Drift kaschieren und Audioqualität verschlechtern; beides
  getrennt messen.
- WiFi-/CPU-Last ist eine Testdimension, kein Ersatz für Clockmessung.
- Linkverlust→Mute und RF-TX-OFF sind getrennte Aktoren, falls ein externer
  Synthesizer weiterträgt.

## Beispiel-Einsätze

RF-B2/B6/B7/B9 einer künftigen Netzwerk-PCM→FM/RDS-Kampagne; alle Ergebnisse
bis zum Messlauf `UNKNOWN`.
