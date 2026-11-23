# Audit: AV Session Control vs Audio Transport (B3)

```yaml
id: bmw-av-session-control-vs-audio-2026-11-21
project_id: esp32-bt-analyzer
related_projects: [pidrive, bimmergestalt-idrive-refs]
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits: [bmw-rhmi-music-handle23-field-2026-11-21, method-raw-bcl-etch-forensic-2026-11]
reuse_outcomes:
  reused: [technologies/bmw-rhmi, technologies/bluetooth-a2dp, technologies/bmw-etch-rpc]
  new: [technologies/bmw-av]
  not_helped: []
  process: "Isolate AV control path FACT; define audio boundary OPEN + dual-plane protocol; new bmw-av sheet."
```

## Ziel

AV-Control-Pfad (`av_create` → ENTERTAINMENT → `connectionGranted` → `av_playerStateChanged` PLAY) als FIELD FACT isolieren und klar vom (noch unbekannten) Audio-Transport abgrenzen.

## Scope

- Im Scope: AV Etch-Sequenz; PLAY-Anchor `P@0x000315a6`; post-PLAY Bulk-Klassifikation; Dual-Plane-Protokoll-Definition.
- Nicht im Scope: A2DP-Deep-Dive; RHMI Model-Catalog (→ RHMI-Audit); audible Root-Cause.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | AV Control-Pfad im Sheet `bmw-av` | erfüllt |
| 2 | Control ≠ Audio-Transport explizit | erfüllt |
| 3 | Dual-Plane next-field protocol lock | erfüllt |
| 4 | post-PLAY 4004 ≠ Audio als Default | erfüllt |

## Claim-Level-Tabelle

| Claim | Level | Evidence |
|-------|-------|----------|
| `av_create(id=…music)` → handle 1 | **FIELD FACT** | AV_EVENTS.json / Raw `P@0x1912c` |
| `av_requestConnection(ENTERTAINMENT)` | **FIELD FACT** | same |
| HU `av_connectionGranted` + `av_requestPlayerState` | **FIELD FACT** | HU Raw |
| Phone `av_playerStateChanged` **PLAY** @ `P@0x000315a6` | **FIELD FACT** | Timeline / PLAY skim |
| Kein weiteres `av_*` nach PLAY in Capture | **FIELD FACT** | PLAY skim |
| Post-PLAY Bulk auf dest **4004** | **FIELD FACT** | PLAY skim |
| Bulk = RHMI-Fragmente | **INFERENCE** | header/hash pattern |
| Bulk = PCM/A2DP/iAP Audio | **NOT PROVEN** | — |
| Separater Non-4004 Audio-Kanal in Raw-Bins | **NOT OBSERVED** | — |
| Audible Playback | **NOT OBSERVED** (Operator: kein Ton) | EVAL / Timeline |
| Ursache (Bridge / missing transport / HU backend) | **UNKNOWN** | NEXT_AUDIO_BOUNDARY |
| AV Control = Audio-Transport | **REJECTED** | Dual-plane framing |

## Dual-Plane Next Protocol (locked)

```text
T0 Capture START (dual-plane + shared monotonic clock)
T1 Music Entry
T2 Spotify / artist / title / cover visible
T3 PLAY
T4 wait 10–20 s
T5 observe audio-transport plane
T6 STOP
```

Planes: Etch/BCL control (`P@`/`H@`) **and** candidate audio plane (A2DP/other) — or explicit absence FACT.

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Nächster P0 nach Control-Closure? | Mehr RHMI-RE? | NEXT_AUDIO_BOUNDARY | Nein — Dual-Plane Audio |
| Sheet neu oder unter RHMI? | Eigene API-Oberfläche? | av_* IDL | Neu `bmw-av` |

## Kill-Kriterien

**Hypothese:** AV-Etch-Sequenz in B3 steuert Session-State, transportiert aber keinen Audio-Stream auf dest 4004.

| # | Kill | Status |
|---|------|--------|
| 1 | Nachweisbarer Audio-Codec-Stream auf 4004 nach PLAY | nicht eingetreten |

`NO JUSTIFIED KILL` für „Audio existiert irgendwo“ — Abwesenheit braucht Dual-Plane-Capture.

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-AV-CONTROL-PATH` | `technologies/bmw-av/SHEET.md` |
| `EVID-B3-AV-PLAY-315A6` | same |
| `EVID-B3-AUDIO-BOUNDARY-OPEN` | same + method dual-plane |

## Offene Punkte

- Audio-Transport-Identifikation (P0 Dual-Plane)
- Track A→B Re-Init vs Metadata-only
- Home Entry Object-ID (P4)
