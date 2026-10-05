# Audit Campaign: pidrive-2026-bmw-hu

```yaml
id: pidrive-2026-bmw-hu
project_id: pidrive
started: 2026-10-05
ended: null
status: active
pilot: 2
prior_audit: pidrive-2026-msc
next_pilots: [avrcp]
tech_slug: bmw-nbt-evo
```

## Ziel

**BMW NBT Evo** als zweiten Pilot durch das Framework: Technology Sheet (A) + Application (C) + Evidence — Host-Verhalten getrennt von USB-MSC-Spec und PiDrive-Device-Impl (**B** in `usb-msc`).

## Scope

- Im Scope: Sheet `technologies/bmw-nbt-evo/`; Application; Evidence für C-Claims (Migration aus MSC-Pilot); Reifegrade; Verknüpfung zu MSC-Application.
- Nicht im Scope: vollständiges HU-Reverse-Engineering; AVRCP (Pilot 3); neue Feldmessungen in diesem Commit.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Sheet `technologies/bmw-nbt-evo/SHEET.md` (nur A) | erfüllt |
| 2 | Application mit C-Claims (aus MSC übernommen) | erfüllt |
| 3 | Evidence-Register (C-Layer) | erfüllt |
| 4 | MSC-Application: C gekürzt, Verweis hierher | erfüllt |
| 5 | Inventar / Indexe aktualisiert | erfüllt |
| 6 | Feld-AV PASS (Ohr) | offen — Lab A+B PASS; Feld blockiert (Meta-Menü / Sender-Gate). C′ Feld PASS 2026-10-05 · [MSC-AKTUELL](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) |

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Sheet | [`technologies/bmw-nbt-evo/SHEET.md`](../../technologies/bmw-nbt-evo/SHEET.md) |
| Application | [`projects/pidrive/applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) |
| Evidence | [`evidence.md`](evidence.md) |

## Vorgänger

Pilot 1: [`pidrive-2026-msc/`](../pidrive-2026-msc/) — Schema-Validation MSC; C-Claims formal hierher verlagert.

## Lessons Learned (Zwischenstand)

1. Gleiche Evidence-IDs (`EVID-USBMSC-*`) vermeiden Doppelpflege beim Migrationsschritt; neue HU-Claims → `EVID-BMWHU-*`.
2. Feld-AV bleibt produktseitiges Exit-Kriterium — überlappt MSC- und HU-Pilot, bis upstream PASS dokumentiert ist.

## Offene Punkte

- Evidence 2026-10-05 nachgezogen (`EVID-BMWHU-*`); Exit #6 bleibt bis Feld-Ohr PASS upstream
- Nach Feld-AV PASS: Maturity (field_evidence R4+) + ggf. Method Note `field-av-correlation`
- Pilot 3 `avrcp` — BT-Host-Profil ergänzen (nicht USB-C duplizieren)
