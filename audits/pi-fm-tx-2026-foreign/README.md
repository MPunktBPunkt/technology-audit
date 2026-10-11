# Audit Campaign: pi-fm-tx-2026-foreign

```yaml
id: pi-fm-tx-2026-foreign
project_id: pi-fm-tx
started: 2026-10-10
ended: null
status: active
profile: lab-tool
standard_version: "0.6.6"
revalidated_from: "0.6.3"
revalidated: 2026-10-11
reviewed_commit: "pifm@6c30d00 PiFmRds@2707ecc fm_transmitter@322500e rpitx@ee7ff57 Pi-Fm_transmitter@552f955 pi-fm-player@f602f42"
reuse_outcomes:
  - reused: [rpi-gpio-fm-tx, fm-rds, rpitx]
  - sharpened: "0.6.6 chip-scope + signal path + RP1 gate (no new sheet)"
  - contrast: esp32-apll-fm-tx
  - process: "revalidation delta vs 0.6.3; kb-cross-check lineage"
  - not_created: [bcm-mailbox-dma]
```

## Ziel

Fremd-Repos zu Pi-Software-TX in die KB: UKW-FM-Linie (pifm → markondej → Wrapper) und **rpitx** Multi-Mode — Match gegen Empfangs-Sheets, Recht/Filter/Pi-Modell als Fallstricke, Kontrast PiDrive.

**Revalidation 2026-10-11:** denselben Materialstand unter Audit-Standard **0.6.6** erneut prüfen (Chip-Scope, Signalpfad, Gate vor Varianten-Sheet, Kontrast zu `esp-fm-tx`). Historischer 0.6.3-Befund bleibt in Git + [DELTA](DELTA.md) nachvollziehbar — nicht überschrieben ohne Spur.

## Scope

[SCOPE](../../projects/pi-fm-tx/SCOPE.md) — Desk only; **keine** Antennen-Feldversuche. Revalidation = gleiche sechs Commits, keine neuen Upstreams.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard_version 0.6.3 + lab-tool (Original) | erfüllt (2026-10-10) |
| 2 | Reuse: RX-Sheets nicht missbraucht; Forks ohne Sheet-Explosion | erfüllt |
| 3 | Sheets `rpi-gpio-fm-tx`, `fm-rds`, `rpitx` + Apps | erfüllt |
| 4 | Evidence für alle sechs Repos | erfüllt |
| 5 | `ta-assist check` 0 errors | erfüllt (lokal) |
| 6 | Geschirmter Lab-Loopback gemessen | offen (bewusst) |
| 7 | Revalidation 0.6.6: Chip-Scope + Signalpfad + RP1-Gate + DELTA | erfüllt (2026-10-11) |
| 8 | Kein Pi5/RP1-Sheet ohne `hw-path-gate` E-0/E-1 | erfüllt (Gate in FOLLOW-ON) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Hardware-Path Gate | [`hw-path-gate`](../../methods/hw-path-gate.md) |
| KB Cross-Check (Lineage) | [`kb-cross-check`](../../methods/kb-cross-check.md) — Auslöser 0.6.6 / `esp-fm-tx` |

## Lessons (Revalidation)

- 0.6.3 hatte Pi5 bereits als `UNKNOWN` — 0.6.6 macht daraus ein **benanntes Gate** (G19), nicht ein Sheet.
- Formale Signalpfad-Kette und Chip-Scope machen denselben Desk-Befund für Blindtests brauchbarer (G17).
- `bcm-mailbox-dma` bleibt observed: Mailbox/DMA ist Implementierungsdetail der FM-Linie, kein eigener Contract ohne Mehrwert.

## Bezug

[INVENTORY](../../projects/pi-fm-tx/INVENTORY.md) · [evidence](evidence.md) · **[DELTA](DELTA.md)** · Empfang [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/) · Kontrast [`esp-fm-tx-2026-foreign`](../esp-fm-tx-2026-foreign/)
