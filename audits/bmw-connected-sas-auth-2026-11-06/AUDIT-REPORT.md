# BMW Connected Apps Authentication Audit

```yaml
id: bmw-connected-sas-auth-2026-11-06
type: source-reverse-engineering-audit
date: 2026-11-06
standard_version: "0.7.1"
classification_scheme: [FACT, INFERENCE, HYPOTHESIS, UNKNOWN, REJECTED]
evidence_rating: [E0, E1, E2, E3, E4]
scope: desk-external + our-prior-field-AOA/BCL-only
```

**Legende Evidenzrating:** E0 Behauptung · E1 Dokumentation · E2 Quellcode · E3 Trace/Capture (fremd oder eigen) · E4 reproduzierbarer Test  
**Legende Herkunft:** `external` = Fremdquellen · `our` = eigenes technology-audit / hu-probe / Analyzer

---

## 1. Executive Summary

**SAS Authentication existiert** als Etch-Service-Methoden `sas_certificate` → Challenge → `sas_login` und ist durch IDL, AAIdrive/Kit-Code, Analysis-Docs und die hufman-Story **mehrfach unabhängig** belegt (Desk-FACT, E1+E2). Die kryptographische Antwort erzeugt die **Phone-seitige** Security-Komponente (Connected Classic Binder / MyBMW SecurityModule / rekonstruiertes `PrivateKeyHandling`); die **HU** liefert Challenge und verifiziert Zertifikat + Signatur (Doc+IDL; HU-Firmware-Code nur indirekt zitiert).

**Unser Stand:** G1 teilweise MEASURED (AOA Enum), G2 teilweise Desk + Lab-Framer ohne USB-Wire-SAS, **G3 Feld-Fact = fehlt**, G4 Feld-Fact = fehlt. AOA/BCL-Messungen sind **kein** SAS-Beweis.

---

## 2. Quellen und Evidenzqualität

