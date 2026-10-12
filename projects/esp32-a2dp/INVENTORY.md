# Project Inventory: esp32-a2dp (Fremd)

```yaml
project_id: esp32-a2dp
updated: 2026-10-12
reviewed_commit: "a9e946a"
profile: lab-tool
pilot_order: [bluetooth-a2dp, avrcp]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| A2DP Sink/Source Bluedroid + SBC | `bluetooth-a2dp` | **reuse** (ESP-Stack-Zelle) |
| AVRCP Meta / Pass-Through mit A2DP | `avrcp` | **reuse** (ESP-Stack-Zelle) |
| HFP/HSP / AVRCP ohne A2DP | — | observed (Upstream: nicht supported) |
| BLE parallel (`ESP_BT_MODE_BTDM`) | — | observed Coex-Beispiel; kein Sheet |

Kampagne: [`esp32-a2dp-2026-foreign`](../../audits/esp32-a2dp-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `bluetooth-a2dp` | Bluetooth A2DP | C | applied | partial | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `avrcp` | AVRCP | C | applied | partial | [SHEET](../../technologies/avrcp/SHEET.md) | [app](applications/avrcp.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| NBT-Evo Sink-Stabilität | Desk only | Gateway Lab / `bmw-nbt-evo` |
| AAC Endpoint auf IDF 6.1+ | Upstream runtime-gated | gemessenes SEP-Register |
| WiFi+Classic Coex unter Last | Beispiel vorhanden, keine Messung | Coex-Gate |

## Signale ohne Eintrag

- SPP Support-Flag in `config.h` — Nebenpfad, nicht inventarisiert
- AudioTools-Ökosystem — Output-API, kein eigener Profile-Slug
