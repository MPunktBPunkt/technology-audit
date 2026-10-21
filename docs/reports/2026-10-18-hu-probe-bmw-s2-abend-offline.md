# hu-probe — BMW S2 Abend-Offline 2026-10-18

**Audit-Nachrechnung + Übergabe an die nächste KI**

| Feld | Wert |
|------|------|
| Repo | `MPunktBPunkt/hu-probe` @ **`5e60303`** (PR #4) |
| FW | **0.2.30** · Probe `.89` |
| Audit | [`audits/hu-probe-bmw-s2-abend-offline-2026-10-18/`](../../audits/hu-probe-bmw-s2-abend-offline-2026-10-18/) |
| Rohdaten | lokal `sessions/20261018-*_bmw_s2_prefetch/` (nicht in Git) |
| Meta | [`session-summaries.json`](../../audits/hu-probe-bmw-s2-abend-offline-2026-10-18/session-summaries.json) |

Eingang: Feldbericht + Mistral-Review + GPT-Review.  
Ausgang: **CBW-Atom bestätigt**, **312/„3 Meta“ beerdigt**, Hold erklärt, P0 unverändert scharf.

---

## 1. Kurzfazit

Drei Offline-PASS am Auto sind real. Das gesuchte Muster ist schärfer als „ein 39er“:

> **Jeder volle Track-Load = genau zwei READ10: `(head, 240) + (head+240, 69)` = 309 LBA = 158208 B.**  
> Die „39 Reads“ sind `bot_data`-Chunks (38×4096 + **1×2560**), nicht 39× READ10(8).

Hold auf T1 kehrt nur die **CBW-Reihenfolge** um (69 zuerst, dann 240) — keine dritte Geometrie.

`212635` bleibt der beste Prefetch-Kandidat (Hold-2-Protokoll, T3-Buffer), aber **kein Beweis**.

---

## 2. Was die Rohdaten wirklich zeigen

### 2.1 Offline-PASS (FACT)

| Session | complete | Order | CBWs | kinds |
|---------|----------|-------|------|-------|
| `175203` | yes | head_then_tail | (627,240)+(867,69) | 39× file |
| `212136` | yes | **tail_then_head** | (249,69)+(9,240) | 34 file + 4 dir + 1 fat |
| `212635` | yes | head_then_tail | (627,240)+(867,69) | 39× file |

FAIL mit gleichem Atom: `175404`, `211058`, `211811` (Footer/Upload).  
Truncated: `211423` (37 events — 240er-CBW unvollständig).

### 2.2 Zahlkorrektur (wichtig)

| Größe | Multi-KI / Bericht | Nachrechnung | Klasse |
|-------|-------------------|--------------|--------|
| Event-Count | 39 | **39** | FACT |
| Event-Bytes | 39×4096 = 159744 | **38×4096 + 2560 = 158208** | FACT korrigiert |
| Covered T3 | 627…938 (312 LBA) | **627…935 (309 LBA)** | FACT korrigiert |
| READ-Starts T3 | 627…931 step 8 | gleich; letzter Start 931 mit **actual=2560** | FACT geschärft |
| CBW | (implizit 39×8) | **240 + 69** | FACT neu/geschärft |
| „3 Meta“ (312−309) | INFERENCE | **REJECTED** — 312 war Zählfehler | — |

Profil-Caveat `also_rest_to_eof_e_g_69` war die richtige Spur — Abend macht sie zum **Track-Atom**.

### 2.3 Track-Karte (CBW)

| Track | head | tail (=head+240) | Δ next head |
|-------|-----:|-----------------:|------------:|
| T1 | 9 | 249 | 309 |
| T2 | 318 | 558 | 309 |
| T3 | 627 | 867 | — |

T2 live: `4028`/`2264` zeigen `(318,240)+(558,69)`. **T2 offline fehlt weiter.**

---

## 3. Muster (kanonisch für nächste KI)

### M1 — Track-Load-Atom (FACT)

```
READ10(head, 240) → 30 × 4096 bot_data
READ10(head+240, 69) → 8 × 4096 + 1 × 2560 bot_data
Sum = 39 events = 309 LBA = 158208 B
```

Operativ: ein Offline-Lauf „sieht richtig aus“, wenn genau **dieses Paar** einmal im Buffer liegt — nicht weil „39=PASS“, sondern weil ein voller Track-Load so aussieht. FAIL kann dasselbe Paar ohne Footer haben.

### M2 — Zwei Orders, eine Geometrie (FACT)

| Order | Beispiel | Erscheinung auf Event-Ebene |
|-------|----------|-----------------------------|
| `head_then_tail` | T3 `175203`/`212635` | monotone Step-8-Kette, rein `file` |
| `tail_then_head` | T1-Hold `212136` | Sprung −296 nach Tail, dann Head; dir/fat am Kopf (LBA 9…41) |

**Nicht tun:** T1b als eigene Start-Karte „~249“ neben 9/318/627 führen.  
**Tun:** Order-Label (`head_then_tail` / `tail_then_head`).

### M3 — Entkopplung Hold vs. USB (`212635`, INFERENCE stark)

Operator: Start 1 → AP 2 → Hold 2. Buffer: T3-Atom.  
Kandidaten: Prefetch-Ahead · Autoplay schon bei T3 · früherer T3-Miss.  
Ohne Marker + B7-Fix nicht entscheidbar.

### M4 — Ein-Track-Halten (INFERENCE operativ)

Weniger Magenta/NEED_RESET als Multi-Track-Nachmittag — plausibel, nicht kontrolliert gegengeprüft.

---

## 4. Abgleich Mistral / GPT

| Punkt | Bewertung |
|-------|-----------|
| 3× Offline-PASS, T3 reproduziert | bestätigt |
| Zwei Morphologien | bestätigt, aber **als Order**, nicht als zwei Geometrien |
| T1a/T1b-Split (B10) | sinnvoll als Order-Alias; Band-Karte nicht aufspalten |
| B11 FAT/309-vs-312 | **312 beerdigt**; Medien-Image optional, CBW entscheidet schon |
| B9/M3 Diskriminierung | übernommen als P0 |
| B12 Rohdaten nicht im Repo | bleibt; Summaries jetzt im Audit |
| „Offline-PASS ⟺ genau ein 39er“ als HU-Gesetz | mit GPT: **nicht** kausal überhöhen |
| GPT P0 „direkt T2 starten“ | bestes nächstes Experiment |

---

## 5. Ampel

| Bereich | Status |
|---------|--------|
| Offline-Integrity BMW (3× PASS) | 🟢 |
| Track-Atom 240+69 / 309 LBA | 🟢 FACT |
| T3 offline | 🟢 |
| T1 Hold offline (Reverse-Order) | 🟢 |
| T2 live CBW | 🟢 · offline 🟠 |
| 312 / „3 Meta“ | ⚫ REJECTED |
| 39×4096-Byteformel | ⚫ korrigiert → 158208 |
| M3 Prefetch-Kandidat | 🟡 |
| B7 Offline-Timing | 🟠 |
| GATE-01 Prefetch-Lead | 🔴 OPEN |

---

## 6. Auftrag an die nächste KI

### P0 — Ein kontrollierter T2-Hold (höchster Ertrag)

```
frischer RST
→ Offline ARM (kein RST im Capture)
→ Start direkt bei Track 2 (nicht 1→2)
→ Hold 2
→ Marker: play_start, hold_2, audible_change (falls FW)
→ 90–120 s
→ Stop
```

| Ergebnis | Bedeutung |
|----------|-----------|
| `(318,240)+(558,69)` | T2 offline FACT; M3 nicht reproduziert |
| `(627,240)+(867,69)` unter echtem Hold-2 | Prefetch-/Vorablese-Evidenz steigt stark |
| T1 Reverse-Order | Hold-Mechanismus/Position, nicht Prefetch |
| kein/partial Burst | Cache-Hit / Fenster / Truncation prüfen |

### P0b — B7

`capture_t_us` von Replay trennen. Vorher keine Prefetch-Lead-Zahlen.

### P1

- Session-Meta (CBW-Paar, order, kind_counts, covered, bytes) versionieren — Muster wie `session-summaries.json`.
- Terminologie in Feldberichten: Order statt T1a/T1b-Band.
- Optional: Dateigrößen im Medien-Image (nicht mehr für 312-Frage nötig).

### P2

Hold auf T2 und T3: bleibt Reverse-Order? Bleibt dir/fat am 240-Kopf?

### Nicht tun

- `212635` als „T2 verfehlt, egal“ ablegen
- 39-Start-Zahlen zwischen Orders mischen
- Offline-Gaps für Pace/Prefetch-Lead verwenden
- „3 Meta-Blöcke“ weiter argumentieren
- 39×4096 als Byte-Summe annehmen, ohne `actual` des letzten Chunks

---

## 7. Epistemik (Stand)

| Aussage | Klasse |
|---------|--------|
| 3× Offline-PASS am BMW | FACT |
| Track-Load = 240+69 CBW | FACT |
| 39 bot_data / Load, letzter 2560 B | FACT |
| Covered = 309 LBA / 158208 B | FACT |
| Hold = CBW-Order reverse | FACT (n≥1 PASS + Repros) |
| T2 offline | OPEN |
| Prefetch während Hold-2 | starke INFERENCE |
| 312 LBA / 3 Meta | REJECTED |
| 39 = globale HU-Konstante | REJECTED |
| Offline Gap=0 = HU-Pace | REJECTED |
| GATE-01 geschlossen | NEIN |

---

## 8. Eine Zeile für den Kontext der nächsten KI

**Hu-probe Abend 0.2.30:** Offline-PASS reproduziert; Track-Atom ist **240+69**; „39er“ = Chunks inkl. Partial; Hold dreht nur die Order; nächster Lauf = **direkt T2 halten** (+ Marker), nicht noch ein unkontrollierter 90-s-Arm.
