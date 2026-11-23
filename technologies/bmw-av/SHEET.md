# Technology Sheet: BMW AV (Connected Entertainment Session)

```yaml
slug: bmw-av
title: BMW AV — Connected Entertainment Session Control
primary: H
tags: [automotive, protocol, audio, foreign-desk]
type: technology
status: active
seen_in: [esp32-bt-analyzer, bimmergestalt-idrive-refs]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R3   # B3 FIELD_B3_GATEB — av_create→PLAY control path
  reusability: W2
  evidence_scope: [FIELD]
```

Ebene **A** + F20-Feld. Primär:
[`audits/bmw-av-session-control-vs-audio-2026-11-21/`](../../audits/bmw-av-session-control-vs-audio-2026-11-21/).  
Evidence: `bt-analyzer` `FIELD_B3_GATEB_20261121T112446Z` (`AV_EVENTS.json`, PLAY skim, Timeline).  
Grenzt an [`bmw-rhmi`](../bmw-rhmi/SHEET.md) (UI) und [`bluetooth-a2dp`](../bluetooth-a2dp/SHEET.md) (Kandidat Audio-Plane — **nicht** bewiesen als B3-Pfad).

## Kurzfassung

**AV** ist die Etch-API für Entertainment-Session-Control der Connected Apps:
`av_create` → `av_requestConnection(ENTERTAINMENT)` → HU `av_connectionGranted` /
`av_requestPlayerState` → Phone `av_playerStateChanged(PLAY|…)`.  
Das ist **Control**, nicht der Audio-Bytestrom. Ob/wo hörbares Audio läuft, ist in B3
**NOT PROVEN** / **NOT OBSERVED**.

## Abgrenzung

- **Ist:** Etch `av_*` Session-/Player-State.
- **Ist nicht:** RHMI Now-Playing Widgets; A2DP/SBC Payload; USB-MSC Audio; iAP Audio.
- **Grenzt an:** [`bmw-etch-rpc`](../bmw-etch-rpc/SHEET.md), [`bmw-rhmi`](../bmw-rhmi/SHEET.md),
  [`bluetooth-a2dp`](../bluetooth-a2dp/SHEET.md), [`bmw-bcl`](../bmw-bcl/SHEET.md).

## Sequenz (FIELD FACT — B3)

```
av_create(id="me.hufman.androidautoidrive.music") → handle
av_requestConnection(AV_CONNECTION_TYPE_ENTERTAINMENT)
  ← av_connectionGranted / av_requestPlayerState
av_playerStateChanged(PLAY)   # B3 anchor P@0x000315a6
```

Danach in B3: kein weiteres `av_*`; RHMI setData/Events laufen weiter auf dest 4004.

## Fallstricke

| Claim | Status |
|-------|--------|
| AV PLAY = hörbares Audio bewiesen | `REJECTED` / `NOT OBSERVED` |
| Post-PLAY Bulk auf BCL dest 4004 = Audio-Stream | `NOT PROVEN` (Default: RHMI-Fragment **INFERENCE**) |
| AV Control = A2DP | `REJECTED` (Schichten) |
| Lab NP stub ohne av_* = Field PLAY-Pfad | `REJECTED` |
| Dual-Plane Capture unnötig wenn UI sichtbar | `REJECTED` — Audio-Boundary braucht parallele Plane |

## Transfer

- PiDrive / AAIdrive-Nachbau: AV-Control und Audio-Transport **getrennte Gates**.
- Nächster Feldlauf: Dual-Plane-Protokoll aus AV-Audit / [`methods/raw-bcl-etch-forensic`](../../methods/raw-bcl-etch-forensic.md).

### Projektstart-Checkliste

- [ ] Control-Pfad und Audio-Plane getrennt instrumentieren
- [ ] PLAY-Offset / Timestamp auf Control-Plane verankern
- [ ] 4004-Bulk nicht als Audio verbuchen ohne Codec-Beweis
- [ ] Operator: audible ja/nein notieren

## Offene Fragen

- Welcher Transport trägt B3-hörbares Audio (falls überhaupt unter Relay)?
- Track-Wechsel: neuer AV-Zyklus oder nur RHMI-Metadata?
- Zusammenhang AVRCP ↔ `av_*` auf NBT Evo

## Lessons

- Gate B / Music-UI CLOSED ≠ Audio-Plane CLOSED.
- Operator „UI sichtbar, kein Ton“ ist valides Feld-Datum — Ursache noch UNKNOWN.
