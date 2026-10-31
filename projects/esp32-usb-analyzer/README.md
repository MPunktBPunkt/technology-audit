# Project: esp32.usb-analyzer

Dual-ESP32-S3 **USB Protocol Analyzer / MITM-Lab** mit Debian-Control-Plane.  
OTG Host↔Device-Loop + WiFi Mode-A Proxy-Slices; Gate-Disziplin (kein transparentes MITM, kein L0-Wire).

Ursprungsrepo **read-only**. Kampagne: [`esp32-usb-analyzer-2026-pilot`](../../audits/esp32-usb-analyzer-2026-pilot/).

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen und Systeme |
| [INVENTORY.md](INVENTORY.md) | Technologie-Inventar + Match |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | Folgeideen |
| [applications/](applications/) | Project Applications |
| Method | [`usb-otg-loop-baseline`](../../methods/usb-otg-loop-baseline.md) |

Ursprungsrepo: [MPunktBPunkt/esp32.usb-analyzer](https://github.com/MPunktBPunkt/esp32.usb-analyzer) @ `b2c9987` (FW **0.0.35**).

**Reuse:** wächst `usb-msc`, `esp-usb-host`, `usb-aoa`, `bmw-bcl` (Lab-Framing), Coex/Silicon/Hub; neues Pattern-Sheet `usb-dual-esp-observe-proxy`.
