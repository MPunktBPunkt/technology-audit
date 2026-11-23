# Audit: Method — Raw BCL/Etch Forensic Pipeline (B3)

```yaml
id: method-raw-bcl-etch-forensic-2026-11
project_id: esp32-bt-analyzer
started: 2026-11-22
ended: 2026-11-23
status: closed
profile: lab-tool
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits:
  - bmw-bcl-bt-rfcomm-framing-2026-11-21
  - bmw-etch-rpc-binary-reassembly-2026-11-21
  - bmw-sas-auth-field-crypto-2026-11-21
  - bmw-av-session-control-vs-audio-2026-11-21
reuse_outcomes:
  reused: [methods/kb-cross-check]
  new: [methods/raw-bcl-etch-forensic.md]
  not_helped: []
  process: "Generalize B3 run_raw_forensic pipeline into reusable method note."
```

## Ziel

Generische Methode: Raw-Bin → Frame-Index → Coverage → Crypto-Verify → Timeline, abgeleitet aus dem erfolgreichen B3-Forensic-Lauf.

## Scope

- Im Scope: Verfahrensschritte, Artefakt-Vertrag, Pass/Fail, Fallstricke, Dual-Plane-Erweiterung.
- Nicht im Scope: Tool-Code committen; neue Captures erzeugen.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Method Note unter `methods/` | erfüllt |
| 2 | Reference auf B3 als Example | erfüllt |
| 3 | Anti-Methoden (naive DEADBEEF) markiert | erfüllt |

## Pipeline (summary)

```text
1. Hash integrity of raw bins
2. Strip/mark bridge envelopes
3. BCL frame walk (cmd/src/dest/len)
4. Etch reassembly on (src,dest) substreams
5. Type-hash → method map
6. Coverage / gap classification
7. Domain extractors (SAS/RHMI/AM/CDS/AV)
8. Crypto verify (if SAS)
9. Offset timeline with causality classes
10. Dual-plane attach (if Music/PLAY)
```

Reference implementation (product): `FIELD_B3_…/forensic/run_raw_forensic.py`.

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Method generalisieren? | Nur B3-one-off? | Wiederverwendbar für künftige Captures | Method Note |

## Kill-Kriterien

**Hypothese:** Fragment-aware BCL→Etch liefert vollständige Methodenabdeckung ohne unmapped hashes auf B3.

| # | Kill | Status |
|---|------|--------|
| 1 | Unmapped type_hash bei erfolgreicher Session | nicht eingetreten |

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-METHOD-RAW-FORENSIC` | `methods/raw-bcl-etch-forensic.md` |

## Offene Punkte

- Tooling in technology-audit `tools/` vs product-only
- Wall-clock merge when dual-plane clocks exist
