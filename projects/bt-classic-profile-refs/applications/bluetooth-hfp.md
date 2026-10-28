# Project Application: bluetooth-hfp in bt-classic-profile-refs

```yaml
project_id: bt-classic-profile-refs
tech_slug: bluetooth-hfp
status: active
sheet: ../../../technologies/bluetooth-hfp/SHEET.md
audit: ../../../audits/bt-classic-gaps-2026-foreign/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle

HFP HF/AG Evidenz aus a2dpSinkHfpClient, EspBle, esp32-hsp-hf (BTstack), IDF hfp_hf/ag.

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| a2dpSink: HF Client, Classic-only, call APIs | `EVID-BTCL-2026-10-28-001` | `FACT` |
| a2dpSink: HCI-SCO + mSBC path + I2S mux vs A2DP | `EVID-BTCL-2026-10-28-002` | `FACT` |
| EspBle: HFP Client + AG auf ESP32 | `EVID-BTCL-2026-10-28-010` | `FACT` |
| esp32-hsp-hf: HFP HF (nicht HSP) + SCO CVSD/mSBC | `EVID-BTCL-2026-10-28-020` | `FACT` |
| IDF hfp_hf: BR/EDR-only + HFP client enable | `EVID-BTCL-2026-10-28-030` | `FACT` |
