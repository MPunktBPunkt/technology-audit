# PKCS#12 Anatomy Addendum (2026-11-21 → rev. 2026-11-22b)

```yaml
parent: README.md
subject: embedded PKCS#12 @ 0x5249e in libaudio.so
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
build_id: cf781dbc8425a5fe2cbbd02be5cfc7630398301f
elf: AArch64, stripped, size 1981072
scope: key-origin + EVP_PKEY dataflow — observe/document only
status: >
  PFX origin CLOSED; EVP_PKEY* from PKCS12_parse → x3 of 0x12e564 CLOSED (FACT);
  plaintext credentials NOT published; deepest RSA pmeth inside 0x12e564 = next hop
```

## Verdict

> **Where does the private key come from?** → CLOSED (embedded PFX + local pass).  
> **Does that `EVP_PKEY*` enter the sign path?** → **YES (FACT)** — same pointer is
> returned from `0xbdf84` and passed as **x3** into `0x12e564` (prior: EVP_sign_finalize).

Remaining hop:

```text
0x12e564  ──?──►  innermost EVP_PKEY_sign / RSA private op
```

Not a cryptography gap; not a missing key — one wrapper to resolve.

**STOP (repo hygiene):** do **not** commit plaintext passphrase, PKCS#8, or usable private
key material. Architecture + addresses + public cert fingerprints only.

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

## SAS signer linkage — EVP_PKEY dataflow (rev. 2026-11-22c)

### BMW PFX loader `0xbdf84` (FACT)

Called from `AudioModule_e` / `AudioModule_f` (e.g. `@bd8fc`):

| Arg | Value |
|-----|-------|
| x0 | PFX / resource object |
| x1 | NULL |
| x2 | `&local_pkey` (`x29-0x88`) |
| x3 | NULL |
| x4 | `0x407df` = **`com.bmwgroup.connected.bmw`** |

Inside loader: password path → `PKCS12_parse` (`0x164988`) → writes `EVP_PKEY*` to
caller out-ptr (`str` via `[sp,#0x10]` / `[x29-0x88]`).

### Same `EVP_PKEY*` → `0x12e564` (FACT)

```text
bd8fc  bl   0xbdf84
bd908  ldur x0, [x29,#-0x88]     ; EVP_PKEY* from parse
bd90c  bl   0x12d04c             ; key-method size → ~512 for RSA-4096
bd918  bl   malloc               ; output buffers
bd924  ldur x3, [x29,#-0x88]     ; SAME EVP_PKEY*
bd938  bl   0x12e564             ; x0=ctx, x1=out, x2=&len, x3=pkey
```

`0x12e564` prologue: `w1=#0x200` (512), keeps `x22=pkey`. Prior parent audit named this
**EVP_sign_finalize** (OPENSSL `pmeth_fn.c` / `pmeth_lib.c` tags).

### Same function: 16-byte digest path (FACT structure)

Immediately before the loader call: NEON XOR of 16 B → EVP digest update
(`0xd75f4` / `0xd7668` / `0xd78f0`, `w2=#0x10`, source tag `crypto/evp/digest.c`).

| Claim | Level |
|-------|-------|
| 16-byte block fed to digest ctx in this function | **FACT** |
| Byte-identical to SAS `MD5(challenge XOR pad)` | **STRONG** (matches reconstructed schema; not yet byte-traced end-to-end here) |

### Claim table (linkage)

| Claim | Level |
|-------|-------|
| Alias `com.bmwgroup.connected.bmw` passed into PFX loader | **FACT** |
| `PKCS12_parse` → `EVP_PKEY*` returned to caller | **FACT** |
| That pointer is `x3` of `0x12e564` | **FACT** |
| Key size path yields 512-capable output | **FACT** |
| This PFX key is the SAS APP_AUTH signer key | **VERY STRONG INFERENCE** (dataflow + cert/SPKI + field 8/8) |
| Innermost call inside `0x12e564` == `EVP_PKEY_sign` / RSA op | **NEXT** (prior audit already asserted; confirm callees `0x12a244`…`0x12ef34`) |

Field: **8/8** VERIFY vs APP_AUTH leaf (unchanged).

---

## Status ladder

| Layer | Status |
|-------|--------|
| SAS protocol / challenge / RSA params | CLOSED |
| Field 8/8 VERIFY | CLOSED |
| PFX location / structure / PBE / MAC | CLOSED |
| Local password + `PKCS12_parse` / shrouded unwrap | CLOSED |
| Key RSA-4096 e=3 + cert SPKI match | CLOSED |
| Alias → PFX loader `0xbdf84` | CLOSED |
| `EVP_PKEY*` → `0x12e564` (x3) | **CLOSED** |
| Keystore/TEE / remote key source | REJECTED |
| Deepest RSA/`EVP_PKEY_sign` inside `0x12e564` | **NEXT** |
| Same key in every `libaudio.so` build | UNKNOWN |
| PiDrive standalone SAS product-ready | OPEN (Weg B + policy) |

---

## Falsified / superseded

| Claim | Status |
|-------|--------|
| `0x19d860` / empty password explains SAS PFX | REJECTED |
| `0x51987` / `0x5210d` = SAS PFX | REJECTED |
| Password unknown / external | SUPERSEDED |
| Unwrap callsite unknown | SUPERSEDED |
| “Where is the key?” | CLOSED |
| `EVP_PKEY*` never shown entering sign-capable path | **SUPERSEDED** → enters `0x12e564` FACT |

---

## Next step

Resolve **inside** `0x12e564` only:

```text
0x12e564
  → 0x12a244 / 0xd79a8 / 0x12d04c / 0x13048c / 0x12ee9c / 0x130a68 / 0x12ef34
  → EVP_PKEY_sign / RSA private operation
```

Then the native chain is fully closed:

```text
PFX → pass → PKCS12_parse → EVP_PKEY → 16-B digest path → 0x12e564 → 512-B APP_AUTH
```

**Not next for product:** publishing credentials. Menu work remains **Weg A** until an
explicit Weg B decision.

Cross-links: [`README.md`](README.md) · [`FUNCTION-NOTES.md`](FUNCTION-NOTES.md) ·
bt-analyzer `SAS_STATUS_CRYPTO_CLOSED_20261120.md` · `SAS_SIGNER_CASE_A_CLOSED_20261119.md`
