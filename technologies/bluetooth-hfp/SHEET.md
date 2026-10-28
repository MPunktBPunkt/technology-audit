# Technology Sheet: Bluetooth HFP (Hands-Free)

```yaml
slug: bluetooth-hfp
title: Bluetooth HFP (Hands-Free Profile)
primary: C
tags: [esp-idf, classic-bt, audio]
type: protocol
status: active
seen_in: [bt-classic-profile-refs]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. A2DP-Mux und Chip-Scope → Applications / `bluetooth-a2dp` / `bt-dual-mode-coex`.

## Kurzfassung

Hands-Free Profile: **HF** (Hands-Free Unit, z. B. Auto/Headset) spricht mit **AG** (Audio Gateway, typ. Phone) über RFCOMM/AT; Sprachpfad über **SCO/eSCO** mit **CVSD** und optional Wideband (**mSBC**/neuere Codecs). Call-Control und Audio-Pfad sind getrennte Verträge — A2DP ersetzt keines von beiden.

## Abgrenzung

- **Ist:** HFP HF/AG, Call-Control, SCO/eSCO, Codec-Wahl, PCM- vs HCI-Audio-Pfad.
- **Ist nicht:** A2DP/AVRCP; HSP (älteres Headset-Profil — eigener Kontrast); BLE Audio; generisches „Phone Audio“.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | UI / Telefonie-App | Dial, Answer, Reject, Volume, VR |
| unten | Stack (Bluedroid / BTstack / …) | `esp_hf_*` bzw. `hfp_hf_*` |
| lateral | SCO Audio | PCM-GPIO **oder** HCI-SCO + External Codec |
| lateral | A2DP | gemeinsame I2S/DAC → Mux/Suspend-Policy |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| A2DP deckt Anrufe ab | `REJECTED` | eigener SCO-Pfad + AT |
| HFP HF = HSP | `REJECTED` | Fremd-Repo-Namen können irreführen |
| mSBC-Pfad decodiert still CVSD | `REJECTED` / Gate | Codec-State prüfen (`CONNECTED` vs `CONNECTED_MSBC`) |
| PCM-GPIO und HCI-SCO sind austauschbar ohne Kconfig | `REJECTED` | IDF: `BT_HFP_AUDIO_DATA_PATH_*` |
| Call startet immer automatisches A2DP-Suspend | `HYPOTHESIS` | oft nur VR/explizit; sonst I2S-Konflikt |
| HFP auf ESP32-S3 wie Classic ESP32 | `UNKNOWN` / Gate | Classic BR/EDR chip-abhängig |
| AG und HF APIs sind spiegelbar 1:1 | `REJECTED` | unterschiedliche Rollen/AT-Oberflächen |

## Transfer

Car/Gateway: HF + Media braucht **Audio-Mux-Policy** und Sync-Conn-Budget. Phone-Emulation: AG. Stack-Wahl Bluedroid vs BTstack ändert API, nicht das Profil-Contract.

### Projektstart-Checkliste

- [ ] Rolle HF vs AG geklärt
- [ ] Audio-Pfad: PCM vs HCI + External Codec
- [ ] Codec: CVSD / Wideband (mSBC) Evidence-Plan
- [ ] Call-Control-Oberfläche (min. answer/reject/dial/volume)
- [ ] A2DP parallel? → Mux/Suspend + `bluetooth-a2dp`
- [ ] Chip Classic-fähig? → `bt-dual-mode-coex`
- [ ] Application + `seen_in`

## Referenzen

- ESP-IDF `examples/.../classic_bt/hfp_hf`, `hfp_ag`
- a2dpSinkHfpClient (HF + I2S Mux)
- EspBle Classic HFP Client/AG
- btstack `hfp_hf.c` / `hfp_ag.c`; atomic14 `esp32-hsp-hf` (HFP trotz Name)

## Offene Fragen

- Einheitliche Call→A2DP-Suspend-Policy für Gateway-Produkte?
- LC3-SWB auf ESP-IDF: wann produktiv vs CI-only?
