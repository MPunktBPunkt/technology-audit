# Project Application: bluetooth-a2dp in squeezelite-esp32

```yaml
project_id: squeezelite-esp32
tech_slug: bluetooth-a2dp
status: active
sheet: ../../../technologies/bluetooth-a2dp/SHEET.md
audit: ../../../audits/squeezelite-esp32-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle

Zwei Rollen (Add-ons am LMS-Core):

1. **Sink:** Stream von Phone/Tablet (BT) in den Player
2. **Source:** Ausgabe an BT-Lautsprecher (nur 44.1 kHz; Resample LMS oder `-R`)

**Chip-Gate:** ESP32-S3 ohne Classic BT Audio — BT-Pfade Classic-ESP32.

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| BT sink + BT speaker source; Source 44.1 kHz | `EVID-SQZ-2026-10-25-006` | `FACT` |
| S3: no Classic BT audio | `EVID-SQZ-2026-10-25-006` | `FACT` |
| Spotify+SPDIF+stats stutter on Classic | `EVID-SQZ-2026-10-25-007` | `FACT` |
