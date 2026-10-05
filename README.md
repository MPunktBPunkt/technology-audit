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

1. [`docs/DOCUMENT-STANDARD.md`](docs/DOCUMENT-STANDARD.md) — verbindliche Dokumenttypen und Regeln  
2. [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — Phasen 0–5  
3. [`docs/TAXONOMY.md`](docs/TAXONOMY.md) — Kategorien und Tags  
4. [`projects/pidrive/`](projects/pidrive/) — erstes Projekt-Gerüst  

Vorlagen liegen unter [`templates/`](templates/).

## Status

| Feld | Wert |
|------|------|
| Version | siehe [`VERSION`](VERSION) |
| Phase | Pilot 2 — BMW NBT Evo (Host / C); Pilot 1 MSC closed (Schema) |
| Pilot-Reihenfolge | `usb-msc` → `bmw-nbt-evo` → `avrcp` |
| Erstes Projekt | PiDrive |

## Herkunft

Siehe [`docs/ORIGIN.md`](docs/ORIGIN.md).
