# Audit Campaign: pi-fm-tx-2026-foreign

```yaml
id: pi-fm-tx-2026-foreign
project_id: pi-fm-tx
started: 2026-10-10
ended: null
status: active
profile: lab-tool
standard_version: "0.6.3"
reviewed_commit: "pifm@6c30d00 PiFmRds@2707ecc fm_transmitter@322500e rpitx@ee7ff57 Pi-Fm_transmitter@552f955 pi-fm-player@f602f42"
```

## Ziel

Fremd-Repos zu Pi-Software-TX in die KB: UKW-FM-Linie (pifm → markondej → Wrapper) und **rpitx** Multi-Mode — Match gegen Empfangs-Sheets, Recht/Filter/Pi-Modell als Fallstricke, Kontrast PiDrive.

## Scope

[SCOPE](../../projects/pi-fm-tx/SCOPE.md) — Desk only; **keine** Antennen-Feldversuche.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.3 + lab-tool | erfüllt |
| 2 | Reuse: RX-Sheets nicht missbraucht; Forks ohne Sheet-Explosion | erfüllt |
| 3 | Sheets `rpi-gpio-fm-tx`, `fm-rds`, `rpitx` + Apps | erfüllt |
| 4 | Evidence für alle sechs Repos | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 6 | Geschirmter Lab-Loopback gemessen | offen (bewusst) |

## Bezug

[INVENTORY](../../projects/pi-fm-tx/INVENTORY.md) · [evidence](evidence.md) · Empfang [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/)
