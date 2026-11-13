# Technology Sheet: BMW BCL (Car Link Multiplex)

```yaml
slug: bmw-bcl
title: BMW BCL — Connected-App Multiplex Tunnel
primary: H
tags: [automotive, protocol, foreign-desk]
type: technology
status: active
seen_in: [bimmergestalt-idrive-refs, esp32-usb-analyzer, hu-probe, esp32-bt-analyzer]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R0   # own HU wire still UNKNOWN; secondary NBT-AAD R1 observations (SPP contention) — see secondary note
  reusability: W2
  evidence_scope: [LAB]
```

Ebene **A** (Protokollbeschreibung aus Fremdquellen) plus **erste eigene Lab-TEST-Kette**
in [`esp32-bt-analyzer` / `bmw-bcl`](../../projects/esp32-bt-analyzer/applications/bmw-bcl.md)
(synth stream + Dummy-HU RFCOMM/SDP). **Keine** eigene HU-Wire-FACT. Herkunft Desk:
BimmerGestalt (`BclCarLink`, `wireshark_bmw_bcl`, `BMWConnectedAnalysis`).
Secondary Field-Observation (SPP-Contention / Transport-Owner): NBT-AAD
[`supra-idrive6-android-auto-2026-secondary`](../../audits/supra-idrive6-android-auto-2026-secondary/).
**Nicht** USB-MSC / NBT-Host-C.

## Kurzfassung

**BCL** ist eine Multiplex-Kapselung zwischen Handset und BMW-HU: ein physischer
Stream (beobachtet/implementiert vor allem Bluetooth RFCOMM) trägt virtuelle Kanäle
zu Diensten in der HU. Connected Apps sprechen typischerweise **Apache Etch** über
den BCL-Zielport **0x0FA4 (4004)**. BCL ist der Tunnel; Etch/RHMI liegen darüber.

## Abgrenzung

- **Ist:** 8-Byte-Header-Framing, Commands, src/dest-Kanäle, Handshake/SelectProto/Knock, Watchdog-Kanal.
- **Ist nicht:** Etch-RPC-Semantik; RHMI-UI; USB-MSC-Hostverhalten; PiDrive-Audio-Pfad.
- **Grenzt an:** [`bmw-etch-rpc`](../bmw-etch-rpc/SHEET.md), [`bmw-rhmi`](../bmw-rhmi/SHEET.md), [`bmw-nbt-evo`](../bmw-nbt-evo/SHEET.md) (andere Schicht); physischer USB-Transport-Kandidat [`usb-aoa`](../usb-aoa/SHEET.md) (AOA ≠ BCL).

## Framing (Desk-FACT aus Code/Doc)

| Feld | Typ | Bemerkung |
|------|-----|-----------|
| command | u16 BE | OPEN=1, DATA=2, CLOSE=3, HANDSHAKE=4, SELECTPROTO=5, DATAACK=6, … |
| src | u16 BE | virtuelle Source-ID |
| dest | u16 BE | Dienst in der HU; **0x0FA4 = Etch**, **0x1389 = Watchdog** |
| dataLen | u16 BE | Payload-Länge; Docs/Buffers ≈ 4000 Bytes praktisches Limit |
| data | bytes | Payload |

## Session-Skizze (Implementierung BclCarLink)

```
OPENING → init bytes → HANDSHAKE(version, instanceId, bufferSize)
  → (version>3: SELECTPROTO(3) + KNOCK) → ACTIVE
  → OPEN/DATA/CLOSE Multiplex → HANGUP
```

