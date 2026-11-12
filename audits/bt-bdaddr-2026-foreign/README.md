# Audit Campaign: bt-bdaddr-2026-foreign

```yaml
id: bt-bdaddr-2026-foreign
project_id: bt-bdaddr-refs
started: 2026-11-12
ended: 2026-11-12
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "bdaddr@53dae3f"
upstream_pins:
  bdaddr: "53dae3f"
reuse_outcomes:
  reused: []
  new:
    - technologies/bt-bdaddr-rewrite
  not_helped:
    - "bdaddr als ESP32 MAC-Tool"
  process: "Minimal desk; related to BlueZ relay MAC-clone gap; no attack how-to."
  decisions_touched:
    - fact-vendor-hci-write-bdaddr
    - reject-bdaddr-for-espressif
    - inference-link-key-invalidate
    - unknown-hu-reaction
```

## Ziel

Minimal Knowledge Pack: **Vendor-HCI BD_ADDR rewrite** Capability-Matrix und ESP-Abgrenzung. Ergänzt Pack A (BluetoothInterceptor DESIGN: MAC clone out-of-scope).

## Scope

[SCOPE](../../projects/bt-bdaddr-refs/SCOPE.md). Related: [`ble-gatt-bluez-relay-2026-foreign`](../ble-gatt-bluez-relay-2026-foreign/).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + pin bdaddr | erfüllt |
| 2 | Sheet + Application + Evidence | erfüllt |
| 3 | Espressif-Lücke dokumentiert | erfüllt |
| 4 | C10–C13 | erfüllt |
| 5 | Kein Attack-How-to | erfüllt |

## Decision Trace (C10)

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Eigenes Sheet? | Fehlt Capability-Taxonomie? | 001–003 | Ja `bt-bdaddr-rewrite` | DISCOVERED |
| In BlueZ-Relay-Pack falten? | Scope? | Pack A Non-Ziele | Separates Mini-Projekt | KNOWN BEFORE |
| Link-Key Invalidate als FACT? | Tool-Beweis? | 004 | `INFERENCE` | DISCOVERED |
| HU-Reaktion claimen? | Messung? | 005 | `UNKNOWN` | DISCOVERED |

## Engineering Review Checks (C11)

| Evidence | Check |
|----------|-------|
| 001 | Vendor-Opcodes nicht als universelles HCI darstellen |
| 002–003 | ESP-Pfade nicht mit Host-`bdaddr` vermischen |
| 004–005 | INFERENCE/UNKNOWN nicht zu FACT hochstufen |
| KB | Keine Spoofing-Schritte |

## Kill-Kriterien (C12)

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk Capability-Karte; Lab HU-Reaktion bleibt offen, kein Kill.
```

## Knowledge Feedback (C13)

Desk only — `field_evidence: R0`. Kein MEASURED.

## Lessons → Transfer

- BD_ADDR Rewrite = Vendor-Matrix, nicht ein Command.
- ESP ≠ `bdaddr`; IDF MAC/Controller APIs.
- BlueZ GATT-Clone mit Bonding braucht Adress-Strategie separat — Tooling oft out-of-scope.

## Bezug

[INVENTORY](../../projects/bt-bdaddr-refs/INVENTORY.md) · [evidence](evidence.md) · [`bt-bdaddr-rewrite`](../../technologies/bt-bdaddr-rewrite/SHEET.md)
