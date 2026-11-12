# Audit Campaign: bmw-bcl-rfcomm-role-2026-desk

```yaml
id: bmw-bcl-rfcomm-role-2026-desk
project_id: bimmergestalt-idrive-refs
started: 2026-11-12
ended: 2026-11-12
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "BclCarLink@7cfd959"
upstream_pins:
  BclCarLink: "7cfd959"
reuse_outcomes:
  reused:
    - technologies/bmw-bcl
    - audits/bimmergestalt-idrive-2026-foreign
    - audits/bmw-connected-sas-auth-2026-11-06
    - projects/bimmergestalt-idrive-refs/applications/bmw-bcl.md
  new:
    - projects/bimmergestalt-idrive-refs/applications/bmw-bcl-rfcomm.md
  not_helped: []
  process: "Focused desk follow-up gap 4/5 RFCOMM roles only; no full BimmerGestalt re-audit; SAS/Etch CROSSREF only."
  decisions_touched:
    - fact-phone-rfcomm-client-spp-uuid
    - inference-hu-rfcomm-server
    - fact-watchdog-5001-ping-timeout
    - fact-a2dp-discovery-hint
```

## Ziel

Schließt Knowledge-Gap **RFCOMM-Rollen** (Phone = Client, HU = Server/SDP) für BCL über Bluetooth.
**Kein** Re-Audit von Framing, Handshake, Etch oder SAS.

## Scope

| Im Scope | Nicht im Scope |
|----------|----------------|
| `BtConnection` / `BtClientService` / `WatchdogProtocol` @ BclCarLink `7cfd959` | Gesamtes BimmerGestalt Ecosystem |
| SPP UUID, Client-Connect-Pattern, A2DP Hint, Watchdog Timing | SAS challenge/response (bereits desk-audited) |
| Sheet-Wachstum `bmw-bcl` Fallstrick/FACT | Neue Protocol-Implementierung / Attack |

**CROSSREF SAS/Etch:** [`bmw-connected-sas-auth-2026-11-06`](../bmw-connected-sas-auth-2026-11-06/) — nicht duplizieren.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + focused pin BclCarLink | erfüllt |
| 2 | RFCOMM Client/Server Claims mit Evidence | erfüllt |
| 3 | Watchdog Port/Ping/Timeout FACT | erfüllt |
| 4 | Application `bmw-bcl-rfcomm.md` + Sheet Update | erfüllt |
| 5 | SAS nur CROSSREF | erfüllt |
| 6 | C10–C13 | erfüllt |

## Decision Trace (C10)

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Eigenes Sheet `bmw-bcl-rfcomm`? | Neue Technology? | 001–005 | Nein — Application + Sheet-Wachstum | DISCOVERED |
| HU = RFCOMM Server FACT? | Code zeigt nur Client | 003 | `INFERENCE` aus Connect-Pattern | DISCOVERED |
| SAS hier vertiefen? | Gap 4/5? | Prior SAS audit | CROSSREF only | KNOWN BEFORE |
| SDP_BCL = BMW-spezifisch? | UUID-Wert | 002 | `REJECTED` — generic SPP | DISCOVERED |

## Engineering Review Checks (C11)

| Evidence | Check |
|----------|-------|
| 001–003 | Client-API nicht als Server-Implementierung zitieren; HU-Server = INFERENCE markieren |
| 002 | SPP UUID nicht als OEM-proprietär claimen |
| 004 | Watchdog Bytes nur als Client-Ping; HU-Pong-Semantik nicht überinterpretieren |
| 005 | A2DP = Discovery-Hint, nicht BCL-Transport |
| SAS CROSSREF | Keine Secrets / Bypass-Schritte |

## Kill-Kriterien (C12)

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Full BimmerGestalt Re-Audit ohne Fokus | `REJECTED` |
| 2 | SAS-Duplikat statt CROSSREF | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Focused Knowledge Gap Closure; HU-Server bleibt INFERENCE bis eigenes Capture.
```

## Knowledge Feedback (C13)

Desk only — `field_evidence: R0` bleibt. Lab Dummy-HU RFCOMM in `esp32-bt-analyzer` ist orthogonal (synth), nicht dieses Audit.

## Lessons → Transfer

- Phone-App ist RFCOMM **Client** gegen SPP UUID; HU muss SDP/RFCOMM **Server** anbieten (INFERENCE).
- BCL Watchdog ist Multiplex-Dest **5001**, nicht RFCOMM-Kanalnummer.
- A2DP-Connected-Liste filtert Kandidaten (`hasBCL` via SPP UUID) — Transport bleibt RFCOMM.
- Analyzer Dummy-HU sollte SPP SDP + RFCOMM Accept spiegeln, wenn Phone-Client-Pfad getestet wird.

## Bezug

[Application](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-rfcomm.md) · [evidence](evidence.md) · Sheet [`bmw-bcl`](../../technologies/bmw-bcl/SHEET.md) · Prior [`bmw-bcl.md`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl.md)
