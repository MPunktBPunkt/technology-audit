# AUDIT DELTA — pidrive-2026-bmw-hu

```yaml
campaign: pidrive-2026-bmw-hu
old_standard: "0.5.1"
new_standard: "0.6.6"
revalidated: 2026-10-11
method: process parity + desk re-read of existing C-register (no new field session)
note: "mixes framework jump (0.5.1→0.6.6) with historically evolved evidence; DELTA separates both"
```

## OLD AUDIT (0.5.1)

| Bereich | Stand |
|---------|--------|
| Claims | Host-Sheet `bmw-nbt-evo`; C-Claims MSC-Prefetch/Seed/AV; Lab≠Feld-Ohr |
| Gaps | `reuse-playbook`, `audit-profiles`, `sheet-checklists`, `standard_version-field` |
| Evidence | USBMSC-* + BMWHU-* (2026-10-04/05) |
| UNKNOWN | Feld-AV / Ohr-PASS |

## NEW AUDIT (0.6.6 Revalidation)

| Bereich | Delta |
|---------|--------|
| Framework | Profile `ops-field` bestätigt; Reuse-Match; Checklisten; `standard_version` 0.6.6; Gaps geschlossen |
| Host-Scope (G17-analog) | Claims = **NBT Evo** in PiDrive-Kontext — nicht still Evo2/andere HU |
| Schicht | C bleibt in Application; `usb-msc` ohne HU-Timing (bereits gut) |
| Gates | Feld-Ohr weiter `UNKNOWN`; kein neues HU-Varianten-Sheet; AVRCP → radio-bt / Gateway, nicht USB-C duplizieren |
| Source-Evolution | Register bleibt Stand 2026-10-05 Artefakte — **kein** stilles Nachziehen neuer Upstream-Feldläufe in dieser Revalidation |
| Cross-Project | `esp32-bt-gateway` / `avrcp` angrenzend; MSC-Pilot closed als Vorgänger |

## Quantitativ

| Metrik | 0.5.1 | nach 0.6.6 | Δ |
|--------|-------|------------|---|
| Host-Sheet | 1 | 1 | 0 |
| Evidence-IDs (Register) | 12 | 14 | +2 Prozess/Scope |
| Offene Exit Ohr | 1 | 1 | 0 (bewusst) |
| `standard_gaps` | 4 Items | keine | Parität |

## Urteil

Wert liegt im **Framework-Sprung** und der expliziten Host-Varianten-Bremse — nicht in neuen Ohr-PASSes. Vergleich zu pi-fm-tx ist schwieriger (Source+Prozess), aber für Audit-Qualität der älteste relevante PiDrive-Fall.

## Nachtrag 2026-10-12 (nicht Teil der 0.6.6-Revalidation)

Busy-Pacing E7/S6 am NBT: `EVID-BMWHU-2026-10-12-001`–`005`. Exit #6 (Menü/Sender-Gate) bleibt offen — Busy-Pacing-Ton ≠ globales Ohr-PASS. Framework-Nachzug: Standard **0.7.0** (Decision Trace / Review Checks / Kill / Knowledge Feedback).

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Kampagne | [README.md](README.md) |
| Sheet | [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md) |
| App C | [`applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) |
| Radio/BT | [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/) |
