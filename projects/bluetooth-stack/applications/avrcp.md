# Project Application: avrcp in bluetooth-stack

```yaml
project_id: bluetooth-stack
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/bluetooth-stack-2026-foreign/
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0
  reusability: W2
```

## Rolle

AVRCP **Controller**-Implementierung im Host-Stack (`bt_avrcp_controller.h`); in mehreren `bt_config.h` ist `PROFILE_AVRCP_ENABLE` default **0** — Code vorhanden ≠ aktiviert/feldgetestet.

## Architektur / Datenfluss

```text
Host app
  → AVRCP Controller (AVCTP)
  → Peer Target (Speaker/Phone)
  (optional parallel A2DP Sink path)
```

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `component/bluetooth/src/include/classical/bt_avrcp_controller.h` | Controller API |
| `component/bluetooth/src/include/classical/bt_avctp.h` | AVCTP |
| `project/*/bt_config.h` | `PROFILE_AVRCP_ENABLE` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| AVRCP Controller sources exist | `EVID-BTSTK-AVRCP-2026-10-12-001` | `FACT` |
| linux_bt default AVRCP off | `EVID-BTSTK-AVRCP-2026-10-12-002` | `FACT` |
| Browse/Meta vs. NBT | — | `UNKNOWN` |

## Offene Fragen

- Welcher AVRCP-Feature-Subset ist im Stack fertig vs. Stub?
