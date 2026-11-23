# Audit: AM Bootstrap Field (B3)

```yaml
id: bmw-am-bootstrap-field-2026-11-21
project_id: esp32-bt-analyzer
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits: [bmw-rhmi-music-handle23-field-2026-11-21, bmw-etch-rpc-binary-reassembly-2026-11-21]
reuse_outcomes:
  reused: [technologies/bmw-etch-rpc, technologies/bmw-rhmi]
  new: []
  not_helped: []
  process: "Record am_create/registerApp×5 + Spotify REJECTED as AM app."
```

## Ziel

AM Bootstrap (`am_create` / `am_registerApp` / EventHandler) aus B3 dokumentieren und Spotify-als-AM **REJECTED** festnageln.

## Scope

- Im Scope: fünf registerApp-Einträge; create/handler; Abgrenzung Music/RHMI.
- Nicht im Scope: Icon/PNG-Anatomie Deep-Dive; AM UI Layout.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Fünf AM-Apps als FIELD FACT | erfüllt |
| 2 | Spotify ≠ AM REJECTED im Sheet | erfüllt |

## Claim-Level-Tabelle

| Claim | Level | Evidence |
|-------|-------|----------|
| `am_create` / `_result_am_create` | **FIELD FACT** | Raw / FORENSIC_B3 counts |
| Genau **5×** `am_registerApp` | **FIELD FACT** | ADDENDUM + AM_REGISTER_FULL |
| Apps: Google, Amazon Alexa, Bluetooth, YouTube, Screen Mirroring | **FIELD FACT** | ADDENDUM table |
| `am_addAppEventHandler` u. a. assistant/screenmirror/music | **FIELD FACT** | ADDENDUM |
| Spotify / `com.spotify.music` als AM-Eintrag | **REJECTED** | nicht in fünf; package nicht im Raw |
| Media-UI über RHMI `…music` Handle 23 | **FIELD FACT** | RHMI audit |
| Fünf registerApp = fünf sichtbare Menüeinträge | **REJECTED** (als Gleichheit) | ADDENDUM hygiene |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Spotify-Integration-Pfad? | AM oder RHMI+AV? | B3 | RHMI Music + AV; nicht AM |

## Kill-Kriterien

**Hypothese:** Spotify erscheint nicht unter den fünf `am_registerApp`.

| # | Kill | Status |
|---|------|--------|
| 1 | `am_registerApp` mit Spotify/com.spotify.music | nicht eingetreten |

## Knowledge Feedback

| Evidence-ID | Zurück in |
|-------------|-----------|
| `EVID-B3-AM-FIVE-APPS` | `technologies/bmw-etch-rpc/SHEET.md`, `bmw-rhmi` |
| `EVID-B3-AM-SPOTIFY-REJECTED` | same |

## Offene Punkte

- weight/category Semantik für eigene AM-Registrierung
- PNG 48×48 Icon-Format-Kontrakt
