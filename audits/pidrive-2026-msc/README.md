# Audit Campaign: pidrive-2026-msc

```yaml
id: pidrive-2026-msc
project_id: pidrive
started: 2026-10-04
ended: null
status: active
pilot: 1
next_pilots: [bmw-nbt-evo, avrcp]
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
| 2 | Application mit B + C-Abgrenzung | erfüllt |
| 3 | Evidence-Register mit IDs | erfüllt |
| 4 | Inventar-Status/Coverage aktualisiert | erfüllt |
| 5 | Lessons: Templates ausreichend? | offen (nach Review) |
| 6 | Feld-AV PASS | offen (Ursprungsrepo) |

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Sheet | [`technologies/usb-msc/SHEET.md`](../../technologies/usb-msc/SHEET.md) |
| Application | [`projects/pidrive/applications/usb-msc.md`](../../projects/pidrive/applications/usb-msc.md) |
| Evidence | [`evidence.md`](evidence.md) |

## Genutzte Methoden

Noch keine eigenen Method-Notes — Tracing/Korrelation bleiben vorerst in pidrive-Tools; nach Pilot ggf. `methods/msc-trace-correlation.md`.

## Lessons Learned (Zwischenstand)

1. A/B/C funktioniert: HU-Claims lassen sich ohne Sheet-Verschmutzung führen.
2. Evidence-IDs brauchen stabile Links ins Ursprungsrepo — Rohtraces nicht kopieren.
3. Maturity-Vierklang (R/W) ist aussagekräftiger als „fertig“.
4. Nächster Pilot **`bmw-nbt-evo`** soll Abschnitt C aus dieser Application übernehmen/erweitern, nicht MSC-Sheet aufblasen.
5. Dritter Pilot **`avrcp`** — anderes Profil (State Machine / Metadata).

## Offene Punkte nach diesem Stand

- Template-Felder für Maturity/Evidence nach Pilot-Feedback festziehen
- Method Notes anlegen
- Feld-AV schließen (außerhalb dieses Repos)