| ID | Quelle | Typ | Qualität für Auth |
|----|--------|-----|-------------------|
| S1 | [hufman BMW Connected Apps Protocol](https://hufman.github.io/stories/bmwconnectedapps) | Narrative RE | E1; beschreibt Discovery-Pfad; Challenge/RSA-Größe |
| S2 | [BMWConnectedAnalysis](https://bimmergestalt.github.io/BMWConnectedAnalysis/) / `docs/authentication.md` @`9e96ac6` | Doc + AIDL | E1; detailliertste Auth-Spez |
| S3 | [AAIdrive](https://github.com/BimmerGestalt/AAIdrive) @`3e93419` | App-Code | E2; Call-Graph Cert→Login→RHMI |
| S4 | [IDriveConnectKit](https://github.com/BimmerGestalt/IDriveConnectKit) @`95492b0` | IDL + Etch client | E2; `BMWRemoting.etch` sas_* |
| S5 | [IDriveConnectAddons](https://github.com/BimmerGestalt/IDriveConnectAddons) | App-Code | E2; gleiche Auth-Sequenz |
| S6 | [BclCarLink](https://github.com/BimmerGestalt/BclCarLink) @`7cfd959` | BCL transport | E2 für Tunnel; **kein** SAS |
| S7 | [IDriveConnectKitAndroid](https://github.com/BimmerGestalt/IDriveConnectKitAndroid) @`4a567bc` | SecurityAccess | E2+E4 (Unit/Instrumented Tests) |
| S8 | [Simulator](https://github.com/BimmerGestalt/Simulator) | Fake-HU | E2; Auth **nicht** geprüft |
| S9 | [wireshark_bmw_bcl](https://github.com/hufman/wireshark_bmw_bcl) | Dissector | E2/E3-abgeleitet; Etch-Reassembly |
| S10 | Eigenes Repo: `bmw-bcl-handshake`, AOA-Desk, hu-probe Feld | prior audits | our E2/E3 für AOA; **nicht** SAS |

**Nicht gefunden trotz Suche:** öffentliche PCAPs mit SAS-Payload im Repo; HU-Firmware-Quelle für Challenge-RNG; OEM-Spec.

---

## 3. Ursprünglicher Reverse-Engineering-Prozess

Rekonstruktion aus S1 (Story) + S2 + Code-Nachfolge. Keine Spekulation über undokumentierte Lab-Tagebücher.

```text
Bluetooth SPP Capture (Android BT logging)
        ↓
Muster Val1–3/Len + 0xDEADBEEF  →  BCL Multiplex + Apache Etch  [S1]
        ↓
Wireshark Lua Dissector (bmw_bcl)  [S9]
        ↓
APK-Decompile → ValueFactoryBMWRemoting Symbolnamen → Etch-Hash/ewh  [S1]
        ↓
Localhost TCP Proxy in Connected entdeckt; Intent ATTACHED  [S1,S2 app-behavior]
        ↓
Rekonstruiertes Etch IDL → eigene Proxies  [S1 → S4]
        ↓
Fake-Car (Etch Server + Intent) → Auth-Challenge beobachten  [S1]
        ↓
CarSecurityManager / CarSecurityService Binder + JNI/OpenSSL  [S1,S2]
        ↓
Test-App: sas_certificate → signChallenge → sas_login → rhmi_getCapabilities  [S1]
        ↓
RHMI setResource Fail bei Layout-Edit → SHA256 in Cert  [S1,S2]
        ↓
AAIdrive / Kit / BclCarLink / Simulator (spätere Implementierungen)  [S3–S8]
```

| Behauptung | Ursprüngliche Evidenz | Methode | Spätere Impl |
|------------|----------------------|---------|--------------|
| BCL Multiplex | BT Capture Patterns | Lua Dissector | BclCarLink |
| Etch / DEADBEEF | Capture + Apache Docs | ewh aus Symbolen | Kit etch |
| sas_* Namen | Decompiled ValueFactory | IDL-Rekonstruktion | `BMWRemoting.etch` |
| Challenge/Response | Capture + Fake-Car | Binder-Service + Captures vergleichen | SecurityAccess |
| Resource-Hashes | Cert-Extension + Fail-Upload | Experiment am echten Auto (Story) | Doc + AAIdrive Assets |

**FACT** (E1): Story beschreibt diesen Pfad.  
**INFERENCE** (E1+E2): Heutiger Open-Source-Stack ist die Operationalisierung derselben Erkenntnisse.  
**UNKNOWN:** Datum/VIN/HU-Generation der ersten erfolgreichen Garage-Session (Story nennt Trips, keine Capture-IDs).

---

## 4. Architektur

```text
Phone Apps (AAIdrive / Spotify / …)
    │  TCP localhost (Etch)
    ▼
BMW Connected / MyBMW / BclCarLink
    │  BCL multiplex (BT RFCOMM FACT; USB Accessory Doc; ENET Doc)
    ▼
HU CarEtchServer (BMWRemoting)
    │
    ├─ SAS Authentication          ← G3
    └─ nach Login: RHMI / AV / CDS / AM  ← G4
```

Layer-Rollen:

| Schicht | Rolle | Seite |
|---------|-------|-------|
| USB AOA / BT SPP | physischer Stream | Phone Device ↔ HU Host (AOA) bzw. RFCOMM |
| BCL | Multiplex-Transport | Phone Tunnel-Owner (Connected/BclCarLink) |
| Apache Etch | RPC | App Client ↔ HU Server |
| SAS | Auth-Service in Etch | HU challenge+verify; Phone sign |
| SecurityService/Module | Signatur + APP_AUTH-Cert | **nur Phone** |
| RHMI/AV/CDS | autorisierte APIs | nach erfolgreichem Login |

---

## 5. BCL

Siehe prior Desk: [`bmw-bcl/SHEET.md`](../../technologies/bmw-bcl/SHEET.md),
[`bmw-bcl-handshake.md`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md).

Kurz (für Auth-Kontext):

| Claim | Class | E | Quelle |
|-------|-------|---|--------|
| 8-Byte Header cmd/src/dest/len BE | FACT | E2 | BclPacket.kt |
| dest `0x0FA4` = Etch | FACT | E1+E2 | Analysis + Code |
| Session-Init `12 34 56 78` (4 B hex) | FACT | E2 | BclClientTransport |
| USB trägt BCL | Doc FACT; Wire our UNKNOWN | E1 / — | protocol-bcl vs Capture-Lücke |
| BCL enthält SAS-Semantik | **REJECTED** | E2 | SAS ist Etch-RPC in DATA |

---

## 6. Apache Etch

**FACT** E2 — `IDriveConnectKit/idriveconnectkit-etch/BMWRemoting.etch` @`95492b0` Zeilen 132–136:

```text
byte[] sas_certificate (byte[] data) throws IllegalArgumentException, SecurityException;
void   sas_crl (byte[] data) throws …;
string sas_permission (byte[] data) throws …;
void   sas_login (byte[] data) throws IllegalArgumentException, IllegalStateException, SecurityException;
void   sas_logout (byte[] data) throws …;
```

**FACT** E2 — Client: `IDriveConnection.getEtchConnection(host, port, client)` → TCP URI
`tcp://host:port?Packetizer.maxPktSize=8388608&TcpTransport.noDelay=true`.

**FACT** E1 — Wire: Symbol-Hashes; Magic `DE AD BE EF` (Apache Etch / Story / Dissector).

Weitere sas_*-Methoden (`sas_crl`, `sas_permission`, `sas_logout`) existieren in der IDL;
AAIdrive Happy-Path nutzt praktisch nur `sas_certificate` + `sas_login`. Nutzung von
`sas_crl`/`sas_permission` im Feld: **UNKNOWN**.

---

## 7. SAS Authentication

### 7.1 Rekonstruierte Sequenz (korrigiertes Modell)

```text
Phone App                         SecurityService/Module              HU CarEtchServer
   │                                       │                                │
   │ createSecurityContext(pkg, appName)   │                                │
   │──────────────────────────────────────►│                                │
   │◄──────────────────────────────────────│ handle                         │
   │ (optional) loadAppCert(handle)        │                                │
   │──────────────────────────────────────►│                                │
   │◄─ APP_AUTH / connection cert ─────────│                                │
   │ merge APP + APP_AUTH → P7B            │                                │
   │                                                                        │
   │ sas_certificate(p7b)  ────────────────────────────────────────────────►│
   │◄──────────────────────────────────────────────── challenge: byte[] ────│
   │                                       │                                │
   │ signChallenge(handle, challenge)      │                                │
   │──────────────────────────────────────►│  (JNI/native oder MD5withRSA)  │
   │◄─ response: byte[] ───────────────────│                                │
   │                                                                        │
   │ sas_login(response) ──────────────────────────────────────────────────►│
   │◄─ (void / Exception) ──────────────────────────────────────────────────│
   │                                                                        │
   │ rhmi_* / av_* / cds_* … ──────────────────────────────────────────────►│
```

**Abweichung vom Auftragsskizzen-Modell:** Das Zertifikat geht **nicht** „Phone→HU“ ohne Phone-interne Vorbereitung; typisch wird APP-Cert (App-Assets) mit APP_AUTH/Connection-Cert (SecurityService) **gemerged** (`CertMangling.mergeBMWCert`). Challenge kommt von der **HU**, Signatur von der **Phone-Security-Komponente**.

### 7.2 AAIdrive Happy Path (Beispiel MusicApp)

**FACT** E2 — `AAIdrive/.../carapp/music/MusicApp.kt` init ~64–68:

1. `IDriveConnection.getEtchConnection(host, port, listener)`
2. `carAppAssets.getAppCertificate(brand)` → APP-Cert bytes
3. `carConnection.sas_certificate(appCert)` → `sas_challenge`
4. `securityAccess.signChallenge(challenge=sas_challenge)` → `sas_login` bytes
5. `carConnection.sas_login(sas_login)`
6. danach RHMI create/setResource/…

Identisches Muster: `AssistantApp`, `CalendarApp`, `CarInfoApp`, `CarProber`, Addons `screen_mirror/CarApp.kt`.

### 7.3 CarProber Variante (Cert-Merge)

**FACT** E2 — `CarProber.probeCar`: `CertMangling.mergeBMWCert(cert, securityAccess.fetchBMWCerts(brandHint))` vor `sas_certificate`.

### 7.4 State Machine (Connected-App Session)

```text
[IDLE]
  │ ATTACHED Intent / CarProber finds open TCP port
  ▼
[ETCH_CONNECTING] ──fail──► [IDLE]
  │ TCP Etch up
  ▼
[SAS_CERT] ──SecurityException/IllegalArgument──► [FAIL_AUTH]
  │ challenge received
  ▼
[SAS_SIGN] ──no SecurityService / invalid challenge──► [FAIL_AUTH]
  │
  ▼
[SAS_LOGIN] ──reject──► [FAIL_AUTH]
  │
  ▼
[AUTHORIZED] ── rhmi/av/cds/am ──► [ACTIVE_APP]
  │
  ├─ keepalive (CarProber: ver_getVersion) fail ──► [IDLE] (IDriveConnectionStatus.reset)
  ├─ DETACHED / disconnect ──► [IDLE]
  └─ sas_logout (IDL; App-Nutzung selten) ──► [IDLE?]  UNKNOWN Feldverhalten
```

---

## 8. Certificate

| Aspekt | Befund | Class | E | Quelle |
|--------|--------|-------|---|--------|
| Format | PKCS#7 / P7B (PEM `PKCS7`) | FACT | E1+E2 | authentication.md; CertMangling |
| Bundle | Mehrere X509 in einem CMS | FACT | E2 | CertMangling.loadCerts |
| Spezial-Certs | `SAS.CertificateType=APP` und `APP_AUTH` | FACT | E1 | authentication.md openssl dump |
| Extension OID | `1.3.6.1.4.1.513.59.4.1` oder `.4.2` IA5String key=value&… | FACT | E1 | authentication.md |
| APP_AUTH | Public Key für Challenge-Verifikation | FACT | E1 | authentication.md |
| APP | Permissions: AVS, CDS, RHMI, Make, Digests | FACT | E1 | authentication.md |
| Digests | `SAS.Digests.RHMIDescriptions`, `ImageDatabases`, `TextDatabases` = SHA256-Listen | FACT | E1 | authentication.md + rhmi-resources.md |
| Make | BMW / MINI / J29 | FACT | E1 | authentication.md; CarProber J29 path |
| Merge | App-P7B + Connection-Cert aus SecurityService | FACT | E2 | CertMangling.mergeBMWCert |
| Root/CA | CN `a4a_root-ca` in Bundles erwähnt (gefiltert beim Merge) | FACT | E2 | CertMangling |
| Signatur-Alg der Certs selbst | **UNKNOWN** in diesem Audit nicht neu geparsed | UNKNOWN | — | — |
| Gültigkeitsfenster Feld | **UNKNOWN** ohne eigenes Cert-Inventory | UNKNOWN | — | — |
| Private Keys | existieren in OEM-Apps / Test-`BMWAppKitDevelopment.p12` | FACT Existenz | E2 | PrivateKeyHandlingTest; **keine Extraktion hier** |

Story: Certs aus APKs / ContentProvider der Companion-Apps. AAIdrive `external/README.md`: Build extrahiert aus Connected/MyBMW APKs nach `assets/carapplications`.

---

## 9. Challenge / Nonce

| Frage | Antwort | Class | E |
|-------|---------|-------|---|
| Wer erzeugt? | HU (`CarEtchServer`) als Return von `sas_certificate` | FACT | E1+E2 IDL |
| Wann? | Sofort nach Präsentation des Cert-Bundles | FACT | E1+E2 |
| Länge? | Doc + Code-Kommentare/Tests: **16 Bytes observed** | INFERENCE (observed) | E1+E2+E4 |
| Zufallsquelle HU? | **UNKNOWN** | UNKNOWN | — |
| Pro Session neu? | **HYPOTHESIS** (Challenge-Response-Muster); kein Capture-Beweis hier | HYPOTHESIS | E0/E1 |
| Was wird signiert? | Challenge bytes; bei APP_AUTH zusätzlich XOR mit MD5(LE u32=2) | FACT (Phone Impl) | E1+E2 |
| Extra Context/Session-ID im Signatur-Input? | In `PrivateKeyHandling.signChallenge`: **nur** Challenge(+XOR) | FACT | E2 |
| Replay-Schutz? | Session-Challenge impliziert Nonce; HU-seitige Speicherung **UNKNOWN** | UNKNOWN | — |
| Timestamp/Counter im Challenge? | In 16-B Beobachtung nicht dokumentiert | UNKNOWN | — |
| Falsche Signatur? | Etch `SecurityException` / Login fail (IDL throws) | INFERENCE | E2 IDL |
| Abgelaufene Challenge? | **UNKNOWN** | UNKNOWN | — |
| Leere Challenge? | Phone: `IllegalArgumentException` (native/Classic) | FACT | E4 TestSecurityAccess |

---

## 10. Cryptography

### 10.1 Phone-seitige Antwort (belegt)

Aus `PrivateKeyHandling.signChallenge` @`4a567bc` und `authentication.md`:

```text
challenge[16]
    │
    ├─ if APP_AUTH / applyXor=true:
    │     pad = MD5( 02 00 00 00 )     # little-endian uint32 = 2
    │     message[i] = challenge[i] XOR pad[i % 16]
    │  else (legacy iOS-style):
    │     message = challenge
    ▼
Signature.getInstance("MD5withRSA")
    initSign(privateKey from APP_AUTH / PKCS12)
    update(message)
    sign() → response bytes
```

| Element | Befund | Class |
|---------|--------|-------|
| Digest+Sign | `MD5withRSA` (Java/JCE = typ. PKCS#1 v1.5 + MD5) | FACT E2 |
| Key type | RSA PrivateKey aus PKCS#12 | FACT E2 |
| Response-Länge Connected Classic | 512 Bytes (RSA-4096-Größe) | FACT E4 TestSecurityAccess |
| Response-Länge Dev-P12 Test | 192 Bytes | FACT E4 PrivateKeyHandlingTest |
| Doc „byte[512] / RSA4096“ | gilt für beobachteten Connected-Pfad | INFERENCE E1 |
| Padding-Details ASN.1 | nicht separat spezifiziert; Java `MD5withRSA` Default | INFERENCE |
| Wer signiert? | Phone SecurityService / SecurityModule / (Test) PrivateKeyHandling | FACT |
| Wer verifiziert? | HU (CarEtchServer) mit Public Key aus präsentiertem APP_AUTH | FACT Doc E1 |
| Signatur in JNI? | Official path: JNI/NDK um OpenSSL (Story); Kit rekonstruiert Java-Äquivalent | FACT Story E1; Kit E2 |
| Exakte Äquivalenz JNI↔PrivateKeyHandling am echten HU | Story: Service matches captures; Kit Unit-Test gegen Dev-Key | INFERENCE |

**Keine privaten Schlüssel in diesem Audit veröffentlicht.**

---

## 11. Authorization / RHMI whitelist

Strikte Trennung:

| Ebene | Frage | Mechanismus |
|-------|-------|-------------|
| AUTHENTICATION | Wer bist du? | P7B + Challenge/Response (`sas_*`) |
| AUTHORIZATION (Feature) | Was darfst du? | Cert-KV: `AVS`, `CDS`, `RHMI`, `Make`, … |
| RESOURCE AUTHORIZATION | Welche Layouts/Assets? | `SAS.Digests.*` SHA256-Listen |

**Claim „RHMI Layouts per SHA256 an Auth-Cert gebunden“:**

| | |
|--|--|
| Class | **FACT** (Doc + Story Experiment) |
| Wo | authentication.md; rhmi-resources.md; Story „RHMI Whitelist“ |
| Hashes | SHA256 der DESCRIPTION / ImageDB / TextDB (comma-separated) |
| Wer prüft | Doc: `CRHMIAuthPermHandler::verifyResource` in `libhmiremoting.so` (HU) |
| Wann | bei `rhmi_setResource` Upload |
| Falscher Hash | Upload rejected / Exception (Story: edit layout → fail; original → ok) |
| Negativer Test open-source? | Story Experiment; **kein** automatisierter HU-Negativtest in AAIdrive | E1 vs fehlendes E4 |
| ZIP vs Datei | ImageDB/TextDB als Zip-Uploads; Hash über die hochgeladene Resource (Doc) | INFERENCE E1 |
| Icons | ImageDatabases Digests → ja betroffen | FACT E1 |
| Cert-Typen | APP vs APP_AUTH; APP trägt Digests/RHMI flags | FACT E1 |

---

## 12. SecurityService / MyBMW

| Frage | Befund | Class |
|-------|--------|-------|
| Welche Apps? | Connected Classic, Connected, Mini-Varianten, MyBMW/MiniMine/J29Mine Regional Packages | FACT E2 KnownSecurityServices |
| Package-IDs (Auszug) | `com.bmwgroup.connected.bmw.usa`, `de.bmw.connected`, `de.bmw.connected.mobile20.row`, … | FACT E2 |
| Binder Intent Classic/Connected | `*.SECURITY_SERVICE` | FACT E2 AIDL Kommentare |
| MyBMW Komponente | `com.bmwgroup.connected.core.services.security.CarSecurityService` | FACT E2 |
| MyBMW Binder export? | Doc: ab Connected 5.1 / MyBMW **nicht** mehr exportiert für Fremd-Apps | FACT E1 |
| Alternative | `SecurityModuleManager`: `createPackageContext` + Reflection auf `com.bmwgroup.connected.core.security.SecurityModule` (oder AudioModule) | FACT E2 |
| mobile20 Binder | explizit **nicht** binden (`!packageName.contains("mobile20")`) | FACT E2 SecurityServiceManager |
| Schnittstelle | AIDL `ICarSecurityService`: create/release/loadAppCert/signChallenge | FACT E2 |
| JNI | Story: native Lib mit OpenSSL-Symbolen; Fehlertexte „native function signChallenge“ in Tests | FACT E1+E4 |
| Native Lib Dateiname | **UNKNOWN** in diesem Audit (nicht aus APK extrahiert) | UNKNOWN |
| Zertifikat-Herkunft | loadAppCert aus Service/Module; App-Assets für APP; Merge | FACT E2 |
| Signatur Ort | native in OEM; Java-Rekonstruktion in Kit für PKCS12-Pfad | FACT |

AAIdrive FAQ: Connected Classic liefert Security-Modul; neues Connected exportiert nicht — Classic parallel installierbar (auch andere Marke).

---

## 13. AAIdrive Code Trace

```text
App start / Main
  → SecurityServiceThread / CarConnectionDebugging
       SecurityAccess.connect() → discover KnownSecurityServices
       → SecurityServiceManager.bindService OR SecurityModuleManager
  → IDriveConnectionListener / ATTACHED extras (host, port, brand)
  → CarAppService subclasses start when connected + securityAccess.isConnected()
       → MusicApp / CalendarApp / …
            IDriveConnection.getEtchConnection(127.0.0.1, port, …)
            getAppCertificate(brand)
            sas_certificate → signChallenge → sas_login
            rhmi_create / setResource / …
  parallel: CarProber scans 4004–4008, merge certs, same SAS, rhmi_getCapabilities
```

| Schritt | Datei | Klasse/Methode |
|---------|-------|----------------|
| Security connect | `SecurityServiceThread.kt` | `securityAccess.connect()` |
| Service enum | KitAndroid `KnownSecurityServices.kt` | packages/intents |
| Sign | KitAndroid `SecurityAccess.signChallenge` | Binder/Module |
| Cert merge | KitAndroid `CertMangling.mergeBMWCert` | CarProber |
| Etch | Kit `IDriveConnection.getEtchConnection` | TCP |
| SAS | z.B. `MusicApp.kt` init | sas_* |
| Probe | `CarProber.kt` | probeCar |
| USB ready UI | `UsbStatus.kt` / `ConnectionStatusModel` | Accessory≠SAS |

Fehler: Exceptions beim Probe → Analytics; leere Challenge → IllegalArgumentException; fehlendes Security → App startet Etch-Auth nicht (`CarAppService` wartet auf `securityAccess.isConnected()`).

---

## 14. Fake-Car / Test Implementations

| Impl | Auth-Verhalten | Class |
|------|----------------|-------|
| Story Fake-Car | Etch Server stubs; Intent spoof; Auth-Challenges der echten Apps beobachten | FACT E1 Narrative |
| `MockBMWRemotingServer` (AAIdrive tests) | `sas_certificate` → `ByteArray(16)`; `sas_login` no-op | FACT E2 — **keine Prüfung** |
| Simulator `BMWRemotingServerImpl` | „ignore the cert, we'll be wide open“; returns 16 zero/empty challenge; login ignored | FACT E2 |
| Unit tests | mock `signChallenge` → `ByteArray(512)` | FACT E2 — Happy Path only |

**Schluss:** Fake-HU erzeugt den Eindruck einer vollständigen Spec, prüft aber **weder** Cert noch Signatur. Happy-Path-Code ≠ kryptographische Spezifikation der echten HU.

---

## 15. Negative Tests

| Fall | Evidenz | Typ |
|------|---------|-----|
| Invalid / empty challenge (Phone sign) | TestSecurityAccess: erwartet Exception | E4 Code-Test (Phone) |
| Wrong brand cert am HU | CarProber try bmw/mini/j29; fail → next | E2 Verhaltenscode; Feld-Capture fehlt |
| Modified RHMI layout | Story: reject | E1 Experiment Narrative |
| Unknown resource hash | Doc verifyResource | E1 |
| No SAS login | IDL SecurityException auf späteren Calls vermutet | HYPOTHESIS; kein E4 HU-Test in Repo |
| Invalid certificate wire | **UNKNOWN** (kein öffentlicher Negativ-Capture) | UNKNOWN |
| Wrong signature wire | **UNKNOWN** Capture; IDL throws SecurityException | INFERENCE |
| Certificate not whitelisted | Make/J29 / coding ENTWICKLER_MENUE | E1 Doc |

---

## 16. Replay / Session Behaviour

| Frage | Befund | Class |
|-------|--------|-------|
| Alte Response wiederverwenden? | **UNKNOWN** HU-seitig | UNKNOWN |
| Challenge session-specific? | Erwartbar ja; nicht wire-belegt | HYPOTHESIS |
| Reconnect neu auth? | Jede neue Etch-Connection: erneut sas_* in App-Code | FACT E2 App; HU-Pflicht UNKNOWN |
| Auth gecacht? | Phone cached `bmwCerts` in SecurityAccess; Session-Login nicht | FACT E2 / INFERENCE |
| Session lifetime | CarProber keepalive `ver_getVersion` 5s; fail → reset | FACT E2 |
| Session IDs | BCL instanceId; ATTACHED EXTRA_INSTANCE_ID; Etch handle ints | FACT E2 — Bindung an SAS **UNKNOWN** |
| USB/BT disconnect | DETACHED Intent → Apps stoppen | FACT E1+E2 |
| HU reboot | **UNKNOWN** ohne Feld | UNKNOWN |

---

## 17. USB vs Bluetooth

```text
USB AOA bulk ──┐
               ├── BCL ── Etch ── SAS   ? 
BT SPP ────────┘
```

| Claim | Class | Hinweis |
|-------|-------|---------|
| BCL Framing identisch über Streams | INFERENCE | BclClientTransport stream-agnostisch |
| BT SPP BCL implementiert | FACT E2 | BclCarLink BtConnection |
| USB Accessory BCL dokumentiert | FACT Doc E1 | protocol-bcl / app-behavior |
| USB BCL in BclCarLink Code | **REJECTED** als Impl | nur BT verdrahtet |
| SAS/Etch oberhalb Transport identisch | INFERENCE | gleiche Etch-API; kein USB-SAS-Capture |
| AOA Audio ≠ Apps Tunnel | FACT | AOAv2 Audio deprecated; Story/FAQ |

Für Feld: USB und BT können **getrennt** den Tunnel zeigen; SAS-Bytes sitzen in Etch in BCL DATA dest 0x0FA4 — sichtbar nur wenn Payload mitgeschnitten wird.

---

## 18. Evidence Matrix (Auszug)

| ID | Claim | Class | E | external/our |
|----|-------|-------|---|--------------|
| EVID-SAS-001 | IDL sas_certificate/login existieren | FACT | E2 | external |
| EVID-SAS-002 | AAIdrive ruft Cert→Sign→Login | FACT | E2 | external |
| EVID-SAS-003 | Challenge observed 16 B | INFERENCE | E1+E2+E4 | external |
| EVID-SAS-004 | MD5withRSA + optional XOR | FACT | E1+E2 | external |
| EVID-SAS-005 | APP/APP_AUTH + Digests in P7B | FACT | E1 | external |
| EVID-SAS-006 | Simulator prüft Auth nicht | FACT | E2 | external |
| EVID-SAS-007 | SecurityService Packages/AIDL | FACT | E2 | external |
| EVID-SAS-008 | BCL≠SAS | FACT | E2 | external+our |
| EVID-SAS-009 | Eigenes USB-SAS Capture | UNKNOWN | — | our **fehlt** |
| EVID-AOA-030 | AOA Enum 0x18D1:0x2D00 Feld | MEASURED | E3 | our (≠SAS) |

Vollständige IDs: [`evidence.md`](evidence.md).

---

## 19. G1–G4 Mapping

**Gate-Definition dieses Audits** (nicht identisch mit C1b-PLAN-G1–G4):

| Gate | Bedeutung |
|------|-----------|
| G1 | USB Identity / Enumeration / HU reaction |
| G2 | Transport / AOA / BCL / Etch framing |
| G3 | SAS Authentication |
| G4 | Authorized Connected-App functionality (RHMI/AV/CDS) |

| Gate | Externe Evidenz | Eigene Evidenz | Status | Lücke |
|------|-----------------|----------------|--------|-------|
| G1 | AOSP AOA; AAIdrive UsbStatus BMW manufacturer | hu-probe `aoa_observe` Enum `0x18D1:0x2D00`; 51/52/53=0 Already-Accessory; Analyzer MSC `303A:1001` | **partial MEASURED** | Phone-like Identity / Control-Path B1 |
| G2 | BclCarLink+Dissector+Doc; Etch DEADBEEF | C1a BclFramer Lab; **kein** BCL-on-USB Wire | **Desk stark / Field schwach** | USB Bulk BCL Capture |
| G3 | IDL+AAIdrive+Auth Doc+SecurityAccess+Tests | **keine** | **Desk FACT / Field absent** | Session Capture mit sas_* oder Log-Korrelation |
| G4 | RHMI/AV/CDS Code+Docs; Digests Doc | **keine** Connected-Session am F20 | **Desk FACT / Field absent** | Music/RHMI Session nach Auth |

**Explizit:** AOA/BCL evidence ≠ SAS authentication evidence.

---

## 20. What our ESP32 can observe

### Aktuell direkt messbar (hu-probe / usb-analyzer Rolle)

- USB enumeration (VID/PID, configs, interfaces)
- Selected control transfers (Vendor-Tap Limits beachten)
- Bulk endpoint activity / reconnects / timing
- BCL framing **wenn** Bulk-Bytes zum Framer gelangen
- Etch magic `DEADBEEF` **wenn** Payload sichtbar
- Session timing correlierbar mit Phone-Logs

### Nicht direkt messbar

- USB PHY PID/DATA0/1/CRC/ACK/NAK
- D+/D− Wellenform
- Traffic, den TinyUSB/Callback nicht exposed
- Inhalt signierter Challenges **als kryptographische Verifikation** ohne Etch-Decode
- Private Keys / JNI inside Phone

### Mit Phone + AAIdrive zusätzlich

- ATTACHED lifecycle, Security connected flags (Logcat)
- TCP localhost Etch (tcpdump auf Phone — nicht ESP32)
- RHMI traffic in BCL DATA (wenn USB-Tunnel captured)
- Reconnect behavior

---

## 21. What remains invisible

- HU Challenge-CSPRNG
- HU Verifier Exact Code (nur Symbolname Doc)
- Native `.so` Exact Crypto ohne APK-RE in diesem Lauf
- Ob USB und BT byte-identische SAS-Sessions haben
- Replay-Fenster / Challenge-TTL
- Vollständige Negativmatrix am echten NBT Evo
- Live Cockpit: Protocol deprecated (Story) — außerhalb F20/NBT Ziel

---

## 22. BMW Field Experiment

### Ziel-Setup

BMW F20 / NBT Evo + Android + MyBMW/Connected (+ Classic falls Security) + AAIdrive + ESP32 Analyzer/hu-probe (USB observe; parallel optional BT).

### Run-Sheet

| Test-ID | Setup | Aktion | Erwartete Beobachtung | Capture-Daten | Erfolgskriterium | Interpretation | Fehlinterpretation |
|---------|-------|--------|----------------------|---------------|------------------|----------------|--------------------|
| FX-G1-01 | Probe alone | Plug USB | Enum / UI reaction | descriptors, timing | G1 baseline | HU sieht Device | „Connected works“ |
| FX-G1-02 | Phone only | Plug Phone | Accessory/MSC modes | VID/PID, AOA strings if any | Phone identity documented | Contrast to probe | AOA⇒SAS |
| FX-G2-01 | Phone+Connected | Connect Apps | BCL-like bulk / BT SPP | BCL headers, dest 0x0FA4 | Tunnel framing seen | G2 progress | Tunnel⇒Auth OK |
| FX-G2-02 | +AAIdrive | Start AAIdrive | ATTACHED, TCP :400x | Logcat host/port; bulk timing | Etch connect attempt | G2+app | UI alone≠SAS |
| FX-G3-01 | Full stack | First app login | sas_certificate / challenge / sas_login in Etch | Etch decode or AAIdrive logs + correl. bulk | **Challenge+Login visible once** | **G3 Field-Fact** | Simulator logs |
| FX-G3-02 | Full stack | Disconnect/reconnect | New challenge? | two session captures | challenge differs | session binding | cached login |
| FX-G3-03 | Full stack | Kill Security / no Classic | Auth fail | exceptions in log | fail closed | Security dependency | transport fail |
| FX-G4-01 | After G3 | Music browse/play | RHMI/AV calls | Etch rhmi_/av_ | UI+AV after login | G4 | Auth assumed |
| FX-G4-02 | After G3 | Play/Pause/Next | AV events | av_* + timing | controls work | G4 media | BT A2DP≠RHMI |
| FX-G4-03 | Optional | Modified assets (lab only) | resource reject | exception | Digests enforced | Authz≠Auth | car bug |

**Minimale Messung, die G3 erstmals als Field-Fact belegt:**  
FX-G3-01 — in **einer** realen F20-Session entweder (a) Etch-dissektierter Trace mit `sas_certificate` / challenge / `sas_login`, oder (b) synchron AAIdrive/Security-Log mit Challenge-Länge + erfolgreichem `sas_login` **und** korreliertem BCL/Etch-Traffic auf dem Analyzer.

---

## 23. Open Questions

1. Exakte Challenge-Entropie / RNG der NBT Evo HU?
2. Challenge immer 16 B auf allen HU-Generationen?
3. Response immer 512 B oder key-size-abhängig am Wire?
4. USB-Bulk BCL Byte-identisch zu BT?
5. `sas_crl` / `sas_permission` / `sas_logout` Feldnutzung?
6. Replay einer Response in neuer Session?
7. MyBMW-only (ohne Classic) Signaturpfad am Testphone stabil?
8. Native library filename + OpenSSL API surface?

---

## 24. Final Assessment

### FACT

- SAS existiert als Etch-API `sas_certificate` / `sas_login` (+ crl/permission/logout in IDL).
- AAIdrive und Addons implementieren Cert → Challenge → signChallenge → Login.
- Phone SecurityService/Module signiert; HU liefert Challenge und prüft (Doc + Architektur).
- P7B mit APP / APP_AUTH; Digests whitelisten RHMI-Ressourcen.
- Crypto der Phone-Rekonstruktion: MD5withRSA, optional XOR mit MD5(2).
- Simulator/Mocks prüfen Auth nicht.
- BCL ist Transport; SAS ist Etch darüber.
- Eigenes Feld: AOA Enum ja; SAS nein.

### INFERENCE

- Challenge typisch 16 B; Connected-Response typisch 512 B.
- USB und BT teilen SAS/Etch oberhalb BCL.
- Feature-Flags im Cert steuern Authorization nach Login.

### HYPOTHESIS

- Challenge ist pro Session frisch und replay-resistent.
- Ohne SAS schlagen alle RHMI/AV/CDS Calls fehl.

### UNKNOWN

- HU-Verifier- und RNG-Details; USB-Wire-SAS; Challenge-TTL; Negativmatrix am NBT Evo.

### REJECTED

- AOA funktioniert ⇒ Connected/SAS funktioniert.
- BCL funktioniert ⇒ SAS erfolgreich.
- Etch TCP offen ⇒ App authentifiziert.
- AAIdrive UI / Simulator ⇒ Zertifikat kryptographisch geprüft.
- hu-probe ASCII-`12345678` ≡ BCL Session-Init (prior; hex4 belegt).
- BclCarLink implementiert USB BCL.

---

## Sieben Leitfragen

1. **Existiert SAS Authentication tatsächlich?**  
   **Ja (Desk-FACT, E1+E2).** Feld-FACT am F20 noch ausstehend.

2. **Challenge/Response-Sequenz?**  
   App→HU `sas_certificate(p7b)` → HU→App `byte[] challenge` → Phone `signChallenge` → App→HU `sas_login(response)`.

3. **Rolle des BMW-Zertifikats?**  
   Identitäts- und Autorisierungscontainer (APP + APP_AUTH); Public Key für Verify; Digests/Make/Feature-Flags.

4. **Wer erzeugt / prüft die kryptographische Antwort?**  
   Erzeugt: Phone Security (Binder/JNI/Module). Prüft: HU CarEtchServer.

5. **Authentication vs Authorization?**  
   Auth = Cert+Challenge/Response. Authz = Cert-Permissions + Resource-SHA256 bei RHMI Upload.

6. **Was sieht der ESP32-Analyzer?**  
   USB/BCL/Etch-Framing und Timing — **nicht** die Phone-JNI-Signatur selbst; SAS-Payload nur bei Payload-Capture+Decode.

7. **Welche Messung belegt G3 als Feld-Fact?**  
   FX-G3-01: echte Session mit sichtbarer Cert/Challenge/Login-Sequenz (Etch-Trace oder korrelierte Logs+Tunnel).

---

## Quellen-Kurzverweise (wichtigste)

| Claim | URL / Repo | Datei | Zeilen/Stelle |
|-------|------------|-------|---------------|
| IDL sas_* | IDriveConnectKit@95492b0 | `BMWRemoting.etch` | 132–136 |
| Auth Doc + Mermaid | BMWConnectedAnalysis@9e96ac6 | `docs/authentication.md` | gesamtes Doc |
| Crypto | KitAndroid@4a567bc | `PrivateKeyHandling.kt` | `signChallenge` |
| Security packages | KitAndroid | `KnownSecurityServices.kt` | enum |
| AIDL | KitAndroid / Analysis | `ICarSecurityService.aidl` | — |
| Music SAS | AAIdrive@3e93419 | `MusicApp.kt` | init ~64–68 |
| Probe SAS | AAIdrive | `CarProber.kt` | `probeCar` |
| Fake open | Simulator | `BMWRemotingServerImpl.kt` | 41–47 |
| Story RE | hufman.github.io/stories/bmwconnectedapps | — | — |
| Prior BCL | technology-audit | `bmw-bcl-handshake.md` | — |
