# AUDIT DELTA — welle-io-2026-foreign

```yaml
campaign: welle-io-2026-foreign
old_standard: "0.6.5"
new_standard: "0.6.6"
revalidated: 2026-10-11
method: desk revalidation (same commit 512558d) — control case 0.6.5→0.6.6
contrasts: [pidrive-2026-radio-bt, pi-fm-tx-2026-foreign, esp-fm-tx-2026-foreign]
```

## OLD AUDIT (0.6.5)

| Bereich | Stand |
|---------|--------|
| Claims | Gain-Index, Software-AGC, Kanalmap, `/spectrum`=T_u, Airspy HF+ ungeeignet; Reuse `dab-plus`/`rtl-sdr` |
| Sheets | kein neues Sheet — Wachstum bestehender Empfangs-Slugs |
| Process | bereits nahe current (0.6.5); Chip-/Input-Scope weniger formal als 0.6.6 |

## NEW AUDIT (0.6.6 Revalidation)

| Bereich | Delta |
|---------|--------|
| Input-Scope | RTL Gain-Index-Contract **nur** librtlsdr-Pfad; Soapy/Airspy/Lime ≠ still gleicher Gain-FACT |
| RX≠TX | expliziter Querverweis zu `rpi-gpio-fm-tx` / `esp32-apll-fm-tx` (nach radio-bt/pi-fm Parität) |
| Gates | Airspy/Soapy/Lime bleiben observed — kein Sheet aus Factory-Liste (G19) |
| Cross-Project | Bidirektional mit revalidiertem `pidrive-2026-radio-bt` |

## Quantitativ

| Metrik | 0.6.5 | nach 0.6.6 | Δ |
|--------|-------|------------|---|
| Active Sheets (neu) | 0 | 0 | 0 |
| Evidence-IDs | 12 | 14 | +2 Scope/Match |
| Spez-FACTs geändert | — | — | ~0 (Kontrollfall) |

## Urteil

Erwarteter **kleiner Kontroll-Delta**: 0.6.5 hatte die fachlichen Fallstricke schon. 0.6.6 formalisiert Input-/Tuner-Scope und die TX-Abgrenzung nach den späteren Transfer-Gates — ohne neue Desk-FACTs aus demselben Commit.

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Kampagne | [README.md](README.md) |
| Ops-Nachbar | [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/) |
| TX-Kontrast | [`pi-fm-tx`](../pi-fm-tx-2026-foreign/), [`esp-fm-tx`](../esp-fm-tx-2026-foreign/) |
