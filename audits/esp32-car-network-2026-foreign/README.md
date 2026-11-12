# Audit Campaign: esp32-car-network-2026-foreign

```yaml
id: esp32-car-network-2026-foreign
project_id: esp32-car-network-refs
started: 2026-11-12
ended: 2026-11-12
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "multi-2026-11-12"
upstream_pins:
  trombik/esp_wireguard: "9217c5b"
  martin-ger/esp32_nat_router: "08da293"
  CamM2325/microlink: "216da33"
reuse_outcomes:
  reused:
    - bt-dual-mode-coex
    - esp32-s3-usb-wifi-coex
    - iobroker-fritzwireguard-adapter
  new:
    - esp-wireguard
    - esp-wifi-nat-router
    - esp-tailscale-client
  not_helped:
    - "SoftAP-Wait als primäres Car-Rendezvous"
    - "reines WireGuard ohne erreichbaren Endpoint / keepalive hinter NAT"
  process: "Desk Fremd-Pins; A6/B1 Blocker = outbound hinter Hotspot/NAT; Rendezvous > SoftAP."
  decisions_touched:
    - prefer-microlink-rendezvous
    - wg-needs-endpoint-or-keepalive
    - nat-router-lab-not-car-primary
    - softap-bt-c1-gate
```

## Ziel

ESP32 car-side **outbound** über Phone-Hotspot/NAT klären (bt-analyzer A6/B1 Blocker): WireGuard-Component, SoftAP+STA NAT-Router (Lab), Tailscale-compat Rendezvous — Go/No-Go für Reachability-Muster ohne Attack-Content.

## Scope

[SCOPE](../../projects/esp32-car-network-refs/SCOPE.md) — **Desk only**. Pins immutable. Kein Build/Lab in diesem Lauf.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 0.7.1 + lab-tool + drei Pins | erfüllt |
| 2 | Sheets + Apps: wireguard / nat-router / tailscale-client (Primary D) | erfüllt |
| 3 | Decision: microlink-Rendezvous > SoftAP-Wait | erfüllt |
| 4 | SoftAP+BT C1 dokumentiert; kein `esp-wifi-bt-coex` Sheet → Note (nachträglich: Sheet parallel durch `esp32-wifi-bt-coex-2026-foreign` angelegt) | erfüllt |
| 5 | C10–C13 | erfüllt |
| 6 | Lab Hotspot MEASURED | FOLLOW-ON |

## Decision Trace — C10

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Primär-Rendezvous | SoftAP-Wait oder Tailscale-style? | `EVID-CARNET-2026-11-12-020`–`022` | **microlink/DERP+STUN** bevorzugen | KNOWN BEFORE TEST |
| Reines WG ausreichend? | Endpoint hinter Hotspot erreichbar? | `…-001`, `…-002` | Nein ohne erreichbaren Endpoint **oder** keepalive-Mapping; peer_is_up separat | KNOWN BEFORE TEST |
| nat_router Rolle | Car-Primär oder Lab? | `…-010`, `…-030` | **Lab-AP**; SoftAP+BT C1 | KNOWN BEFORE TEST |
| SoftAP+BT produktiv? | Espressif Coex-Klasse? | `…-030` | Gate C1; kein neues Coex-Sheet jetzt | KNOWN BEFORE TEST |
| Primary Kategorie | D oder F? | Taxonomy | **D** konsistent (`[esp-idf, networking, vpn]`) | KNOWN BEFORE TEST |

## Engineering Review Checks — C11

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `…-001` | `persistent_keepalive` gesetzt wenn STA hinter NAT/Hotspot; Config enthält keys/endpoint/port | KNOWN BEFORE TEST |
| `…-002` | Observability: nicht nur `connect` ESP_OK — `peer_is_up` / Link-State pollen | KNOWN BEFORE TEST |
| `…-010` | nat_router WG-Pfad = `vpn_manager` → esp_wireguard; kein doppeltes WG-Stack-Annehmen | KNOWN BEFORE TEST |
| `…-020` | microlink: PreferredDERP advertise == connected region; DERP-Failover bedacht | KNOWN BEFORE TEST |
| `…-030` | Kein SoftAP+Classic-BT Car-Pfad ohne C1-Gate / Coex-Plan | KNOWN BEFORE TEST |

## Kill-Kriterien — C12

**Hypothese:** Ein outbound Rendezvous (microlink-Stil) hinter Phone-Hotspot kann Analyzer-Reachability für A6/B1 tragen, ohne SoftAP-Wait und ohne öffentlichen WG-Endpoint.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Desk zeigt kein DERP/STUN-Muster und kein WG-Keepalive-Pfad für Hotspot-NAT | nicht eingetreten |
| 2 | SoftAP als einzig dokumentiertes Muster und SoftAP+BT als „stabil“ behauptet | nicht eingetreten (C1 Gate) |

```text
NO JUSTIFIED KILL CRITERION (Lab)
Begründung: Desk schließt Musterwahl; Falsifikation der Reachability braucht Lab G-HOTSPOT — präregistriert als FOLLOW-ON, nicht als Desk-Kill.
```

**Präregistriertes Lab-Kill (FOLLOW-ON):** G-HOTSPOT — Hotspot STA + microlink → Peer unerreicht trotz DERP und korrekter Auth → Muster für A6 verwerfen oder Gate verschärfen.

## Knowledge Feedback — C13

Desk-Evidence in Applications/Sheets verdrahtet. Lab/Field noch offen:

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| G-HOTSPOT (Phone AP → ESP STA → Peer) | neue `EVID-CARNET-YYYY-MM-DD-nnn` | `applications/esp-tailscale-client.md` |
| G-WG-KA (keepalive hinter NAT) | neue ID | `applications/esp-wireguard.md` |
| SoftAP+BT C1 Messung | neue ID | `applications/esp-wifi-nat-router.md` + Sheet `esp-wifi-bt-coex` |

Desk-`FACT` ≠ Lab-`MEASURED`.

## Empfehlung kurz

| Bedarf | Muster |
|--------|--------|
| Car Analyzer Reachability (A6/B1) | **esp-tailscale-client** (microlink: WG+DERP+STUN) |
| Fester WG-Peer, Endpoint erreichbar | `esp-wireguard` + keepalive hinter NAT |
| Lab SoftAP / Portmap / Bench | `esp-wifi-nat-router` (SoftAP+BT = C1) |

## Lessons → Transfer

- Hinter Hotspot/CGNAT: Rendezvous (DERP) schlägt SoftAP-Wait und reines WG ohne Endpoint.
- `connect` OK ≠ Peer up; keepalive ist NAT-Pflicht, kein Nice-to-have.
- SoftAP+BT ist Espressif C1 — Lab-AP ja, Car-Primär nein.
- WiFi↔BT-Coex gehört ins Sheet [`esp-wifi-bt-coex`](../../technologies/esp-wifi-bt-coex/SHEET.md) (parallel entstanden), nicht nach `bt-dual-mode-coex`.

## Bezug

[INVENTORY](../../projects/esp32-car-network-refs/INVENTORY.md) · [evidence](evidence.md) · Kontext: [`esp32-bt-analyzer`](../../projects/esp32-bt-analyzer/) A6/B1
