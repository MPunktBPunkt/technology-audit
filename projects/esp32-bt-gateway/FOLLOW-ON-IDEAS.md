# Folgeprojekte (aus esp32.bt-gateway)

| Idee | Nutzt | Lücke |
|------|-------|-------|
| Phase-0-Firmware nach A17 | `bluetooth-a2dp`, `avrcp`, `pdap` | Stack + Coex-Messung |
| Analyzer-Mode am Gateway | `bmw-nbt-evo`, `avrcp` | Observe-first Logs |
| PiDrive Output `gateway` | `pdap` | Client-Integration |
| Zweites Sink-Fahrzeug | `bmw-nbt-evo` Pattern | neues Host-Sheet |
| Pi BlueZ-Betrieb als Referenz | `bluetooth-a2dp`, `avrcp` | Desk: [`pidrive-2026-radio-bt`](../../audits/pidrive-2026-radio-bt/) |
| ESP Bluedroid Library-Baseline | `bluetooth-a2dp`, `avrcp` | Desk: [`esp32-a2dp-2026-foreign`](../../audits/esp32-a2dp-2026-foreign/) |
| EspBle CT/TG + Dual-Host | `avrcp`, `bluetooth-a2dp` | Desk: [`espble-2026-foreign`](../../audits/espble-2026-foreign/) — TG Volume-Limit |
| IDF Cover Art / Abs Volume SoT | `avrcp` | Desk: [`esp-idf-classic-bt-2026-foreign`](../../audits/esp-idf-classic-bt-2026-foreign/) |
| Sink+HFP API-Vergleich | `avrcp` | Desk: [`a2dpsinkhfpclient-2026-foreign`](../../audits/a2dpsinkhfpclient-2026-foreign/) |
| HCI-Host-Stack als Alternative | `bluetooth-a2dp` | Desk: [`bluetooth-stack-2026-foreign`](../../audits/bluetooth-stack-2026-foreign/) — Kontrast, kein Default |
