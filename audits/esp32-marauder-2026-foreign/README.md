# Audit Campaign: esp32-marauder-2026-foreign

```yaml
id: esp32-marauder-2026-foreign
project_id: esp32-marauder
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "9386f3c0348c171eb58ef2e1ce1f0c2f555ba30c"
reuse_outcomes:
  reused: [rf-environment-monitor, lan-device-inventory]
  new: [esp-wifi-promiscuous-pcap]
  not_helped: []
  process: "Desk foreign; Capture/PCAP A only; offensive TX existence-only; no attack recipes"
```

## Ziel

ESP32 Marauder als Fremd-Upstream für **Promiscuous-Sniff + PCAP-High-Rate-Pipeline** in die KB bringen; Offensive-Features nur als Inventar-Signale ohne How-to; Kontrast zu RF-Score-Monitoren.

## Scope

[SCOPE](../../projects/esp32-marauder/SCOPE.md) — Desk only; keine Angriffsrezepte; keine Evil-Portal-Inhalte.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | `standard_version` 0.7.1 + `lab-tool` + Commit-Pin | erfüllt |
| 2 | Sheet `esp-wifi-promiscuous-pcap` + App; Kontrast RF/LAN | erfüllt |
| 3 | Kein Offensive-TX-Sheet / keine Attack-Steps | erfüllt |
| 4 | Evidence inkl. Dual-Band vs. Dual-Core-Klarstellung | erfüllt |
| 5 | C10–C12; C13 n/a Desk | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 7 | Authorized Lab pps | offen (FOLLOW-ON) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neues Sniff-Sheet? | = `rf-environment-monitor`? | Sheet-Abgrenzung + `…-002` | Nein — neuer Slug Capture/PCAP | KNOWN BEFORE TEST |
| Deauth-Sheet? | Policy / A-Nutzen | `…-005` | Nein — existence only | KNOWN BEFORE TEST |
| „Dual-Core“ als FACT? | Pinned Worker im Code? | `…-004` | Nein — Double-Buffer/`portMUX`; Dual-Band separat | DISCOVERED DURING TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-MARAUDER-2026-10-25-002` | Sniff ≠ Hub-RF-Score still matchen | KNOWN BEFORE TEST |
| `EVID-MARAUDER-2026-10-25-003` | BUF/SNAP Budget vor „kein Drop“-Claim | KNOWN BEFORE TEST |
| `EVID-MARAUDER-2026-10-25-004` | Dual-Band ≠ Dual-Core-Worker; Chip-Gate C5 | DISCOVERED DURING TEST |
| `EVID-MARAUDER-2026-10-25-005` | Keine Attack-A aus Mode-Enums ableiten | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** Upstream liefert belastbare Promiscuous→PCAP-Pipeline auf ESP32-Familie.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Kein Promiscuous/PCAP-Pfad, nur STA-Scan | nicht eingetreten |
| 2 | KB würde Attack-How-to erfordern | Policy-Exit — nicht eingetreten (Capture-only A) |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Capture-Audit; eigene pps UNKNOWN ≠ STOP. Offensive Features bewusst ohne Sheet.
```

## Knowledge Feedback

Desk only — C13 n/a.

## Lessons → Transfer

- Community „dual-core + hohe Raten“ oft = Double-Buffer + WiFi-Callback-Concurrency und/oder **Dual-Band**, nicht zwingend pinned Worker (vgl. esp32-ai LLM).
- Sniff/PCAP und RF-Environment-Monitor getrennt halten (REUSE Scanner-Schicht).

## Bezug

[INVENTORY](../../projects/esp32-marauder/INVENTORY.md) · [evidence](evidence.md)
