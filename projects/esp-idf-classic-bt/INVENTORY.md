# Project Inventory: esp-idf-classic-bt (Fremd)

```yaml
project_id: esp-idf-classic-bt
updated: 2026-10-12
reviewed_commit: "86f72d0"
profile: lab-tool
pilot_order: [bluetooth-a2dp, avrcp]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| A2DP Sink/Source | `bluetooth-a2dp` | **reuse** |
| AVRCP CT/TG / Meta / Volume | `avrcp` | **reuse** |
| HFP / SPP / HID Examples | `bluetooth-hfp`, `bluetooth-spp`, `bluetooth-hid` | **documented** — [`bt-classic-gaps-2026-foreign`](../../audits/bt-classic-gaps-2026-foreign/) |

Kampagne: [`esp-idf-classic-bt-2026-foreign`](../../audits/esp-idf-classic-bt-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `bluetooth-a2dp` | Bluetooth A2DP | C | applied | partial | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `avrcp` | AVRCP | C | applied | partial | [SHEET](../../technologies/avrcp/SHEET.md) | [app](applications/avrcp.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| NBT-Evo Lab | Desk | Gateway FOLLOW-ON |

## Signale ohne Eintrag

- PAN/OPP/L2CAP demos — observed; HFP/SPP/HID → Sheets unter `bt-classic-profile-refs`
