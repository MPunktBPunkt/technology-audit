# Audit Campaign: esp-fm-tx-2026-foreign

```yaml
id: esp-fm-tx-2026-foreign
project_id: esp-fm-tx
started: 2026-10-11
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
reviewed_commit: "ESP32FMRadio@f62c72b esp32_fm_radio@870dc33"
reuse_outcomes:
  - new_sheet: esp32-apll-fm-tx
  - process: "0.6.6 chip-transfer gates + kb-cross-check"
  - contrast: rpi-gpio-fm-tx
```

## Ziel

Fremd-Repos zu Classic-ESP32 **APLL/MCLK-FM** in die KB: eigenständiger Slug, Chip-Scope, Abgrenzung zu Pi-TX und zu ESP32-S3 (Gate). Auslöser: KB-Cross-Check 2026-10-11 (Auditwissen → Machbarkeitsfrage Hub-FM-Knoten).

## Scope

[SCOPE](../../projects/esp-fm-tx/SCOPE.md) — Desk only; **keine** Antennen-Feldversuche.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.6 + lab-tool | erfüllt |
| 2 | Sheet `esp32-apll-fm-tx` + Application + Evidence (2 Repos) | erfüllt |
| 3 | Compile-Guard / kein S3-Transfer als FACT | erfüllt |
| 4 | Signalpfad-Kette im Sheet mit Status pro Stufe | erfüllt |
| 5 | FOLLOW-ON E-0/E-1 für S3; kein S3-Sheet | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-11) |
| 7 | Lab-Träger/Harmonics gemessen | offen (bewusst) |

## Lessons (vorläufig)

- Zwei Upstreams bestätigen denselben RF-Contract → Sheet gerechtfertigt (nicht nur eine GitHub-Kuriosität).
- Tiefe bei hiperiondev (`polar_mod`) bleibt Application — gleicher Slug.
- Cross-Check-Wert: Absolutismus „einziger Kandidat“ und S3-Transfer wurden Prozessregeln (G17–G19).

## Bezug

[INVENTORY](../../projects/esp-fm-tx/INVENTORY.md) · [evidence](evidence.md) · Kontrast [`pi-fm-tx-2026-foreign`](../pi-fm-tx-2026-foreign/) · Methods [`hw-path-gate`](../../methods/hw-path-gate.md), [`kb-cross-check`](../../methods/kb-cross-check.md)
