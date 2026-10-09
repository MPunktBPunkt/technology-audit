# Audit-Profile

Nicht jedes Quellenrepo ist „Firmware fertig“. Derselbe Dokumentenstandard gilt, aber **Exit-Tiefe und Coverage** hängen vom Profil ab.

Verwandt: [METHODOLOGY.md](METHODOLOGY.md) · [REUSE.md](REUSE.md) · [REVIEW-CHECKS.md](REVIEW-CHECKS.md)

## Profile

| Profil | Wann | Typische Coverage | Pflicht-Artefakte |
|--------|------|-------------------|-------------------|
| `firmware` | lauffähige Firmware + Doku | Sheets `partial`+ wo applied | SCOPE, INVENTORY, Sheets A, Apps B/C, Evidence, Kampagne |
| `lab-tool` | Mess-/Sonden-Repo | wie firmware, Method Note stark | + `methods/<slug>.md` verlinkt |
| `planning` | nur Konzept/Pflichtenheft, **keine** FW | oft `none`/`partial`; Status ≤ `observed` oder `documented` (Sheet aus Spec/Plan) | SCOPE, INVENTORY, Kampagne; Apps dürfen **Design-B** sein; Feld-C meist `UNKNOWN` |
| `ops-field` | Betriebs-/Feldrepo (z. B. PiDrive) | Evidence-lastig | Evidence-IDs auf Upstream-Artefakte; Sheets nur A |

Profil in Audit-YAML setzen: `profile: planning` (o. Ä.).

## Layout-Varianten (firmware)

| Layout | Hinweis |
|--------|---------|
| PlatformIO `src/` | Standardpfade in Applications |
| Arduino `.ino` Monolith | Pfade auf `.ino` + `docs/` ok (siehe [REUSE.md](REUSE.md)) |

## Gemeinsame Mindest-Parität (alle Profile)

Jedes Projekt unter `projects/<id>/` braucht:

1. `README.md`, `SCOPE.md` (mit `reviewed_commit` oder bewusst `reviewed_commit: none` + Begründung), `INVENTORY.md`, `FOLLOW-ON-IDEAS.md`
2. Inventar-Spalten Status + Coverage + Links nach `technologies/…/SHEET.md`
3. Kurzer **Reuse-/Match-Hinweis** (welche Slugs schon existierten)
4. Mindestens eine Audit-Kampagne mit Exit-Tabelle + `evidence.md` (auch wenn nur Planungs-Claims / `UNKNOWN`)

Jedes **active**-Sheet braucht:

- YAML (`slug`, `primary`, `seen_in`, `maturity`)
- Abgrenzung, Fallstricke mit Epistemic-Status, Transfer
- **Projektstart-Checkliste** (Reuse)

## Was in der Definitionsphase oft fehlte

| Lücke | Früher (PiDrive/erste Pilots) | Soll |
|-------|-------------------------------|------|
| Reuse-Match | implizit | explizit in Inventar + Bootstrap |
| Sheet-Checkliste | fehlte | Pflicht im Template |
| `reviewed_commit` | oft fehlend | in SCOPE/Inventar |
| Planungsrepos | nicht vorgesehen | Profil `planning` |
| Method Notes | nur Kandidatenliste | bei Lab-Tools anlegen |
| Hub-Varianten | Arduino-only gedacht | A: Contract vs. Client-Stack trennen |

## Qualitätsreview alter Audits

Bei Nachzug: **nicht** Inhalte erfinden. Nur Struktur/Parität und klar markierte Planungs- vs. Mess-Claims. Reifegrade nicht nachträglich hochsetzen ohne Evidence.
