# Evidence — bimmergestalt-idrive-2026-foreign

Desk 2026-10-28 · **standard_version 0.7.1** · Org **BimmerGestalt** (14 Repos).  
Pins unter `/tmp/bimmergestalt/` bzw. GitHub-Metadaten wo nicht geklont.

**Legende classification:** FACT / INFERENCE / HYPOTHESIS / UNKNOWN / REJECTED  
**source_type:** code | idl | dissector | analysis-doc | readme | test | experiment  
**evidence_level (KB):** R0 = nur fremd/desk; keine eigenen Captures in dieser Kampagne.

## Evidence Matrix

| ID | Claim | Source | Classification | Confidence | Generation | hu-probe | PiDrive |
|----|-------|--------|----------------|------------|------------|----------|---------|
| `EVID-BG-2026-10-28-001` | BCL Header 8 B: cmd/src/dest/len BE + payload | BclCarLink `bcl/BclPacket.kt` @7cfd959; Analysis `protocol-bcl.md` @9e96ac6 | FACT | high | n/a (wire) | Gap (andere Schicht) | Complementary |
| `EVID-BG-2026-10-28-002` | dest 0x0FA4 (4004) = Etch | `BtClientService.ETCH_DEST_PORT`; `bmw_bcl.lua` DST_NAMES | FACT | high | n/a | Gap | Complementary |
| `EVID-BG-2026-10-28-003` | Handshake payload: version, instanceId, bufferSize (8 B) | `BclPacket.Specialized.Handshake`; `BclPacketTest` | FACT | high | n/a | Gap | Complementary |
| `EVID-BG-2026-10-28-004` | Session-Init sendet 8 Bytes aus Hex `12345678` | `BclClientTransport.initSession` | FACT | high | n/a | Gap | Context |
| `EVID-BG-2026-10-28-005` | version>3 → SelectProto(3) + Knock | `BclClientTransport` | FACT | high | n/a | Gap | Complementary |
| `EVID-BG-2026-10-28-006` | MUX OPEN/DATA/CLOSE über (src,dest) | `BclMultiplexer.kt` | FACT | high | n/a | Gap | Complementary |
| `EVID-BG-2026-10-28-007` | Watchdog Kanal 5001 / 0x1389 | `WatchdogProtocol`; lua DST_NAMES | FACT | high | n/a | Gap | Context |
| `EVID-BG-2026-10-28-008` | Etch URI `tcp://host:port?Packetizer.maxPktSize=8388608&TcpTransport.noDelay=true` | IDriveConnectKit `IDriveConnection.kt` @95492b0 | FACT | high | n/a | Gap | Complementary |
| `EVID-BG-2026-10-28-009` | IDL `BMWRemoting`: sas/cds/am/rhmi/av/map | `idriveconnectkit-etch/BMWRemoting.etch` | FACT | high | RHMIVersion ID5/ID6 enums | Gap | Complementary |
| `EVID-BG-2026-10-28-010` | Auth: sas_certificate → signChallenge → sas_login | AAIdrive apps; Analysis `authentication.md` | FACT (API-Reihenfolge) | high | Connected Classic/MyBMW | No relation (MSC) | Context / Security gate |
| `EVID-BG-2026-10-28-011` | ATTACHED Intent: host, port, instanceId, brand | IDriveConnectKitAndroid `IDriveConnectionListener` @4a567bc | FACT | high | Android Connected | No relation | Complementary |
| `EVID-BG-2026-10-28-012` | BclCarLink announced Proxy 127.0.0.1:4007 | `EtchProxyService` | FACT | high | n/a | Gap | Complementary |
| `EVID-BG-2026-10-28-013` | RHMI: XML + create/setResource/initialize/handlers | Kit deserialization; AAIdrive `NotificationApp` | FACT | high | ID4/5/6 via caps | Gap | Complementary (UI layer) |
| `EVID-BG-2026-10-28-014` | Layout aus `hmi.type` / `hmi.version` (ID4/5/6, EntryEvo_ID5_) | `RHMIDimensions.kt`; CarProber | FACT | high | ID4/5/6 | Complementary (Gen-Labels) | Complementary |
| `EVID-BG-2026-10-28-015` | AV: av_create(instanceId) + av_requestConnection ENTERTAINMENT | `AVContextHandler`; IDL | FACT | high | n/a | Gap | Possibly relevant (alt audio path) |
| `EVID-BG-2026-10-28-016` | Simulator Etch server :4006; SAS stub | Simulator `CarServer` / `BMWRemotingServerImpl` @6a38086 | FACT | high | lab fake HU | Lab tool idea | Lab tool idea |
| `EVID-BG-2026-10-28-017` | Experiment richtext List-Model + Markup | IDriveExperiments `HomeView` @4b6d5fa | FACT (Code) | med | UNKNOWN HU | No relation | Context |
| `EVID-BG-2026-10-28-018` | CDS ContentProvider `io.bimmergestalt.cardata.provider` | AAIdrive `CDSContentProvider` | FACT | high | n/a | No relation | Context |
| `EVID-BG-2026-10-28-019` | Dissector: AppTypes A4A/TouchCommand/Carplay/AndroidAuto | `bmw_bcl.lua` APPTYPE_NAMES | FACT (Dissector) | med | n/a | Gap | Context |
| `EVID-BG-2026-10-28-020` | Doc USB/ENET BCL; Code nur BT RFCOMM | Analysis `protocol-bcl.md` vs BclCarLink `BtConnection` | Contradiction | high | n/a | Gap | Open investigation |
| `EVID-BG-2026-10-28-021` | Challenge length 16 bytes observed | Analysis `authentication.md` | INFERENCE | med | n/a | No relation | Context |
| `EVID-BG-2026-10-28-022` | NBT/NBT Evo Kompatibilität (Marketing/FAQ) | AAIdrive README/FAQ | FACT (Doc claim) | low→med | NBT/NBT Evo | Confirmed label only | Confirmed label |
| `EVID-BG-2026-10-28-023` | ReadYou/breezy = Consumer-Forks, kein Protokollkern | GitHub README (nicht geklont) | FACT (meta) | high | n/a | No relation | No relation |
| `EVID-BG-2026-10-28-024` | HassGestalt RHMI assets from SmartThings APK | `external.gradle` @63da6a4 | FACT | high | n/a | No relation | Context |
| `EVID-BG-2026-10-28-025` | `rhmi_create_version` in IDL, keine Kotlin-Calls | Grep Kit/AAIdrive | FACT (IDL≠Nutzung) | high | n/a | — | — |
| `EVID-BG-2026-10-29-026` | BCL client stream-agnostisch; konkreter Wire nur BT RFCOMM | BclCarLink `BclClientTransport` / `BtConnection` @7cfd959 | FACT | high | n/a | Gap→C1b | Open USB |
| `EVID-BG-2026-10-29-027` | Doc Start: USB Acc oder BT → BCL knock/handshake → ATTACHED → Etch TCP | Analysis `app-behavior.md` @9e96ac6 | FACT (Doc) | high | n/a | Gap | Complementary |

