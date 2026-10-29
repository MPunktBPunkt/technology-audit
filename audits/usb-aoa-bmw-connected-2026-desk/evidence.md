# Evidence — usb-aoa-bmw-connected-2026-desk

Desk 2026-10-28 · **standard_version 0.7.1** · Technologie **USB AOA** + BMW-Transport-Hinweise.

**Legende:** FACT / INFERENCE / HYPOTHESIS / UNKNOWN / REJECTED / Contradiction  
**Ebene:** A (technologieweit) / B (Projekt-Impl / Fremdcode) / C (Host-/Feld)  
**evidence_level:** R0 = fremd/desk; keine eigenen Captures in dieser Kampagne.

## Evidence Matrix

| ID | Claim | Source | Class | Ebene | Conf |
|----|-------|--------|-------|-------|------|
| `EVID-AOA-2026-10-28-001` | Accessory = USB Host; Android = Device in Accessory Mode | AOSP aoa / protocol | FACT | A | high |
| `EVID-AOA-2026-10-28-002` | Control 51 Get Protocol: IN\|VENDOR, u16 LE version | AOSP aoa | FACT | A | high |
| `EVID-AOA-2026-10-28-003` | Control 52 Send String: OUT\|VENDOR, index 0–5, UTF-8 ≤256 + `\0` | AOSP aoa | FACT | A | high |
| `EVID-AOA-2026-10-28-004` | Control 53 Start Accessory: OUT\|VENDOR, no data; dann Re-Enum | AOSP aoa | FACT | A | high |
| `EVID-AOA-2026-10-28-005` | Nach Switch VID `0x18D1`; PID `0x2D00`/`0x2D01` (+ AOAv2 `2D02`–`2D05`) | AOSP aoa / aoa2 | FACT | A | high |
| `EVID-AOA-2026-10-28-006` | `0x2D00` = 1 IF / 2 Bulk; `0x2D01` = 2 IF (acc+adb) | AOSP aoa | FACT | A | high |
| `EVID-AOA-2026-10-28-007` | Bulk trägt „own communication protocol“ der Accessory | AOSP aoa | FACT | A | high |
| `EVID-AOA-2026-10-28-008` | AOAv2 = protocol 2; Audio via req 58 vor 53; Audio deprecated Android 8 | AOSP aoa2 | FACT | A | high |
| `EVID-AOA-2026-10-28-009` | AOA und MTP nicht simultan; Disconnect zum Wechsel | AOSP aoa | FACT | A | high |
| `EVID-AOA-2026-10-28-010` | Ohne Manufacturer+Model: kein App-Dialog, keine Accessory-IF (AOAv2) | AOSP aoa2 | FACT | A | high |
| `EVID-AOA-2026-10-28-011` | Analysis Doc: BCL über BT, USB Accessory, ENET | BMWConnectedAnalysis `protocol-bcl.md` @9e96ac6 | FACT (Doc) | B | high |
| `EVID-AOA-2026-10-28-012` | BclCarLink Transport nur BT RFCOMM | BclCarLink `BtConnection.kt` @7cfd959 | FACT (Code) | B | high |
| `EVID-AOA-2026-10-28-013` | USB/ENET BCL in BclCarLink implementiert | — | REJECTED / Contradiction | B | high |
| `EVID-AOA-2026-10-28-014` | AAIdrive: USB reliable; ggf. File Transfer vor Accessory | AAIdrive connection tips / README @3e93419 | FACT (Doc) | B | med |
| `EVID-AOA-2026-10-28-015` | Phone: BMW-Accessory wenn `UsbAccessory.manufacturer` contains `"BMW"` | AAIdrive `UsbStatus.kt` @3e93419 | FACT (Code) | B | high |
| `EVID-AOA-2026-10-28-016` | BCL Ready u.a. wenn `isUsbAccessoryConnected` | AAIdrive `ConnectionStatusModel` @3e93419 | FACT (Code) | B | high |
| `EVID-AOA-2026-10-28-017` | AOAv2 USB audio für Connected USB-Audio seit Oreo weg | AAIdrive README/FAQ @3e93419 | FACT (Doc) | B | high |
| `EVID-AOA-2026-10-28-018` | Maintainer: nach Switch VID 0x18D1 PID 2D00/2D01 erwartet | AAIdrive Issue #834 (hufman) | INFERENCE / Doc | B | med |
| `EVID-AOA-2026-10-28-019` | NBT/NBT Evo Connected-Apps-fähig (Marketing/FAQ) | AAIdrive README | FACT (Doc claim) | B | low→med |
| `EVID-AOA-2026-10-28-020` | AOA-Proxy: 51→52→[58]→53; PIDs 2D00–2D05; aggressives Probe | AOA-Proxy `accessory.c` @f66aa42 | FACT (Code) | B | high |
| `EVID-AOA-2026-10-28-021` | AOA-Proxy: kernel driver an IF0 → ignore oder detach | AOA-Proxy `switchDroidToAcc` | FACT (Code) | B | high |
| `EVID-AOA-2026-10-28-022` | Accessory-Kit: Strings müssen App + filter.xml + Host matchen | Accessory-Kit README @1c7f650 | FACT (Doc/Code) | B | high |
| `EVID-AOA-2026-10-28-023` | Accessory-Kit SOH+Len+EOT Framing ist App-Protokoll über AOA | Accessory-Kit plugin/README | FACT | B | high |
| `EVID-AOA-2026-10-28-024` | ESP32-S3 Host: AOA Control via `usb_host_transfer_submit_control` | esp32.com t=28400 / t=28405 | INFERENCE (Forum) | B | med |
| `EVID-AOA-2026-10-28-025` | AOA am F20/NBT Evo Wire bestätigt | — | UNKNOWN | C | — |
| `EVID-AOA-2026-10-28-026` | BCL-Frames auf USB-Bulk NBT Evo | — | UNKNOWN | C | — |
| `EVID-AOA-2026-10-29-027` | AAIdrive: USB_STATE Profile `connected`/`mtp`/`accessory` getrennt; Accessory=BMW via manufacturer | `UsbStatus.kt` @3e93419 | FACT (Code) | B | high |
| `EVID-AOA-2026-10-29-028` | Analysis: Connected wartet auf USB Accessory **oder** BT; dann BCL knock/handshake; dann `ACTION_CAR_ACCESSORY_ATTACHED` | `app-behavior.md` @9e96ac6 | FACT (Doc) | B | high |
| `EVID-AOA-2026-10-29-029` | BclClientTransport nimmt beliebige `InputStream`/`OutputStream`; nur `BtConnection` verdrahtet RFCOMM SPP UUID | BclCarLink @7cfd959 | FACT (Code) | B | high |
| `EVID-AOA-2026-10-29-030` | Feld F20/NBT Evo: `aoa_observe` Enum `0x18D1:0x2D00`, UI Zubehör; Vendor 51/52/53=0; Bulk RX=0 | hu-probe Feld `2026-10-29-c1b-p0-aoa-observe-feld.md` / FW 0.3.23 | MEASURED (Field) | C | high |
| `EVID-AOA-2026-10-29-031` | `AoaControlTap` instrumentiert Vendor-Control-SETUPs an USBVendor; Standard/Class-Requests nicht vollständig sichtbar | hu-probe `AoaControlTap.h` | FACT (Impl) | C | high |
| `EVID-AOA-2026-10-29-032` | Post-53 Descriptor-Re-Enum in hu-probe `aoa_observe` **NOT IMPLEMENTED** (TinyUSB Descriptor lock) | hu-probe Feld / `AoaObserveGadget.h` | FACT (Impl) | C | high |
| `EVID-AOA-2026-10-29-033` | AAIdrive Doc: USB Charging Only → oft File Transfer nötig, bevor Apps-Connection startet | `docs/connection.md` @3e93419 | FACT (Doc) | B | high |

