# Audit Campaign: esp32-usb-analyzer-2026-pilot

```yaml
id: esp32-usb-analyzer-2026-pilot
project_id: esp32-usb-analyzer
started: 2026-10-31
ended: null
status: active
reviewed_commit: b2c9987
profile: lab-tool
standard_version: "0.7.1"
reuse_outcomes:
  reused: [usb-msc, esp-usb-host, usb-aoa, bmw-bcl, esp32-s3-usb-wifi-coex, esp32-s3-silicon, esp-hub-telemetry]
  new: [usb-dual-esp-observe-proxy]
  process: "bootstrap + Lab MEASURED import; Gate claim boundaries preserved"
  decisions_touched: [otg-loop-baseline, aoa-lab-not-hu, wifi-bottleneck-mode-a]
  cycles_avoided: [pattern-fail-as-usb-loss-false-positive]
```

## Ziel

Lab-Instrument und Messungen (MSC/TCP/AOA/BCL-Framing/Enum/HID) in die Wissensbasis holen; bestehende USB-/S3-Sheets mit Lab-Evidence wachsen lassen; Dual-ESP Observe/Proxy als wiederverwendbares Pattern + Method verankern — **ohne** transparente MITM- oder HU-Wire-Claims.

## Scope

Siehe [SCOPE.md](../../projects/esp32-usb-analyzer/SCOPE.md). Upstream FW **0.0.35** @ `b2c9987`. Messungen: OTG-Loop `.88`↔`.89` + WiFi TCP (2026-10-31).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SCOPE + INVENTORY mit Match auf bestehende Slugs | erfüllt |
| 2 | Evidence-IDs auf Upstream `docs/evidence/*` | erfüllt |
| 3 | Method `usb-otg-loop-baseline` | erfüllt |
| 4 | Sheet `usb-dual-esp-observe-proxy` + Kern-Applications | erfüllt |
| 5 | `usb-msc` / `esp-usb-host` / `usb-aoa` / Coex `seen_in` + Apps | erfüllt |
| 6 | `ta-assist check` grün | erfüllt (0 Errors, 2026-10-31) |
| 7 | Observer-effect / transparent MITM Baseline | offen (Gate 4) |
| 8 | HU/Feld-Lauf AOA oder MSC | bewusst deferred |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| OTG-Loop als Integrity-Baseline | Pattern-fail = USB-Verlust? | `EVID-USBA-2026-10-31-004` | Nein — Gadget multi-LBA Fill-Bug; Re-Run autoritativ | DISCOVERED DURING TEST |
| Mode-A USB-over-WiFi für Bulk | TCP ≥ USB MSC Nutzrate? | `EVID-USBA-2026-10-31-001`/`003` | Nein heute — WiFi Bottleneck; SF/window nötig | MEASURED |
| AOA Lab = HU Connected? | 51→53 OTG-Loop ⇒ HU? | `EVID-USBA-2026-10-31-006` | REJECTED — Lab only | KNOWN BEFORE TEST |
| BCL Lab-Framing = HU Wire? | Echo HANDSHAKE ⇒ Connected? | `EVID-USBA-2026-10-31-009` | REJECTED | KNOWN BEFORE TEST |
| Gate-Badge vs GATES.md Pointer | Welcher Gate-Status gilt? | Upstream Drift | README/GATE7 = Timeline-Slice; transparente MITM offen | DISCOVERED DURING TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `EVID-USBA-2026-10-31-004` | Multi-LBA Device-Fill muss alle Sektoren eines Callbacks füllen; `pattern_ok=false` nicht als PHY-Fehler lesen | DISCOVERED DURING TEST |
| `EVID-USBA-2026-10-31-012` | Capture `source` taggen: `class_api_inferred` ≠ `class_hook_mscd_xfer` ≠ wire | KNOWN BEFORE TEST |
| `EVID-USBA-2026-10-31-013` | MSC-proxy byte-exact ≠ transparent MITM; MITM-Wiring (DUT vs OTG-Loop) prüfen | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese H1:** Dual-ESP OTG-Loop liefert bit-integre MSC READ/WRITE unter Lab-Last.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Pattern-fail Bytes > 0 nach Device-Fill-Fix bei chunk≤8, clean LBA | nicht eingetreten (`EVID-USBA-2026-10-31-001`) |
| 2 | Host sieht kein DUT / kein FS Enum trotz Verkabelung | nicht eingetreten |

**Hypothese H2:** WiFi Mode-A ACK-each reicht für USB-MSC Nutzrate.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Peak TCP ≪ Peak USB MSC (~0.14 vs ~0.93 MB/s) | **Kill getroffen** — Bottleneck bestätigt |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| OTG-Loop Baseline Campaign | [`usb-otg-loop-baseline`](../../methods/usb-otg-loop-baseline.md) |
| BOT Command Observation (Kontrast) | [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md) |
| USB↔WiFi Discrimination (Kontrast) | [`usb-wifi-coex-discrimination`](../../methods/usb-wifi-coex-discrimination.md) |

## Bezug Inventar

[INVENTORY](../../projects/esp32-usb-analyzer/INVENTORY.md) · [evidence](evidence.md)

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Neu | `usb-dual-esp-observe-proxy`, Method `usb-otg-loop-baseline` |
| Gewachsen | `usb-msc`, `esp-usb-host`, `usb-aoa`, `bmw-bcl`, Coex/Silicon/Hub Applications |
| Upstream Evidence | `docs/evidence/LAB_*_MEASURED.md` @ `b2c9987` |

## Lessons → Transfer

- OTG-Loop MSC Integrity-clean ≈ **0.93 MB/s** READ / **0.25–0.46 MB/s** WRITE — Stack, nicht Wire-Rate.
- Mode-A WiFi ≪ USB-Kabel → Proxy-Claims und SF-Gates trennen.
- AOA Lab A/B + Bulk-Echo bestätigen Desk-`usb-aoa`; HU bleibt getrennt.
- Capture-Source-Tags verhindern App-Fiction als Wire-FACT.
- Früherer `pattern_ok=false` war Gadget-Bug — Audit-Hygiene dokumentieren.

## Offene Punkte nach Abschluss

- Exit 6: `ta-assist check` nach Index
- Exit 7/8: transparent MITM / HU deferred
- Upstream `docs/GATES.md` „Current pointer“ vs Gate-7 Badge — Doc-Drift notieren (kein Auto-Fix im Fremdrepo)
