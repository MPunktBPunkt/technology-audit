# Follow-on ideas (aus esp32-usb-analyzer)

Ideen aus Lab + Feld — noch keine neuen Repos.

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [usb-msc, usb-aoa, bmw-nbt-evo, esp-usb-host, bmw-bcl, esp32-s3-usb-wifi-coex, esp32-s3-silicon, esp-hub-telemetry, usb-dual-esp-observe-proxy, usb-otg-loop-baseline]
  new: [usb-msc-host-behaviour, usb-msc-host-fingerprint]
  not_helped:
    - "Path-A GPIO sniffer — falsifiziert, kein Transfer"
    - "TV/Soundbar/FRITZ n=1 — noch keine GENERAL Host-Klassen"
    - "Windows write-cache eviction — Test Gap, kein Tech-FACT"
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | MSC/AOA/NBT/Host/BCL/Coex/Silicon/Hub + Dual-ESP + OTG Baseline |
| Neu (Feld 2026-11-06) | `usb-msc-host-behaviour` + Method Fingerprint |
| Nicht geholfen | Path-A Sniffer; voreilige Host-Klassen; Write-Loch-Claim |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| **BMW C0** FAT/Media unter `303a:1001` | `usb-msc`, `bmw-nbt-evo` | Identity vs Content; UI-Stille erklären |
| **BMW C1** AOA phone-like / `aoa_observe` | `usb-aoa` | Connected-Apps-Gate; danach Full Audit |
| Self-powered Hub Phone→`.88` | VBUS gap `011` | Enum vor MITM |
| SCSI Aggregate Counters + Histograms | `usb-msc-host-behaviour` | Overflow-fest Fingerprint |
| Write-LBA-Audit (evict counter) | `usb-msc` | 64 vs 106 Sektoren entscheiden |
| Full Audit nach C1→BCL→Etch | `usb-aoa`, `bmw-bcl` | echter Knowledge-Sprung |
| Kontroll-Host Observer Method | `usb-dual-esp-observe-proxy` | Transparenz erst nach PC↔Stick Diff |
| Mode-A pipeline vs Store-and-Forward | `esp32-s3-usb-wifi-coex` | 332–436≪917 kB/s |
| Path-B Hi-Z Tap Bring-up | Gate 10 / Silicon | `.l0samp` + L0/L1 n≥100 |
| Capability Harness in CI/Release | `usb-otg-loop-baseline` | vor jedem FW-Tag |
| Host-Klassen (minimal/scanner/FS/OS) | Fingerprint Matrix | erst nach n≥3 Wiederholung |
