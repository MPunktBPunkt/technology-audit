# Audit Campaign: esp32-wifi-bt-coex-2026-foreign

```yaml
id: esp32-wifi-bt-coex-2026-foreign
project_id: esp32-wifi-bt-coex-refs
started: 2026-11-12
ended: 2026-11-12
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "desk-docs-2026-11-12"
upstream_pins:
  esp-idf-rf-coex-guide: "ESP32 RF Coexistence (docs desk)"
  esp_coexist.h: "IDF header symbols (A2DP bits / EXTERNAL / prefer deprecated)"
  esp-idf-issue-12434: "#12434"
  esp-idf-issue-1291: "#1291"
  esp-faq-coexistence: "FAQ coexistence page"
reuse_outcomes:
  reused:
    - bt-dual-mode-coex
    - esp32-s3-usb-wifi-coex
  new:
    - esp-wifi-bt-coex
  not_helped:
    - "esp32-s3-usb-wifi-coex — USB-PHY/BBPLL, nicht RF WiFi↔BT"
    - "bt-dual-mode-coex — Classic+BLE Budgets, nicht WiFi-TDM (WiFi ≠ BTDM)"
    - "öffentliche Messprojekte esp_coex_* + Classic A2DP + WiFi-Throughput — nicht gefunden"
  process: "Enges Fremd-Desk: TDM/Status-Bits/SoftAP-C1-Karte + Gap für HCI_TCP; keine Lab-Remessung."
  decisions_touched:
    - new-slug-esp-wifi-bt-coex-primary-d
    - reject-usb-coex-as-rf-soT
    - reject-btdm-as-wifi-tdm
    - fact-softap-c1-vs-sta-y
    - uart-hci-offload-vs-same-chip-esp-coex
```

## Ziel

Navigationskarte **ESP32 WiFi ↔ Classic Bluetooth RF-Coexistence** (`esp_coex_*`):
TDM, SoftAP/STA×BT-Stabilität, Status-Bits vs. deprecated Prefer, Bluedroid Vendor HCI,
FAQ-Truncation — und explizite **Wissenslücke** für `esp32-bt-analyzer` HCI_TCP über WiFi
bei laufendem Classic-BT. **Kein** Lab-Remeasure in dieser Kampagne.

## Scope

[SCOPE](../../projects/esp32-wifi-bt-coex-refs/SCOPE.md)

```text
kill: SoftAP×BT als „stabil laut Guide“; USB-Coex-Sheet als RF-SoT; Prefer-API als aktuell;
      bt-analyzer ACL-kB/s als Fremd-Desk-FACT
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + closed 2026-11-12 | erfüllt |
| 2 | Sheet `esp-wifi-bt-coex` Primary D · Maturity R2/R0/R0/W2 | erfüllt |
| 3 | SoftAP C1 / STA Y / `SW_COEXIST` / Core-Pin dokumentiert | erfüllt |
| 4 | Status-Bits + prefer deprecated + EXTERNAL + #12434/#1291/FAQ | erfüllt |
| 5 | Gap: keine Public-Mess-Repos `esp_coex_*`+A2DP+WiFi thr. | erfüllt |
| 6 | Abgrenzung USB-Coex + BTDM; bt-dual-mode Sheet Cross-Ref | erfüllt |
| 7 | Key Decision UART HCI vs same-chip `esp_coex_*` | erfüllt |
| 8 | C10–C13 Desk; Application Kontrast ohne Remeasure | erfüllt |
| 9 | Lab HCI_TCP Diskriminierung SoftAP vs STA | FOLLOW-ON |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Neuer Slug `esp-wifi-bt-coex` (Primary **D**) | Reicht BTDM oder USB-Coex? | Kampagnenziel; Abgrenzung | Neu — RF WiFi↔BT; reused nur als Kontrast | `KNOWN BEFORE TEST` |
| SoftAP CONNECTED+BT = C1; STA+BT = Y | Welche WiFi-Rolle für HCI_TCP? | `002`, `003` | STA bevorzugen; SoftAP×BT meiden | `DISCOVERED DURING TEST` |
| Prefer-API nicht empfehlen | Ist prefer aktuell? | `007` | Status-Bits / Stack-Pfad | `DISCOVERED DURING TEST` |
| UART HCI offload vs same-chip Coex-Tuning | Reicht `esp_coex_*` für HCI_TCP+Classic? | `010`–`012` + Gap | Architekturentscheid vor Feintuning; Lab FOLLOW-ON | `KNOWN BEFORE TEST` |
| bt-analyzer ~41–45 kB/s nicht als Desk-FACT | Misst dieses Audit? | Application Kontrast | Nur Projekt-`MEASURED` → Application-`INFERENCE` | `KNOWN BEFORE TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `002`/`003` | Vor HCI_TCP SoftAP: Guide-C1 vs STA-Y im konkreten Build verifizieren | `KNOWN BEFORE TEST` |
| `004`/`005` | `SW_COEXIST` + Core-Pin im sdkconfig, nicht annehmen | `KNOWN BEFORE TEST` |
| `006`/`009` | A2DP: App-Status-Bits vs Bluedroid Vendor HCI — wer setzt Streaming? | `DISCOVERED DURING TEST` |
| `007` | Keine Prefer-API in neuen Docs/Code-Reviews | `DISCOVERED DURING TEST` |
| `012` | Keine erfundenen „Mess-Repos“ als Vorbild zitieren | `DISCOVERED DURING TEST` |
| Application | ACL-kB/s nur mit Projekt-STATUS-Link; Epistemik `MEASURED`/`INFERENCE` trennen | `KNOWN BEFORE TEST` |

