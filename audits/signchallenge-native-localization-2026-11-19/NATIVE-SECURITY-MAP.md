# NATIVE-SECURITY-MAP

## OEM libraries (MyBMW 6.11.3 ROW, arm64-v8a)

| Library | ABI | Exports (security) | JNI registration | Strings/Symbols |
|---------|-----|--------------------|------------------|-----------------|
| **`libaudio.so`** | arm64-v8a | `Java_com_bmwgroup_connected_core_audio_AudioModule_{a..g}` | classic JNI short names (no `RegisterNatives` required) | `native function signChallenge`; `md5WithRSAEncryption`; OpenSSL RSA sign; private-key load errors |
| `libapproov.so` | arm64-v8a | Approov attestation | separate product | **not** SAS signChallenge |
| `libapp.so` / `libflutter.so` | arm64-v8a | Flutter | Flutter JNI | UI / remote features — **not** signer |
| Mapbox / Ramses / WebRTC / pdfium / … | arm64-v8a | — | — | unrelated |

**SHA-256 `libaudio.so`:** `7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90`

### AudioModule JNI map

| JNI | Java | Role |
|-----|------|------|
| `_a` | `init` | prepare native signer |
| `_b` | `deInit` | teardown |
| `_c` | `createSecurityContext` | package + appName → handle |
| `_d` | `destroySecurityContext` | release handle |
| `_e` | `addAndVerifyCertificateFromPackage` | cert inject/verify |
| `_f` | `getCertificates` | export certs for APP_AUTH bundle |
| **`_g`** | **`signChallenge`** | **challenge → signature** |

## Keystore / TEE screen

| API | In OEM APK this run? | Nutzung für signChallenge? |
|-----|----------------------|----------------------------|
| AndroidKeyStore | present in **Java** DEX (many hits) | **No evidence in `libaudio.so`** tying Keystore to `AudioModule.g` |
| OpenSSL private-key load | **yes** inside `libaudio.so` | **STRONG INFERENCE** production path uses in-process OpenSSL key object |
| StrongBox / TEE | no dedicated binder in signer path | **UNKNOWN / unlikely** for this JNI |

Java strings like `Could not retrieve the PrivateKey from the HU keystore` belong to **HU pairing / remoting cert stores**, not the `AudioModule` JNI signer.

**Antwort:** Die SAS-Signatur wird in **`libaudio.so`** erzeugt (JNI). Ein Android-Keystore/TEE-Dienst als Executor von `signChallenge` ist **nicht** belegt.

## Binder / OEM-Service screen

| Interface | Status |
|-----------|--------|
| Classic `*.SECURITY_SERVICE` + `ICarSecurityService` | **FACT** — Fall C at Classic app boundary (prior) |
| MyBMW `CarSecurityService` | **FACT** present; **`exported=false`** |
| Binder → native | **FACT** — stub calls `SecurityModule` → `AudioModule.g` → `libaudio.so` |
| Kit policy for `mobile20` | still prefers **in-process reflect** over bind (prior) |

## Crypto step ownership

| Step | Expected owner | Known executor |
|------|----------------|----------------|
| XOR preprocess | OEM signer | Algorithm prior FACT; runs inside native (`libaudio`) **INFERENCE** (XOR string also in DEX) |
| MD5 | OEM signer | `md5WithRSA` / `md5WithRSAEncryption` strings in `libaudio.so` — **FACT** (naming) |
| RSA | OEM signer | OpenSSL RSA sign symbols in `libaudio.so` — **FACT** |
| 512-B output | `signChallenge` return | **FACT** (prior field + tests); produced by `AudioModule.g` — **FACT** |

## STOP

Spur endet am **identifizierten** `libaudio.so` JNI entry.  
Keine Key-Extraktion, kein Forge, kein Bypass.
