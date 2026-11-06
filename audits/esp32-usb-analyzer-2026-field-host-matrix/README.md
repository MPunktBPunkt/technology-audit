# Audit Campaign: esp32-usb-analyzer-2026-field-host-matrix

```yaml
id: esp32-usb-analyzer-2026-field-host-matrix
project_id: esp32-usb-analyzer
started: 2026-11-06
ended: 2026-11-06
status: closed
reviewed_commit: 688a40b
profile: lab-tool
standard_version: "0.7.1"
prior_audit: esp32-usb-analyzer-2026-0.0.50
upstream_pin:
  repo: https://github.com/MPunktBPunkt/esp32.usb-analyzer
  commit: "688a40b"
  fw_version: "0.0.52"
  evidence_claim: "field_host_matrix_analyzer_msc_gadget_2026_11_06"
reuse_outcomes:
  reused: [usb-msc, usb-aoa, bmw-nbt-evo, usb-bot-command-observation]
  new: [usb-msc-host-behaviour, usb-msc-host-fingerprint]
  process: "Evidence-Update only — kein Full Technology-Audit; Feldmatrix 688a40b → Sheets/Apps"
  decisions_touched:
    - evidence-not-full-audit
    - host-fingerprint-as-reusable-knowledge
    - aoa-not-implied-by-msc-identity
    - write-cache-eviction-unknown
  cycles_avoided:
    - third-full-usb-system-audit
    - generalizing-tv-soundbar-fritz-to-host-classes
    - claiming-windows-write-data-loss-without-lba-audit
```

## Ziel

Die Feldmatrix vom 2026-11-06 (Upstream `688a40b`, Analyzer MSC Gadget **0.0.52**) als
**Evidence-Update** in die KB holen — Wissensstand erhöhen, nicht den Projektstand
wiederholen. Fokus: drei wiederverwendbare Themen, kein Full Audit.

## Scope

**Im Scope**

1. **USB MSC Host Behaviour / Fingerprinting** — neues Sheet + Method; Dimensionen + Claim-Grenzen
2. **BMW NBT Evo MSC / P-MOUNT** — Evidence-Update (`MODE_SENSE(6)`, `PREVENT/ALLOW` am F20)
3. **AOA vs. MSC Identity Gate** — FACT/INFERENCE/UNKNOWN sauber trennen

**Nicht im Scope**

