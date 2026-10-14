# Evidence — usb-bot-observation-2026-instrument-sources

Desk 2026-10-14 · **standard_version 0.7.1** · Profile `lab-tool` · keine
Builds, keine USB-Hardware, kein NBT-Capture.

## Quellen-Snapshots

| Repository | SHA | Vertiefter Pfad | Lizenz |
|------------|-----|-----------------|--------|
| https://github.com/hathach/tinyusb | `4c195b7b94f813a37b77b184bcae7b2b6ef2835e` | `src/class/msc/` (`msc.h`, `msc_device.c`, `msc_device.h`) | MIT |
| https://github.com/yeet-src/usbsnoop | `30f9fad04871252934ca0edd74b0089cb96688da` | `main.js`, `usbsnoop.bpf.c`, README | `UNKNOWN` (GitHub `null`; keine LICENSE-Datei) |
| https://github.com/adafruit/Adafruit_TinyUSB_Arduino | `1b7317255f7127b816fad7913ffaeb7fd416ace3` | `src/arduino/msc/`, `examples/MassStorage/` | MIT |
| https://github.com/tianocore/edk2 | `e4d139f4880625aed2e1e81d800afebc2b2c9630` | nur `MdeModulePkg/Bus/Usb/UsbMassStorageDxe/UsbMassBot.h` | BSD-2-Clause-Patent (SPDX im File-Header) |
| https://github.com/wireshark/wireshark | `f28ca85a4b40aaa3d9eea4bf2a878ce9b68d4469` | nur `epan/dissectors/packet-usbms-bot.c` | GPL-2.0 (GitHub) |
| https://github.com/torvalds/linux | `2c0f5ca48674a5b5f9fa4a9c3325aa48053af0bc` | nur `drivers/usb/gadget/function/f_mass_storage.c` (Reuse Vor-Kampagne) | GPL-2.0-or-later (SPDX im File) |

