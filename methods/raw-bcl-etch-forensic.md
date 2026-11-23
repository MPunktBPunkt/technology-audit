# Method: Raw BCL → Etch Forensic Pipeline

```yaml
slug: raw-bcl-etch-forensic
title: Raw BCL → Etch Forensic Pipeline
status: active
tags: [bluetooth, bcl, etch, forensic, field]
```

## Zweck

Aus byte-exakten Phone↔HU Raw-Bins eine reproduzierbare, epistemisch getaggte Analyse erzeugen: Frame-Index, Coverage, Methoden-Timeline, optionale Crypto-Verify — unabhängig von (oft unvollständigen) Live-JSONL-Dissektor-Logs.

Einsetzen bei Connected-App / BCL / Etch Captures (Gate B, Music, SAS, RHMI), besonders wenn `b3.jsonl`-artige Logs Certs/Fragments unterdekodieren.

## Voraussetzungen

- Raw bins beider Richtungen (oder dokumentierte Einseitigkeit)
- BCL-Header-Kenntnis (`u16BE cmd|src|dest|len`)
- Etch BinaryTaggedData v3 Envelope (`DEADBEEF` + u32BE length)
- Type-Hash-Registry (IDL / `.ewh` / bestehendes Mapping)
- Optional: Leaf-Cert für SAS RSA-Verify; Dual-Plane-Log für Audio

Werkzeuge (Referenz): Product `run_raw_forensic.py` unter
`bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/forensic/`.

## Ablauf

1. **Integrity** — SHA-256/MD5 der Raw-Dateien; Größen; First/Last-Bytes notieren.
2. **Envelope triage** — Bridge-/Relay-Preamble (UUID, padding) markieren; nicht als BCL werten.
3. **BCL walk** — Frames parsen; cmd-Histogramm; dest 4004 vs 5001 (WD) trennen.
4. **Etch reassembly** — Pro `(src,dest)`: Substream byte-weise; nur erstes Fragment hat `DEADBEEF`; Fortsetzung längenbasiert; Restbytes können nächste Message starten.
5. **Method map** — Type-Hash → Name; unmapped = OPEN/FAIL je nach Gate.
6. **Coverage matrix** — decoded / preamble / desync gaps / unparsed tail %.
7. **Gap class** — Capture-loss vs Protocol-change vs Parser-bug (getrennt!).
8. **Domain extract** — SAS / RHMI / AM / CDS / AV Event-JSON.
9. **Crypto verify** (falls SAS) — Pad `0x02000000`, Digest=MD5(chal⊕MD5(pad)), RSA-4096 PKCS#1 v1.5 DigestInfo-MD5 vs Leaf.
10. **Timeline** — Offsets `P@`/`H@` (Etch-Magic); Kausalität DIRECT/ORDERED/CORRELATED/UNKNOWN; keine erfundene Wall-Clock.
11. **Dual-plane** (Music/PLAY) — parallele Audio-Kandidatenebene oder explizite Absenz; post-PLAY Bulk auf 4004 nicht als Audio defaulten.

## Artefakte

| Artefakt | Inhalt |
|----------|--------|
| `RAW_FRAME_INDEX.jsonl` | BCL frames |
| `CHRONO_*.json` / `ETCH_TIMELINE.json` | ordered events |
| `METHOD_COMPARE.json` | counts / hash coverage |
| `SAS_CRYPTO_VERIFY.json` | optional crypto |
| `*_EVENTS.json` | domain slices |
| `*_END_TO_END_TIMELINE.md` | human index |
| Analysis summary MD | epistemic tags per finding |

Offset-Konvention:

| Symbol | Bedeutung |
|--------|-----------|
| `P@0x…` | Etch-Magic-Start in phone→hu |
| `H@0x…` | Etch-Magic-Start in hu→phone |
| CSV `file_offset` | oft BCL-Header; contiguous: Etch = csv+8 |

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Integrity | Hashes dokumentiert | Raw geändert ohne Note |
| Grammar | BCL frames + Etch reassembly konsistent | Sticky PayloadTooLarge / naive scan as truth |
| Coverage | Gaps klassifiziert | Unparsed als „Protokoll neu“ ohne Klasse |
| Methods | Registry deckt Session | Unmapped hash als FACT verkauft |
| Crypto | VERIFY pairs = HU accepts | Accept ohne Verify verschwiegen |
| Epistemik | FACT/INFERENCE/OPEN getrennt | jsonl-alone Claims gegen Raw-Widerspruch |
| Audio | Dual-plane oder Absenz FACT | 4004-Bulk = Audio ohne Beweis |

## Fallstricke

- **Naive `DEADBEEF`-Suche** ohne BCL-Grenzen → falsch bei Fragmenten (REJECTED Methode).
- **`b3.jsonl` als Primärquelle** → Cert/Results fehlen; Raw gewinnt.
- **MAX_PAYLOAD=4000** → HU sendet bis ~5306 B.
- **Bridge `13371337`** außerhalb WD-Kanal ≠ BCL-Watchdog-Wire.
- **Multi-INIT concat** in einer Datei → Session-Grenzen markieren.
- **Wall-Clock erfinden** aus File-Order.
- **Post-PLAY Bulk auf dest 4004** automatisch als Audio klassifizieren.

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| B3 Gate B forensic | `FIELD_B3_GATEB_20261121T112446Z` · Audit `method-raw-bcl-etch-forensic-2026-11` |
| SAS crypto closure | `bmw-sas-auth-field-crypto-2026-11-21` |
| BCL framing | `bmw-bcl-bt-rfcomm-framing-2026-11-21` |
| Etch reassembly | `bmw-etch-rpc-binary-reassembly-2026-11-21` |
| AV vs audio | `bmw-av-session-control-vs-audio-2026-11-21` |
