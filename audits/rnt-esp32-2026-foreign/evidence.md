# Evidence — rnt-esp32-2026-foreign

Desk-Katalog-Scan 2026-10-11 · **standard_version 0.6.6** · Profile `lab-tool` · Quelle **sekundär**.

| Quelle | Snapshot | Art |
|--------|----------|-----|
| https://randomnerdtutorials.com/projects-esp32/ | 2026-10-11 | Web-Index (kein Git-Commit) |

Roh-Tutorial-Texte werden **nicht** archiviert. Evidence = Index-Beobachtungen + Match-Entscheidungen.

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-RNT-2026-10-11-001` | Öffentlicher Index „250+ ESP32 Projects…“ mit Themenclustern (Web, BLE, ESP-NOW, MQTT, OTA, Sensoren, …) | `FACT` | Index-Seite @ Snapshot |
| `EVID-RNT-2026-10-11-002` | Starke Überlappung mit bestehenden Slugs: Web/SSE, ESP-NOW, MQTT, Lab-GPIO, OLED | `INFERRED` | Match gegen `technologies/index.yaml` |
| `EVID-RNT-2026-10-11-003` | Viele Guides Arduino-IDE / „ESP32“ ohne SoC-Variante — Chip-Scope nötig vor Transfer | `INFERRED` | Katalog-Titel/Cluster + G17 |
| `EVID-RNT-2026-10-11-004` | Airspy/CYD/FreeRTOS/LoRa/Firebase erscheinen als Themen — kein Sheet aus Katalog allein | `FACT` | Inventar observed/candidate; G19 |
| `EVID-RNT-2026-10-11-005` | MAX30102-/PPG-Tutorials ≠ BLE-HRM-Gurt-Contract (`ble-hrm-gatt`) | `INFERRED` | Themenabgrenzung Katalog vs. Sheet |
| `EVID-MATCH-2026-10-11-003` | Bootstrap: keine Applications, kein `seen_in` — Katalog ≠ Implementierungsprojekt | `FACT` | Kampagnen-Exit |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Konkreter Artikel bestätigt Sheet-Fallstrick X | `UNKNOWN` | FOLLOW-ON Vertiefung |
| Index unverändert seit Snapshot | `UNKNOWN` | bei Rescan erneuern |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-11 | Bootstrap Fremd-Katalog; Match-Tabelle; keine Tutorial-Ingest |
