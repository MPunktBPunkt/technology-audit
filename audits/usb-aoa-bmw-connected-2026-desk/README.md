# Audit Campaign: usb-aoa-bmw-connected-2026-desk

```yaml
id: usb-aoa-bmw-connected-2026-desk
project_id: hu-probe
started: 2026-10-28
ended: 2026-10-28
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "desk-2026-10-28"
upstream_pins:
  AOSP_aoa: "source.android.com/docs/.../aoa (retrieved 2026-10-28)"
  AOSP_aoa2: "source.android.com/docs/.../aoa2 (retrieved 2026-10-28)"
  AOA-Proxy: "f66aa42"
  Accessory-Kit: "1c7f650"
  AAIdrive: "3e93419"
  BclCarLink: "7cfd959"
  BMWConnectedAnalysis: "9e96ac6"
reuse_outcomes:
  reused:
    - bmw-bcl
    - bluetooth-spp
    - usb-msc
    - esp-usb-host
    - bmw-nbt-evo
  new:
    - usb-aoa
  not_helped:
    - "USB-MSC host timing / Prefetch from AOA sources"
    - "BCL framing details from AOA specs"
    - "Wire confirmation AOA@NBT Evo"
  process: "Desk External Knowledge; A/B/C Trennung; keine Wire-Claims; MSC-Gates unberührt."
  decisions_touched:
    - fact-aoa-is-byte-pipe-not-app-protocol
    - reject-merge-aoa-into-bcl-or-msc
    - keep-itransport-agnostic
    - defer-aoa-impl-until-c1b
    - contradiction-usb-doc-vs-bclcarlink-bt-only
```

## Ziel

Desk-Audit der Technologie **USB Android Open Accessory (AOA)** als möglicher
**Transport** unter BCL für Connected-App / Control-Plane (Bezug hu-probe / PiDrive /
NBT Evo) — mit klarer A/B/C-Trennung, ohne Implementierung und ohne Fahrzeug-Wire.

Leitfrage: *Was ist AOA spezifiziert, wie grenzt es an BCL, was sagen BG-Quellen zum
USB-Pfad, und was muss C1b messen?*

## Scope

**Im Scope**

- AOA 1.0 / 2.0 (Google / AOSP): Rollen, 51/52/53, Strings, PIDs, Bulk-Rohr
- Relevanz als Transport unter BCL (Abgrenzung, keine BCL-Analyse)
- Referenz-Repos als Evidence: AOA-Proxy, Accessory-Kit, ESP32-Host-Beispiele
- BimmerGestalt/AAIdrive + BclCarLink **nur Transport-Hinweise**

**Explizit außerhalb**

- BCL-Framing, Etch, DEADBEEF, BMWRemoting, SAS, RHMI, CDS, AV, AM
- Bluetooth SPP/RFCOMM (nur Kontrast)
- hu-probe Firmware-Änderungen; AOA-Implementierung auf ESP32
- Wire-Claims am NBT Evo; Audio über AOAv2 (nur Status)

Siehe Sheet [`usb-aoa`](../../technologies/usb-aoa/SHEET.md) · Evidence [`evidence.md`](evidence.md).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Technology Sheet `usb-aoa` mit Definition/Handshake/PIDs/Fallstricke | erfüllt |
| 2 | Audit-Fragen 1–9 mit FACT/INFERENCE/UNKNOWN + A/B/C | erfüllt |
| 3 | Evidence.md mit gepinnten Quellen | erfüllt |
| 4 | Applications hu-probe / pidrive / bimmergestalt (Transport-Sicht) | erfüllt |
| 5 | Keine neuen Wire-/MSC-FACTS; AOA≠BCL markiert | erfüllt |
| 6 | C1b Messfragen B1/B2 + Empfehlung ITransport | erfüllt |
| 7 | `ta-assist index` + `check` (0 errors) | erfüllt |

---

## Executive Summary

AOA ist ein **USB-Rollen-/Handshake-Protokoll**: Accessory = USB Host schaltet das
Android-Gerät in Accessory Mode (51→52→53), danach Bulk-Byte-Rohr unter Google
VID/`0x2D0x`. Es ist **kein** Anwendungsprotokoll und **nicht** BCL.

BimmerGestalt dokumentiert USB Accessory als Connected-Transport in Docs; **Code**
(BclCarLink) spricht BT RFCOMM. AAIdrive beobachtet Phone-seitig `UsbAccessory` mit
Manufacturer „BMW“ und rät File-Transfer → HU startet Accessory — Desk-`FACT` aus
Doc/Code, **kein** eigenes Feld-MEASURED am F20/NBT Evo.

