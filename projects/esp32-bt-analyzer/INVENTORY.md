# Project Inventory: esp32.bt-analyzer

```yaml
project_id: esp32-bt-analyzer
updated: 2026-11-13
reviewed_commit: 0352824
fw_pin: "0.3.19"
profile: lab-tool
pilot_order: [esp-hub-telemetry, esp32-s3-silicon, esp32-s3-usb-wifi-coex, esp-usb-host]
```

Ursprungsrepo: [esp32.bt-analyzer](https://github.com/MPunktBPunkt/esp32.bt-analyzer).  
Methods: [bt-passive-host-sniff](../../methods/bt-passive-host-sniff.md) (HCI semantics).  
Lab: `.88` Central · `.89` Peripheral peer · `.87` Classic+BLE.

**Match (Signal → Slug):**

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Hub register / OTA | `esp-hub-telemetry` | Application |
| YD-ESP32-S3 N8R2 / PSRAM | `esp32-s3-silicon` | Application |
| WiFi + BT coexistence (S3 BT13 stress) | `esp32-s3-usb-wifi-coex` | BT13 stress MEASURED |
| WiFi STA + Classic ACL (D1 HCI agent) | `esp-wifi-bt-coex` | Application — wifi_ps sweeps MEASURED |
| UART-HCI-Offload (Ausweg aus dem Coex-Boden) | `esp-hci-uart-controller` | nicht gebaut — Desk `esp32-hci-controller-2026-foreign` |
| Car-Netz hinter Handy-Hotspot (A6/B1) | `esp-tailscale-client` / `esp-wireguard` | nicht gebaut — Desk `esp32-car-network-2026-foreign` |
| A2DP über BlueZ + HCI TCP | `bluetooth-a2dp` | Application — single path / dual relay MEASURED |
| BCL über RFCOMM | `bmw-bcl` | Application — lab TEST |
| Pairing-Agent auf .108 (Handy→.131, HU→.87) | `bluez-pairing-agent` | Application — HU-Kopplung A6 MEASURED |
| BMW-HU über BT (SDP, A2DP-SEPs, AVRCP, HFP) | `bmw-nbt-evo` | Application — A6-Capture dekodiert |
| On-chip VHCI HCI | Method `bt-passive-host-sniff` | Anker |
| USB OTG + dongle | `esp-usb-host` | legacy optional |
| Classic on-chip S3 | `bluetooth-a2dp` | **REJECTED** |
| RF Air | — | **BT15 deferred** |

## Übersicht

| Slug / Artifact | Status | Coverage |
|-----------------|--------|----------|
| On-chip VHCI BT1–BT3 | MEASURED | lab 0.2.6+ |
| BTAC / JSONL / PCAPNG BT4/7/8 | MEASURED | `tools/lab_run_gates.py` |
| BLE peer + connect BT9/11 | MEASURED | F_ONCHIP |
| Classic discoverable BT10 | MEASURED (HCI path) | `.87` |
| PSRAM ring / lossless BT5/6 | MEASURED | S3 512 slots |
| `esp-usb-host` dongle path | deferred/legacy | A_OBSERVE |
| HCI over TCP A1–A5 (`hci-agent-esp32`) | MEASURED | 0.3.16–0.3.18 |
| Coex budget (`wifi_ps`) / Coex API | MEASURED / UNKNOWN | 0.3.17–0.3.19 |
| A2DP relay | MEASURED (choppy) | 0.3.16 |
| BCL synth / Dummy-HU SDP | TEST | 0.3.18 |
| Pairing-Agent `bt-pair-agent` | MEASURED (HU-Kopplung A6) | `tools/bt_pair_agent.py` |
| BMW-HU BT-Verhalten | MEASURED (state A/B, ein Termin) | `tools/btsnoop_decode.py` · `FIELD_B1_FROM_A6_*` |

## Coverage-Lücken

| Bereich | Status | Nächster Schritt |
|---------|--------|------------------|
| External audit sign-off | partial | BT14 reviewer |
| Classic×Classic peer | limited (one Classic board) | second ESP32 or phone |
| Profile Flavors (GATT/HOGP/FTMS/Classic) | desk only | [`host-profiles-2026-desk`](../../audits/esp32-bt-analyzer-host-profiles-2026-desk/) → upstream Flavor Bus |
| RF/Air | out of scope | BT15 separate |
| BMW HU über BT — BCL auf RFCOMM (B2) | UNKNOWN | HFP off, B2-A ch 6 + 5, B2-B (`CAR_FIELD_1H.md`) |
| Coex-API-Wirkung | UNKNOWN | `lab_hci_coex_ab.py` |
| BLE-HR-Relay über BlueZ (zwei HCI) | not started | `ble-hr-relay` Fallstricke; zwei-HCI ≠ Dual-Role |
