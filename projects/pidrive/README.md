# Project: PiDrive

Erstes Audit-Zielprojekt. Raspberry-Pi-/ESP32-Infotainment mit BMW-iDrive-Anbindung — hoher Technologie-Mix, deshalb der Maßstab für diesen Dokumentenstandard.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen und Quellen |
| [INVENTORY.md](INVENTORY.md) | Technologie-Inventar (Gerüst) |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | Folgeprojekt-Ideen |
| [applications/usb-msc.md](applications/usb-msc.md) | MSC-Anwendung (B) |
| [applications/bmw-nbt-evo.md](applications/bmw-nbt-evo.md) | Pilot 2: NBT Host (C) |
| [applications/](applications/) | Radio/FFT: dab-plus, rtl-sdr, pmr446, airband-am, sdr-spectrum-fft · BT: bluetooth-a2dp, avrcp |
| Audits | [`pidrive-2026-msc`](../../audits/pidrive-2026-msc/) (closed) · [`pidrive-2026-bmw-hu`](../../audits/pidrive-2026-bmw-hu/) (active) · [`pidrive-2026-radio-bt`](../../audits/pidrive-2026-radio-bt/) (active) |

**Pilot-Reihenfolge:** `usb-msc` → `bmw-nbt-evo` → Radio/FFT → A2DP/AVRCP (siehe Inventar).

Ursprungsrepos: `MPunktBPunkt/pidrive`, `MPunktBPunkt/esp32.pidrive` (und verwandte ESP-/BT-Arbeiten).  
Firmware-Desk: [`esp32-pidrive`](../esp32-pidrive/) · BT-Planung: [`esp32-bt-gateway`](../esp32-bt-gateway/).
