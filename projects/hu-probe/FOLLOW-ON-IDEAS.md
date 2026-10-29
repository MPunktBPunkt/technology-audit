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
| ~~C1b AOA Rohr (P0)~~ | Feld 29.10. | **done partial:** P0-0/A/C/D PASS; P0-E absent; 51–53 bei 2D00 erwartbar absent (Already-Accessory) |
| ~~C1b B1 phone_like~~ | `04E8:6860` | **done NEGATIVE** — HU „USB nicht unterstützt“ (Fingerprint, kein AOA-Kill) |
| ~~C1b B2b Knock hex4~~ | 0.3.32 | **done NEGATIVE** — TX ok, rx=0; Blind-Knock **STOP** |
| **C1b Referenz Phone+Connected (#9)** | Capture | **PRIORITÄT** — Checkliste `hu-probe/docs/feld/2026-10-29-c1b-massnahmen-nach-b1-b2b.md` |
| C1b BCL-on-USB Retry | nach #9 | nur mit echter Init-Sequenz aus Capture |
| C1c BT-SPP (#11) | nach #9 | nur wenn Capture USB-BCL absent; BclCarLink RFCOMM |
| ~~C1b Control-Callback-Sicht (P0.5-A)~~ | Instrumentierung | **done** hu-probe 0.3.24 |

**Nicht tun:** Blind VID/Knock/Timing; 51–53 bei 2D00 als AOA-FAIL; Soft-Composite MSC+AOA; Etch/SAS vor BCL-RX; BT-SPP vor Capture-Entscheidung.
