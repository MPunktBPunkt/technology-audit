# Technology Sheet: USB Android Open Accessory (AOA)

```yaml
slug: usb-aoa
title: USB Android Open Accessory (AOA)
primary: C
tags: [usb-host, automotive, foreign-desk]
type: protocol
status: active
seen_in: [hu-probe, pidrive, bimmergestalt-idrive-refs]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
  evidence_scope: []
pilot: audits/usb-aoa-bmw-connected-2026-desk
```

Ebene **A** (technologieweit, AOSP/Google). BMW-Transport-Hypothesen → Applications /
Kampagne [`usb-aoa-bmw-connected-2026-desk`](../../audits/usb-aoa-bmw-connected-2026-desk/).  
**Nicht** BCL/Etch/RHMI (`bmw-bcl`, `bmw-etch-rpc`, `bmw-rhmi`). **Nicht** USB-MSC-Gadget
(`usb-msc`). Host-Rolle ESP → Kontrast [`esp-usb-host`](../esp-usb-host/SHEET.md).

## Kurzfassung

**AOA** ist ein USB-Vendor-Protokoll, mit dem ein externes Gerät (**Accessory = USB Host**)
ein Android-Gerät in den **Accessory Mode** schaltet und danach über **Bulk-Endpoints**
einen eigenen Byte-Stream führt. AOA definiert Handshake (Control 51/52/53), Identitäts-
Strings und nach dem Switch Google-VID/`0x2D0x`-PIDs — **kein** Anwendungsprotokoll.
Alles darüber (BCL, Framing, App-Logik) ist fremd und muss getrennt auditiert werden.

## Definition und Rolle im USB-Stack

| Rolle (AOA-Begriff) | USB-Rolle | Typische Aktion |
|---------------------|-----------|-----------------|
| Accessory | **USB Host** | speist Bus, enumeriert, sendet Vendor-Control 51→52→53, danach Bulk IN/OUT |
| Android-powered device | **USB Device** (Accessory Mode) | antwortet auf 51, empfängt Strings, re-enumeriert als `0x18D1` / `0x2D0x` |

