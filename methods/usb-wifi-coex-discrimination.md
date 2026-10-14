# Method: USB ↔ WiFi Coexistence Discrimination

```yaml
slug: usb-wifi-coex-discrimination
title: USB ↔ WiFi Coexistence Discrimination (Power / Starve / RF)
status: active
tags: [lab, wifi, usb-device, esp32s3]
```

## Zweck

Lab-Messplan, um bei ESP32-S3 (OTG Device + WiFi STA) **Power**, **CPU/Task-Starve**
und **RF/Desense** zu trennen — ohne Desk-Root-Cause. Einsetzen nach Desk-Karte
[`esp32-s3-usb-wifi-coex`](../technologies/esp32-s3-usb-wifi-coex/SHEET.md).

## Voraussetzungen

- ESP32-S3 Dual-USB oder bekanntes OTG-Pinout; WiFi-Assoc-Indikator (HTTP/ping/LED)
- Host, der kontrolliert **keine** Reads vs. sustained Bulk (`dd`/MSC Read) erzeugen kann
- Option: externe stabile 5 V (nicht nur VBUS vom Host)
- Optional: Task-Runtime (`uxTaskGetSystemState` / Run-Time Stats) für `usbd` vs. WiFi
- Verwandt: [`plug-power-reset-isolation`](plug-power-reset-isolation.md)

## Ablauf

1. **Baseline A — OTG ab:** WiFi Assoc + TCP/HTTP ≥ N Minuten stabil.
2. **Baseline B — OTG an, Host idle** (enum/mount, minimale Reads): Assoc halten?
3. **Last C — sustained Host-Reads** (`dd` o. ä.): Zeit bis Assoc-Verlust notieren.
4. **Power-Zweig:** C wiederholen mit **externer 5 V**; Reset-Reason/Brownout loggen.
5. **Starve-Zweig:** unter C Task-Runtime `usbd` / WiFi / `tcpip` / `loop` samplen;
   optional WiFi-Task kurz prio-anheben *nur als Experiment* (Ergebnis = Lab-Evidence,
   kein Desk-FACT).
6. **RF-Zweig:** Antenne/Abstand/Kabelvariante bei gleicher Software; TX-Power fest.
7. **App-Last-Kontrolle:** WIFI_OFF während Drain / Drain-Cap — trennt Emit von USB-Last.
8. Jeden Lauf mit FW-Version, Versorgung, Host-Lastprofil, Zeit-bis-Kill dokumentieren.

## Artefakte

| Artefakt | Inhalt |
|----------|--------|
| Lauf-Tabelle | A/B/C × Power/RF-Variante → t_kill, Reset-Reason |
| Task-Sample | %CPU / Runtime Counters pro Task unter C |
| Decision Trace | welche Hypothese (H1–H5) gestützt/geschwächt |

## Pass / Fail (für die *Methode*, nicht für „WiFi geheilt“)

| Kriterium | Pass | Fail |
|-----------|------|------|
| A vs C unterscheidbar | C killt, A nicht (oder klar andere t_kill) | kein reproduzierbarer Unterschied |
| Power isolierbar | externe 5 V ändert t_kill klar | Versorgung unverändert + Brownout=0 → H3 schwach |
| Starve sichtbar | `usbd` Runtime ≫ WiFi vor Kill | WiFi Runtime hoch bis Kill → H1 schwach |
| Kein Desk-Übertrag | Claims als Lab-Evidence-IDs | „Issue X beweist Ursache“ |

## Fallstricke

- IDF USB-Start-Issues (#7957/#8241) mit Dauerlast-Assoc-Tod vermischen.
- esp-faq BT-Coex-Schalter als USB-Fix interpretieren.
- Arduino-`usbd`-Prio mit esp-usb-Kconfig-Defaults gleichsetzen.
- Ein erfolgreicher Soft-Reconnect als „kein Problem“ werten.

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| hu-probe / Coex-Desk | [`esp32-s3-usb-wifi-coexistence-2026`](../audits/esp32-s3-usb-wifi-coexistence-2026/) — Method präregistriert, Lab offen |
