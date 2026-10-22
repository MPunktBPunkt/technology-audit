# Project: hu-probe

ESP32-S3 USB-MSC Head-Unit-Messsonde (Lokal: `/home/martin/projects/hu-probe`).
In `technology-audit`: Desk-/Feld-Kampagnen und wiederverwendbare Sheets — kein
Firmware-Mirror.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen, Quellen-Pins |
| [INVENTORY.md](INVENTORY.md) | Tech-Slugs |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | nächste Schritte |
| [applications/esp32-s3-usb-wifi-coex.md](applications/esp32-s3-usb-wifi-coex.md) | Stack-Pin + Hypothesen-Rahmen |
| [applications/usb-msc.md](applications/usb-msc.md) | Device/Instrument + Offline/Trip |
| [applications/bmw-nbt-evo.md](applications/bmw-nbt-evo.md) | Host-C Transport + free + Media-Leiter |
| Audits | [`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/) · [`msc-host-read-semantics-s1s2s3-2026`](../../audits/msc-host-read-semantics-s1s2s3-2026/) · [`hu-probe-bmw-s0s2-field-2026`](../../audits/hu-probe-bmw-s0s2-field-2026/) · [`hu-probe-bmw-s2-abend-offline-2026-10-18`](../../audits/hu-probe-bmw-s2-abend-offline-2026-10-18/) · [`hu-probe-psram-board-free-2026-10-21`](../../audits/hu-probe-psram-board-free-2026-10-21/) · [`hu-probe-media-ladder-2026-10-22`](../../audits/hu-probe-media-ladder-2026-10-22/) |
| Method S1–S3 | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| Reports | [`2026-10-15`](../../docs/reports/2026-10-15-hu-probe-bmw-s0s2-field.md) · [`2026-10-18`](../../docs/reports/2026-10-18-hu-probe-bmw-s2-abend-offline.md) · [`2026-10-21`](../../docs/reports/2026-10-21-hu-probe-psram-board-free.md) · [`2026-10-22-media-ladder`](../../docs/reports/2026-10-22-hu-probe-media-ladder.md) |

**Stand:** 2026-10-22 · reviewed `hu-probe@8234982` · FW **0.3.17**.
Board **YD-ESP32-S3 N8R2** mit PSRAM; Offline-Capture **1 MiB**; free Grammar +
Media-Leiter (Head 32+128, Tail-Prefetch, Elevator STRONG) geschlossen;
PiDrive = Struktur+Head Pflicht; formal A8 / audible / Lab-Replay B50 offen.
