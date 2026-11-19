# SIGNCHALLENGE-CALLCHAIN

## Visualisierung (OEM MyBMW 6.11.3 ROW)

```text
Caller (AAIdrive / Kit consumer)
  ↓
SecurityAccess.signChallenge(appName, challenge)          FACT — Kit
  ↓
SecurityModuleManager (createPackageContext + reflect)
  ↓
SecurityModule.init("bmw")                                FACT — Java → AudioModule.a
SecurityModule.createSecurityContext(pkg, appName) → int  FACT — Java → AudioModule.c
SecurityModule.signChallenge(handle, challenge) → byte[]  FACT — Java → AudioModule.g
  ↓
AudioModule.<clinit>: System.loadLibrary("audio")         FACT
AudioModule.g(I[B)[B   ACC_NATIVE                         FACT
  ↓
libaudio.so
  Java_com_bmwgroup_connected_core_audio_AudioModule_g    FACT — readelf
  (OpenSSL-style RSA / md5WithRSA path; private-key load)  FACT strings — no key dump
  ↓
512 B signature → sas_login
```

Parallel in-app Binder (not used by Kit for `mobile20`):

```text
CarSecurityService (exported=false)
  → Stub.signChallenge(longHandle, challenge)
      → verifyCaller(uid)
      → SecurityContext.getmNativeHandle()
      → SecurityModule.signChallenge(intHandle, challenge)
          → same AudioModule.g / libaudio.so
```

## Stufen-Tabelle

### Stufe 1 — Consumer

| Feld | Wert |
|------|------|
| Evidence | AAIdrive / Kit — **FACT** (prior) |

### Stufe 2 — Kit SecurityAccess

| Feld | Wert |
|------|------|
| Evidence | `SecurityAccess.kt` — **FACT** (prior) |

### Stufe 3b — MyBMW SecurityModule (OEM bytecode)

| Feld | Wert |
|------|------|
| APK | MyBMW ROW 6.11.3 |
| Class | `com.bmwgroup.connected.core.security.SecurityModule` |
| Method | `public static signChallenge(I[B)[B` |
| Flags | **not native** — 5 code units: `invoke-static AudioModule.g` + `move-result-object` + `return-object` |
| Evidence | DEX disassembly — **FACT** |

Mapping SecurityModule → AudioModule:

| SecurityModule | AudioModule (obfuscated) |
|----------------|--------------------------|
| `init(String)` | `a(String)` native |
| `deInit()` | `b()` native |
| `createSecurityContext(String,String)->int` | `c(String,String)->int` native |
| `destroySecurityContext(int)` | `d(int)` native |
| `addAndVerifyCertificateFromPackage(int,byte[])` | `e(int,byte[])` native |
| `getCertificates(int)->byte[]` | `f(int)->byte[]` native |
| **`signChallenge(int,byte[])->byte[]`** | **`g(int,byte[])->byte[]` native** |

### Stufe 4 — JNI / native — **CONFIRMED**

| Feld | Wert |
|------|------|
| Library | `libaudio.so` (`arm64-v8a`) |
| Load | `System.loadLibrary("audio")` in `AudioModule.<clinit>` |
| JNI symbol | `Java_com_bmwgroup_connected_core_audio_AudioModule_g` @ `0xbda2c` size 324 |
| Error string | `Error while calling native function signChallenge with handle %d. ErrorCode %d` |
| Algo strings | `md5WithRSA`, `md5WithRSAEncryption`, `RSA-MD5`, OpenSSL `crypto/rsa/rsa_sign.c` |
| NEEDED | only `libc`, `libm`, `libdl` (OpenSSL statically linked inside) |
| Evidence | readelf + strings + DEX — **FACT** |

### Stufe 3a — Classic / MyBMW Binder

| Feld | Wert |
|------|------|
| MyBMW service | `com.bmwgroup.connected.core.services.security.CarSecurityService` |
| Exported | **false** |
| Inner call | Binder stub → `SecurityModule.signChallenge` |
| Evidence | Manifest + DEX invokes — **FACT** |

## Certificate entry (unchanged)

Cert is **not** an argument to `signChallenge`; context + challenge only.  
`getCertificates` / `addAndVerifyCertificateFromPackage` are sibling natives on the same module.

## STOP-Grenze

Gate **located** at `libaudio.so` / `AudioModule.g`.  
Gate **not solved**: no key extraction, no forge, no auth circumvention.
