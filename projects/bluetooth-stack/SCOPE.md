# Project Scope: bluetooth-stack (Fremd)

```yaml
project_id: bluetooth-stack
title: bluetooth_stack — Lightweight Dual-Mode BT Host Stack (Fremd)
updated: 2026-10-12
profile_hint: lab-tool
reviewed_commit: "6ef9436"
repos:
  - https://github.com/sj15712795029/bluetooth_stack
status: active
```

## Zweck

Kontrastzelle: **Host-Stack** (HCI H4) mit A2DP/AVRCP/HFP/… auf STM32/Linux — Controller separat (CSR/BCM/…, ESP32 als `H4_NO_FW`). Zeigt: Profile-Slug ≠ Bluedroid-on-chip.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| sj15712795029/bluetooth_stack | Lern-/Leichtgewicht-Stack | ja (Desk) |
| linux_bt + vendor H4_NO_FW | ESP32 als HCI-Controller | ja (Signal) |
| On-chip ESP Bluedroid | — | **Abgrenzung** (`esp32-a2dp`) |
| Feld-NBT | — | **nein** |

## Nicht-Ziele

- Stack als Drop-in für Gateway ohne Lab behaupten
- AVRCP-Browse aus Compile-Flags ableiten

## Prioritäten

1. Applications A2DP (+ AVRCP observed) mit Stack-Kontrast  
2. Sheet-Fallstrick: HCI-Host ≠ Bluedroid  
3. ESP32-Zeile in Matrix = Controller, nicht Firmware-Stack
