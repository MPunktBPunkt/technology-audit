# Evidence — usb-control-stall-recovery-2026

Desk 2026-10-14 · **standard_version 0.7.1** · Profile `lab-tool` · keine
Builds, keine USB-Hardware, kein NBT-Capture, kein Timing-Lab.

## Quellen-Snapshots

| Repository | SHA | Vertiefter Pfad | Lizenz |
|------------|-----|-----------------|--------|
| https://github.com/hathach/tinyusb | `4c195b7b94f813a37b77b184bcae7b2b6ef2835e` | `src/device/usbd.c`, `src/class/msc/msc_device.c` | MIT |
| https://github.com/espressif/esp-usb | `c40b86dc3a3e760b3dfdc28ec83010b9799a7e88` | nur `device/esp_tinyusb/` | Apache-2.0 (SPDX in Dateien; GitHub `NOASSERTION`) |
| https://github.com/tanakamasayuki/EspUsbDevice | `c10a44e2b220f473a9aba7076695301544745c5d` | `docs/usb-device-guide.md`, `docs/usb-device-advanced.md`, `docs/DESIGN_NOTES.ja.md` | MIT |
| esp-idf / arduino-esp32 Issues | Issue-URLs (Stand 2026-10-14) | USB↔WiFi Korrelation | n/a (Issue-Desk) |

