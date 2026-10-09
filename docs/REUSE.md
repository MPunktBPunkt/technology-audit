# Wissensbasis nutzen (Reuse)

Wie man bei einem **neuen** Projekt auf bestehendes Wissen zurückgreift — ohne Forks und ohne Spec mit Host-Quirks zu vermischen.

Verwandt: [DOCUMENT-STANDARD.md](DOCUMENT-STANDARD.md) (Wissenswachstum) · [METHODOLOGY.md](METHODOLOGY.md) · [technologies/](../technologies/) · Assistenz: `tools/ta-assist prepare bootstrap <url>`

## Einstieg in 5 Schritten

0. **Profil** — [`AUDIT-PROFILES.md`](AUDIT-PROFILES.md): Firmware, Lab-Tool, **Planung** oder Ops/Feld? Exit-Tiefe danach bemessen.
1. **Index lesen** — [`technologies/README.md`](../technologies/README.md): welche Sheets existieren schon?
2. **Fremdrepo scannen** — Signale sammeln (`prepare bootstrap` oder manuell Phase 0).
3. **Matchen, nicht neu erfinden** — jedes Signal einem bestehenden Slug zuordnen oder bewusst neuen Slug beantragen.
4. **Sheet nur um A erweitern** — neue Fallstricke/Transfer/Referenzen; `seen_in` ergänzen; Reusability prüfen (G5). Bei `planning`: Spec-/Design-A erlaubt, keine erfundenen Messungen.
5. **Application neu** — B/C nur für *dieses* Projekt; Evidence-IDs neu, Querverweise auf ältere Kampagnen erlaubt.

```text
neues Repo
   │
   ├─► bekannter Slug? ──ja──► Sheet wachsen + Application
   │                         (kein technologies/foo-v2/)
   └─► neu? ──────────────► Sheet anlegen + Application
                            (Abgrenzung zu Nachbar-Slugs klar)
```

## Was man wiederverwenden darf

| Artefakt | Wiederverwenden als | Nicht |
|----------|---------------------|-------|
| Technology Sheet (A) | Checkliste / Fallstricke / Steuerstrategien | Projektdateipfade kopieren |
| Method Note | Lab-/Feldverfahren Schritt für Schritt | Rohtraces hierher spiegeln |
| Project Application (B/C) | Inspiration, Kontrast („anders als in ergo…“) | 1:1 als Wahrheit für neues Projekt |
| Evidence-IDs | zitieren / verlinken | IDs umdeklarieren oder löschen |
| Inventar-Zeilen | Status-Vorbild | Coverage `full` ohne Beleg übernehmen |

## Projektstart-Fragen (pro Kandidat)

Bevor ein neues Sheet entsteht:

1. Gibt es schon einen Slug mit gleicher Primary + Abgrenzung?
2. Unterscheidet sich nur die **Implementierung** (→ Application) oder die **Technologie** (→ neues Sheet)?
3. Liegt der neue Claim auf Ebene A (gilt ohne dieses Repo) oder B/C?
4. Welche Sheet-Fallstricke muss der neue Code bewusst behandeln?
5. Welche Method Note liefert den ersten Lab-Pfad?

## Geschwister-Produkte (gleiche Tech, anderer Produktzuschnitt)

Wenn zwei Repos dieselbe Tech nutzen, aber unterschiedlich zuschneiden (z. B. `esp32.rfmonitor` = Einzweck-RF vs. `esp32.toolnode` = RF-Modul in Modular-Firmware):

| Tun | Nicht |
|-----|--------|
| **Denselben** Sheet-Slug verwenden; `seen_in` erweitern | `rf-environment-monitor-toolnode` forken |
| In Applications den Zuschnitt kontrastieren (Einzweck vs. Modul, Flags, BLE an/aus) | Sheet in „unser Modulsystem“ umschreiben |
| A-Fallstricke nur generalisieren (z. B. shared radio) | Produktnamen als Spec |

Inventar-Match-Tabellen: Spalte **nicht** `Slug` nennen (Parser greift sonst) — besser `Ziel-Sheet`.

## Repo-Layout-Hinweise

| Layout | Typisch | Audit-Hinweis |
|--------|---------|---------------|
| PlatformIO `src/` | die meisten `esp32.*` | Pfade wie gewohnt |
| Arduino `.ino` Monolith | z. B. MeterMaster | Application-Pfade auf `.ino` + `docs/`; kein erzwungenes `src/` |
| Nur `docs/planung/` | planning-Profil | keine FW-Claims |

## Assistenz

```bash
# Fremdrepo: Bootstrap-Prompt inkl. Katalog bestehender Sheets
python3 tools/ta-assist prepare bootstrap https://github.com/ORG/REPO

# Danach: gezielt Sheet/Application/Evidence
python3 tools/ta-assist prompt new-tech-sheet --project <id> --slug <slug>
python3 tools/ta-assist prompt new-application --project <id> --slug <slug>
```

Der Bootstrap-Prompt verlangt explizit den Abgleich mit dem Sheet-Index (`{{existing_sheets}}`).

## Qualitätsmaß für „wiederverwendbar“

| Stufe | Bedeutung |
|-------|-----------|
| W1 | Sheet existiert, nur ein Kontext |
| W2 | Transfer-Abschnitt + Fallstricke nutzbar |
| W3 | ≥2 Projekte mit Application, A-Claims überlebt |
| W4+ | Multi-Host / Modulgrenze belegt |

„Ich starte ein neues Projekt“ → mindestens die **W2/W3-Sheets** im Index lesen und die Projektstart-Checkliste im jeweiligen Transfer-Abschnitt abarbeiten.
