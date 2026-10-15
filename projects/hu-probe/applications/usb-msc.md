# Project Application: usb-msc in hu-probe

```yaml
project_id: hu-probe
tech_slug: usb-msc
status: active
sheet: ../../../technologies/usb-msc/SHEET.md
audit: ../../../audits/hu-probe-bmw-s0s2-field-2026/
maturity:
  technology: R3
  implementation: R2
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

hu-probe ist ein **USB-MSC Device** (ESP32-S3, TinyUSB/Arduino): Demo-/Virtual-FAT,
BOT-Instrumentierung (`t_us`, `gap_us`, CBW/CSW, `read`-Events), TCP- oder
RAM-Offline-Capture zum Collector. Ziel = Host-Lesen messen, nicht Medien-Player.

## Architektur / Datenfluss

```text
HU USB Host ──BOT/SCSI──► TinyUSB MSC Device (hu-probe)
                              │
                              ├─ read/CBW Events (Ring)
                              ├─ tcp_live ──WiFi──► Collector
                              └─ ram_offline (WIFI_OFF → Replay) ──► Collector
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `firmware/` (MSC / TinyUSB Hooks) | BOT, MODE_SENSE6-Pad ≥0.2.18 |
| `collector/` | Session-Store, validate |
| `tools/` | Offline-P0 / Auswerte-Skripte |
| `docs/SCHEMA.md`, `docs/SZENARIEN.md` | Event-/Szenario-Vertrag |
| `sessions/*` | Rohdaten (nicht hierher kopieren) |

## Konfiguration und Parameter

| Parameter | Wert | Status |
|-----------|------|--------|
| BOT-Pfad | `bot_source=tinyusb` (Feld S0/S2) | `MEASURED` `EVID-HUPROBE-2026-10-15-001`/`003` |
| MODE_SENSE6 | Pad auf CBW-Länge (0.2.18) — vorher Case-5 STALL | `FACT` (FW) + Feld `005`/`006` |
| Offline RAM | 64 KiB Default / Rec~91 B / max ~180 s | `FACT` (FW-Doku) |
| Lab Offline | Session `181642` complete | `MEASURED` `007` |
| BMW Offline | 1 Versuch fail (Stand 2026-10-15) | `MEASURED` `007` |
| Pace-Metrik | `gap_us` (nicht fragmentierte `t_us`) | `FACT` (Instrument-Regel) |

## Ebene C — Host- / Feld-Evidenz

Host-Verhalten (NBT) → [`bmw-nbt-evo.md`](bmw-nbt-evo.md). Hier nur **Device/Instrument**:

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| dropped=0 in S0/S2 Kern-Sessions | `001`, `003` | `MEASURED` |
| MODE_SENSE6-Stalls vor Fix = Instrument | `006` | `MEASURED` / HU-Recovery `REJECTED` |
| ep_stall≈0 nach 0.2.18 (S2 Stichprobe) | `005` | `MEASURED` |
| große READ10 → mehrere 4096-`read`-Events | `004` | `MEASURED` |
| Lab ram_offline E2E; BMW Offline fail | `007` | `MEASURED` |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-15 S0 0.2.17 | Transport belastbar in Burst-Fenstern; WiFi-Gelb unter Dauergrün |
| 2026-10-15 Offline-P0 | STALL↔ms6; Burst-Def `gap_us`>500 ms |
| 2026-10-15 S2 0.2.23 | Live tcp_live brauchbar; Offline Auto noch nicht |

## Abweichungen vom „Lehrbuch“

- TinyUSB Case-5 MODE_SENSE6 (4 B) vs. BMW-CBW 192 B → STALL ohne Pad.
- Capture unter Coex: Timeline fragmentiert; Burst-Epistemik statt unbroken GATE-01.

## Offene Fragen

- Auto Offline reproduzieren (Soft-Re-Enum / measure_ms / Power)
- t_us-Regression in langen Sessions (P1a)
- Marker-Pipeline ohne WiFi

## Verwandte Applications / Methods

- [`bmw-nbt-evo.md`](bmw-nbt-evo.md) · [`esp32-s3-usb-wifi-coex.md`](esp32-s3-usb-wifi-coex.md)
- Method [`msc-host-read-semantics`](../../../methods/msc-host-read-semantics.md)
- Prior Desk: [`msc-host-read-semantics-s1s2s3-2026`](../../../audits/msc-host-read-semantics-s1s2s3-2026/)
