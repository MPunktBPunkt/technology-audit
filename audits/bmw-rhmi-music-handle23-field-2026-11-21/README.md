# Audit: RHMI Music Handle 23 Field Catalog (B3)

```yaml
id: bmw-rhmi-music-handle23-field-2026-11-21
project_id: esp32-bt-analyzer
related_projects: [bimmergestalt-idrive-refs, pidrive]
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits: [nbt-evo-bt-control-plane-closure-2026-11-21, bimmergestalt-rhmi-checkresource-2026-11-17]
reuse_outcomes:
  reused: [technologies/bmw-rhmi]
  new: []
  not_helped: []
  process: "Ingest Handle-23 NP spine, setData catalog, actions/events into bmw-rhmi; close lab-ID transfer REJECTED with field IDs."
```

## Ziel

Handle-23 State Machine und Feld-IDs (Models 444–458/655, Actions 336/248, Events 660/661, NP-Spine) aus B3 als FIELD FACT in `bmw-rhmi` übernehmen.

## Scope

- Im Scope: create/check/initialize für `…music`; setData-Katalog; Actions/Events; DESCRIPTION fingerprint + extract; Abgrenzung Spotify≠AM.
- Nicht im Scope: eigener RHMI-PoC am F20; TEXTDB/IMAGEDB-Extract; Audio-Transport.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Handle 23 ↔ `me.hufman.androidautoidrive.music` FACT | erfüllt |
| 2 | NP-Spine Model/Action/Event-IDs im Sheet | erfüllt |
| 3 | Lab 100/200 ≠ F20 explizit REJECTED mit Field-Ersatz | erfüllt |
| 4 | DESCRIPTION MD5/size CLOSED | erfüllt |

## Claim-Level-Tabelle

| Claim | Level | Evidence |
|-------|-------|----------|
| Handle **23** = `me.hufman.androidautoidrive.music` | **FIELD FACT** | create map / ADDENDUM |
| Handles 21–25 = calendar / readout / music / mapview / screenmirror | **FIELD FACT** | ADDENDUM |
| `checkResource` ×11 True; **0×** `setResource`; then `initialize` | **FIELD FACT** | jsonl + Raw |
| DESCRIPTION MD5 `e9e31c31110680e13b7a112a7d77eb55`, 92085 B | **FIELD FACT** | EXTRACT.md |
| setData **444/655** = `"Spotify"`; **445** artist; **446/447** title | **FIELD FACT** | rhmi_music / EVAL |
| Cover JPEG model **456** (XML) / image path 441/453 | **FIELD FACT** / STRONG | HANDLE23 + EXTRACTED_MEDIA |
| Playlist model **458** | **FIELD FACT** | PLAY skim / catalog |
| Actions **336**, **248**; Events **660**, **661** | **FIELD FACT** | INTERACTION / ADDENDUM |
| NP spine `audioHmiState` 24 → 444–447 (+ Zeit/Progress) | **STRONG** (XML∩Field) | HANDLE23_CORRELATION |
| 78 modelIds / 20 components H23 alle in XML | **STRONG** | correlation |
| Lab actionId **200** / modelId **100** = F20 | **REJECTED** | Field IDs ersetzen |
| Spotify = `am_registerApp` | **REJECTED** | AM audit / ADDENDUM |
| Multi-track NP state machine vollständig | **PARTIAL** | HOME_MULTITRACK |
| Home/Launcher Entry Object-ID | **NOT OBSERVED** | EVAL |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| PiDrive Lab stub IDs? | 100/200 oder Field? | H23 catalog | Nur 444/445/446·447/660/661/336/248 |
| Template-Upload nötig? | setResource gesehen? | 0× set | Cache-Hit-Pfad; DESCRIPTION-Bytes für eigene App weiter GAP |

## Kill-Kriterien

**Hypothese:** Music-UI in B3 läuft über Handle 23 mit DESCRIPTION `e9e31c31…`.

| # | Kill | Status |
|---|------|--------|
| 1 | Dominante Media-setData auf anderem Handle ohne 23 | nicht eingetreten |

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-RHMI-H23-MAP` | `technologies/bmw-rhmi/SHEET.md` |
| `EVID-B3-RHMI-NP-SPINE` | same |
| `EVID-B3-RHMI-DESC-E9E31C31` | same |

## Offene Punkte

- Eigener RHMI-Client PoC am F20
- TEXTDB/IMAGEDB extract
- Whitelist SHA-256 Digests vollständige Liste
