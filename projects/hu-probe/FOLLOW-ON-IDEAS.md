# Follow-on Ideas: hu-probe

| Idee | Bezug | Hinweis |
|------|-------|---------|
| ~~P1c Profil Upstream~~ | `bmw_nbt_evo.json` schema 3 | **done 2026-10-17**; free-FACTS 2026-10-20 im Quellrepo |
| ~~CBW-Atom 240+69~~ | Abend 18.10. | **done** |
| ~~PSRAM / Board N8R2~~ | Audit 21.10. | **done** (Doc §2.3 Upstream nachziehen) |
| ~~free Offline Grammar demo_v1~~ | 0.2.40 | **done** (Prefetch-15s REJECTED) |
| ~~Media-Leiter Head/Tail/Bulk~~ | Audit 22.10. | **done** (32+128, Prefetch-Struktur, Elevator STRONG; A8 formal offen) |
| ~~Trip-Replay 0.3.17~~ | PhaseGate | **done** Feld Upload PASS (`#17`/`#18`) |
| P0 audible-Marker / GATE-01 | Media-Leiter | Lead mit `audible_change`-Anker |
| P0 Analyzer B47 | Prefetch-Stats | Scan-Fenster aus Compare ausschließen |
| P1 Profil-Nachzug Leiter | `bmw_nbt_evo.json` | Head 160, Tail-Prefetch, Bulk 240, Reject nur-Struktur |
| P1 Identity / Cache-Key | `ident_b` | Serial/Label/Volume; Head-vs-Rest A→B→A |
| P1 Lab-Replay B50 | `.88` vs `.89` | `replay_records=0` trotz Offline-Records |
| P2 formal Größenleiter A8 | Feldplan 21.10. | `seq_size` / H-A/B/C — Leiter ersetzt Formal nicht |
| P2 Elevator-Drittstichprobe | zwei ungelesene Spans | Rückwärtssprung ohne Cache |
| P1 HARDWARE.md §2.3 | Doc-Drift | PSRAM-aktiviert + eFuse `hw.module` |
| Lab Power/Starve/RF | Method `usb-wifi-coex-discrimination` | vor weiteren Hub-only Mitigations |
| Runtime-Prio-Verify | `usbd`=24 / WiFi=23 | `uxTaskPriorityGet` im Image |
| esp-usb Task-API Migration | Kontrast Arduino-HAL | nur wenn Port geplant |
