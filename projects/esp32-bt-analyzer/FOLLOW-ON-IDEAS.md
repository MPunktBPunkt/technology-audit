# Follow-on ideas (aus esp32.bt-analyzer)

```yaml
reuse_outcomes:
  reused: [esp-hub-telemetry, esp32-s3-silicon, esp32-s3-usb-wifi-coex, bt-passive-host-sniff, bluetooth-ftms, bluetooth-hid, bt-dual-mode-coex, esp-wifi-bt-coex]
  new: [bt-analyzer-flavor-bus, ble-gatt-client-fsm, hogp-host-client]
  not_helped: [esp-usb-host as primary — superseded by F_ONCHIP, BTstack as vendored commercial host, FTMS.NET code (GPL-3)]
```

Desk Host-Profiles: [`esp32-bt-analyzer-host-profiles-2026-desk`](../../audits/esp32-bt-analyzer-host-profiles-2026-desk/).

Knowledge-gap foreign desk 2026-11-12 (HCI / Coex / Car-Net / BCL-RFCOMM / BlueZ-GATT / BDADDR):
[`esp32-hci-controller-2026-foreign`](../../audits/esp32-hci-controller-2026-foreign/) ·
[`esp32-wifi-bt-coex-2026-foreign`](../../audits/esp32-wifi-bt-coex-2026-foreign/) ·
[`esp32-car-network-2026-foreign`](../../audits/esp32-car-network-2026-foreign/) ·
[`bmw-bcl-rfcomm-role-2026-desk`](../../audits/bmw-bcl-rfcomm-role-2026-desk/) ·
[`ble-gatt-bluez-relay-2026-foreign`](../../audits/ble-gatt-bluez-relay-2026-foreign/) ·
[`bt-bdaddr-2026-foreign`](../../audits/bt-bdaddr-2026-foreign/).

| Idee | Baut auf | Kurz |
|------|----------|------|
| UART HCI offload vs WiFi HCI_TCP | `esp-hci-uart-controller`, `esp-wifi-bt-coex` | Lab: same ACL load over UART vs SoftAP/STA |
| Car reachability A6/B1 | `esp-tailscale-client` / `esp-wireguard` | Outbound rendezvous hinter Handy-Hotspot |
| HU RFCOMM channel X | `bmw-bcl` RFCOMM desk | A6 link → B1 SDP (nicht Lab-Kanal 5) |
| BlueZ two-adapter HR/FTMS relay | BluetoothInterceptor pattern | Bonding/CCCD Lab gegen H9 |
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
