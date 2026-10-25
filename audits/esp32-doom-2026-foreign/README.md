# Audit Campaign: esp32-doom-2026-foreign

```yaml
id: esp32-doom-2026-foreign
project_id: esp32-doom
started: 2026-10-25
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "085f21b630f11adb69a3894db5a1efa39a7aa31a"
reuse_outcomes:
  reused: [esp32-s3-silicon, ssd1306-oled-ui]
  new: [esp-psram-heavy-port]
  not_helped: []
  process: "Desk historical PoC; Classic PSRAM heap ≠ S3 sheet; FB internal nuance"
```

## Ziel

[espressif/esp32-doom](https://github.com/espressif/esp32-doom) als Fremd-Upstream für **PSRAM-pflichtige schwere Ports** (PrBoom + SPI-LCD + WAD-mmap) — mit klarer Internal-vs-PSRAM-Nuance und Chip-Gate Classic ≠ S3.

## Scope

[SCOPE](../../projects/esp32-doom/SCOPE.md) — Desk; unsupported PoC 2017.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | standard 0.7.1 + lab-tool + Commit-Pin | erfüllt |
| 2 | Sheet `esp-psram-heavy-port` + App; Kontrast S3/OLED | erfüllt |
| 3 | Grok: PSRAM + schwere Grafik/Logik + PrBoom erfasst | erfüllt |
| 4 | FB-internal vs PSRAM-heap Evidence | erfüllt |
| 5 | C10–C12; C13 n/a | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-25) |
| 7 | Lab FPS | offen |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neues Sheet vs nur `esp32-s3-silicon`? | Classic Wrover? | `…-001` | Neu — anderes Silicon | KNOWN BEFORE TEST |
| Alles PSRAM? | Wo liegt FB? | `…-003` | Nein — internal FB | DISCOVERED DURING TEST |
| OLED-Reuse? | Game vs Status UI | — | Kontrast only | KNOWN BEFORE TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-DOOM-2026-10-25-001` | Ohne PSRAM-Hardware = Gate | KNOWN BEFORE TEST |
| `EVID-DOOM-2026-10-25-003` | DMA/FB Caps ≠ SPIRAM-Heap Caps | DISCOVERED DURING TEST |
| `EVID-DOOM-2026-10-25-002` | Historische SPIRAM-Kconfig ≠ moderne IDF still | KNOWN BEFORE TEST |
| `EVID-DOOM-2026-10-25-005` | Unsupported/Feature-Gaps nicht als Produkt-FACT | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** PoC belegt PSRAM-pflichtigen Heavy-Port mit messbarer Architektur.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Läuft ohne PSRAM laut Upstream | nicht eingetreten |
| 2 | Kein Grafik-/Engine-Pfad | nicht eingetreten |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-PoC; FPS UNKNOWN ≠ STOP. Historischer IDF-Lag dokumentiert.
```

## Lessons → Transfer

- „Braucht PSRAM“ ≠ „Framebuffer in PSRAM“.
- Classic Heavy-Port-Lessons nicht still auf S3-Errata-Sheet schreiben.
- Historische PoCs: Commit-Alter und unsupported-Status in SCOPE halten.

## Bezug

[INVENTORY](../../projects/esp32-doom/INVENTORY.md) · [evidence](evidence.md)
