# Project: esp32.bt-analyzer

ESP32-S3 **USB/HCI Capture**-Lab (Bluetooth Controller über USB-Dongle) — nicht RF-Sniffer, nicht MITM.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen und Systeme |
| [INVENTORY.md](INVENTORY.md) | Technologie-Inventar + Match |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | Folgeideen |
| [applications/](applications/) | Project Applications |
| Method | [`bt-passive-host-sniff`](../../methods/bt-passive-host-sniff.md) |

Ursprungsrepo: [MPunktBPunkt/esp32.bt-analyzer](https://github.com/MPunktBPunkt/esp32.bt-analyzer) (bootstrap 0.1.0).

**Reuse:** `esp-usb-host`, Method HCI-Snoop, Capture-Family Trennung; Contrast: Endpoint / nRF / Classic-on-S3 REJECTED.
