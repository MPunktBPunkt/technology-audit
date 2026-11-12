# Audit Campaign: ble-gatt-bluez-relay-2026-foreign

```yaml
id: ble-gatt-bluez-relay-2026-foreign
project_id: ble-gatt-bluez-relay-refs
started: 2026-11-12
ended: 2026-11-12
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "BluetoothInterceptor@4a10bcf bluez_peripheral@8174c15"
upstream_pins:
  BluetoothInterceptor: "4a10bcf"
  bluez_peripheral: "8174c15"
reuse_outcomes:
  reused:
    - ble-gatt-transparent-bridge
    - ble-gatt-dual-role
    - ble-gatt-observe-proxy
  new: []
  not_helped:
    - "bluez_peripheral als volles BLE↔BLE Dual-Role-Relay (Peripheral-only API)"
    - "neues Sheet bluez-gatt-peripheral (reuse Transparent/Dual-Role)"
  process: "Desk delta nach ble-gatt-bridge-refs; Offensive Clone nur Architektur; ifit CROSSREF only."
  decisions_touched:
    - reinforce-reject-two-hci-equals-on-chip-dual-role
    - fact-bluez-bluer-two-adapter-clone
    - fact-cccd-local-bluez-stack
    - reject-new-bluez-peripheral-sheet
```

## Ziel

Knowledge Extraction: **BlueZ/bluer two-adapter GATT relay** (BluetoothInterceptor) + Peripheral building block (bluez_peripheral). Grow bestehende Pattern-Sheets. **Nicht** Attack-How-to; **nicht** Re-Audit von ifit/btlejuice.

## Scope

[SCOPE](../../projects/ble-gatt-bluez-relay-refs/SCOPE.md) — Desk; keine Attack-How-tos.

**Prior:** [`ble-gatt-bridge-refs-2026-foreign`](../ble-gatt-bridge-refs-2026-foreign/) · **Related Pack B:** [`bt-bdaddr-2026-foreign`](../bt-bdaddr-2026-foreign/) (MAC clone out-of-scope hier).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + dual pin | erfüllt |
| 2 | Inventory Interceptor + bluez_peripheral | erfüllt |
| 3 | Sheets Transparent + Dual-Role gewachsen; observe-proxy Cross-Ref | erfüllt |
| 4 | Evidence `EVID-BZGATT-2026-11-12-*` mit Code-Links | erfüllt |
| 5 | ifit nur CROSSREF | erfüllt |
| 6 | C10–C13 | erfüllt |
| 7 | Kein neues Attack-How-to | erfüllt |

## Decision Trace (C10)

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Sheet `bluez-gatt-peripheral`? | Fehlt API-Taxonomie? | 010 | Nein — Building Block → Transparent/Dual reuse | DISCOVERED |
| Zwei-HCI = on-chip Dual-Role? | Budget/Failure Modes gleich? | 005/006 + Prior 060 | `REJECTED` verstärkt | DISCOVERED |
| CCCD 1:1 klonen? | Default Interceptor? | 003 | Local stack; descriptors opt-in | DISCOVERED |
| ifit neu auditieren? | Schon in bridge-refs? | Prior 021–023 | CROSSREF only | KNOWN BEFORE |
| EventBus → observe-proxy Sheet? | Analyse-Logging? | 007 | Cross-Ref, kein neues Sheet | DISCOVERED |

## Engineering Review Checks (C11)

| Evidence | Check |
|----------|-------|
| 001–002 | Forward-Pfade nur als Architektur zitieren; kein MITM-Rezept |
| 003 | CCCD Source≠Dest / local BlueZ nicht als Auto-Sync lesen |
| 005–006 | ESP Dual-Role-Budget nicht aus Two-HCI ableiten |
| 010 | bluez_peripheral nicht als Relay-Vorbild markieren |
| CROSSREF ifit | Keine doppelten Evidence-IDs |

## Kill-Kriterien (C12)

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Attack-How-to in KB geschrieben | `REJECTED` |
| 2 | Taxonomie = neues Sheet ohne Interaktionsmodell | `REJECTED` (reuse) |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Delta schließt BlueZ/bluer-Lücke; Single-Adapter Concurrent bleibt FOLLOW-ON Lab.
```

## Knowledge Feedback (C13)

Desk only — kein neuer MEASURED-Claim. Sheets: `field_evidence` unverändert R0 (eigene Lab). Applications: Desk-Pin-Verifikation R3.

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.

## Lessons → Transfer

- BlueZ/bluer Two-Adapter-Clone ist das moderne Pendant zu btlejuice — gleiche Achse, andere API.
- Concurrent Central+Peripheral auf **einem** HCI ist controller-dependent; Tooling warnt und empfiehlt zwei Adapter.
- CCCD bleibt lokal am Peripheral-Stack; Upstream-Subscribe lazy bei Downstream-Notify (Source≠Dest).
- Python `bluez_peripheral` eignet sich als Peripheral-Baustein, nicht als Relay-Architektur.
- MAC-Address-Clone auf Clone-Adapter → separates `bt-bdaddr-rewrite` (Pack B).

## Bezug

[INVENTORY](../../projects/ble-gatt-bluez-relay-refs/INVENTORY.md) · [evidence](evidence.md) · Sheets: [`ble-gatt-transparent-bridge`](../../technologies/ble-gatt-transparent-bridge/SHEET.md) · [`ble-gatt-dual-role`](../../technologies/ble-gatt-dual-role/SHEET.md) · [`ble-gatt-observe-proxy`](../../technologies/ble-gatt-observe-proxy/SHEET.md)
