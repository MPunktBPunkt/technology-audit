# Project Application: esp32-s3-silicon in esp32-usb-analyzer

```yaml
project_id: esp32-usb-analyzer
tech_slug: esp32-s3-silicon
status: active
sheet: ../../../technologies/esp32-s3-silicon/SHEET.md
audit: ../../../audits/esp32-usb-analyzer-2026-pilot/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle im Projekt

Beide Lab-Nodes: **YD-ESP32-S3 N8R2**. OTG Full-Speed; Host/Device getrennte Chips. UART/COM (CH343) für Bring-up — Internal-PHY vs Serial/JTAG sharing beachten.

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `docs/LAB_INVENTORY.md` | `.88` / `.89` boards |
| `docs/HARDWARE-RISKS.md` | Risk register |
| `docs/HUB-BASELINE.md` | Partition / OTA family notes |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Lab boards N8R2 Host/Device | `EVID-USBA-2026-10-31-016` | `FACT` (inventory) |
| FS-only Host | Sheet / Gate1 | `FACT` |
| PSRAM automatically used | Sheet | `REJECTED` still — not claimed healed |

## Beobachtungen

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| Lab | Serial oft ein UART im LXC; OTG ≠ COM |

## Verwandte Applications / Methods

- hu-probe silicon Application (PSRAM field)
- Coex Application (USB+WiFi simultaneous)
