# Project Application: BCL+Etch Handshake (AOA→App) — Desk

```yaml
project_id: bimmergestalt-idrive-refs
tech_slug: bmw-bcl
related_tech: [bmw-etch-rpc, usb-aoa]
status: active
sheet: ../../../technologies/bmw-bcl/SHEET.md
etch_sheet: ../../../technologies/bmw-etch-rpc/SHEET.md
aoa_sheet: ../../../technologies/usb-aoa/SHEET.md
audit: ../../../audits/bimmergestalt-idrive-2026-foreign/
aoa_audit: ../../../audits/usb-aoa-bmw-connected-2026-desk/
c1b_plan: ../../../audits/usb-aoa-bmw-connected-2026-desk/C1b-PLAN.md
maturity:
  technology: R2
  implementation: R2   # fremd: BclCarLink client
  field_evidence: R0   # kein eigenes BCL-on-USB Capture; AOA Enum only
  reusability: W2
updated: 2026-10-29
standard_version: "0.7.1"
```

**Zweck:** Evidenzbasiertes Desk-Dokument für den Übergang
**USB-AOA-Bulk → BCL-Session → Etch/SAS**, damit hu-probe den Handshake gezielt
nachbauen / beobachten kann. **Keine** spekulativen Lückenfüllungen; Fehlendes ist
als Capture-/Dokumentations-Lücke markiert.

