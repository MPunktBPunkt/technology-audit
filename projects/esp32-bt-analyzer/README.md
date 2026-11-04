# Project: esp32.bt-analyzer

ESP **on-chip Bluetooth HCI analyzer** (VHCI) — Capture L1 Controller↔Host, Debian BTAC/JSONL/PCAPNG, bounded L2 ATT probe.  
**Nicht** RF-Sniffer, **nicht** MITM, **nicht** Classic-on-S3.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen (F_ONCHIP primary) |
| [INVENTORY.md](INVENTORY.md) | Technologie-Inventar + Match |
| [STATUS.md](STATUS.md) | Gate exits / MEASURED pins |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | Folgeideen inkl. BT15 |
| [applications/](applications/) | Project Applications |
| Method | [`bt-passive-host-sniff`](../../methods/bt-passive-host-sniff.md) |

Upstream: [MPunktBPunkt/esp32.bt-analyzer](https://github.com/MPunktBPunkt/esp32.bt-analyzer) **FW 0.3.0** (see SCOPE `fw_pin`).

Evidence contract: CAPABILITY ≠ BENCHMARK; App/Capture/BTAC/File loss layers separate. technology-audit stays claim/scope; implementation stays in upstream.

**Reuse:** esp-hub-telemetry, S3 silicon/coex sheets.  
**Contrast:** Endpoint / nRF Air / Classic-on-S3 **REJECTED**. BT14 = ready for external review; BT15 RF deferred.

**Profile Flavors (desk):** [`esp32-bt-analyzer-host-profiles-2026-desk`](../../audits/esp32-bt-analyzer-host-profiles-2026-desk/) — GATT Client → HOGP → FTMS → Classic; Core stays measurement-only.
