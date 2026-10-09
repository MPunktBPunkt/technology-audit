# Technology Sheet: Web-Radio Browser Host (ESP)

```yaml
slug: webradio-browser-host
title: Web-Radio Browser Host (ESP)
primary: G
tags: [streaming]
type: pattern
status: active
seen_in: [esp32-webradio]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
```

## Kurzfassung

ESP hostet Web-UI und Metadaten (Sender, Favoriten, Now-Playing); **Audio spielt der Browser** (HTML5 Audio / Media Session). Entdecken oft über externe Radio-APIs; ESP kann RSS/HTTP-Proxy. Kein On-Device-Decoder, kein A2DP-Sender.

## Abgrenzung

- **Ist:** Browser-Media-Host + Station-Store + optional Hub-Now-Playing.
- **Ist nicht:** A2DP-Sink/Source; PipeWire-/Pi-Webradio; DAB+; ESP-I2S-Audio-Shield-Player.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| ESP streamt Audio per Classic-BT | `REJECTED` | S3 ohne Classic-BT; WiFi+BT parallel oft ungeeignet |
| radio-browser.info = Pflichtteil | `HYPOTHESIS` | Discovery-Quelle austauschbar |
| Proxy-URL ohne Allowlist ist harmlos | `REJECTED` | offener Proxy-Risiko im LAN |

### Projektstart-Checkliste

- [ ] Audio-Pfad: Browser vs. ESP-Hardware klären
- [ ] Nicht mit A2DP/DAB/PipeWire-Sheets vermischen
- [ ] Hub-IO Now-Playing Keys
- [ ] Application + `seen_in`

## Referenzen

- HTML5 Audio / Media Session
- Beispiel: esp32.webradio

## Offene Fragen

- Einheitliches Now-Playing-Schema über Nodes?
