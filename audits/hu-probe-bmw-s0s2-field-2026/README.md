# Audit Campaign: hu-probe-bmw-s0s2-field-2026

```yaml
id: hu-probe-bmw-s0s2-field-2026
project_id: hu-probe
started: 2026-10-15
ended: 2026-10-15
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: bmw-nbt-evo
prior_audit: msc-host-read-semantics-s1s2s3-2026
reuse_outcomes:
  reused:
    - bmw-nbt-evo
    - usb-msc
    - virtual-fat
    - esp32-s3-usb-wifi-coex
    - msc-host-read-semantics
    - msc-lba-timing-instrument
  new: []
  not_helped:
    - "PiDrive Prefetch≈15s / Eager / Cache als hu-probe-FACT — weiter INFERENCE."
    - "Burst-39 als Konstante — Histogramm widerspricht."
    - "MODE_SENSE6→STALL als HU-Recovery — Instrument-Artefakt (Fix 0.2.18)."
  process: "Feldnachzug S0 0.2.17 + S2 0.2.23 + Lab ram_offline; Transport-FACTs registrieren; Semantik bewusst offen; Profil-P1c nur skizziert (Upstream)."
  decisions_touched:
    - gap-as-measurement-not-hu-scheduler
    - read10-blocks-cbw-vs-event-chunk
    - ms6-cap-ratio-hu-after-stall-fix
    - burst-39-inference-only
    - lab-offline-not-bmw-offline
```

## Ziel

hu-probe-**Feld-/Lab-Messlage** 2026-10-15 (BMW NBT Evo S0+S2, Lab Offline)
in Evidence und Applications nachziehen — **Transport-FACTs** und epistemische
Korrekturen, **ohne** Prefetch/Eager/Cache/Burst-39 als hu-probe-`FACT`.
Pin: Upstream `hu-probe@5dbec43` · FW bis **0.2.23**.

## Scope

- **Im Scope:** S0-Feld 0.2.17 (Gap/BOT/SCSI); Offline-P0 (Burst-Def, STALL↔ms6,
  Mount→INQUIRY, TUR/QD); MODE_SENSE6-Pad 0.2.18; Lab `ram_offline` E2E 0.2.23;
  BMW Offline-FAIL; S2 Live 0.2.23 (8 Kern-Sessions); READ10-`blocks`-Verteilung;
  Gap-p50 als Messgröße vs. HU-Scheduler-INFERENCE; ms6/cap=2,0 nach Stall-Fix;
  Knowledge Feedback → hu-probe Applications + Inventar; Profil-P1c **Patch-Skizze**.
- **Nicht im Scope:** Upstream-Edit von `profiles/bmw_nbt_evo.json` (P1c bleibt
  offen im Quellrepo); S1 Eager-EOF (≥4 MiB); S3 Cache-Hit; formelle LBA-Semantik
  (P0b); Auto-Offline-Diagnose (P0c); WiFi-Root-Cause; Mazda; Wire-Claims;
  PiDrive→hu-probe Semantik-Übernahme.

