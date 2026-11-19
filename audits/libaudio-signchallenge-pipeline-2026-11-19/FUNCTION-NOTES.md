# Function notes (signChallenge-relevant only)

Subject: `libaudio.so` SHA-256 `7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90`

---

## JNI entry

```
offset: 0xbda2c
function: Java_com_bmwgroup_connected_core_audio_AudioModule_g
input: x0=JNIEnv*, x1=jclass, w2=jint handle, x3=jbyteArray challenge
output: x0=jbyteArray signature | null (exception via 0xbc8c4)
calls:
  - JNIEnv+0x5c0 GetByteArrayElements
  - JNIEnv+0x558 GetArrayLength
  - 0xbd73c native_sign_impl
  - JNIEnv+0x580 NewByteArray
  - JNIEnv+0x680 SetByteArrayRegion
  - JNIEnv+0x600 ReleaseByteArrayElements (mode=2 JNI_ABORT)
relevant constants:
  - 0x4686f "Given challenge is null"
  - 0x4ccab "Error while calling native function signChallenge with handle %d. ErrorCode %d"
confidence: FACT
```

---

## Native sign core

```
offset: 0xbd73c
function: native_sign_impl (unnamed; sole BL target of g)
input: w0=handle, x1=challenge*, w2=len, x3=out**, x4=out_len*
output: w0=1 success / 0 fail; *out / *out_len on success
calls: context walk; cert ensure; MD5 serial; XOR; EVP MD5; 0xbdf84; 0x12e564; malloc/free/memcpy
relevant constants: challenge length must be 0x10
confidence: FACT
```

### Context + cert ensure (inside 0xbd73c)

```
offset: ~0xbd790–0xbd830
function: ensure context+0x18 X509*
input: context node
output: X509* in [ctx+0x18]
calls:
  - fallback: adr 0x51987; mov w1,#0x3c9; bl 0xca93c; bl 0x19d860 (arg1=0)
  - 0xbdf00 with "Feature Certificate" / "Debug Feature Certificate"
relevant constants:
  - embed X509 @ 0x51987 len 969 (sha1WithRSAEncryption; SAS.CertificateType=APP)
confidence: FACT (structure); INFERENCE name "Feature Certificate" path
```

### XOR pad from serial

```
offset: 0x196240 → 0xc4cf0 ; then 0x15523c / 0x15466c / 0x155170
function: serial extract + MD5_Init/Update(4)/Final
input: X509* from ctx+0x18
output: 16-byte digest at [fp-0x20]
relevant constants: MD5 IV @ 0x53770 = standard MD5
confidence: FACT
```

```
offset: 0xbd88c–0xbd8a0
function: length check + XOR
input: challenge[16], pad[16]
output: xored[16] on stack buffer
calls: —
relevant constants: cmp w27,#0x10 ; eor v0.16b
confidence: FACT
```

### EVP MD5 of xored challenge

```
offset: 0xd75f4 / 0x12b08c / 0xd7668 / 0xd78f0
function: EVP_MD_CTX_new / EVP_md5 / DigestInit_ex / DigestUpdate
input: xored[16]
output: MD_CTX ready for final+sign
relevant constants: "crypto/evp/digest.c"; MD5 method object
confidence: FACT
```

### PKEY lookup

```
offset: 0xbdf84
function: lookup_signer_pkey
input: x0=global+0x108 store; x4="com.bmwgroup.connected.bmw"
output: EVP_PKEY* via out-param (fp-0x88)
calls: OpenSSL helpers; 0x12d690 free path
relevant constants: 0x407df "com.bmwgroup.connected.bmw"
confidence: FACT (lookup+name); INFERENCE alias maps to PKCS#12 identity
```

### RSA sign

```
offset: 0x12e564
function: evp_sign_with_pkey
input: MD_CTX*, out_buf*, out_len*, EVP_PKEY*
output: success flag; *out_len set (RSA-4096 → 512)
calls: 0x12a244 (flag & 0x200); DigestFinal 0xd79a8; 0x13048c; 0x12ee9c; 0x130a68; 0x12ef34
relevant constants:
  - w1=#0x200 size/capability gate
  - "crypto/evp/pmeth_fn.c" @ EVP_PKEY_sign
  - "crypto/evp/pmeth_lib.c" @ CTX helpers
confidence: FACT
```

---

## Init / key material

```
offset: 0xbe448 (from AudioModule_a → 0xbc7b4)
function: load_embedded_pkcs12
input: adr 0x5249e ; length 0x10f2 (4338)
output: parsed crypto state (via 0xca93c)
calls: 0xca93c
relevant constants:
  - PKCS#12 DER @ 0x5249e
  - OID pkcs8ShroudedKeyBag ×1
  - OID pkcs7-encryptedData ×1
  - OID pbeWithSHAAnd3-KeyTripleDES-CBC ×2
confidence: FACT (presence/OID inventory only — no unwrap)
```

---

## Crypto backend

| Check | Result | Class |
|-------|--------|-------|
| NEEDED libs | only `libc`,`libm`,`libdl` | **FACT** |
| OpenSSL | statically linked; EVP/RSA/MD5 used on path | **FACT** |
| `dlsym`/`dlopen` on sign path | not in depth-≤3 PLT closure | **FACT** (unused for sign) |
| BoringSSL distinct | OPENSSL `crypto/…` paths → OpenSSL tree | **FACT** |

---

## Non-path OpenSSL strings (do not count as sign proof)

`PEM_read_bio_PrivateKey`, `cannot load private key`, `RSA PRIVATE KEY`, `md5WithRSAEncryption` — present in static OpenSSL; **0 ADRP xrefs** from BMW JNI wrappers. Catalog only.
