# Technology Sheet: ESP-Hub Base Firmware Template

```yaml
slug: esp-hub-base-template
title: ESP-Hub Base Firmware Template
primary: J
tags: [arduino, esp-idf]
type: pattern
status: active
seen_in: [esp32-esp-hub]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W3
```

## Kurzfassung

Ableitungsmuster für neue Hub-Nodes: gemeinsame Basis (WiFiManager, Heartbeat, OTA, Status-Web/SSE) **unverändert lassen**; nur markierte Abschnitte (Device-Name, ios, Sensorik, UI-Erweiterung) anfassen. Ergebnis: konsistente Familie + schneller Start.

## Abgrenzung

- **Ist:** Template-/Fork-Disziplin für Hub-Nodes.
- **Ist nicht:** Modular-Host (`esp-module-host`); der HTTP-Contract (`esp-hub-telemetry`); der Adapter.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Heartbeat-Kern für Features umbauen | `REJECTED` | Kern belassen; ios erweitern |
| WLAN-Secrets im Repo | `REJECTED` | nur WiFiManager/NVS |
| Beliebige Bin-Namen | `REJECTED` | `{projekt}.{version}.esp32[.s3].bin` |
| Jede Ableitung braucht neues Hub-Sheet | `REJECTED` | Contract-Sheet wächst; Application neu |

### Projektstart-Checkliste

- [ ] Von `esp-hub-base` kopieren/forken
- [ ] DEVICE_NAME, FW_VERSION, Portal-SSID
- [ ] ios + updateIoValues
- [ ] Contract-Checkliste `esp-hub-telemetry`
- [ ] Application + `seen_in`

## Referenzen

- [ESP32.esp-hub](https://github.com/MPunktBPunkt/ESP32.esp-hub) „Neue Firmware ableiten“

## Offene Fragen

- Wann Template vs. `esp-module-host` (toolnode)?
