# Project Application: USB-MSC in PiDrive

```yaml
project_id: pidrive
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/pidrive-2026-msc/
maturity:
  technology: R4          # Sheet
  implementation: R3      # Lab-stabil, Feld-AV noch offen
  field_evidence: R3      # C′ + Busy-Pacing ~65 s (2026-10-12); Exit #6 Menü-Gate offen (→ bmw-nbt-evo C)
  reusability: W2         # noch eng an PiDrive/BMW-Geometrie
```

## Rolle im Projekt

`esp32.pidrive` (ESP32-S3) erscheint am **USB-Host der BMW-HU** als Mass-Storage-Device mit virtuellem FAT und on-the-fly-MP3-Sektoren. PiDrive bleibt Quellen-/Menü-Gehirn; Audio kann perspektivisch über `audio_output=usb_gadget` laufen (BT-Pfad bleibt parallel wählbar, nicht gleichzeitig).

Referenz-Einstieg Betrieb: [`MSC-AKTUELL.md`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) (Stand 2026-10-05).

## Architektur / Datenfluss (B)

```text
PiDrive Quellen / Menü-UIDs
        │  PUMP (UART/CDC V1, später ggf. WLAN)
        ▼
esp32.pidrive (ESP32-S3)
  TinyUSB MSC + Puffer / Prefill / Body-Seed
  virtuelle FAT-Geometrie (Slots = Medien)
        │  USB Device (OTG) — nur MSC zum Auto
        ▼
BMW NBT Evo USB-Host  →  Liste + MP3-Decode (HU)
```

Zweites Kabel: Pi↔ESP (PUMP) ≠ OTG→BMW.

## Relevante Pfade

| Repo | Pfad | Rolle |
|------|------|-------|
| `esp32.pidrive` | `src/`, `components/` | MSC-Firmware |
| `esp32.pidrive` | `tools/msc_host_test.py`, `nbt_*.py` | Lab-Host / Replay |
| `esp32.pidrive` | `tools/traces/*.replay.json` | Trace-Replays |
| `pidrive` | `docs/planung/KONZEPT-USB-MSC.md` | Architekturkonzept |
| `pidrive` | `docs/betrieb/MSC-AKTUELL.md` | Normativer Betriebsstand |
| `pidrive` | `docs/betrieb/artifacts-2026-10-04-*` | Lab/Feld-Gesamtberichte |

## Konfiguration und Parameter (B)

| Thema | Stand (kurz) | Epistemic |
|-------|--------------|-----------|
| Chip | ESP32-S3 (natives USB-OTG) | `FACT` (B) |
| Geometrie | u. a. Lab L0: FAT16, begrenzte Slot-Größe; weiterentwickelt Prefill ab LBA-Fenstern | `MEASURED` / im Fluss |
| Prefill / Body-Seed | Seed kann Body-Reads bedienen; Live-Producer konkurriert — Priorität FW-gesteuert | `MEASURED` |
| Detect-Policy | Cold vs. Warm bewusst getrennt; nicht mit Transfer-Ende verwechseln | `INFERRED`→`MEASURED` in Lab |
| Sequenz-GO | betrieblich gesperrt bis hörbarer AV | Prozessregel (B) |

Details und Zahlen immer über Evidence-IDs, nicht als „MSC-Wahrheit“.

---

## Ebene C — BMW NBT Evo Host-Verhalten

Liegt bei Pilot 2: [`applications/bmw-nbt-evo.md`](bmw-nbt-evo.md) · Audit [`pidrive-2026-bmw-hu`](../../../audits/pidrive-2026-bmw-hu/) · Sheet [`bmw-nbt-evo`](../../../technologies/bmw-nbt-evo/SHEET.md).

Kurz: HU-Reads/Prefetch/Auto-Next/Seed **gemessen**; C′ Feld **PASS** (2026-10-05); Busy-Pacing-Ton ~65 s vs. ~6 s Stall-off (**MEASURED** 2026-10-12); Exit #6 Menü/Sender-Gate **offen**. C-Register: [`audits/pidrive-2026-bmw-hu/evidence.md`](../../../audits/pidrive-2026-bmw-hu/evidence.md) · MSC-Pilot historisch: [`pidrive-2026-msc`](../../../audits/pidrive-2026-msc/evidence.md) · Busy-Desk: [`tinyusb-msc-busy-retry-2026`](../../../audits/tinyusb-msc-busy-retry-2026/).

---

## Abweichungen vom „Lehrbuch“ (B)

- Medien sind **virtuell/on-the-fly**, kein klassischer Stick-Inhalt.
- Statische/slotbasierte Geometrie und Prefill/Seed sind **PiDrive-Strategien**, keine MSC-Pflicht.
- Erfolgskriterium ist HU-Decode + Ohr — übersteigt Block-I/O-Konformität.

## Offene Fragen

- Exit #6 Feld-AV/Ohr (Menü/Sender-Gate) — getrennt vom Busy-Pacing-Tonfenster
- Korrelation Fenster × `liveBytes` × Ton nach Gate
- Welche Geometrie (L0 vs. größere Images) bleibt langfristig?
- Wie scharf Detect-Heuristik vs. Observe-only?

## Verwandte

- Sheet: [`technologies/usb-msc`](../../../technologies/usb-msc/SHEET.md) · [`virtual-fat`](../../../technologies/virtual-fat/SHEET.md)
- Firmware-Desk: [`esp32-pidrive/applications/usb-msc`](../../esp32-pidrive/applications/usb-msc.md) · PUMP [`pump-control-link`](../../esp32-pidrive/applications/pump-control-link.md)
- Host: [`bmw-nbt-evo`](bmw-nbt-evo.md)
- Fremd-Referenzen (Callback/Perf): [`esp32-msc-gadget-refs`](../../esp32-msc-gadget-refs/)
- Methods: [`msc-lba-timing-instrument`](../../../methods/msc-lba-timing-instrument.md) · [`msc-trace-correlation`](../../../methods/msc-trace-correlation.md); Kandidat: `field-av-correlation`
