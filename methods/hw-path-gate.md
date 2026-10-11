# Method: Hardware-Path Gate (RF / Clock)

```yaml
slug: hw-path-gate
title: Hardware-Path Gate (RF / Clock)
status: active
tags: [lab-only, radio-tx, validation]
```

## Zweck

Falsifizierbare Gates, bevor eine Chip-/Pfad-Variante als Technologie behauptet oder als Hub-Ausgabeknoten geplant wird. Verhindert „Dokumentation ersetzt Messung“.

## Voraussetzungen

- Desk: Datasheet/TRM + ESP-IDF (oder BCM-)Quellen; Ziel-Chip bekannt
- Lab (ab E-1): geschirmter Aufbau, Dämpfung, Spektrumanalysator oder SDR — **keine Antenne**

## Ablauf

1. **E-0 Desk** — Signalpfad bis Register/Mux skizzieren (Source → Divider → Peripheral → Pad). Keine FM-Modulation.
2. **E-1 Lab** — konstanter Träger auf **einem** validierten Pin; Sollfrequenzen im Zielband (z. B. 90/100/108 MHz) prüfen.
3. **E-2** — Raster, Drift, Sprünge dokumentieren.
4. **E-3** — Teiler-/Frac-Updates → Modulation nachweisbar.
5. **Safety (optional E-4)** — Disconnect/Underrun/Reset → TX OFF.

## Artefakte

- Evidence-Zeilen pro Gate (`FACT` Desk / `MEASURED` Lab)
- FOLLOW-ON oder Kampagne-Exit aktualisieren
- Bei positivem Gate: Sheet anlegen/erweitern; bei Fail: `REJECTED`/`UNKNOWN` + Fallback-Architektur

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| E-0 | konkrete Register/API + Pin-Kandidat benennbar | nur „API vorhanden“ ohne Mux-Kette |
| E-1 | Träger @ Sollfrequenz messbar | Frequenz nicht erreichbar / nicht stabil genug für nächsten Schritt |
| E-3 | Hub/Modulation plausibel messbar | nur unmodulierter Träger oder Glitches dominieren |

## Fallstricke

- „Einziger Kandidat“ vor E-0/E-1 als Absolutismus formulieren
- Mehrere GPIOs abstrahieren, bevor **ein** Pin funktioniert
- Classic-ESP32-APLL-Evidence auf S3 übertragen
- Antennenbetrieb / illegale Aussendung

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| `esp-fm-tx` | Classic APLL belegt; S3-Gate offen in FOLLOW-ON |
| `pi-fm-tx` | BCM-GPCLK Pi1–4 belegt; **Pi5/RP1-Gate** E-0/E-1 in FOLLOW-ON; Harmonics `UNKNOWN` ohne Lab |