**Empfehlung:** Transport-Interface agnostisch halten; AOA nicht implementieren bis
C1b B1/B2 geklärt; MSC-Gates unangetastet.

---

## Antworten Audit-Fragen 1–9

### 1 — Was ist AOA und Rolle im USB-Stack?

Accessory = USB Host; Android-Gerät = Device im Accessory Mode. AOA: Detect → optional
Switch → Bulk-Kommunikation mit App-Protokoll.  
**Status:** `FACT` · **A** · AOSP aoa/protocol.

### 2 — Handshake 51 → 52 → 53?

Get Protocol (IN 51) → Send String(s) (OUT 52, Index 0–5) → Start (OUT 53) → Re-Enum.  
AOAv2 optional 58 (Audio) vor 53.  
**Status:** `FACT` · **A** · AOSP aoa/aoa2.

### 3 — Strings — spezifiziert vs. Praxis?

Indices 0–5 spezifiziert (Manufacturer…Serial). Praxis: Manufacturer+Model für App-
Filter; Version-Fallstrick ≤Android 10; ohne Manufacturer+Model → kein App-Interface
(AOAv2 Dock-Pfad).  
**Status:** Spec `FACT` A; Match-Gewichtung `INFERENCE` A; BMW-String-Werte `UNKNOWN` C.

### 4 — PIDs / Interfaces AOAv1 vs v2?

`2D00`/`2D01` (acc / acc+adb); AOAv2 zusätzlich `2D02`–`2D05` (Audio-Kombis).  
**Status:** `FACT` · **A** · AOSP aoa2.

### 5 — Anwendungsprotokoll oder Byte-Rohr?

Nur Rohr (+ Handshake/IDs). App-Protokoll (BCL, SOH-Framing, …) liegt darüber.  
**Status:** `FACT` · **A** · AOSP („own communication protocol“).

### 6 — AAIdrive zu USB-AOA bei NBT / NBT Evo?

USB „very reliable“; File Transfer oft nötig; Accessory-Mode-Erkennung; Manufacturer
BMW; AOAv2 Audio für USB-App-Audio seit Oreo weg; VID/PID-Hinweis 0x18D1/2D00|2D01 in
Issues. Kompatibilität NBT/NBT Evo = Doc-Claim.  
**Status:** Doc/Code `FACT` **B**; Wire am Fahrzeug `UNKNOWN` **C**.

### 7 — BclCarLink Kontrast?

Nur BT RFCOMM-Implementierung; Doc Analysis nennt USB Accessory / ENET.  
**Status:** Contradiction Doc↔Code · `EVID-BG-020` / `EVID-AOA-2026-10-28-020`.

### 8 — Fallstricke Referenz-Repos?

AOA-Proxy: aggressives Probe aller Devices; kernel-driver detach; Audio-Request 58;
Exclude-Liste. Accessory-Kit: String-Triple-Match (App/filter/Host); App-Framing ≠ AOA;
Re-Enum. ESP32-Host: Control-Transfer korrekt über Host-API.  
**Status:** `FACT` Praxis **B** (Ref-Code) · keine BMW-C.

### 9 — UNKNOWN für C1b?

Siehe unten B1/B2 und Offene Messfragen.

---

## Decision Trace (C10)

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neues Sheet `usb-aoa`? | Fehlt Transport-A im KB? | 001–010 | Ja | DISCOVERED |
| AOA in `bmw-bcl` mergen? | Gleiche Schicht? | Abgrenzung | Nein | KNOWN BEFORE |
| AOA jetzt in hu-probe FW? | C1b Evidence? | UNKNOWN C | Nein — Desk only | DISCOVERED |
| MSC-Gates anfassen? | Interferenz? | Scope | Nein | KNOWN BEFORE |
| ITransport festlegen auf AOA? | Alternativen? | BT Doc/Code | Agnostisch halten | DISCOVERED |

## Engineering Review Checks (C11)

| Evidence | Check |
|----------|-------|
| 001–005 | Keine BCL-Felder als AOA-Claims zitieren |
| 011–015 | AAIdrive/BG nur als B/R0; kein MEASURED-Overwrite |
| 020–025 | Ref-Framing (SOH) nicht als AOA-Spec übernehmen |
| Sheet | Rollen Host vs Device im Projektziel explizit machen vor Lab |

