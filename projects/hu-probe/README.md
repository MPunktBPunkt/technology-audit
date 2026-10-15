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
| [applications/usb-msc.md](applications/usb-msc.md) | Device/Instrument + Offline |
| [applications/bmw-nbt-evo.md](applications/bmw-nbt-evo.md) | Host-C Transport S0/S2 |
| Audits | [`esp32-s3-usb-wifi-coexistence-2026`](../../audits/esp32-s3-usb-wifi-coexistence-2026/) · [`msc-host-read-semantics-s1s2s3-2026`](../../audits/msc-host-read-semantics-s1s2s3-2026/) · [`hu-probe-bmw-s0s2-field-2026`](../../audits/hu-probe-bmw-s0s2-field-2026/) |
| Method S1–S3 | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| Report Feld | [`2026-10-15-hu-probe-bmw-s0s2-field`](../../docs/reports/2026-10-15-hu-probe-bmw-s0s2-field.md) |

**Stand:** 2026-10-15 · reviewed `hu-probe@5dbec43`. Coex-Desk geschlossen;
S1–S3-Messplan geschlossen; **S0/S2 Transport-Feld** geschlossen (Semantik offen).
P1c Profil-Upstream und Auto-Offline offen.
