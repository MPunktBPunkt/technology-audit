# SIGNCHALLENGE-CALLCHAIN

## Visualisierung (aktuell belegt)

```text
Caller (AAIdrive MusicApp / CarProber / …)
  ↓
SecurityAccess.signChallenge(appName, challenge)     FACT — KitAndroid
  ↓
┌─────────────────────────────────────────────────────┐
│ Classic path                                         │
│   SecurityServiceManager                             │
│     Intent(className).setPackage(packageName)        │
│     bindService → ICarSecurityService                │
│       createSecurityContext(pkg, appName)            │
│       signChallenge(handle, challenge)  → byte[512]  │
│       releaseSecurityContext(handle)                 │
└─────────────────────────────────────────────────────┘
  OR
┌─────────────────────────────────────────────────────┐
│ MyBMW path                                           │
│   SecurityModuleManager                              │
│     createPackageContext(mybmwPkg, INCLUDE_CODE)     │
│     reflect SecurityModule / AudioModule             │
│       init("bmw")                                    │
│       createSecurityContext(pkg, appName) → int      │
│       signChallenge(handle, challenge) → byte[]      │
│       getCertificates(handle) → p7b                  │
│       destroySecurityContext / deInit                │
└─────────────────────────────────────────────────────┘
  ↓
??? OEM inner implementation                           UNKNOWN — needs APK
  ↓  (Hypothesis D: JNI → .so; not CONFIRMED)
512 B signature
  ↓
carConnection.sas_login(response)
```

## Stufen-Tabelle

### Stufe 1 — Consumer

| Feld | Wert |
|------|------|
| APK | AAIdrive (open source) — nicht MyBMW |
| Class | z. B. `me.hufman.androidautoidrive.carapp.music.MusicApp` |
| Method | auth sequence: `sas_certificate` → `securityAccess.signChallenge` → `sas_login` |
| Descriptor | n/a (Kotlin) |
| Evidence | AAIdrive `MusicApp.kt` @`cc81d8e` — **FACT** |

### Stufe 2 — Kit SecurityAccess

| Feld | Wert |
|------|------|
| APK | IDriveConnectKitAndroid library |
| Class | `io.bimmergestalt.idriveconnectkit.android.security.SecurityAccess` |
| Method | `signChallenge(appName: String, challenge: ByteArray): ByteArray` |
| Descriptor | takes 16-B challenge (comment); returns OEM response |
| Evidence | `SecurityAccess.kt` @`4a567bc` — **FACT** |

### Stufe 3a — Classic Binder

| Feld | Wert |
|------|------|
| APK | OEM Connected Classic (**not present this run**) |
| Class / Action | `…SECURITY_SERVICE` (enum `KnownSecurityServices`) |
| Method | AIDL `signChallenge(long, byte[])` |
| Descriptor | `ICarSecurityService.aidl` |
| Evidence | Kit bind + AIDL — **FACT** (interface). Inner body **UNKNOWN** ohne Classic APK |

### Stufe 3b — MyBMW SecurityModule (external surface only)

| Feld | Wert |
|------|------|
| APK | MyBMW (**not present**) |
| Class | `com.bmwgroup.connected.core.security.SecurityModule` (or AudioModule) |
| Method | reflected: `(String,String)->Int` create; `(Int,byte[])->byte[]` sign; `(Int)->byte[]` certs |
| Descriptor | **kein** Smali/`native` Keyword hier — nur Reflect-Filter in Kit |
| Evidence | `SecurityModuleManager.kt` — **FACT** that Kit *expects* these method shapes. **NOT** FACT that methods are `native` |

### Stufe 4 — JNI / native

| Feld | Wert |
|------|------|
| APK | — |
| Class / Method | — |
| Evidence | Analysis Doc „JNI/NDK library“; Test message `native function signChallenge` |
| Klassifikation | **STRONG INFERENCE** — **not** JNI FACT (no `native` declaration / `RegisterNatives` / `JNI_OnLoad` from OEM binary) |

## Certificate entry (Pipeline, not re-audited)

```text
getAppCertificate / mergeBMWCert(app, fetchBMWCerts)
  → sas_certificate(mergedP7b)     ← cert NOT passed into signChallenge()
  ← challenge[16]
signChallenge(challenge)           ← only challenge (+ context handle from createSecurityContext)
```

| Frage | Antwort | Klassifikation |
|-------|---------|----------------|
| Cert an `signChallenge()` übergeben? | Nein — nur Challenge (+ zuvor Context) | FACT (Kit) |
| Cert vorher verarbeitet? | Ja — merge vor `sas_certificate` | FACT |
| SecurityModule lädt Cert? | `loadAppCert` / `getCertificates` für APP_AUTH bundle | FACT (Kit surface) |
| Package/Cert Bindung | `createSecurityContext(packageName, …)`; Analysis: package must be valid for client | FACT Doc + Kit |

## STOP-Grenze

Keine OEM-APK → keine Bestätigung von `native` keyword / `.so` Bindung.  
Hypothese D **nicht** zu CONFIRMED hochstufen.
