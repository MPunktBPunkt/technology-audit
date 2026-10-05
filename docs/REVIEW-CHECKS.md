# Review-Checks

Prüffragen pro Dokumenttyp. Nutzen für Mensch, KI und (später) Structure-Check.

Verwandt: [DOCUMENT-STANDARD.md](DOCUMENT-STANDARD.md) · [PROMPT-CONTRACT.md](PROMPT-CONTRACT.md) · [METHODOLOGY.md](METHODOLOGY.md).

**Schweregrade (für Tools):**

| Stufe | Bedeutung |
|-------|-----------|
| `error` | Standard verletzt; sollte vor Merge/Abschluss behoben werden |
| `warning` | vermutlich falsch oder unvollständig; Begründung nötig |
| `info` | Hinweis / nächster sinnvoller Schritt |

---

## Technology Sheet (`technologies/<slug>/SHEET.md`)

| # | Check | Stufe |
|---|-------|-------|
| S1 | YAML-Frontmatter vorhanden; `slug`, `primary`, `status`, `maturity` gesetzt | error |
| S2 | Genau eine Primary-Kategorie aus der Taxonomie | error |
| S3 | Inhalt ist nur Ebene **A** (kein projektspezifisches Host-/Feldverhalten als allgemeines Tech-Wissen) | error |
| S4 | Heuristik: Häufung von Projektnamen, Feldzeiten, konkreten Host-Claims → wahrscheinlich B/C-Vermischung | warning |
| S5 | Fallstricke mit Epistemic-Status (`FACT` / `HYPOTHESIS` / `REJECTED` / …) | warning |
| S6 | Referenzen: Specs/Docs verlinkt oder als offen markiert | warning |
| S7 | Offene Fragen explizit gelistet (oder bewusst „keine“) | info |
| S8 | `seen_in` listet Projekte, die eine Application haben (sonst Nachzug) | info |

---

## Project Scope (`projects/<id>/SCOPE.md`)

| # | Check | Stufe |
|---|-------|-------|
| P1 | Grenzen und Nicht-Ziele genannt | error |
| P2 | Quellen-/Ursprungsrepos verlinkt | warning |
| P3 | Systeme/Hardware grob umrissen | warning |

---

## Project Inventory (`projects/<id>/INVENTORY.md`)

| # | Check | Stufe |
|---|-------|-------|
| I1 | YAML oder klarer Kopf mit `project_id` / `updated` | warning |
| I2 | Status ∈ {`candidate`,`observed`,`documented`,`applied`,`transferred`} | error |
| I3 | Coverage ∈ {`none`,`partial`,`full`} | error |
| I4 | Status `documented`/`applied` ⇒ Sheet-Pfad existiert als Datei | error |
| I5 | Status `applied` ⇒ Application-Datei existiert | error |
| I6 | Status `observed`/`candidate` und Sheet-Link fehlt als Datei ⇒ nur **warning** (Zielpfad darf vorausweisen) | warning |
| I7 | Primary + Tags konsistent zur Taxonomie | warning |
| I8 | Coverage-Lücken / Pilot-Reihenfolge dokumentiert | info |

---

## Project Application (`projects/<id>/applications/<slug>.md`)

| # | Check | Stufe |
|---|-------|-------|
| A1 | Verweis auf Technology Sheet (gleicher Slug) | error |
| A2 | Ebene **B** (Implementierung) und **C** (Host/Feld) erkennbar getrennt | error |
| A3 | C-Claims mit Evidence-ID und Epistemic-Status | error |
| A4 | Keine generischen Spec-Lehrbuchpassagen (gehören ins Sheet) | warning |
| A5 | Relevante Pfade / Datenfluss / Konfig skizziert | warning |
| A6 | Maturity-Block vorhanden und Werte gültig (`R0–R5`, `W0–W5`) | warning |
| A7 | Offene Fragen gelistet | info |

---

## Audit Campaign (`audits/<id>/README.md`)

| # | Check | Stufe |
|---|-------|-------|
| C1 | YAML: `id`, `project_id`, `status`, `started` | error |
| C2 | Exit-Kriterien als Tabelle mit Status | error |
| C3 | `status: closed` ⇒ alle Pflicht-Exit-Kriterien erfüllt **oder** bewusste Abweichung dokumentiert | error |
| C4 | Artefakte (Sheet/Application/Evidence) verlinkt | warning |
| C5 | Lessons Learned bei `closed` vorhanden | warning |
| C6 | Offene Punkte / Transfer nach Abschluss | info |

---

## Evidence-Register (`audits/<id>/evidence.md`)

| # | Check | Stufe |
|---|-------|-------|
| E1 | IDs im Format `EVID-<AREA>-<YYYY-MM-DD>-<nnn>` | error |
| E2 | Jede Zeile: Claim + Status + Quelle/Link | error |
| E3 | Status ∈ Epistemic-Status aus dem Dokumentenstandard | error |
| E4 | Rohdaten nicht inline; nur Links ins Ursprungsrepo | warning |
| E5 | Offene Claims ohne ID explizit als solche geführt | info |
| E6 | Application-C-Claims haben Entsprechung im Register (oder Verweis) | warning |

---

## Method Note (`methods/<slug>.md`)

| # | Check | Stufe |
|---|-------|-------|
| M1 | Beschreibt Verfahren, nicht einmaliges Projektergebnis | warning |
| M2 | Wann anwenden / Inputs / Outputs klar | warning |
| M3 | Verlinkt aus mindestens einer Application oder Audit-Kampagne | info |

---

## Maturity-Konsistenz (übergreifend)

| # | Check | Stufe |
|---|-------|-------|
| R1 | Field evidence ≥ R4 verlangt in der Regel dokumentiertes Feld-PASS (nicht nur Lab) | warning |
| R2 | Aktive Kampagne mit offenem Feld-Exit und Application `field_evidence: R4+` ⇒ Widerspruch prüfen | warning |
| R3 | Technology-Sheet `implementation`/`field_evidence` oft R0, wenn Details in Application liegen — das ist ok | info |
| R4 | Coverage `full` bei offenen kritischen Fragen / fehlender Evidence ⇒ eher `partial` | warning |

Siehe Beispiele in [DOCUMENT-STANDARD.md](DOCUMENT-STANDARD.md#reifegrade-beispiele).

---

## Prompt-Artefakte (`artifacts/prompts/`)

| # | Check | Stufe |
|---|-------|-------|
| Q1 | Enthält die neun Pflichtbausteine aus dem Prompt-Contract | error |
| Q2 | Schreibt keine Anweisung, Wissensdateien ohne Review zu committen | error |
| Q3 | Nennt konkrete Input-Pfade | warning |

---

## Verwendung

- Manuell: Checkliste beim Review eines PRs oder Prompt-Laufs.
- Prompt-Typ `quality-review`: diese Datei als verbindliche Prüfliste einbinden.
- Später CLI/`ta-assist check`: `error` → Exit ≠ 0; `warning`/`info` → Report.
