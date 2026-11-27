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
| **In scope** | Referenz-WG-Client auf `esp-hub-base`; UiTab/Modul; Storage/NVS; trombik/esp_wireguard v0.9.0; SNTP; selektives Routing; Lab Fritz/Gast/Hotspot; DoD-Evidence |
| **Nicht in scope** | Prophylaktische Integration aller ESP-Projekte; Feld-Langzeit; natürlicher WiFi-Failover (noch UNKNOWN); PiDrive-Implementierung (→ eigener Readiness-Audit) |
| **Hardware** | Lab ESP32 `.87`/`.131`, ESP32-S3 `.88` |
| **Version** | **v0.4.9** — Transport-DoD **geschlossen** (Lab) |

## Systeme

```text
esp-hub-base
  └── optional WireGuard (esp32.wireguard 0.4.9)
        ├── WireGuardModule / Storage / SNTP
        └── esp_wireguard (trombik) → Fritz endpoint
              │
              ├── consumer: hu-probe 0.3.42-wg (Lab E2E)
              └── consumer: bt-analyzer 0.3.21-wg (Lab E2E)
```

## Abschluss

Audit: [`../../audits/esp32-wireguard-2026-11-dod-close/`](../../audits/esp32-wireguard-2026-11-dod-close/).  
Nächster sinnvoller Schritt (separat): **esp32.pidrive WireGuard Integration Readiness** — kein Copy-Paste der Consumer-Integration ohne Verkehrsanalyse.
