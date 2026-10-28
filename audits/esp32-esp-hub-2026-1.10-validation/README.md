# Audit Campaign: esp32-esp-hub-2026-1.10-validation

```yaml
id: esp32-esp-hub-2026-1.10-validation
project_id: esp32-esp-hub
started: 2026-10-28
ended: 2026-10-28
status: closed
profile: firmware
standard_version: "0.7.1"
standard_gaps: []
prior_audit: esp32-esp-hub-2026-pilot
reviewed_commit: eebbcd9
upstream_pin:
  repo: https://github.com/MPunktBPunkt/ESP32.esp-hub
  commit: "eebbcd9"
  fw_version: "1.10.5"
  baseline_freeze_fw: "1.8.0"
reuse_outcomes:
  reused:
    - esp-hub-base-template
    - esp-hub-telemetry
    - esp-embedded-web-sse
  new: []
  not_helped:
    - "Monolith-.ino allein als Ableitungsvorlage (ab 1.9 Ordner + src/core/)"
    - "Diag/Recovery still in Derived A/B nachziehen"
  process: "Pilot 1.7.0 @ a03400a / 0.6.3 → Revalidation Base 1.10.5 (M0–M11 + gzip UI + Derived A/B Freeze) unter 0.7.1."
  decisions_touched:
    - fact-appcore-template-zones
    - fact-heartbeat-slim-compat-1.8
    - fact-hub-reply-interval-otaurl-name
    - fact-gzip-progmem-webui
    - reject-diag-as-ab-mandatory
    - fact-derived-ab-rollout-reuse
```

## Ziel

Revalidation von `ESP32.esp-hub` nach Plattform-Umbau **1.7.0 → 1.10.5** (AppCore, M0–M11, OTA-Lifecycle, BaseModule, gzip Web-UI) und dokumentiertem Derived-A/B-Rollout. Sheets/Apps/Evidence auf Pin `eebbcd9` unter **Audit-Standard 0.7.1**; Pilot schließen.

## Scope

Siehe [SCOPE](../../projects/esp32-esp-hub/SCOPE.md).

- **Im Scope:** `esp-hub-base/` (ProjectConfig, `.ino`-Zonen, `src/core/`), Heartbeat-/Reply-Contract, Status/SSE + gzip-UI, Ableiten-Pfad, Upstream A/B-Freeze + ROLLOUT.
- **Nicht im Scope:** ioBroker-Adapter-Internals; Stufe C/D Diag/Recovery in Derived; pidrive/hu-probe Produktlogik; Security-/Memory-Deep-Dive; physischer BOOT-3s-Reset.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Kampagne `standard_version: "0.7.1"` + Pin `eebbcd9` / FW 1.10.5 + Reuse-Outcomes | erfüllt |
| 2 | Sheet `esp-hub-base-template` um AppCore/Ableiten/A/B-Grenze gewachsen | erfüllt |
| 3 | Sheets `esp-hub-telemetry` + `esp-embedded-web-sse` additive Contract-/Pack-Fakten | erfüllt |
| 4 | Applications + Evidence auf `eebbcd9` / FW 1.10.5 | erfüllt |
| 5 | Ableiten-Checkliste (Sheet + README) geschlossen; Bootstrap-Prompt → FOLLOW-ON | erfüllt (Sheet); Bootstrap offen |
| 6 | `python3 tools/ta-assist check` 0 errors | erfüllt (lokal) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Vorlage = Ordner `esp-hub-base/` + `ProjectConfig.h` / `.ino`-Zonen; `src/core/` Plattform | Monolith-`.ino` noch SoT? | `EVID-BASE-2026-10-28-001` | Sheet: Ableiten-Zonen; Application-Pfade | `KNOWN BEFORE TEST` (README) |
| Heartbeat bleibt schlank; 1.8-Vertrag + additive Keys | Brechen `freePsram`/CPU den Basis-Contract? | `EVID-HUB-2026-10-28-001` · `EVID-HUB-2026-10-28-003` | Contract-Sheet wächst additiv; Diag ≠ Register | `KNOWN BEFORE TEST` |
| Hub-Reply nur `interval` / `otaUrl` / `name` | Rename über Reply? | `EVID-HUB-2026-10-28-002` | Application + Fallstrick Rename/NVS | `KNOWN BEFORE TEST` / Lab Upstream |
| gzip-PROGMEM (Ergo-Weg) Familienstandard | B64-PROGMEM noch Vorbild? | `EVID-WEB-2026-10-28-001` | Web-Sheet: Pack-Pipeline | `KNOWN BEFORE TEST` |
| Derived A/B ohne Diag/Recovery-Vendor | Base-only still nachziehen? | `EVID-BASE-2026-10-28-003` · `EVID-BASE-2026-10-28-004` | `REJECTED` als A/B-Pflicht; Stufe C/D Gate | `DISCOVERED DURING TEST` (Upstream A/B-Audit) |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-BASE-2026-10-28-001` | Ableitung: `ProjectConfig.h` + `.ino`-Zonen; `src/core/` nicht für Features umbauen | `RETROFIT` |
| `EVID-HUB-2026-10-28-001` | Heartbeat bleibt Basis-Keys + optionale Additive; keine Diag-Payload im Register | `KNOWN BEFORE TEST` |
| `EVID-HUB-2026-10-28-002` | Client konsumiert `interval`/`otaUrl`/`name` sofort; `otaUrl` einmalig | `RETROFIT` |
| `EVID-WEB-2026-10-28-001` | UI-Änderung → `pack_ui.py` → `UiPagesGz.h` committen; `Content-Encoding: gzip` | `RETROFIT` |
| `EVID-BASE-2026-10-28-004` | Derived A/B: HI/CpuLoad sync; Diag/Recovery nicht still kopieren | `DISCOVERED DURING TEST` |

## Kill-Kriterien

**Hypothese:** Base 1.10.5 ist als Familienstandard ableitbar, ohne Hub-Basisvertrag (interval/otaUrl/name + schlanker Heartbeat) zu brechen.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Ableitung erfordert Umbau von `src/core/` für Minimal-Node | `REJECTED` (Doku/Struktur) |
| 2 | Heartbeat-Additive ersetzen `mac`/`name`/`hwType`/`ios` | `REJECTED` (Contract) |
| 3 | A/B-Rollout ohne Labor-Smoke als End-to-End-Feld-FACT verkauft | Gate — Upstream Lab zitiert; kein neues Field hier |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk + Upstream-Lab belegen Template/Contract/A/B-Freeze; physischer BOOT-3s und Adapter-Deep-Dive sind bewusst out-of-scope — nicht als „kein Test nötig“ lesen.
```

