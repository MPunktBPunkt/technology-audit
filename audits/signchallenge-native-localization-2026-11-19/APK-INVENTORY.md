# APK Inventory

## Ergebnis

| Ziel | Status |
|------|--------|
| MyBMW (`de.bmw.connected.mobile20.row`) | **FOUND** — 6.11.3 (56034) |
| BMW Connected Classic | not pulled this run (MyBMW path sufficient for Fall D) |
| adb device | none attached |

## Source

| Feld | Wert |
|------|------|
| User pointer | https://www.apkmirror.com/apk/bmw/my-bmw-2/ |
| APKMirror direct download | **blocked** (Cloudflare challenge from this host) |
| Alternate | APKPure via `apkeep -d apk-pure -o acknowledge_dangers=true` (research ack) |
| Artifact | `de.bmw.connected.mobile20.row@6.11.3.xapk` |
| SHA-256 (xapk) | `abd9dad0ed67455d242f9577bd23b61fe66d0f3d0baf875d7ffc74601e79f75c` |
| Working copy | `/tmp/mybmw-apk/` (not committed) |

## Package metadata

| Feld | Wert |
|------|------|
| package name | `de.bmw.connected.mobile20.row` |
| versionName / versionCode | `6.11.3` / `56034` |
| minSdk / targetSdk | 28 / 36 |
| ABI in analyzed split | `arm64-v8a` (`config.arm64_v8a.apk`) |
| XAPK members | base APK + `config.arm64_v8a` + `config.en` + `config.xxhdpi` + `manifest.json` |

## Native libraries (`lib/arm64-v8a/`)

Security-relevant:

| Library | SHA-256 | Role |
|---------|---------|------|
| `libaudio.so` | `7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90` | **SAS signer** — JNI `AudioModule_a`…`_g` |
| other `.so` | see analysis notes | Flutter/Mapbox/Approov/Ramses/WebRTC — **not** signChallenge |

Full arm64 `.so` list (23): `libaudio`, `libapp`, `libapproov`, `libflutter`, Mapbox, Ramses, WebRTC, ML Kit, pdfium, etc.

## Class / method hits

| Symbol | Location |
|--------|----------|
| `com.bmwgroup.connected.core.security.SecurityModule` | `classes2.dex` — Java wrappers |
| `com.bmwgroup.connected.core.audio.AudioModule` | `classes2.dex` — `native` methods + `loadLibrary("audio")` |
| `com.bmwgroup.connected.core.services.security.CarSecurityService` | service, **`android:exported="false"`** |
| `ICarSecurityService` AIDL stubs | present; used by internal Binder path |
| `signChallenge` / `createSecurityContext` / `getCertificates` | SecurityModule + AudioModule + Binder stub |

## Cert assets (names only — no key material)

| Path | Note |
|------|------|
| `assets/carapplications/*/*.p7b` | app feature certs |
| `assets/flutter_assets/assets/certificates/my_BMW-00.00.16.p7b` | Flutter-bundled cert |
| No APP_AUTH `.pem` / `.p12` / `.bks` found under obvious names | key locus inside native still open |

## Unblock note

Prior run was blocked on missing APK. This inventory unblocks JNI mapping.
