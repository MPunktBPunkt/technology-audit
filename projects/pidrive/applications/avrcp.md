# Project Application: avrcp in PiDrive

```yaml
project_id: pidrive
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/pidrive-2026-radio-bt/
maturity:
  technology: R2
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle

BMW als AVRCP-Controller → `avrcp_trigger.py` (D-Bus MediaPlayer1 / Pass-Through) → `/tmp/pidrive_cmd`. WebUI/Probe-Tab; Ringbuffer Events. Meta oft über MPRIS-Brücke — getrennt vom ESP-Gateway-Zielbild (Target auf ESP).

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| D-Bus → File-Trigger Bridge | `EVID-AVRCP-2026-10-09-001` | `FACT` |
| HU-Tasten nicht alle als AVRCP | `EVID-AVRCP-2026-10-09-002` | `FACT` (Sheet + Probe) |
| Gateway-Alternative | — | [`esp32-bt-gateway` avrcp](../../esp32-bt-gateway/applications/avrcp.md) |
