# Follow-on Ideas: hu-probe

| Idee | Bezug | Hinweis |
|------|-------|---------|
| ~~P1c Profil Upstream~~ | `bmw_nbt_evo.json` schema 3 | **done 2026-10-17**; free-FACTS 2026-10-20 im Quellrepo |
| ~~CBW-Atom 240+69~~ | Abend 18.10. | **done** |
| ~~PSRAM / Board N8R2~~ | Audit 21.10. | **done** (Doc §2.3 Upstream nachziehen) |
| ~~free Offline Grammar demo_v1~~ | 0.2.40 | **done** (Prefetch-15s REJECTED) |
| ~~Media-Leiter Head/Tail/Bulk~~ | Audit 22.10. | **done** (32+128, Prefetch-Struktur, Elevator lokal STRONG; A8 formal offen) |
| ~~Heimfahrt Remount/Scheduler~~ | Audit 22.10. Abend | **done** (Remount≠Cold Start; LBA-Interleave; Lead kontextabhängig; Eager≠Play) |
| ~~Trip-Replay 0.3.17~~ | PhaseGate + Heimfahrt `#22`–`#24` | **done** Feld Upload PASS |
| P0 audible-Marker / GATE-01 | Heimfahrt / Leiter | Read ↔ hörbarer Track mit Zeitmarker |
| P0 Play-Intent-Unterscheidung | Heimfahrt C0x Eager | großer/Nachbar-Read ≠ Decode/Play |
| P1 395xxx Remount-Semantik | `#22` 2. Mount | was die Positions-LBAs bedeuten |
| P1 Cache-Key / Identity | `seq_ident` / `ident_b` | Serial/Label/Volume; Head-vs-Rest A→B→A |
| P1 Profil-Nachzug Leiter+Heimfahrt | `bmw_nbt_evo.json` | Head 160, Reject Lead=8 s / global Elevator / Remount=Cold |
| P1 Lab-Replay B50 | `.88` vs `.89` | `replay_records=0` trotz Offline-Records |
| P2 formal Größenleiter A8 | Feldplan 21.10. | `seq_size` / H-A/B/C — Leiter/Heimfahrt ersetzen Formal nicht |
| P2 Elevator-Drittstichprobe | zwei ungelesene Spans | lokal; global SUPERSEDED |
| P1 HARDWARE.md §2.3 | Doc-Drift | PSRAM-aktiviert + eFuse `hw.module` |
| Lab Power/Starve/RF | Method `usb-wifi-coex-discrimination` | vor weiteren Hub-only Mitigations |
| Runtime-Prio-Verify | `usbd`=24 / WiFi=23 | `uxTaskPriorityGet` im Image |
| esp-usb Task-API Migration | Kontrast Arduino-HAL | nur wenn Port geplant |
| C1b-0 AOA Reachability (B1) | Desk [`usb-aoa`](../../technologies/usb-aoa/SHEET.md) | NBT Evo: Switch/`0x18D1`? Kein AOA-FW vor Messplan |
| C1b BCL-on-USB (B2) | nach B1 | Bulk-Capture vs BT Framing; `ITransport` agnostisch |

**Nicht tun:** weitere Media-Ladder-Varianten nur um Prefetch-Zahlen zu sammeln; AOA/SAS/Etch in hu-probe ohne C1b.
