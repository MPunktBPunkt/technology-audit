# Follow-on ideas (aus esp32-usb-analyzer)

Ideen aus dem Lab — noch keine neuen Repos.

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [usb-msc, esp-usb-host, usb-aoa, bmw-bcl, esp32-s3-usb-wifi-coex, esp32-s3-silicon, esp-hub-telemetry]
  new: [usb-dual-esp-observe-proxy, usb-otg-loop-baseline]
  not_helped: []
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | MSC/Host/AOA/BCL/Coex/Silicon/Hub Sheets + BOT-Observation Methods |
| Neu | Dual-ESP Observe/Proxy Pattern + OTG-Loop Baseline Method |
| Nicht geholfen | — |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Observer-effect Baseline Method | `usb-dual-esp-observe-proxy` | Gate-4 Transparenz erst nach Kontroll-Host Diff |
| Mode-A window vs Store-and-Forward | `esp32-s3-usb-wifi-coex` | TCP ≪ USB MSC — SF-* Gates wenn Proxy Last braucht |
| HU AOA B1/B2 am Analyzer | `usb-aoa`, hu-probe C1b | Analyzer als Host-Accessory gegen Phone/HU — getrennt claimen |
| Class-hook vs App-decode Diff-Tool | `usb-bot-command-observation` | Automatischer Source-Tag Check in Captures |
| Sync residual under load | Gate 8 | Offset-Estimate Stress; hard-lock bleibt REJECTED bis belegt |
