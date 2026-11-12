# Project Scope: bt-bdaddr-refs (Fremd)

```yaml
project_id: bt-bdaddr-refs
title: BT BD_ADDR Rewrite References (Fremd)
updated: 2026-11-12
profile_hint: lab-tool
reviewed_commit: "bdaddr@53dae3f"
repos:
  - https://github.com/thxomas/bdaddr
status: active
```

## Zweck

Desk: Vendor-spezifische HCI Write-BD_ADDR Mechanismen und **Nicht-Unterstützung von Espressif** in Host-Tool `bdaddr`. Kontrast zu ESP IDF MAC-APIs. Keine Spoofing-Anleitung.

## Systeme und Grenzen

| Repo / API | Rolle | Im Scope? |
|------------|-------|-----------|
| thxomas/bdaddr @ `53dae3f` | Vendor-Tabelle + HCI writes | ja — Architektur/Capability |
| ESP-IDF `esp_base_mac_addr_set` / Controller APIs | Kontrast (kein Deep-Pin) | ja — Abgrenzung FACT |
| BluetoothInterceptor MAC clone | DESIGN open Q | CROSSREF Pack A |

## Nicht-Ziele

- Attack-/Impersonation-How-tos
- Vollständiges ESP MAC-Sheet
- Lab MEASURED HU-Reaktion