- Vollständiges Technology-Audit wie Pilot / 0.0.50
- Neues USB-Protokoll-Audit (AOA/BCL/Etch) — erst nach C1-Positiv
- Host-Klassen aus TV / Soundbar / FRITZ!Box generalisieren (Project Evidence only)
- Windows Write-Cache-Eviction als FACT (bleibt UNKNOWN / Test Gap)
- Path-B / Live-L0 / transparent MITM

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Sheet `usb-msc-host-behaviour` + Method `usb-msc-host-fingerprint` | erfüllt |
| 2 | Evidence-IDs auf Upstream Feldmatrix @ `688a40b` | erfüllt |
| 3 | BMW P-MOUNT / Soft-Reenum in `bmw-nbt-evo` + Analyzer-App | erfüllt |
| 4 | AOA-Gate FACT/INFERENCE/UNKNOWN in `usb-aoa` + Apps | erfüllt |
| 5 | Write-Cache Eviction als UNKNOWN / Test Gap dokumentiert | erfüllt |
| 6 | TV/Soundbar/FRITZ nicht als GENERAL Host-Klassen claimen | erfüllt |
| 7 | `ta-assist check` grün | erfüllt |
| 8 | Full USB-System-Reaudit | bewusst **nicht** |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Full Audit jetzt? | Neue Tech-Felder oder nur Evidence-Maxima? | Matrix + Reviews | **Nein** — Evidence-Update | KNOWN BEFORE TEST |
| Neues Sheet Host-Behaviour? | Wiederverwendbare Dimensionen jenseits Device-MSC? | `001`–`007` | **Ja** | DISCOVERED DURING TEST |
| TV/Soundbar/FRITZ → Tech-FACT? | n≥3 / Klassen stabil? | `005` | **Nein** — Project Evidence | KNOWN BEFORE TEST |
| AOA=0 ⇒ HU kann kein AOA? | Identity vs Capability | `008`/`009` | **REJECTED** als Capability-Claim | DISCOVERED DURING TEST |
| 106 Sektoren vs 64 Cache = Loch? | Eviction gemessen? | `010` | **UNKNOWN** / Test Gap | DISCOVERED AFTER TEST |
| Nächster Full Audit wann? | AOA/BCL-Übergang C1? | Follow-on | Nach C1-Positiv | KNOWN BEFORE TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001`–`004` | Fingerprint nur mit dokumentierter Identity+Content; Pattern-Stick ≠ FAT-Media | KNOWN BEFORE TEST |
| `006`/`007` | MODE_SENSE6/PREVENT am NBT nicht als Spec-Default, sondern als Feld-FACT führen | DISCOVERED DURING TEST |
| `008`/`009` | AOA=0 nur unter MSC-Identity `303a:1001` claimen — nicht „Host ohne AOA“ | DISCOVERED DURING TEST |
| `010` | Kein „Datenloch“-Claim ohne Write-LBA-Audit / Evict-Counter | DISCOVERED AFTER TEST |
| `005` | Consumer-Hosts nicht zu GENERAL-Klassen aufblasen | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese H1:** Responding MSC-Endpoint unter Lab-Identity reicht für BMW AOA-Initiation.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Mount + SCSI-Traffic, aber `aoa51/52/53=0` unter `303a:1001` | **Kill getroffen** (`008`) |

**Hypothese H2:** Windows Write-Bytes > Cache-Slots beweist Datenverlust.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Ohne LBA-/Evict-Audit als FACT geführt | Integritäts-Kill — als `UNKNOWN` belassen (`010`) |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| **USB MSC Host Fingerprint** | [`usb-msc-host-fingerprint`](../../methods/usb-msc-host-fingerprint.md) |
| BOT Command Observation | [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md) |

## Bezug Inventar

[INVENTORY](../../projects/esp32-usb-analyzer/INVENTORY.md) · [evidence](evidence.md) ·
Prior Soft-Lab: [`esp32-usb-analyzer-2026-0.0.50`](../esp32-usb-analyzer-2026-0.0.50/) ·
AOA Desk: [`usb-aoa-bmw-connected-2026-desk`](../usb-aoa-bmw-connected-2026-desk/)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Fingerprint-Dimensionen + Matrix | `001`–`005` | Sheet `usb-msc-host-behaviour` · App · Method |
| BMW P-MOUNT / Soft-Reenum | `006`/`007` | `bmw-nbt-evo` Sheet/App · Analyzer App |
| AOA vs MSC Identity | `008`/`009` | `usb-aoa` Sheet · Analyzer/hu-probe Apps |
| Write-Cache Test Gap | `010` | App usb-msc / FOLLOW-ON (UNKNOWN) |

## Ergebnisse

| Artefakt | Pfad |
|----------|------|
| Neu | `usb-msc-host-behaviour`, Method `usb-msc-host-fingerprint` |
| Gewachsen | `usb-aoa`, `bmw-nbt-evo`, Analyzer Apps `usb-msc` / `usb-aoa` |
| Upstream | [Feldbericht](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/reports/2026-11-06-field-host-matrix.md) · [MEASURED](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/LAB_FIELD_HOST_MATRIX_2026-11-06_MEASURED.md) |

## Lessons → Transfer

- Evidence-Update ≠ Full Audit: Evidence-Maxima erhöhen, Tech-Slugs nur bei echtem Transferbedarf.
- Host-Fingerprint ist wiederverwendbar; Host-**Klassen** noch nicht.
- MSC-Identity `303a:1001` ist Storage-Probe, nicht Connected-Apps-Probe.
- Nächster großer Audit: nach C1 (AOA identity) → BCL → Etch Übergang.

## Offene Punkte nach Abschluss

- **P0 C0:** gleiche Identity + echtes FAT/Media (Identity vs Content)
- **P0 C1:** hu-probe `aoa_phone_like` / `aoa_observe` am Analyzer — dann Full Audit prüfen
- **P0:** SCSI Aggregate Counters + Write-LBA-Audit (Upstream Software)
- Write-Cache Eviction (`010`) bleibt UNKNOWN bis Audit
