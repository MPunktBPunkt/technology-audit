# Project Inventory: esp32-a2dp-codecs (Fremd)

```yaml
project_id: esp32-a2dp-codecs
updated: 2026-10-12
reviewed_commit: "cfint@bf8b482 WillyBilly06@f4eb125"
profile: lab-tool
pilot_order: [bluetooth-a2dp, avrcp]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Multi-codec A2DP Sink | `bluetooth-a2dp` | **reuse** (Codec-Fallstricke) |
| AVRCP parallel | `avrcp` | **reuse** (dünn) |

Kampagne: [`esp32-a2dp-codecs-2026-foreign`](../../audits/esp32-a2dp-codecs-2026-foreign/).

## Übersicht

| Slug | Name | Status | Sheet | Application |
|------|------|--------|-------|-------------|
| `bluetooth-a2dp` | A2DP | applied | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `avrcp` | AVRCP | applied | [SHEET](../../technologies/avrcp/SHEET.md) | [app](applications/avrcp.md) |

## Coverage-Lücken

| Bereich | Nächster Schritt |
|---------|------------------|
| Eigene Codec-Matrix vs. Phone | Lab / cfint a2dp-codec-tests |
