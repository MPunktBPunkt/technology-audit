# Project Scope: esp32.bt-analyzer

```yaml
project_id: esp32-bt-analyzer
title: ESP32 On-Chip Bluetooth HCI Analyzer (VHCI)
updated: 2026-11-04
source_repo: https://github.com/MPunktBPunkt/esp32.bt-analyzer
reviewed_commit: 542eed6
profile_hint: lab-tool
status: active
fw_pin: "0.2.9"
repos:
  - https://github.com/MPunktBPunkt/esp32.bt-analyzer
```

## Zweck

Lab-Instrument: **On-Chip Bluetooth Controller** der ESP-Boards über **VHCI** (thin HCI host) capturen — Timestamp, Richtung, Typ, Payload — Export nach Debian (BTAC / JSONL / PCAPNG).

Primärtopologie: **F_ONCHIP**. USB-Dongle Observe (A_OBSERVE) ist legacy/optional.

**Nicht** RF-/Air-Sniffer, **nicht** Universal-MITM, **nicht** Classic-on-S3.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP32-S3 N8R2 on-chip BLE VHCI | Capture + thin host (scan/adv/connect) | **ja (primary)** |
| ESP32 D1 (`.87`) Classic+BLE VHCI | Classic discoverable/inquiry + BLE | **ja** |
| Debian Collector `:8081` / BTAC `:9753` | Decode / PCAPNG / Lab UI | ja |
| esp-hub OTA / Heartbeat | FW-Verteilung | ja |
| Peer ESP advertise/connect (BT11/BT9) | L1 stimulus | ja |
| Thin ATT/GATT over HCI ACL | **L2** lab probe (not SoT for air) | ja (bounded) |
| USB BT-Dongle + USB Host | legacy A_OBSERVE | optional |
| nRF / RF Air sniffer | L0 | **nein** — BT15 deferred |
| S3 on-chip Classic BR/EDR | — | **REJECTED** |

## Nicht-Ziele

- Bluetooth RF / channel-hopping sniffer (→ BT15)
- Universal Phone↔Device MITM
- Fremde Bond-Decryption
- Full profile stacks (A2DP/HFP) on the analyzer node
- HCI MEASURED als Air FACT verkaufen

## Epistemik

`FACT` · `MEASURED` · `INFERENCE` · `HYPOTHESIS` · `UNKNOWN` · `REJECTED`  
**HCI ≠ RF/Air.** Layer L0/L1/L2 nie in einem MEASURED-Block vermischen.

## Quellen

| Quelle | Pfad |
|--------|------|
| Upstream | `firmware/`, `controller/`, `tools/`, `docs/` |
| Gates | [`docs/GATES.md`](https://github.com/MPunktBPunkt/esp32.bt-analyzer/blob/main/docs/GATES.md) |
| Evidence | `docs/evidence/LAB_GATES_BT5_13_*`, `LAB_F_ONCHIP_PEER_*` |
| Method | [`bt-passive-host-sniff`](../../methods/bt-passive-host-sniff.md) |
| Capture family | [`bt-sniffing-capture-refs`](../bt-sniffing-capture-refs/) |

## Offene Fragen (bewusst klein)

- BT14 external reviewer sign-off in technology-audit CI
- BT15 eigenes Repo/Scope wenn Air gebraucht wird
