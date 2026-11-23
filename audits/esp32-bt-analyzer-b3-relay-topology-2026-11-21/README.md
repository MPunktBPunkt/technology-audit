# Audit: B3 Profile-Relay Topology & Capture Discipline

```yaml
id: esp32-bt-analyzer-b3-relay-topology-2026-11-21
project_id: esp32-bt-analyzer
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits: [esp32-bt-analyzer-f20-connected-2026-11-17, bmw-av-session-control-vs-audio-2026-11-21]
reuse_outcomes:
  reused: [projects/esp32-bt-analyzer, technologies/esp-wifi-bt-coex, technologies/bluez-pairing-agent]
  new: []
  not_helped: []
  process: "Freeze B3 relay topology + operator discipline + dual-plane protocol into project STATUS/apps."
```

## Ziel

B3 Profile-Relay-Architektur (Phone ↔ .131 ↔ Relay ↔ .87 ↔ F20), Capture-Discipline und Dual-Plane-Protokoll als wiederverwendbaren Projekt-Transfer dokumentieren.

## Scope

- Im Scope: Topologie; Operator-Runbook; coex/wifi_ps/btmon; freeze-on-AUTH; Bridge-Envelope-Artefakte; Dual-Plane-Definition.
- Nicht im Scope: FW-Refactor; Audio-Transport-Implementierung.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Topologie + MACs im Projektstatus | erfüllt |
| 2 | Capture-Discipline Checkliste | erfüllt |
| 3 | Dual-Plane als nächster Feldstandard | erfüllt |

## Topology (FIELD FACT)

```text
OnePlus / MyBMW+AAIdrive
    → BMW 38304 C8:C9:A3:CB:7B:0A  (.131 / hci2)  RFCOMM ch6
    ↔ b3_profile_relay / b3_rfcomm_relay
    ↔ BT-Analyzer-Phone C8:C9:A3:CB:37:96  (.87 / hci1)
    → F20 D4:36:39:CF:E1:B5  RFCOMM ch6
```

Quellen: `OPERATOR.md`, `EVAL.md`.

## Capture Discipline

| Maßnahme | Status |
|----------|--------|
| `wifi_ps=none`, `coex=prefer_bt` beide ESP | **FIELD** (OPERATOR) |
| USB hci0 powered off | **FIELD** |
| btmon auf hci1 + hci2 | **FIELD** Artefakte `btmon/*.btsnoop` |
| F20 bonded on .87; Connected=false until car connects | **FIELD** |
| Freeze on AUTHENTICATED / Reject (kein AM/RHMI weiter) | **FIELD** Runbook; B3 live lief durch zu Music |
| Raw bins + jsonl + SDP control | **FIELD** MANIFEST |

## Bridge vs Wire (epistemic)

| Artefakt | Klassifikation |
|----------|----------------|
| 56-B UUID Envelope vor BCL | Bridge (STRONG) — nicht BT-Wire |
| Isolierte `13371337` außerhalb WD | Bridge keepalive (STRONG) |
| Concatenated multi-INIT in phone_to_hu.bin | Capture/Session-Concat **FACT** |

## Dual-Plane (next — locked from AV audit)

Jeder Music/PLAY-Lauf: BCL/Etch **und** Audio-Kandidatenebene (oder explizite Absenz) mit gemeinsamer Monotonie-Uhr.

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Repro-Topologie für Gate B? | Braucht Profile-Relay? | B3 CLOSED nur via Relay | Ja — Standard für Live-APP_AUTH Capture |
| jsonl allein genug? | Cert decode? | Gap | Nein — immer Raw mitschreiben |

## Kill-Kriterien

```text
NO JUSTIFIED KILL CRITERION
Begründung: Topologie-/Disziplin-Audit ohne falsifizierbare Protokollhypothese;
Falsifikation läge in AV/SAS-Audits (Accept ausbleibt / Planes fehlen).
```

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-RELAY-TOPO` | `projects/esp32-bt-analyzer/STATUS.md` |
| `EVID-B3-CAPTURE-DISCIPLINE` | same + FOLLOW-ON |
| `EVID-B3-DUAL-PLANE-PROTOCOL` | STATUS + `bmw-av` + method |

## Offene Punkte

- Relay-Tool Quellcode-Pin vs Bridge-Envelope
- Automatisches Dual-Plane-Logging im Lab-Harness
