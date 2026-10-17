# hu-probe BMW S0/S2 Feld · 2026-10-15

**Standard:** 0.7.1  
**Kampagne:** [`hu-probe-bmw-s0s2-field-2026`](../../audits/hu-probe-bmw-s0s2-field-2026/)  
**Upstream-Pin:** `hu-probe@5dbec43` · FW bis 0.2.23

## Ergebnis

Transportschicht NBT ist mit **eigener** hu-probe-Messlage bestätigt (S0≈S2 Gap,
tinyusb-BOT, Writes=false, dropped=0). **Kaum neue Scheduler-FACTs** — stärkere
Messlage + CBW-Klarheit (READ10 blocks, ms6/cap, Stall=Instrument). Prefetch /
Eager / Cache / Burst-39 bleiben **INFERENCE**.

| Neu / gestärkt | Als HU-Parameter? | Evidence |
|----------------|-------------------|----------|
| S2 Gap-p50 ~3783 µs ≈ S0 ~3739 µs | Messgröße bestätigt, nicht neuer Scheduler-Wert | `001`–`003`, `008` |
| READ10 oft blocks=8 (=4096 B) und blocks=240 | ja, CBW-seitig neu belegt | `004` |
| ms6/cap = 2,0 auch nach Stall-Fix | ja, HU-Verhalten | `005`–`006` |
| Read-Kind-Gaps (file/fat/dir/boot) | informativ; Deutung offen | `011` |
| Burst-39, Prefetch ~15 s | weiter nur INFERENCE | `009`–`010` |
| 4096-Event-Gap ≈ FS-Link | eher Probe/Link, nicht blind HU-Pace | `008` |

Zusätzlich: Lab `ram_offline` E2E PASS · BMW Offline FAIL · ep_stall≈0 nach 0.2.18
(`007`, `005`).

## Kill (unverändert / geschärft)

PiDrive-Semantik ≠ hu-probe-FACT · Burst-39 nicht konstant · ms6-STALL ≠ HU-Recovery ·
Lab≠BMW · Gap/4096 nicht blind als Scheduler · keine Wire-Claims.

## Deliverables

- Evidence `EVID-HUPROBE-2026-10-15-001`–`013`
- Applications: [`usb-msc`](../../projects/hu-probe/applications/usb-msc.md), [`bmw-nbt-evo`](../../projects/hu-probe/applications/bmw-nbt-evo.md)
- P1c Patch-Skizze in Evidence; **Upstream ausgeführt 2026-10-17** (schema 3)

## Nächster Schritt

1. ~~Upstream **P1c** `bmw_nbt_evo.json`~~ **done 2026-10-17**  
2. Offline blocks/LBA-Check + S2 Formalauswertung (Semantik)  
3. Auto-Offline-Diagnose · dann S3 → S1 ≥4 MiB