## Evidence Records (Langform, Auszug)

### EVID-BG-2026-10-28-001

```yaml
id: EVID-BG-2026-10-28-001
source_repo: BimmerGestalt/BclCarLink
source_path: app/src/main/java/io/bimmergestalt/bcl/BclPacket.kt
source_ref: serialize/readFrom; COMMAND enum
source_type: code
topic: BCL framing
claim: BCL packets use an 8-byte big-endian header (command, src, dest, dataLen) plus payload.
evidence: Matching struct in BclPacket + protocol-bcl.md table; lua dissector same layout.
classification: FACT
evidence_level: R0
confidence: high
vehicle_generation: UNKNOWN
hu_generation: UNKNOWN
software_version: UNKNOWN
direct_observation: false
reproducibility: code-reproducible; field capture not done here
limitations: Desk foreign; no own PCAP in this audit
related_evidence: [EVID-BG-2026-10-28-002, EVID-BG-2026-10-28-006]
technology_audit_relevance: HIGH — new protocol sheet bmw-bcl
hu_probe_relevance: Gap — hu-probe measures USB-MSC host reads, not BCL
pidrive_relevance: Complementary — alternate car link layer vs MSC
knowledge_value: HIGH
reuse: HIGH (as hypothesis catalog for captures)
```

### EVID-BG-2026-10-28-010

