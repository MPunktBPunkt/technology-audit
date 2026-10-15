# Follow-on Ideas: hu-probe

| Idee | Bezug | Hinweis |
|------|-------|---------|
| **P1c Profil Upstream** | `bmw_nbt_evo.json` | nur `origin: hu_probe_field`; Gap/4096 als Messgröße; Semantik nicht hochstufen — Skizze in [`evidence`](../../audits/hu-probe-bmw-s0s2-field-2026/evidence.md) |
| P0a Offline blocks/gap/LBA | S2 Rohdaten | READ10-`blocks`, Bytes/s, LBA-Folgen |
| P0b S2 Formalauswertung | Method `msc-host-read-semantics` | Prefetch/Cache weiter INFERENCE bis dann |
| P0c Auto Offline | `ram_offline` | Lab PASS ≠ BMW; reproduzieren |
| S3 → S1 ≥4 MiB | Method | nach Transport-Stabilität |
| Profil-Epistemik | PiDrive-`FACT`-Labels | parallel P1c |
| Lab Power/Starve/RF | Method `usb-wifi-coex-discrimination` | vor weiteren Hub-only Mitigations |
| t_us-Regression P1a | Sessions 2176/2199/2280 | Pace weiter `gap_us` |
| Marker ohne WiFi | Queue/BOOT | S2-Handicap |
| Runtime-Prio-Verify | `usbd`=24 / WiFi=23 | `uxTaskPriorityGet` im Image |
| GATE-01 / Burst-Epistemik | GATES.md | formal dokumentieren; Gate OPEN |
| esp-usb Task-API Migration | Kontrast Arduino-HAL | nur wenn Port geplant |
