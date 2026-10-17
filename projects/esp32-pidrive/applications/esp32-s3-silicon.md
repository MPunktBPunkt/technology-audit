# Project Application: esp32-s3-silicon in esp32.pidrive

```yaml
tech_slug: esp32-s3-silicon
project_id: esp32-pidrive
sheet: ../../../technologies/esp32-s3-silicon/SHEET.md
audit: ../../../audits/esp32-s3-hw-limits-2026/
updated: 2026-10-18
```

## Rolle im Projekt

ESP32-S3 ist das USB-MSC-Gadget (`TinyUSB` Device) plus SoftAP/STA. Silicon-
Errata und Sleep/Analog-Gates begrenzen, was in langen MessCapture-/Storm-
Sessions (M30) ohne Lab als „sicher“ gelten darf — getrennt von Host-NBT-
Semantik und von USB↔WiFi-Coex.

## Relevante Pfade / Pins

| Thema | Projektbezug | Hinweis |
|-------|--------------|---------|
| USB-OTG MSC | `src/msc/` | USBOTG-4289 betrifft **Download**, nicht Bulk-Semantik |
| MessCapture-Ring | `MessCapture` DRAM | CACHE-126: aktuelle IDF/Arduino-Basis prüfen |
| Sleep | typisch aus im Feld-OTG | ANALOG-160 / RTC-126 = hartes Gate falls Sleep experimentiert wird |
| WiFi + USB | SoftAP/Status | Coex → Application `…` nur indirekt; Sheet `esp32-s3-usb-wifi-coex` |

## Epistemik (B/C)

| Claim | Ebene | Status |
|-------|-------|--------|
| Offizielle S3-Errata-Tabelle gilt für eingesetzte Module | A→B | `FACT` wenn Rev bekannt; sonst Rev/`UNKNOWN` |
| Light-Sleep unter aktivem MSC ist für Storm-P0 aus | B Politik | `INFERENCE` aus Errata+Issues; Lab offen |
| Storm-Drops = CACHE-126 | C | `REJECTED` ohne Capture-Korrelation |

## Offene Fragen

- Date Code / Chip-Rev der Feldmodule?
- Nutzt die aktuelle Build-Linie Octal-PSRAM? (Issue #18806)
- Light-Sleep jemals in Lab-Envs aktiv?

## Links

- Sheet: [`esp32-s3-silicon`](../../../technologies/esp32-s3-silicon/SHEET.md)
- Audit: [`esp32-s3-hw-limits-2026`](../../../audits/esp32-s3-hw-limits-2026/)
- Coex: [`esp32-s3-usb-wifi-coex`](../../../technologies/esp32-s3-usb-wifi-coex/SHEET.md)
- Storm-Tooling: [`pidrive-2026-storm-capture-tooling`](../../../audits/pidrive-2026-storm-capture-tooling/)
