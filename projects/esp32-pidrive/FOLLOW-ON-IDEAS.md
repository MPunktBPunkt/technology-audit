# Folgeprojekte

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Sheets `scsi` / `fat` aus Geometrie-Leitern (L0/L3) | `usb-msc`, `virtual-fat` | A-Abgrenzung |
| SSE/Live-Status für SoftAP-UI | `esp-embedded-web-sse` | heute REST-Polling |
| LBA/Timing-Instrumentierung am Read-Callback | `msc-lba-timing-instrument`, Gadget-Refs | HU-Burst/Latenz messen |
| Trace ↔ PUMP `msc.reads` + AV | `msc-trace-correlation`, Lab `nbt_*.py` | Korrelation nach Gate |
| On-the-fly Body (kein Full-Disk-PSRAM) | `virtual-fat`, aoscarius-Hooks | Live-MP3 ohne RAM-Image |
| Bridge in PiDrive systemd verdrahten | `pump-control-link` | Ops bei `pidrive` |

Gadget-Referenzen: [`esp32-msc-gadget-refs`](../esp32-msc-gadget-refs/).
