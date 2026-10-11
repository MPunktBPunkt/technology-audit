# AUDIT DELTA — esp32-ergo-2026-pilot

```yaml
campaign: esp32-ergo-2026-pilot
old_standard: "0.6.0"
new_standard: "0.6.6"
revalidated: 2026-10-11
method: desk revalidation (same commit edaeb19) + 0.6.1–0.6.6 process rules
siblings: [esp32-heartrate, esp32-ftmsprobe]
```

## OLD AUDIT (0.6.0)

| Bereich | Stand |
|---------|--------|
| Claims | FTMS + Varon Host; HR/Web/Hub-Reuse von heartrate; Bridge/Coach-Kontext |
| UNKNOWNs | MyWhoosh Bridge-PASS; Nachtest 6; SIM-Passthrough |
| Sheets | neu `bluetooth-ftms`, `hammer-varon-xtr`; Wachstum shared Slugs |
| Process gaps | nur 0.6.1 in `standard_gaps`; Produkt-Chip-Scope (S3-only) nicht als G17 am Bridge-Pfad |

## NEW AUDIT (0.6.6 Revalidation)

| Bereich | Delta |
|---------|--------|
| neue FACTs | Produkt-Chip-Scope = **ESP32-S3** (`env:ergo`); FTMS Dual-Role Bridge+Central auf S3 |
| geschärft | HR-Relay = Deployment-Consumer von heartrate-S3, kein Code-Transfer; Varon bleibt Host-Sheet |
| Gates | `ftms-erg-control` bleibt observed (G19); Classic-ESP32-Ergo nicht behauptet |
| Reuse | Geschwister-Wachstum formal bestätigt; Method aus ftmsprobe bleibt Lab-SoT für Caps |
| verworfene Transfers | Varon → alle Indoor-Bikes; Control-Success → Wirkung; S3-Bridge → Classic |

## Quantitativ

| Metrik | 0.6.0 | nach 0.6.6 | Δ |
|--------|-------|------------|---|
| Active Sheets (Pilot-neu) | 2 | 2 | 0 |
| Evidence-IDs | 11 | 14 | +3 Scope/Reuse |
| `standard_gaps` | [0.6.1…] | keine | Parität |

## Urteil

Ergo ist der **Geschwister-/Wachstums-Kontrollfall**: 0.6.6 ändert wenig an den Spec-FACTs, formalisiert aber S3-Produkt-Scope und die Grenze „Relay = anderer Node“. Zusammen mit heartrate/ftmsprobe ergibt sich eine konsistente Familien-Chip-Story.

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Kampagne | [README.md](README.md) |
| Sheets | [`bluetooth-ftms`](../../technologies/bluetooth-ftms/SHEET.md), [`hammer-varon-xtr`](../../technologies/hammer-varon-xtr/SHEET.md) |
| Relay-Consumer | [applications/ble-hr-relay.md](../../projects/esp32-ergo/applications/ble-hr-relay.md) |
