# MSC Host-Read-Semantik S1–S3 · Desk 2026-10-15

**Standard:** 0.7.1  
**Kampagne:** [`msc-host-read-semantics-s1s2s3-2026`](../../audits/msc-host-read-semantics-s1s2s3-2026/)  
**Method:** [`msc-host-read-semantics`](../../methods/msc-host-read-semantics.md)

## Ergebnis

Messplan und Auswerteskript-Spez für hu-probe **S1/S2/S3** — ohne neue NBT-Zahlen.
PiDrive-Profilwerte (`eager_eof`, `prefetch_lead_s≈15`, `cache_hit`) sind
**Herkunftshypothesen**, nicht hu-probe-`FACT`.

| Deliverable | Inhalt |
|-------------|--------|
| Marker | `play_start`, `track_next`, `audible_change`, `replay`, `stop` |
| Regeln | LBA-Monotonie · Bytes-bis-EOF · Reads-vor-hörbarem-Wechsel · Replay-ohne-Replug |
| Medium S1 | Mess-Slots ≥ 4 MiB; 512 KiB nur Kontrolle |
| Claim-Tabelle | hypothesis / superseded / needs_field |

## Primärquellen (Pins)

| Quelle | Pin | Nutzen |
|--------|-----|--------|
| hu-probe | `463c0f0…` | Profil + Szenarien |
| pidrive | `8223719…` | R21 ~15 s [S], Eager-ANALYSE, G4N |
| technology-audit | pre-Kampagne + diese | A/B/C, HU-A1…, gadget-refs |
| tinyusb / IDF / esp32usbmsc | siehe Evidence | `tud_msc_read10_cb` / Virtual FAT |

## Kill (unverändert)

fremde Host-Muster ≠ NBT-FACT · PiDrive-Zahlen ≠ hu-probe-FACT · keine Wire-Claims ·
Linux-Read-Ahead ≠ NBT-Prefetch.

## Nächster Schritt

Feld/Lab-Sessions nach Instrument-Freigabe (GATE-01); Auswerteskript gegen
`derived/s1s2s3_eval.json`; neue Evidence-IDs nur aus Läufen.