## Evidence Records (Langform, Auszug)

### EVID-AOA-2026-10-28-001

```yaml
id: EVID-AOA-2026-10-28-001
source: AOSP Android Open Accessory documentation
source_url: https://source.android.com/docs/core/interaction/accessories/aoa
source_type: spec-doc
topic: AOA roles
claim: In AOA the accessory acts as USB host (powers bus, enumerates); the Android-powered device acts as USB device in accessory mode.
classification: FACT
level: A
evidence_level: R0
confidence: high
direct_observation: false
limitations: Desk retrieval 2026-10-28; not a local AOSP tree pin
technology_audit_relevance: HIGH — foundational role model for usb-aoa sheet
hu_probe_relevance: Context — opposite of current MSC gadget role if acting as phone-side device; host role if probing like HU
```

### EVID-AOA-2026-10-28-007

```yaml
id: EVID-AOA-2026-10-28-007
source: AOSP aoa "Establish communication with the device"
source_type: spec-doc
topic: payload semantics
claim: After accessory mode, bulk endpoints carry the accessory's own communication protocol; AOA does not define application framing.
classification: FACT
level: A
evidence_level: R0
confidence: high
related_evidence: [EVID-AOA-2026-10-28-023]
technology_audit_relevance: HIGH — rejects AOA≡BCL merge
hu_probe_relevance: Gap — BclFramer would sit above ITransport, not inside AOA
```

