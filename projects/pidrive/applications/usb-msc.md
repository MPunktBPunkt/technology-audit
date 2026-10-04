# Project Application: USB-MSC in PiDrive

```yaml
project_id: pidrive
tech_slug: usb-msc
status: active
sheet: ../../technologies/usb-msc/SHEET.md
audit: ../../audits/pidrive-2026-msc/
maturity:
  technology: R4          # Sheet
  implementation: R3      # Lab-stabil, Feld-AV noch offen
  field_evidence: R4      # Read/Seed/LED vielfach belegt; Ton/AV Feld noch FAIL
  reusability: W2         # noch eng an PiDrive/BMW-Geometrie
```

## Rolle im Projekt

`esp32.pidrive` (ESP32-S3) erscheint am **USB-Host der BMW-HU** als Mass-Storage-Device mit virtuellem FAT und on-the-fly-MP3-Sektoren. PiDrive bleibt Quellen-/Menü-Gehirn; Audio kann perspektivisch über `audio_output=usb_gadget` laufen (BT-Pfad bleibt parallel wählbar, nicht gleichzeitig).

Referenz-Einstieg Betrieb: [`MSC-AKTUELL.md`](https://github.com/MPunktBPunkt/pidrive/blob/main/docs/betrieb/MSC-AKTUELL.md) (Stand 2026-10-04).

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

**Nicht** in [`usb-msc` Sheet](../../technologies/usb-msc/SHEET.md) verschieben. Vollpilot Host: `bmw-nbt-evo` (nächste Kampagne nach diesem MSC-Pilot).

| Claim | Evidence | Status |
|-------|----------|--------|
| HU liest Medien-Slots blockweise über MSC/SCSI-READ; Prefetch/Burst vor Wiedergabe beobachtbar | `EVID-USBMSC-2026-10-04-001` | `MEASURED` |
| Auto-Next (Kurzdatei zu Ende) triggert vorhersagbaren Cold-Body-Burst des nächsten Slots (LBA-Fenster, mehrfach) | `EVID-USBMSC-2026-10-04-002` | `MEASURED` |
| Türöffnen kann zusätzlichen Cold-Body-/Re-Read auslösen | `EVID-USBMSC-2026-10-04-003` | `MEASURED` (Kausalität noch `INFERRED`) |
| Seed-Bytes können an die HU gehen (`bytesServed` ↑, Body-LBAs im Trace) — Lauf 17:32 PASS | `EVID-USBMSC-2026-10-04-004` | `MEASURED` |
| Seed bei GO tot / Reboot → C′ FAIL (17:38) | `EVID-USBMSC-2026-10-04-005` | `MEASURED` |
| Lab: MPEG-Bytes am Host-dd im Live-Fenster (A+B PASS) ≠ Feld-Ohr/Decoder | `EVID-USBMSC-2026-10-04-006` | `MEASURED` |
| Feld-AV/hörbarer Ton über MSC-Pfad | — | `UNKNOWN` / Ziel offen (Ampel FAIL) |
| „Warm-konfundierte Trace = Sequenz tot“ | frühere Fehlinterpretation | `REJECTED` (Trace-Korrektur 2026-10-04) |

### Evidence-Register (Auszug)

| ID | Quelle (Ursprungsrepo) | Kurz |
|----|------------------------|------|
| `EVID-USBMSC-2026-10-04-001` | `pidrive` Feldtraces / Q3b-Berichte | Host-Reads / Burst |
| `EVID-USBMSC-2026-10-04-002` | `feld-q3b-next-1732`, `1738`, PD0056/57 | Auto-Next → LBA 761-Fenster |
| `EVID-USBMSC-2026-10-04-003` | Feld 17:55 Tür | zusätzlicher Burst |
| `EVID-USBMSC-2026-10-04-004` | `GESAMTBERICHT-FELD-Q3B-1732` | Seed +8 MiB |
| `EVID-USBMSC-2026-10-04-005` | `GESAMTBERICHT-FELD-Q3B-1738` | Seed inactive bei GO |
| `EVID-USBMSC-2026-10-04-006` | `lab88-av-mpeg-2035` | Lab AV A+B PASS |

Vollständige Pfade: [`audits/pidrive-2026-msc/evidence.md`](../../audits/pidrive-2026-msc/evidence.md).

---

## Abweichungen vom „Lehrbuch“ (B)

- Medien sind **virtuell/on-the-fly**, kein klassischer Stick-Inhalt.
- Statische/slotbasierte Geometrie und Prefill/Seed sind **PiDrive-Strategien**, keine MSC-Pflicht.
- Erfolgskriterium ist HU-Decode + Ohr — übersteigt Block-I/O-Konformität.

## Offene Fragen

- Wann ist Feld-AV PASS (Korrelation Fenster × `liveBytes` × Ton)?
- Welche Geometrie (L0 vs. größere Images) bleibt langfristig?
- Wie scharf Detect-Heuristik vs. Observe-only?

## Verwandte

- Sheet: [`technologies/usb-msc`](../../technologies/usb-msc/SHEET.md)
- Geplant: Applications/Sheets `scsi`, `fat`, `bmw-nbt-evo`
- Methods (noch anzulegen): `msc-trace-correlation`, `field-av-correlation`
