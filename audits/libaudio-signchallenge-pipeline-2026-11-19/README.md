# Audit: libaudio.so signChallenge pipeline (2026-11-19)

```yaml
id: libaudio-signchallenge-pipeline-2026-11-19
continuation_of:
  - audits/signchallenge-native-localization-2026-11-19/
subject: libaudio.so (MyBMW ROW 6.11.3 / 56034, arm64-v8a)
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
scope: AudioModule.g → crypto → key/signer provider (observe-only)
status: complete
classification: CASE A — Embedded software key
```

## Auftrag

Wie gelangt die native Signierpipeline vom JNI-Einstieg `AudioModule.g` zur RSA-Signatur, und woher kommt die Signer-/Key-Ressource?

Kein Key-Dump, kein Forge, kein Bypass.

---

## A. Confirmed Call Chain

```text
Java_com_bmwgroup_connected_core_audio_AudioModule_g   @ 0xbda2c  (size 324)
  │  JNIEnv: GetByteArrayElements / GetArrayLength
  │  JNIEnv: NewByteArray / SetByteArrayRegion / ReleaseByteArrayElements(JNI_ABORT)
  ↓
native_sign_impl                                        @ 0xbd73c
  │  lookup security_context by handle (list @ 0x1eb110)
  │  ensure X509* at context+0x18 (fallback: embed cert @ 0x51987)
  │  serial = X509_get_serialNumber-style extract (@ 0x196240 → 0xc4cf0)
  │  pad16 = MD5(serial_u32)                            @ 0x15523c/0x15466c/0x155170
  │  xored = challenge[16] XOR pad16                    (NEON eor v0.16b)
  │  EVP_MD_CTX + EVP_md5 + DigestInit/Update(xored,16) @ 0xd75f4/0x12b08c/0xd7668/0xd78f0
  │  pkey = lookup(global@0x1eb108, "com.bmwgroup.connected.bmw")  @ 0xbdf84
  ↓
EVP_sign_finalize                                       @ 0x12e564
  │  requires MD_CTX flag 0x200 (RSA capability check)
  │  EVP_DigestFinal → digest
  │  EVP_PKEY_CTX_new / sign_init / ctrl / EVP_PKEY_sign
  │    (OPENSSL file tags: crypto/evp/pmeth_fn.c, pmeth_lib.c)
  ↓
512-byte signature → jbyteArray
```

**Init (key material load, before sign):**

```text
AudioModule_a (init)
  → 0xbc7b4 → 0xbe448
       adr  x0, #0x5249e
       mov  w1, #0x10f2          ; 4338 bytes
       b    0xca93c              ; parse embedded blob
  → PKCS#12 (embedded in libaudio.so) into process crypto state
```

---

## B. Crypto Pipeline

```text
challenge[16]                         FACT — cmp w27,#0x10 rejects other lengths
      ↓
MD5( cert_serial as 4 bytes ) → 16 B  FACT — MD5 IV constants @ 0x53770; MD5_Update len=4; MD5_Final
      ↓
XOR (16-byte NEON eor)                FACT — eor v0.16b,v1.16b,v0.16b @ 0xbd89c
      ↓
MD5 digest of XORed block             FACT — EVP_md5 + DigestUpdate(len=0x10)
      ↓
RSA via EVP_PKEY_sign                 FACT — pmeth_fn.c; size check w1=#0x200
      ↓
signature length written to *out_len  FACT — typically 512 for RSA-4096
```

| offset | function (role) | input | output | calls | constants | confidence |
|--------|-----------------|-------|--------|-------|-----------|------------|
| `0xbda2c` | `AudioModule_g` JNI | `JNIEnv*, jclass, jint handle, jbyteArray` | `jbyteArray` or null+throw | JNIEnv vtable; `0xbd73c`; throw `0xbc8c4` | err `"Given challenge is null"` `@0x4686f`; `"…signChallenge…"` `@0x4ccab` | **FACT** |
| `0xbd73c` | native sign core | handle, challenge*, len, out**, out_len* | `1`/`0` + buffers | MD5 family; `0xbdf84`; `0x12e564` | len must be `0x10` | **FACT** |
| `0x15523c`/`0x15466c`/`0x155170` | MD5_Init/Update/Final | serial u32 | 16-byte digest | memset/memcpy | IV `67452301…` | **FACT** |
| `0xbd89c` | XOR | challenge∥pad | 16-byte buffer | — | NEON 16B | **FACT** |
| `0xd75f4`/`0x12b08c`/`0xd7668`/`0xd78f0` | EVP_MD_CTX / MD5 / Init / Update | xored[16] | MD_CTX state | OpenSSL EVP | `"crypto/evp/digest.c"` | **FACT** |
| `0xbdf84` | PKEY/cert lookup | global store + name | `EVP_PKEY*` out | OpenSSL helpers | `"com.bmwgroup.connected.bmw"` `@0x407df` | **FACT** |
| `0x12e564` | sign finalize | MD_CTX + PKEY | sig bytes + len | `EVP_PKEY_sign` path | `#0x200` | **FACT** |