**Pins (shallow clone 2026-10-29):** BclCarLink@`7cfd959`, wireshark_bmw_bcl@`07b7982`,
BMWConnectedAnalysis@`9e96ac6`, IDriveConnectKit@`95492b0`,
IDriveConnectKitAndroid@`4a567bc`, AAIdrive@`3e93419`.
Zusätzlich Narrative: [hufman.github.io/stories/bmwconnectedapps](https://hufman.github.io/stories/bmwconnectedapps).

---

## 0. Quellen-Inventar (Handshake-relevant)

| Quelle | Pfad / Artefakt | Was belegt |
|--------|-----------------|------------|
| **BclCarLink** | `bcl/BclPacket.kt` | 8-Byte BE Header, COMMAND-Enum, Handshake/Knock/SelectProto Layouts |
| **BclCarLink** | `client/BclClientTransport.kt` | Session-Init `decodeHex("12345678")`, wartet auf HU-HANDSHAKE, SelectProto(3)+Knock |
| **BclCarLink** | `android/BtConnection.kt` | Einziger Wire-Transport: BT RFCOMM SPP UUID `00001101-…` |
| **BclCarLink** | `android/BtClientService.kt` | Etch-Proxy Listen **4007**, HU-Dest **4004** |
| **BclCarLink** | `android/EtchProxyService.kt` | Broadcast `ACTION_CAR_ACCESSORY_ATTACHED` + `TRANSPORT_SWITCH=BT` |
| **BclCarLink** | `multiplex/BclMultiplexer.kt` | OPEN vor Kanal; DATA/CLOSE Routing |
| **BclCarLink** | `protocols/WatchdogProtocol.kt` | Dest **5001** / `0x1389`, Ping `13 37 13 37` |
| **BclCarLink** | `test/.../BclPacketTest.kt` | Beispiel Handshake-Payload (synthetisch) |
| **wireshark_bmw_bcl** | `bmw_bcl.lua` | Val1–3/Len-Namen→cmd/src/dst/len; Startup-Magic 4 B `12345678`; AppTypes; Dest-Namen |
| **wireshark_bmw_bcl** | `bmw_bcl_etch.lua` | Etch-Reassembly über BCL; Magic `de ad be ef` |
| **BMWConnectedAnalysis** | `docs/protocol-bcl.md` | Framing-Tabelle; USB/BT/ENET als Multiplex-Träger (Doc) |
| **BMWConnectedAnalysis** | `docs/app-behavior.md` | Start: BT/USB → BCL → ATTACHED Intent → TCP Etch |
| **BMWConnectedAnalysis** | `docs/protocol-etch.md` | Erste App-Calls: `sas_certificate` → challenge → `sas_login` |
| **BMWConnectedAnalysis** | `docs/authentication.md` | SAS-Sequenz, Cert-Typen, Challenge-Längen (observed) |
| **IDriveConnectKit** | `IDriveConnection.kt` | Etch TCP URI + `maxPktSize=8388608` |
| **IDriveConnectKit** | `BMWRemoting.etch` | IDL `sas_*` / `rhmi_*` / … |
| **IDriveConnectKitAndroid** | `IDriveConnectionListener.kt` | Intent-Konstanten ATTACHED/DETACHED/INFO |
| **IDriveConnectKitAndroid** | `security/SecurityAccess.kt` + `PrivateKeyHandling.kt` | Binder/JNI Signatur-Pfad; XOR+MD5withRSA (öffentlich dokumentiert) |
| **AAIdrive** | `connections/UsbStatus.kt` | BMW-Accessory = `UsbAccessory.manufacturer` contains `"BMW"` |
| **AAIdrive** | `connections/CarConnectionDebugging.kt` | BCL Ready über SPP **oder** USB-Accessory **oder** ATTACHED |
| **AAIdrive** | `CarProber.kt` / `carapp/*/…App.kt` | Etch-Client: Cert→Login→`rhmi_getCapabilities` |
| **AAIdrive** | `docs/connection.md` | USB oft File-Transfer vor Apps-Connection |
| **Story** | hufman.github.io | Discovery-Pfad: Val1–3/Len → DEADBEEF → Etch; localhost Proxy |
| **Eigenes Repo** | `EVID-AOA-*`, C1b-PLAN, hu-probe Feld 2026-10-29 | AOA Enum ja; Bulk/BCL-on-USB **UNKNOWN** |
| **Captures im Repo** | — | **fehlen** (kein PCAP mit Session-Init / Handshake) |

---

## 1. Gesamtablauf (Schichten)

```text
[USB Host = HU]                     [USB Device = Phone / Probe]
     │                                       │
     │  AOA Control 51/52/53 (AOSP)          │  ← nur wenn Device noch nicht Accessory
     │  Re-Enum → VID 0x18D1 PID 0x2D00/01   │
     │  Bulk IN/OUT „Rohr“ offen             │  AOA spezifiziert KEIN App-Framing
     │                                       │
     │══════════ Byte-Stream (Bulk) ═════════│
     │                                       │
     │         BCL Multiplex Tunnel          │
     │   (gleiche Framing-Idee wie BT SPP)   │  USB-Identität = Doc + AAIdrive Ready;
     │                                       │  Wire-Identität USB = Capture fehlt
     │         dest 0x0FA4 = Etch bytes      │
     │                                       │
     │   Phone: TCP localhost Proxy :4007    │  ← Connected / BclCarLink
     │   App: Etch TCP → BMWRemoting         │
     │   sas_certificate → challenge → login │
     │   rhmi_getCapabilities / …            │
```

### 1.1 USB/AOA-Ebene → Bulk offen

| Schritt | Beleg | Status |
|---------|-------|--------|
| Accessory = USB Host, Android = Device | AOSP AOA / `EVID-AOA-001` | FACT A |
| Control 51→52→53, Re-Enum `0x18D1:0x2D0x` | AOSP / `usb-aoa` Sheet | FACT A |
| Bulk trägt „own communication protocol“ | AOSP; AOA≠BCL | FACT A |
| NBT Evo enumeriert Probe als Accessory `0x2D00` | hu-probe Feld `EVID-AOA-030` | MEASURED C (Enum) |
| Vendor 51/52/53 und Bulk-RX am Already-Accessory-Boot | Feld: Counts 0 | MEASURED ABSENT (Pfad) |
| BCL-Frames auf USB-Bulk | — | **UNKNOWN** — Capture fehlt (`EVID-AOA-026`) |

### 1.2 Erster BCL-Frame / „Knock“ / Session-Init — wer zuerst?

Aus **BclClientTransport.connect()** (Phone-Client-Rolle, belegt für BT-Streams):

| # | Richtung | Was | Beleg |
|---|----------|-----|-------|
| 1 | **Phone → HU** | Session-Init Magic **4 Bytes** `12 34 56 78` (Hex-Decode von String `"12345678"`), wiederholt alle ~1 s solange noch kein Handshake | `initSession()`; lua Heuristik `pktlen==4 && hex==12345678` |
| 2 | **HU → Phone** | Erster BCL-Packet: **HANDSHAKE** (cmd=4), Payload 8 B: `version`, `instanceId`, `bufferSize` | `waitForHandshake` / `readHandshake` — alles andere → FAIL |
| 3 | **Phone → HU** | Wenn `version > 3`: **SELECTPROTO** mit Payload version=`3`, danach **KNOCK** | `selectProtocol` / `doKnock` |
| 4 | — | State → ACTIVE; danach OPEN/DATA/CLOSE Multiplex | `BclMultiplexer` |

**Wichtig (Doc↔Code):** Analysis `app-behavior.md` schreibt skizzenhaft „BCL knock and handshake“ Phone→Car. Der **implementierte** Client wartet auf **Handshake von der HU** und sendet Knock **danach**. Wer auf dem USB-Pfad zuerst sendet, ist **nicht** durch USB-Capture belegt — nur der BT-Client-Pfad.

**AAIdrive** beobachtet Status `SESSION_INIT_BYTES_SEND` (über Connected BCL-Report Intent) als „stuck“ wenn Apps in der HU nicht freigeschaltet — das korreliert mit dem Init-Byte-Warten, ist aber kein Wire-Hex-Beweis.

### 1.3 BCL-Multiplex-Header

Story-Namen **Val1 / Val2 / Val3 / Length** = Code/Dissector **command / src / dest / dataLen** — je **u16 big-endian**.

| Offset | Feld | Story-Name | Bekannte Werte |
|--------|------|------------|----------------|
| 0 | command | Val1 | siehe COMMAND-Tabelle |
| 2 | src | Val2 | virtuelle Source-ID (Kanal) |
| 4 | dest | Val3 | **0x0FA4** Etch; **0x1389** Watchdog |
| 6 | dataLen | Length | Payload-Länge; Doc „bis ~4000“ |

### 1.4 Übergang zu Etch (`0xDEADBEEF`)

1. Nach ACTIVE öffnet Client Kanäle per **OPEN**(src, dest) — Etch-Dest = **4004 = 0x0FA4**.
2. BclCarLink startet **TcpProxyProtocol** Listen **127.0.0.1:4007**, mappt TCP→BCL DATA auf dest 4004.
3. Broadcast ATTACHED → Apps verbinden Etch-TCP zum Proxy.
4. Etch-Wire beginnt mit Magic **`DE AD BE EF`** (Apache Etch) — Story + `bmw_bcl_etch.lua` + Analysis.

### 1.5 Security-Challenge → Service-Discovery

Nach Etch-Connect (App-Ebene, **nicht** BCL-Header):

```text
sas_certificate(p7b)  →  _result: challenge (Doc: observed 16 B)
sas_login(response)   →  (Doc: ~512 B / RSA4096-Größe)
rhmi_getCapabilities("", 255)  →  u.a. hmi.type / vehicle.type
… RHMI create/setResource/… (außerhalb dieses Handshake-Fokus)
```

Beleg: Analysis authentication/protocol-etch; AAIdrive `CarProber` / Apps; IDL.

---

## 2. Konkrete Byte-Strukturen

Alle Hex-Dumps unten sind **aus Code/Unit-Test/Dissector abgeleitet**.  
**Kein** Hex stammt aus einem eigenen oder im Repo liegenden Wire-Capture.

### 2.1 Session-Init (Phone → HU)

| | |
|--|--|
| Bytes | `12 34 56 78` |
| Länge | **4** |
| Herkunft | `"12345678".decodeHex()` in `BclClientTransport.initSession` |
| Dissector | `bmw_bcl.lua`: genau 4 Bytes, Label „BMW BCL Startup“ |

**Korrektur gegenüber hu-probe `sendKnock("ascii8"|"12345678")`:** Firmware sendet derzeit die **ASCII**-Zeichen `31 32 33 34 35 36 37 38` (8 B). Das ist **nicht** der BclCarLink-/Lua-Beleg. Nächster Knock-Test muss **`12 34 56 78`** senden (Pattern-Name z. B. `hex4` / `session_init`).

### 2.2 HANDSHAKE (HU → Phone) — Layout

```text
00 04 | 00 00 | 00 00 | 00 08 |  vv vv  ii ii  bb bb bb bb
 cmd    src     dest    len=8     version  instanceId  bufferSize (u32 BE)
```

Beispiel **nur aus Unit-Test** (nicht Capture): version=4, instanceId=14, bufferSize=0x8000:

```text
00 04 00 00 00 00 00 08 00 04 00 0e 00 00 80 00
```

Feld-Semantik: FACT (Code). Konkrete Werte am NBT Evo: **Capture fehlt**.

### 2.3 SELECTPROTO(3) (Phone → HU, wenn version>3)

```text
00 05 00 00 00 00 00 02 00 03
```

### 2.4 KNOCK (Phone → HU) — BclCarLink Default

Payload-Struktur (alle Längen u16 BE, dann Bytes):

```text
serial_len | serial | bt_len | bt | mac_len | mac | wifi_len | wifi | appType | param1
```

Default in `doKnock`: alle Adressfelder leer, `appType=0` (A4A), `param1=1`:

```text
Header:  00 08 00 00 00 00 00 0c
Payload: 00 00 00 00 00 00 00 00 00 00 00 01
Gesamt:  00 08 00 00 00 00 00 0c 00 00 00 00 00 00 00 00 00 00 00 01
```

**Hinweis:** hu-probe Pattern `bcl_knock` sendet nur 8-Byte-Header mit `len=0` — das ist **kein** BclCarLink-Knock (dort `len=12`). Als Experiment ok, aber nicht als „offizieller Knock“ labeln.

AppTypes (Dissector): 0=A4A, 1=TouchCommand, 2=Carplay, 3=AndroidAuto. Code-Kommentar: alternativ `appType=1`, `param1=7`.

### 2.5 OPEN Etch-Kanal (Beispiel src=1)

```text
00 01 00 01 0f a4 00 00
```

### 2.6 Watchdog

| | |
|--|--|
| Dest | `0x1389` = 5001 |
| Ping-Payload (Client) | `13 37 13 37` |
| Interval / Timeout | 5 s / 20 s (`WatchdogProtocol`) |

### 2.7 Konstanten-Kurzliste

| Konstante | Wert | Schicht |
|-----------|------|---------|
| Session-Init | `12 34 56 78` (4 B) | BCL pre-frame |
| Etch dest | `0x0FA4` / 4004 | BCL |
| Watchdog dest | `0x1389` / 5001 | BCL |
| Etch magic | `DE AD BE EF` | Etch in DATA |
| Proxy listen | 4007 (BclCarLink) | TCP localhost |
| App fallback port | 8003 (AAIdrive Defaults) | TCP |
| Simulator | 4006 | Fake-HU |
| SPP UUID | `00001101-0000-1000-8000-00805F9B34FB` | BT only |
| AOA Accessory VID/PID | `0x18D1` / `0x2D00`–`0x2D05` | USB |

### 2.8 Richtungstabelle (Client-Implementierung)

| Bytes / Frame | Richtung (BclCarLink-Rolle) | USB-Wire belegt? |
|---------------|----------------------------|------------------|
| `12 34 56 78` | Phone → HU | nein |
| HANDSHAKE | HU → Phone | nein |
| SELECTPROTO / KNOCK | Phone → HU | nein |
| OPEN / DATA / CLOSE / DATAACK | beide (MUX) | nein |
| Watchdog ping | Phone → HU (dest 5001) | nein |
| Etch `DEADBEEF`… | in DATA dest 0x0FA4 | nein |
| sas_* / rhmi_* | Etch RPC über Proxy | nein (USB); BT historisch Analysis |

---

## 3. Rollenverteilung

### 3.1 Wer initiiert den BCL-Tunnel?

| Akteur | Rolle | Beleg |
|--------|-------|-------|
| **Offizielle MyBMW / Connected** | Primärer Tunnel-Owner: wartet auf USB-Accessory **oder** BT; führt BCL; startet localhost Etch-Proxy; broadcastet ATTACHED | Analysis `app-behavior.md` |
| **BclCarLink** | **Ersatz**-Tunnel für BT RFCOMM: derselbe BCL-Client + Proxy + ATTACHED-Intent (`TRANSPORT_SWITCH=BT`) | `BtClientService` / `EtchProxyService` |
| **AAIdrive** | **Kein** BCL-Transport. Lauscht ATTACHED / BCL-Reports; prüft USB-Accessory-Präsenz und SPP; spricht Etch als App | `IDriveConnectionReceiver`, `UsbStatus`, `CarConnectionDebugging` |
| **IDriveConnectKit(+Android)** | Etch-Client-Factory, Intent-Listener, SecurityAccess — kein USB-Host/AOA, kein BCL-Framer | Kit-Repos |

### 3.2 Was AAIdrive selbst macht vs. delegiert

| Funktion | AAIdrive | Offizielle App / BclCarLink |
|----------|----------|------------------------------|
| AOA Switch 51/52/53 | nein (Device-seitig beobachtet nur Accessory) | Connected (Phone Device) + HU Host |
| BCL Session / MUX | nein | Connected oder BclCarLink |
| ATTACHED Intent senden | nein | Connected / BclCarLink |
| ATTACHED empfangen → Etch connect | **ja** | — |
| Cert merge + `sas_*` | **ja** (via SecurityAccess) | Connected Security Service / Module |
| RHMI Apps | **ja** | — |

USB-Ready in AAIdrive (`ConnectionStatusModel`):  
`isSPPAvailable || isUsbAccessoryConnected || isBCLConnected` — d. h. Accessory-Präsenz reicht als **Vorbedingungs-UI**, ersetzt aber nicht den Tunnel.

### 3.3 Bereits als Client in BclCarLink / Kit

| Komponente | Status |
|------------|--------|
| BCL Framer + Handshake/SelectProto/Knock | **implementiert** (Stream-agnostisch) |
| BT RFCOMM Bindung | **implementiert** |
| USB Accessory / AOA Bindung | **nicht** implementiert (`EVID-BG-020`, Contradiction Doc↔Code) |
| ENET | Doc only |
| Etch TCP Proxy :4007 → dest 4004 | **implementiert** |
| SAS / RHMI | **nicht** in BclCarLink — in Kit + AAIdrive |

---

## 4. Security-Grenze (für Emulation)

### 4.1 Ablauf (API-FACT)

1. App lädt/merged P7B (`APP` + `APP_AUTH` Cert-Typen in X509-Extension).
2. `sas_certificate(cert)` → HU liefert Challenge.
3. Challenge wird über **CarSecurityService / Security Module** (Binder oder eingebettetes JNI) signiert → `sas_login(response)`.
4. Danach RHMI/CDS/AV/AM freigeschaltet (Capability-/Permission-abhängig).

### 4.2 Was aus APKs / öffentlichen Quellen bekannt ist

| Element | Extrahierbar / dokumentiert | Quelle |
|---------|----------------------------|--------|
| App-P7B-Bundles / ContentProvider-Certs | ja (Analysis + Story) | APK / CarAPI |
| IDL-Methoden `sas_*` | ja | `BMWRemoting.etch` |
| Challenge-Länge observed 16 B; Response ~512 B | Doc INFERENCE | `authentication.md` / `protocol-etch.md` |
| Algorithmus-Skizze (XOR mit MD5(u32le=2) + MD5withRSA, Key aus APP_AUTH) | in Analysis + `PrivateKeyHandling` öffentlich | Desk — **kein** Bypass-How-to hier |
| RHMI-Resource-SHA256-Whitelist in Cert | Doc FACT | Analysis |

### 4.3 Was den nativen Security-Service braucht

| Element | Realistisch ohne OEM/Connected-Modul? |
|---------|----------------------------------------|
| Gültige Challenge-Response am echten Fahrzeug | **blockierend**, sofern kein installiertes Connected/MyBMW-Security-Modul (oder Simulator-Stub) |
| Simulator SAS stub | lab-tauglich ohne Fahrzeug (`Simulator` :4006) |
| Nur BCL-Framing beobachten / Knock senden | **ohne** SAS möglich |
| Voller RHMI-Stack auf ESP32 | **nicht** realistisch in einem Schritt (Etch+Cert+UI) |

### 4.4 ESP32 / hu-probe Realismus

| Ziel | Einschätzung |
|------|----------------|
| AOA Device darstellen + Bulk beobachten | laufend (C1b); Enum MEASURED |
| Session-Init `12 34 56 78` senden + auf HANDSHAKE warten | **nächstes realistisches BCL-Experiment** |
| SelectProto+Knock nach Handshake | realistisch, sobald Handshake-Bytes vom Wire |
| OPEN Etch + DEADBEEF sprechen | Framing realistisch; Semantik braucht Etch-Stack |
| sas_login am echten HU | **blockierend** ohne Security-Modul / autorisierte Umgebung |
| RHMI auf Probe | außerhalb C1b-Scope |

---

## 5. Ableitung für hu-probe

### 5.1 Minimaler Knock-/Init-Test (nächster aktiver Schritt)

Voraussetzung: Bulk-Rohr überhaupt beschrieben (C1b B1 / Phone-like oder Already-Accessory mit TX-fähigem Vendor-IF).

1. **TX:** genau 4 Bytes `12 34 56 78` (nicht ASCII-8).  
2. **RX:** ≥16 Bytes erwarten → als BCL lesen; erstes Packet muss HANDSHAKE (cmd=`0004`, len=`0008`) sein.  
3. Bei Erfolg optional TX: SelectProto(3) + voller Knock (20 B wie oben).  
4. **Kein** Auto-Feed in `BclFramer` vor stabilem Header-Muster (C1b-PLAN).  
5. Parallel: Referenz-Capture Phone+Connected (BT oder USB) für Hex-Korrelation.

### 5.2 Was wir erzeugen vs. von der HU erwarten

| Wir (Probe als Phone-Client) | Erwarten von HU |
|------------------------------|-----------------|
| Session-Init Magic | HANDSHAKE (version/instanceId/bufferSize) |
| SELECTPROTO(3), KNOCK | (Antworten: **nicht dokumentiert** im Client — Capture fehlt) |
| später OPEN Watchdog/Etch, DATAACK | DATA/CLOSE/HANGUP; Watchdog-Pong |
| — | AOA Host-Seite (wenn Probe noch nicht Accessory) |

Wenn Probe die **HU-Rolle** spielen soll (Accessory Host): Rollen **umkehren** — dann müsste die Probe HANDSHAKE **senden**. Das ist in BclCarLink **nicht** implementiert (nur Client). HU-seitiges Handshake-Verhalten: **Capture fehlt**.

### 5.3 Offene Fragen / fehlende Captures

| ID | Lücke |
|----|-------|
| G-USB-1 | Existiert BCL auf NBT-Evo-USB-Bulk nach Accessory? |
| G-USB-2 | Gleiches Init `12 34 56 78` auf USB wie auf BT? |
| G-HS-1 | Exakte Handshake-Bytes (version/instanceId/bufferSize) am Ziel-HU |
| G-HS-2 | Sendet die HU jemals zuerst ohne Phone-Init? |
| G-KN-1 | Knock-Antwort / Pflichtfelder serial/bt/mac |
| G-ET-1 | Erste Etch-Frames nach OPEN 0x0FA4 (Richtung, Länge) |
| G-AOA-1 | Wann HU 51/52/53 sendet vs. Already-Accessory |
| G-SEC-1 | Challenge-Länge am NBT Evo (nur „observed 16“ in Doc) |

### 5.4 Empfohlene Experiment-Reihenfolge

1. C1b B1 Phone-like / Control-Sicht (bereits geplant).  
2. Init-Magic **hex4** TX + Bulk RX dump (dieses Dokument §5.1).  
3. Bei HANDSHAKE: SelectProto+Knock; Framer quality (C1b-P1).  
4. Referenz-PCAP Phone+Connected (USB und/oder BT) → Evidence-IDs.  
5. Erst danach Etch/SAS-Diskussion für Probe — nicht vorher.

---

## 6. Code-Referenzen (Pin + Stelle)

| Thema | Repo@Pin | Datei | Stelle (ungefähr) |
|-------|----------|-------|-------------------|
| Header serialize/read | BclCarLink@7cfd959 | `…/bcl/BclPacket.kt` | `readFrom`, `serialize`, `COMMAND`, `Specialized.*` |
| Session-Init + HS wait | BclCarLink | `…/client/BclClientTransport.kt` | `initSession`, `waitForHandshake`, `selectProtocol`, `doKnock` |
| BT-only wire | BclCarLink | `…/android/BtConnection.kt` | `SDP_BCL`, `connectBcl` |
| Proxy ports / ATTACHED | BclCarLink | `BtClientService.kt`, `EtchProxyService.kt` | `ETCH_*`, `announceProxy` |
| MUX OPEN | BclCarLink | `…/multiplex/BclMultiplexer.kt` | `openConnection` → `Open` |
| Watchdog | BclCarLink | `…/protocols/WatchdogProtocol.kt` | `WATCHDOG_PORT`, `WATCHDOG_DATA` |
| Dissector / Magic | wireshark@07b7982 | `bmw_bcl.lua` | Startup `12345678`; COMMAND/DST/APPTYPE |
| Etch wrap | wireshark | `bmw_bcl_etch.lua` | `DE AD BE EF` |
| Doc framing / USB claim | Analysis@9e96ac6 | `docs/protocol-bcl.md`, `app-behavior.md` | — |
| Auth sequence | Analysis | `docs/authentication.md`, `protocol-etch.md` | Mermaid + Challenge notes |
| Etch connect | Kit@95492b0 | `IDriveConnection.kt` | `getEtchConnection` |
| Intent / Security | KitAndroid@4a567bc | `IDriveConnectionListener.kt`, `security/*` | ATTACHED; `signChallenge` |
| USB observe / BCL ready | AAIdrive@3e93419 | `UsbStatus.kt`, `CarConnectionDebugging.kt`, `ConnectionStatusModel.kt` | manufacturer BMW; Ready-OR |
| SAS→Capabilities | AAIdrive | `CarProber.kt` | `sas_certificate` → `sas_login` → `rhmi_getCapabilities` |
| Narrative | Story | hufman.github.io/stories/bmwconnectedapps | Val1–3, DEADBEEF, Proxy |

---

## 7. Epistemic Summary

| Claim | Status |
|-------|--------|
| BCL 8-Byte BE Framing + Commands | FACT (Code+Dissector+Doc) |
| Phone-Client: Init hex4 → wait HANDSHAKE → SelectProto3+Knock | FACT (BclCarLink) |
| dest 0x0FA4 = Etch; DEADBEEF = Etch magic | FACT |
| USB Accessory trägt BCL | Doc FACT; **Code fehlt**; Wire **UNKNOWN** |
| Exakte erste USB-Bulk-Bytes am NBT Evo | **Capture fehlt** |
| SAS API-Reihenfolge | FACT |
| Challenge immer 16 B | INFERENCE (Doc „observed“) |
| hu-probe ASCII-`12345678` ≡ BclCarLink Init | **REJECTED** (Längen/Encoding) |

Verwandt: [`bmw-bcl.md`](bmw-bcl.md) · [`bmw-etch-rpc.md`](bmw-etch-rpc.md) · [`usb-aoa.md`](usb-aoa.md) ·
[C1b-PLAN](../../../audits/usb-aoa-bmw-connected-2026-desk/C1b-PLAN.md) ·
[FOLLOW-ON bimmergestalt](../FOLLOW-ON-IDEAS.md) · [FOLLOW-ON hu-probe](../../hu-probe/FOLLOW-ON-IDEAS.md).
