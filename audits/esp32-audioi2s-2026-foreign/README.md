# Audit Campaign: esp32-audioi2s-2026-foreign

```yaml
id: esp32-audioi2s-2026-foreign
project_id: esp32-audioi2s
started: 2026-10-13
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "45db753"
reuse_outcomes:
  reused: [bluetooth-a2dp, webradio-browser-host]
  new: [esp-i2s-audio]
  not_helped: []
  process: "Desk foreign I2S decode-player under 0.7.1"
```

## Ziel

schreibfaul1/ESP32-audioI2S (`45db753`) als Referenz-I2S-Player in die KB — Chip-/PSRAM-Gates und Abgrenzung Browser-Webradio / A2DP.

## Scope

[SCOPE](../../projects/esp32-audioi2s/SCOPE.md) — Desk only.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.7.1 + lab-tool | erfüllt |
| 2 | Sheet `esp-i2s-audio` + Application | erfüllt |
| 3 | Evidence Commit `45db753` | erfüllt |
| 4 | C11 Chip-Gates; C12 Kill klar | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (2026-10-13) |
| 6 | DAC Labmatrix | offen (bewusst) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neuer Slug vs. webradio-browser-host? | Audio-Ort Browser oder I2S? | `EVID-AUDIOI2S-2026-10-13-002` | I2S → `esp-i2s-audio` | KNOWN BEFORE TEST |
| A2DP Example = neues Sheet? | Nur Bridge? | Example README | Nein — Kontrast `bluetooth-a2dp` | KNOWN BEFORE TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-AUDIOI2S-2026-10-13-001` | Vor Portierung: Chip multi-core? S2/C3 = STOP-Transfer | KNOWN BEFORE TEST |
| `EVID-AUDIOI2S-2026-10-13-003` | PSRAM-Anforderung der Library prüfen | KNOWN BEFORE TEST |
| `EVID-AUDIOI2S-2026-10-13-002` | DAC/BT-Modul Sample-Rate-Contract ≠ Quellrate annehmen | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** Library ist gültige Desk-Referenz für I2S-Decode-Player auf unterstützten Chips.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Upstream behauptet S2/C3-Support ohne Einschränkung | nicht eingetreten (explizite Warnung) |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Audit ohne Messlauf. Chip-Gates sind Transfer-STOP, kein Lab-Kill. UNKNOWN DAC-Qualität ≠ automatisches STOP.
```

## Knowledge Feedback

Desk only — C13 n/a.

## Bezug

[INVENTORY](../../projects/esp32-audioi2s/INVENTORY.md) · [evidence](evidence.md) · A2DP [`esp32-a2dp-2026-foreign`](../esp32-a2dp-2026-foreign/) · Browser [`esp32-webradio-2026-pilot`](../esp32-webradio-2026-pilot/)

## Lessons → Transfer

- On-device I2S-Player und Browser-Host-Webradio teilen „Radio“-Wort, nicht den Contract.
- A2DP-Example ist Lateralpfad, kein Ersatz für I2S-Sheet.
