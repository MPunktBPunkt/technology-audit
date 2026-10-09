# Audit Campaign: pidrive-2026-msc

```yaml
id: pidrive-2026-msc
project_id: pidrive
started: 2026-10-04
ended: 2026-10-05
profile: ops-field
standard_version: "0.5.0"
standard_gaps: [reuse-playbook, audit-profiles, sheet-checklists, standard_version-field]
status: closed
pilot: 1
next_pilots: [bmw-nbt-evo, avrcp]
successor: pidrive-2026-bmw-hu
```

## Ziel

USB-MSC als **ersten vollständigen Pilot** durch das technology-audit-Framework laufen lassen (Schema-Validation): Sheet → Application → Evidence → Maturity → Lessons — mit harter **A/B/C**-Trennung (Spec vs. PiDrive-Impl vs. BMW-HU).

## Scope

- Im Scope: `usb-msc` Technology Sheet; PiDrive Application; Evidence-IDs auf bestehende Lab/Feld-Artefakte; Reifegrade.
- Nicht im Scope: vollständige Sheets für `scsi`/`fat`/`bmw-nbt-evo`; AVRCP; neues Feldmessen in diesem Commit.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Sheet `technologies/usb-msc/SHEET.md` (nur A) | erfüllt |
| 2 | Application mit B + C-Abgrenzung | erfüllt (C → Pilot 2 migriert) |
| 3 | Evidence-Register mit IDs | erfüllt |
| 4 | Inventar-Status/Coverage aktualisiert | erfüllt |
| 5 | Lessons: Templates ausreichend? | erfüllt (siehe unten) |
| 6 | Feld-AV PASS | **nicht erfüllt** — siehe [`pidrive` MSC-AKTUELL](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md); letzter upstream-Stand 2026-10-04, Feld-Ohr FAIL |

### Pilot-1-Abschluss (2026-10-05)

**Schema-Validation:** abgeschlossen — Framework-Zyklus durchlaufen, Kampagne `closed`.

**Produkt/Feld:** Feld-AV nicht PASS. GitHub `MPunktBPunkt/pidrive` hatte am 2026-10-05 **keine** neueren Commits zu `MSC-AKTUELL` oder Feld-AV-Artefakten als der Stand 2026-10-04 (Lab A+B PASS, Feld-Ohr offen). Nachverfolgung bleibt im Ursprungsrepo; C-Claims liegen in [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/).

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Sheet | [`technologies/usb-msc/SHEET.md`](../../technologies/usb-msc/SHEET.md) |
| Application | [`projects/pidrive/applications/usb-msc.md`](../../projects/pidrive/applications/usb-msc.md) |
| Evidence | [`evidence.md`](evidence.md) |

## Genutzte Methoden

Noch keine eigenen Method-Notes — Tracing/Korrelation bleiben vorerst in pidrive-Tools; nach Feld-AV ggf. `methods/msc-trace-correlation.md`.

## Lessons Learned

1. A/B/C funktioniert: HU-Claims lassen sich ohne Sheet-Verschmutzung führen.
2. Evidence-IDs brauchen stabile Links ins Ursprungsrepo — Rohtraces nicht kopieren.
3. Maturity-Vierklang (R/W) ist aussagekräftiger als „fertig“.
4. **Templates (6 Stück) reichen** für Pilot 1; optional später: explizite Felder für Claim-Chronik in Evidence.
5. Pilot 2 **`bmw-nbt-evo`**: C aus MSC-Application übernommen — siehe [`pidrive-2026-bmw-hu`](../pidrive-2026-bmw-hu/).
6. Dritter Pilot **`avrcp`** — anderes Profil (State Machine / Metadata).

## Offene Punkte (Transfer)

- Feld-AV schließen (Ursprungsrepo) → Evidence/Maturity in `bmw-nbt-evo` + `usb-msc` nachziehen
- Method Notes anlegen bei Bedarf