Dataflow does **not** leave `libaudio.so` for the crypto operation (no `open`/`dlopen`/`socket` on depth-≤3 sign graph).

---

## C. Key / Signer Source

| Possibility | Evidence | Status |
|-------------|----------|--------|
| Embedded in `libaudio.so` | Init loads VA `0x5249e` len `0x10f2` PKCS#12; OID **`pkcs8ShroudedKeyBag` count=1**; `pkcs7-encryptedData`; `pbeWithSHAAnd3-KeyTripleDES-CBC`×2. Separate X.509 Feature Certificate `@0x51987` (APP SAS attrs) for context fallback — **not** the private key. | **CONFIRMED** (embedded shrouded key material + local sign) |
| File/resource (`open`/`AAsset`/`/data/…`) | No `/data/`, `AAsset` strings in SO; sign-path PLT has no `open`/`mmap` usage | **REJECTED** for signChallenge path |
| Android Keystore / TEE / KeyMint | Zero hits: `keystore`, `KeyStore`, `KeyMint`, `keymaster`, `StrongBox`, `AndroidKeyStore` | **REJECTED** (`NOT_FOUND`) |
| External IPC / Binder / socket | `socket`/`connect` imported but **not** reached from sign depth-≤3; no `libbinder` strings; PLT on path = malloc/free/memcpy/pthread/rand only | **REJECTED** for signChallenge path |

OpenSSL PEM/`cannot load private key` strings exist in the static OpenSSL copy; **no ADRP xrefs from BMW wrappers** to those strings. They are library capability residue, **not** proof the live path PEM-reads a file. Live path uses **embedded PKCS#12** + `EVP_PKEY_sign`.

### Keystore / TEE classification

| Result | Class |
|--------|-------|
| Android Keystore/TEE for this path | **NOT_FOUND** |

### VIN-derived key (explicit)

| Claim | Status |
|-------|--------|
| Embedded RSA key material in `libaudio.so` PKCS#12 @ fixed VA `0x5249e` (4338 B) | **FACT** |
| `private_key = f(VIN)` / per-vehicle KDF into the sign path | **HYPOTHESIS / not evidenced** — treat as **REJECTED for planning** until a contrary dataflow appears |

**Why VIN→key is incompatible with the FACTs above:** the PKCS#12 blob sits at a **fixed VA in a single public APK release binary**. A VIN-derived private key would require either (a) different key material per vehicle build or (b) a runtime KDF/VIN dataflow into key construction on the sign path. Disassembly shows **neither**: no `open`/`AAsset` on depth≤3, and the sign graph inputs are challenge + cert serial only. A universal release `.so` cannot hold a per-VIN RSA private key at a fixed offset.

Do **not** open a “derive key from VIN” workstream from this audit.

---

## D. APP_AUTH / certificate binding

**CONFIRMED (partial mechanism) / name-string UNKNOWN**

| Observation | Class |
|-------------|-------|
| `createSecurityContext(package, appName)` stores strdup names on context (`+0x08`,`+0x10`) | **FACT** |
| Sign uses **MD5(cert_serial_u32)** as XOR **pad** (not raw serial in XOR) from `context+0x18` X509 | **FACT** |
| Fallback embed cert CN/attrs include `SAS.CertificateType=APP`, BMW A4A FeatureCertificate | **FACT** |
| PKEY lookup name hardcoded `"com.bmwgroup.connected.bmw"` | **FACT** |
| That alias **maps to** the embedded PKCS#12 identity | **INFERENCE** (not dynamically proven; see §G) |
| Literal `APP_AUTH` / `sas_certificate` strings inside `libaudio.so` | **NOT_FOUND** |
| Java-side CertMangling / `sas_certificate` merge still outside this SO | prior audit — not re-proven here |

