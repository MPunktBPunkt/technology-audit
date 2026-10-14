# USB Control / Stall / Enum Recovery · 2026-10-14

**Standard:** 0.7.1  
**Kampagne:** [`usb-control-stall-recovery-2026`](../../audits/usb-control-stall-recovery-2026/)  
**Vorläufer:** [`usb-bot-observation-2026-instrument-sources`](../../audits/usb-bot-observation-2026-instrument-sources/)

## Ergebnis

Schmales Follow-on für die fehlenden GATE-01-Control-Pfade. Hook-Karte +
Evidence, kein Code-Import. Timing und S1–S3 bleiben eigene Arbeit.

| Quelle | Rolle | Snapshot |
|--------|-------|----------|
| `hathach/tinyusb` `usbd.c` + `msc_device.c` | SET_ADDRESS, SET_CONFIGURATION, STALL, CLEAR_HALT, NEED_RESET | `4c195b7…` |
| `espressif/esp-usb` `esp_tinyusb/` | Mount/Umount ↔ Storage + Events; Descriptor-Control | `c40b86d…` Device-Pfad |
| `tanakamasayuki/EspUsbDevice` Docs | Enum-Stufen; kein VBUS-Sense → Replug ohne umount | `c10a44e…` |
| esp-idf / arduino-esp32 Issues | USB↔WiFi Korrelation | Issue-URLs; nur `HYPOTHESIS` |

## Transfer

- Control-/Enum-Epochs → [`usb-msc` Sheet](../../technologies/usb-msc/SHEET.md) und
  [`usb-bot-observation` Application](../../projects/usb-bot-observation/applications/usb-msc.md)
- Method: Enum-/Clear-Halt-/NEED_RESET-Trennung in
  [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md)

## Kernaussagen (Desk-FACT)

1. Mount = `SET_CONFIGURATION n` → `tud_mount_cb`; Address allein reicht nicht.
2. Clear-Halt heilt `MSC_STAGE_NEED_RESET` nicht — BOT Reset nötig.
3. Ohne VBUS-Sense: Replug oft ohne `tud_umount_cb`; Mount-Hook clearen.
4. WiFi↔USB-Issues stützen Hypothesen, keine Root-Cause der Sonde.

## Bewusst offen

- Timing-Lücke, S1–S3, Transparenz, NBT: `UNKNOWN`
- usbsnoop / Hardware-Sniffer: nicht priorisiert
