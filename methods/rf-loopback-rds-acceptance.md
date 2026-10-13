# Method: RF Loopback / RDS Acceptance

```yaml
slug: rf-loopback-rds-acceptance
title: RF Loopback / RDS Acceptance
status: active
tags: [rf, fm, rds, spectrum, safety, preregistered]
```

## Zweck

FM-Audio, Stereo, RDS, Spektrum und Abschaltung als getrennte
Abnahmedimensionen prüfen. Die Methode deckt RF-B8 und RF-B10 ab und liefert
Abnahmegates für Pfade aus RF-B2 bis RF-B5. Sie ist keine
Sendeberechtigung und enthält keine Implementierungsanleitung.

## Voraussetzungen

- bestandener Signalpfad gemäß [`hw-path-gate`](hw-path-gate.md)
- geschirmter Aufbau, Dämpfung/Dummy-Load, **keine Antenne**
- dokumentierter maximaler Laborpegel und lokale Freigabe
- kalibrierte Spektrummessung/SDR, Referenzdecoder und mindestens ein reales
  Radio; definierte PI/PS/RT-Testsequenz
- unabhängig auslösbarer TX-OFF

## Ablauf

1. Aufbau ohne TX auf Umgebungs-/Leakage-Baseline prüfen.
2. Unmodulierten Träger bei vorab gewählten Frequenzen messen; Frequenz,
   Pegel, Drift, Spurs und relevante Harmonische erfassen.
3. Mono-Audio einspeisen und Deviation, Frequenzgang/Verzerrung sowie
   Empfang getrennt prüfen.
4. Stereo/19-kHz-Pilot und danach RDS/57-kHz einzeln zuschalten. PI, PS, RT,
   Gruppenfolge und Updatezeit am Referenzdecoder erfassen.
5. Dasselbe am realen Radio beobachten; SDR-/Gruppendecode und UX-Anzeige
   nicht zu einem globalen PASS verschmelzen.
6. Boot, Linkverlust, Underrun, Watchdog und geordnetes Shutdown einzeln
   auslösen. Ausgang und Transienten bis TX-OFF messen.
7. Dauerlauf nur nach Safety-PASS; Audio/Metadaten und Spektrum parallel
   protokollieren.

## Artefakte

- Aufbau-/Dämpfungsbudget und Messgeräteversionen
- Spektrum-/Harmonischen-/Transientenprotokoll
- Audio-, Stereo- und RDS-Matrix pro Empfänger
- RDS-Gruppenlog plus PI/PS/RT-Updatezeiten
- Evidence erst im ausführenden Audit

## Präregistrierte Gates

Grenzwerte für Frequenz, Deviation, Spurs/Harmonische, Leakage, Updatezeit und
TX-OFF-Latenz müssen vor Aktivierung im Audit stehen; bis dahin `UNKNOWN`.

| Gate | Pass | Fail | Kill / Stop |
|------|------|------|-------------|
| R1 Containment | Leakage und Pegel innerhalb präregistrierter Laborgrenze | Grenze überschritten/unklar | TX sofort aus; kein weiterer RF-Lauf |
| R2 Carrier/Spektrum | Frequenz, Drift, Spurs und Harmonische innerhalb Limits | ein Limit verletzt | keine Modulationsabnahme |
| R3 Audio/Stereo | Referenzdecoder erfüllt getrennte Mono-/Pilot-/Stereo-Kriterien | Lock oder Audio instabil | kein RDS-Gesamt-PASS |
| R4 RDS | PI/PS/RT und Gruppenfolge am Referenzdecoder korrekt und rechtzeitig | falsche/stale Daten oder CRC-/Gruppenlimit verletzt | RDS-Pfad FAIL |
| R5 Empfängermatrix | Referenz + reales Radio je Dimension dokumentiert | nur UX oder nur SDR | Interoperabilität `UNKNOWN` |
| R6 Fail-safe | jeder Fehlerfall erreicht TX-OFF innerhalb Limit, ohne unzulässigen Transienten | Träger bleibt oder Transient verletzt Limit | Architektur-Kill bis Hardware-Fix |

## Fallstricke

- Ein Radio mit angezeigtem PS beweist weder Spektrum noch vollständige
  Gruppenrichtigkeit.
- SDR-Softwarepegel ohne kalibrierte Kette ist kein absoluter Ausgangspegel.
- Audio-PASS, Stereo-PASS, RDS-PASS und RF-Safety-PASS getrennt halten.
- Resettransienten gehören zur Abnahme, nicht nur der stationäre Träger.
- Kein Antennenbetrieb und kein ungeschirmter Test.

## Beispiel-Einsätze

RF-B8/B10 nach Architektur- und Hardwaregate; sämtliche Messwerte derzeit
`UNKNOWN` und präregistriert.
