# Method: BT USB-HCI Observe Baseline

```yaml
slug: bt-usb-hci-observe-baseline
title: BT USB-HCI Observe Baseline (ESP32-S3 Host + Dongle)
status: active
tags: [bluetooth, usb, hci, lab, esp32s3, preregistered]
```

## Zweck

Vor RF-/MITM-/Profile-Claims eine **reproduzierbare L1-Baseline**: ESP32-S3 als USB Host enumeriert einen USB-Bluetooth-Dongle, klassifiziert USB-HCI-Endpoints und erfasst Raw-Frames (Timestamp/Richtung/Typ/Payload) Richtung Debian.

Epistemik: Ergebnis = **Host↔Controller (HCI)**, nicht Air/PHY, nicht Phone↔DUT.

## Voraussetzungen

- ESP32-S3 mit USB OTG (z. B. YD-ESP32-S3 N8R2), Instrument-FW `esp32.bt-analyzer`
- Self-powered USB Hub / bus-powered Dongle mit eigener Versorgung (DevKit OTG oft ohne 5 V)
- Ein Dongle-Typ pro Kampagne: **BLE** oder **Classic** (nicht mischen)
- Optional zweiter S3 / classic ESP32 nur nach Topologie-Registry (Stimulus / Endpoint-Ref)
- Serial = UART/COM, nicht OTG-Port während Host-Betrieb

## Topologie-IDs (Instrument-Repo)

| ID | Bedeutung |
|----|-----------|
| `A_OBSERVE` | Dongle → S3 USB Host → WiFi → Debian |
| `B_STIMULUS` | S3 Host ↔ S3 Device synthetisches HCI (kein Funk) |
| `C_DUAL_DONGLE` | zwei Observe-Nodes + zwei Dongles |
| `D_ENDPOINT_REF` | classic ESP32 on-chip Endpoint (L2), getrennt labeln |
| `E_INJECT` | HTTP-Inject Pipeline-Smoke ohne Dongle |

Quelle: `esp32.bt-analyzer` → `docs/LAB_METHODS.md`.

## Ablauf

1. **Inventory freeze:** Node-FW/Chip/IP snapshot (`lab_inventory_snapshot.py`).
2. **Enum-Sanity (BT1):** `/api/usb/status` → VID/PID/speed/interfaces/endpoints.
3. **HCI map (BT2):** `hci.detected=true` nur bei Wireless Controller `0xE0/0x01`; sonst Fail der Kampagne A.
4. **Raw capture (BT3):** Frames mit `seq`, `ts_us`, `dir`, `type`, `endpoint`, `payload_hex`; Drops/Gaps sichtbar.
5. **Drain:** JSONL speichern; später PCAPNG nur mit HCI-Linktype (nie RF).
6. **Claim boundary** schreiben (In/Out). Kein Air-/MITM-Claim.
7. BLE- vs Classic-Dongle = **getrennte** Kampagnen (BT9 vs BT10).

## Artefakte

| Artefakt | Naming |
|----------|--------|
| Inventory JSON | `LAB_INVENTORY_<UTC>.json` |
| Observe run | `LAB_BT_HCI_OBSERVE_<UTC>.json` + MEASURED.md |
| Inject smoke | `LAB_BT_INJECT_<UTC>.json` (Topology E only) |
| Capture JSONL | session-scoped under instrument `docs/evidence/` |

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Enum | DUT present, FS | crash / no device |
| HCI detect | `hci.detected` on known BT dongle | false positives on MSC/HID gadgets |
| Frames | ≥1 raw frame with ts/seq | undocumented inject as „dongle HCI“ |
| Loss visibility | drops/gaps explicit | silent corruption |
| Docs | FW pins + topology ID + boundary | „Bluetooth works“ / HCI=RF |

## Fallstricke

- S3 **ohne** Classic on-chip → Classic nur über Dongle (Chip-FACT).
- D1 Mini / classic ESP32: **kein** USB-OTG-Host → nicht als Observe-USB-HCI-Node.
- Inject-Pipeline (`E_INJECT`) ≠ Controller-Evidence.
- HCI Event auf Interrupt-IN kann library-seitig noch offen sein — als `UNKNOWN`/`pending` führen, nicht als vollständig verkaufen.
- Endpoint-Events auf `.87` nicht mit HCI-Capture auf `.88` vermischen.

## Abgrenzung Capture-Pipelines

| Pfad | Sicht | Method / Sheet |
|------|--------|----------------|
| **USB-HCI Observe** (diese) | Host↔Controller am Dongle | dieses Dokument |
| **HCI snoop Phone/BlueZ** | Stack am Endgerät | `bt-passive-host-sniff` |
| **nRF OTA** | Air/Link | `bt-passive-host-sniff` |
| **ESP Endpoint** | App-Events | `bt-endpoint-event-stream` |
| **USB Stimulus Loop** | synthetisch USB | Topology B (Instrument) |

**Regel:** ESP Observe misst USB-HCI; nRF/Phone für Air/Stack-Referenz; Endpoint separat; Debian wertet aus.

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| esp32.bt-analyzer | [`projects/esp32-bt-analyzer`](../projects/esp32-bt-analyzer/) · `docs/LAB_METHODS.md` |
