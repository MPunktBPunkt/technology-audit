# Evidence — espusbhost-2026-foreign

Desk 2026-10-12 · **standard_version 0.6.6** · Profile `lab-tool`.

| Repo | Commit |
|------|--------|
| https://github.com/tanakamasayuki/EspUsbHost | `6386f2a` (v2.10.0) |

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBH-2026-10-12-001` | S2/S3/P4; library 2.10.0; Arduino min versions | `FACT` | README, library.properties |
| `EVID-USBH-2026-10-12-002` | Supported classes HID/CDC/MSC/MIDI/Audio/Hub/NCM/CCID/Vendor | `FACT` | README table |
| `EVID-USBH-2026-10-12-003` | S2/S3 host FS-only | `FACT` | README / tested-devices |
| `EVID-USBH-2026-10-12-004` | DevKitC-1 OTG ohne Device-Power | `FACT` | docs/tested-devices.md |
| `EVID-USBH-2026-10-12-005` | Control-Transfer-Max 256 B → große Configs fail | `FACT` | tested-devices UVC |
| `EVID-USBH-2026-10-12-006` | API 2.x incompatible with 1.x | `FACT` | README Version 2 status |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Getestete Geräte in unserer Lab | `UNKNOWN` | Upstream matrix only |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-12 | Desk; neuer Slug `esp-usb-host` |
