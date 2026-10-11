# Project Inventory: rnt-esp32 (Fremd-Katalog)

```yaml
project_id: rnt-esp32
updated: 2026-10-11
reviewed_snapshot: "2026-10-11"
profile: lab-tool
source: https://randomnerdtutorials.com/projects-esp32/
pilot_order: [esp-embedded-web-sse, esp-now-messaging, mqtt-node-telemetry, esp-lab-bus-tools, ssd1306-oled-ui]
```

Desk-Index-Scan 2026-10-11. **Sekundärquelle** — Claims aus Tutorials allein höchstens `INFERRED`/`HYPOTHESIS` bis TRM/Code.  
Kampagne: [`rnt-esp32-2026-foreign`](../../audits/rnt-esp32-2026-foreign/).  
Reuse: [`docs/REUSE.md`](../../docs/REUSE.md) · Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md).

**Kein `seen_in` auf Sheets** in diesem Bootstrap: RNT ist Katalog, keine Implementierung. Applications nur bei späterer Vertiefung.

## Reuse / Match (Index → Slug)

| RNT-Signal (Katalog) | Ziel-Sheet | Aktion |
|----------------------|------------|--------|
| Web Server / Async / SPIFFS / LittleFS / SSE / Charts-UI | `esp-embedded-web-sse` | **reuse** — Muster bekannt; Arduino-UI ≠ Hub-Contract |
| ESP-NOW (+ Wi-Fi Web Server Combos) | `esp-now-messaging` | **reuse** |
| MQTT (+ Sensor-Topics) | `mqtt-node-telemetry` | **reuse** |
| GPIO / PWM / Relay / Bus-Lab | `esp-lab-bus-tools` | **reuse** (Lab-Tools-Familie) |
| OLED Displays | `ssd1306-oled-ui` | **reuse** — Geometrie/Controller prüfen |
| BLE GATT / BLE Client-Server | `ble-hrm-gatt` / `ble-hr-relay` | **partial** — HR-Spezial ≠ generisches BLE-Tutorial |
| Bluetooth Classic | `bluetooth-a2dp` | **partial** — Profil ≠ Arduino-Serial-BT-Guide |
| OTA (Arduino / VS Code) | `esp-hub-telemetry` | **partial** — Hub-`otaUrl` ≠ ArduinoOTA-Tutorial |
| Wi-Fi / AP / Hostname / Fixed IP | — | observed (`wifi-sta-ap`) |
| Wi-Fi Manager / Captive | — | observed (`wifi-manager-captive`) |
| mDNS | — | observed (`mdns-discovery`) |
| HTTP GET/POST / Web APIs | — | observed (oft Teil Web-SSE-App) |
| WebSocket | — | observed — **≠** SSE-Sheet still erweitern |
| Firebase / PHP / MySQL Cloud | — | observed — nicht Hub-Familie |
| LoRa | — | observed (`lora-radio`) |
| FreeRTOS Tasks/Queues/Mutex/Timers | — | observed (`freertos-esp`) |
| Deep Sleep / Dual Core | — | observed |
| I2S Mic (INMP441) / MP3-Player Modules | — | observed — Abgrenzung `webradio-browser-host` / `esp32-apll-fm-tx` |
| CYD / Touch Display / RGB Matrix | — | observed / **gap** — Gate vor Sheet |
| Sensors (DHT, BME, DS18B20, PIR, …) | — | observed (`env-sensors`) |
| MAX30102 Pulse Ox / HR Sensor | — | observed — **≠** `ble-hrm-gatt` (PPG on-device vs. BLE Gurt) |
| ESP32-C3 Super Mini Guides | — | Chip-Scope: **nicht** Classic-APLL/S3-Claims übertragen |
| ESP32-CAM / ESP8266 Learn-Links | — | out of family / observed |
| APLL/GPIO FM TX | `esp32-apll-fm-tx` | **Abgrenzung** — nicht im RNT-Index als Kern; kein TX aus Web-Tutorials |

## Übersicht (KB-relevant)

| Slug / Signal | Primary | Status | Coverage | Sheet | Application |
|---------------|---------|--------|----------|-------|-------------|
| `esp-embedded-web-sse` | G | observed | none | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | — |
| `esp-now-messaging` | C | observed | none | [SHEET](../../technologies/esp-now-messaging/SHEET.md) | — |
| `mqtt-node-telemetry` | F | observed | none | [SHEET](../../technologies/mqtt-node-telemetry/SHEET.md) | — |
| `esp-lab-bus-tools` | H | observed | none | [SHEET](../../technologies/esp-lab-bus-tools/SHEET.md) | — |
| `ssd1306-oled-ui` | G | observed | none | [SHEET](../../technologies/ssd1306-oled-ui/SHEET.md) | — |
| `ble-hrm-gatt` | C | observed | none | [SHEET](../../technologies/ble-hrm-gatt/SHEET.md) | — (nur Abgrenzung) |
| `esp-hub-telemetry` | F | observed | none | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | — (OTA-Kontrast) |
| `webradio-browser-host` | A | observed | none | [SHEET](../../technologies/webradio-browser-host/SHEET.md) | — (Audio-Abgrenzung) |
| `esp32-apll-fm-tx` | D | observed | none | [SHEET](../../technologies/esp32-apll-fm-tx/SHEET.md) | — (TX-Abgrenzung) |
| `rf-environment-monitor` | A | observed | none | [SHEET](../../technologies/rf-environment-monitor/SHEET.md) | — (WiFi/BLE-Scan ≠ RNT) |
| `wifi-manager-captive` | F | observed | none | — | — |
| `freertos-esp` | D | observed | none | — | — |
| `esp32-cyd-ui` | G | candidate | none | — | — Gate vor Sheet |
| `i2s-mems-mic` | D | candidate | none | — | — Gate vor Sheet |
| `lora-radio` | A | observed | none | — | — |
| `env-sensors-i2c` | D | observed | none | — | — |

## Coverage-Lücken (bewusst)

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| CYD / große Displays | kein Sheet; Tutorial-lastig | Gate: ein Artikel + TRM/Pin — oder defer |
| FreeRTOS-Patterns | observed | Sheet nur bei Transfer in ≥2 eigenen Projekten |
| Generisches BLE (nicht HR) | nur HR-Sheets | eigenes BLE-Central-Sheet nur bei Bedarf |
| Cloud-Firebase | fremd zum Hub | nicht matchen |

## Signale ohne Eintrag

- Alexa / Telegram / Google Sheets / ThingSpeak — Cloud-Integrationen, kein KB-Fokus
- Solar Panels / Weather Station PCB — Hardware-Kits
- „10 Easy Projects“ / Marketing-Listen — kein Tech-Signal
