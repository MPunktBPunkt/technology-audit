# Project Application: bmw-nbt-evo in esp32-bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
upstream: https://github.com/MPunktBPunkt/esp32.bt-analyzer
maturity:
  technology: R2
  implementation: R1
  field_evidence: R1   # A6+B1A + B2 state A: SDP/A2DP/AVRCP MEASURED; ch5/6 accept empty; BCL UNKNOWN
  reusability: W1
updated: 2026-11-13
```

## Rolle im Projekt

Bluetooth-Seite der NBT Evo am F20, gemessen über `.87` (spielt „Smartphone“) und BlueZ auf `.108`.
Ergänzt die USB-Host-Applications ([pidrive](../../pidrive/applications/bmw-nbt-evo.md),
[hu-probe](../../hu-probe/applications/bmw-nbt-evo.md)) um HU-SDP, A2DP-/AVRCP-Verhalten und HFP-SLC.
Hebt die PiDrive-Doku-Claims im Sheet (Abschnitt „Bluetooth-Verhalten“) auf `MEASURED` bzw. `REJECTED`.

## Architektur / Datenfluss

```text
BMW HU (D4:36:39:CF:E1:B5, ALPS-Modul) ──BR/EDR──► .87 (C8:C9:A3:CB:37:96, hci2)
                                                   │ HCI over TCP
                                                   ▼
                                    bluetoothd + PipeWire (INFERRED) auf .108
                                                   │ btmon -w
                                                   ▼
                          tools/btsnoop_decode.py → docs/evidence/FIELD_B1_FROM_A6_*
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `docs/evidence/FIELD_A6_HU_20261113T062824Z.*` | Pairing + btsnoop (192 s, 945 Records) |
| `docs/evidence/FIELD_B1_FROM_A6_20261113T062824Z.{md,json}` | Dekodierte SDP-/RFCOMM-/AVDTP-/AVRCP-Tabelle |
| `docs/evidence/FIELD_B2_20261113T154728Z.*` | B2-A ch5/6 + B2-B observe-only (HFP-off) |
| `tools/btsnoop_decode.py` | Passiver Decoder (btmon 2001 / H4 1002) |
| `docs/analysis/HFP_SLC_A6_20261113.md` | HFP-SLC-Abbruch |
| `tools/lab_hfp_stack.py` | Stack-Diagnose `.108`, HFP an/aus |
| `tools/field_b1_b2.py` | Feld-Orchestrierung B1/B2 + btmon |

## Konfiguration und Parameter

| Parameter | Wert | Status |
|-----------|------|--------|
| HU-Class | `0x340408` (Audio/Video Hands-free) | `MEASURED` |
| Pairing | Numeric Comparison (RequestConfirmation) | `MEASURED` |
| SDP-Provider | `ALPS_*` (Records `ALPS_HFM`, `ALPS_MNS_SERVER1`) | `MEASURED` |

HU-SDP (Kanal → Dienst):

