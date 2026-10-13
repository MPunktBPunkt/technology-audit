# Project Application: fm-rds in esp-fm-rds-node

```yaml
project_id: esp-fm-rds-node
tech_slug: fm-rds
status: active
sheet: ../../../technologies/fm-rds/SHEET.md
audit: ../../../audits/esp-fm-rds-node-2026-foreign/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

Das vorhandene [`fm-rds`](../../../technologies/fm-rds/SHEET.md)-Sheet wird
für RDS-Gruppen, PS/RT und den 57-kHz-Anteil wiederverwendet. Ebene B hat zwei
getrennte Implementierungsfamilien:

1. **Software-MPX:** PiratESP32 assembliert RDS-Bits und mischt BPSK bei 57 kHz
   in einen Stereo-MPX-DAC-Stream. Der nachfolgende RF-Modulator ist extern.
2. **Sender-IC:** QN8027 oder Si4713 erzeugen FM-Stereo/RDS im externen Chip;
   ESP-Code liefert Steuerdaten und Audio.

Diese Application macht aus beiden Familien keinen neuen gemeinsamen
Hardware-Contract.

## Ebene A — wiederverwendeter Contract

- RDS bleibt ein vorhandener Protokoll-/Metadatencontract.
- Generische Gruppen-, PI/PTY-, PS-/RT- und 57-kHz-Aussagen gehören in das
  bestehende Sheet, nicht in diese Application.
- In dieser Kampagne wurde kein A-Delta in Technology Sheets geschrieben.

## Ebene B — Projektimplementierungen

### B1: Software-MPX (ESP32-S3 / Classic im PiratESP32-Code)

```text
PS/RT/PI/PTY → RDSAssembler → Bit-FIFO
  → 1187,5-symbol/s BPSK @ 57 kHz
  → Mix mit L+R, 19-kHz-Pilot und (L-R)@38 kHz
  → I2S-DAC-MPX → externer FM-Modulator (nicht im Repo)
