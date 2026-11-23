# Audit: BMW BCL BT/RFCOMM Framing from B3 Raw

```yaml
id: bmw-bcl-bt-rfcomm-framing-2026-11-21
project_id: esp32-bt-analyzer
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits: [nbt-evo-bt-control-plane-closure-2026-11-21, bmw-bcl-rfcomm-role-2026-desk]
reuse_outcomes:
  reused: [technologies/bmw-bcl]
  new: []
  not_helped: []
  process: "Promote BCL framing/fragmentation/coverage from B3 raw into bmw-bcl sheet as FIELD FACT."
```

## Ziel

BCL-Grammatik, Fragmentierung, dest 4004, Watchdog und Coverage/Desync aus Byte-exakten Raw-Bins als Field-FACT in `bmw-bcl` verankern (bisher stark Desk/Lab).

## Scope

- Im Scope: 8-B Header; cmd-Codes; Phone 4000-B vs HU ≤5306-B; dest 4004 Etch; WD 5001/`13371337`; Coverage-Matrix; Desync-Gaps; Bridge-Envelope-Abgrenzung.
- Nicht im Scope: Etch-Methoden-Semantik; Audio-Transport; USB/ENET-BCL.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Header-Grammatik FIELD FACT im Sheet | erfüllt |
| 2 | Fragmentierungsregeln Phone/HU dokumentiert | erfüllt |
| 3 | Coverage + Desync-Klassifikation | erfüllt |
| 4 | Bridge-Envelope ≠ BCL Wire getrennt | erfüllt |

## Claim-Level-Tabelle

| Claim | Level | Evidence |
|-------|-------|----------|
| `u16BE cmd\|src\|dest\|len` + payload | **FIELD FACT** | FORENSIC_B3 + RAW_FORENSIC §4 |
| cmds OPEN/DATA/CLOSE/HS/SELECTPROTO/DATAACK/KNOCK beobachtet | **FIELD FACT** | Frame index |
| dest **4004** = Etch-Nutzlast | **FIELD FACT** | DATA src 10–19 → 4004 |
| dest **5001** WD payload `13 37 13 37` | **FIELD FACT** | Raw WD frames |
| Phone fragmentiert bei **4000** B BCL-DATA | **FIELD FACT** | cert 4000+2126 |
| HU sendet BCL-DATA bis **5306** B | **FIELD FACT** | hu_to_phone |
| Reassembly längenbasiert auf `(src,dest)` ohne Seq-Feld | **FIELD FACT** | FORENSIC_B3 §1.3–1.4 |
| `hu_to_phone` Coverage 100 %; `phone_to_hu` ≈99.76 % | **FIELD FACT** | Coverage matrix |
| Phone Desync @ `0x52a8b` (fehlende Header-Bytes) | **FIELD FACT** / Relay-loss **HYPOTHESIS** | RAW_FORENSIC §4.4 |
| 56-B UUID-Preamble = Debian-Bridge-Envelope | **STRONG** (nicht BT-Wire) | FORENSIC_B3 §2 |
| Isolierte `13371337` außerhalb WD-Kanal = Bridge keepalive | **STRONG** / ≠ BCL-Spec | §2.2 |
| INIT magic `12 34 56 78` | **FIELD FACT** | phone_to_hu |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Parser MAX_PAYLOAD=4000? | Reicht für HU? | HU len=5306 | Nein — Fail-Risiko; Sheet + Tools |
| Raw vs jsonl Primär? | Cert in jsonl? | MANIFEST/EVAL | Raw Primär |

## Kill-Kriterien

**Hypothese:** Alle Nutzdaten der B3-Session folgen BCL-Header-Grammatik (außer markierten Bridge-Envelopes).

| # | Kill | Status |
|---|------|--------|
| 1 | Nutzlaststrom ohne BCL/Envelope-Erklärung als neuer Layer | nicht eingetreten |

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-BCL-GRAMMAR` | `technologies/bmw-bcl/SHEET.md` |
| `EVID-B3-BCL-FRAG-4000-5306` | same |
| `EVID-B3-BCL-COVERAGE` | same |

## Offene Punkte

- USB/ENET gleiches Framing?
- REGISTER/BROADCAST in anderen Captures?
