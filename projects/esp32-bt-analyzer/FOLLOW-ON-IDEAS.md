# Follow-on ideas (aus esp32.bt-analyzer)

```yaml
reuse_outcomes:
  reused: [esp-hub-telemetry, esp32-s3-silicon, esp32-s3-usb-wifi-coex, bt-passive-host-sniff]
  new: []
  not_helped: [esp-usb-host as primary — superseded by F_ONCHIP]
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| External BT14 sign-off | STATUS.md | Reviewer stamp in audit CI |
| Second Classic ESP peer | BT10 | Dual Classic inquiry symmetry |
| Richer ATT/GATT lab (bounded L2) | thin ATT | Still ≠ Air FACT |
| Live BTAC session UI | Collector :8081 | **done in 0.2.7** · polish download UX |
| RF/Air Capability | nRF / externe Sniffer | **BT15 — eigenes Scope/Repo** |
| Legacy USB-dongle A_OBSERVE | `esp-usb-host` | optional only |
