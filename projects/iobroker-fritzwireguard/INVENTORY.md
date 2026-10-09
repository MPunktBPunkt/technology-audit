# Project Inventory: iobroker.fritzwireguard

```yaml
project_id: iobroker-fritzwireguard
updated: 2026-10-09
reviewed_commit: 829b455
profile: adapter
pilot_order: [iobroker-fritzwireguard-adapter, fritzbox-tr064]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| wg-quick + Config-Sanitizer + TCP-Tunnel + WebUI :8094 | `iobroker-fritzwireguard-adapter` | **neu** |
| TR-064 Hosts/WAN/DeviceInfo über VPN | `fritzbox-tr064` | **wachsen** (Remote/VPN; Default :49000) |
| LAN-Hostlist lokal HTTPS :49443 | `fritzbox-tr064` | schon bei `esp32-network` — kontrastieren, nicht forken |
| Kostalpiko `networkMode=fritzwireguard` | — | Konsument → [`iobroker-kostalpiko`](../iobroker-kostalpiko/) |

Ursprung: [ioBroker.fritzwireguard](https://github.com/MPunktBPunkt/ioBroker.fritzwireguard).  
Kampagne: [iobroker-fritzwireguard-2026-pilot](../../audits/iobroker-fritzwireguard-2026-pilot/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `iobroker-fritzwireguard-adapter` | FritzWireguard Adapter | F | `iobroker`,`nodejs`,`vpn` | applied | partial | [SHEET](../../technologies/iobroker-fritzwireguard-adapter/SHEET.md) | [app](applications/iobroker-fritzwireguard-adapter.md) |
| `fritzbox-tr064` | FritzBox TR-064 | F | — | applied | partial | [SHEET](../../technologies/fritzbox-tr064/SHEET.md) | [app](applications/fritzbox-tr064.md) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Catalog listing | Fork-Scan absent | [`iobroker-repositories`](../iobroker-repositories/) |
| HTTPS :49443 über VPN | Spec/Default noch :49000 | Readme/Changelog nachziehen |

## Signale ohne Eintrag

- `cap_net_admin` / sudo-rs Host-Quirks
- Same-subnet AllowedIPs=/32 Heuristik (UI 0.2.35)
