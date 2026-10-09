# Project Inventory: esp32.webradio

```yaml
project_id: esp32-webradio
updated: 2026-10-09
reviewed_commit: caee2f8
profile: firmware
pilot_order: [webradio-browser-host, esp-hub-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.2](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| ESP hostet UI, Browser spielt Streams | `webradio-browser-host` | **neu** |
| Hub Heartbeat ohne fwType | `esp-hub-telemetry` | wachsen |
| REST Web-UI ohne SSE | `embedded-web-ui` | observed — nicht esp-embedded-web-sse |
| radio-browser.info Discovery | `radio-browser-api` | observed |
| mDNS webradio-*.local | `mdns-discovery` | observed |
| A2DP | `bluetooth-a2dp` | **kein Match** (explizit abgelehnt) |

Ursprung: [esp32.webradio](https://github.com/MPunktBPunkt/esp32.webradio).  
Kampagne: [esp32-webradio-2026-pilot](../../audits/esp32-webradio-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `webradio-browser-host` | Web-Radio Browser Host | G | `streaming` | applied | partial | [SHEET](../../technologies/webradio-browser-host/SHEET.md) | [app](applications/webradio-browser-host.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `embedded-web-ui` | Embedded Web (poll) | G | — | observed | none | — | — |
| `radio-browser-api` | radio-browser.info | F | — | observed | none | — | — |
| `mdns-discovery` | mDNS | F | — | observed | none | — | — |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Feldserie | Desk-Audit | Evidence nachziehen |

## Signale ohne Eintrag

- WiFiManager / NVS — observed-Familie
