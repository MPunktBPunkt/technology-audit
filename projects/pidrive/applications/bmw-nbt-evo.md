# Project Application: BMW NBT Evo in PiDrive

```yaml
project_id: pidrive
tech_slug: bmw-nbt-evo
status: active
sheet: ../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../audits/pidrive-2026-bmw-hu/
related_applications:
  - ../../projects/pidrive/applications/usb-msc.md
maturity:
  technology: R2
  implementation: R0      # HU ist Host; „Implementation“ = Beobachtungs- und Korrelationsmodell
  field_evidence: R3      # Reads/Seed/Auto-Next; Feld-AV/Ohr noch offen
  reusability: W1
```

## Rolle im Projekt

Die **BMW NBT Evo** ist der USB-**Host**, der PiDrives ESP32-MSC-Gadget mountet, Medien listet und MP3 dekodiert. PiDrive liefert virtuelle Medien und Steuerlogik; die HU bestimmt **wann** und **welche LBAs** gelesen werden — das ist Gegenstand dieser Application (**C**).

Device-Seite (TinyUSB, Geometrie, Seed, Producer): [`usb-msc.md`](usb-msc.md) (**B**).

Normativer Betriebsstand: [`MSC-AKTUELL.md`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md).

## Architektur / Beobachtungsebene

```text
esp32.pidrive (MSC Device, B)
        │  USB MSC — BOT, SCSI READs
        ▼
BMW NBT Evo (Host, C)
  Prefetch / Burst / Auto-Next / Decode
        ▼
  Lautsprecher (Erfolgskriterium: hörbarer Ton — noch offen im Feld)
```

## Relevante Pfade

| Repo | Pfad | Rolle |
|------|------|-------|
| `pidrive` | `docs/betrieb/MSC-AKTUELL.md` | Ampel, Lesereihenfolge |
| `pidrive` | `docs/betrieb/artifacts-2026-10-04-feld/` | Feld Q3b, Traces |
| `pidrive` | `docs/betrieb/artifacts-2026-10-04-lab/` | Lab AV, Seed-Gate |
| `esp32.pidrive` | `tools/nbt_*.py`, `tools/traces/` | Replay / Lab-Host |

## Ebene C — empirisches Host-Verhalten (NBT Evo, USB-MSC)

**Nicht** ins [`usb-msc` Sheet](../../technologies/usb-msc/SHEET.md). Evidence-Register: [`audits/pidrive-2026-bmw-hu/evidence.md`](../../audits/pidrive-2026-bmw-hu/evidence.md).

| Claim | Evidence | Status |
|-------|----------|--------|
| HU liest Medien-Slots blockweise über MSC/SCSI-READ; Prefetch/Burst vor Wiedergabe beobachtbar | `EVID-USBMSC-2026-10-04-001` | `MEASURED` |
| Auto-Next (Kurzdatei zu Ende) triggert vorhersagbaren Cold-Body-Burst des nächsten Slots (LBA-Fenster, mehrfach) | `EVID-USBMSC-2026-10-04-002` | `MEASURED` |
| Türöffnen kann zusätzlichen Cold-Body-/Re-Read auslösen | `EVID-USBMSC-2026-10-04-003` | `MEASURED` (Kausalität noch `INFERRED`) |
| Seed-Bytes können an die HU gehen (`bytesServed` ↑, Body-LBAs im Trace) — Lauf 17:32 PASS | `EVID-USBMSC-2026-10-04-004` | `MEASURED` |
| Seed bei GO tot / Reboot → C′ FAIL (17:38) — HU-seitig sichtbar als fehlende Seed-Lieferung | `EVID-USBMSC-2026-10-04-005` | `MEASURED` |
| Lab: MPEG-Bytes am Host-dd im Live-Fenster (A+B PASS) ≠ Feld-Ohr/Decoder | `EVID-USBMSC-2026-10-04-006` | `MEASURED` |
| Feld-AV / hörbarer Ton über MSC-Pfad | — | `UNKNOWN` (Ampel FAIL, Stand upstream 2026-10-04) |
| „Warm-konfundierte Trace = Sequenz tot“ | `EVID-USBMSC-2026-10-04-007` | `REJECTED` |

Evidence-IDs bleiben vorerst `EVID-USBMSC-*` (aus Pilot 1); neue HU-only Claims erhalten künftig `EVID-BMWHU-*`.

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-04 17:32 | C′ Seed PASS — `bytesServed` ≈ +8 MiB |
| 2026-10-04 17:38 | C′ FAIL — Seed inactive bei GO |
| 2026-10-04 Lab | AV A+B PASS am Host-dd; Feld-Ohr offen |
| 2026-10-05 | Kein neuer upstream-Commit zu Feld-AV (GitHub `pidrive`) |

## Offene Fragen

- Feld-AV: Korrelation `fileOff`/`hostAbs` × `liveBytes` × Underruns × Ton
- Auto-Next vs. manueller Track-Wechsel — gleiches Read-Muster?
- BT-Pfad (A2DP/AVRCP) vs. MSC — getrennte Host-Profile unter einem Sheet?

## Verwandte

- Sheet: [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md)
- MSC Application (B): [`usb-msc.md`](usb-msc.md)
- Audit: [`pidrive-2026-bmw-hu`](../../audits/pidrive-2026-bmw-hu/)
