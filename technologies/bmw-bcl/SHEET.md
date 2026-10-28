# Technology Sheet: BMW BCL (Car Link Multiplex)

```yaml
slug: bmw-bcl
title: BMW BCL — Connected-App Multiplex Tunnel
primary: H
tags: [automotive, protocol, foreign-desk]
type: technology
status: active
seen_in: [bimmergestalt-idrive-refs]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
  evidence_scope: []
```

Ebene **A** (Protokollbeschreibung aus Fremdquellen). Keine eigenen Lab-/Field-Captures
in diesem Sheet. Herkunft: BimmerGestalt (`BclCarLink`, `wireshark_bmw_bcl`,
`BMWConnectedAnalysis`). **Nicht** USB-MSC / NBT-Host-C.

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

## Lessons

- Fremd-Implementierung ≠ Feldbeweis; BclCarLink ist starke **static/behavioural** Quelle.
- Doc-USB/ENET ohne Codepfad = Widerspruch markieren, nicht glätten.
