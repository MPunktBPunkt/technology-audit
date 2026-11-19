# SecurityAccess + CertMangling Deep Dive

Pins: KitAndroid `@4a567bc` · Analysis `@9e96ac6` · AAIdrive `@cc81d8e` · BclCarLink `@7cfd959`.

## 1. End-to-End Call-Graph (AAIdrive / Kit)

```text
SecurityAccess.connect()
  ├─ discover() → PackageManager.getPackageInfo(KnownSecurityServices.*)
  ├─ SecurityServiceManager.connect()   // Classic Binder (skip mobile20)
  └─ SecurityModuleManager.connect()    // MyBMW: createPackageContext + reflect SecurityModule

CarAppAssetResources.getAppCertificate(brand)
  └─ CertMangling.mergeBMWCert(appCert, SecurityAccess.fetchBMWCerts(brandHint))

IDriveConnection.getEtchConnection(...)   // already on BCL tunnel / localhost proxy
carConnection.sas_certificate(mergedP7b)  // Etch → HU
  ← challenge: ByteArray                 // expected 16 B
securityAccess.signChallenge(challenge)
  └─ OEM ICarSecurityService.signChallenge(handle, challenge)
carConnection.sas_login(response)
  → RHMI / AM / CDS …
```

Belegte Consumer: `MusicApp.kt` (getAppCertificate → sas_certificate → signChallenge → sas_login);
`CarProber.kt` (explizites mergeBMWCert); `CarAppAssetResources.kt` (merge in getAppCertificate).

## 2. SecurityAccess.signChallenge (FACT)

Quelle: `security/SecurityAccess.kt`.

| Schritt | Verhalten |
|---------|-----------|
| Input | `challenge: ByteArray` — Kommentar: **16 bytes**; `appName` optional/egal |
| Connection | erst `connectedSecurityServices.values.firstOrNull()`, sonst `securityModuleManager.getConnection()` |
| Context | `createSecurityContext(packageName, appName)` — default `context.packageName` |
| Sign | `connection.signChallenge(handle, challenge)` |
| Cleanup | `releaseSecurityContext(handle)` |
| Errors | leere Response / SecurityException / JNI → `IllegalArgumentException("Invalid challenge")` |

**INFERENCE:** Ohne installierte + erreichbare OEM-Security-Quelle schlägt Auth fehl — unabhängig von BCL-Erfolg.

## 3. Zwei OEM-Anbindungen

### A) Classic Binder — `SecurityServiceManager`

| Feld | Wert |
|------|------|
| Intent action | `KnownSecurityServices.className` (z. B. `com.bmwgroup.connected.bmw.SECURITY_SERVICE`) |
| `setPackage` | `packageName` |
| Bind | `bindService(..., BIND_AUTO_CREATE)` |
| Proxy | `ICarSecurityService.Stub.asInterface` |
| Skip | Packages mit `mobile20` — **kein** Binder-Versuch |

AIDL (`ICarSecurityService.aidl`):  
`createSecurityContext` · `releaseSecurityContext` · `loadAppCert` · `signChallenge`.

### B) MyBMW / Mobile20 Module — `SecurityModuleManager`

| Feld | Wert |
|------|------|
| Zugang | `createPackageContext(pkg, IGNORE_SECURITY \| INCLUDE_CODE)` |
| Klassen | `com.bmwgroup.connected.core.security.SecurityModule` (Fallback `…audio.AudioModule`) |
| Init | `proxy.init("bmw")` |
| API | Reflection auf create/getCertificates/signChallenge/destroy/deInit |

BclCarLink README FACT: AAIdrive braucht MyBMW / Mini / SupraConnect **für das Security Module**.

## 4. KnownSecurityServices (Package-Katalog)

| Enum | Package | Service class |
|------|---------|---------------|
| BMWClassicUSA | `com.bmwgroup.connected.bmw.usa` | `…SECURITY_SERVICE` |
| MiniClassicUSA | `com.bmwgroup.connected.mini.usa` | idem |
| BMWClassic | `com.bmwgroup.connected.bmw` | idem |
| MiniClassic | `com.bmwgroup.connected.mini` | idem |
| BMWConnectedNA | `de.bmw.connected.na` | idem |
| MiniConnectedNA | `de.mini.connected.na` | idem |
| BMWConnected | `de.bmw.connected` | idem |
| MiniConnected | `de.mini.connected` | idem |
| BMWMine | `de.bmw.connected.mobile20.row` | `com.bmwgroup.connected.core.services.security.CarSecurityService` |
| MiniMine | `de.mini.connected.mobile20.row` | idem |
| J29Mine | `de.j29.connected.mobile20.row` | idem |
| + CN/HK/KR/NA Varianten | `…mobile20.cn/hm/kr/na` | idem |

Analysis Doc: ab Connected 5.1 / MyBMW exportiert der Binder oft **nicht** mehr → Module-Pfad.

## 5. CertMangling.mergeBMWCert (FACT)

Quelle: `security/CertMangling.kt`.

```text
appCert (APP p7b from 3rd-party app)
  filter: drop CN == "a4a_root-ca"
bmwCert (from fetchBMWCerts / loadAppCert of OEM)
  keep: CN contains "connection" (case-insensitive)   ← APP_AUTH / connection leaf
merge into new PKCS#7 PEM (preserve CRLs from appCert CMS)
```

Instrumented Test erwartet u. a. CN  
`a4a_app_BMWTouchCommand_Connection_00.00.10` im Bundle — **gleicher CN** wie Feld-Deep-Forensic APP_AUTH-Blatt.

## 6. PrivateKeyHandling (Desk Crypto — nicht Produktionspfad)

| Claim | Status |
|-------|--------|
| XOR: `challenge ⊕ MD5(LE u32=2)` dann `MD5withRSA` wenn `applyXor=true` (APP_AUTH) | FACT (Code + Test) |
| Legacy ohne CertificateType: Signatur über raw challenge | FACT (Doc + Code) |
| Dev-P12 Test-Response **192 B** | FACT (Unit test) |
| Classic instrumented `signChallenge` → **512 B**, first byte `0x15` | FACT (E4) |
| AAIdrive Runtime nutzt diesen Helper für echte HU-Login | **REJECTED** — Runtime geht über OEM `signChallenge` |

Dieser Helper erklärt die **Algorithmus-Form**; er liefert **keine** Produktions-Credentials.

## 7. fetchBMWCerts

Lädt über OEM `loadAppCert(handle)` das Connection-/APP_AUTH-Bundle, cached in `SecurityAccess.bmwCerts`.  
Dient als Input für CertMangling — nicht als Challenge-Response.

## 8. Was BclCarLink **nicht** macht

BclCarLink: USB/BT serial → BCL (INIT/HS/SelectProto/KNOCK/DATA/WD).  
Kein `sas_*`, kein CertMangling. README verweist explizit auf OEM Security Module für AAIdrive.
