# AUDIT DELTA — pi-fm-tx-2026-foreign

```yaml
campaign: pi-fm-tx-2026-foreign
old_standard: "0.6.3"
new_standard: "0.6.6"
revalidated: 2026-10-11
method: desk revalidation (same six repos / same commits) + 0.6.6 process rules
reference_audit: esp-fm-tx-2026-foreign
```

Vergleich **derselben** Fremdquellen unter dem neuen Regelstand. Keine neuen Upstream-Commits; kein Lab.

## OLD AUDIT (0.6.3)

| Bereich | Stand |
|---------|--------|
| Claims | UKW-FM-Linie + rpitx + RDS + Fork/Wrapper-Abgrenzung; Legal/Filter/Pi-Modell als Fallstricke |
| UNKNOWNs | Harmonic-Pegel; Pi5-Nachfolger-Pfad |
| HYPOTHESIS | rpitx Easytest 434 MHz „frei nutzbar“ (lokal prüfen) |
| Sheets | `rpi-gpio-fm-tx`, `fm-rds`, `rpitx` |
| Evidence | 21 IDs (PIFM/RDS/FMTX/RPITX/MATCH) |
| Reuse | RX≠TX; Forks ohne Sheet-Explosion; Kontrast PiDrive |
| Process gaps vs 0.6.6 | kein formales Chip-Scope; keine Signalpfad-Kette; kein benanntes Gate vor RP1-Variante; kein KB-Cross-Check-Artefakt; G17–G19 fehlten |

## NEW AUDIT (0.6.6 Revalidation)

| Bereich | Delta |
|---------|--------|
| neue FACTs | Chip-Scope BCM283x/BCM2711 vs RP1 formalisiert; Signalpfad-Stufen belegt wo Code/Docs reichen; symmetrischer Kontrast zu `esp32-apll-fm-tx` |
| herabgestufte / geschärfte Claims | „Pi Software-TX“ ohne SoC-Variante unvollständig (G17); rpitx Bandbreite/GPIO4 gelten für belegte Pi-Matrix, **nicht** still für Pi5; Pi4≠Pi5 Transfer = `UNKNOWN`/Gate |
| neue UNKNOWNs | RP1 Clock→Pad-Kette (E-0); rpitx Modes auf Pi5/RP1 |
| neue Gates | `hw-path-gate` E-0/E-1 für Pi5/RP1 — **kein** neues Sheet vor Evidence (G19) |
| verworfene Transfers | BCM-GPCLK-Evidence ↛ RP1; ESP-APLL-Evidence ↛ Pi; Pi-DMA-Exit ↛ ESP als FACT (bleibt Prüfpunkt) |
| Cross-Project-Reuse | Bidirektional mit `esp-fm-tx` / Sheet `esp32-apll-fm-tx`; Method `kb-cross-check` als Herkunft von 0.6.6 anerkannt |
| bewusst nicht angelegt | Sheet `bcm-mailbox-dma` (observed) — G19: kein Sheet nur aus Architekturidee |

## Quantitativ (Desk)

| Metrik | 0.6.3 | nach 0.6.6 | Δ |
|--------|-------|------------|---|
| Active Sheets | 3 | 3 | 0 (kein Varianten-Sheet) |
| Evidence-IDs | 21 | 24 | +3 Prozess-/Scope-Belege |
| Offene Lab-UNKNOWNs | 2 | 3 | +1 (RP1-Pfad explizit) |
| Benannte Gates | 0 | 1 (Pi5/RP1) | +1 |
| Formale Signalpfad-Tabelle | 0 | 1 (`rpi-gpio-fm-tx`) | +1 |
| `standard_gaps` offen | n/a (Lag undokumentiert) | keine | Parität |

## Urteil

0.6.6 liefert hier **Prozessqualität**, nicht eine Flut neuer Spec-FACTs: dieselben Upstream-Commits werden schärfer scoped, Transfers gebremst, und die Pi5-Lücke wird vom offenen Punkt zum **Gate**. Das ist der erwartete Kontrollbefund gegenüber `esp-fm-tx` (dort Chip-Scope Classic≠S3).

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Kampagne | [README.md](README.md) |
| Evidence | [evidence.md](evidence.md) |
| Sheet (Signalpfad) | [`rpi-gpio-fm-tx`](../../technologies/rpi-gpio-fm-tx/SHEET.md) |
| FOLLOW-ON Gate | [FOLLOW-ON-IDEAS](../../projects/pi-fm-tx/FOLLOW-ON-IDEAS.md) |
| Methoden | [`hw-path-gate`](../../methods/hw-path-gate.md), [`kb-cross-check`](../../methods/kb-cross-check.md) |
