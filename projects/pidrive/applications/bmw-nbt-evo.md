# Project Application: BMW NBT Evo in PiDrive

```yaml
project_id: pidrive
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/pidrive-2026-bmw-hu/
related_audits:
  - ../../../audits/pidrive-2026-10-17-prefetch-livelock/
  - ../../../audits/pidrive-2026-storm-capture-tooling/
  - ../../../audits/prefetch-livelock-public-gap-2026/
related_applications:
  - usb-msc.md
maturity:
  technology: R2
  implementation: R0      # HU ist Host; „Implementation“ = Beobachtungs- und Korrelationsmodell
  field_evidence: R3      # C′ + Busy-Pacing ~65 s (2026-10-12) + Abend-Muster 2026-10-17; Exit #6 Menü-Gate noch offen
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
  Lautsprecher (Busy-Pacing-Ton ~65 s belegt 2026-10-12; Exit #6 Menü-Gate noch offen)
```

## Relevante Pfade

| Repo | Pfad | Rolle |
|------|------|-------|
| `pidrive` | `docs/betrieb/MSC-AKTUELL.md` | Ampel, Lesereihenfolge |
| `pidrive` | `docs/betrieb/artifacts-2026-10-05-feld/` | C′ PASS, AV-Menü-Hindernis |
| `pidrive` | `docs/betrieb/artifacts-2026-10-05-lab/` | Menü-Seite, Correlate, Lock-after-RST |
| `pidrive` | `docs/betrieb/artifacts-2026-10-04-feld/` | Feld Q3b (Historie) |
| `pidrive` | `docs/betrieb/artifacts-2026-10-04-lab/` | Lab AV MPEG @ Host |
| `pidrive` | `docs/betrieb/artifacts-2026-10-17-feld/` | Abend-Feld + Tri-Review Prefetch-Livelock |
| `esp32.pidrive` | `tools/nbt_*.py`, `tools/traces/` | Replay / Lab-Host |

## Ebene C — empirisches Host-Verhalten (NBT Evo, USB-MSC)

**Nicht** ins [`usb-msc` Sheet](../../../technologies/usb-msc/SHEET.md). Evidence-Register: [`audits/pidrive-2026-bmw-hu/evidence.md`](../../../audits/pidrive-2026-bmw-hu/evidence.md) · Abend-Muster 2026-10-17: [`audits/pidrive-2026-10-17-prefetch-livelock/evidence.md`](../../../audits/pidrive-2026-10-17-prefetch-livelock/evidence.md).

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
| Feld-AV / hörbarer Ton (Exit „Ohr“ — Sender/Menü-Gate) | — | `UNKNOWN` (teilweise; Gate Rock/Bayern/BOB) |
| NBT akzeptiert Busy-Pacing; READ10 bleibt offen | `EVID-BMWHU-2026-10-12-001` | `MEASURED` |
| Busy-Pacing: ~65 s Wiedergabe bis Dateiende (512 KiB) | `EVID-BMWHU-2026-10-12-002` | `MEASURED` |
| Stall-off: wieder ~6 s Tonfenster (A/B) | `EVID-BMWHU-2026-10-12-003` | `MEASURED` |
| Busy-Pacing kausaler Faktor (A/B) | `EVID-BMWHU-2026-10-12-004` | `INFERRED` |
| „Kleiner Ring + kurze Tonphase = technische Grenze“ | `EVID-BMWHU-2026-10-12-005` | `REJECTED` |
| Unter Stall: Menü/Enumeration ~20 s träge | `EVID-BMWHU-2026-10-12-006` | `MEASURED` (Ursache `INFERRED`/`UNKNOWN`) |
| Rock Antenne 8 MiB in S6 oft stumm (Resume/Start) | `EVID-BMWHU-2026-10-12-007` | `MEASURED` (Ursache `UNKNOWN`) |
| `readCount − playRejectCount ∈ {31,32}` session-weit (Abend 0.4.53) | `EVID-BMWHU-2026-10-17-001` | `MEASURED` |
| `(167,136)` + `pref≈8` = Quiet-Plateau — **kein** Stuck-allein-Marker | `EVID-BMWHU-2026-10-17-002` | `MEASURED` |
| Stuck-Morphologien Quiet vs Storm (pref/midFile/bytesFile) | `EVID-BMWHU-2026-10-17-003` | `MEASURED` |
| Meta-Bytes (Dir/Fat/Meta/Boot) session-konstant; Livelock = File-Body | `EVID-BMWHU-2026-10-17-004` | `MEASURED` |
| Play-Guess mitten im Reject-Storm möglich (17:58:21) | `EVID-BMWHU-2026-10-17-005` | `MEASURED` |
| `fromHead` ∈ {0,2}; Mid-file dominiert | `EVID-BMWHU-2026-10-17-006` | `MEASURED` |
| fav2 oft voll vorgelesen ohne Play | `EVID-BMWHU-2026-10-17-007` | `MEASURED` |
| hostAbs-Overshoot nach Tonfenster (bis ~859 KiB; M27) | `EVID-BMWHU-2026-10-17-008` | `MEASURED` |
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
| 2026-10-12 E7/S6 | Busy-Pacing an NBT: ~65 s bis Dateiende; Stall-off ~6 s; Menü ~20 s; Rock oft stumm — `EVID-BMWHU-2026-10-12-001`–`007` · [ERGEBNIS-S6](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/artifacts-2026-10-12-feld/feld-s6-prep/ERGEBNIS-S6.md) |
| 2026-10-17 Abend | Quiet/Storm-Muster, Meta konstant, Guess-im-Storm, hostAbs-Overshoot — `EVID-BMWHU-2026-10-17-001`–`010` · [TRI-REVIEW](https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/TRI-REVIEW-ABEND-2026-10-17.md) · Audit [`pidrive-2026-10-17-prefetch-livelock`](../../../audits/pidrive-2026-10-17-prefetch-livelock/) |
| 2026-10-18 Desk | Öffentliche Boot/Dump/KeenLab/Generic-MSC-Quellen liefern **keinen** Prefetch-Livelock-/Q/S-Analyzer — Gap · `EVID-PREFGAP-2026-10-18-015` · [`prefetch-livelock-public-gap-2026`](../../../audits/prefetch-livelock-public-gap-2026/) |

