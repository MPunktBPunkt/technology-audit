# Project Application: esp32-s3-usb-wifi-coex in hu-probe

```yaml
project_id: hu-probe
tech_slug: esp32-s3-usb-wifi-coex
status: active
sheet: ../../../technologies/esp32-s3-usb-wifi-coex/SHEET.md
audit: ../../../audits/esp32-s3-usb-wifi-coexistence-2026/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Die Sonde streamt MSC-Host-Events per **WiFi/TCP**, während sie gleichzeitig als
**USB-OTG MSC Device** am HU-Host hängt. Unter Host-Reads stirbt die WiFi-Assoc
im Lab (FW ≤0.2.15) — dieses Application-Dokument hält den **Stack-Pin** und den
Hypothesen-Rahmen; die Ursache bleibt `UNKNOWN`.

## Architektur / Datenfluss

```text
HU Host ──USB MSC Bulk──► TinyUSB usbd (Arduino)
                              │
                              ├─ EventBus / Ring
                              └─ TcpStreamer ──WiFi STA──► Collector
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `firmware/platformio.ini` | `espressif32@6.4.0`, `ARDUINO_USB_MODE=0`, FW 0.2.15 |
| `firmware/src/app/App.cpp` | WiFi setup (`PS_NONE`, TX 19.5), `superviseWifi` |
| `firmware/src/net/TcpStreamer.cpp` | Flush/yield unter MSC-Last |
| `docs/feld/2026-10-14-wifi-otg-0.2.15.md` | Lab-Symptom (Kontext, nicht Desk-IDF-FACT) |

## Konfiguration und Parameter

| Parameter | Wert (Pin) | Status |
|-----------|------------|--------|
| Platform | `espressif32@6.4.0` | `FACT` |
| Arduino-ESP32 | 2.0.11 (`3.20011.230801`) | `FACT` |
| IDF in Headers | 4.4.5 | `FACT` |
| USB Mode | OTG Device (`ARDUINO_USB_MODE=0`) | `FACT` |
| `CONFIG_ESP_PHY_ENABLE_USB` (prebuilt S3) | 1 | `FACT` (Package) |
| TinyUSB `usbd` prio | 24, no affinity | `FACT` (Arduino-HAL) |
| WiFi task | prio 23, Core 0 | `FACT` (IDF/Arduino defaults) |
| `loopTask` | prio 1, Core 1 | `FACT` |
| WiFi-Death Root-Cause | — | `UNKNOWN` |

Evidence: `EVID-USBWIFI-2026-10-14-007`–`012`, `016`.

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Lab: OTG + Host-Reads → Assoc weg in Sekunden (0.2.15 Mitigationen unzureichend) | Lokal-Feldnotiz; **nicht** `EVID-USBWIFI-*` | Projekt-`FACT` außerhalb IDF-Desk |
| Desk: IDF erklärt 0.2.15-Ursache | — | `REJECTED` |

## Offene Fragen

- Lab-Diskriminierung nach [`usb-wifi-coex-discrimination`](../../../methods/usb-wifi-coex-discrimination.md)
- Auto-HU gleicher Kill?
