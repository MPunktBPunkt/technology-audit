# Follow-on ideas (aus esp32.bt-analyzer)

```yaml
reuse_outcomes:
  reused: [esp-hub-telemetry, esp32-s3-silicon, esp32-s3-usb-wifi-coex, bt-passive-host-sniff, bluetooth-ftms, bluetooth-hid, bt-dual-mode-coex]
  new: [bt-analyzer-flavor-bus, ble-gatt-client-fsm, hogp-host-client]
  not_helped: [esp-usb-host as primary — superseded by F_ONCHIP, BTstack as vendored commercial host, FTMS.NET code (GPL-3)]
```

Desk Host-Profiles: [`esp32-bt-analyzer-host-profiles-2026-desk`](../../audits/esp32-bt-analyzer-host-profiles-2026-desk/).

| Idee | Baut auf | Kurz |
|------|----------|------|
| External BT14 sign-off | STATUS.md | Reviewer stamp in audit CI |
| Second Classic ESP peer | BT10 | Dual Classic inquiry symmetry |
| **Profile Flavor Bus** | Host-Profiles desk | Core stays capture; Flavors = tagged stimulus clients |
| **GATT Client Flavor (MVP)** | NimBLE blecent + BTstack service-client FSM | Discovery/MTU/CCCD; `STIMULUS` timeline |
| **HOGP Host Flavor** | GATT Client + BTstack `hids_host` pattern | Report Map buffer + Input notify |
| **FTMS Flavor** | pyftms parsers + `ftms-capability-probe` | CP Indicate quirks; Success ≠ Wirkung |
| Classic SDP/RFCOMM Flavor | `.87` + Classic-gaps | Low-bandwidth Classic stimulus first |
| A2DP/HFP heavy Flavors | IDF classic_bt | Opt-in only; capture-budget gate |
| Richer ATT/GATT lab (bounded L2) | thin ATT | Prefer Flavor path over growing Core |
| Live BTAC session UI | Collector :8081 | **done in 0.2.7** · polish download UX |
| RF/Air Capability | nRF / externe Sniffer | **BT15 — eigenes Scope/Repo** |
| Legacy USB-dongle A_OBSERVE | `esp-usb-host` | optional only |
