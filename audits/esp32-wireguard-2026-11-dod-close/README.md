# Audit Campaign: esp32-wireguard-2026-11-dod-close

```yaml
id: esp32-wireguard-2026-11-dod-close
project_id: esp32-wireguard
started: 2026-11-27
ended: 2026-11-27
status: closed
profile: firmware
environment: lab
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "esp32.wireguard@v0.4.9 + hu-probe@feat/wireguard-transport + bt-analyzer@0.3.21-wg"
upstream_pins:
  trombik/esp_wireguard: "v0.9.0"
reuse_outcomes:
  reused:
    - esp-wireguard
    - esp-hub-base-template
    - esp-module-host
  new: []
  not_helped:
    - "Full-tunnel 0.0.0.0/0 on same STA LAN (blackhole)"
    - "tcpip_send_msg_wait_sem without signalling trampoline (boot hang)"
  process: "Abschluss-/Evidenz-Audit — keine neue Stack-Entscheidung. SoT + Retrieval aus Lab-FACTs."
  decisions_touched:
    - wg-optional-overlay-not-hard-dep
    - selective-allowedips-over-full-tunnel
    - sntp-before-handshake
    - consumer-ab-build-gate
```

## Ziel

**WireGuard-Meilenstein abschließen:** Transport-DoD von `esp32.wireguard` **v0.4.9** und zwei unabhängige Consumer-Lab-E2Es als SoT festschreiben — nicht neu architekturieren.

## Scope

| In | Out |
|----|-----|
| Core / Data Plane / Recovery / OTA (Referenz-FW) | Feld / Fahrzeug-Langzeit |
| hu-probe `0.3.42-wg`, bt-analyzer `0.3.21-wg` Lab-E2E | Weitere prophylaktische Consumer |
| FACT vs UNKNOWN sauber trennen | PiDrive-Implementierung |

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Vier Ebenen (Core, Data Plane, Recovery, OTA) mit Evidence-IDs | erfüllt |
| 2 | Zwei Consumer Lab-E2E dokumentiert | erfüllt |
| 3 | UNKNOWN: natürlicher WiFi-Failover + Feld | festgehalten |
| 4 | SHEET + Applications + Retrieval regeneriert | erfüllt |
| 5 | Keine neue Stack-Entscheidung | erfüllt |

## Architektur (validiert)

```text
esp-hub-base
        │
 optional WG (esp32.wireguard 0.4.9 / trombik v0.9.0)
        │
┌───────┴────────┐
▼                ▼
hu-probe         bt-analyzer
0.3.42-wg        0.3.21-wg
(Lab E2E)        (Lab E2E)
```

## Ebenen → Evidence

Siehe [`evidence.md`](evidence.md). Kurz:

| Bereich | Ergebnis |
|---------|----------|
| Core | FACT — Stack, Storage, SNTP, connect ≠ peer_is_up |
| Data Plane | FACT — Guest/WAN/NAT, selektive `/24`, Hub HTTP, Counter |
| Recovery | FACT — WLAN-Wechsel + WG-Reconnect; WG-Ausfall ohne Consumer-Abbruch (hu-probe) |
| OTA | FACT — OTA über aktiven WG-Tunnel; Config bleibt |
| Consumer hu-probe | FACT — E2E + peer_down resilience |
| Consumer bt-analyzer | FACT — E2E + Hub heartbeat |
| Natürlicher WiFi-Failover | **UNKNOWN** |
| Feld / Roaming / HU-Bedingungen | **UNKNOWN** |

## Follow-on (nicht dieser Audit)

`esp32.pidrive` — **WireGuard Integration Readiness** (separater Audit): welcher Verkehr durch den Tunnel, reicht `/24`, Failure-Semantics. **Keine Implementierung** bis Readiness geschlossen.

## Referenzen

- Repo: https://github.com/MPunktBPunkt/esp32.wireguard (v0.4.9)
- App evidence: [`../../projects/esp32-wireguard/applications/EVIDENCE-2026-11-27-v049-closed.md`](../../projects/esp32-wireguard/applications/EVIDENCE-2026-11-27-v049-closed.md)
- Sheet: [`../../technologies/esp-wireguard/SHEET.md`](../../technologies/esp-wireguard/SHEET.md)
