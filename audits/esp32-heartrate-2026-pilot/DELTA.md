# AUDIT DELTA — esp32-heartrate-2026-pilot

```yaml
campaign: esp32-heartrate-2026-pilot
old_standard: "0.6.0"
new_standard: "0.6.6"
revalidated: 2026-10-11
method: desk revalidation (same commit 72acae4) + 0.6.1–0.6.6 process rules
sibling_growth: [esp32-ergo, esp32-ftmsprobe]
```

Vergleich **desselben** Quellenstands unter dem neuen Regelstand. Kein neuer Upstream-Commit; keine neuen Lab-PASSes.

## OLD AUDIT (0.6.0)

| Bereich | Stand |
|---------|--------|
| Claims | HR-Central, HR-Relay (S3), Web/SSE, Hub-IO; Polar H9 Quirks |
| UNKNOWNs | Relay-Abnahme 1–15 Lab-PASS; Feld Radcomputer; Continuity-KPIs; live Hub |
| Sheets | `ble-hrm-gatt`, `ble-hr-relay`, `esp-embedded-web-sse`, `esp-hub-telemetry` |
| Evidence | 7 IDs |
| Reuse | Erstes ESP-Bootstrap; später Geschwister gewachsen (noch nicht in Gaps reflektiert) |
| Process gaps | nur `standard_gaps` → 0.6.1; fehlten u. a. Geschwister-Formalisierung, Schichtregeln, Chip-Scope G17–G19 |

## NEW AUDIT (0.6.6 Revalidation)

| Bereich | Delta |
|---------|--------|
| neue FACTs | Chip-Scope Relay = **ESP32-S3** (`heartrate-s3`); Classic Mini = Peripheral/Relay absichtlich off (`PERIPHERAL_DISABLED` / `relay.supported=false`) |
| herabgestufte / geschärfte Claims | „HR-Relay auf ESP32“ ohne SoC = unvollständiger FACT (G17); Connection-Budget Mini≠S3 |
| neue UNKNOWNs | Classic dual-role Relay tragfähig? → Gate / eigene Evidence — kein Sheet-Ausweiten |
| neue Gates | Dual-role / höheres `MAX_CONNECTIONS` auf Classic = Gate vor Claim-Transfer von S3 |
| verworfene Transfers | S3-Relay-Evidence ↛ Classic Mini; Hub/Web bleiben chip-neutral (A) |
| Cross-Project-Reuse | Geschwister `esp32-ergo` / `esp32-ftmsprobe` als Sheet-Wachstum bestätigt (W3); keine Forks |
| bewusst nicht angelegt | Sheets für `rr-quality-pipeline`, `littlefs-session-archive`, … (observed; G19) |

## Quantitativ (Desk)

| Metrik | 0.6.0 | nach 0.6.6 | Δ |
|--------|-------|------------|---|
| Active Pilot-Sheets | 4 | 4 | 0 |
| Evidence-IDs | 7 | 10 | +3 Scope/Reuse |
| Offene Lab-UNKNOWNs | 4 | 5 | +1 (Classic dual-role) |
| Formale Chip-Scope am Relay-Sheet | nein | ja | +1 |
| `standard_gaps` offen | [0.6.1…] | keine | Parität |

## Urteil

Stärkster 0.6.6-Hebel hier ist **G17 Chip-Scope am Dual-Role-Relay**, nicht RF-Signalpfad. Das Audit hatte die S3-Grenze in Application/SCOPE schon implizit — die Revalidation hebt sie auf Sheet-A und bremst stillen Transfer auf Classic. Zusätzlich schließt die Kampagne den Gap-Rückstand 0.6.1–0.6.5 (Geschwister/Schicht/Index) dokumentarisch.

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Kampagne | [README.md](README.md) |
| Evidence | [evidence.md](evidence.md) |
| Sheet (Chip-Scope) | [`ble-hr-relay`](../../technologies/ble-hr-relay/SHEET.md) |
| Geschwister | [`esp32-ergo`](../../projects/esp32-ergo/), [`esp32-ftmsprobe`](../../projects/esp32-ftmsprobe/) |
