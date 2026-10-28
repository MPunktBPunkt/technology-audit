# Technology Sheet: Bluetooth A2DP

```yaml
slug: bluetooth-a2dp
title: Bluetooth A2DP
primary: C
tags: [bluetooth-classic, streaming]
type: protocol
status: active
seen_in: [pidrive, esp32-bt-gateway, esp32-a2dp, bluetooth-stack, espble, a2dpsinkhfpclient, esp-idf-classic-bt, esp32-a2dp-codecs, esp32-a2dp-source, esp32-bt-iap, esphome-a2dp-sink, squeezelite-esp32]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/pidrive-2026-radio-bt
```

Nur Ebene **A**. Host-/Fahrzeugverhalten → Application C oder Host-Sheet.  
**Stack-Scope:** Profil spezseitig gemeinsam; **Implementierung** Pi BlueZ/PipeWire ≠ ESP Bluedroid ≠ HCI-Host-Stack — Evidence getrennt (G17-analog).  
**Chip-Scope (ESP on-chip):** **Classic ESP32** (BR/EDR). S2/S3/C3/… ohne Classic = `REJECTED`. Upstream-Flag `ESP32-S31` in IDF-Beispielen = Compile-Zelle, Caps bis Lab `UNKNOWN`.

## Kurzfassung

Advanced Audio Distribution Profile: punkt-zu-punkt Streaming komprimierter Audio (Default **SBC**) zwischen Source und Sink. Optionale Zusatz-Codecs (AAC, aptX*, LDAC, Opus, …) brauchen gepatchte IDF-/Bluedroid-Pfade und oft PSRAM/CPU-Headroom — nicht der Standard-Contract.

## Abgrenzung

- **Ist:** Classic-BT Audio-Transport (Source/Sink-Rollen).
- **Ist nicht:** AVRCP; HFP/HSP (→ `bluetooth-hfp`); BLE Audio; USB-Audio; Mix/Routing (PipeWire); A2DP auf BLE-only SoCs; Dual-Mode-Budget (→ `bt-dual-mode-coex`).
- **Grenzt an:** Multi-Codec-Forks = Implementation-Variante derselben Profile-Klasse (Application + Fallstricke), kein neuer Profile-Slug pro Codec.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | PCM/Encoder/Decoder | SBC Default; weitere Codecs verhandeln |
| unten | Classic BT Controller + Host-Stack | Bluedroid / BlueZ / HCI-Host |
| lateral | AVRCP | oft gleiches Pairing, stark gekoppelt in Libraries |
| lateral | HFP | Phone-Audio; eigener Profil-Contract (`bluetooth-hfp`); gemeinsame I2S ⇒ Mux/Suspend-Policy |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| A2DP-Sink ohne Default-Route = hörbar | `REJECTED` | PipeWire/pactl Profil setzen |
| Ein Gerät gleichzeitig Sink und Source | `REJECTED` | Classic-Rollen am ESP typ. exklusiv |
| ESP32-S3 on-chip A2DP | `REJECTED` | kein BR/EDR-Controller |
| AAC/aptX/LDAC „überall“ | `REJECTED` | IDF-Patch/Fork + oft PSRAM; SBC bleibt Baseline |
| AAC ohne PSRAM auf Classic | `REJECTED` / Gate | cfint: AAC braucht WROVER/PSRAM @80 MHz Flash |
| Linux BlueZ behält alte Codec-Liste | `FACT` | Cache unter `/var/lib/bluetooth/…/cache/` — Gerät vergessen/neu pairen |
| WiFi + Classic Coex gratis | `HYPOTHESIS` | Gate; Dual-Host BLE+Classic oft experimental |
| Pi BlueZ beweist ESP-Gateway | `REJECTED` | getrennte Stack-Evidence |
| Externer HCI „ESP32“ = Bluedroid-FW | `REJECTED` | Controller ≠ Profile-Host |
| Multi-Codec-Fork = drop-in Arduino-Library | `REJECTED` | oft forked IDF tree |

## Transfer

Gateway/`esp32-bt-gateway`: Rolle **Source** gegen HU-Sink; Referenz-Libraries: pschatzmann (Sink+Source), EspBle Classic (CT/TG + Dual-Host experimental), Espressif `a2dp_source*` / `a2dp_sink_stream*`. Codec-Forks nur wenn Peer sie braucht — sonst SBC.

### Projektstart-Checkliste

- [ ] Source vs. Sink (kein stilles Dual)
- [ ] Stack: BlueZ / Bluedroid / HCI-Host / EspBle-namespaced Classic
- [ ] Chip Classic BR/EDR?
- [ ] Codec: SBC only vs. patched multi-codec + PSRAM
- [ ] AVRCP + optional HFP (`bluetooth-hfp`) als eigene Slugs/Apps; Audio-Mux planen
- [ ] Classic-only vs BTDM → `bt-dual-mode-coex`
- [ ] Coexistence WiFi/BLE als Gate
- [ ] Application + `seen_in`

## Referenzen

- Bluetooth A2DP / SBC (SIG)
- Desk: `esp32-a2dp`, `espble`, `a2dpsinkhfpclient`, `esp-idf-classic-bt`, `esp32-a2dp-codecs`, …
- Planung: `esp32.bt-gateway`

## Offene Fragen

- NBT-Evo Bitpool/Buffer Defaults?
- ESP32-S31 Classic-Caps im Lab?