| RFCOMM / PSM | Dienst | Profil |
|---|---|---|
| ch 1 | MAP-MNS | MAP 1.2 |
| ch 2 | HFP HF | HFP 1.6 |
| ch 5 | „SPP Server 0“, UUID `00000000-deca-fade-deca-deafdecacaff` | 1.2 |
| ch 6–10 | „SPP Server 1–5“, SPP `0x1101` | SPP 1.2 |
| ch 11 | OPP | 1.2 |
| PSM 25 | A2DP Sink | A2DP 1.3 |
| PSM 23 | AVRCP CT | AVRCP 1.5 |
| – | PnP | – |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| HU koppelt mit `.87` per Numeric Comparison; Agent auf `.108` bestätigt | `FIELD_A6_HU_20261113T062824Z` | `MEASURED` |
| HU-SDP wie Tabelle oben (6 SPP-artige Server, ch 5 `deca-fade`, ch 6–10 `0x1101`) | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` (state A/B) |
| AVRCP-Version HU = **1.5** (CT, kein TG-Record) | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` |
| HU nutzt AVRCP **Browsing** (GetFolderItems Media-Player-Liste auf PSM `0x1B`) | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` |
| HU nutzt GetElementAttributes, GetPlayStatus, Player-Settings, RegisterNotification; registriert abgelehnte Events (`0x05 0x06 0x07 0x09 0x0c`) wiederholt | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` |
| HU sendet Pass-through PLAY/FORWARD/BACKWARD an unseren TG | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` |
| A2DP-Sink-SEPs: SBC (alle Modi, 44,1/48 kHz, **Bitpool 2..53**), AAC (MPEG-2/4 LC, VBR), MPEG-1,2; alle mit SCMS-T + Delay Report | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` |
| HFP HF 1.6, `AT+BRSF=255`, `AT+BAC=1,2` (mSBC) | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` |
| HU bricht HFP-SLC ab, wenn AG kein Three-Way meldet und `AT+CHLD=?` mit ERROR beantwortet; Retry alle 20–35 s | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` (gegen unseren AG) |
| HU öffnet in state A (idle, keine Phone-App) keinen SPP-/`deca-fade`-Kanal | `FIELD_B1_FROM_A6_20261113T062824Z` | `MEASURED` (192 s, ein Termin) |
| Phone→HU RFCOMM ch **6** und ch **5**: HU **UA**, 0 Payload (state A, HFP-off) | `FIELD_B2_20261113T154728Z` | `MEASURED` Transport; BCL `UNKNOWN` |
| HU→unser SPP „BMW Connected“ in state A (HFP/Apps off) | `FIELD_B2B_20261113T1653Z` | `REJECTED` inbound (180 s) |
| HFP-AG-off entfernt Kanal-13-Rauschen vollständig | `FIELD_B2_20261113T154728Z` | `MEASURED` (0× `AT+`) |
| HU-Kanal für BCL / first UIH / BCL-Initiator | — | `UNKNOWN` (next: state C/D) |
| Nutzer des `deca-fade`-Dienstes (MyBMW? Connected Classic?) | — | `UNKNOWN` (Server akzeptiert, sendet nichts ohne App) |
| Gleiche UUID-Menge (1101, 111e, 1105, 110b, 110e, 1133, `deca-fade`) + zusätzlich `d31fbf50-5d57-2797-a240-41cd484388ec` bei einer HU im Fremd-Logcat | BimmerGestalt `IDriveExperiments/logcat.crash` Z. 41790–41798 (2022-03-29, Gerät `…:49:60`) | `INFERENCE` (secondary; HU-Identität im Log nicht genannt) |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-11-13 A6 | HU startete A2DP (START) 11 s nach OPEN, ohne dass Media-Pakete flossen; wir SUSPEND nach 5,5 s |
| 2026-11-13 A6 | Unser AG meldete HFP 1.9 + Super-Wideband → Stack auf `.108` vermutlich PipeWire native (Diagnose offen) |
| 2026-11-13 A6 | Bimmer-Fremdlog zeigt `d31fbf50-…` zusätzlich — fehlt im F20-SDP state A/B |
| 2026-11-13 A6 | HU AVRCP-CT features `0x004d` ohne Browsing-Bit, nutzt trotzdem PSM `0x1B` |
| 2026-11-13 B2 | ch5/6 accept+empty; B2-B negativ; nach HU-Off Reconnect remote-init A2DP/AVRCP; Pass-Through PLAY1/FWD6/BWD7 |

## Abweichungen vom „Lehrbuch“

- HFP: HU sendet `AT+CHLD=?`, obwohl der AG kein Three-Way meldet (HFP: nur wenn beide unterstützen), und trennt bei ERROR.
- SPP: sechs Server mit gleichem bzw. Vendor-UUID. Android `createRfcommSocketToServiceRecord(0x1101)` landet auf dem ersten passenden Record (ch 6), nicht auf ch 5.

## Offene Fragen

- Welche App nutzt `deca-fade` (ch 5)? Phone-HCI-Snoop mit MyBMW / Connected Classic aktiv.
- Erscheint `d31fbf50-…` in state C/D (App aktiv) oder ist es eine andere Variante?
- Nimmt die HU auf ch 6 bzw. ch 5 einen Phone-SABM an (UA vs DM) und spricht sie zuerst?
- Wählt die HU AAC, wenn die Source es anbietet? (AAC passt unter die Coex-Decke, SBC 53 liegt auf ihr.)

## Verwandte Applications / Methods

- [bmw-bcl](bmw-bcl.md) — BCL-Messkette, B2-Plan
- [bluez-pairing-agent](bluez-pairing-agent.md) — A6-Pairing
- [bluetooth-a2dp](bluetooth-a2dp.md) — Coex-Budget vs SBC-Bitpool
- [pidrive bmw-nbt-evo](../../pidrive/applications/bmw-nbt-evo.md) · [hu-probe bmw-nbt-evo](../../hu-probe/applications/bmw-nbt-evo.md)
