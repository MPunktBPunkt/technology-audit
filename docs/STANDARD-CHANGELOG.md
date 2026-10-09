# Audit-Standard Changelog

Die Datei [`VERSION`](../VERSION) ist die **Audit-Standard-Version**. Jede Kampagne trägt sie als `standard_version` in der YAML mit — so sieht man später, gegen welchen Regelstand das Audit lief.

Verwandt: [DOCUMENT-STANDARD.md](DOCUMENT-STANDARD.md) · [AUDIT-PROFILES.md](AUDIT-PROFILES.md) · [REUSE.md](REUSE.md) · [REVIEW-CHECKS.md](REVIEW-CHECKS.md)

## Semver (Framework)

| Stelle | Bedeutung |
|--------|-----------|
| MAJOR | harte Regelbrüche / Pflichtfelder geändert |
| MINOR | neue Pflicht-Checks, Profile, Reuse-Pflichten |
| PATCH | Klarstellungen, Templates, Docs ohne neue Pflicht |

CLI `tools/ta-assist` hat eine **eigene** Semver und ist davon unabhängig.

## Versionen

### 0.6.0 — 2026-10-09

**Neu / Pflicht:**

- `standard_version` in jeder Audit-Kampagne (dieses Changelog)
- [`REUSE.md`](REUSE.md) — Match vor neuem Sheet
- [`AUDIT-PROFILES.md`](AUDIT-PROFILES.md) — `firmware` / `lab-tool` / `planning` / `ops-field`
- Sheet **Projektstart-Checkliste**
- Review G1–G8, PL1–PL4; Checker G6/G7
- Bootstrap-Prompt: `existing_sheets`-Katalog
- Hub-Sheet: IDF-Client / einmalige `otaUrl` (A)

**Wer darunter fehlt:** Kampagnen ohne Profil, ohne Reuse-Hinweis, ohne Checklisten, ohne `standard_version`.

### 0.5.1 — 2026-10-05 (ungefähr)

Prompt-Contract, `ta-assist`, Review-Checks, Evidence-IDs, A/B/C — noch ohne REUSE/Profile/`standard_version`.

### 0.5.0 — 2026-10-04 (Definitionsphase)

Erste Pilots (MSC/BMW): Sheets/Apps/Evidence, Status/Coverage. Viele spätere Pflichtstücke fehlten noch.

## Nachziehen älterer Audits

1. `standard_version` auf den **damals gültigen** Stand setzen (nicht still auf current heben).
2. Optional `standard_gaps:` in der YAML auflisten (was gegenüber current fehlt).
3. Parität nachziehen = neuer Commit; dann `standard_version` anheben **und** Gaps schließen oder bewusst belassen.
