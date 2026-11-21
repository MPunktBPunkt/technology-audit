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
  │  pad16 = MD5(u32_be)  # APP_AUTH Wire: u32=0x02000000 @ 0x15523c/…
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
MD5( u32_be as 4 bytes ) → 16 B       FACT — MD5 IV @ 0x53770; MD5_Update len=4; MD5_Final
      ↓
XOR (16-byte NEON eor)                FACT — eor v0.16b,v1.16b,v0.16b @ 0xbd89c
      ↓
MD5 digest of XORed block             FACT — EVP_md5 + DigestUpdate(len=0x10)
      ↓
RSA via EVP_PKEY_sign                 FACT — pmeth_fn.c; size check w1=#0x200
      ↓
signature length written to *out_len  FACT — typically 512 for RSA-4096
```

**Wire FACT supersession (2026-11-20):** Disassembly shows `MD5(u32)` then XOR — **not**
raw serial XOR. For APP_AUTH Wire sessions the effective u32 is **`0x02000000`**
(CertificateType-shaped), **not** the TouchCommand X509 serial `0x0AA9`.  
RSA-VERIFY 8/8 + 2³² unique hit — product
`SAS_PAD_RSA_VERIFY_LAB_20261120.md` / gap audit
[`docs/analysis/F20_CONNECTED_GAP_AUDIT_20261120.md`](../../docs/analysis/F20_CONNECTED_GAP_AUDIT_20261120.md).

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

---

## D. APP_AUTH / certificate binding

**CONFIRMED (partial mechanism) / name-string UNKNOWN**

| Observation | Class |
|-------------|-------|
| `createSecurityContext(package, appName)` stores strdup names on context (`+0x08`,`+0x10`) | **FACT** |
| Sign uses **MD5(u32)** as XOR pad (u32 from cert/context path; **not** raw serial XOR) | **FACT** (native) |
| APP_AUTH Wire pad-u32 = `0x02000000` (≠ X509 serial `0x0AA9`) | **FACT** (Wire 2026-11-20) |
| Fallback embed cert CN/attrs include `SAS.CertificateType=APP`, BMW A4A FeatureCertificate | **FACT** |
| PKEY lookup name hardcoded `"com.bmwgroup.connected.bmw"` | **FACT** |
| Literal `APP_AUTH` / `sas_certificate` strings inside `libaudio.so` | **NOT_FOUND** |
| Java-side CertMangling / `sas_certificate` merge still outside this SO | prior audit — not re-proven here |

Binding is via **security-context certificate + named PKEY alias**, not a string token `APP_AUTH` inside the .so.

---

## E. Final Classification

### CASE A — Embedded software key

```text
libaudio.so
  ↓  AudioModule.init embeds PKCS#12 (pkcs8ShroudedKeyBag)
  ↓  unwrap into OpenSSL EVP_PKEY (in-process; PBE-shrouded at rest)
  ↓  AudioModule.g → XOR+MD5 → EVP_PKEY_sign (RSA)
  ↓  512-byte signature
```

Not CASE B/C/D for the `signChallenge` path.

---

## F. Remaining Gap

**Known:** Java → JNI `AudioModule.g` → in-process OpenSSL RSA in `libaudio.so`, with embedded PKCS#12 providing shrouded private-key material.

**PKCS#12 anatomy (revised 2026-11-22):** PFX @ `0x5249e` CLOSED; two PBE salts +
separate MAC salt, all **Iter=1**, SHA1-3DES — **FACT**. Empty password **REJECTED**.
`0xca93c` = resource **registration** (**REJECTED** as parse/unwrap). `0x167184` =
generic consumer (**REJECTED** as PFX unwrap). Exact `PKCS12_*` callsite + passphrase
origin = **OPEN**. Full table: [`PKCS12-ANATOMY.md`](PKCS12-ANATOMY.md).

**Unknown:** passphrase **origin** + unwrap callsite — not “where is the key?”.
Feature-cert `x1=xzr` paths ≠ SAS-PFX password (**REJECTED** conflation).

**STOP:** No attempt to decrypt the shrouded key bag or export a usable private key.
No passphrase brute-force tooling in this audit.

---

## G. Next Step

**Preferred (product):** Weg A / Music RHMI (Gate B CLOSED) — Standalone-Signer is **not**
the blocker for PiDrive menu work.

**Optional (observe-only, Weg B prep):** break at **PLT `PKCS12_parse`** and capture
password pointer + length (registers) to promote Alias↔PKCS#12 and passphrase origin
INFERENCE→FACT — **no key dump**. See [`PKCS12-ANATOMY.md`](PKCS12-ANATOMY.md).

---

## Evidence rules applied

- OpenSSL strings alone ≠ path proof; path proven by **disassembly + OPENSSL source-file ADR tags + PLT closure**.
- Embedded PKCS#12 **structure/OID inventory only** — no private-key extraction.
- Imported `open`/`socket` ≠ use on sign path.
- `CarSecurityService` not re-audited; prior: converges to same native.
- Iter=1 = cheap KDF (**FACT-math**); does not imply a known passphrase (**UNKNOWN**).

## Artefakte

- This README (A–G report)
- [`PKCS12-ANATOMY.md`](PKCS12-ANATOMY.md) — Salt/Iter/MAC claim table (2026-11-21)
- Prior: `audits/signchallenge-native-localization-2026-11-19/`
