# Project: esp32.usb-analyzer

Dual-ESP32-S3 **USB Protocol Analyzer / MITM-Lab** mit Debian-Control-Plane.  
OTG Host↔Device-Loop + WiFi Mode-A Proxy-Slices + **Feld Host-Matrix**; Gate-Disziplin (kein transparentes MITM, kein Live-L0-Wire, kein AOA-aus-MSC-Identity).

Ursprungsrepo **read-only**. Aktuelle Kampagne: [`esp32-usb-analyzer-2026-field-host-matrix`](../../audits/esp32-usb-analyzer-2026-field-host-matrix/). Prior Soft-Lab: [`esp32-usb-analyzer-2026-0.0.50`](../../audits/esp32-usb-analyzer-2026-0.0.50/) · Pilot: [`esp32-usb-analyzer-2026-pilot`](../../audits/esp32-usb-analyzer-2026-pilot/).

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen und Systeme |
| [INVENTORY.md](INVENTORY.md) | Technologie-Inventar + Match |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | Folgeideen |
| [applications/](applications/) | Project Applications |
| Methods | [`usb-otg-loop-baseline`](../../methods/usb-otg-loop-baseline.md) · [`usb-msc-host-fingerprint`](../../methods/usb-msc-host-fingerprint.md) |

Ursprungsrepo: [MPunktBPunkt/esp32.usb-analyzer](https://github.com/MPunktBPunkt/esp32.usb-analyzer) — Soft-Lab @ `60244b3` (0.0.50) · Feldmatrix @ `688a40b` (0.0.52).

**Reuse:** wächst `usb-msc-host-behaviour` (neu), `usb-aoa` (MSC-Identity-Gate), `bmw-nbt-evo` (P-MOUNT Feld); Soft-Lab Path-A **REJECTED**; Full Audit erst nach C1.
