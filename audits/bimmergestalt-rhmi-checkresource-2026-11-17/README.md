# Audit Campaign: bimmergestalt-rhmi-checkresource-2026-11-17

```yaml
id: bimmergestalt-rhmi-checkresource-2026-11-17
project_id: bimmergestalt-idrive-refs
started: 2026-11-17
ended: 2026-11-17
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commits:
  IDriveConnectKit: "95492b0"
  AAIdrive: "3e93419"
  IDriveConnectAddons: "270032d"
  BMWConnectedAnalysis: "9e96ac6"
  BclCarLink: "7cfd959"
upstream_org: BimmerGestalt
related:
  - audits/bimmergestalt-idrive-2026-foreign/
  - audits/esp32-bt-analyzer-f20-connected-2026-11-17/
reuse_outcomes:
  reused:
    - bmw-rhmi
    - bmw-etch-rpc
    - bmw-sas-auth
    - bmw-bcl
  new: []
  not_helped:
    - "HU verifyResource binary internals beyond public docs"
    - "F20 digest whitelist contents (not in public sources)"
  process: "Desk External Knowledge; pin-cited Code/Doc FACTS; no new RE; no Attack-How-tos."
```

## Ziel

Offene Fragen **nach erfolgreichem `rhmi_checkResource`** aus öffentlichen
BimmerGestalt-Quellen beantworten und den Client-seitigen Resource-/Lifecycle-Pfad
absichern — als Grundlage für Experimentplan W0–W5.

## Scope

- Im Scope: IDL-Signaturen, `rhmi_setResourceCached`, App-Lifecycle (Music /
  Notification / Readout/CarInfo / ScreenMirror), Whitelist-/verifyResource-Doku,
  Watchdog-Client-Modell, Image-Transport.
- Nicht im Scope: neues Reverse-Engineering der HU-Firmware; Bypass-Anleitungen;
  eigene Feldmessungen (→ Audit B).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Exakte Signaturen `checkResource` / `setResource` / `initialize` | erfüllt |
| 2 | Sequenz nach `checkResource(true)` aus Code | erfüllt |
| 3 | Resource-Typen-Tabelle pro App | erfüllt |
| 4 | Whitelist / `verifyResource` / p7b Digests dokumentiert | erfüllt |
| 5 | ScreenMirror Image-Pfad + Action-Korrelation | erfüllt |
| 6 | Offene Restfragen markiert | erfüllt |

---

## Executive Summary

Nach `rhmi_checkResource(result=true)` sendet ein AAIdrive-/Kit-Client **keine**
weitere Resource-Payload für diesen Typ — `rhmi_setResourceCached` überspringt
`setResource` und geht zur nächsten Resource bzw. zu `rhmi_initialize`. Cache-Miss
(`false`) → `rhmi_setResource(handle, data, type)`. Die HU-seitige
SHA-256-Whitelist (`SAS.Digests.*` im APP-Zertifikat, Enforce in
`libhmiremoting.so` / `CRHMIAuthPermHandler::verifyResource`) bleibt der zentrale
Autorisierungsblocker und ist in den öffentlichen Quellen **dokumentiert, aber
nicht als F20-Digest-Liste messbar**.

---

## 1. IDriveConnectKit — IDL & Helpers

### 1.1 Signaturen (`BMWRemoting.etch`, Pin `95492b0`)

| Call | Signatur | Zeilen |
|------|----------|--------|
| create | `int rhmi_create(string token, RHMIMetaData metaData)` | 178 |
| initialize | `void rhmi_initialize(int handle)` | 180 |
| checkResource | `boolean rhmi_checkResource(byte[] hash, int handle, int size, string name, RHMIResourceType type)` | 188 |
| setResource | `void rhmi_setResource(int handle, byte[] data, RHMIResourceType type)` | 189 |
| setData | `void rhmi_setData(int handle, int modelId, object value)` | 207 |
| setProperty | `void rhmi_setProperty(int handle, int componentId, int propertyId, Map values)` | 208 |
| AM handler | `void am_addAppEventHandler(int handle, string ident)` | 160 |

Kommentar IDL Z.187: **„the hash is MD5 of the zip file“** — gilt für den
Cache-Check (`checkResource`), **nicht** für die Cert-Whitelist (SHA-256, s. §4).

### 1.2 `RHMIResourceType` (Enum, Z.72–85)

