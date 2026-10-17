# Evidence — pidrive-2026-10-17-prefetch-livelock

Rohdaten bleiben in `pidrive`. Pin: **`pidrive@d50196e`**, FW **`0.4.53-dev`**,
Stall aus, UART nein. Primärquelle Konsens:
[`TRI-REVIEW-ABEND-2026-10-17.md`](https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/TRI-REVIEW-ABEND-2026-10-17.md).

Feldordner:
[`feld-go-abend-01/`](https://github.com/MPunktBPunkt/pidrive/tree/d50196e/docs/betrieb/artifacts-2026-10-17-feld/feld-go-abend-01)
· Status: `…/status/status-*.json` · Polls: `…/m20-repro/poll-*.jsonl`.

Nachrechnung (dieser Audit-Lauf): alle 17 Status-Snapshots + Poll
`poll-replug-1757.jsonl` gegen TRI-Review-Muster geprüft — bestätigt.

| ID | Claim (Kurz) | Status | Quelle | Review Check |
|----|--------------|--------|--------|--------------|
| `EVID-BMWHU-2026-10-17-001` | Über alle Abend-Status: `readCount − playRejectCount ∈ {31,32}` (14×31, 3×32) | `MEASURED` | `feld-go-abend-01/status/status-*.json` · TRI-Review §2 | Alerts nicht nur auf Reads/Rejects |
| `EVID-BMWHU-2026-10-17-002` | `(167,136)` + `prefetchHits≈8` = **Quiet-Plateau** (after-plug, post-Ton, Stuck-ohne-Ton) — kein Stuck-allein-Marker | `MEASURED` | u. a. `status-1752-after-plug`, `status-bayern-ton-175402`, `status-bayern-notone-180227`, `status-replug-180335` | Zusatzachsen pref/stream/midFile/Ohr |
| `EVID-BMWHU-2026-10-17-003` | Zwei Stuck-Morphologien: **Quiet** (`pref≈8`) vs **Storm** (`pref` 200–2200+, `fav0.midFile` 600–2054, `bytesFile` bis ~9 MiB) | `MEASURED` | Quiet: `bayern-notone`, `replug-180335` · Storm: `tip-rock-175732`, `rst-rock-180559`, `all-files-175913`, `stuck-1801` | Stuck-Capture muss Morphologie loggen |
| `EVID-BMWHU-2026-10-17-004` | `bytesDir/Fat/Meta/Boot` = **57344 / 44544 / 114688 / 12800** in allen 17 Snapshots; Livelock-Delta sitzt in `bytesFile` | `MEASURED` | alle `status-*.json` · TRI-Review §3.3 | Kein Meta-Rescan-Claim ohne steigende Meta-Bytes |
| `EVID-BMWHU-2026-10-17-005` | Guess mitten im Storm: `poll-replug-1757` @ **17:58:21** `guess 0→1`, `play=Rock Antenne Bayern`, `stream_active=true` bei `rej` 2025→2057 (fav0 bereits ~8 MiB) | `MEASURED` | [`poll-replug-1757.jsonl`](https://github.com/MPunktBPunkt/pidrive/blob/d50196e/docs/betrieb/artifacts-2026-10-17-feld/feld-go-abend-01/m20-repro/poll-replug-1757.jsonl) | Livelock ≠ Guess-unmöglich |
| `EVID-BMWHU-2026-10-17-006` | `fromHead` nur **0 oder 2**; Mid-file dominiert (z. B. fav1 post-Ton: `fromHead=2`, `midFile=126`, `bytes=524288`) | `MEASURED` | `slotMap` in Status-Snapshots · TRI-Review §3.4 | Head-Commit = Ausnahme |
| `EVID-BMWHU-2026-10-17-007` | fav2 oft voll vorgelesen (`bytes=524288`, `fromHead=2`, `midFile=126`) in 11/17 Snapshots — auch ohne `playingName` / mit `streamSlot=-1` | `MEASURED` | u. a. `1752-after-plug`, `1751-otg-out`, Storm-Snapshots · TRI-Review §3.5 | Scan/Prefetch ≠ Play |
| `EVID-BMWHU-2026-10-17-008` | hostAbs-Overshoot nach Tonfenster: `bayern-ton-175402` hostAbs **592164** vs expect **524288** (+67876); `bayern-ton2/3` Overshoot **+859417** (~859 KiB) | `MEASURED` | `status-bayern-ton-*.json` · M27 · TRI-Review §3.6 | Cursor-Modell; kein stiller Decoder-Claim |
| `EVID-BMWHU-2026-10-17-009` | Status-Poll-Lücken in `m20-repro`: max Gap typisch &lt;5 s (1757 max 3,1 s; 1759 max 4,6 s; bob-retry ein Gap 5,25 s) — 29‑s-Pause nicht in diesen Polls | `MEASURED` | `poll-*.jsonl` · TRI-Review §3.8 | 29 s ggf. Bridge-`msc.reads`-Journal |
| `EVID-BMWHU-2026-10-17-010` | Soft-Serial driftet `PD0305→PD0325` auch über `power_on`-Zyklen; ≠ Panic-Marker | `MEASURED` | Status `usbSerial` / `resetReason` · TRI-Review §3.7 | M24 „Serial gehalten“ nur gate-zeitpunkt |

## Offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| Panic-Ursache | `UNKNOWN` | UART fehlt (P0) |
| Stuck-LBAs / Read-Klasse im Livelock | `UNKNOWN` | braucht MessCapture / Journal |
| Ob nur HU-Power-Cycle Session heilt | `UNKNOWN` | ESP-RST beendet Livelock nicht (Konsens INFERENCE/FACT-Mix — RST beobachtet, Heilung nicht) |
| Welche Read-Klasse den Storm-Guess auslöst | `UNKNOWN` | `005` zeigt Timing, nicht LBA-Klasse |
| Tonfenster vs. Ring exakt (6–7 s vs 8,2 s) | `INFERRED` | Operator vs `liveAvailMs=8192` |
| Persistenter HU/Media-Session-Anteil nach Weiß/Panic | `INFERRED` | Tri-Review Konsens |

## Epistemik (Kampagnen-Stand)

| Klasse | Inhalt |
|--------|--------|
| FACT / MEASURED | `001`–`010`; Panic beobachtet; Meta konstant; Quiet≠Stuck-Marker; Storm-Guess möglich |
| INFERENCE | Prefetch-Livelock-Begriff; HU-persistenter Anteil; Ton ≈ Ringfenster |
| HYPOTHESE | Zweistufiger Handshake (~1 s Scan, ~17–22 s Play-Commit); Identity zeitabhängig |
| UNKNOWN | Panic-Ursache; Stuck-LBAs; Reset-Isolation A–D; Storm-Guess-Auslöser-Klasse |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-17 | Feld Abend `feld-go-abend-01` (M20/M21/M22/M24) |
| 2026-10-17 | Tri-Review GPT/Grok/Mistral + Rohdaten-Nachrechnung → Upstream `d50196e` |
| 2026-10-17 | KB-Audit `pidrive-2026-10-17-prefetch-livelock` gestartet; Patterns als `EVID-BMWHU-2026-10-17-*` |
