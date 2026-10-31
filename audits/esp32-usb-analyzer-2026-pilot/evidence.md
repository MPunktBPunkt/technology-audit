# Evidence — esp32-usb-analyzer-2026-pilot

Lab 2026-10-31 · Upstream FW bis **0.0.35** @ `b2c9987`.  
Basis: `https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/`

Rohdaten bleiben im Quellenrepo — hier nur Claims + Links.

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBA-2026-10-31-001` | OTG MSC READ peak **~934 kB/s** (chunk=8, FS); pattern fail **0**; sustained 3× media OK | `MEASURED` | [LAB_BASELINE_MEASURED.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/docs/evidence/LAB_BASELINE_MEASURED.md) · [JSON T120705Z](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/docs/evidence/LAB_BASELINE_20261031T120705Z.json) |
| `EVID-USBA-2026-10-31-002` | Single-sector MSC RTT p50 **~0.73 ms**; 8-sector p50 **~4.1 ms** | `MEASURED` | same |
| `EVID-USBA-2026-10-31-003` | WiFi TCP ESP↔ESP peak **~139 kB/s** (ack-each); small frames RTT ~250 ms; 0 frame errors | `MEASURED` | same |
| `EVID-USBA-2026-10-31-004` | Früher `pattern_ok=false` bei chunk>1 = Gadget multi-LBA Fill-Bug (Device 0.0.12), **kein** USB-Bitfehler; Fix 0.0.14; T120435Z verworfen | `REJECTED` (als USB-Verlust) / `FACT` (Bug) | LAB_BASELINE_MEASURED §Earlier false positive · [T120435Z](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/docs/evidence/LAB_BASELINE_20261031T120435Z.json) |
| `EVID-USBA-2026-10-31-005` | OTG MSC WRITE ~**246–463 kB/s** (chunk 1…8) mit readback `pattern_ok` (FW 0.0.18) | `MEASURED` | LAB_BASELINE_MEASURED §C |
| `EVID-USBA-2026-10-31-006` | AOA Lab A: GET_PROTOCOL=1, SEND_STRING×6, START, re-enum → **`18d1:2d00`**, Dauer **~0,55 s** | `MEASURED` | [LAB_AOA_HANDSHAKE_MEASURED.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/docs/evidence/LAB_AOA_HANDSHAKE_MEASURED.md) |
| `EVID-USBA-2026-10-31-007` | AOA Lab B (responder OFF): Host Handshake fail / STALL — expected | `MEASURED` | same |
| `EVID-USBA-2026-10-31-008` | AOA vendor-bulk echo Host↔Device byte-exact (TinyUSB FIFO; EP 0x02/0x82) | `MEASURED` | same · FW 0.0.32 |
| `EVID-USBA-2026-10-31-009` | Lab BCL 8-byte BE + init über AOA bulk: HANDSHAKE/DATA/empty echo + host units — **nicht** HU wire | `MEASURED` (lab) | LAB_AOA_HANDSHAKE_MEASURED Epistemic · CHANGELOG 0.0.33/34 |
| `EVID-USBA-2026-10-31-010` | Post-enum: address≠0, configuration≠0, GET_CONFIGURATION match; soft-reenum OK — mid-enum SETUP **UNKNOWN** | `MEASURED` / `UNKNOWN` | [LAB_ENUM_HID_MEASURED.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/docs/evidence/LAB_ENUM_HID_MEASURED.md) |
| `EVID-USBA-2026-10-31-011` | HID interrupt: Device inject → Host EspUsbHost callback + capture `hid_input` — nicht L0 | `MEASURED` | same |
| `EVID-USBA-2026-10-31-012` | Class-hook BOT CBW/CSW (`mscd_xfer_cb` / `send_csw`) vs App-inferred decode — source tags | `MEASURED` / `FACT` (B) | [GATE4_STATUS](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/docs/GATE4_STATUS.md) · README capture table · Method usb-bot-command-observation |
| `EVID-USBA-2026-10-31-013` | MSC bulk proxy Device↔Host DUT byte-exact CRC/hex — **nicht** transparent MITM | `MEASURED` | GATE4_STATUS · `tools/lab_usb_proxy_verify.py` |
| `EVID-USBA-2026-10-31-014` | Cross-node sync = median `offset_us` estimate — hard µs lock **REJECTED** | `MEASURED` / `REJECTED` | GATE7/8 status · `tools/lab_sync_offset.py` |
| `EVID-USBA-2026-10-31-015` | Windowed TCP bulk window=8 ≈ **0.26 MB/s**; window=16 can regress — noch ≪ USB cable | `MEASURED` | LAB_BASELINE takeaways · GATE4 window notes |
| `EVID-USBA-2026-10-31-016` | Lab boards: `.88` Host / `.89` Device YD-ESP32-S3 N8R2; controller `.187:9750` | `FACT` (lab inventory) | [LAB_INVENTORY.md](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/docs/LAB_INVENTORY.md) |
| `EVID-USBA-2026-10-31-017` | Explicit non-claims: D+/D− wire, transparent MITM, HS USB, HU BCL-on-Bulk | `REJECTED` / not claimed | [README](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/b2c9987/README.md) · GATES.md |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Transparent MITM + Observer-effect Baseline | `UNKNOWN` | Exit 7 / Gate 4 |
| Mid-enum SET_ADDRESS/SET_CONFIGURATION on wire | `UNKNOWN` | Enum-Outcome nur Post-Enum |
| Hard synchronized µs clocks | `REJECTED` until proven | Offset only |
| HU AOA / BCL Feld | `UNKNOWN` | deferred; Desk `usb-aoa` / hu-probe |
| D+/D− sampling feasibility | `UNKNOWN` | Gate 10 |
| Mode-A ausreichend für sustained HU Bulk | `UNKNOWN` / unlikely ohne SF | Coex + SF-* |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-30 | Gate 0 Architecture / Evidence-Digest im Upstream |
| 2026-10-31 | Lab Baseline MSC/TCP; AOA; BCL lab; Enum/HID; FW → 0.0.35 |
| 2026-10-31 | Import technology-audit Pilot @ `b2c9987` |
