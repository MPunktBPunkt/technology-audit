# Follow-on ideas (aus esp-fm-rds-node)

```yaml
reuse_outcomes:
  reused: [fm-rds, esp-i2s-audio]
  new: []
  not_created: [fm-stereo-rds-mpx, fm-rds-synthesizer-ic]
  not_helped: [esp32-apll-fm-tx]
  process: "A/B/C-Trennung, G17-Chip-Scope, präregistrierte Desk-/Lab-Gates"
```

## Präregistrierte Gates

Diese Gates sind Planung, keine durchgeführten Tests. Lab und Field bleiben
`UNKNOWN`. Vor einem späteren Messlauf müssen Aufbau, Instrumente, Grenzwerte
und Rohdatenpfad ergänzt werden.

| Gate | Stufe | Voraussetzung | PASS | STOP / Kill | Status |
|------|-------|---------------|------|-------------|--------|
| G-MPX-0 | Desk | ausgewählter externer FM-Modulator | dokumentierter MPX/Composite-Eingang deckt Audio, 19/38/57 kHz ab | kein geeigneter Composite-Eingang oder unklare Grenzwerte | offen |
| G-MPX-1 | Lab, geschirmt | G-MPX-0 PASS | Träger und MPX-Komponenten nach präregistriertem Plan nachweisbar | kein stabiler Träger oder fehlender Pilot trotz verifiziertem DAC-MPX | offen |
| G-MPX-2 | Lab, geschirmt | G-MPX-1 PASS | Stereo und RDS werden vom Referenzempfänger reproduzierbar dekodiert | Pilot vorhanden, aber Stereo/RDS nach kontrollierter Wiederholung nicht dekodierbar | offen |
| G-I2S-1 | Lab | S3-Build + Audiohardware | keine I2S-Fehler/Underruns im festgelegten Dauerfenster | reproduzierbare I2S-Fehler/Underruns bei unverändertem Aufbau | offen |
| G-IC-1 | Desk | QN8027- und Si4713-Datenblätter/APIs | gemeinsame minimale Contract-Fläche klar; Unterschiede explizit | Contract würde Chip-spezifische Audio-/RDS-Semantik verdecken | offen |
| G-IC-2 | Lab, geschirmt | G-IC-1 PASS | derselbe Control-Testvektor liefert je Chip erwartete Zustände | ein gemeinsamer Testvektor ist nicht semantisch vergleichbar | offen |
| G-LIC-1 | Desk | PiratESP32/S3-DSP als Codequelle | Lizenzbedingungen eindeutig kompatibel | Zusatzbedingung oder fehlende Lizenz bleibt ungeklärt | offen |
| G-LEGAL-1 | vor jedem RF-Lab | lokaler Rechts-/Aufbaucheck | geschirmte, leitungsgebundene oder äquivalent kontrollierte Prüfung freigegeben | Antenne/Feldabstrahlung nötig oder Rechtslage ungeklärt | offen |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| S3-MPX-Modulatormatrix | G-MPX-0 | Composite-Eingang, Pegelbereich und DC-Kopplung möglicher externer Modulatoren vergleichen |
| Deterministischer S3-Labaufbau | G-MPX-1/G-I2S-1 | PiratESP32 + S3-DSP-Board + externer Modulator; keine Antenne |
| MPX-Contract erst nach Lab | G-MPX-2 | nur bei reproduzierbarem Stereo/RDS-PASS neues Sheet vorschlagen |
| QN8027/Si4713 Interface-Matrix | G-IC-1 | I2C, Audio analog/digital, Tune/Power, PS/RT, Status-/FIFO-Semantik |
| Dynamic-RDS-Testvektor | `fm-rds` | PS/RT-Wechsel mit A/B-Toggle/Refresh als desk-definierter Vektor |
| C3-Control-Node | QN8027 + Web | C3 nur als Controller behandeln; Audioquelle und RF-Chip separat |
| Classic-A2DP-Kontrast | esp32_fmdevkit | A2DP/I2S-DAC/Metadaten-Paging gegen S3-Netzwerk-PCM abgrenzen |
| Lizenzklärung | G-LIC-1 | PiratESP32 README/Lizenz und fehlende S3-DSP-Lizenz upstream klären |

## Kill-Kriterien für Contract-Erweiterungen

- **Kein `fm-stereo-rds-mpx`-Sheet**, wenn G-MPX-0 scheitert oder G-MPX-2
  nicht reproduzierbar PASS ist.
- **Kein gemeinsamer QN8027/Si4713-Contract**, wenn G-IC-1 nur eine
  Überschrift über inkompatible Audio-/RDS-Interfaces erzeugt.
- **Kein Variantentransfer**, wenn der Claim ESP32 Classic, ESP32-S3 und
  ESP32-C3 nicht separat belegt.
- **Kein Field-Gate**, solange G-LEGAL-1 oder ein geschirmtes Lab offen ist.
- `UNKNOWN` allein ist kein automatisches STOP; die oben präregistrierte
  Kombination aus fehlender Voraussetzung und konkretem Kill entscheidet.

## Reuse-Ergebnis

- `fm-rds`: **reused**, mit zwei Implementierungsfamilien
  (Software-MPX und Sender-IC-RDS).
- `esp-i2s-audio`: **reused**, mit explizitem S3-/Classic-Scope.
- `esp32-apll-fm-tx`: **not helped / contrast**; falscher RF-Contract für
  S3-I2S-MPX und externe QN8027/Si4713.
- Neue Contracts: **nicht erstellt**; zwei Kandidaten bleiben gated.
