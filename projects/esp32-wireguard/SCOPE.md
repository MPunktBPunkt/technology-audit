# Project Scope: esp32-wireguard

```yaml
project_id: esp32-wireguard
updated: 2026-11-27
source_repo: https://github.com/MPunktBPunkt/esp32.wireguard
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | Referenz-WG-Client auf `esp-hub-base` 1.12+; UiTab/Modul; Storage/NVS; trombik/esp_wireguard; SNTP; Fritz!Box/Hotspot Lab |
| **Nicht in scope** | Integration in hu-probe / bt-hci-agent / pidrive / bt-gateway (erst nach Tunnel-DoD) |
| **Hardware** | Lab ESP32 `.87`/`.131`, ESP32-S3 `.88` |
| **Version** | `wireguard` **0.2.0** (Fassade); Stack-Link folgt |

## Systeme

```text
esp-hub-base 1.12
  └── WireGuardModule (optional)
        ├── UiTab /api/ui/tabs
        ├── WireGuardStorage → NVS
        └── esp_wireguard (trombik) → Fritz!Box endpoint
```