## Kill-Kriterien (C12)

```text
NO JUSTIFIED KILL CRITERION for this desk campaign.
Begründung: Knowledge Acquisition ohne Messhypothese zum Verwerfen.
C1b trägt eigene Kill-Kriterien (B1 negativ → AOA-Transport-Pfad verwerfen).
```

| # | Späteres C1b-Kill | Hinweis |
|---|-------------------|---------|
| K1 | HU initiiert keinen AOA-Switch / keine 0x18D1 | B1 fail |
| K2 | Bulk ohne BCL-ähnliche Frames und ohne nutzbaren Byte-Stream | B2 fail |

## Knowledge Feedback (C13)

Desk only — kein neuer MEASURED-Claim in hu-probe/PiDrive Host-C.  
Sheet `field_evidence: R0`. Applications `implementation: R0` (kein AOA-Code).

---

## Lessons → Transfer

- AOA ist Schicht **unter** BCL; Doc „USB Accessory“ ≠ BclCarLink-Implementierung.
- AAIdrive beobachtet Phone-`UsbAccessory` (Manufacturer BMW); HU-Host-Handshake 51/52/53 ist dort nicht der Code-Pfad.
- Referenz-Repos belegen Handshake-Robustheit und Filter-Matching — keine NBT-Wire-FACTS.
- Control-Plane: `ITransport` agnostisch; AOA/SPP austauschbar unter `BclFramer`.
- MSC-Gates und Host-C bleiben orthogonal und unberührt.

## Empfehlung hu-probe / C1b-0

**Gilt aus diesem Desk**

1. AOA als möglichen **Transport unter BCL** katalogisieren — Sheet `usb-aoa`.
2. Control-Plane-Design **transport-agnostisch**: `ITransport` → später optional
   `AoaTransport` / `SppTransport`; Framer (`BclFramer`) sieht nur Bytes.
3. C1b Messfragen priorisieren (B1 Erreichbarkeit, B2 BCL-ähnliche Frames).

**Darf bewusst noch nicht**

- AOA-Handshake/Firmware auf ESP32
- SAS / Etch / RHMI / BCL-Session-Implementierung „weil AOA desk fertig“
- MSC-Pfad oder bestehende Gates ändern
- Wire-FACTS aus AAIdrive-Issues ableiten

## Offene Messfragen C1b

| ID | Frage | Erfolgskriterium (Skizze) | Stand 2026-10-29 |
|----|-------|---------------------------|------------------|
| **B1** | Ist AOA am F20 / NBT Evo erreichbar (Host-Switch, VID/PID, Accessory-Strings)? | Beobachteter Switch/`51–53` **oder** dokumentierter Fail nach Phone-like Enum | Enum/`0x18D1` ja (Already-Accessory); Control/Bulk **absent** |
| **B2** | Kommen BCL-ähnliche Frames (8 B BE Header) auf dem Bulk-Rohr? | Capture mit korrelierbarem Framing oder klar negativ | noch nicht messbar (kein Bulk) |
| B3 | Welche Manufacturer/Model sendet die HU? | String-Capture nach 52 / Phone `UsbAccessory` | offen (kein req 52) |
| B4 | Parallelität/Konflikt mit MSC-Gadget am gleichen Port? | Enum-/Mode-Matrix | bewusst isoliert (`aoa_observe` ≠ MSC) |

Ausführlicher Plan (A/B/C, Aufwand, Kill): [`C1b-PLAN.md`](C1b-PLAN.md).

### Continuation 2026-10-29 (Desk only)

- Tier-1 Re-Read: stream-agnostisches BCL; USB nur Doc; AAIdrive USB_STATE/File-Transfer/BMW-manufacturer bestätigt.
- hu-probe Feld `aoa_observe` als **A**-Evidence (`EVID-AOA-030`…`032`) — kein Code-Change in diesem Audit.
- Applications `usb-aoa` / `bmw-bcl` / `bmw-etch-rpc` + hu-probe Application ergänzt.

## Bezug

Sheet: [`usb-aoa`](../../technologies/usb-aoa/SHEET.md) ·  
Evidence: [`evidence.md`](evidence.md) ·  
C1b Plan: [`C1b-PLAN.md`](C1b-PLAN.md) ·  
Connected-App Desk: [`bimmergestalt-idrive-2026-foreign`](../bimmergestalt-idrive-2026-foreign/) ·  
Host-C MSC: [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md)
