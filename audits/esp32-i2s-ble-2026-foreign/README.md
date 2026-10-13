# Audit Campaign: esp32-i2s-ble-2026-foreign

```yaml
id: esp32-i2s-ble-2026-foreign
project_id: esp32-i2s-ble
started: 2026-10-13
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "4d053c4"
reuse_outcomes:
  reused: [esp-i2s-audio]
  new: [ble-pcm-notify-stream]
  not_helped: [bluetooth-a2dp, ble-hrm-gatt]
  process: "Desk custom BLE PCM pattern; README≠Wire-rate gate"
```

## Ziel

I2S-Mic→BLE-Notify-Beispiel als Pattern `ble-pcm-notify-stream` katalogisieren — mit expliziter Abgrenzung zu A2DP/LE Audio und Korrektur Capture- vs. Wire-Sample-Rate.

## Scope

[SCOPE](../../projects/esp32-i2s-ble/SCOPE.md) — Desk only.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.7.1 + lab-tool | erfüllt |
| 2 | Sheets/Apps BLE-PCM + I2S Capture | erfüllt |
| 3 | Evidence `4d053c4`; Wire=8 kHz dokumentiert | erfüllt |
| 4 | C11/C12; kein A2DP-Transfer | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-13) |
| 6 | iOS Packet-Loss Lab | offen (bewusst) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| A2DP-Sheet reuse? | Classic A2DP? | Code NimBLE GATT | Nein → neues Pattern-Sheet | KNOWN BEFORE TEST |
| Wire-Rate 16 oder 8 kHz? | README vs. Code | `EVID-I2SBLE-2026-10-13-002` | Code 8 kHz = FACT | DISCOVERED DURING TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-I2SBLE-2026-10-13-002` | Capture-Rate ≠ Notify-Rate nicht aus README allein lesen | DISCOVERED DURING TEST |
| `EVID-I2SBLE-2026-10-13-001` | Custom UUID ≠ LE Audio / A2DP Claim | KNOWN BEFORE TEST |
| `EVID-I2SBLE-2026-10-13-003` | Ohne Ring/Batching Peer-Drops erwarten | KNOWN BEFORE TEST |
| `EVID-I2SBLE-2026-10-13-004` | Mic SEL/Kanal vor „kein Audio“-Debug prüfen | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** Custom BLE-PCM ist ein dokumentierbares Transfer-Pattern getrennt von Standard-Audio-Profilen.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Repo implementiert LE Audio/A2DP statt Custom GATT | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Pattern-Audit. UNKNOWN iOS-Loss ≠ automatisches STOP; kein Kill-Criterion für „Audio klingt schlecht“ ohne präregistrierte Messgröße.
```

## Knowledge Feedback

Desk only — C13 n/a.

## Bezug

[INVENTORY](../../projects/esp32-i2s-ble/INVENTORY.md) · [evidence](evidence.md) · I2S Player [`esp32-audioi2s-2026-foreign`](../esp32-audioi2s-2026-foreign/) · UAC [`esp-usb-audio-example-2026-foreign`](../esp-usb-audio-example-2026-foreign/)

## Lessons → Transfer

- README und Wire-Contract können divergieren — Code gewinnt für FACT.
- Ringbuffer-Batching ist A-Fallstrick für Custom BLE-Audio, kein Project-Quirk allein.
