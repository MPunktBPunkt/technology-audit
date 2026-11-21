# PKCS#12 Anatomy Addendum (2026-11-21 → rev. 2026-11-22d)

```yaml
parent: README.md
subject: embedded PKCS#12 @ 0x5249e in libaudio.so
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
build_id: cf781dbc8425a5fe2cbbd02be5cfc7630398301f
elf: AArch64, stripped, size 1981072
scope: key-origin + native SAS sign E2E — observe/document only
status: >
  Native SAS sign chain CLOSED end-to-end (PFX→pass→EVP_PKEY→MD5/XOR/MD5→
  EVP_SignFinal→EVP_PKEY_sign→RSA-4096). Credentials withheld.
  Micro-gap: ASN.1 field provenance of CertificateType integer (STRONG).
```

## Verdict

Native SAS signing in `libaudio.so` is **end-to-end CLOSED**:

```text
Challenge[16] → MD5(LE32(certType)) → XOR → MD5 → EVP_SignFinal
  → EVP_PKEY_sign → RSA-4096 PKCS#1 → 512 B
         ▲
         └── EVP_PKEY from embedded PFX (local pass + PKCS12_parse)
```

**STOP:** do not publish passphrase / PKCS#8 / private key in this repo.

---

## Binary identity (FACT)

| Item | Value |
|------|-------|
| Size | 1 981 072 B |
| SHA-256 | `7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90` |
| Build ID | `cf781dbc8425a5fe2cbbd02be5cfc7630398301f` |

---

## Embedded PFX (FACT)

| Item | Value |
|------|-------|
| VA / length | `0x5249e` / `0x10f2` (4338 B) |
| Encoding | BER indefinite (`30 80…`), PKCS#12 v3 |
| Contents | AuthenticatedSafe, MACData, CertificateBag, **one** `pkcs8ShroudedKeyBag` |
| Load | `0xbe448`: `adr x0,#0x5249e` ; `mov w1,#0x10f2` ; `b 0xca93c` |

`0xca93c` = resource/blob **registration** — **REJECTED** as PKCS#12 parser
(unchanged from rev. 2026-11-22).

---

## PBE + MAC (FACT)

| Region | Salt | Iter | Alg |
|--------|------|-----:|-----|
| PBE #1 | `8d6188b36bf04974` | 1 | SHA1 + 3-Key 3DES-CBC |
| PBE #2 | `4b7f305e4f959733` | 1 | same |
| MAC | `38dbae698b76e656` | 1 | SHA-1 |

Stored MAC digest: `da709b8794d657ab786f8ea210da98955f4822c1`  
Reconstructed local passphrase → **same MAC** → passphrase correctness **FACT**
(cryptographic), not mere plausibility.

Empty/NULL password → **REJECTED**.

---

## Local passphrase (FACT — value withheld)

```text
obfuscated material (@ ~0x4e699)
        │
        ▼
0xbe458  Base64 decode
        │
        ▼
0xbe59c  BMW deobfuscator (XOR const 0x17 + LUT + feedback)
        │
        ▼
40-byte passphrase  →  PKCS12_verify_mac / PKCS12_parse
        │
        ▼
password buffer wiped after parse
```

| Claim | Level |
|-------|-------|
| Passphrase is locally reconstructible inside `libaudio.so` | **FACT** |
| Length 40 bytes | **FACT** |
| MAC verifies reconstructed passphrase | **FACT** |
| External/server-supplied passphrase required | **REJECTED** |
| Plaintext passphrase published in this repo | **STOP** (withheld) |

---

## OpenSSL unwrap callsites (FACT)

| Address | Role |
|---------|------|
| `0x164988` | `PKCS12_parse(p12, pass, pkey**, cert**, ca**)` |
| `0x165b74` | `PKCS12_verify_mac` (incl. NULL/`""` fallbacks then real pass) |
| `0xbe100` area | caller: `x0=p12`, `x1=pass`, `x2..x4` out-ptrs → `bl 0x164988` |
| `0x165348` / `0x1653b8` / `0x16561c` | shrouded-bag / PBE decrypt path |

Generic init consumers `0xc8484`, `0x167184`, `0xc7950` remain **not** the parser
(**REJECTED** as unwrap — prior correction stands).

---

## Unwrapped key + certificate (FACT)

After local unwrap:

| Item | Value |
|------|-------|
| Key | RSA-4096, 2-prime, **e = 3** |
| Form | PKCS#8 PrivateKeyInfo → `EVP_PKEY` |
| Cert friendlyName / CN | `a4a_app_BMWTouchCommand_Connection_00.00.10` |
| Issuer CN | `a4a_android-ca` |
| Serial | `0x0AA9` |
| Validity | 2014-10-31 – 2015-07-30 |
| Cert SHA-256 | `991517428f7f5213897a9538e5deef7666ab3bc246a19b3a4289b04158626877` |
| SPKI SHA-256 (key ≡ cert) | `3291483fe3170ccfdd44422ef7024e838753c1b31c75b4267be3ed13dcc7cf05` |

Private-key → SPKI and certificate → SPKI match → same key material **FACT**.

---

## Native sign entry (rev. 2026-11-22d) — FACT

**Correction:** `AudioModule_f` is **not** the signer. Symbol bounds:

| Range | Role |
|-------|------|
| `0xbd674`–`0xbd738` | `Java_…AudioModule_f` |
| `0xbd73c` | **`native_sign_impl`** (anonymous) |
| `0xbda2c` | `Java_…AudioModule_g` → JNI get challenge bytes → **`bl 0xbd73c`** |

