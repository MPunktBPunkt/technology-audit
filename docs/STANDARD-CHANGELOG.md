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

### 0.7.1 — 2026-10-13

**PATCH — Klarstellungen nach Validierung** ([Change Proposal](reports/2026-10-13-v0.7.0-to-v0.7.1-change-proposal.md) · [Release Review](reports/2026-10-13-v0.7.1-release-review.md)):

- **C-001:** `NO JUSTIFIED KILL CRITERION` als erlaubtes C12-Ergebnis (mit Begründung); bedeutet nicht „kein Test / alles bewiesen / UNKNOWN ok / nie stoppen“.
- **C-002:** optionale Spalte **Wissenszeitpunkt** in Decision Trace / Review Checks (`KNOWN BEFORE TEST` / `DISCOVERED DURING TEST` / `DISCOVERED AFTER TEST` / `RETROFIT`) — keine Pflicht.
- **C-003:** `UNKNOWN` ≠ automatisches STOP ([METHODOLOGY](METHODOLOGY.md), Epistemic-Status); Semantik von `UNKNOWN` unverändert.
- **C-004:** optionaler **Retro-Impact**-Block nur für Revalidation/Counterfactual — nicht für normale Audits Pflicht.

**Nicht Teil dieses PATCH:** neue Pflicht-Checks, CLI-Pflicht C10–C13, globale Callback-Re-Entry-Pflicht, neue E-0/E-1-/Feld-/Upstream-Pflichten, Migration alter Audits.

### 0.7.0 — 2026-10-12

**Operationalisierung nach PiDrive-Validierung (E7/S6 Busy-Pacing am BMW NBT):**

Das Audit reduziert den Suchraum (Desk → Hypothese → Lab → Feld). Die nächste Qualitätsstufe ist die systematische Brücke **Evidence → Decision → Engineering Action → Knowledge Feedback**.

