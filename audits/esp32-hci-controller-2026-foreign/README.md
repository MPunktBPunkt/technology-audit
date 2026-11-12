# Audit Campaign: esp32-hci-controller-2026-foreign

```yaml
id: esp32-hci-controller-2026-foreign
project_id: esp32-hci-controller-refs
started: 2026-11-12
ended: 2026-11-12
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "multi-2026-11-12"
upstream_pins:
  uart_hci_bluetooth_module_esp32: "ef5d792"
  ESP32-Bluetooth-USB-dongle: "4ebcbc1"
  esp-idf_controller_hci_uart: "827cc62"
  zephyr_hci_uart_docs: "docs-latest"
reuse_outcomes:
  reused:
    - bt-dual-mode-coex
    - bt-usb-hci-observe-baseline
    - bt-passive-host-sniff
  new:
    - esp-hci-uart-controller
    - bt-hci-host-attach
  not_helped:
    - "HCI-over-TCP /dev/vhci als Drop-in für UART-Dongle"
    - "Analyzer WiFi ACL kB/s als UART-HCI-Throughput"
  process: "Desk multi-repo; Controller-Transport Pattern (primary D); Host-Attach Method; Kontrast eigener TCP-Bridge."
  decisions_touched:
    - fact-uart-h4-controller-pattern
    - fact-vs-hci-off-third-party
    - reject-tcp-kbps-as-uart-evidence
    - fact-sco-path-hci-config
    - infer-uart-escapes-wifi-coex
```

## Ziel

Fremd-Desk: ESP32 als **Bluetooth HCI-Controller** für Linux/BlueZ — UART H4 / USB-UART, Attach-Prozedur, SCO/VS-HCI-Fallstricke; klarer Kontrast zum eigenen HCI-over-TCP + VHCI Analyzer.

## Scope

[SCOPE](../../projects/esp32-hci-controller-refs/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + upstream pins | erfüllt |
| 2 | Inventory Match Signal→Sheet + Repos | erfüllt |
| 3 | Sheet `esp-hci-uart-controller` (primary D) | erfüllt |
| 4 | Method `bt-hci-host-attach` | erfüllt |
| 5 | Kontrast Analyzer TCP/VHCI dokumentiert | erfüllt |
| 6 | C10–C13 | erfüllt |
| 7 | Keine erfundenen UART-Throughput-MEASURED | erfüllt |
| 8 | Lab Attach Smoke | FOLLOW-ON |

## Decision Trace (C10)

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Sheet primary D | HCI-Transport Embedded-Muster? | `…-001`/`…-020` | `esp-hci-uart-controller` | DISCOVERED |
| Method statt Sheet für Attach | Prozedur wiederholbar? | `…-002`/`…-011`/`…-030` | `bt-hci-host-attach` | DISCOVERED |
| VS HCI OFF Pflicht | Third-Party BlueZ? | `…-020` | Fallstrick FACT | DISCOVERED |
| Analyzer kB/s nicht übernehmen | Gleicher Transport? | `…-040` + analyzer STATUS | `REJECTED` Transfer | KNOWN BEFORE |
| SCO → eigener Config-Gate | Audio über Host? | `…-003`/`…-011` | SCO_PATH / MTU Gate | DISCOVERED |
| UART = Escape WiFi-Coex | vs HCI_TCP? | `…-040` | `INFERENCE` Transfer | DISCOVERED |

## Engineering Review Checks (C11)

| Evidence | Check |
|----------|-------|
| `…-001`/`…-020` | Pins/Baud/HWFC nur mit Pin zitieren; Zephyr 1 M ≠ ESP 921600 |
| `…-002`/`…-011` | `btattach -P h4` vs `hciattach … noflow` nicht still gleichsetzen |
| `…-003` | SCO Host-Pfad nur mit `SCO_DATA_PATH_HCI` (o. ä.) |
| `…-020` | VS HCI OFF vor BlueZ-Claims |
| `…-040` | Keine Analyzer-WiFi-kB/s als UART-Evidence |
| Reset | dakhnod Tangle als `UNKNOWN` bis Lab — kein „immer so“ |

## Kill-Kriterien (C12)

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | UART-Repos mit Analyzer-TCP-Throughput verkauft | `REJECTED` |
| 2 | Generisches „ESP Bluetooth“ Sheet ohne Host/Controller-Split | `REJECTED` |
| 3 | Attack-/Inject-How-tos in Sheet/Method | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk schließt Controller-Transport-Muster und Attach-Method;
Lab-Throughput und Reset-Stabilität bleiben FOLLOW-ON, kein STOP.
```

## Knowledge Feedback (C13)

Desk only — kein neuer MEASURED-Claim an UART/USB-UART.
Sheet + Application: `field_evidence: R0`, `implementation: R0`;
`technology: R2` / `reusability: W2` = Desk-Pin-Verifikation über multi-repo Convergence, nicht Feld.

Analyzer ACL/WiFi-Zahlen bleiben in [`esp32-bt-analyzer/STATUS`](../../projects/esp32-bt-analyzer/STATUS.md); hier nur Cross-Ref + `REJECTED` Transfer.

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.

## Empfehlung kurz

| Bedarf | Tooling |
|--------|---------|
| Günstiger Dual-Mode Adapter an BlueZ | ESP32 Controller-FW (IDF/redchenjs) + `btattach -P h4` |
| USB-Stick-Formfaktor | dakhnod USB-UART + Flow/Reset-Gate |
| Instrument mit WiFi JSONL/TCP | eigener `esp32-bt-analyzer` — **anderer** Transport |
| Architektur Host/Controller | Zephyr hci_uart Docs |

**Regel:** UART/USB-UART für Host-Attach; TCP/VHCI nur wo der Analyzer-Vertrag gilt — Zahlen nicht mischen.

## Lessons → Transfer

- ESP32 „Bluetooth“ kann **nur Controller** bedeuten — Host auf Linux.
- Default-Pinmap 5/18/19/23 @ 921600+HWFC ist Desk-FACT (multi-source); Baud aus Zephyr-Docs nicht blind übernehmen.
- VS HCI und SCO-Pfad sind Config-Gates, keine Nebensache.
- HCI-over-TCP bleibt selten/eigen; UART ist der Community-Standard-Escape aus WiFi-Coex.

## Bezug

[INVENTORY](../../projects/esp32-hci-controller-refs/INVENTORY.md) · [evidence](evidence.md) · [sheet](../../technologies/esp-hci-uart-controller/SHEET.md) · [method](../../methods/bt-hci-host-attach.md) · Kontrast: [`esp32-bt-analyzer`](../../projects/esp32-bt-analyzer/) · Prior BT: [`bt-analysis-relay-2026-foreign`](../bt-analysis-relay-2026-foreign/) · [`bluetooth-stack-2026-foreign`](../bluetooth-stack-2026-foreign/)