Binding is via **security-context certificate + named PKEY alias**, not a string token `APP_AUTH` inside the .so.

**A ↔ B (open link):** embedded PKCS#12 key material **(A)** vs wire `sas_certificate` / APP_AUTH context **(B)**. Protocol *math* is reconstructed; a successful Field `sas_login` still needs HU-accepted cert context **and** the matching private key. MyBMW is not required to *compute* the pad/hash pipeline, but remains required for an *accepted* constellation until A↔B is settled with a lawful matching pair.

---

## E. Final Classification

### CASE A — Embedded software key

```text
libaudio.so
  ↓  AudioModule.init embeds PKCS#12 (pkcs8ShroudedKeyBag)
  ↓  unwrap into OpenSSL EVP_PKEY (in-process; PBE-shrouded at rest)
  ↓  AudioModule.g → MD5(serial)→XOR→MD5 → EVP_PKEY_sign (RSA)
  ↓  512-byte signature
```

Not CASE B/C/D for the `signChallenge` path.

### Dual-gate invariant (do not collapse)

```text
(A) Client sign mechanism     → FACT (this audit / CASE A)
(B) HU acceptance of cert+sig → OPEN (Field / product gate)
```

“SAS is not an unknown protocol problem” applies to **(A) only**. Lab stub `AUTHENTICATED` ≠ Field `(B)`.

---

## F. Remaining Gap

**Known:** Java → JNI `AudioModule.g` → in-process OpenSSL RSA in `libaudio.so`, with embedded PKCS#12 providing shrouded private-key material.

**Unknown:** PKCS#12 unlock passphrase / unwrap details (empty vs hardcoded vs derived) — static evidence shows PBE OIDs and a null-password-style call on the **feature-cert** branch (`0x19d860` with `x1=xzr`), but does **not** fully document the init unwrap password without dynamic observation.

**STOP:** No attempt to decrypt the shrouded key bag or export a usable private key.

---

## G. Next Step

### Preferred — Test A: B3 / wire serial pad cross-check (no key access)

Capture a real MyBMW/AAIdrive session (B3 relay or equivalent jsonl):

1. `sas_certificate` → extract effective X509 **serial_u32**
2. `_result_sas_certificate` → **challenge[16]**
3. `sas_login` → signature bytes (for later; not required for pad-only check)

Compute `pad16 = MD5(serial_u32_be)` and verify the native transform `challenge XOR pad → MD5` against the CASE A recipe. This bridges **APK ↔ Wire** without private-key access and feeds the A↔B identity question.

Implementation live in `esp32.bt-analyzer`: `tools/sas_pad_crosscheck.py`, B3 `etch.sas` enrichment, `etch_codec.extract_pkcs7_cert_serials` — see consolidation doc below.

### Optional — dynamic observe-only (alias binding)

Break on `0xbe448` / PKCS#12 parse and on `EVP_PKEY_sign` to confirm which PKEY alias/`com.bmwgroup.connected.bmw` maps to after init — still without dumping key material. Useful for promoting alias↔PKCS#12 from **INFERENCE** → **FACT**; weaker than Test A for Field protocol work.

---

## Evidence rules applied

- OpenSSL strings alone ≠ path proof; path proven by **disassembly + OPENSSL source-file ADR tags + PLT closure**.
- Embedded PKCS#12 **structure/OID inventory only** — no private-key extraction.
- Imported `open`/`socket` ≠ use on sign path.
- `CarSecurityService` not re-audited; prior: converges to same native.

## Artefakte

- This README (A–G report)
- `SAS_SIGNER_CASE_A_CLOSED_20261119.md` — dual-gate / VIN / Test A consolidation
- `FUNCTION-NOTES.md` — per-function FACT/INFERENCE
- Prior: `audits/signchallenge-native-localization-2026-11-19/`
- Product mirror + tooling: `esp32.bt-analyzer` `docs/analysis/SAS_SIGNER_CASE_A_CLOSED_20261119.md`