Klassifikation: **FACT** = so im Client-Code; **nicht** = eigenes Feld-MEASURED.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| BCL-Akronym offiziell ausgeschrieben | `UNKNOWN` | in Repos nicht belegt |
| USB/ENET-BCL identisch zu BT-Pfad | `HYPOTHESIS` | Doc nennt USB/ENET; BclCarLink nur BT; AOA-Desk [`usb-aoa`](../usb-aoa/SHEET.md) |
| BCL = Etch | `REJECTED` | Etch läuft *in* DATA-Kanälen dest 4004 |
| Dest-Port-Namen aus Lua = BMW-Spec | `INFERENCE` | Dissector aus Captures/Code, nicht OEM-Spec |
| Gleiches Framing auf allen HU-Generationen | `UNKNOWN` | Desk ohne Generations-Capture-Matrix |
| Phone-App ist RFCOMM **Server** | `REJECTED` | BclCarLink `createRfcommSocketToServiceRecord(SDP_BCL)` = **Client** (`EVID-BCLRF-2026-11-12-001`) |
| `SDP_BCL` = BMW-proprietäre UUID | `REJECTED` | generic SPP `00001101-…` (`EVID-BCLRF-2026-11-12-002`) |
| HU = SDP provider / RFCOMM server | `INFERENCE` | aus Client-Connect-Pattern; kein HU-Server-Code in BclCarLink (`EVID-BCLRF-2026-11-12-003`) |
| Watchdog nur „alive“ ohne Timing | `REJECTED` | dest **5001**, **request** `0x13371337` alle **5 s**, timeout **20 s** (`EVID-BCLRF-2026-11-12-004`) |
| HU Watchdog-Pong = exakt `13371337` | `UNKNOWN` | BclCarLink zählt jedes Antwort-Byte; kein Byte-Vergleich (`WatchdogProtocol` listener) |
| OPEN dest **4004** folgt deterministisch auf HANDSHAKE | `REJECTED` | erst nach lokalem TCP-Consumer auf Proxy `:4007` (`EtchProxyService` / `TcpProxyProtocol`) |
| A2DP = BCL-Transport | `REJECTED` | A2DP-Connected nur Discovery-Hint in `BtClientService` (`EVID-BCLRF-2026-11-12-005`) |
| Native AA (nbt-aad) = BCL-Pfad von BclCarLink | `REJECTED` | AA-UUID/`WifiStart*` ≠ Companion-BCL; Secondary `EVID-SUPRA-2026-11-13-005` Heuristik trennt Links |
| MyBMW belegt HU-SPP; parallel AAIdrive/nbt-aad stört | `FACT` (secondary) | Issue/Logs NBT-AAD (`EVID-SUPRA-2026-11-13-003`/`004`) — kein eigener Capture |
| HU = RFCOMM/SPP-Server immer / Phone immer Client | `UNKNOWN` (Spannung) | BclCarLink Client-Pattern vs. nbt-aad „CAR öffnet MyBMW-Link“ — bis Capture offen |

## Transport Owner vs. Etch Consumer

| Rolle | Akteur | Status | Beleg |
|-------|--------|--------|-------|
| **Transport Owner** (führt BCL über SPP/USB) | Connected / MyBMW (primär); BclCarLink als BT-Ersatz | Desk `FACT` + Secondary `INFERENCE` Owner-Belegung | Handshake §3.1; `EVID-SUPRA-2026-11-13-007` |
| **Etch Consumer** (kein eigener BCL-Tunnel) | AAIdrive | Desk `FACT` | Handshake §3.1; Secondary `EVID-SUPRA-2026-11-13-006`/`008` |
| **Konkurrent am HU-SPP** (nicht BCL) | nbt-aad / native Wireless AA | Secondary `FACT` Contention | `EVID-SUPRA-2026-11-13-001`–`004` |

Messbedingung A6/B1/B2: MyBMW und AAIdrive während SDP/RFCOMM-Captures **deaktivieren** und dokumentieren
([`esp32-bt-analyzer` / `bmw-bcl`](../../projects/esp32-bt-analyzer/applications/bmw-bcl.md)).

## Transfer

Wiederverwendbar als **Protokollkarte** für eigene Captures (Wireshark-Dissector-Pin).
Keine Engineering-Action ohne eigene Trace-Korrelation. Knowledge-Value **HIGH**,
eigene Evidence weiterhin **R0** bis Lab/Field.

### Projektstart-Checkliste

- [ ] Schicht BCL vs Etch vs RHMI vs USB-MSC nicht vermischen
- [ ] Claims mit Repo-Pin + Datei belegen; README allein unzureichend
- [ ] USB/ENET nur mit eigenem Capture als FACT — sonst Contradiction belassen
- [ ] Application + `seen_in` nachziehen; `field_evidence` erst nach eigenem Lab/Field

## Offene Fragen (A)

- Exakte Semantik aller Knock-Felder / AppTypes jenseits Dissector-Namen?
- USB Accessory / ENET: gleiches Handshake?
- BCL v4 „unknown watchdog“ — HU-seitig bestätigt?

Handshake-Vertiefung (Session-Init Hex, Rollen, hu-probe-Experimente):
[`bmw-bcl-handshake`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md).
Init-Bytes sind **4 B** `12 34 56 78`, nicht ASCII-8.

RFCOMM-Rollen (Phone Client / HU Server INFERENCE, SPP UUID, Watchdog Timing, A2DP Hint):
[`bmw-bcl-rfcomm`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-rfcomm.md) · Audit [`bmw-bcl-rfcomm-role-2026-desk`](../../audits/bmw-bcl-rfcomm-role-2026-desk/).

Secondary HU-SPP / Contention (NBT-AAD, R1):
[`supra-idrive6-android-auto-2026-secondary`](../../audits/supra-idrive6-android-auto-2026-secondary/).

SAS/Etch Auth: **CROSSREF** [`bmw-connected-sas-auth-2026-11-06`](../../audits/bmw-connected-sas-auth-2026-11-06/) — hier nicht duplizieren.

## Lessons

- Fremd-Implementierung ≠ Feldbeweis; BclCarLink ist starke **static/behavioural** Quelle.
- Doc-USB/ENET ohne Codepfad = Widerspruch markieren, nicht glätten.
