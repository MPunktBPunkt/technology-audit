# Project Application: bmw-nbt-evo in hu-probe

```yaml
project_id: hu-probe
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/hu-probe-psram-board-free-2026-10-21/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R3   # Transport + demo_v1 free Grammar MEASURED; Prefetch large OPEN
  reusability: W1
```

## Rolle im Projekt

**BMW NBT Evo** ist der Golden-Host für hu-probe (Profil `bmw_nbt_evo`). Die Sonde
misst Host-Reads am OTG; PiDrive-Semantik ist **Anker**, nicht automatischer
hu-probe-`FACT`. PiDrive-C:
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
| `profiles/bmw_nbt_evo.json` | Erwartungen schema 3; free-/TUR-/Atom-FACTS 2026-10-20 |
| `docs/feld/2026-10-15-*.md` | S0/S2 |
| `docs/feld/2026-10-18-*.md` / `2026-10-20-bmw-free-offline-0.2.40.md` | CBW-Atom + free Grammar |
| `docs/feld/2026-10-21-feldplan-groessenleiter.md` | präregistrierte Größenleiter |
| `sessions/*_bmw_*` | Rohdaten (lokal) |

## Konfiguration und Parameter

| Parameter | Wert (hu-probe Feld) | Epistemik |
|-----------|----------------------|-----------|
| File-Gap-p50 S0 / S2 | ~3739 µs / ~3783 µs | `MEASURED` — nicht Scheduler-FACT |
| Read-Event n mode | 4096 dominant | `MEASURED` |
| READ10 blocks | 8 und **240**; Rest-bis-EOF z. B. **69** | `MEASURED` CBW |
| Track-Atom demo_v1 | **240+69** = 158208 B / 309 LBA | `MEASURED` |
| TUR Idle-Periode | **2238–2239 ms** (phase-locked) | `MEASURED` free 0.2.40 |
| Prefetch lead demo_v1 | **0** (Idle ohne File-Reads) | `MEASURED`; 15 s **REJECTED** |
| Prefetch lead große Dateien | — | `UNKNOWN` (Größenleiter) |
| next_track 9–18 s (S2 alt) | Resume-Restzeit | **SUPERSEDED** / **REJECTED** als Prefetch |
| tail_then_head | T3→T1 Nearest-LBA | `INFERRED` Elevator; Re-Entry **REJECTED** |
| Writes | keine gesehen | `MEASURED` |
| Cache-Hit A→B→A | bestätigt Serie | `FACT` (Key offen) |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| S0/S2 Transport Gaps, 4 KiB-Events, blocks 8/240 | `EVID-HUPROBE-2026-10-15-001`…`004` | `MEASURED` |
| CBW-Atom 240+69 / 309 LBA / 158208 B | `EVID-HUPROBE-2026-10-18-002` | `MEASURED` |
| free Offline 3× PASS; Idle nur TUR; Atom-Timing | `EVID-HUPROBE-2026-10-21-006`…`009` | `MEASURED` |
| Prefetch-15s demo_v1 | `008` / Profil reject | `REJECTED` |
| Plug→first read ~1,51 s; Media-Loss Burst | `010`, `011` | `MEASURED` |
| Remount Resume; Playlist-T1 Reject; Elevator | `012`, `013` | `MEASURED` / `INFERRED` / `REJECTED` |
| Fenster A8 / Größenleiter | `017` | `HYPOTHESIS` OPEN |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-15 S0/S2 | Transport belastbar; Semantik damals offen |
| 2026-10-18 Abend | Offline PASS; Atom + Hold-Order |
| 2026-10-20 free | Grammar geschlossen; Multi-Review §7 Nachrechnung |
| 2026-10-21 | Audit PSRAM/Board/Profil; Größenleiter präreg. offen |

## Abweichungen vom „Lehrbuch“ / PiDrive-Profil

- `gap_ms_p50≈4` war ms-quantisiert — hu-probe liefert µs; Scheduler getrennt.
- Event n=4096 ≠ CBW-Länge.
- R21 ~15 s Prefetch gilt **nicht** für 158 KiB demo_v1; große Dateien separat.
- `eager_eof` / Cache-Key bleiben Herkunft/offen bis Größenleiter + ident_b.

## Offene Fragen

- Größenleiter H-A/B/C (`seq_size`)
- Elevator-Test Rückwärtssprung ohne Wrap
- Cache-Key Replug `ident_b`
- audible-Marker → GATE-01 Restlatenz
- A7 512-KiB auf hu-probe nachmessen

## Verwandte Applications / Methods

- [`usb-msc.md`](usb-msc.md) · PiDrive [`bmw-nbt-evo`](../../pidrive/applications/bmw-nbt-evo.md)
- Sheet [`bmw-nbt-evo`](../../../technologies/bmw-nbt-evo/SHEET.md) (nur A)
- Audits [`hu-probe-bmw-s0s2-field-2026`](../../../audits/hu-probe-bmw-s0s2-field-2026/) ·
  [`hu-probe-bmw-s2-abend-offline-2026-10-18`](../../../audits/hu-probe-bmw-s2-abend-offline-2026-10-18/) ·
  [`hu-probe-psram-board-free-2026-10-21`](../../../audits/hu-probe-psram-board-free-2026-10-21/)
- Method [`msc-host-read-semantics`](../../../methods/msc-host-read-semantics.md)