`DESCRIPTION`, `TEXTDB`, `IMAGEDB`, `TEXTID`, `IMAGEID`, `PREINSTTEXTID`,
`PREINSTIMAGEID`, `IMAGEDATA`, `IBADB`, `FLOATDATA`, `WIDGETDB`, `ASSETDB`.

Für Resource-**Upload** relevant: `DESCRIPTION` / `TEXTDB` / `IMAGEDB` /
`WIDGETDB`. Laufzeit-Bilder nutzen `IMAGEDATA` über `RHMIResourceData` in
`setData` (nicht `setResource`).

### 1.3 `rhmi_setResourceCached` — exakte Parameterreihenfolge

Quelle: `IDriveConnectKit/.../RHMIUtils.kt` L14–21 (`95492b0`):

```kotlin
fun BMWRemotingServer.rhmi_setResourceCached(handle: Int, type: RHMIResourceType, data: ByteArray?): Boolean {
    data ?: return false
    val hash = md5sum(data)                          // MD5 of bytes
    val cached = rhmi_checkResource(hash, handle, data.size, "", type)
    //                          ↑hash  ↑handle ↑size   ↑name="" ↑type
    if (!cached) {
        rhmi_setResource(handle, data, type)
        //               ↑handle ↑bytes ↑type   — kein hash/size/name
    }
    return cached
}
```

**Antwort auf „welche Parameter erwartet setResource?“:** nur
`(handle, data, type)`. Hash/Size/Name gehören ausschließlich zu `checkResource`.

---

## 2. Lifecycle-Sequenz (Client, belegbar)

```text
1  rhmi_create(token=null, RHMIMetaData{id, VersionInfo, name, vendor}) → handle
2  für jeden geplanten Resource-Typ:
     a  MD5(bytes) berechnen
     b  rhmi_checkResource(hash, handle, size, name="", type) → bool
     c  wenn false: rhmi_setResource(handle, bytes, type)
     d  wenn true:  skip setResource (Cache-Hit)
3  rhmi_initialize(handle)
4  rhmi_addActionEventHandler(handle, ident, actionId=-1)
5  rhmi_addHmiEventHandler(handle, ident, componentId=-1, eventId=-1)
6  Laufzeit: rhmi_setData / rhmi_setProperty
7  HU→Phone: rhmi_onActionEvent / rhmi_onHmiEvent → rhmi_ackActionEvent(...)
```

**Nach `checkResource(true)`:** Schritt 2c entfällt für diesen Typ; Client fährt
mit nächstem Typ oder direkt mit `initialize` fort. Es gibt **keinen** weiteren
„Commit“-Call außer `initialize`.

---

## 3. AAIdrive / Addons — Resource-Typen pro App

| App | Asset-Bundle | DESCRIPTION | TEXTDB | IMAGEDB | WIDGETDB | „sneaky“ | initialize | Beleg |
|-----|--------------|:-----------:|:------:|:-------:|:--------:|----------|------------|-------|
| **Music** | `multimedia` / `spotify` | ✅ | ✅ | ✅ | — | nein | nach 3× setResourceCached | `MusicApp.kt` 163–171 |
| **Notification** | `basecoreOnlineServices` | ✅ | ✅ | ✅ | — | nein | nach 3× | `NotificationApp.kt` 201–209 |
| **ID5 Statusbar** | `bmwone` (+ unsigned) | ✅ | optional unsigned | ✅ | ✅ | TEXTDB weggelassen wenn nicht `SEND_UNSIGNED_RESOURCES` | nach Resources | `ID5StatusbarApp.kt` 45–59 |
| **CarInfo / Readout-ID** | `news` (+ `carinfo_unsigned`) | ✅ | optional unsigned | optional unsigned | — | TEXTDB+IMAGEDB weggelassen („no icons or text, so sneaky“) | nach DESCRIPTION (± unsigned) | `CarInfoApp.kt` 110–126 |
| **Map** | `smartthings` | ✅ | auskommentiert | ✅ | — | TEXTDB bewusst aus | nach DESC+IMAGEDB | `MapApp.kt` 63–66 |
| **ScreenMirror** | Addon assets | ✅ | auskommentiert | ✅ | — | TEXTDB bewusst aus | nach DESC+IMAGEDB | `screen_mirror/.../CarApp.kt` 89–97 |

Alle genannten Apps nutzen **`rhmi_setResourceCached`**, nicht bare `setResource`.

### App-Unterschiede (kurz)

