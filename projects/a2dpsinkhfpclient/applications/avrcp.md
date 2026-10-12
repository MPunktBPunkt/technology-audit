# Project Application: avrcp in a2dpsinkhfpclient

```yaml
project_id: a2dpsinkhfpclient
tech_slug: avrcp
status: active
sheet: ../../../technologies/avrcp/SHEET.md
audit: ../../../audits/a2dpsinkhfpclient-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle

Explizite AVRC-API: `a2dpSinkHfpHf_avrc_play/pause/next/prev`, `get_avrc_metadata()` → `bt_avrc_metadata_t` (title/artist/album/…). Header: CT **und** TG Init-Pfade in `bt_app_avrc`.

## Relevante Pfade

| Pfad | Rolle |
|------|-------|
| `include/bt_app_avrc.h` | Metadata struct + CT/TG |
| `src/bt_app_avrc.c` | Implementation |
| README Music Control | Public wrappers |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Explicit avrc_play/pause/next/prev + metadata struct | `EVID-HFPCLI-AVRCP-2026-10-12-001` | `FACT` |
| bt_app_avrc documents CT and TG | `EVID-HFPCLI-AVRCP-2026-10-12-002` | `FACT` |
