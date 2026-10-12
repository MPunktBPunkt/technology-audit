# Audit Campaign: pidrive-2026-bmw-hu

```yaml
id: pidrive-2026-bmw-hu
project_id: pidrive
started: 2026-10-05
ended: null
profile: ops-field
standard_version: "0.6.6"
revalidated_from: "0.5.1"
revalidated: 2026-10-11
status: active
pilot: 2
prior_audit: pidrive-2026-msc
next_pilots: [avrcp]
tech_slug: bmw-nbt-evo
reuse_outcomes:
  - new: [bmw-nbt-evo]
  - layer: "C-host claims stay in Application; usb-msc stays protocol"
  - sharpened: "0.6.6 host-variant scope NBT Evo; process parity from 0.5.1"
  - process: "closed standard_gaps; DELTA separates framework vs source"
  - not_transferred: "HU timing → usb-msc sheet; NBT → other BMW HU"
```

## Ziel

**BMW NBT Evo** als zweiten Pilot durch das Framework: Technology Sheet (A) + Application (C) + Evidence — Host-Verhalten getrennt von USB-MSC-Spec und PiDrive-Device-Impl (**B** in `usb-msc`).

**Revalidation 2026-10-11:** Prozess-Parität **0.5.1 → 0.6.6** (Reuse/Profile/Checklisten/`standard_version`) + Host-Varianten-Scope. Historie: Git + [DELTA](DELTA.md).

**Field Feedback 2026-10-12:** E7/S6 Busy-Pacing am NBT (~65 s vs. ~6 s Stall-off) → `EVID-BMWHU-2026-10-12-*`. Exit #6 (Sender/Menü-Gate) bleibt **offen** — kein stilles globales Ohr-PASS.

## Scope

- Im Scope: Sheet `technologies/bmw-nbt-evo/`; Application; Evidence für C-Claims; Reifegrade; Verknüpfung zu MSC-Application.
- Nicht im Scope: vollständiges HU-Reverse-Engineering; AVRCP als USB-C-Duplikat (→ radio-bt / Gateway); neue Feldmessungen in dieser Revalidation.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Sheet `technologies/bmw-nbt-evo/SHEET.md` (nur A) | erfüllt |
| 2 | Application mit C-Claims (aus MSC übernommen) | erfüllt |
| 3 | Evidence-Register (C-Layer) | erfüllt |
| 4 | MSC-Application: C gekürzt, Verweis hierher | erfüllt |
| 5 | Inventar / Indexe aktualisiert | erfüllt |
| 6 | Feld-AV PASS (Ohr) — Sender-Slots / Meta-Menü-Gate | offen — getrennt vom Busy-Pacing-Tonfenster 2026-10-12 (`EVID-BMWHU-2026-10-12-002`). C′ Feld PASS 2026-10-05 · [MSC-AKTUELL](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) |
| 7 | Revalidation 0.6.6: Gaps geschlossen + Host-Scope + DELTA | erfüllt (2026-10-11) |
| 8 | Knowledge Feedback Busy-Pacing E7/S6 → Evidence + Applications | erfüllt (2026-10-12; Upstream-Artefakt nachziehen) |

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Sheet | [`technologies/bmw-nbt-evo/SHEET.md`](../../technologies/bmw-nbt-evo/SHEET.md) |
| Application | [`projects/pidrive/applications/bmw-nbt-evo.md`](../../projects/pidrive/applications/bmw-nbt-evo.md) |
| Evidence | [`evidence.md`](evidence.md) |
| DELTA | [`DELTA.md`](DELTA.md) |

## Vorgänger

Pilot 1: [`pidrive-2026-msc/`](../pidrive-2026-msc/) — Schema-Validation MSC; C-Claims formal hierher verlagert.

## Knowledge Feedback (2026-10-12)

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| E7/S6 Busy-Pacing NBT | `EVID-BMWHU-2026-10-12-001`–`005` | [`bmw-nbt-evo` Application](../../projects/pidrive/applications/bmw-nbt-evo.md) · [`esp32-pidrive` usb-msc](../../projects/esp32-pidrive/applications/usb-msc.md) |
| Desk-Basis | `EVID-TINYUSB-MSC-2026-10-12-*` | [`tinyusb-msc-busy-retry-2026`](../tinyusb-msc-busy-retry-2026/) |

Upstream-Rohartefakte der Session: **nachziehen** (kein erfundener GitHub-Pfad).

## Lessons Learned

1. Gleiche Evidence-IDs (`EVID-USBMSC-*`) vermeiden Doppelpflege beim Migrationsschritt; neue HU-Claims → `EVID-BMWHU-*`.
2. Feld-AV Exit #6 (Sender/Menü-Gate) bleibt getrennt vom Busy-Pacing-Tonfenster — kein stilles globales Ohr-PASS.
3. Revalidation mischt Framework-Sprung und historische Evidence — DELTA trennt beides; kein stilles „alles neu gemessen“.
4. **2026-10-12:** Desk TinyUSB-BUSY → gezieltes E7 → Feld S6 (~65 s vs. ~6 s Stall-off) widerlegt „kleiner Ring = Grenze“. Rückkanal Field→Audit ist Pflicht (0.7.0 C13).

## Offene Punkte

- Exit #6 Feld-Ohr PASS upstream (Menü/Sender-Gate) — nicht durch Busy-Pacing-Session erfüllt
- Upstream-Artefakt-Links für `EVID-BMWHU-2026-10-12-*` nachziehen
- Nach Exit #6 PASS: Maturity (field_evidence R4+) + ggf. Method Note `field-av-correlation`
- Pilot 3 `avrcp` — BT-Host-Profil in [`pidrive-2026-radio-bt`](../pidrive-2026-radio-bt/) / Gateway, nicht USB-C duplizieren
