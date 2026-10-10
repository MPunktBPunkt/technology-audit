# Project Application: bluetooth-a2dp in PiDrive

```yaml
project_id: pidrive
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/pidrive-2026-radio-bt/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle

BlueZ + PipeWire/WirePlumber: A2DP-Sink zur BMW-HU; `bt_audio.py` Profil/Default-Sink/Stream-Move. Parallel-Pfad USB-Gadget (`esp32.pidrive`) über `audio_output` — nicht gleichzeitig.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| A2DP Routing via PipeWire/pactl | `EVID-A2DP-2026-10-09-001` | `FACT` |
| Kontrast ESP-Gateway-Planung | — | siehe [`esp32-bt-gateway`](../../esp32-bt-gateway/applications/bluetooth-a2dp.md) |