```text
SecurityModule.signChallenge
  → AudioModule.g
  → GetByteArrayElements / GetArrayLength (challenge)
  → 0xbd73c native_sign_impl
```

Intermediate wording that treated `AudioModule_f` as the signer is **REJECTED**.

---

## Message preparation inside `0xbd73c` (FACT)

### First MD5 — machine-code exact

| Addr | Role |
|------|------|
| `0x15523c` | `MD5_Init` (IV @ `0x53770` = classic MD5 IVs) |
| `0x15466c` | `MD5_Update` — here **exactly 4 bytes** `LE32(w20)` |
| `0x155170` | `MD5_Final` → 16-byte pad |

For Wire `CertificateType = 0x02000000` → bytes `02 00 00 00`:

```text
PAD = MD5(02 00 00 00) = F2DD0DEDB2C260419ECE4A9E03B2E828
```

### XOR + length gate

```text
cmp w27, #0x10          ; challenge length MUST be 16
eor v0.16b, challenge, PAD
```

### Second MD5 (EVP)

`EVP_MD_CTX` via `0xd75f4` / `0x12b08c` / `0xd7668` / `0xd78f0` with
`Update(..., XOR_result, 16)` → digest into `EVP_SignFinal`.

Closed formula (native ≡ Wire):

```text
D = MD5( Challenge[16] XOR MD5(LE32(CertificateType)) )
```

### CertificateType provenance (micro-gap)

`0x196240` → `0xc4cf0` → `0xc4858(..., type=2)` extracts an **ASN.1 INTEGER** into `w20`.

| Claim | Level |
|-------|-------|
| ASN.1 INTEGER extracted and MD5'd as LE32 | **FACT** |
| That integer is Wire `CertificateType` / `0x02000000` | **STRONG** (Wire-closed; not hard-coded at this site) |

---

## PFX loader + `EVP_PKEY*` → sign (FACT)

Loader `0xbdf84` (alias `com.bmwgroup.connected.bmw` @ `0x407df`): pass deobfuscate →
`PKCS12_parse` → returns `EVP_PKEY*`.

Inside sign path (`0xbd73c` region, e.g. `@bd8fc`):

```text
bl  0xbdf84
ldur x0/x3, [x29,#-0x88]   ; SAME EVP_PKEY*
bl  0x12e564               ; EVP_SignFinal(ctx, sig, &len, pkey)
```

---

## `0x12e564` = `EVP_SignFinal` (FACT)

Matched to classic OpenSSL `EVP_SignFinal` sequence:

| Addr | Role |
|------|------|
| `0xd79a8` | `EVP_DigestFinal_ex` |
| `0x12d04c` | `EVP_PKEY_size` → 512 for RSA-4096 |
| `0x13048c` | `EVP_PKEY_CTX_new` |
| `0x12ee9c` | `EVP_PKEY_sign_init` |
| `0x130a68` | `EVP_PKEY_CTX_ctrl` (signature MD) |
| **`0x12ef34`** | **`EVP_PKEY_sign`** (`pmeth->sign` dispatch) **FACT** |

```text
EVP_PKEY_sign(pkctx, sigret, &siglen, digest, digest_len)
```

RSA-4096 PKCS#1 v1.5 → 512-byte APP_AUTH signature. Field **8/8** VERIFY unchanged.

**PFX key is the local SAS signer key** — **FACT** (dataflow + OpenSSL match + cert/SPKI + wire).

---

## Four layers (summary)

| Layer | Status |
|-------|--------|
| A Secret/key material (embedded PFX RSA-4096) | CLOSED |
| B Key unwrapping (local pass + MAC + parse) | CLOSED |
| C Message prep (LE32 MD5 → XOR → MD5, len=16) | CLOSED |
| D Signature (`EVP_SignFinal` → `EVP_PKEY_sign` → RSA) | CLOSED |
| CertificateType ASN.1 field identity | STRONG / micro-OPEN |
| Same key every `libaudio.so` build | UNKNOWN |
| PiDrive standalone SAS product-ready | OPEN (Weg B + policy) |

---

## Falsified / superseded

| Claim | Status |
|-------|--------|
| Empty password / Keystore / remote signer for this path | REJECTED |
| `AudioModule_f` is the SAS signer | **REJECTED** (bounds; signer = `g` → `0xbd73c`) |
| `0x12e564` only a vague “output wrapper” | **SUPERSEDED** → `EVP_SignFinal` FACT |
| `EVP_PKEY_sign` not located | **SUPERSEDED** → `0x12ef34` FACT |
| “Where is the key?” / “does PFX key sign?” | **CLOSED** |

---

## Next step

1. Trace ASN.1 object into `0x196240` / `0xc4cf0` until the field that yields `0x02000000`
   is named (CertificateType bind FACT).  
2. Optional: instruction-level annotate of `0xbd73c` + `0xbdf84` (pass wipe, pkey store).

**Not next for product:** publishing credentials. Menu work remains **Weg A** until an
explicit Weg B decision.

Cross-links: [`README.md`](README.md) · [`FUNCTION-NOTES.md`](FUNCTION-NOTES.md) ·
bt-analyzer `SAS_STATUS_CRYPTO_CLOSED_20261120.md` · `SAS_SIGNER_CASE_A_CLOSED_20261119.md`