```text
kill:
  - Prefetch≈15s / Eager / Cache als hu-probe-FACT ohne LBA+Marker-Formal
  - Burst-39 als Profil-Konstante
  - Gap/4096 blind als HU-Scheduler-Pace
  - MODE_SENSE6-Stalls als HU-Recovery
  - Lab Offline = BMW Offline
  - Wire-Claims
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1 · Kampagne + Evidence + Report | erfüllt |
| 2 | Primärquellen auf `hu-probe@5dbec43` + Session-/Feld-Docs | erfüllt |
| 3 | Transport-FACT-Tabelle S0↔S2 (Gap, BOT, Writes, dropped) | erfüllt |
| 4 | Epistemik: Gap/4096 Messgröße; READ10 blocks; ms6/cap HU; Burst/Prefetch INFERENCE | erfüllt |
| 5 | REJECTED: Burst-39 konstant · ms6-STALL = HU-Recovery | erfüllt |
| 6 | Lab ram_offline PASS ≠ BMW Offline FAIL dokumentiert | erfüllt |
| 7 | Applications `usb-msc` + `bmw-nbt-evo` (hu-probe) + Inventar | erfüllt |
| 8 | P1c nur Skizze — kein stilles Upstream-Profil-Edit | erfüllt |
| 9 | C10–C13 Lab/Field | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Gap-p50 ~3,7–3,8 ms als **Messgröße** FACT, nicht als HU-Scheduler | Ist S2-Gap ≈ S0 und ≈ FS-Bulk-Sättigung? | `001`–`003`, `008` | Ja Messgröße; Scheduler nur INFERENCE bis LBA/CBW | `DISCOVERED DURING TEST` |
| `read`-Event n=4096 ≠ blind „HU immer 4 KiB CBW“ | Was sagt READ10 `blocks`? | `004`, `008` | oft blocks=8 (=4096 B) **und** 240→30×4096 Chunks | `DISCOVERED DURING TEST` |
| ms6/cap=2,0 nach Stall-Fix = HU | Verschwindet Ratio mit ep_stall=0? | `005`, `006` | Nein — Ratio bleibt; Stalls waren Instrument | `DISCOVERED DURING TEST` |
| Burst-39 / Prefetch~15 s nicht in Profil-FACT | Reicht Histogramm + Marker-Lage? | `009`, `010` | Nein — INFERENCE; P1c darf sie nicht einziehen | `DISCOVERED DURING TEST` |
| Lab Offline freigibt kein Auto Offline | BMW ram_offline? | `007` | Nein — 1 FAIL; tcp_live bleibt Feldpfad | `DISCOVERED DURING TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`–`003` | Pace weiter über `gap_us` (nicht `t_us`-Monotonie in fragmentierten Sessions) | `KNOWN BEFORE TEST` (0.2.17) |
| `004`, `008` | Vor Profil-Update: READ10-`blocks`-Hist + Event-Chunk-Split dokumentieren | `DISCOVERED DURING TEST` |
| `005`–`006` | Nach MODE_SENSE6-Pad: ep_stall und ms6/cap getrennt werten | `DISCOVERED DURING TEST` |
| `009`–`010` | Marker nachgezogen ≠ Operator-Mikrozeit; Prefetch-Claim ohne LBA-Formal = INVALID | `DISCOVERED DURING TEST` |
| `007` | Lab-PASS nie als BMW-Offline-PASS in README/Ampel | `KNOWN BEFORE TEST` |

## Kill-Kriterien

**Hypothese:** S0/S2 liefern belastbare **Transport**-FACTs am NBT; Semantik bleibt
getrennt bis LBA/Marker-Formal.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Prefetch/Eager/Cache als hu-probe-`FACT` ohne Formalauswertung | Integritäts-Kill — vermieden |
| 2 | Burst-39 als Konstante ins Profil | Integritäts-Kill — vermieden (`009` REJECTED) |
| 3 | Gap/4096 blind als HU-Pace / Scheduler-FACT | Integritäts-Kill — vermieden |
| 4 | ms6-STALLs als HU-Recovery nach Fix behaupten | Integritäts-Kill — vermieden (`006`) |
| 5 | Lab Offline = BMW Offline | Integritäts-Kill — vermieden (`007`) |
| 6 | Wire-/Paketebene behauptet | Integritäts-Kill — vermieden |
| 7 | Mazda-Defaults still | Integritäts-Kill — vermieden |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| MSC Host-Read-Semantik | [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md) |
| LBA/Timing-Instrument | [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) |
| Trace-Korrelation | [`msc-trace-correlation`](../../methods/msc-trace-correlation.md) |

## Bezug Inventar

- Projekt: [`hu-probe`](../../projects/hu-probe/)
- Applications: [`usb-msc`](../../projects/hu-probe/applications/usb-msc.md) · [`bmw-nbt-evo`](../../projects/hu-probe/applications/bmw-nbt-evo.md)
- Sheets: [`usb-msc`](../../technologies/usb-msc/SHEET.md) · [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md)
- Prior: [`msc-host-read-semantics-s1s2s3-2026`](../msc-host-read-semantics-s1s2s3-2026/) · [`esp32-s3-usb-wifi-coexistence-2026`](../esp32-s3-usb-wifi-coexistence-2026/) · [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/)
- Upstream-Docs: `docs/feld/2026-10-15-uebergabe-abend-multi-ki.md`, `…-bmw-s2-0.2.23-auswertung.md`, `…-bmw-s0-0.2.17-auswertung.md`, `…-offline-p0.md`, `…-massnahmen-01d.md`

## Ergebnisse

| # | Artefakt | Ort |
|---|----------|-----|
| 1 | Evidence-Register | [`evidence.md`](evidence.md) |
| 2 | Kurzbericht | [`docs/reports/2026-10-15-hu-probe-bmw-s0s2-field.md`](../../docs/reports/2026-10-15-hu-probe-bmw-s0s2-field.md) |
| 3 | Applications | hu-probe `usb-msc` + `bmw-nbt-evo` |
| 4 | P1c Patch-Skizze | Evidence § Profil · FOLLOW-ON |

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| BMW S0 0.2.17 Transport | `001`–`002`, `006`, `009` | [`applications/bmw-nbt-evo.md`](../../projects/hu-probe/applications/bmw-nbt-evo.md) · [`usb-msc.md`](../../projects/hu-probe/applications/usb-msc.md) |
| BMW S2 0.2.23 Transport + CBW | `003`–`005`, `008`, `010` | dieselben Applications |
| Lab Offline / BMW Offline | `007` | Application usb-msc · FOLLOW-ON |
| Epistemik Gap/4096 | `008` | Method + FOLLOW-ON P1c (Upstream) |

Desk ≠ Lab ≠ Field. PiDrive-C bleibt in `projects/pidrive/applications/bmw-nbt-evo.md`.

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 Kill-Kriterien | PASS (Integritäts-Kills vermieden; Semantik-Kills weiter präregistriert) |
| C13 Knowledge Feedback | PASS → Applications + Method-Hinweis + FOLLOW-ON |

## Lessons → Transfer

- hu-probe bestätigt **NBT-Transportsignatur** unabhängig von PiDrive (Gap ~3,7–3,8 ms, 4 KiB-dominant Events, tinyusb-BOT, Writes=false).
- `read`-Event-Größe und READ10-`blocks` sind **zu trennen**; große CBWs werden im Stack gechunkt.
- MODE_SENSE6-Pad (0.2.18) entlarvt frühere Stalls als Instrument; **ms6/cap=2,0** bleibt Host-Muster.
- S2 Live ist für Transport brauchbar; Prefetch-Semantik braucht noch LBA/Marker-Formal (Messplan aus Vor-Audit).
- Profil-Update (P1c) nur mit `origin: hu_probe_field` und expliziter Messgröße vs. Hypothese.

## Offene Punkte nach Abschluss

- **P1c** Upstream `bmw_nbt_evo.json` (noch nicht aktualisiert)
- P0a Offline-Skript blocks/gap/LBA · P0b S2 Formalauswertung · P0c Auto-Offline
- S3 → S1 ≥4 MiB · GATE-01 · t_us-Regression (P1a) · Marker ohne WiFi