## Kill-Kriterien

Präregistriert für künftigen Lab (**C12**); hier kein Messlauf.

**Hypothese (Lab):** Unter SoftAP CONNECTED+BT bricht HCI_TCP/ACL-Stabilität klar gegenüber STA+BT — konsistent mit Guide-C1; UART-HCI entlastet same-chip TDM messbar.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Desk behauptet SoftAP×BT sei Guide-seitig stabil | Integritäts-Kill |
| 2 | USB-Coex- oder BTDM-Sheet als RF-WiFi↔BT-SoT verkauft | Integritäts-Kill |
| 3 | Prefer-API als aktuelle Empfehlung | Integritäts-Kill |
| 4 | bt-analyzer ACL-Zahlen als Fremd-Desk-`FACT`/`MEASURED` | Integritäts-Kill |
| 5 | Lab: SoftAP×BT und STA×BT gleich stabil unter gleicher HCI_TCP-Last → C1-Framing für diesen Use-Case prüfen | präregistriert |
| 6 | Lab: UART-HCI ohne Vorteil vs. getuntes STA+`esp_coex_*` → Offload-Priorität senken | präregistriert |

```text
NO JUSTIFIED KILL CRITERION (Kampagnen-Exit)
Begründung: Desk schließt Coex-Karte + Gap; Lab-Diskriminierung FOLLOW-ON.
```

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Desk-Quellen / Epistemik | Kampagnen-Evidence; Abgrenzung zu [`usb-wifi-coex-discrimination`](../../methods/usb-wifi-coex-discrimination.md) (USB-Domäne — **nicht** anwenden) |

## Bezug Inventar

- Projekt: [`esp32-wifi-bt-coex-refs`](../../projects/esp32-wifi-bt-coex-refs/)
- Sheet: [`esp-wifi-bt-coex`](../../technologies/esp-wifi-bt-coex/SHEET.md)
- Application: [`applications/esp-wifi-bt-coex.md`](../../projects/esp32-wifi-bt-coex-refs/applications/esp-wifi-bt-coex.md)
- Abgrenzung: [`bt-dual-mode-coex`](../../technologies/bt-dual-mode-coex/SHEET.md) · [`esp32-s3-usb-wifi-coex`](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md)
- Kontrast-Projekt: [`esp32-bt-analyzer`](../../projects/esp32-bt-analyzer/)

## Ergebnisse

- [`evidence.md`](evidence.md) — `EVID-WBTCOEX-2026-11-12-*`
- Key Decision: **UART HCI offload** entlastet WiFi↔BT-TDM vs. **same-chip SoftAP/STA + `esp_coex_*`-Tuning** (SoftAP×BT meiden).

## Knowledge Feedback

**C13:** n/a Lab/Field — Desk-only. Rückkanal: Sheet A + Application B (Kontrast) + FOLLOW-ON.

| Ergebnis | Evidence-ID | Zurück in |
|----------|-------------|-----------|
| RF Coex-Karte Desk | `001`–`011` | Sheet · Application |
| Public-Mess-Gap | `012` | Sheet Fallstricke · FOLLOW-ON |
| UART vs same-chip Entscheidungsskizze | Decision Trace | INVENTORY · FOLLOW-ON |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 präregistrierte Kill-Kriterien | PASS; Messlauf offen |
| C13 Knowledge Feedback | n/a dokumentiert |

## Lessons → Transfer

- WiFi↔BT ist **TDM + Status-Bits**, nicht USB-PHY und nicht BTDM.
- SoftAP CONNECTED + BT = **C1**; für HCI_TCP eher STA oder UART-HCI.
- Prefer-API ist tot; A2DP läuft über Status-Bits / Bluedroid Vendor HCI.
- Kein Public-Messvorbild — Gap bleibt; eigene Lab-Matrix nötig.
- Downstream-Entscheidung zuerst: **UART HCI offload** vs. same-chip Coex-Tuning.

## Offene Punkte nach Abschluss

- Lab SoftAP vs STA unter HCI_TCP + Classic
- Status-Bit / Vendor-HCI Wirkung unter Last
- bt-analyzer Topology-Entscheidung (UART vs WiFi SoftAP/STA)
