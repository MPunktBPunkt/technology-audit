# Project Application: BMW NBT Evo in PiDrive

```yaml
project_id: pidrive
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/pidrive-2026-bmw-hu/
related_applications:
  - usb-msc.md
maturity:
  technology: R2
  implementation: R0      # HU ist Host; „Implementation“ = Beobachtungs- und Korrelationsmodell
  field_evidence: R3      # C′ Feld PASS; Lab Menü/Lock; Exit Ohr/AV-Feld noch offen
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
  Lautsprecher (Erfolgskriterium: hörbarer Ton — AV-Feld blockiert, C′ Feld PASS)
```

## Relevante Pfade

| Repo | Pfad | Rolle |
|------|------|-------|
| `pidrive` | `docs/betrieb/MSC-AKTUELL.md` | Ampel, Lesereihenfolge |
| `pidrive` | `docs/betrieb/artifacts-2026-10-05-feld/` | C′ PASS, AV-Menü-Hindernis |
| `pidrive` | `docs/betrieb/artifacts-2026-10-05-lab/` | Menü-Seite, Correlate, Lock-after-RST |
| `pidrive` | `docs/betrieb/artifacts-2026-10-04-feld/` | Feld Q3b (Historie) |
| `pidrive` | `docs/betrieb/artifacts-2026-10-04-lab/` | Lab AV MPEG @ Host |
| `esp32.pidrive` | `tools/nbt_*.py`, `tools/traces/` | Replay / Lab-Host |

## Ebene C — empirisches Host-Verhalten (NBT Evo, USB-MSC)

**Nicht** ins [`usb-msc` Sheet](../../../technologies/usb-msc/SHEET.md). Evidence-Register: [`audits/pidrive-2026-bmw-hu/evidence.md`](../../../audits/pidrive-2026-bmw-hu/evidence.md).

| Claim | Evidence | Status |
|-------|----------|--------|
| HU liest Medien-Slots blockweise über MSC/SCSI-READ; Prefetch/Burst vor Wiedergabe beobachtbar | `EVID-USBMSC-2026-10-04-001` | `MEASURED` |
| Auto-Next (Kurzdatei zu Ende) triggert vorhersagbaren Cold-Body-Burst des nächsten Slots (LBA-Fenster, mehrfach) | `EVID-USBMSC-2026-10-04-002` | `MEASURED` |
| Türöffnen kann zusätzlichen Cold-Body-/Re-Read auslösen | `EVID-USBMSC-2026-10-04-003` | `MEASURED` (Kausalität noch `INFERRED`) |
| Seed-Bytes können an die HU gehen (`bytesServed` ↑, Body-LBAs im Trace) — Lauf 17:32 PASS | `EVID-USBMSC-2026-10-04-004` | `MEASURED` |
| Seed bei GO tot / Reboot → C′ FAIL (17:38) — HU-seitig sichtbar als fehlende Seed-Lieferung | `EVID-USBMSC-2026-10-04-005` | `MEASURED` |
| Lab: MPEG-Bytes am Host-dd im Live-Fenster (A+B PASS) ≠ Feld-Ohr/Decoder | `EVID-USBMSC-2026-10-04-006` | `MEASURED` |
| Feld-Oracle C′ (Seed/Settle im Auto) | `EVID-BMWHU-2026-10-05-001` | `MEASURED` |
| Feld-AV blockiert (Meta-Menü, kein Live-Stream) | `EVID-BMWHU-2026-10-05-002` | `MEASURED` |
| Lab: Menü-Seite / Sender-Slots für AV-Vorbereitung | `EVID-BMWHU-2026-10-05-003` | `MEASURED` |
| Lab: Meta vs. Sender Correlate | `EVID-BMWHU-2026-10-05-004` | `MEASURED` |
| Lab: Meta-Erstsiegel / Menü-Lock nach RST | `EVID-BMWHU-2026-10-05-005` | `MEASURED` |
| Feld-AV / hörbarer Ton (Exit „Ohr“) | — | `UNKNOWN` (Gate Sender-Slots; Abend-EAR upstream) |
| Host-Scope: Claims = NBT Evo (nicht still andere BMW-HU) | `EVID-SCOPE-2026-10-11-001` | `FACT` |
| „Warm-konfundierte Trace = Sequenz tot“ | `EVID-USBMSC-2026-10-04-007` | `REJECTED` |

Ältere HU-Reads: Pilot-1-IDs (Präfix USBMSC in Tabelle). Ab 2026-10-05: Präfix BMWHU.

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-04 17:32 | C′ Seed PASS — `bytesServed` ≈ +8 MiB |
| 2026-10-04 17:38 | C′ FAIL — Seed inactive bei GO |
| 2026-10-04 Lab | AV A+B PASS am Host-dd |
| 2026-10-05 07:45 | C′ Feld **PASS** — siehe `EVID-BMWHU-2026-10-05-001` |
| 2026-10-05 07:50 | Feld-AV blockiert (Meta-Menü) — `EVID-BMWHU-2026-10-05-002` |
| 2026-10-05 Lab | Menü-Seite, Correlate, Lock-after-RST — `EVID-BMWHU-2026-10-05-003`–`005` |

## Community / SIB (Transfer-Hinweise — nicht MEASURED)

Siehe Sheet-Abschnitt „Community / SIB-Muster“. Für Live-Fake-MP3 relevant:

1. Volume-Label + USB-Serial bewusst versionieren / Cache-Tests planen.  
2. Re-Index-Ritual (mehrere Sticks) als Experiment, nicht als Spec.  
3. FAT32-Hypothese vs. bestehende FAT12/16-Labgeometrie — eigener Gate-Lauf.  
4. Dateizahl/Namen kurz halten; große Libs = Index-Risiko.  
5. Callback-Latenz/Bursts instrumentieren: [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md).

Referenz-Gadgets (kein HU-Feld): [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/).

## Offene Fragen

- Feld-AV/Ohr: Gate Rock/Bayern/BOB + erstes `MSC_MAP_FROZEN` loggen (Abend-EAR upstream)
- Korrelation `fileOff`/`hostAbs` × `liveBytes` × Underruns × Ton (nach Gate)
- Auto-Next vs. manueller Track-Wechsel — gleiches Read-Muster?
- BT-Pfad (A2DP/AVRCP) vs. MSC — getrennte Host-Profile unter einem Sheet?
- Welche Label/Serial-Änderung flush’t NBT-Cache empirisch?
- Max `onRead`-Latenz vor HU-Abort?

## Verwandte

- Sheet: [`bmw-nbt-evo`](../../../technologies/bmw-nbt-evo/SHEET.md)
- MSC Application (B): [`usb-msc.md`](usb-msc.md)
- Audit: [`pidrive-2026-bmw-hu`](../../../audits/pidrive-2026-bmw-hu/)
- Gadget-Refs: [`esp32-msc-gadget-refs-2026-foreign`](../../../audits/esp32-msc-gadget-refs-2026-foreign/)
- Methods: [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md) · [`msc-trace-correlation`](../../../methods/msc-trace-correlation.md)
