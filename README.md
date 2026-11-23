# technology-audit

Cross-project knowledge base for hobby/embedded work: reusable technology sheets, project applications, and evidence-backed audits — so the next build does not start from zero.

Systematische Zerlegung von Hobby-/Embedded-Projekten in Technologien, konkrete Projektanwendungen und wiederverwendbares Wissen. Lizenz: [`LICENSE`](LICENSE) (MIT).

PiDrive ist der Maßstab: In einem Projekt können Dutzende Technologien zusammentreffen (DAB+, USB-MSC, AVRCP, PipeWire, ESP32, …). Deshalb trennt dieses Repository **Projektkontext** von **Technologie-Wissen**.

## Schichten

| Schicht | Pfad | Inhalt |
|---------|------|--------|
| Projekte | [`projects/`](projects/) | Scope, Inventar, projektspezifische Anwendungen |
| Technologien | [`technologies/`](technologies/) | Wiederverwendbare Technology Sheets |
| Methoden | [`methods/`](methods/) | Analyseverfahren (Tracing, Replay, …) |
| Audits | [`audits/`](audits/) | Zeitlich begrenzte Analyse-Kampagnen |

```
projects/<id>/INVENTORY ──► technologies/<slug>/SHEET
projects/<id>/applications/<slug> ──► technologies/<slug>/SHEET
audits/<kampagne> ──► Inventar + Methoden
```

## Einstieg

1. [`AGENTS.md`](AGENTS.md) / [`generated/retrieval/`](generated/retrieval/) — **AI-Einstieg (Retrieval)**  
2. [`docs/PROJECT-START.md`](docs/PROJECT-START.md) — **Neues Projekt starten (Permalink)**  
3. [`technologies/`](technologies/) — Sheet-Index (Primary A–J) · [`index.yaml`](technologies/index.yaml)  
4. [`docs/KNOWLEDGE-MATURITY.md`](docs/KNOWLEDGE-MATURITY.md) — **W vs Evidence (R) vs Scope** (generiert; nicht Pilot-Status)  
5. [`docs/EVIDENCE-CLAIM-MODEL.md`](docs/EVIDENCE-CLAIM-MODEL.md) — Evidence/Claim/Scope für Skalierung  
6. [`docs/FAMILIES.md`](docs/FAMILIES.md) — Produktfamilien  
7. [`docs/REUSE.md`](docs/REUSE.md) — Match-Regeln (Sprache ≠ Fork)  
8. [`docs/MAINTENANCE.md`](docs/MAINTENANCE.md) — SoT / Index regenerieren / Check-Stufen  
9. [`docs/AUDIT-PROFILES.md`](docs/AUDIT-PROFILES.md) — Firmware / Lab / Planung / Ops / Adapter  
10. [`docs/DOCUMENT-STANDARD.md`](docs/DOCUMENT-STANDARD.md) — Dokumenttypen  
11. [`docs/KB-FIT.md`](docs/KB-FIT.md) — Eignung & Grenzen  
12. [`docs/PROMPT-CONTRACT.md`](docs/PROMPT-CONTRACT.md) · [`docs/REVIEW-CHECKS.md`](docs/REVIEW-CHECKS.md) · [`projects/`](projects/)

Vorlagen: [`templates/`](templates/) · Prompt-Vorlagen: [`templates/prompts/`](templates/prompts/) · generierte Aufträge: [`artifacts/prompts/`](artifacts/prompts/).

Fremdrepos werden nur **gelesen** (Scan / Evidence-Links). Wissen und Tools leben hier — nicht im Zielrepo.

### Assistenz-CLI

```bash
python3 tools/ta-assist index    # Sheet-Katalog + README nach Primary
python3 tools/ta-assist check
python3 tools/ta-assist prepare next
python3 tools/ta-assist prepare bootstrap https://github.com/MPunktBPunkt/esp32.ftmsprobe
```

Details: [`tools/README.md`](tools/README.md).

## Status

| Feld | Wert |
|------|------|
| Version | [`VERSION`](VERSION) (= Audit-Standard) · [`STANDARD-CHANGELOG`](docs/STANDARD-CHANGELOG.md) |
| KB-Maturity | generierte Übersicht: [`docs/KNOWLEDGE-MATURITY.md`](docs/KNOWLEDGE-MATURITY.md) (W ≠ Evidence ≠ Projekt-Status) |
| Aktive Feld-Kampagnen | BMW NBT Evo Host/C (historisch „Pilot 2“); MSC-Schema closed — **nicht** die Reife der gesamten KB |
| Projekte | generierter Katalog: [`projects/`](projects/) · [`projects/index.yaml`](projects/index.yaml) |
| Technologien | [`technologies/`](technologies/) · [`index.yaml`](technologies/index.yaml) · Reuse: [REUSE.md](docs/REUSE.md) |
| Audit-Index | generiert: [`audits/INDEX.yaml`](audits/INDEX.yaml) (`A-YYYY-NNN`) |
| Retrieval (AI) | [`AGENTS.md`](AGENTS.md) · [`generated/retrieval/`](generated/retrieval/) · Modell: [EVIDENCE-CLAIM-MODEL](docs/EVIDENCE-CLAIM-MODEL.md) |
| Retrieval-Tests | [`docs/retrieval-tests.yaml`](docs/retrieval-tests.yaml) · Topics: [retrieval-topics](docs/retrieval-topics.yaml) |
| Assistenz | `ta-assist` index / check / prepare / bootstrap · Pflege: [MAINTENANCE.md](docs/MAINTENANCE.md) |

## Herkunft

Siehe [`docs/ORIGIN.md`](docs/ORIGIN.md).
