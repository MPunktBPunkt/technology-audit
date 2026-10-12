# Project Inventory: a2dpsinkhfpclient (Fremd)

```yaml
project_id: a2dpsinkhfpclient
updated: 2026-10-12
reviewed_commit: "db7ff2f"
profile: lab-tool
pilot_order: [bluetooth-a2dp, avrcp]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| A2DP Sink/Source | `bluetooth-a2dp` | **reuse** |
| AVRCP CT/TG / Meta / Volume | `avrcp` | **reuse** |
| HFP (falls vorhanden) | — | observed |

Kampagne: [`a2dpsinkhfpclient-2026-foreign`](../../audits/a2dpsinkhfpclient-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `bluetooth-a2dp` | Bluetooth A2DP | C | applied | partial | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `avrcp` | AVRCP | C | applied | partial | [SHEET](../../technologies/avrcp/SHEET.md) | [app](applications/avrcp.md) |
| `bluetooth-hfp` | HFP HF | C | observed | none | — | — |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| NBT-Evo Lab | Desk | Gateway FOLLOW-ON |

## Signale ohne Eintrag

- HFP/PBAP/SPP wo vorhanden — observed
