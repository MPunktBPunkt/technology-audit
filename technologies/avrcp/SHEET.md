# Technology Sheet: AVRCP

```yaml
slug: avrcp
title: AVRCP
primary: C
tags: [bluetooth-classic, metadata]
type: protocol
status: active
seen_in: [pidrive, esp32-bt-gateway, esp32-a2dp, bluetooth-stack, espble, a2dpsinkhfpclient, esp-idf-classic-bt, esp32-a2dp-codecs, esp32-a2dp-source, esp32-bt-iap, esphome-a2dp-sink]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W3
pilot: audits/pidrive-2026-radio-bt
```

Nur Ebene **A**. Konkretes HU-Tasten-/Browse-Verhalten → Host-Sheet / Application C.  
**Stack-Scope:** BlueZ vs. Bluedroid vs. HCI-Host vs. EspBle Classic getrennt.

## Kurzfassung

Audio/Video Remote Control Profile über AVCTP: Pass-Through (Play/Pause/Next/…), Metadata, Notifications, optional **Absolute Volume**, optional **Browsing**, ab AVRCP **1.6** optional **Cover Art** (BIP/OBEX). Spec erlaubt Remote Control von einem getrennten Controller — **Espressif/Bluedroid und die meisten Libraries koppeln AVRCP stark an A2DP**.

## Abgrenzung

- **Ist:** Classic-BT Remote Control + Metadata (+ Browse / Cover Art / Abs Volume wo belegt).
- **Ist nicht:** A2DP-Audio; HFP Call-Control; MPRIS; lokale HU-Tasten ohne AVRCP.
- **Rollen:** **Controller (CT)** steuert / fragt ab; **Target (TG)** empfängt / antwortet. Gateway gegen HU ist typisch **Source + TG** (HU = CT).

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | App / Infotainment | Events, Meta, Menü, Volume-UI |
| unten | AVCTP Control / Browsing; Cover Art über BIP/OBEX | IDF-Versionsgate |
| lateral | A2DP | in Praxis fast immer gekoppelt |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Standalone AVRCP ohne A2DP in Libraries | `REJECTED` (Praxis) | Spec erlaubt es; Bluedroid/Libraries koppeln stark (pschatzmann explizit) |
| Alle HU-Tasten = AVRCP | `REJECTED` | viele lokal |
| Metadata = volle Playlist | `REJECTED` | oft nur aktueller Track |
| Absolute Volume immer | `REJECTED` | Peer muss Feature anbieten; viele ältere Android-Geräte nicht |
| Cover Art ohne IDF ≥5.4 / PSRAM | `REJECTED` / Gate | Espressif Beispiel: AVRCP 1.6 + `CONFIG_SPIRAM` für Stream+Decode |
| AVRCP-TG als Source vollständig | `HYPOTHESIS` / Gate | Community: oft unvollständig; EspBle: Target-Notifications außer Volume im bundled Host eingeschränkt |
| BlueZ Target = volles Browse | `REJECTED` | typischer Gateway-Treiber |
| Altes Repo „Metadata unsupported“ = heute wahr | `REJECTED` still | fanthos/esp32-bt-iap (2018) historisch; IDF hat CT-Metadata-Beispiele |
| ESP-A2DP-Lib = Cover Art + Browse | `UNKNOWN` / Gate | Desk: Meta+Pass-Through üblich; Cover Art = IDF-Beispielpfad |

## Transfer

Gateway-Stufen: Pass-Through → Meta → Abs Volume → Browse → Cover Art. EspBle als CT/TG-API-Referenz; Espressif `avrcp_ct_*` / `avrcp_absolute_volume` als SoT für Stack-Capabilities; pschatzmann für Arduino-Sink/Source-Praxis.

### Projektstart-Checkliste

- [ ] CT vs. TG Rollen (HU meist CT)
- [ ] A2DP-Kopplung akzeptieren oder Standalone-Gate
- [ ] Feature-Stufe wählen (Pass-Through / Meta / AbsVol / Browse / Cover Art)
- [ ] IDF-Version für 1.6 Cover Art (≥5.4) + PSRAM
- [ ] Peer Abs-Volume Capability messen
- [ ] Application + `seen_in`

## Referenzen

- Bluetooth AVRCP Spec (SIG); Cover Art / BIP
- Espressif: `examples/bluetooth/bluedroid/classic_bt/avrcp_*`
- Desk: `espble`, `esp-idf-classic-bt`, `esp32-a2dp`, `a2dpsinkhfpclient`
- PiDrive / Gateway Planung

## Offene Fragen

- NBT-Evo Browse-Subset und Abs-Volume-Support?
- EspBle Target-Notification-Limits im Lab vs. custom Classic host?
