# Project Application: bmw-nbt-evo in hu-probe

```yaml
project_id: hu-probe
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/hu-probe-bmw-s0s2-field-2026/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R2   # Transport S0/S2; Semantik noch INFERENCE
  reusability: W1
```

## Rolle im Projekt

**BMW NBT Evo** ist der Golden-Host für hu-probe (Profil `bmw_nbt_evo`). Die Sonde
misst Host-Reads am OTG; PiDrive-Semantik (Eager/Prefetch/Cache) ist **Anker**,
nicht automatischer hu-probe-`FACT`. PiDrive-C bleibt in
[`projects/pidrive/applications/bmw-nbt-evo.md`](../../pidrive/applications/bmw-nbt-evo.md).

## Architektur / Datenfluss

```text
NBT USB Host ──READ10/TUR/MS6/…──► hu-probe MSC Device
                     │
                     └─ Sessions (tcp_live | ram_offline) + Marker → Auswertung
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `profiles/bmw_nbt_evo.json` | Erwartungen; **P1c noch nicht** auf hu-probe-Feld nachgezogen |
| `docs/feld/2026-10-15-*.md` | S0/S2/Offline/Übergabe |
| `sessions/*_bmw_s0_plug_enum` / `*_bmw_s2_prefetch` | Rohdaten |

## Konfiguration und Parameter

| Parameter | Wert (hu-probe Feld) | Epistemik |
|-----------|----------------------|-----------|
| File-Gap-p50 S0 / S2 | ~3739 µs / ~3783 µs | `MEASURED` Messgröße — **nicht** neuer Scheduler-FACT |
| Read-Event n mode | 4096 dominant | `MEASURED` |
| READ10 blocks | oft 8 (=4096 B), auch 240 | `MEASURED` CBW |
| ms6 / capacity | 2,0 (vor und nach Stall-Fix) | `MEASURED` HU |
| Writes | keine gesehen | `MEASURED` |
| Prefetch lead ~15 s | — | `INFERRED` (PiDrive-Erbe) |
| Burst file-reads p50 39 | Cluster vorhanden | `INFERRED`; Konstante `REJECTED` |
| Eager / Cache-Hit | — | `needs_field` / `INFERRED` |

Profil-Upstream: weiter gemischt PiDrive-`class: FACT` — Update = **P1c offen**
(`EVID-HUPROBE-2026-10-15-013`).

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| S0 Transport: Gap~3739 µs, 4 KiB-Events, tinyusb, dropped=0 | `EVID-HUPROBE-2026-10-15-001` | `MEASURED` |
| S2 Transport ≈ S0 (~3783 µs) | `003` | `MEASURED` |
| READ10 blocks 8 und 240; Event-Chunk-Split | `004` | `MEASURED` |
| ms6/cap=2,0 HU; Stalls vor Fix ≠ HU-Recovery | `005`, `006` | `MEASURED` / `REJECTED` |
| Gap als Scheduler-Pace | `008` | `INFERRED` |
| Burst-39 konstant | `009` | `REJECTED` |
| Prefetch/Eager/Cache | `010` | `INFERRED` |
| Read-Kind-Gaps file/fat/dir/boot | `011` | Zahlen `MEASURED`; Deutung `UNKNOWN` |
| Mount→INQUIRY ~1 s; TUR-Hz session-weit ~2 | `012` | `MEASURED` (Fenster ≠ Profil-idle) |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-15 S0 | Autoplay-Bursts trotz WiFi-Gelb brauchbar |
| 2026-10-15 S2 | Autoplay oft Track 3; Tippen↔kurze Grün-Fenster; Semantik offen |
| 2026-10-15 | Marker oft nachgezogen — Erzählreihenfolge ok, Mikrozeit nicht |

## Abweichungen vom „Lehrbuch“ / PiDrive-Profil

- `gap_ms_p50≈4` war ms-quantisiert — hu-probe liefert µs-Messgröße; Scheduler-Deutung getrennt.
- `read_size_bytes_mode=4096` darf nicht Event-Chunk und CBW-blocks vermengen.
- Semantik-FACTs im Profil (`eager_eof`, `prefetch_lead_s`, `cache_hit_*`) bleiben Herkunft PiDrive bis Formalauswertung.

## Offene Fragen

- P1c Profil-Update Upstream
- S2 LBA/Marker-Formal (Prefetch-Beweis)
- S3 Cache · S1 Eager ≥4 MiB
- HU-Aus während Grün (Kausalität / Power P2c)

## Verwandte Applications / Methods

- [`usb-msc.md`](usb-msc.md) · PiDrive [`bmw-nbt-evo`](../../pidrive/applications/bmw-nbt-evo.md)
- Sheet [`bmw-nbt-evo`](../../../technologies/bmw-nbt-evo/SHEET.md) (nur A)
- Method [`msc-host-read-semantics`](../../../methods/msc-host-read-semantics.md)