- **Music / Notification:** volle signed Packs (DESC+TEXT+IMAGE).
- **Sneaky-Pattern:** nur DESCRIPTION (ggf. + signed IMAGEDB/WIDGETDB), Labels/Icons
  fehlen → leerer Menüeintrag; vermeidet Whitelist-Rejects für unsignierte DBs
  (`CarInfoApp`, `ID5Statusbar`, ScreenMirror TEXTDB).
- **WIDGETDB:** nur Statusbar-Pfad.
- **Readout:** in AAIdrive als Meta-ID `…notification.readout` im CarInfo-Pfad;
  Feld sieht `am_registerApp` mit Frame-Größe 1874 B (Audit B).

---

## 4. Resource-Whitelist / verifyResource

| Claim | Status | Quelle |
|-------|--------|--------|
| Resource-Packs durch SHA-256 in SAS APP-Cert geschützt | Desk FACT (Doc) | `BMWConnectedAnalysis/docs/rhmi-resources.md`; `authentication.md` |
| Permissions `SAS.Digests.RHMIDescriptions` / `ImageDatabases` / `TextDatabases` = kommagetrennte SHA-256-Listen | Desk FACT (Doc) | `authentication.md` Z.53 |
| Enforce in HU: `CRHMIAuthPermHandler::verifyResource` in `libhmiremoting.so` | Desk FACT (Doc + Community) | `authentication.md` Z.53; AAIdrive Discussion [#801](https://github.com/BimmerGestalt/AAIdrive/discussions/801) |
| Cache-Check (`checkResource`) nutzt **MD5** der Bytes | Desk FACT (IDL+Code) | `BMWRemoting.etch` Z.187; `RHMIUtils.md5sum` |
| Whitelist-Check ≠ Cache-Check (SHA-256 Cert vs MD5 Cache) | Desk FACT | Konvergenz Doc+Code |
| Fehlender/ungültiger Digest → Upload abgelehnt | Desk FACT (Doc); Community: Patch `verifyResource`→1 | #801; PR #804 (`SEND_UNSIGNED_RESOURCES`) |
| Autorisierte Ressource = Digest aus existierendem OEM-`*.p7b` + passende Bytes | Desk FACT (Doc) | `known-apps.md` |
| Konkrete F20-Digest-Liste / Verhalten bei Reject-Code | **OPEN** | nicht in Public Sources |

**Workarounds (nur dokumentiert, nicht empfohlen/implementiert hier):**
1. OEM-autorisierte Resource-Bytes (Digest match) verwenden.
2. HU-seitig `verifyResource` patchen (Community #801) — außerhalb Scope; Security-Grenze.

---

## 5. ScreenMirror — Image-Transport & Actions

Pin `IDriveConnectAddons` `270032d`.

```text
am_create → am_addAppEventHandler(handle, "…screenmirror")
  → am_registerApp(…)
  → rhmi_create → setResourceCached(DESCRIPTION) → setResourceCached(IMAGEDB)
  → rhmi_initialize → addAction/Hmi handlers
  → Focus → ScreenMirrorProvider.start()
       JPEG compress (default quality 60; low-end 30)
       → RaImageModel.value = jpegBytes
       → setData(handle, modelId, RHMIResourceData(IMAGEDATA, bytes))
  ← rhmi_onActionEvent → ackActionEvent(handle, actionId, 1, true)
```

Belege:

- JPEG: `ScreenMirrorProvider.kt` L39, L179 (`jpgQuality`, `Bitmap.CompressFormat.JPEG`)
- `RaImageModel` → `IMAGEDATA`: `RHMIModelLive.kt` L52–59
- Focus→callback→`imageModel.value`: `ImageState.kt` L39–46
- AM + RHMI create: `CarApp.kt` L66–97
- Action ack: `CarApp.kt` L160–169

**Bezug ~216-KiB-Burst:** Client-Muster (JPEG via `setData`/`IMAGEDATA` nach Focus/
Action) korreliert mit Feld-STRONG in Audit B; Quellen allein beweisen den F20-Burst
nicht (Feldmessung nötig).

---

## 6. ServiceException(213) / Image-Modelle

`MockBMWRemotingServer.kt` L84–86 (AAIdrive `3e93419`):

> refuse to set any ImageID model to 0, according to model year 2019 behavior  
> → `throw ServiceException(213, "SetData was not successful.")`

Das ist **Client-Testnachbau** beobachteten HU-Verhaltens (ImageID←0). Cover-/Icon-
Modelle (Lab: u. a. modelId **456**) erwarten gültige `IMAGEID`/`IMAGEDATA`, nicht 0.
Quellen erklären nicht modelId→Semantik der F20-Multimedia-DESCRIPTION (Lab/Feld).

---

## 7. Watchdog (Client-Seite)

| Aspekt | Wert | Quelle | Epistemik |
|--------|------|--------|-----------|
| Port | 5001 | `BclCarLink/.../WatchdogProtocol.kt` L12 | Desk FACT |
| Payload | `13 37 13 37` | L13 | Desk FACT |
| Interval | 5000 ms | L14 | Desk FACT (Desk-Modell) |
| Timeout | 20000 ms | L15 | Desk FACT (Desk-Modell) |
| Proto v4 WD | „unknown watchdog behavior“ → Client hardcodet v3 | `BclClientTransport.kt` L84 | Desk FACT |
| AAIdrive | liest nur `EXTRA_WATCHDOG_RTT` | `BclStatusListener.kt` | Desk FACT |
| Wire-Timing F20 | ≠ festes 5-s-Desk-Modell | → Audit B | FIELD FACT dort |

---

## 8. Konkrete Fragen — Kurzantworten

| Frage | Antwort | Beleg |
|-------|---------|-------|
| Sequenz nach `checkResource(true)`? | Skip `setResource` für diesen Typ; weiter nächster Typ / `initialize` | `RHMIUtils.kt` 17–21 |
| Welche Typen / Reihenfolge realer Client? | Music/Notification: DESC→TEXTDB→IMAGEDB; ScreenMirror: DESC→IMAGEDB; sneaky: oft nur DESC | §3 Tabelle |
| Parameter `setResource`? | `(handle, data, type)` | IDL 189 |
| Wann `initialize`? | Sofort nach allen Resource-Schritten, **vor** Action/Hmi-Handlern | Music/Notification/ScreenMirror |
| modelId 456 / ServiceException(213)? | 213 = ImageID←0 (2019-Verhalten, Mock); 456 = Cover in Lab-Multimedia — Quellen ohne F20-Map | Mock L84–86; Audit B Lab |
| Watchdog Client? | Port 5001, 5 s / 20 s Desk; Wire separat | §7 |
| Whitelist? | SHA-256 in `SAS.Digests.*`; `verifyResource` in `libhmiremoting.so` | §4 |

---

## 9. Offene Restfragen (Quellen reichen nicht)

1. Exakte SHA-256-Digest-Liste der auf dem **F20** akzeptierten Resources.
2. HU-Return-Codes / Exceptions bei Whitelist-Reject vs. Cache-Miss.
3. Ob `checkResource(true)` die Whitelist erneut prüft oder nur Cache.
4. F20-Watchdog-Timeout (HU-seitig) — Desk 20 s ≠ gemessenes Wire-Verhalten.
5. Vollständige modelId-Map der Multimedia-DESCRIPTION am F20.
6. Ob WIDGETDB auf NBT/F20 überhaupt akzeptiert wird.

---

## Decision Trace (C10)

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Cache-Hit skip setResource? | Nach true noch Upload? | `RHMIUtils` | Nein — W2 = checkResource stabil + nur Miss upload |
| Whitelist = Hauptblocker? | Auth-Grenze? | authentication.md + #801 | Ja — P0 Resource-Authorization |
| Sneaky nur DESC? | Unsigned vermeiden? | CarInfo/ScreenMirror | Ja als Desk-Pattern; Feld muss Digests matchen |
| Attack/Patch doku? | verifyResource=1 | #801 | Nur als bekannte Community-Option nennen, nicht ausführen |

## Kill-Kriterien (C12)

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | BG-Desk als F20 FIELD FACT übernommen | `REJECTED` |
| 2 | Bypass-/Patch-How-to in KB | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Audit ohne Messhypothese; Gaps sind Digest-Liste und HU-Timeout.
```

## Knowledge Feedback (C13)

| Desk | Neue Erkenntnis | Zurück in |
|------|-----------------|-----------|
| Sequenz check→set→init | präzisiert | `technologies/bmw-rhmi/SHEET.md` |
| MD5-Cache vs SHA-256-Whitelist | präzisiert | Sheet + Application |
| App Resource-Matrix | neu verdichtet | dieses Audit |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.
