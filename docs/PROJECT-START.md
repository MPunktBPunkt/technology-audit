# Neues Projekt starten (Wissensbasis nutzen)

Kurzpfad, wenn du **später auf diese Datenbank verweisen** willst — ohne alles lesen zu müssen.

## 90-Sekunden-Pfad

```text
1. technologies/README.md     → gibt es den Slug schon?
2. docs/REUSE.md Match-Fragen → Sheet wachsen oder neu?
3. docs/FAMILIES.md           → welche Produktfamilie / Nachbarn?
4. ta-assist prepare bootstrap <repo-url>
5. projects/<id>/ anlegen     → SCOPE + INVENTORY (Reuse-Tabelle!)
6. Sheets A nur erweitern     → Application B/C neu
```

Assistenz: `python3 tools/ta-assist prepare bootstrap https://github.com/…`

## Was du zitierst (für dich / Agenten)

| Brauchst du… | Nimm… |
|--------------|--------|
| „Kann ich X wiederverwenden?“ | Sheet A + Projektstart-Checkliste |
| „Wie hat Projekt Y es gemacht?“ | `projects/<id>/applications/<slug>.md` |
| „Ist das belegt?“ | `audits/…/evidence.md` |
| „Welches Profil / Exit-Tiefe?“ | [`AUDIT-PROFILES.md`](AUDIT-PROFILES.md) |
| „Welche Checks gelten?“ | [`REVIEW-CHECKS.md`](REVIEW-CHECKS.md) + `VERSION` |

**Nicht** die ganze KB in den Prompt kippen: Index → 1–3 Sheets → 1 Nachbar-Application.

## Sprache / Stack — spielt sie eine Rolle?

| Ebene | Rolle der Sprache |
|-------|-------------------|
| **A Technology Sheet** | **Nein** — Contract, Fallstricke, Abgrenzung sind stack-neutral |
| **B Application** | **Ja** — Pfade, Libs, Build (Arduino `.ino`, PlatformIO, Node `main.js`, …) |
| **C Evidence** | Quelle kann jede Sprache sein; Claim bleibt sprachneutral formulierbar |

Beispiel: `esp-hub-telemetry` gilt für C++-Nodes **und** den Node.js-Adapter — der **HTTP-Contract** ist A; `esp-hub-base.ino` vs. `main.js` sind Applications.

Tags wie `esp-idf` / `nodejs` / `iobroker` sind **Secondary**, keine eigenen Slugs.

## Damit wir uns zurechtfinden (Navigationsregeln)

1. **Ein Index:** [`technologies/README.md`](../technologies/README.md) — Einstieg immer hier.
2. **Familienkarte:** [`FAMILIES.md`](FAMILIES.md) — Hub-Familie vs. PiDrive vs. BLE-Training.
3. **Kein Sheet-Fork** bei Geschwistern — gleicher Slug, kontrastierende Apps ([REUSE](REUSE.md)).
4. **Schichten nicht mischen** — RF ≠ LAN ≠ ESP-NOW; Hub ≠ Simple-API ≠ Produkt-Adapter.
5. **Lag sichtbar:** `standard_version` + optional `standard_gaps` in Kampagnen.
6. **Observed ohne Sheet** ist ok** — nicht jedes Signal sofort A verdienen.

Sheet-Index ist **nach Primary gruppiert** (`technologies/README.md` + `index.yaml`). Nach Sheet-Änderungen:

```bash
python3 tools/ta-assist index && python3 tools/ta-assist check
```

Pflege-SoT: [`MAINTENANCE.md`](MAINTENANCE.md). FAMILIES weiter kurz halten.

## Checkliste „neues ESP-Hub-Node“

- [ ] Von [`esp-hub-base-template`](../technologies/esp-hub-base-template/SHEET.md) ableiten?
- [ ] Contract: [`esp-hub-telemetry`](../technologies/esp-hub-telemetry/SHEET.md) Checkliste
- [ ] Adapter-Fähigkeiten brauchen? [`iobroker-esp-hub-adapter`](../technologies/iobroker-esp-hub-adapter/SHEET.md)
- [ ] Web SSE? [`esp-embedded-web-sse`](../technologies/esp-embedded-web-sse/SHEET.md)
- [ ] Fach-Tech schon im Index? (RF, Lab, LAN, …)

## Checkliste „PiDrive / USB-MSC-Gadget“

- [ ] Ops vs. Firmware trennen: [`pidrive`](../projects/pidrive/) · [`esp32-pidrive`](../projects/esp32-pidrive/)
- [ ] [`usb-msc`](../technologies/usb-msc/SHEET.md) + Host [`bmw-nbt-evo`](../technologies/bmw-nbt-evo/SHEET.md)
- [ ] Control-Link? [`pump-control-link`](../technologies/pump-control-link/SHEET.md)
- [ ] Hub? [`esp-hub-telemetry`](../technologies/esp-hub-telemetry/SHEET.md) — Web ohne SSE bleibt observed