Pfadspezifische Snapshots sind keine Aussage über den vollständigen Upstream.
TinyUSB-MSC wurde gegenüber Vor-Pin `3024dd2` am neuen HEAD erneut gelesen;
Stage-/Busy-Claims der Vor-Kampagne bleiben gültig und werden hier um Hook-
und Feld-Detail ergänzt.

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBBOT-INST-2026-10-14-001` | TinyUSB definiert `msc_cbw_t` (31 B: `signature`, `tag`, `total_bytes`, `dir`, `lun`, `cmd_len`, `command[16]`) und `msc_csw_t` (13 B: `signature`, `tag`, `data_residue`, `status`) mit Signaturen `0x43425355` / `0x53425355`. | `FACT` | TinyUSB `msc.h` |
| `EVID-USBBOT-INST-2026-10-14-002` | Nach gültigem CBW in `mscd_xfer_cb` (`MSC_STAGE_CMD`) kopiert der Driver den CBW, setzt `csw.signature/tag/status`, `total_len`/`xferred_len`, und wechselt in `MSC_STAGE_DATA`. `send_csw` setzt `data_residue = total_bytes - xferred_len` und sendet 13 B auf EP IN. | `FACT` | `msc_device.c`: `mscd_xfer_cb`, `send_csw` |
| `EVID-USBBOT-INST-2026-10-14-003` | Ungültiger CBW (Länge ≠ 31 oder Signatur falsch) → `MSC_STAGE_NEED_RESET`, Stall beider Bulk-EPs. `mscd_control_xfer_cb` handhabt Clear Endpoint Feature (Stall-Recovery), Class-Request Reset (`MSC_REQ_RESET` = 255) via `proc_bot_reset`, und Get Max LUN (`MSC_REQ_GET_MAX_LUN` = 254). | `FACT` | `msc_device.c`: CMD-Validierung, `mscd_control_xfer_cb`, `proc_bot_reset` |
| `EVID-USBBOT-INST-2026-10-14-004` | `fail_scsi_op` setzt CSW-Status, Residue, optional Default-Sense (`ILLEGAL_REQUEST` 0x20/0x00), und ställt die Daten-EP bei Rest-Residue. `tud_msc_set_sense(lun, key, asc, ascq)` ist die öffentliche Sense-API. `TU_LOG_DRV` loggt SCSI-Opcode-Namen und Status. | `FACT` | `msc_device.c` / `msc_device.h` |
| `EVID-USBBOT-INST-2026-10-14-005` | usbsnoop hängt an `usb_submit_urb` und `usb_hcd_giveback_urb` (eBPF), paart Submit→Complete per URB-Pointer, und dekodiert Control-SETUP (u. a. `SET_ADDRESS`, `SET_CONFIGURATION`) sowie Bulk BOT: 31-B CBW (`READ(10)`/`WRITE(10)` mit LBA/Blocks) und 13-B CSW (`PASS`/`FAIL`/`PHASE_ERR` + Residue). | `FACT` | usbsnoop README, `usbsnoop.bpf.c`, `main.js` `decodeSetup` / `decodeScsi` |
| `EVID-USBBOT-INST-2026-10-14-006` | usbsnoop Limits: max. 16384 B Payload/Transfer, SG braucht x86-64-KASLR-Symbole, Transfers vor Attach ohne Latenz, Ring ~512 Events — Desk-Doku, kein Lab-Lauf. | `FACT` (Doku) | usbsnoop README „Limits“ |
| `EVID-USBBOT-INST-2026-10-14-007` | Am Pin `30f9fad` hat usbsnoop **keine** erkannte SPDX-/LICENSE-Datei; GitHub `license: null`. Nutzung hier nur als Research-Kontrast / Lab-Tool-Idee, **nicht** als kopierbare Implementierungsgrundlage. | `FACT` | Repo-Root + GitHub API 2026-10-14 |
| `EVID-USBBOT-INST-2026-10-14-008` | edk2 `UsbMassBot.h` spiegelt dieselben BOT-Konstanten (Reset `0xFF`, GetLUN `0xFE`, Signaturen, Status 0/1/2) und Struct-Felder (`USB_BOT_CBW` / `USB_BOT_CSW`) — Schema-Referenz, Host-seitig. | `FACT` | `UsbMassBot.h` @ `e4d139f` |
| `EVID-USBBOT-INST-2026-10-14-009` | Wireshark `packet-usbms-bot.c` dissectet `dCBWSignature`, Tag, TransferLength, Flags, LUN, CDB-Länge, CDB→SCSI und CSW Signatur/Tag/Residue/Status — geeigneter Feldname-Abgleich für Logger-Schema. | `FACT` | `packet-usbms-bot.c` @ `f28ca85` |
| `EVID-USBBOT-INST-2026-10-14-010` | Adafruit `Adafruit_USBD_MSC` mappt App-`rd_cb(lba, buffer, bufsize)` auf `tud_msc_read10_cb` und **verwirft `offset`**. Beispiele (`msc_ramdisk`, `msc_esp32_file_browser`) setzen Capacity/Callbacks und ggf. detach/attach zur Re-Enumeration — **kein** CBW/CSW an der App-API. | `FACT` | `Adafruit_USBD_MSC.cpp`, `examples/MassStorage/` |
| `EVID-USBBOT-INST-2026-10-14-011` | Linux `f_mass_storage` (Reuse Vor-Kampagne) bleibt die Gadget-Referenz für CBW-Validierung und Reset-Recovery; physische Paketebene (DATA0/1, ACK/NAK) ist in keiner dieser Quellen belegt. | `FACT` / `UNKNOWN` | Vor-`EVID-USBBOT-2026-10-13-004`; Scope |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „`onRead`/`msc_read_callback` = vollständiges `bot_cbw`-Event“ | `REJECTED` | App sieht nur LBA/Buffer/Size (`010`); CBW im Driver (`002`) |
| „usbsnoop-Capture = NBT-Verhalten“ | `REJECTED` | kontrollierter Linux-Host; NBT `UNKNOWN` |
| „usbsnoop-Code darf ungeprüft in Produkt übernommen werden“ | `REJECTED` | Lizenz `UNKNOWN` (`007`) |
| „Schema braucht neues Technology Sheet“ | `REJECTED` | Contract bleibt `usb-msc`; Structs sind A-Wachstum |
| „DATA0/1/ACK aus TinyUSB/usbsnoop ableiten“ | `REJECTED` | nur URB-/Class-Ebene (`011`) |

## Hook-Karte (Implementierungs-Hypothese, nicht Lab-FACT)

| Event-Kandidat | TinyUSB-Stelle | Pflichtfelder |
|----------------|----------------|---------------|
| `bot_cbw` | `mscd_xfer_cb` / `MSC_STAGE_CMD` nach `memcpy` | tag, lun, total_bytes, dir, cmd_len, command[] |
| `bot_data_chunk` | `proc_read10_cmd` / IO-Pfad | xferred_len, chunk, **nicht** als CDB-Länge ausgeben |
| `bot_csw` | `send_csw` / Status-Stage | tag, data_residue, status |
| `bot_sense` | `tud_msc_set_sense` / REQUEST SENSE | key, asc, ascq + auslösender tag |
| `usb_control` / epoch | `mscd_control_xfer_cb`, `MSC_STAGE_NEED_RESET` | bRequest, Clear-Halt, BOT Reset |

Host-Gegenprobe (Lab): usbsnoop `decodeScsi`/`decodeSetup` am Kontrollhost.

## Engineering Review Checks aus Evidence

| Evidence-ID | Review Check |
|-------------|--------------|
| `001`–`003` | Logger nach CBW-Validierung, nicht in App-Callback allein |
| `002` | CSW-Residue aus `total_bytes - xferred_len` prüfen |
| `003` | NEED_RESET und Class-Reset als Epoch; keine Tag-Korrelation darüber |
| `004` | Sense an fehlgeschlagenen Command binden |
| `005`–`007` | Host-Validate nur mit Lizenz-/Scope-Hinweis; Truncation/Ring beachten |
| `010` | Adafruit-Offset-Drop: Chunk-Offset ggf. nur im Stack sichtbar |

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| Device-Logger + usbsnoop Tag-Match am Lab-Host | `UNKNOWN` | Lab-Lauf, neue IDs |
| Logger-Transparenz (Latenz/Drops) | `UNKNOWN` | Baseline |
| NBT CBW/CDB/Sense/Reset/Timing | `UNKNOWN` | Fahrzeug-Capture nach Gates |
| usbsnoop-Lizenz für produktive Nutzung | `UNKNOWN` | Upstream LICENSE / Author |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | Vor-Kampagne closed: Pfadvergleich Device/Inline/Host |
| 2026-10-14 | Instrumentierungsquellen gepinnt; Hook-/Schema-Evidence; Kampagne closed |
