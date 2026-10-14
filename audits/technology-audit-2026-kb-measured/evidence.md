# Evidence — technology-audit-2026-kb-measured

Meta-Desk 2026-10-14 · **standard_version 0.7.1** · Profile `ops-field` ·
Snapshot der KB bei Commit `5fab7f5` (danach nur Meta-Artefakte). Keine neuen
Lab-/Feldmessungen; Zähler aus Repo-Scan.

## Quellen-Snapshots

| Quelle | Pin / Stand | Rolle |
|--------|-------------|-------|
| Dieses Repo `technology-audit` | `5fab7f5` (+ Meta-Dateien) | Evidence-, Sheet-, Audit-Corpus |
| [`docs/DOCUMENT-STANDARD.md`](../../docs/DOCUMENT-STANDARD.md) Epistemic | 0.7.1 | Statusdefinitionen |
| PiDrive Upstream-Artefakte (via Links) | in MEASURED-Zeilen der HU/MSC-Kampagnen | Feld/Lab-Rohdaten (nicht hier gespiegelt) |

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-KBMEAS-2026-10-14-001` | Im Corpus gibt es **~28 unique** Evidence-IDs mit Status `MEASURED` (Rohvorkommen ~36 inkl. bewusster Doppel-Listung USBMSC in MSC+HU). | `FACT` | Scan `audits/*/evidence.md` 2026-10-14 |
| `EVID-KBMEAS-2026-10-14-002` | MEASURED-Cluster **PiDrive/HU**: Prefetch/Burst, Seed/`bytesServed`, C′, Lab≠Feld-Ohr, Busy-Pacing ~65 s vs. Stall-off ~6 s, Menü-Trägheit — IDs `EVID-USBMSC-2026-10-04-*`, `EVID-BMWHU-2026-10-05-*`, `EVID-BMWHU-2026-10-12-*`; Artefakte unter `pidrive/docs/betrieb/artifacts-*`. | `FACT` | [`pidrive-2026-bmw-hu/evidence.md`](../pidrive-2026-bmw-hu/evidence.md), [`pidrive-2026-msc/evidence.md`](../pidrive-2026-msc/evidence.md) |
| `EVID-KBMEAS-2026-10-14-003` | MEASURED-Cluster **Ergo/FTMS/HR**: Varon Caps/Resistance/Advertising, Probe-Scan, Polar H9 — IDs `EVID-FTMS-*`, `EVID-VARON-*`, `EVID-PROBE-*`, `EVID-HRM-*`, `EVID-RELAY-*`; Quellen Geräteprofil/Ergebnisbericht/README. | `FACT` | ergo / ftmsprobe / heartrate `evidence.md` |
| `EVID-KBMEAS-2026-10-14-004` | Epistemik-Skala im Repo: grob **~383× `FACT`**, **~36× `MEASURED`-Vorkommen**, **~110× `UNKNOWN`**, **~27× `INFERRED`**, **~20× `REJECTED`**, **~5× `HYPOTHESIS`** in Evidence-Dateien — Desk-`FACT` dominiert zahlenmäßig. | `FACT` | Status-Token-Scan 2026-10-14 |
| `EVID-KBMEAS-2026-10-14-005` | Kampagnenlage: **~50 active** vs. **~7 closed**; Profile stark **lab-tool** (Desk-Fremd). PILOT-Info warnt vor evidence-update vor neuen Pilots. MEASURED steckt vor allem in ops-field/firmware-Pilots, nicht im Desk-Boom. | `FACT` | `audits/*/README.md` YAML; `ta-assist check` Info |
| `EVID-KBMEAS-2026-10-14-006` | Sheet-`field_evidence`: **49× R0**, **1× R3** (`bmw-nbt-evo`). Application-`field_evidence` ≥ R3: **10** Dateien (pidrive usb-msc/bmw-nbt-evo, ergo/ftmsprobe/heartrate FTMS/HR-Apps). Pattern: Feldreife in Apps, nicht in A-Sheets — regelkonform. | `FACT` | Scan SHEET.md / applications |
| `EVID-KBMEAS-2026-10-14-007` | Härtegradient: PiDrive-MEASURED verlinken Gesamtberichte/Feldordner; Teile der Heartrate-MEASURED stützen sich primär auf README-„Getestet“ / Config — schwächer als Trace-Artefakte (PL2-Risiko). | `FACT` / `INFERRED` | Stichprobe heartrate vs. BMWHU evidence |
| `EVID-KBMEAS-2026-10-14-008` | Epistemik-Hygiene Stichprobe HU/MSC/usb-msc Sheet: Host-Timing und Busy-Akzeptanz als **C**/`MEASURED` oder Verweis; Sheet A hält REJECTED gegen Spec→Host-Transfer; Desk≠Lab≠Field in Kampagnen dokumentiert. Kein Beleg, dass S6-Zahlen als usb-msc-A-FACT geführt werden. | `FACT` | Sheet `usb-msc`/`bmw-nbt-evo`; Apps pidrive |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „Kaum gemessen — KB nur Desk“ | `REJECTED` | Cluster `002`/`003` |
| „50 Sheets = 50 Feldreife“ | `REJECTED` | Sheet-R0 korrekt (`006`) |
| „Viele FACT = viele Messungen“ | `REJECTED` | FACT≃Desk/Code (`004`) |
| „Meta-Scan = neue Feldmessung“ | `REJECTED` | Scope |
| „Alle MEASURED gleich belastbar“ | `REJECTED` | Härtegradient `007` |

## MEASURED-Kernkarte (unique IDs, Kurz)

| Cluster | Prefix / IDs | Charakter |
|---------|--------------|-----------|
| MSC Host Reads / Seed | `USBMSC-2026-10-04-001`–`006` | Feld+Lab Artefakte |
| HU Oracle / Menü / Lock | `BMWHU-2026-10-05-001`–`005` | Feld+Lab |
| Busy-Pacing S6 | `BMWHU-2026-10-12-001`–`003`, `006`, `007` | Feld; Desk-BUSY validiert |
| FTMS / Varon | `FTMS-*`, `VARON-*`, `PROBE-*` | Lab/Geräteprofil |
| HR / Relay | `HRM-*`, `RELAY-*` | Lab/README-Mix |
| Neben | `WEB-*`, `HUB-*` (ergo) | Build/Partition — schwach „Messung“ |

Vollständige Claims: jeweilige `evidence.md` der Quellkampagnen.

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| Zentraler MEASURED-Ledger existiert | `UNKNOWN` → Follow-on | neues Artefakt |
| Anzahl desk-complete Closable ohne Inhaltsverlust | `UNKNOWN` | Batch-Review active audits |
| Heartrate-MEASURED nach PL2 härtbar | `HYPOTHESIS` | Rohlogs oder Downgrade |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-04…12 | PiDrive Lab/Feld → USBMSC/BMWHU MEASURED |
| 2026-10-08…09 | Heartrate / Ergo / FTMS-Probe MEASURED |
| 2026-10-13…14 | Starker Desk-Fremd-Boom (FACT↑, MEASURED unverändert) |
| 2026-10-14 | Meta-Audit KB-MEASURED closed |
