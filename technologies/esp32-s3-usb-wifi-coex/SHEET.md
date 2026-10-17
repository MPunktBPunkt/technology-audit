# Technology Sheet: ESP32-S3 USB ↔ WiFi Coexistence

```yaml
slug: esp32-s3-usb-wifi-coex
title: ESP32-S3 USB ↔ WiFi Coexistence (OTG Device + STA)
primary: D
tags: [esp32s3, usb-device, wifi, freertos, tinyusb, phy]
type: pattern
status: active
seen_in: [hu-probe]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/esp32-s3-usb-wifi-coexistence-2026
```

Ebene **A**. Projektsymptome / FW-Pins → Application. Desk:
[`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/).
MSC-Protokoll → [`usb-msc`](../usb-msc/SHEET.md).
Silicon-Errata (Cache/Sleep/OTG-Download) → [`esp32-s3-silicon`](../esp32-s3-silicon/SHEET.md).

## Kurzfassung

Auf ESP32-S3 teilen USB-OTG und verwandte Pfade kritische PHY-/Clock-Ressourcen mit
dem WiFi/PHY-Stack. Gleichzeitiger Betrieb ist vorgesehen und historically buggy
(Start-Interferenz, BBPLL/USB-PHY-Workaround), aber **kein** offizieller Satz
„Bulk hungert WiFi“. Task-Defaults (besonders Arduino TinyUSB) erzeugen eine
messbare Prioritäten-Landschaft über dem WiFi-Driver.

## Abgrenzung

- **Ist:** Navigationskarte PHY/BBPLL, Shared-PHY, Default-Task/Core/Prio, Issue-Korrelation.
- **Ist nicht:** Root-Cause eines konkreten Gadgets; WiFi↔BT Software-Coex (`esp-faq`);
  USB-Host-only Claims als Device-Wahrheit; Capture-/Flush-Architektur.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | App: MSC Bulk + WiFi STA/TCP | Lastprofile projektspezifisch |
| seitlich | TinyUSB Device Task / ISR | Arduino-HAL ≠ esp-usb Task-API |
| unten | esp_phy / BBPLL / USB PHY | `ESP_PHY_ENABLE_USB`, `phy_bbpll_en_usb` |
| parallel | USB Serial/JTAG | teilt internen PHY mit OTG (eFuse `USB_PHY_SEL`) |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| `esp_wifi_start` kann USB Device auf S3 brechen (historisch) | `FACT` | IDF #7957/#8241; PHY-Fix |
| `ESP_PHY_ENABLE_USB` / `phy_bbpll_en_usb` = S3/C3-Workaround | `FACT` | #12185; Kconfig |
| WiFi-Task prio 23 / Core 0 Default | `FACT` | IDF Docs + Kconfig |
| Arduino 2.0.11 `usbd` prio 24, no affinity | `FACT` | `esp32-hal-tinyusb.c` |
| USB-Bulk verursacht WiFi-Tod | `HYPOTHESIS` | Lab-Diskriminierung |
| esp-faq Coex gilt für USB | `REJECTED` | nur WiFi↔BT |
| IDF-Issue = Ursache Projekt X | `REJECTED` | Epistemik |

## Default-Karte (Orientierung)

| Rolle | Prio (typ.) | Core | Stack-Hinweis |
|-------|------------:|------|---------------|
| TinyUSB Device (`usbd`) | 24 (Arduino) / konfigurierbar (esp-usb) | none / `xCoreID` | Pfad prüfen |
| WiFi driver | 23 | 0 | Kconfig |
| lwIP tcpip | 18 | oft 0 | Kconfig |
| Arduino loop | 1 | 1 | Arduino |

## Transfer

- Bei jedem S3-Projekt mit **OTG Device + WiFi**: PHY-Option, Task-Prios und Core-Pin
  vor Optimismus aus „usb_dongle existiert“ prüfen.
- Method: [`usb-wifi-coex-discrimination`](../../methods/usb-wifi-coex-discrimination.md).

### Projektstart-Checkliste

- [ ] Sheet gelesen (Abgrenzung + Fallstricke)
- [ ] Arduino-HAL vs. esp-usb Task-Pfad bestimmt
- [ ] `ESP_PHY_ENABLE_USB` im tatsächlichen sdkconfig verifiziert
- [ ] Application mit Stack-Pin; keine Ursachenbehauptung ohne Lab
- [ ] `seen_in` ergänzt

## Referenzen

- esp-idf Issues #7957, #8241, #15079, #12185
- esp-idf `esp_phy` Kconfig / `phy_init.c`; USB OTG Console Doc
- espressif/esp-usb `device/esp_tinyusb/tinyusb_task.c`
- IDF `api-guides/performance/speed.rst` (Built-In Task Priorities)
- Audit Evidence: `EVID-USBWIFI-2026-10-14-*`

## Offene Fragen

- SOF/ISR-Lastanteil unter Full-Speed Bulk?
- Ob Host-Reads vs. bloßes Enum denselben WiFi-Effekt auslösen (Lab)?
