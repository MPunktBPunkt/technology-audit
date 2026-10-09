# Project: iobroker.fritzwireguard

ioBroker-Adapter: **WireGuard-VPN** zur entfernten FritzBox (`wg-quick`), optional **TR-064** (Geräte/WAN), **TCP-Tunnel** `127.0.0.1:<port>` → Remote-Host, WebUI :8094.

| Dokument | Inhalt |
|----------|--------|
| [SCOPE.md](SCOPE.md) | Grenzen |
| [INVENTORY.md](INVENTORY.md) | Inventar + Reuse |
| [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) | Folge |
| [applications/](applications/) | Applications |
| Audit | [`iobroker-fritzwireguard-2026-pilot`](../../audits/iobroker-fritzwireguard-2026-pilot/) (`standard_version` 0.6.3) |

Ursprung: [MPunktBPunkt/ioBroker.fritzwireguard](https://github.com/MPunktBPunkt/ioBroker.fritzwireguard) @ `829b455`.  
Konsument-Beispiel: [`iobroker-kostalpiko`](../iobroker-kostalpiko/) (`networkMode=fritzwireguard`).  
TR-064 Geschwister: [`esp32-network`](../esp32-network/) (lokal HTTPS :49443).
