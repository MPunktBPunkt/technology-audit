# Audit Campaign: ble-gatt-bridge-refs-2026-foreign

```yaml
id: ble-gatt-bridge-refs-2026-foreign
project_id: ble-gatt-bridge-refs
started: 2026-10-28
ended: 2026-10-28
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "multi-2026-10-28"
upstream_pins:
  ChimeraBLE: "2330423"
  iFitnessProxy: "1c24f58"
  ifit: "d29ca88"
  esp32-ble2mqtt: "e66ec5a"
  BleRemoteBrideg: "958da7c"
  esp32-ble-uart-mx: "3451904"
  btlejuice: "981b2e3"
reuse_outcomes:
  reused:
    - ble-hr-relay
    - bluetooth-ftms
    - ble-http-gatt-probe
  new:
    - ble-gatt-dual-role
    - ble-gatt-transparent-bridge
    - ble-gatt-semantic-bridge
  not_helped:
    - "esp32-ble2mqtt als BLE↔BLE Dual-Role-Vorbild (Central-only↔MQTT)"
    - "generisches ble-relay ohne Profil/Interaktionsmodell"
  process: "Desk multi-repo; Offensive MITM nur Inventar; Pattern-Sheets schließen Taxonomie-Lücken."
  decisions_touched:
    - fact-three-bridge-patterns
    - reject-generic-ble-relay-sheet
    - reject-cccd-auto-sync
    - fact-control-point-semantic
    - reject-two-hci-equals-on-chip-dual-role
```

## Ziel

Knowledge Extraction: Dual-Role, Transparent vs Semantic GATT-Bridge, CCCD-Modellierung, Control-Point-Routing, Failure Modes — für Folgeprojekte. **Nicht** weiteres HR-Relay.

## Scope

[SCOPE](../../projects/ble-gatt-bridge-refs/SCOPE.md) — Desk; keine Attack-How-tos.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + multi-pin | erfüllt |
| 2 | Inventory aller 7 Repos (Roles/Patterns/CCCD/Failures) | erfüllt |
| 3 | Sheets Dual-Role / Transparent / Semantic + Cross-Refs HR/FTMS | erfüllt |
| 4 | Evidence mit Code-Links | erfüllt |
| 5 | Reuse-Empfehlung heartrate/ergo/ftmsprobe | erfüllt |
| 6 | C10–C12 | erfüllt |
| 7 | `ta-assist check` 0 errors | erfüllt |
| 8 | Lab Dual-Role Classic / CPS-Sheet | FOLLOW-ON (kein Kampagnen-Exit) |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Drei Pattern-Sheets statt `ble-relay` | Steuert Profil die Sheet-Wahl? | Matrix | Dual / Transparent / Semantic | KNOWN BEFORE / bestätigt |
| CCCD Source≠Dest als Default | Sync in Fremdcode? | `…-002` `…-010` | `REJECTED` Auto-Sync | DISCOVERED |
| ble2mqtt = Transparent-Verwandt, nicht Dual-Role | GATTS disabled? | `…-030` | Kontrast Central-Gateway | DISCOVERED |
| Control-Point → Semantic + FTMS wachsen | Eigenes CP-Sheet? | `…-021` | kein `ble-control-point-proxy` jetzt | DISCOVERED |
| Chimera/btlejuice nur Architektur | Attack-How-to? | SCOPE | Inventar, kein How-to | KNOWN BEFORE |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-002` | Downstream-CCCD nicht still Upstream mitschreiben annehmen |
| `…-011` | FTMS→CPS: Flags/synthetische Felder dokumentieren |
| `…-021` | CP Success ≠ Wirkung; Indicate-Pfad planen |
| `…-001`/`…-060` | Zwei-HCI ≠ Ein-Chip-Dual-Role Budget |
| `…-040` | Explizite FSM Discovery→Subscribe→Reconnect bevorzugen |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Nur Feature-Listen ohne Mechanismen | nicht eingetreten |
| 2 | Taxonomie = ein Sheet „Relay“ ohne Interaktionsmodell | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk schließt Pattern-Taxonomie; Classic-Lab und CPS-Produktpfad bleiben FOLLOW-ON, kein STOP.
```

## Taxonomie-Mapping (Kurz)

| Achse | Bestehend | Neu / Wachstum |
|-------|-----------|----------------|
| Roles | Chip-Scope in HR/FTMS | **`ble-gatt-dual-role`** |
| Bridge | `ble-hr-relay` Fanout | **`transparent`** / **`semantic`** |
| GATT Probe | `ble-http-gatt-probe` | reused Kontrast |
| Standard Profiles | `ble-hrm-gatt`, `bluetooth-ftms` | CPS **candidate** |
| Failure Modes | teilweise in HR/FTMS | in Dual-Role + Transparent Sheets |

### Bridge-Pattern × Repo

| Pattern | Chimera | iFitness | ifit | ble2mqtt | BleRemote | uart-mx | btlejuice |
|---------|---------|----------|------|----------|-----------|---------|-----------|
| Dual-Role on-chip | Y | Y | Host OS | N | Y | Y | N (2 HCI) |
| Notify Fan-Out same profile | Y* | N | Y* interceptor | MQTT | N | N | Y |
| Transparent Passthrough | Y | N | partial | Y↔MQTT | N | Y FFE0 | Y |
| Semantic A→B | N | FTMS→CPS | Custom→FTMS | typed MQTT | HID→HID | N | N |
| Control-Point Proxy | generic write | N | FTMS CP | generic | HOGP CP | N | N |
| Exclusive Control | N | N | partial | Owner MQTT | de-facto bond | N | N |

\*Fan-Out hier = Multi-Subscriber / Proxy, nicht HR-Service-Fanout.

## Reuse → eigene Projekte

| Projekt | Übernehmen | Nicht still übernehmen |
|---------|------------|------------------------|
| **esp32-heartrate** | Dual-Role-Checkliste; CCCD Source≠Dest; Adv-Restart schon da; FSM-Idee von BleRemote | Transparent Clone; MITM |
| **esp32-ergo** | Semantic Bridge Sheet als Dach über FTMS-Bridge; Exclusive/Observer gegen ifit CP; Poll-vs-Notify | FTMS→CPS Watch-Proxy ohne Bedarf |
| **esp32-ftmsprobe** | Capability-Probe bleibt; Semantic-Mapping-Felder für IBD Flags | Dual-Role Peripheral Pflicht |

## Lessons → Transfer

- Sheet-Wahl: **Profil + Interaktionsmodell + Dual-Role**, nicht „Bluetooth-Relay“.
- CCCD-Upstream und Downstream sind getrennte Zustandsmaschinen, bis Evidence Sync zeigt.
- Semantic Bridges brauchen Feld-Tabellen; Transparent Bridges brauchen Mapping/Handle-Disziplin.
- Offensive Clone-Repos liefern Architektur-Evidence, keine Implementierungsvorlage für Produkte.

## Bezug

[INVENTORY](../../projects/ble-gatt-bridge-refs/INVENTORY.md) · [evidence](evidence.md) · Sheets: [`ble-gatt-dual-role`](../../technologies/ble-gatt-dual-role/SHEET.md) · [`ble-gatt-transparent-bridge`](../../technologies/ble-gatt-transparent-bridge/SHEET.md) · [`ble-gatt-semantic-bridge`](../../technologies/ble-gatt-semantic-bridge/SHEET.md) · [`ble-hr-relay`](../../technologies/ble-hr-relay/SHEET.md) · [`bluetooth-ftms`](../../technologies/bluetooth-ftms/SHEET.md)
