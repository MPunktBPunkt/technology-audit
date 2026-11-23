# Audit: Apache Etch BinaryTaggedData Reassembly over BCL (B3)

```yaml
id: bmw-etch-rpc-binary-reassembly-2026-11-21
project_id: esp32-bt-analyzer
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits: [bmw-bcl-bt-rfcomm-framing-2026-11-21, nbt-evo-bt-control-plane-closure-2026-11-21]
reuse_outcomes:
  reused: [technologies/bmw-etch-rpc, technologies/bmw-bcl]
  new: []
  not_helped: []
  process: "Lift Etch DEADBEEF reassembly + type-hash coverage + offset conventions into bmw-etch-rpc."
```

## Ziel

Etch über BCL: Envelope `DEADBEEF`+u32BE length, Type-Hash→Methoden-Mapping, fragmentierungsbewusste Reassembly, Offset-Konventionen (CSV vs Raw `P@`/`H@`).

## Scope

- Im Scope: BinaryTaggedData v3 Envelope; Reassembly-Regeln; Hash-Registry-Vollständigkeit in B3; Offset-Hygiene; Dissector-Gap jsonl vs Raw.
- Nicht im Scope: RHMI Model-IDs; SAS-Crypto-Details; Audio.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Envelope + Reassembly als FIELD FACT im Sheet | erfüllt |
| 2 | Offset-Konventionen dokumentiert | erfüllt |
| 3 | field_evidence R0→R3; Dissector-Gap markiert | erfüllt |

## Claim-Level-Tabelle

| Claim | Level | Evidence |
|-------|-------|----------|
| Envelope `DE AD BE EF` \| u32BE body_len \| body | **FIELD FACT** | FORENSIC_B3 §1.2 |
| Body start `03 86 <type_hash_u32BE>` (BinaryTaggedData v3) | **FIELD FACT** | RAW_FORENSIC §4.2 |
| Nur erstes Fragment trägt `DEADBEEF`; Fortsetzung rein längenbasiert | **FIELD FACT** | cert split §1.3 |
| Mehrere Etch-Msgs im selben BCL-Payload-Rest möglich | **FIELD FACT** | §1.4 |
| Alle erfolgreichen B3-Methoden mappten auf HASH_REGISTRY (keine unknown hashes) | **FIELD FACT — DECODED** | RAW_FORENSIC §9 |
| ~1502 BCL / ~1115 Etch (fragmentationsbewusst) | **FIELD FACT** | FORENSIC_B3 §3 |
| `P@`/`H@` = Etch-Magic-Start; CSV oft BCL-Header (= Etch−8 contiguous) | **FIELD FACT** | Timeline §1 |
| `b3.jsonl` unterdekodiert vs Raw (kein Cert, fehlende Results) | **FIELD FACT** | EVAL / MANIFEST |
| Naive DEADBEEF-Suche ohne BCL = falsch bei Fragmenten | **REJECTED** (als Methode) | FORENSIC_B3 intro |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Primärquelle Captures | jsonl oder Raw? | Dissector-Gap | Raw + fragment-aware walker |
| Offset in Berichten | CSV oder Magic? | Timeline §1.1–1.2 | Immer `P@`/`H@` autoritativ |

## Kill-Kriterien

**Hypothese:** Jede Etch-Nutzlast in B3 beginnt (nach Reassembly) mit `DEADBEEF` und bekanntem Type-Hash.

| # | Kill | Status |
|---|------|--------|
| 1 | Unmapped type_hash in erfolgreichem Decode | nicht eingetreten |

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-ETCH-ENVELOPE` | `technologies/bmw-etch-rpc/SHEET.md` |
| `EVID-B3-ETCH-REASSEMBLY` | same |
| `EVID-B3-ETCH-OFFSET-CONV` | same + method |

## Offene Punkte

- Payload-Felder `ver_getVersion` / `info_getSystemInfo` inhaltlich
- map_* Feldnutzung
