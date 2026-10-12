# Project Application: bluetooth-a2dp in bluetooth-stack

```yaml
project_id: bluetooth-stack
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/bluetooth-stack-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle

A2DP **Sink** (SBC) als Profil im eigenen Host-Stack über HCI H4 — Controller = CSR/BCM/… oder ESP32 mit `BT_VENDOR_COMMON_NO_FW_SUPPORT` (kein Firmware-Download). **Nicht** Espressif Bluedroid on-chip.

| Repo | Commit | Rolle |
|------|--------|-------|
| [sj15712795029/bluetooth_stack](https://github.com/sj15712795029/bluetooth_stack) | `6ef9436` | Stack + projects |

## Architektur / Datenfluss

```text
External BT controller (UART H4)
  → HCI
  → L2CAP / AVDTP
  → A2DP Sink (SBC decode in stack)
  → Host audio (platform-specific)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `component/bluetooth/src/include/classical/bt_a2dp_sink.h` | Sink API / SBC caps |
| `component/bluetooth/third_party_lib/sbc/` | SBC codec |
| `project/linux_bt/bt_config.h` | `PROFILE_A2DP_ENABLE`, vendor flags |
| `component/bluetooth/vendor/bt_vendor_no_fw.*` | ESP32 / no-FW HCI |

## Konfiguration (Desk)

| Parameter | Wert (Beispiel linux_bt) |
|-----------|--------------------------|
| Transport | H4 (`BT_TRANSPORT_TYPE 0x02`) |
| A2DP | `PROFILE_A2DP_ENABLE 1` |
| ESP32 vendor | `BT_VENDOR_COMMON_NO_FW_SUPPORT` (Default **0**) |
| Default vendor | CSR8X11 oft 1 |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| A2DP Sink headers + SBC lib present | `EVID-BTSTK-A2DP-2026-10-12-001` | `FACT` |
| ESP32 = H4_NO_FW vendor path | `EVID-BTSTK-A2DP-2026-10-12-002` | `FACT` |
| Dual-mode classical+BLE compile options | `EVID-BTSTK-A2DP-2026-10-12-003` | `FACT` |
| Stable audio vs. NBT / Bluedroid parity | — | `UNKNOWN` |

## Abweichungen

- README-Matrix „ESP32“ meint Controller an Linux/STM32-Host — nicht `ESP32-A2DP`-Library.
- Lernstack; kommerzielle Reife `UNKNOWN`.