```yaml
id: EVID-BG-2026-10-28-010
source_repo: BimmerGestalt/AAIdrive + BMWConnectedAnalysis
source_path: carapp/*/NotificationApp.kt; docs/authentication.md
source_ref: sas_certificate → signChallenge → sas_login sequence
source_type: code + analysis-doc
topic: Security / SAS
claim: Connected Apps authenticate to BMWRemoting via certificate exchange then challenge-response login before RHMI/AV.
evidence: IDL methods + AAIdrive call order + Analysis sequence diagram; signing via BMW Security Binder services (names in KnownSecurityServices).
classification: FACT  # API order / existence — NOT a how-to bypass
evidence_level: R0
confidence: high
direct_observation: false  # Analysis cites captures historically; this audit did not re-capture
limitations: No attack steps documented in KB; Security-Service availability varies by Connected/MyBMW version
technology_audit_relevance: HIGH
hu_probe_relevance: No relation to MSC probe path
pidrive_relevance: Context — Connected-App path has auth gate unlike MSC gadget
knowledge_value: HIGH
reuse: LOW without authorized environment
```

### EVID-BG-2026-10-28-015

```yaml
id: EVID-BG-2026-10-28-015
source_repo: BimmerGestalt/AAIdrive
source_path: carapp/music/AVContextHandler.kt
source_ref: av_create / av_requestConnection
source_type: code
topic: Media / AV
claim: Entertainment audio focus toward HU uses Etch AV APIs in addition to RHMI music UI widgets.
evidence: AVContextHandler + BMWRemoting.etch av_*; MusicApp listeners for granted/denied/button events.
classification: FACT
evidence_level: R0
confidence: high
limitations: Android MediaController still used phone-side; AV is HU connection layer
hu_probe_relevance: Gap
pidrive_relevance: Possibly relevant — alternate to USB-MSC for metadata/control; not a drop-in for MSC streaming architecture
knowledge_value: HIGH
reuse: MEDIUM (architecture hypothesis only)
```

## Offene / REJECTED Claims

| Claim | Status | Hinweis |
|-------|--------|---------|
| BCL acronym expansion | UNKNOWN | not in repos |
| USB/ENET BCL implemented in BclCarLink | REJECTED | only BT RFCOMM code path |
| BCL observations overwrite hu-probe MSC FACTS | REJECTED | different layer |
| NBT string is on-wire HMI type | REJECTED | capabilities use hmi.type/version |
| ReadYou/breezy contain BCL parsers | UNKNOWN→unlikely | README-only skim; classified irrelevant for protocol core |
| map_create used in AAIdrive main | REJECTED (usage) | IDL only in scanned tree |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-28 | Org 14 Repos inventarisiert; P0 deep desk; Sheets bmw-bcl/etch/rhmi; Cross-Ref hu-probe/PiDrive |
| 2026-10-29 | Continuation Desk: Transport-Abstraktion + hu-probe C1b-P0 Gaps; C1b-PLAN (kein hu-probe Code) |
| 2026-10-29 | Handshake-Desk: [`bmw-bcl-handshake.md`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md) — Init=`12 34 56 78` (4 B); ASCII-8 REJECTED; USB-Wire weiter UNKNOWN |
