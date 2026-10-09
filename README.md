# technology-audit

Systematische Zerlegung von Hobby-/Embedded-Projekten in Technologien, konkrete Projektanwendungen und wiederverwendbares Wissen.

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

1. [`technologies/`](technologies/) — **Übersicht extrahierter Technologien**  
2. [`docs/DOCUMENT-STANDARD.md`](docs/DOCUMENT-STANDARD.md) — verbindliche Dokumenttypen und Regeln  
3. [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — Phasen 0–5  
4. [`docs/TAXONOMY.md`](docs/TAXONOMY.md) — Kategorien und Tags  
5. [`docs/PROMPT-CONTRACT.md`](docs/PROMPT-CONTRACT.md) — standardisierte Audit-Prompts (Assistenz, kein Schreib-Bot)  
6. [`docs/REVIEW-CHECKS.md`](docs/REVIEW-CHECKS.md) — Qualitätsprüfungen pro Dokumenttyp  
7. [`projects/`](projects/) — Projekte (`pidrive`, `esp32-heartrate`, …)  

Vorlagen: [`templates/`](templates/) · Prompt-Vorlagen: [`templates/prompts/`](templates/prompts/) · generierte Aufträge: [`artifacts/prompts/`](artifacts/prompts/).

Fremdrepos werden nur **gelesen** (Scan / Evidence-Links). Wissen und Tools leben hier — nicht im Zielrepo.

### Assistenz-CLI

```bash
python3 tools/ta-assist check
python3 tools/ta-assist prepare next
python3 tools/ta-assist prepare bootstrap https://github.com/MPunktBPunkt/esp32.ftmsprobe
```

Details: [`tools/README.md`](tools/README.md).

## Status

| Feld | Wert |
|------|------|
| Version | siehe [`VERSION`](VERSION) |
| Phase | Pilot 2 — BMW NBT Evo (Host / C); Pilot 1 MSC closed (Schema); Prompt-Contract v1 |
| Pilot-Reihenfolge | `usb-msc` → `bmw-nbt-evo` → `avrcp` |
| Projekte | [PiDrive](projects/pidrive/) · [esp32-heartrate](projects/esp32-heartrate/) (Desk-Pilot) |
| Technologien | siehe [Index](technologies/) |
| Assistenz | Prompt-Contract + `tools/ta-assist` (check / prepare / bootstrap) |

## Herkunft

Siehe [`docs/ORIGIN.md`](docs/ORIGIN.md).