### EVID-AOA-2026-10-28-015

```yaml
id: EVID-AOA-2026-10-28-015
source_repo: BimmerGestalt/AAIdrive
source_path: app/src/main/java/me/hufman/androidautoidrive/connections/UsbStatus.kt
source_ref: isBMWConnected / manufacturer.contains("BMW")
source_type: code
topic: Connected USB accessory detection (phone side)
claim: AAIdrive treats USB accessory attached as BMW Connected path when UsbAccessory.manufacturer contains "BMW".
classification: FACT
level: B
evidence_level: R0
confidence: high
vehicle_generation: UNKNOWN
hu_generation: UNKNOWN
limitations: Observes phone USB accessory API; does not implement HU-side 51/52/53; string exact value beyond substring BMW unknown
hu_probe_relevance: Complementary — suggests HU identity strings include BMW
pidrive_relevance: Context for future AoaTransport identity expectations
knowledge_value: HIGH
reuse: MEDIUM as hypothesis for C1b string capture
```

### EVID-AOA-2026-10-28-013

```yaml
id: EVID-AOA-2026-10-28-013
source_repo: BimmerGestalt/BclCarLink vs BMWConnectedAnalysis
source_ref: BtConnection vs protocol-bcl.md USB Accessory sentence
source_type: code + analysis-doc
topic: USB BCL implementation gap
claim: USB Accessory BCL is documented but not implemented in BclCarLink (BT-only code path).
classification: Contradiction / REJECTED as impl FACT
level: B
evidence_level: R0
related_evidence: [EVID-BG-2026-10-28-020, EVID-AOA-2026-10-28-011, EVID-AOA-2026-10-28-012]
technology_audit_relevance: HIGH — keeps USB AOA transport as open C1b item
```

## Abgelehnte / offene Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| AOA = BCL | REJECTED | Schichten |
| BclCarLink USB path | REJECTED | nur BT |
| AOA Wire FACT am NBT Evo | UNKNOWN | C1b B1 |
| BCL auf USB-Bulk | UNKNOWN | C1b B2 |
| AOAv2 Audio für neues Design | REJECTED | deprecated 8.0 |
| MSC-Host-C aus AOA ableiten | REJECTED | orthogonal |

### EVID-AOA-2026-10-29-030

```yaml
id: EVID-AOA-2026-10-29-030
source: hu-probe field note 2026-10-29-c1b-p0-aoa-observe-feld.md
source_type: field-operator + device counters
topic: C1b-P0 AOA observe vs NBT Evo
claim: With usb_gadget=aoa_observe presenting 0x18D1:0x2D00, NBT Evo enumerates the probe and shows accessory UI; AOA vendor controls 51/52/53 counts stayed 0 and bulk RX stayed 0 across replugs.
classification: MEASURED
level: C
evidence_level: R2  # own field counters/UI; not a third-party capture of Connected BCL
confidence: high
limitations: Already-accessory boot hypothesis; vendor-only control tap; post-53 re-enum not implemented; MSC absent by design
related_evidence: [EVID-AOA-2026-10-28-025, EVID-AOA-2026-10-28-026, EVID-AOA-2026-10-29-031]
technology_audit_relevance: HIGH — closes partial UNKNOWN on enum; keeps handshake/bulk UNKNOWN
hu_probe_relevance: Direct — C1b-P0 P0-A/C PASS; P0-B/E FAIL this session
```

### EVID-AOA-2026-10-29-029

```yaml
id: EVID-AOA-2026-10-29-029
source_repo: BimmerGestalt/BclCarLink
source_path: client/BclClientTransport.kt; android/BtConnection.kt
source_ref: BclClientTransport(InputStream, OutputStream); BtConnection RFCOMM only
source_type: code
topic: transport abstraction under BCL
claim: BCL client is stream-agnostic; the only concrete wire path in BclCarLink is Bluetooth RFCOMM SPP (UUID 00001101-…).
classification: FACT
level: B
evidence_level: R0
confidence: high
limitations: No named ITransport interface in BG; USB Accessory path remains doc-only
related_evidence: [EVID-AOA-2026-10-28-012, EVID-AOA-2026-10-28-013, EVID-BG-2026-10-28-020]
technology_audit_relevance: HIGH — justifies hu-probe ITransport split (Aoa/Spp) under BclFramer
```

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-28 | Desk AOA AOSP + BG Transport + drei Ref-Repos; Sheet `usb-aoa`; Kampagne closed |
| 2026-10-29 | Continuation: Tier-1 Re-Read + hu-probe C1b-P0 Feld-Gaps; C1b-PLAN.md B1/B2 |
