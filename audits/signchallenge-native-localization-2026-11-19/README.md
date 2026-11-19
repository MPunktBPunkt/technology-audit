# Audit Campaign: signchallenge-native-localization-2026-11-19

```yaml
id: signchallenge-native-localization-2026-11-19
project_id: bimmergestalt-idrive-refs
started: 2026-11-19
ended: 2026-11-19
status: complete   # observe-only; Fall D CONFIRMED
profile: planning
standard_version: "0.7.1"
continuation_of:
  - audits/signchallenge-pipeline-localize-2026-11-19/
  - audits/idriveconnectkit-securityaccess-2026-11-19/
apk_input:
  package: de.bmw.connected.mobile20.row
  versionName: "6.11.3"
  versionCode: 56034
  abi: arm64-v8a
  source: APKPure via apkeep (APKMirror blocked by Cloudflare from this host)
  artifact: de.bmw.connected.mobile20.row@6.11.3.xapk
  sha256_xapk: abd9dad0ed67455d242f9577bd23b61fe66d0f3d0baf875d7ffc74601e79f75c
adb_devices: []
```

## Fragestellung

Wo sitzt die Implementierungsgrenze von `SecurityModule.signChallenge(...)`?

```text
Java/Kotlin → JNI? → native .so? → RSA / Keystore / TEE / Binder?
```

Observe-only. Kein Key-Dump, kein Forge, kein Bypass.

## Verdict

**Fall D CONFIRMED.** MyBMW `SecurityModule.signChallenge` is a Java thin wrapper that
calls obfuscated native `AudioModule.g`; that JNI symbol lives in **`libaudio.so`**.

```text
Kit SecurityAccess
  → SecurityModule.signChallenge(handle, challenge)     FACT — Java, non-native
      → AudioModule.g(handle, challenge)                FACT — ACC_NATIVE
          → System.loadLibrary("audio")                 FACT — AudioModule.<clinit>
          → libaudio.so
               Java_com_bmwgroup_connected_core_audio_AudioModule_g   FACT — readelf
```

Same native path is reached from in-app `CarSecurityService` (`exported=false`) after
caller UID checks — Binder is a wrapper, not a separate signer.

## Fall A/B/C/D

| Fall | Status |
|------|--------|
| A Key in APK/managed blob | **STRONG INFERENCE** — `libaudio.so` loads OpenSSL-style private-key material (`RSA PRIVATE KEY`, `cannot load private key`, `md5WithRSAEncryption`); no APP_AUTH `.pem`/`.p12` found in APK assets (only `.p7b` certs). Exact key file locus **UNKNOWN**. |
| B Keystore/TEE | **UNLIKELY for signChallenge** — no `AndroidKeyStore` strings in `libaudio.so`; Java Keystore hits map to HU pairing cert store, not the JNI signer. |
| C OEM Binder | **Outer Classic path FACT (prior).** MyBMW: `CarSecurityService` present, **`exported=false`**; Binder stub calls `SecurityModule.signChallenge` → same `libaudio.so`. |
| D JNI/native OEM lib | **CONFIRMED** — `libaudio.so` / `AudioModule.g` |

## Wichtigste FACTs (dieser Lauf)

| FACT | Evidence |
|------|----------|
| Package `de.bmw.connected.mobile20.row` 6.11.3 (56034) | APK manifest / androguard |
| `SecurityModule.signChallenge` is **not** `native` | DEX access flags + bytecode → `AudioModule.g` |
| `AudioModule` loads `libaudio` | `<clinit>`: `System.loadLibrary("audio")` |
| JNI exports `AudioModule_a`…`_g` | `readelf -Ws libaudio.so` |
| Error string `native function signChallenge` | UTF-8 string inside `libaudio.so` |
| Algo form `md5WithRSA` / `md5WithRSAEncryption` in native | strings in `libaudio.so` (matches prior Analysis) |
| `CarSecurityService` exported=false | AndroidManifest |

## STOP-Grenze

Identified **where** the signature is produced (`libaudio.so` via `AudioModule.g`).  
**Not** done (and out of scope): private-key extraction, forge, SAS bypass, TEE attack.

## Artefakte

- [APK-INVENTORY.md](APK-INVENTORY.md)  
- [SIGNCHALLENGE-CALLCHAIN.md](SIGNCHALLENGE-CALLCHAIN.md)  
- [NATIVE-SECURITY-MAP.md](NATIVE-SECURITY-MAP.md)  
- [FIELD-CROSSWALK.md](FIELD-CROSSWALK.md)  

## Leitplanke

> Wir wollen wissen, **WO** die Signatur erzeugt wird — nicht den Schlüssel besitzen.
