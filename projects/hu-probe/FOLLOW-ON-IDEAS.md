# Follow-on Ideas: hu-probe

| Idee | Bezug | Hinweis |
|------|-------|---------|
| ~~P1c Profil Upstream~~ | `bmw_nbt_evo.json` schema 3 | **done 2026-10-17**; free-FACTS 2026-10-20 im Quellrepo |
| ~~CBW-Atom 240+69~~ | Abend 18.10. | **done** |
| ~~PSRAM / Board N8R2~~ | Audit 21.10. | **done** (Doc §2.3 Upstream nachziehen) |
| ~~free Offline Grammar demo_v1~~ | 0.2.40 | **done** (Prefetch-15s REJECTED) |
| P0 Größenleiter H-A/B/C | Feldplan 21.10. | `seq_size` / `size_1_4_8` auswerten |
| P0 Elevator-Test | `tail_then_head` | Rückwärtssprung D180→D026 ungelesen |
| P1 Replug Cache-Key | `ident_b` | Serial/Label/Volume |
| P1 audible-Marker | GATE-01 Rest | `next_track_read` → hörbar |
| P1 HARDWARE.md §2.3 | Doc-Drift | PSRAM-aktiviert + eFuse `hw.module` |
| P2 Drive-Home 0.3.x | TripStore | Footer/integrity Census |
| Lab Power/Starve/RF | Method `usb-wifi-coex-discrimination` | vor weiteren Hub-only Mitigations |
| Runtime-Prio-Verify | `usbd`=24 / WiFi=23 | `uxTaskPriorityGet` im Image |
| esp-usb Task-API Migration | Kontrast Arduino-HAL | nur wenn Port geplant |