- **Decision Trace** — bei experimentellen Kampagnen (`lab-tool` / `ops-field` mit Go/No-Go): Tabelle Entscheidung → Frage → Evidence-ID → Konsequenz ([`templates/audit-campaign.md`](../templates/audit-campaign.md)).
- **Engineering Review Checks** — aus entscheidungsrelevanter Evidence konkrete Pre-Test-Prüfungen für den Zielcode (State/Re-Entry/Idempotenz).
- **Kill-Kriterien** — vor dem ersten Messlauf einer Hypothese präregistrieren (falsifizierbar).
- **Knowledge Feedback** — Lab-/Field-Ergebnisse als Evidence-IDs zurück in Application/Sheet (`Desk → Lab → Field → Audit`).
- Desk-Evidence ≠ Lab-Fact ≠ Field-Fact — explizit im [Dokumentenstandard](DOCUMENT-STANDARD.md).
- Review-Checks: C10–C13, E7 (warning; Alt-Kampagnen ohne Revalidation gültig).
- Validierungsbeispiel: [`tinyusb-msc-busy-retry-2026`](../audits/tinyusb-msc-busy-retry-2026/) → Feld [`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/) (`EVID-BMWHU-2026-10-12-*`).

**Unverändert:** Evidence-Register, Epistemic-Status, Reuse, A/B/C-Trennung, explizite Gates. P2-Effizienzmetriken und CLI-Spiegelung von C10–C13 bleiben optional.

### 0.6.6 — 2026-10-11

**Qualität nach KB-Cross-Check (ESP-FM / Pi-TX Transfer):**

- **Chip-/SoC-Varianten-Regel:** Claims gelten nur für die belegte Variante; keine automatische Übertragung (z. B. Classic ESP32 APLL ↛ ESP32-S3). Siehe [`REUSE.md`](REUSE.md), [`METHODOLOGY.md`](METHODOLOGY.md).
- **Signalpfad-Kette:** Bei RF/Clock-Technologien optionale Stufe Source→…→Pad mit Claim-Status pro Stufe ([`DOCUMENT-STANDARD.md`](DOCUMENT-STANDARD.md)).
- **Gate vor Sheet-Ausweitung:** Unbelegte Chip-/Pfad-Varianten bleiben `UNKNOWN`/`HYPOTHESIS` bis Desk-Gate (Register/TRM) und/oder Lab-Gate (Messung); kein neues Sheet nur aus Architekturidee.
- **KB-Cross-Check / Blindtest:** Prompt-Typ `kb-cross-check` + Method `kb-cross-check`; Ziel = Reasoning-Bausteine prüfen, nicht Zusammenfassung wiederholen.
- Review-Checks: G17 (Chip-Scope), G18 (absolute „einzige Kandidat“-Claims), G19 (Gate vor Varianten-Sheet).
- Fremd-Audit-Beispiel: [`esp-fm-tx-2026-foreign`](../audits/esp-fm-tx-2026-foreign/) + Sheet `esp32-apll-fm-tx`.

**Keine** Änderung an A/B/C-Pflichtfeldern — bestehende Kampagnen auf 0.6.x bleiben gültig.

### 0.6.5 — 2026-10-10

**Härtung (Reviews nach 0.6.4):**

- `seen_in` nur kanonische `project_id` (S9/S10 error); bidirektional Sheet↔App (S8/G2)
- Indexer: YAML/Markdown-Escaping, Primary/Slug-Validierung; **Projektkatalog** `projects/index.yaml`
- Retrieval-Fixtures: [`retrieval-tests.yaml`](retrieval-tests.yaml) + Check RT1
- Transfer-Nachweis: `reuse_outcomes` in Kampagne/FOLLOW-ON ([`MAINTENANCE.md`](MAINTENANCE.md))
- Info R5: active Sheet mit `seen_in` aber `field_evidence=R0`

### 0.6.4 — 2026-10-10

**Neu (Navigation / Wartung):**

- Pflicht-Katalog: `python3 tools/ta-assist index` → `technologies/index.yaml` + README **nach Primary**
- Checks NAV1–NAV4 (Index↔Sheets), S8 (`seen_in` ohne Application)
- Pflege-SoT: [`MAINTENANCE.md`](MAINTENANCE.md); KB-FIT aktualisiert
- CLI `ta-assist` 0.1.5; C8 warnt nur bei major.minor-Lag (Patch-Lag = info C8p)

**Keine** Änderung an A/B/C-Inhaltspflicht — bestehende Kampagnen auf 0.6.3 bleiben gültig.

### 0.6.3 — 2026-10-09

**Neu:**

- **Sprache/Stack ist Application-B**, nicht Sheet-A: gleicher Contract (C++/Arduino und Node.js) → gleicher Slug wo Abgrenzung passt
- Profil **`adapter`** für ioBroker-/Dienst-Repos
- Navigations-Einstieg [`PROJECT-START.md`](PROJECT-START.md) + Familienkarte
- Sheets: `iobroker-esp-hub-adapter`, `esp-hub-base-template`; Hub-Contract A geschärft (Server+Client)

### 0.6.2 — 2026-10-09

**Neu:**

- Hub: Identity oft über `name`/`hwType`/`mac` — `fwType` **nicht** Pflicht (Arduino-Monolith-Familie)
- Schicht-Abgrenzung Scan: **RF** (`rf-environment-monitor`) ≠ **LAN/TCP** (`lan-device-inventory`) ≠ **ESP-NOW Peers**
- Browser-Media-Host ≠ A2DP / PipeWire / DAB (webradio-ESP)
- Sheets: `webradio-browser-host`, `esp-lab-bus-tools`, `esp-now-messaging`, `lan-device-inventory`, `fritzbox-tr064`

### 0.6.1 — 2026-10-09

**Neu:**

- Reuse: **Geschwister-Produkte** (gleicher Slug, kontrastierende Applications)
- Reuse: Inventar-Match-Tabellen ohne Spaltenname `Slug` (Parser-Kollision)
- Reuse: Repo-Layout Arduino-`.ino` vs. PlatformIO
- Sheet-Muster für Modular-Firmware / MQTT / ioBroker Simple-API / OLED (aus toolnode + MeterMaster)

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