TinyUSB-SHA identisch zur Instrumentierungs-Kampagne; hier zusätzlich
**`usbd.c`** (zuvor nur `src/class/msc/`). esp-usb-SHA weicht vom Host-MSC-Pin
`f3408e8` der Vor-Kampagne ab — bewusst **Device**-Pfad `esp_tinyusb/`.

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBCTRL-2026-10-14-001` | TinyUSB `process_std_device_request`: `SET_ADDRESS` → `dcd_set_address` + `_usbd_dev.addressed = 1` (Statusphase DCD-verantwortlich). `SET_CONFIGURATION`: bei Wechsel ggf. Close-all + `configuration_reset`; **cfg 0** → `tud_umount_cb()`; **cfg ≠ 0** → `process_set_config` dann `tud_mount_cb()`. | `FACT` | `usbd.c` ~1006–1054 |
| `EVID-USBCTRL-2026-10-14-002` | Weak Defaults: `tud_mount_cb` / `tud_umount_cb`; `tud_mounted()` spiegelt konfigurierten Zustand. Bus-Reset/Unplug-Pfade rufen `tud_umount_cb` (Stack), sofern Event ankommt. | `FACT` | `usbd.c` ~50–53, 489, 633, 739 |
| `EVID-USBCTRL-2026-10-14-003` | Endpoint-Standard: `CLEAR_FEATURE` / `SET_FEATURE` mit `EDPT_HALT` → `usbd_edpt_clear_stall` / `usbd_edpt_stall`, danach Class-`control_xfer_cb`; STD-Request wird ge-ACKed. | `FACT` | `usbd.c` ~1255–1278, 1742+ |
| `EVID-USBCTRL-2026-10-14-004` | MSC: ungültiger CBW → `MSC_STAGE_NEED_RESET`, Stall beider Bulk-EPs. In `mscd_control_xfer_cb`: bei NEED_RESET und CLEAR_FEATURE Halt **weiter stall** („Clear Stall cannot resolve“). BOT Reset `MSC_REQ_RESET` → `proc_bot_reset` (Stage/Sense clear). | `FACT` | `msc_device.c` ~392–433, 471–475; Reuse INST-003 |
| `EVID-USBCTRL-2026-10-14-005` | Außerhalb NEED_RESET: Clear-Halt auf EP IN kann `send_csw` nachholen (STATUS-Stage); auf EP OUT in CMD-Stage `prepare_cbw`. | `FACT` | `msc_device.c` ~403–420 |
| `EVID-USBCTRL-2026-10-14-006` | esp_tinyusb implementiert `tud_mount_cb` / `tud_umount_cb`: bei MSC `msc_storage_mount_to_usb()` bzw. `msc_storage_mount_to_app()`, plus `TINYUSB_EVENT_ATTACHED` / `DETACHED` an User-`event_cb`. Kommentar: Mount = Host `SetConfiguration(n≠0)`. `descriptors_control.c` bedient TinyUSB Descriptor-Callbacks (Device/Config/String/…). Targets u. a. esp32s2/s3/p4. | `FACT` | `tinyusb.c`, `descriptors_control.c`, `idf_component.yml` @ `c40b86d` |
| `EVID-USBCTRL-2026-10-14-007` | EspUsbDevice Guide: Enum-Stufen Attach → Reset → SET_ADDRESS → Descriptors → **SET_CONFIGURATION** (erst dann Klassen-EPs); `device.ready()` nach Stufe 7. Ohne VBUS-Sense: Unplug erreicht `onBusDetached()` nicht; State-Clear auch bei `onBusAttached` (`SET_CONFIGURATION`). | `FACT` (Doku) | `usb-device-guide.md` §1.4, §2.1 |
| `EVID-USBCTRL-2026-10-14-008` | EspUsbDevice Advanced: `SET_CONFIGURATION n` → `tud_mount_cb` → `onBusAttached`; cfg 0 / Detach (nur mit VBUS-Sense) → umount. **Bare bus reset und Replug ohne VBUS ohne umount** — „replug goes straight to re-enumeration undetected“. | `FACT` (Doku) | `usb-device-advanced.md` §4.2, §7.3; DESIGN_NOTES.ja |
| `EVID-USBCTRL-2026-10-14-009` | Fremd-Issues melden USB↔WiFi-Interferenz bzw. USB-Ausfall bei WiFi-Start (u. a. arduino-esp32 [#6264](https://github.com/espressif/arduino-esp32/issues/6264) C3 CDC; esp-idf [#15079](https://github.com/espressif/esp-idf/issues/15079) S3 Host+WiFi / PHY-USB-Option; [#7404](https://github.com/espressif/esp-idf/issues/7404) S2; [#15029](https://github.com/espressif/esp-idf/issues/15029) C6; arduino [#9138](https://github.com/espressif/arduino-esp32/issues/9138) MSC+CDC Stabilität). **Keine** Root-Cause-Übertragung auf die eigene Sonde; Chip-/Modus-Scope je Issue verschieden. | `HYPOTHESIS` | Issue-Desk 2026-10-14 |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „SET_ADDRESS = Gerät mounted / Klassen aktiv“ | `REJECTED` | Mount erst bei SET_CONFIGURATION n (`001`, `007`) |
| „Clear-Halt beendet NEED_RESET“ | `REJECTED` | Stack stallt weiter (`004`) |
| „Unplug feuert immer tud_umount_cb auf ESP-Boards“ | `REJECTED` | ohne VBUS-Sense oft nein (`007`, `008`) |
| „Issue X = WiFi-Death-Root-Cause der Sonde“ | `REJECTED` | nur Korrelation/`HYPOTHESIS` (`009`) |
| „Desk belegt Timing / S1–S3 / NBT“ | `REJECTED` | Scope; `UNKNOWN` |
| „Neues Sheet nötig“ | `REJECTED` | Contract bleibt `usb-msc` A-Wachstum |

## Hook-Karte (Implementierungs-Hypothese, nicht Lab-FACT)

| Event-Kandidat | Stelle | Pflichtfelder |
|----------------|--------|---------------|
| `usb_set_address` | `usbd.c` SET_ADDRESS | wValue (addr), Epoch |
| `usb_set_config` | `usbd.c` SET_CONFIGURATION | cfg_num (0 vs n) |
| `usb_mount` / `usb_umount` | `tud_mount_cb` / `tud_umount_cb` | Port-Events (ESP: ATTACHED/DETACHED); Storage-Ownership |
| `ep_stall` / `ep_clear_halt` | `usbd_edpt_stall` / Clear-Feature Halt | ep_addr |
| `msc_need_reset` | `MSC_STAGE_NEED_RESET` | beide Bulk-EPs stalled; **kein** Tag weiterführen |
| `msc_bot_reset` | `MSC_REQ_RESET` / `proc_bot_reset` | Stage/Sense clear = neue Epoch |
| `bot_cbw` / `bot_csw` | unverändert aus INST-Kampagne | siehe Vorläufer |

Ergänzt die BOT-Hook-Karte aus
[`usb-bot-observation-2026-instrument-sources`](../usb-bot-observation-2026-instrument-sources/evidence.md).

## Engineering Review Checks aus Evidence

| Evidence-ID | Review Check |
|-------------|--------------|
| `001`–`003` | Logger: Address ≠ Mount; cfg 0 und cfg n getrennt |
| `004`–`005` | NEED_RESET bis BOT Reset; Clear-Halt loggen ohne „geheilt“ |
| `006` | ESP: Mount/Umount ↔ Storage + User-Event |
| `007`–`008` | Probe-State bei Mount clearen; Umount nicht voraussetzen |
| `009` | WiFi+USB = Lab-Gate/Hypothese, kein Desk-FACT |

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| Control-Events + BOT Tag-Match am Lab-Host | `UNKNOWN` | Lab |
| Timing / Beobachterwirkung / S1–S3 | `UNKNOWN` | eigene Messung |
| NBT Enum-/Reset-Sequenz | `UNKNOWN` | Fahrzeug-Capture |
| WiFi stirbt unter USB-Last (eigene Sonde) | `UNKNOWN` / `HYPOTHESIS` | Lab unter Last; Issues nur Kontrast |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-14 | Instrumentierungs-Kampagne: CBW/CSW/Class-Control |
| 2026-10-14 | Control/Stall/Enum Follow-on: `usbd.c`, esp_tinyusb, EspUsbDevice, WiFi-Issues; Kampagne closed |
