# Project Inventory: esp32.network

```yaml
project_id: esp32-network
updated: 2026-10-09
reviewed_commit: 3b9b82d
profile: firmware
pilot_order: [lan-device-inventory, fritzbox-tr064, esp-embedded-web-sse, esp-hub-telemetry]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.2](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Subnet/TCP Geräteinventur | `lan-device-inventory` | **neu** (≠ rf-environment-monitor) |
| FritzBox TR-064 HTTPS 49443 | `fritzbox-tr064` | **neu** |
| SSE Scan-Progress | `esp-embedded-web-sse` | wachsen |
| Hub ohne fwType | `esp-hub-telemetry` | wachsen |

Ursprung: [esp32.network](https://github.com/MPunktBPunkt/esp32.network).  
Kampagne: [esp32-network-2026-pilot](../../audits/esp32-network-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `lan-device-inventory` | LAN Device Inventory | H | `lab-only` | applied | partial | [SHEET](../../technologies/lan-device-inventory/SHEET.md) | [app](applications/lan-device-inventory.md) |
| `fritzbox-tr064` | FritzBox TR-064 | F | — | applied | partial | [SHEET](../../technologies/fritzbox-tr064/SHEET.md) | [app](applications/fritzbox-tr064.md) |
| `esp-embedded-web-sse` | Embedded Web + SSE | G | `streaming` | applied | partial | [SHEET](../../technologies/esp-embedded-web-sse/SHEET.md) | [app](applications/esp-embedded-web-sse.md) |
| `esp-hub-telemetry` | ESP-Hub Telemetry | F | `esp-idf` | applied | partial | [SHEET](../../technologies/esp-hub-telemetry/SHEET.md) | [app](applications/esp-hub-telemetry.md) |
| `wifi-manager-captive` | WiFiManager | F | — | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Feldserie | Desk-Audit | Evidence nachziehen |

## Signale ohne Eintrag

- WiFiManager / NVS — observed-Familie
