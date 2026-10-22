# Project Application: bmw-nbt-evo in hu-probe

```yaml
project_id: hu-probe
tech_slug: bmw-nbt-evo
status: active
sheet: ../../../technologies/bmw-nbt-evo/SHEET.md
audit: ../../../audits/hu-probe-media-ladder-2026-10-22/
maturity:
  technology: R2
  implementation: R0
  field_evidence: R3   # Transport + demo_v1 free + Media-Leiter Phasen MEASURED; A8/Identity OPEN
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
| `profiles/bmw_nbt_evo.json` | Erwartungen schema 3; free-/TUR-FACTS; Head/Prefetch-Leiter noch nachziehen |
| `docs/feld/2026-10-15-*.md` | S0/S2 |
| `docs/feld/2026-10-18-*.md` / `2026-10-20-bmw-free-offline-0.2.40.md` | CBW-Atom + free Grammar |
| `docs/feld/2026-10-21-feldplan-groessenleiter.md` | präregistrierte Größenleiter A8 |
| `docs/feld/2026-10-22-bmw-media-ladder-live.md` | Media-Leiter Live |
| `docs/feld/2026-10-22-gesamtbericht-media-ladder-pruefung.md` | Wire + Multi-KI @ `8234982` |
| `sessions/*_bmw_*` | Rohdaten (lokal) |

## Konfiguration und Parameter

| Parameter | Wert (hu-probe Feld) | Epistemik |
|-----------|----------------------|-----------|
| File-Gap-p50 S0 / S2 | ~3739 µs / ~3783 µs | `MEASURED` — nicht Scheduler-FACT |
| Read-Event n mode | 4096 dominant | `MEASURED` |
| READ10 blocks | 8, **32+128 (Head)**, **240** Bulk; Rest-bis-EOF z. B. **69** | `MEASURED` CBW |
| Track-Atom demo_v1 | **240+69** = 158208 B / 309 LBA | `MEASURED` |
| Scan-Head | **32+128 = 160 Blöcke ≈ 80 KiB** | `FACT` (`EVID-HUPROBE-2026-10-22-002`) |
| TUR Idle-Periode | **2238,78 ms** (phase-locked) | `FACT` (Offline `…-19-001` + Live `…-22-006`); „~1/s“ `REJECTED` |
| Mount-Signatur | 32 TUR, 11 READ10 inkl. 2× LBA 24/8 | `FACT` (`…-19-002`); 24/8 Zweck `UNKNOWN` |
| Prefetch lead demo_v1 | **0** (Idle ohne File-Reads) | `MEASURED`; 15 s **REJECTED** |
| Prefetch große / Leiter | Tail 160 @ off 160 im Track-Rhythmus; Lead ~7,5–8 s | `FACT` Struktur / Lead **VARIABLE** (`…-22-004`/`005`) |
| next_track 9–18 s (S2 alt) | Resume-Restzeit | **SUPERSEDED** / **REJECTED** als Prefetch (`…-19-004` umgedeutet) |
| Auswahllatenz | 1,7–1,9 s manuell, ≈0,2 s Autoplay | `MEASURED` (`…-19-005`) |
| tail_then_head | Nearest-LBA / Elevator | **STRONG** (`…-22-007`); Re-Entry **REJECTED** |
| Browse vs Player | 8.3 Dir vs ID3 Head | `FACT` (`…-22-008`) |
| „Nur Ordnerstruktur“ | — | **REJECTED** (`…-22-010`) |
| Media-Loss-Grammatik | TUR(1)→REQUEST_SENSE→PREVENT(1) | `FACT` (`…-19-007`); „Enum-Grammatik“ `REJECTED` |
| Writes | keine gesehen | `MEASURED` |
| Cache-Hit A→B→A | bestätigt Serie | `FACT` (Key offen) |
| Fenster A8 / `seq_size` | 240,240,32 @~16,4 s | `HYPOTHESIS` OPEN (`…-22-013`) |

Profil-Upstream: **P1c closed 2026-10-17** — Transport `origin: hu_probe_field`; free-FACTS 2026-10-20; Leiter-FACTs 2026-10-22 im Quellrepo (Profil-Nachzug FOLLOW-ON).

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| S0/S2 Transport Gaps, 4 KiB-Events, blocks 8/240 | `EVID-HUPROBE-2026-10-15-001`…`004` | `MEASURED` |
| ms6/cap=2,0 HU; Stalls vor Fix ≠ HU-Recovery | `005`, `006` | `MEASURED` / `REJECTED` |
| Burst-39 konstant | `009` | `REJECTED` |
| TUR-Leerlauf 2,239 s; Mount-Signatur / LBA 24/8 | `2026-10-19-001`…`003` | `FACT` / `UNKNOWN` |
| Media-Loss-Grammatik (statt Enum) | `2026-10-19-007` | `FACT` |
| B7/B21 Instrument-Ursachen | `2026-10-19-009` | `FACT` |
| CBW-Atom 240+69 / 309 LBA / 158208 B | `EVID-HUPROBE-2026-10-18-002` | `MEASURED` |
| free Offline 3× PASS; Idle nur TUR; Atom-Timing | `EVID-HUPROBE-2026-10-21-006`…`009` | `MEASURED` |
| Prefetch-15s demo_v1 | `008` / Profil reject | `REJECTED` |
| Plug→first read ~1,51 s; Media-Loss Burst | `010`, `011` | `MEASURED` |
| Remount Resume; Playlist-T1 Reject | `012`, `013` | `MEASURED` / `REJECTED` |
| Media-Leiter Head 32+128; Tail-Prefetch; Bulk 240; TUR Live | `2026-10-22-002`…`006`, `012` | `FACT` / `MEASURED` |
| Elevator STRONG `cache_place` | `2026-10-22-007` | STRONG / Re-Entry `REJECTED` |
| Nur-Struktur REJECT; PiDrive Struktur+Head | `2026-10-22-010` | `REJECTED` / Vertrag |
| Fenster A8 / Größenleiter formal | `017` (21.10.) / `013` (22.10.) | `HYPOTHESIS` OPEN |

## Beobachtungen (Lab / Feld)

| Datum / Artefakt | Beobachtung |
|------------------|-------------|
| 2026-10-15 S0/S2 | Transport belastbar; Semantik damals offen |
| 2026-10-18 Abend | Offline PASS; Atom + Hold-Order |
| 2026-10-19 | TUR/Mount/Media-Loss Evidence `…-19-*` |
| 2026-10-20 free | Grammar geschlossen; Multi-Review §7 Nachrechnung |
| 2026-10-21 | Audit PSRAM/Board/Profil; Größenleiter präreg. offen |
| 2026-10-22 | Media-Leiter Live: Scan-Head + Prefetch-Phasen; PiDrive-Vertrag |

## Abweichungen vom „Lehrbuch“ / PiDrive-Profil

- `gap_ms_p50≈4` war ms-quantisiert — hu-probe liefert µs; Scheduler getrennt.
- Event n=4096 ≠ CBW-Länge.
- R21 ~15 s Prefetch gilt **nicht** für 158 KiB demo_v1; große Dateien: Prefetch ja, Lead nicht konstant 8/15 s.
- „Nur Struktur“ war zu grob — Head ~80 KiB ist Pflicht.
- `eager_eof` / Cache-Key / A8-Refill-Takt bleiben Herkunft/offen bis Identity + `seq_size`.

## Offene Fragen

- audible-Marker → GATE-01 Restlatenz / Lead-Anker
- Analyzer B47 Scan vs Prefetch in Compare
- Formal H-A/B/C auf `seq_size` / A8
- Elevator-Drittstichprobe; Cache-Key Replug `ident_b`
- A7 512-KiB auf hu-probe nachmessen

## Verwandte Applications / Methods

- [`usb-msc.md`](usb-msc.md) · PiDrive [`bmw-nbt-evo`](../../pidrive/applications/bmw-nbt-evo.md)
- Sheet [`bmw-nbt-evo`](../../../technologies/bmw-nbt-evo/SHEET.md) (nur A)
- Audits [`hu-probe-bmw-s0s2-field-2026`](../../../audits/hu-probe-bmw-s0s2-field-2026/) ·
  [`hu-probe-bmw-s2-abend-offline-2026-10-18`](../../../audits/hu-probe-bmw-s2-abend-offline-2026-10-18/) ·
  [`hu-probe-psram-board-free-2026-10-21`](../../../audits/hu-probe-psram-board-free-2026-10-21/) ·
  [`hu-probe-media-ladder-2026-10-22`](../../../audits/hu-probe-media-ladder-2026-10-22/)
- Method [`msc-host-read-semantics`](../../../methods/msc-host-read-semantics.md)
