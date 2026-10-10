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

1. [`docs/PROJECT-START.md`](docs/PROJECT-START.md) — **Neues Projekt starten (Permalink)**  
2. [`technologies/`](technologies/) — Sheet-Index  
3. [`docs/FAMILIES.md`](docs/FAMILIES.md) — Produktfamilien  
4. [`docs/REUSE.md`](docs/REUSE.md) — Match-Regeln (Sprache ≠ Fork)  
5. [`docs/AUDIT-PROFILES.md`](docs/AUDIT-PROFILES.md) — Firmware / Lab / Planung / Ops / **Adapter**  
6. [`docs/DOCUMENT-STANDARD.md`](docs/DOCUMENT-STANDARD.md) — verbindliche Dokumenttypen und Regeln  
7. [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — Phasen 0–5  
8. [`docs/TAXONOMY.md`](docs/TAXONOMY.md) — Kategorien und Tags  
9. [`docs/PROMPT-CONTRACT.md`](docs/PROMPT-CONTRACT.md) — standardisierte Audit-Prompts (Assistenz, kein Schreib-Bot)  
10. [`docs/REVIEW-CHECKS.md`](docs/REVIEW-CHECKS.md) — Qualitätsprüfungen pro Dokumenttyp  
11. [`projects/`](projects/) — Projekte · Eignung: [`docs/KB-FIT.md`](docs/KB-FIT.md)  

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
| Version | [`VERSION`](VERSION) (= Audit-Standard) · [`STANDARD-CHANGELOG`](docs/STANDARD-CHANGELOG.md) |
| Phase | Pilot 2 — BMW NBT Evo (Host / C); Pilot 1 MSC closed (Schema); Prompt-Contract v1 |
| Pilot-Reihenfolge | `usb-msc` → `bmw-nbt-evo` → `avrcp` |
| Projekte | [pidrive](projects/pidrive/) · [pi-fm-tx](projects/pi-fm-tx/) · [esp32-pidrive](projects/esp32-pidrive/) · [heartrate](projects/esp32-heartrate/) · [ergo](projects/esp32-ergo/) · [ftmsprobe](projects/esp32-ftmsprobe/) · [bt-gateway](projects/esp32-bt-gateway/) · [rfmonitor](projects/esp32-rfmonitor/) · [toolnode](projects/esp32-toolnode/) · [metermaster](projects/esp32-metermaster/) · [webradio](projects/esp32-webradio/) · [io-control](projects/esp32-io-control/) · [communicator](projects/esp32-communicator/) · [network](projects/esp32-network/) · [esp-hub-base](projects/esp32-esp-hub/) · [iobroker.esp-hub](projects/iobroker-esp-hub/) · [iobroker.metermaster](projects/iobroker-metermaster/) · [iobroker.kostalpiko](projects/iobroker-kostalpiko/) · [iobroker.fritzwireguard](projects/iobroker-fritzwireguard/) · [freeair100](projects/iobroker-freeair100/) · [kalender](projects/iobroker-kalender/) · [linuxdashboard](projects/iobroker-linuxdashboard/) · [mbrepository](projects/iobroker-mbrepository/) · [metermaster-app](projects/metermaster-app/) · [repositories](projects/iobroker-repositories/) |
| Technologien | [Index](technologies/) · Reuse: [REUSE.md](docs/REUSE.md) |
| Assistenz | Prompt-Contract + `tools/ta-assist` (check / prepare / bootstrap) |

## Herkunft

Siehe [`docs/ORIGIN.md`](docs/ORIGIN.md).