**Status:** `FACT` · Ebene **A** · Quelle: AOSP AOA 1.0 / 2.0  
([aoa](https://source.android.com/docs/core/interaction/accessories/aoa),
[aoa2](https://source.android.com/docs/core/interaction/accessories/aoa2)).

Nach erfolgreichem Switch: Kommunikation über Bulk-Endpoints mit **eigenem**
Kommunikationsprotokoll der Accessory-App — AOA spezifiziert nur den Rohranschluss.

## Handshake (zwingend)

Reihenfolge laut AOSP, wenn das Gerät **noch nicht** in Accessory Mode ist:

```text
1) Control IN  request=51  Get Protocol   → u16 LE Version (≠0 = unterstützt)
2) Control OUT request=52  Send String    → je String-ID 0..5 (UTF-8, max 256 B, zero-terminated)
3) [AOAv2 optional] Control OUT request=58 SET_AUDIO_MODE  (vor START; Audio deprecated Android 8+)
4) Control OUT request=53  Start Accessory → kein Data
5) Warten auf Re-Enumeration; VID 0x18D1 + passende PID prüfen
6) SET_CONFIGURATION; Bulk-EPs der Accessory-Interface(s) claimen
```

| Schritt | Status | Ebene | Quelle |
|---------|--------|-------|--------|
| 51 → 52 → 53 Pflichtpfad zum Switch | `FACT` | A | AOSP aoa |
| 58 nur AOAv2 Audio, vor 53 | `FACT` | A | AOSP aoa2 |
| Re-Enum nach 53 | `FACT` | A | AOSP aoa |
| Schon `0x18D1`+`0x2D00`/`0x2D01` → kein Start nötig | `FACT` | A | AOSP aoa |
| AOA und MTP gleichzeitig | `REJECTED` | A | AOSP: disconnect nötig für MTP-Wechsel |

## Identitäts-Strings (Request 52)

| Index | Name | Spec | Praxis-Relevanz |
|-------|------|------|-----------------|
| 0 | Manufacturer | spezifiziert | App-Matching / `accessory_filter` / Dialog |
| 1 | Model | spezifiziert | App-Matching (häufig entscheidend) |
| 2 | Description | spezifiziert | UI/Filter |
| 3 | Version | spezifiziert | optional, aber fehlende Version + version-only Match → Crash-Risiko Android ≤10 |
| 4 | URI | spezifiziert | Install-/Info-URL wenn keine App |
| 5 | Serial | spezifiziert | Instanz-Unterscheidung |

**Status:** `FACT` Indices/Limits · AOSP aoa.  
**INFERENCE (A):** Manufacturer+Model sind die kritischen Match-Felder für Android Intent /
Filter; URI/Serial oft optional.  
**FACT (A):** Ohne Manufacturer+Model unterdrückt AOAv2 App-Dialoge und lässt die
Accessory-USB-Interface weg (Dock/Audio-only-Pfad) — AOSP aoa2 „Connect without an Android app“.

## PIDs und Interfaces

VID nach Switch: **Google `0x18D1`**.

| PID | Version | Interfaces / Bedeutung |
|-----|---------|------------------------|
| `0x2D00` | AOAv1+ | 1 Interface, 2 Bulk (App-Kommunikation) |
| `0x2D01` | AOAv1+ | 2 Interfaces × 2 Bulk (Accessory + ADB); ADB nur wenn USB-Debugging |
| `0x2D02` | AOAv2 | audio only |
| `0x2D03` | AOAv2 | audio + adb |
| `0x2D04` | AOAv2 | accessory + audio |
| `0x2D05` | AOAv2 | accessory + audio + adb |

**Status:** `FACT` · A · AOSP aoa / aoa2.  
AOAv2 Protocol-Version = `2` (Get Protocol); abwärtskompatibel zu v1.  
**Audio:** AOAv2 USB-Audio **deprecated Android 8.0** — nur Status notieren, nicht vertiefen.

AOAv2 HID: Control 54–57 auf EP0 (kein neues Interface) — außerhalb Connected-App-Transport-Scope.

## Endpoints / Transport-Charakter

- Nach Config: Bulk IN + Bulk OUT der Accessory-Interface(s).
- Payload-Inhalt: **nicht** AOA-spezifiziert → reines Byte-Rohr.
- AOSP Car `AoapInterface`: praktisches Payload-Limit **16384** B / Timeout **2000** ms
  (`FACT` Code AOSP packages/services/Car — Host-Stack-Limit, keine USB-Spec-Grenze).

## Abgrenzung zu BCL / Connected Apps

| Schicht | Was | Sheet |
|---------|-----|-------|
| USB AOA | Host-Switch + Bulk-Rohr | **dieses Sheet** |
| BCL | 8-Byte-MUX Framing über dem Stream | [`bmw-bcl`](../bmw-bcl/SHEET.md) |
| Etch / RHMI / SAS | darüber | `bmw-etch-rpc` / `bmw-rhmi` |
| BT SPP/RFCOMM | Alternativ-Transport unter BCL | [`bluetooth-spp`](../bluetooth-spp/SHEET.md) — hier nur Kontrast |
| USB-MSC | orthogonale HU-Schnittstelle (Storage) | [`usb-msc`](../usb-msc/SHEET.md) |

**REJECTED:** AOA = BCL. AOA liefert Bytes; BCL interpretiert sie (falls auf diesem Rohr).

## BMW / Connected-App (Desk — keine Wire-Claims)

| Claim | Status | Ebene | Quelle |
|-------|--------|-------|--------|
| Doc: Connected kann BT, **USB Accessory**, ENET | `FACT` (Doc) | B/C-fremd | BMWConnectedAnalysis `protocol-bcl.md` |
| BclCarLink implementiert nur BT RFCOMM | `FACT` (Code) | B | BclCarLink `BtConnection` @`7cfd959` |
| USB/ENET-BCL in BclCarLink Code | `REJECTED` | B | Contradiction EVID-BG-020 |
| AAIdrive: USB reliable; oft File Transfer → car startet Accessory | `FACT` (Doc/Issue) | B | AAIdrive connection tips; Issue #834 |
| Phone erkennt BMW-Accessory via `UsbAccessory.manufacturer` enthält `"BMW"` | `FACT` (Code) | B | AAIdrive `UsbStatus.isBMWConnected` @`3e93419` |
| NBT/NBT Evo Connected Apps über USB nutzbar | `FACT` (Doc claim) | B | AAIdrive README/FAQ — **nicht** eigenes MEASURED |
| NBT Evo F20 speist AOA Host und spricht BCL über Bulk | `UNKNOWN` (Bulk/BCL); Enum/UI **MEASURED** bei Already-Accessory | C | `EVID-AOA-030`; C1b B1/B2 |
| BCL Framing auf USB identisch zu BT | `HYPOTHESIS` / `UNKNOWN` | C | Doc impliziert; kein Capture hier |
| Feld: 51/52/53 und Bulk bei `aoa_observe` Boot | **absent** (diese Session) | C | Zähler 0; Vendor-Tap-Gap `031` |

## Typische Fallstricke (A + Ref-Evidence)

| Claim / Falle | Status | Hinweis |
|---------------|--------|---------|
| Accessory = USB Device | `REJECTED` | Accessory = Host |
| AOA = Anwendungsprotokoll | `REJECTED` | nur Rohr + Handshake |
| Strings ohne `\0` immer ok | `INFERENCE` Fallstrick | Spec: zero-terminated; Refs senden oft ohne explizites `\0` |
| Manufacturer/Model/Filter mismatch | `FACT` Praxis | Accessory-Kit: App, `accessory_filter.xml`, Host-Strings müssen matchen |
| AOA-Versuch auf jedem USB-Device | `FACT` Praxis | AOA-Proxy: Default aggressiv; Exclude-Liste nötig; Nebenwirkungen |
| Kernel-Driver an IF0 blockiert Control | `FACT` Praxis | AOA-Proxy: detach/force oder Device ignorieren |
| Re-Enum nicht abwarten | `REJECTED` robust | Handle nach 53 schließen; neu öffnen mit Google VID/PID |
| AOAv2 Audio als zukunftssicherer Pfad | `REJECTED` | deprecated Android 8+; AAIdrive: USB-Audio für Apps weg |
| ESP32 Host: Control-Paket von Hand bauen | `INFERENCE` Fallstrick | Forum: `usb_host_transfer_submit_control` korrekt füllen |
| AOA Device-Mode parallel zu MSC/MTP | `REJECTED` (AOA↔MTP) | AOSP; MSC-Gates unberührt lassen |
| Framing SOH/EOT = AOA | `REJECTED` | Accessory-Kit App-Framing über dem Rohr |

## Transfer

Wiederverwendbar als **Transportkarte**: Handshake, PIDs, Rollen, Abgrenzung zu BCL.  
Für hu-probe / PiDrive / Connected-App-Control-Plane: nur als **ITransport**-Kandidat denken —
keine Festlegung „wir bauen AOA“. MSC-Pfad bleibt SoT für Storage-Host-C.

### Projektstart-Checkliste

- [ ] Rollen klären: Host-Accessory vs. Device-in-Accessory-Mode (Projektabhängig!)
- [ ] AOA ≠ BCL ≠ MSC explizit trennen
- [ ] Strings/Filter-Matching geplant (falls App-seitig)
- [ ] PID-Matrix AOAv1 vs v2; Audio bewusst aus Scope
- [ ] Transport-Interface agnostisch (`ITransport` → später `AoaTransport` / `SppTransport`)
- [ ] Keine Wire-Claims ohne C1b Capture
- [ ] Application + `seen_in`; `field_evidence` erst nach eigenem Lab/Field

## Referenzen

- AOSP: [AOA 1.0](https://source.android.com/docs/core/interaction/accessories/aoa), [AOA 2.0](https://source.android.com/docs/core/interaction/accessories/aoa2), [protocol overview](https://source.android.com/docs/core/interaction/accessories/protocol)
- AOSP Car `AoapInterface.java` (VID/PID/51–53/58 Konstanten)
- Desk-Kampagne: [`usb-aoa-bmw-connected-2026-desk`](../../audits/usb-aoa-bmw-connected-2026-desk/)
- Connected-App-Stack: [`bimmergestalt-idrive-2026-foreign`](../../audits/bimmergestalt-idrive-2026-foreign/)
- Refs (Evidence only): timotto/AOA-Proxy@`f66aa42`; StiffSockets/Accessory-Kit@`1c7f650`; AAIdrive@`3e93419`; BclCarLink@`7cfd959`

## Offene Fragen (A → C1b)

- Welche Manufacturer/Model-Strings sendet die NBT-/NBT-Evo-HU beim AOA-Switch?
- Welche PID erscheint nach Switch am Phone (2D00 vs 2D01 vs Audio-Mix)?
- Trägt der Bulk-Stream BCL-Frames (Header 8 B BE) wie auf BT?
- Kann ein ESP32-S3 als **Host-Accessory** oder nur als **Device-in-AOA** relevant sein für unser Zielbild?
- Interferenz AOA vs. bestehendem MSC-Gadget am selben OTG-Port?

## Lessons

- AOA ist Schicht unter BCL — Doc „USB Accessory“ ≠ BclCarLink-Implementierung.
- AAIdrive beobachtet Accessory-Präsenz auf dem Phone; sie implementiert den HU-Host-Handshake nicht.
- Referenz-Repos zeigen Handshake-Robustheit und Filter-Matching, nicht BMW-Wire-FACTS.
