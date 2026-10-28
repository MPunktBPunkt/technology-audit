# Audit Campaign: bt-classic-gaps-2026-foreign

```yaml
id: bt-classic-gaps-2026-foreign
project_id: bt-classic-profile-refs
started: 2026-10-28
ended: 2026-10-28
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "multi-2026-10-28"
upstream_pins:
  a2dpSinkHfpClient: "df6c5f4"
  EspBle: "ef09bed"
  esp32-hsp-hf: "a7c9529"
  esp32-bthidbridge: "5d3a563"
  BTClassicSPP: "0186d36"
  esp-idf: "4d80c1b"
  btstack: "0f4dd2a"
reuse_outcomes:
  reused: [bluetooth-a2dp, avrcp, bluetooth-stack]
  new:
    - bluetooth-hfp
    - bluetooth-spp
    - bluetooth-hid
    - bt-dual-mode-coex
    - hid-cross-transport-bridge
  not_helped:
    - "esp32-hsp-hf als HSP — Code ist HFP HF"
    - "IDF classic_bt als BTDM-Bridge-SoT — Examples BR/EDR-only"
    - "generisches classic-relay"
  process: "Desk Classic gaps; A2DP nur Cross-Ref; Cross-Transport HID als eigenes Pattern."
  decisions_touched:
    - fact-hfp-not-a2dp
    - fact-spp-vs-ble-uart
    - fact-hid-classic-vs-hogp
    - reject-idf-examples-as-btdm-ref
    - fact-hid-cross-transport-pattern
```

## Ziel

Classic-Lücken schließen: **HFP**, **SPP**, **HID**, **Dual-Mode Coex**, optional **HID Cross-Transport** — Anschluss an Gateway/Bridge/Media, nicht weiteres A2DP.

## Scope

[SCOPE](../../projects/bt-classic-profile-refs/SCOPE.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + multi-pin | erfüllt |
| 2 | Inventory 7 Quellen (Profile/Rollen/Coex) | erfüllt |
| 3 | Sheets HFP/SPP/HID/Dual-Mode/Cross-Transport | erfüllt |
| 4 | Evidence Code-Links | erfüllt |
| 5 | Reuse bt-gateway/pidrive/bridges | erfüllt |
| 6 | C10–C12 | erfüllt |
| 7 | `ta-assist check` 0 errors | erfüllt |
| 8 | Lab HU/Gateway HFP | FOLLOW-ON (kein Kampagnen-Exit) |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Eigenes `bluetooth-hfp` | A2DP-Sheet genug? | `…-001`/`…-002` | Neu — Call+SCO | KNOWN BEFORE |
| Eigenes `bluetooth-spp` | = BLE-UART? | `…-040` | Neu + Abgrenzung | DISCOVERED |
| `bluetooth-hid` + Cross-Transport | Ein Sheet? | `…-032`/`…-061` | Zwei Sheets | DISCOVERED |
| IDF ≠ BTDM-SoT | Examples BTDM? | `…-033` | `REJECTED` | DISCOVERED |
| hsp-hf Name | HSP Code? | `…-020` | Als HFP werten | DISCOVERED |

## Engineering Review Checks

| Evidence | Check |
|----------|-------|
| `…-002` | A2DP+HFP: I2S/Mux/Suspend explizit |
| `…-003` | Classic-only mem_release ⇒ kein stilles BLE danach |
| `…-040` | SPP SEC_NONE/PIN nicht als Produktdefault |
| `…-061` | HID Bridge: Queue-Politik nach Device-Klasse |
| `…-013` | Dual-Host Classic nur ESP32 Gate |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Nur A2DP-Wiederholung | nicht eingetreten |
| 2 | Ein Sheet „classic-relay“ ohne Profil | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk schließt Profile-Taxonomie; Gateway-Lab bleibt FOLLOW-ON.
```

## Taxonomie-Mapping

| Achse | Sheet |
|-------|-------|
| Call + SCO | `bluetooth-hfp` |
| RFCOMM Serial | `bluetooth-spp` |
| Reports Classic/HOGP | `bluetooth-hid` |
| BTDM Budget | `bt-dual-mode-coex` |
| HOGP↔Classic Bridge | `hid-cross-transport-bridge` |
| Media | `bluetooth-a2dp` / `avrcp` (bestehend) |

### Profile × Quelle

| | a2dpHfp | EspBle | hsp-hf | bthid | SPP | IDF | btstack |
|--|---------|--------|--------|-------|-----|-----|---------|
| HFP HF | Y | Y | Y | — | — | Y | Y |
| HFP AG | — | Y | — | — | — | Y | Y |
| SPP | — | Y | — | — | Y | Y | Y |
| HID Dev | — | Y | — | Y Classic | — | Y | Y |
| HID Host | — | Y | — | Y BLE | — | — | Y |
| A2DP | Y | Y | — | — | — | Y | Y |
| BTDM App | N | Y | Flag | Y | ? | N ex. | Port |

## Reuse → eigene Projekte

| Projekt | Übernehmen | Nicht still |
|---------|------------|-------------|
| **esp32-bt-gateway / pidrive** | HFP HF + A2DP Mux; Classic-only vs BTDM Entscheidung | EspBle Dual-Host ohne ESP32-Gate |
| **Bridge-Projekte** | SPP vs BLE-UART Tabelle; HID Cross-Transport nur bei Legacy-Host | SPP SEC_NONE |
| **a2dpsinkhfpclient / espble** (KB) | HFP von observed → Sheet-Link | — |

## Lessons

- Profil + Rolle + Audio/Data-Pfad + Coex steuern Sheet-Wahl — nicht „Classic“.
- IDF-Examples sind Rollen-SoT, nicht BTDM-Bridge-SoT.
- Repo-Namen können lügen (`hsp-hf` = HFP).

## Bezug

[INVENTORY](../../projects/bt-classic-profile-refs/INVENTORY.md) · [evidence](evidence.md) · Prior A2DP-Katalog: [`a2dpsinkhfpclient-2026-foreign`](../a2dpsinkhfpclient-2026-foreign/) · [`espble-2026-foreign`](../espble-2026-foreign/) · [`esp-idf-classic-bt-2026-foreign`](../esp-idf-classic-bt-2026-foreign/)
