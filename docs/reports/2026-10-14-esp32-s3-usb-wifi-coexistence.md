# ESP32-S3 USB ↔ WiFi Coexistence Desk · 2026-10-14

**Standard:** 0.7.1  
**Kampagne:** [`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/)  
**Projekt:** [`hu-probe`](../../projects/hu-probe/)

## Ergebnis

Enges Desk-Audit: **Coex-unter-Last-Karte** (PHY/BBPLL, Shared-PHY, Task/Core/Prio,
Hypothesen + Messplan). **Keine** Root-Cause für hu-probe 0.2.15.

| Quelle | Rolle | Snapshot |
|--------|-------|----------|
| esp-idf Issues #7957/#8241/#15079/#12185 | Start-Interferenz, Host-PHY-Option, BBPLL | Issue-IDs + Fix `65f3bf4…` |
| esp-idf PHY/WiFi Kconfig + speed.rst | Defaults WiFi 23/Core0, tcpip 18 | `ab95e707…` / v4.4.5 |
| esp-usb `tinyusb_task.c` | konfigurierbare Task-API | `c40b86d…` |
| Arduino-ESP32 2.0.11 (PIO-Pin) | `usbd` prio **24**, no affinity | Tag `ae9dae4…` / package `3.20011.230801` |
| esp-faq coexistence | **Abgrenzung** WiFi↔BT ≠ USB | `d8a806e…` |
| esp-iot-solution usb_dongle | Gleichzeitigkeit möglich, Last unklar | `4962410…` |

## Transfer

- Sheet [`esp32-s3-usb-wifi-coex`](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md)
- Method [`usb-wifi-coex-discrimination`](../../methods/usb-wifi-coex-discrimination.md)
- Application [`hu-probe/…/esp32-s3-usb-wifi-coex.md`](../../projects/hu-probe/applications/esp32-s3-usb-wifi-coex.md)

## Kernaussagen (Desk)

1. S3 USB↔WiFi ist offiziell heikel (PHY/BBPLL, `esp_wifi_start`-Historie).
2. Unter Arduino 2.0.11 liegt TinyUSB-`usbd` **über** dem WiFi-Driver (24 > 23).
3. BT-Coex-Doku gilt nicht für USB.
4. „Bulk hungert WiFi“ und „Issue = Sonde“ bleiben verboten als FACT.

## Bewusst offen

- Lab Power vs. Starve vs. RF
- Auto-HU Reproduktion
- SOF/ISR-Anteile