## Community / SIB (Transfer-Hinweise — nicht MEASURED)

Siehe Sheet-Abschnitt „Community / SIB-Muster“. Für Live-Fake-MP3 relevant:

1. Volume-Label + USB-Serial bewusst versionieren / Cache-Tests planen.  
2. Re-Index-Ritual (mehrere Sticks) als Experiment, nicht als Spec.  
3. FAT32-Hypothese vs. bestehende FAT12/16-Labgeometrie — eigener Gate-Lauf.  
4. Dateizahl/Namen kurz halten; große Libs = Index-Risiko.  
5. Callback-Latenz/Bursts instrumentieren: [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md).

Referenz-Gadgets (kein HU-Feld): [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/).

## Offene Fragen

- Feld-AV/Ohr Exit #6: Gate Rock/Bayern/BOB + erstes `MSC_MAP_FROZEN` (getrennt vom Busy-Pacing-Tonfenster 2026-10-12)
- Korrelation `fileOff`/`hostAbs` × `liveBytes` × Underruns × Ton (nach Gate)
- Auto-Next vs. manueller Track-Wechsel — gleiches Read-Muster?
- Storm-Capture M30: LBA/Klasse × Guess (öffentliche RE ersetzt das nicht — Public-Gap-Audit)
- BT-Pfad (A2DP/AVRCP) vs. MSC — getrennte Host-Profile unter einem Sheet?
- Welche Label/Serial-Änderung flush’t NBT-Cache empirisch?
- Max `onRead`-Latenz / BUSY-Budget vor HU-Abort jenseits des belegten Stall-Defaults (`maxMs=500`)?
- Mechanismus Menü-~20 s (`006`) und Rock-8‑MiB-stumm (`007`)

## Verwandte

- Sheet: [`bmw-nbt-evo`](../../../technologies/bmw-nbt-evo/SHEET.md)
- MSC Application (B): [`usb-msc.md`](usb-msc.md)
- Audit: [`pidrive-2026-bmw-hu`](../../../audits/pidrive-2026-bmw-hu/)
- Gadget-Refs: [`esp32-msc-gadget-refs-2026-foreign`](../../../audits/esp32-msc-gadget-refs-2026-foreign/)
- Methods: [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md) · [`msc-trace-correlation`](../../../methods/msc-trace-correlation.md)
