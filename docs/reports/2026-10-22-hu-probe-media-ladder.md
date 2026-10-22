# hu-probe — Media-Leiter / Host-Phasen / PiDrive-Vertrag — 2026-10-22

**Delta-Audit seit PSRAM/Board/free 2026-10-21**

| Feld | Wert |
|------|------|
| Repo | `MPunktBPunkt/hu-probe` @ **`8234982`** (Gesamtbericht; Feldkern `e1da0c6`) |
| FW Pin | **0.3.17** · Probe `.89` · `tcp_live` |
| Audit | [`audits/hu-probe-media-ladder-2026-10-22/`](../../audits/hu-probe-media-ladder-2026-10-22/) |
| Prior | [`2026-10-21-hu-probe-psram-board-free`](2026-10-21-hu-probe-psram-board-free.md) |

---

## 1. Kurzfazit

Die Media-Leiter schließt die große Lücke nach dem PSRAM-/free-Update:

1. **Scan liest Köpfe** — typisch **READ10 32+128 = 160 Blöcke (~80 KiB)**; kleine Dateien oft schon im Scan voll. „Nur Ordnerstruktur“ ist **falsch**.
2. **Prefetch existiert** — bei `id3_cover` Tail-Reads **160 @ file_off 160** im Track-Rhythmus (~22,5 / 49,1 / 75,5 s Wire); Lead ~8 s nur **VARIABLE**, demo_v1 Lead=0 bleibt.
3. **TUR 2238,78 ms** Live bestätigt; **Elevator** an `cache_place` **STRONG**; Bulk **240**.
4. **PiDrive:** Struktur + Dateikopf Pflicht; Rest dynamisch unter Größen/FAT — nicht der ganze Inhalt beliebig.
5. **Instrument:** PSRAM-1 MiB + Trip-Replay **0.3.17 PASS** (Heap-Leak weg) — Offline messen, später übertragen; Lab-Replay B50 getrennt FAIL.

Formal **A8/`seq_size`** bleibt OPEN.

---

## 2. Instrument-Kontext (PSRAM → Offline → Transfer)

| Schicht | Stand | Epistemik |
|---------|-------|-----------|
| PSRAM N8R2 / Capture 1 MiB | ab 0.2.35/0.2.37 | FACT (Audit 21.10.) |
| free Offline Grammar demo_v1 | 0.2.40 | FACT |
| TripStore stored-replay Hang | 0.3.3–0.3.15 | geheilt schrittweise |
| EventBus Ring-Leak + Token-Bucket | **0.3.17** Feld-PASS Upload | `EVID-…-011` |
| Media-Leiter selbst | `tcp_live` (nicht Offline) | 5× BMW Integrity PASS |
| Lab Offline Replay | `065150` B50 | FAIL (`009`) |

PSRAM löst Speicherzugriff/Puffer; Coex-Root-Cause bleibt offen. Live-Leiter zeigt: unter dieser Last ist `tcp_live` nutzbar.

---

## 3. Host-Grammatik (Media-Leiter)

### 3.1 Phasenmodell (FACT-Struktur)

```text
Enum → FS-Probes → Directory-Walk → File-Head (32+128)
      → (optional) Tail/Bulk Prefetch → Cache-only Playback
```

### 3.2 Kanonische Muster

| ID | Muster | Klasse |
|----|--------|--------|
| M1 | Head-Scan **32+128** (=160 / ~80 KiB) | FACT |
| M2 | Tail-Prefetch 160 @ off 160, Δt≈Trackdauer (`id3_cover`) | FACT Struktur |
| M3 | Idle: TUR **2238,78 ms** | FACT (Live=Offline) |
| M4 | Bulk-CBW **240** (`bitrate_mix`) | FACT |
| M5 | `tail_then_head` = Elevator (Tail-first bei LBA-Rücksprung) | STRONG |
| M6 | Browse 8.3 (Dir) ≠ Player ID3 (Head) | FACT |
| M7 | „Nur Ordnerstruktur“ | **REJECTED** |
| M8 | Prefetch-Lead ≈8 s | VARIABLE (≠ Konstante; ≠ demo_v1) |
| M9 | Fenster A8 16,4 s-Refill | OPEN (nicht diese Leiter) |

### 3.3 Referenzsession `081152` (`id3_cover`)

| Phase | Messung |
|-------|---------|
| Scan-Heads | Chunks `[[0,32],[32,128]]` je COVER*/NOCOVER |
| Tail-Prefetch | Analyzer t≈20,97/47,55/73,97 s; Wire 22,51/49,09/75,51 s |
| TUR | `period_ms=2238.78`, grid n=59 |

---

## 4. PiDrive-Vertrag (geschärft)

| Ebene | HU-Verhalten | PiDrive-Pflicht |
|-------|--------------|-----------------|
| Directory / FAT | Baum-Walk | stabil |
| Dateianfang | ~80 KiB Head (ID3/MP3) | gültig/konsistent |
| Kleine Files | oft Scan-komplett | Payload schon „verbraucht“ |
| Großer Rest | Prefetch/Bulk später | dynamisch *unter* Size/EOF |
| Browse UI | 8.3 | Directory |
| Player UI | ID3 | Head, nicht Dir-Name |

**Nicht zulässig:** beliebige Audio-Payload hinter gemeldeter Größe.

---

## 5. Ampel

| Bereich | Status |
|---------|--------|
| Live Media-Leiter Integrity | **grün** |
| Head-/Tail-/Bulk-/TUR-FACTs | **grün** |
| Elevator | **gelb→grün** (STRONG; Drittstichprobe offen) |
| PiDrive Struktur+Head | **grün** (Vertrag) |
| Prefetch-Lead Konstante / audible | **gelb** |
| A8 `seq_size` formal | **gelb** OPEN |
| Trip-Replay 0.3.17 | **grün** |
| Lab Offline Replay B50 | **rot** |
| Coex Root-Cause | **unverändert offen** |

---

## 6. Auftrag Next

1. **P0** Audible-Tap (`id3_cover`/`bitrate_mix`) → GATE-01 + Lead-Anker.  
2. **P0** Analyzer **B47**: Scan-Fenster aus Prefetch-Stats.  
3. **P1** Identity/Head-vs-Rest (A→B→A, Remount).  
4. **P1** Lab-Replay **B50**.  
5. **P2** `seq_size` A8; Elevator-Drittstichprobe; HARDWARE §2.3.

**Nicht tun:** Lead=8 s als Profil-Konstante; „nur Struktur“; A8 ohne `seq_size` schließen.

---

## 7. Verweise

- Audit: [`audits/hu-probe-media-ladder-2026-10-22/`](../../audits/hu-probe-media-ladder-2026-10-22/)
- Upstream: `docs/feld/2026-10-22-gesamtbericht-media-ladder-pruefung.md` @ `8234982`
- Prior: [`2026-10-21-hu-probe-psram-board-free`](2026-10-21-hu-probe-psram-board-free.md)
