# Evidence — hu-probe-bmw-s2-abend-offline-2026-10-18

Abend Offline BMW S2 · FW **0.2.30** · standard **0.7.1** · Profile `lab-tool`  
Pin: `hu-probe@5e60303` (PR #4). Roh-`events.jsonl` lokal beim Collector (gitignored);
replizierbare Meta: [`session-summaries.json`](session-summaries.json).

**Epistemik:** Device-Stack CBW/`bot_data`, nicht Wire. Prefetch ≠ FACT ohne Marker+Timing.

## Quellen-Snapshots

| Artefakt | Pin / Ort | Rolle |
|----------|-----------|-------|
| https://github.com/MPunktBPunkt/hu-probe | `5e60303` | Docs + Profil |
| PR #4 | merged 2026-10-18 | Abendbericht |
| `docs/feld/2026-10-18-bmw-s2-abend-offline.md` | @ `5e60303` | Operator-Bericht |
| `docs/feld/2026-10-18-bmw-s2-0.2.30-multi-ki-review.md` | @ `5e60303` | Multi-KI (Zahlen teilweise zu korrigieren) |
| Lokale Sessions | `sessions/20261018-{175203,175404,211058,211423,211811,212136,212635}_bmw_s2_prefetch` | Rohdaten |
| Live-Stichprobe | `4028`, `2264`, `8630`, `2995` | T2-Band / Order-Vergleich |
| Mistral + GPT Reviews | Chat 2026-10-18 | Hypothesen M1–M3, B9–B12 |

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-HUPROBE-2026-10-18-001` | Drei BMW Offline Integrity-PASS (`complete=true`): `175203`, `212136`, `212635`. Transport `ram_offline`, overflow=0, FW 0.2.30. | `MEASURED` | Sessions; Abendbericht |
| `EVID-HUPROBE-2026-10-18-002` | Pro vollem Track-Load: genau **2 READ10-CBWs** mit `(lba_head, 240)` + `(lba_head+240, 69)` = **309 LBA** = **158208 B**. Event-Ebene: **39** `bot_data` = 38×4096 + **1×2560**. | `MEASURED` / korrigiert | `175203`, `212635` (+ FAIL-Repros) |
| `EVID-HUPROBE-2026-10-18-003` | Track-Köpfe: T1=`9`, T2=`318`, T3=`627` (Δ=309). Tail-Starts: `249`/`558`/`867` (= head+240). Live `4028`/`2264`/`2995` bestätigen T2-Paar `(318,240)+(558,69)`. | `MEASURED` | Live + Offline |
| `EVID-HUPROBE-2026-10-18-004` | „Burst = 312 LBA / 39×4096=159744 / covered …938 / 3 Meta“: **REJECTED** als Byte-/Covered-FACT. Ursache: letzter Chunk der 69er-CBW ist 2560 B → covered Ende = head+308 (T3: **627…935**). 312 entstand aus 39×8 ohne Partial. | `REJECTED` (alte Formel) | Nachrechnung vs. Multi-KI §1.1 |
| `EVID-HUPROBE-2026-10-18-005` | T1-Hold (`212136`, Repros `211811`/`211423`): dieselben CBWs `(249,69)` dann `(9,240)` — **tail_then_head**. Kind-Mix 34 file + 4 dir + 1 fat sitzt am Kopf der 240er-CBW (LBA 9…41). Nicht-Monotonie = Order, keine neue Geometrie. | `MEASURED` | Offline Hold-Sessions |
| `EVID-HUPROBE-2026-10-18-006` | `212635`: Operator Hold-2, Buffer = T3 head_then_tail `(627,240)+(867,69)`. Prefetch-Ahead = **starke INFERENCE**, nicht FACT. Alternativen Autoplay-Vorlauf / früherer Cache-Miss offen. | `MEASURED` (Buffer) / Prefetch `INFERRED` | Abendbericht + Session |
| `EVID-HUPROBE-2026-10-18-007` | Offline `t_us` kollabiert (oft 1 unique über alle `bot_data`) → Gap-p50 ~367x µs ist Replay-/Capture-Artefakt-fähig (B7). LBA/CBW weiter belastbar. | `MEASURED` (collapse) | alle Offline-Sessions |
| `EVID-HUPROBE-2026-10-18-008` | FAIL-Läufe reproduzieren oft volles CBW-Muster ohne Footer (`175404`,`211058`,`211811`); `211423` = truncated (37 events, 240er-CBW unvollständig). „39 im Band“ ≠ PASS-Bedingung. | `MEASURED` | Offline FAIL-Set |

## Claim-Diff vs. Mistral / GPT / Feldbericht

| Claim | Abendbericht / KI | Diese Nachrechnung |
|-------|-------------------|---------------------|
| Offline 3× PASS | FACT | **bestätigt** `001` |
| genau ein 39er pro PASS | FACT (operativ) | **bestätigt** auf Event-Ebene; schärfen: 39 = Chunks, Atom = 2 CBW |
| T3 Starts 627…931 / cov 627–938 / 159744 B | FACT | **korrigiert**: Starts inkl. 931 (Partial); covered **627…935**; **158208 B**; 309 LBA |
| 312 vs 309 → „3 Meta“ | INFERENCE offen | **312-Modell REJECTED**; 309 = 240+69 FACT |
| T1b ~249 Hold-Mix eigene Morphologie | FACT | **FACT als Order-Morphologie**; Geometrie = T1-Paar reversed |
| 34+4+1 kind split | FACT | **bestätigt** `212136` |
| 212635 Prefetch | starke INFERENCE | **unverändert** `006` |
| T2 offline offen | OPEN | **unverändert**; Live T2 CBW bestätigt `003` |

## Track-Atom (kanonisch)

| Track | CBW1 | CBW2 | Order (typ. Autoplay) | Order (Hold gesehen) |
|-------|------|------|------------------------|----------------------|
| T1 | (9, 240) | (249, 69) | head_then_tail | **tail_then_head** (`212136`) |
| T2 | (318, 240) | (558, 69) | head_then_tail (live) | offline offen |
| T3 | (627, 240) | (867, 69) | head_then_tail | — (`212635` trotz Hold-2-Absicht) |

Terminologie-Vorschlag (ersetzt B10 teilweise):

- **T1-head_then_tail** / **T1-tail_then_head** statt T1a/T1b als Band-Karte.
- „T1b“ nur noch als Alias für Reverse-Order, nicht für Start≈249 als eigenen Track.

## Offene Claims

| Claim | Status | Nächster Test |
|-------|--------|---------------|
| T2 offline head_then_tail | OPEN | P0 direkt T2 Hold |
| Prefetch während Hold-2 | INFERRED | P0 + Marker + B7 |
| dir/fat am 240-Kopf = Classifier vs. echte Meta-Reads | INFERRED | Medien-Map / kind-Grenzen |
| Hold Reverse auch auf T2/T3? | UNKNOWN | P2 |

## Maschinenlesbare Summaries

Siehe [`session-summaries.json`](session-summaries.json) — Felder u. a. `read10_file_cbws`, `order`, `kind_counts`, `covered_lba`, `bytes`, `start_lbas`.
