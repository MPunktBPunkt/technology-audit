# USB BOT Instrumentierungsquellen · 2026-10-14

**Standard:** 0.7.1  
**Kampagne:** [`usb-bot-observation-2026-instrument-sources`](../../audits/usb-bot-observation-2026-instrument-sources/)  
**Vorläufer:** [`usb-bot-observation-2026-foreign`](../../audits/usb-bot-observation-2026-foreign/)

## Ergebnis

Desk-Audit der priorisierten Repos für echte CBW/CSW-Instrumentierung und
Host-Lab-Validate. Kein paralleles Technology Sheet; Wachstum in `usb-msc`.

| Quelle | Rolle | Snapshot |
|--------|-------|----------|
| `hathach/tinyusb` | Device-Hooks: CBW→CSW, Control, STALL/NEED_RESET, Sense | `4c195b7…` MSC-Pfad |
| `yeet-src/usbsnoop` | Host eBPF: SETUP + BOT CBW/CSW Decode | `30f9fad…`; Lizenz `UNKNOWN` |
| `adafruit/Adafruit_TinyUSB_Arduino` | App-Callbacks ohne CBW; ESP32-Beispiel | `1b73172…` |
| `tianocore/edk2` `UsbMassBot.h` | Struct-/Signatur-Referenz | `e4d139f…` pfadspezifisch |
| Wireshark `packet-usbms-bot.c` | Feldname-Abgleich | `f28ca85…` pfadspezifisch |

## Transfer

- Hook-Karte und Schema → [`usb-msc` Sheet](../../technologies/usb-msc/SHEET.md) und
  [`usb-bot-observation` Application](../../projects/usb-bot-observation/applications/usb-msc.md)
- Method: Host-eBPF-Validate in
  [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md)
- Nächster Schritt: Device-Ring implementieren + Lab gegen kontrollierten Host
  (usbsnoop nur nach Lizenzklärung)

## Bewusst offen

- NBT-CDB/Sense/Timing/Transparenz: `UNKNOWN`
- Physische Paketebene: out-of-scope
- usbsnoop: Research-Kontrast bis LICENSE klar
