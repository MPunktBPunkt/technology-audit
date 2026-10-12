# Project Inventory: bluetooth-stack (Fremd)

```yaml
project_id: bluetooth-stack
updated: 2026-10-12
reviewed_commit: "6ef9436"
profile: lab-tool
pilot_order: [bluetooth-a2dp, avrcp]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.6](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| A2DP Sink (SBC) im Host-Stack | `bluetooth-a2dp` | **reuse** (HCI-Host-Zelle) |
| AVRCP Controller code present | `avrcp` | **reuse** (Profile oft compile-off) |
| ESP32 in Matrix | `bluetooth-a2dp` | Controller-über-HCI; **nicht** Bluedroid |
| HFP/PBAP/SPP/GATT | — | observed, nicht vertieft |

Kampagne: [`bluetooth-stack-2026-foreign`](../../audits/bluetooth-stack-2026-foreign/).

## Übersicht

| Slug | Name | Primary | Status | Coverage | Sheet | Application |
|------|------|---------|--------|----------|-------|-------------|
| `bluetooth-a2dp` | Bluetooth A2DP | C | applied | partial | [SHEET](../../technologies/bluetooth-a2dp/SHEET.md) | [app](applications/bluetooth-a2dp.md) |
| `avrcp` | AVRCP | C | applied | partial | [SHEET](../../technologies/avrcp/SHEET.md) | [app](applications/avrcp.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| ESP32 HCI bring-up Lab | Flag default 0 | Gate + Messung |
| AVRCP Enable in linux_bt | oft 0 in bt_config | explizit aktivieren + testen |

## Signale ohne Eintrag

- HFP HF, PBAP, SPP, BAS — Profile vorhanden, out of focus
- STM32 board packages — BSP, kein Tech-Slug