## Bezug Inventar

Priorisierte Slugs:

- `esp-hub-base-template` — Coverage partial→stärker (AppCore/Ableiten)
- `esp-hub-telemetry` — additive Keys + Reply-`name`
- `esp-embedded-web-sse` — gzip-Pack + SSE weiter

## Ergebnisse

- [evidence](evidence.md)
- [INVENTORY](../../projects/esp32-esp-hub/INVENTORY.md)
- Sheets: [`esp-hub-base-template`](../../technologies/esp-hub-base-template/SHEET.md) · [`esp-hub-telemetry`](../../technologies/esp-hub-telemetry/SHEET.md) · [`esp-embedded-web-sse`](../../technologies/esp-embedded-web-sse/SHEET.md)
- Upstream: [docs/update/](https://github.com/MPunktBPunkt/ESP32.esp-hub/tree/eebbcd9/docs/update) · [AUDIT_BASE_A-B](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/docs/update/AUDIT_BASE_A-B_2026-10-27.md) · [ROLLOUT_DERIVED](https://github.com/MPunktBPunkt/ESP32.esp-hub/blob/eebbcd9/docs/update/ROLLOUT_DERIVED.md)
- Prior: [`esp32-esp-hub-2026-pilot`](../esp32-esp-hub-2026-pilot/)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Upstream Lab A/B 2026-10-27 (zitiert) | `EVID-BASE-2026-10-28-003` | `applications/esp-hub-base-template.md` |
| Desk Contract/UI @ `eebbcd9` | `EVID-HUB-2026-10-28-*` · `EVID-WEB-2026-10-28-*` | Hub-/Web-Applications + Sheets |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact. Lab-Claims hier nur über Upstream-Evidence-IDs/Dokumente.

## Retro-Impact (Revalidation)

| Spätere Erkenntnis | Früherer Review Check | Betroffene Entscheidung | Potenziell vermeidbarer Umweg | Evidence-Basis | Counterfactual-Unsicherheit |
|--------------------|----------------------|-------------------------|-------------------------------|----------------|------------------------------|
| Vorlage ist Ordner+Core, nicht Einzel-`.ino` | Pilot kanonisierte Monolith-Pfad | Ableiten-/Bootstrap-Checkliste | Node-Repos nach altem Layout kopieren | `EVID-BASE-2026-10-28-001` | niedrig |
| gzip-PROGMEM statt B64 als Familienweg | Web-Sheet nur „gepackte Seiten“ | UI-Pack in Ableitungen | Inkonsistente UI-Einbettung | `EVID-WEB-2026-10-28-001` | mittel |

## Lessons → Transfer

- Familienstandard = unveränderte Plattform (`src/core/`) + markierte Ableiten-Zonen + syncbare HI/CpuLoad-Kopien.
- Heartbeat additiv wachsen lassen; Diagnose bleibt Base-only bis Stufe C/D.
- Derived-Rollout ist der Reuse-Beweis für `esp-hub-base-template` (W4).

## Offene Punkte nach Abschluss

- Bootstrap-Prompt (`ta-assist prepare bootstrap`) Ableiten-Checkliste nachziehen
- BOOT 3 s WLAN-Reset manuell an Base
- MeterMaster optional Hub-`interval`/`otaUrl`; Ergo `HwInfo`→`HardwareInfo`
- Adapter-Kampagne `iobroker-esp-hub` separat nachziehen (0.5.x / Rename)
