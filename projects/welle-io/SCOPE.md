# Project Scope: welle.io (Fremd)

```yaml
project_id: welle-io
title: welle.io — DAB/DAB+ SDR Receiver (Fremd)
updated: 2026-10-11
profile_hint: lab-tool
reviewed_commit: "512558d"
reviewed_commit_note: Upstream master tip at desk audit (tag/message „Bump to 2.7 stable“); Desk only, no RF field
repos:
  - https://github.com/AlbrechtL/welle.io
status: active
```

## Zweck

KB-Reuse-Test für den Upstream von PiDrive-DAB (`welle-cli`): Desk-Audit von [AlbrechtL/welle.io](https://github.com/AlbrechtL/welle.io) gegen bestehende Sheets `dab-plus` / `rtl-sdr` — Gain-Semantik, Kanalmodell, Web-/Spektrum-Grenzen, Input-Treiber. **Kein** neues Empfangsprodukt, kein Feldversuch.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| welle-cli (CMake, ohne Qt) | CLI + optionaler Webserver | ja (Desk) |
| welle-gui (Qt 6) | Desktop-GUI | Überblick / Build-Signale |
| RTL-SDR / rtl_tcp / RAW | Primäre Sample-Quellen | ja |
| Airspy / SoapySDR / LimeSDR | Weitere Inputs | beobachtet, nicht vertieft |
| PiDrive-Integration | Kontrast / Nachbar | angrenzend |
| Antennen-Feldempfang / Tuning-Messung | — | **nein** |

## Nicht-Ziele

- Vollständige GUI-/QML- oder Flatpak-Packaging-Analyse
- SoapySDR-/Airspy-Treiber-für-Treiber-Labor
- Android-/macOS-Wartungsstatus beheben
- PiDrive-Audio-/BT-Politik nachmessen (bleibt in `pidrive`)

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code | https://github.com/AlbrechtL/welle.io @ `512558d` | v2.7 |
| Docs | Upstream `README.md` | Hardware, CLI, Limits |
| Nachbar | [`pidrive`](../pidrive/) Apps `dab-plus`, `rtl-sdr` | Feld/Ops-Kontrast |

## Prioritäten für die Analyse

1. Match: kein neues DAB-Sheet — bestehendes `dab-plus` wachsen lassen  
2. Gain-Index + Software-AGC aus Upstream belegen (nicht nur PiDrive-Doku)  
3. `/spectrum` vs. `sdr-spectrum-fft` klar abgrenzen  
4. Evidence auf Commit `512558d`

## Offene Scope-Fragen

- Ob SoapySDR-/Airspy-Fallstricke später eigene observed-Zeilen rechtfertigen (nur bei Transferbedarf)