```

| Pfad | Rolle | Evidence |
|------|-------|----------|
| [`RDSAssembler.cpp`](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/RDSAssembler.cpp) | Gruppen 0A/2A, PI/PTY/PS/RT, CRC/Bitstream | `EVID-FMRDS-2026-10-13-003` |
| [`RDSSynth.cpp`](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/RDSSynth.cpp) | RDS-Symbol-/BPSK-Synthese | `EVID-FMRDS-2026-10-13-003` |
| [`MPXMixer.cpp`](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/MPXMixer.cpp) | MPX-Mix aus Audio, Pilot, Stereo und RDS | `EVID-FMRDS-2026-10-13-002` |
| [`Config.h`](https://github.com/MarcFinns/PiratESP32-FM-RDS-STEREO-ENCODER/blob/58e16970e3c05cb69d4ae8d51aba6101225f4505/Config.h) | S3-/Classic-Pins, RDS-Amplitude, 44,1/176,4-kHz-Pfad | `EVID-FMRDS-2026-10-13-004` |

### B2: QN8027

| Repo / Chip-Scope | Implementierung | Evidence |
|-------------------|-----------------|----------|
| [PixelRadio](https://github.com/thomastech/PixelRadio/tree/22a3c3d9be38d090509765cfc1c4d0c015f5ebb0), Classic ESP32 | QN8027 über I2C; PS/RT aus Local, Serial, MQTT oder HTTP mit Priorisierung | `EVID-FMRDS-2026-10-13-008`–`011` |
| [esp32_fmdevkit](https://github.com/dragon-engineer/esp32_fmdevkit/tree/f8416d27d4bd5e016d3618a8955cb30e093fbb6d), Classic ESP32 | QN8027, optionaler RDS-Paging-/A2DP-Metadatenpfad; im Beispiel standardmäßig deaktiviert | `EVID-FMRDS-2026-10-13-020`–`021` |
| [ESP32C3_FM_TRANSMITTER](https://github.com/emoestudio/ESP32C3_FM_TRANSMITTER/tree/89e15ecc685345bd09ffc6144ae0cd63ae41983e), ESP32-C3 | QN8027-I2C; PS/RT zyklisch; Web/Serial/NVS | `EVID-FMRDS-2026-10-13-023`–`025` |

Der C3-Pfad steuert den QN8027 und verwendet dessen externen Analogaudioeingang.
Er belegt weder S3-I2S-MPX noch Classic-APLL-RF.

### B3: Si4713

| Repo | Implementierung | Evidence |
|------|-----------------|----------|
| [fm-streamer](https://github.com/russery/fm-streamer/tree/cabc20d2600a7c72ae3d6bafb1702176f96de124) | Si47xx-I2C; PS/RT; README beschreibt DAC→Analog, gepinnter Code aktiviert Digitalinput | `EVID-FMRDS-2026-10-13-012`–`015` |
| [Adafruit-Si4713](https://github.com/adafruit/Adafruit-Si4713-Library/tree/fa38460fb0303d7951ff6a20828d707d13225d30) | Basistreiber für Tune, Power, RDS-Properties, PS und Buffer | `EVID-FMRDS-2026-10-13-016`–`017` |
| [DynamicRDS](https://github.com/RaA-BLNET/Adafruit-Si4713-DynamicRDS/tree/638dce6f64ea403462df31a1dc9aae58ffda27b5) | Serial-gesteuerte PS-/RT-Aktualisierung | `EVID-FMRDS-2026-10-13-018` |

## Konfiguration und Parameter (Desk)

| Familie | Parameter im Snapshot | Status |
|---------|-----------------------|--------|
| PiratESP32 | PI/PTY/TP/TA/MS, PS/RT; 0A/2A; RDS-Toggle und Amplitude | `FACT` (Code) |
| QN8027 | Frequenz, FM-/Pilot-/RDS-Deviation, Stereo/Mono, Leistung, PS/RT | `FACT` (Code) |
| Si4713 | Tune/Power, TX-Komponenten, PI, PS-Mix/Repeat/FIFO, PS/RT-Buffer | `FACT` (Code) |
| Gleiches Laufzeit-/FIFO-Verhalten QN8027 vs. Si4713 | nicht belegt | `UNKNOWN` |

## Ebene C — Lab-/Field-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| PiratESP32-MPX wird von einem ausgewählten externen Modulator als Stereo+RDS dekodiert | `EVID-FMRDS-2026-10-13-027` | `UNKNOWN` |
| QN8027-Pfade liefern im geschirmten Aufbau reproduzierbares PS/RT | `EVID-FMRDS-2026-10-13-028` | `UNKNOWN` |
| Si4713-Pfade liefern im geschirmten Aufbau reproduzierbares PS/RT | `EVID-FMRDS-2026-10-13-029` | `UNKNOWN` |
| Field-/Antennenbetrieb ist validiert oder zulässig | `EVID-FMRDS-2026-10-13-030` | `UNKNOWN` |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| — | Keine Messung durchgeführt; Lab und Field `UNKNOWN` |

## Abweichungen vom „Lehrbuch“

- PiratESP32 liefert fertiges **Basisband-MPX**, aber keinen RF-Träger.
- QN8027 und Si4713 kapseln Stereo-/RDS-Erzeugung im Sender-IC; ihr
  Steuervertrag ist nicht identisch.
- PixelRadio priorisiert Serial vor MQTT und HTTP; das ist Ebene B, kein
  allgemeines RDS-Verhalten.
- Der direkte ManojBhakarPCM-Upstream ist 404/stale. Vendorte QN8027-Kopien
  in PixelRadio und C3 bleiben auf deren Commits belegbar, ersetzen aber
  keinen verfügbaren kanonischen Upstream.

## Offene Fragen

- Welcher externe Modulator akzeptiert den S3-I2S-DAC-MPX-Pfad?
- Ist ein gemeinsamer QN8027/Si4713-Minimalcontract nützlich oder verdeckt er
  wichtige Chipunterschiede?
- Wie werden RDS-A/B-Toggle, Wiederholrate und FIFO/Handshake je Pfad im Lab
  validiert?

## Verwandte Applications / Gates

- [`esp-i2s-audio`](esp-i2s-audio.md)
- Präregistrierte Gates in [FOLLOW-ON-IDEAS](../FOLLOW-ON-IDEAS.md)
- Frühere Reuse-Anwendung: [`pi-fm-tx/applications/fm-rds`](../../pi-fm-tx/applications/fm-rds.md)
