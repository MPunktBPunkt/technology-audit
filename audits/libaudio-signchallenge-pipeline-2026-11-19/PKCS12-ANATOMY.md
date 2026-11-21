# PKCS#12 Anatomy Addendum (2026-11-21 → rev. 2026-11-22b)

```yaml
parent: README.md
subject: embedded PKCS#12 @ 0x5249e in libaudio.so
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
build_id: cf781dbc8425a5fe2cbbd02be5cfc7630398301f
elf: AArch64, stripped, size 1981072
scope: key-origin architecture — observe/document only
status: >
  PFX + local password reconstruction + PKCS12_parse/verify_mac + shrouded unwrap
  CLOSED as architecture FACT; plaintext passphrase/key NOT published;
  EVP_PKEY* identity into EVP_PKEY_sign still OPEN (strong INFERENCE via cert/SPKI)
```

## Verdict

> **Where does the private key come from?** → answered: embedded PFX in `libaudio.so`,
> locally deobfuscated passphrase, OpenSSL `PKCS12_parse` / PBE unwrap → RSA-4096
> `EVP_PKEY`. Not HU, not server, not Keystore/TEE.

Remaining RE gap is **object lifetime / callgraph**:

```text
EVP_PKEY* from PKCS12_parse  ──?──►  EVP_PKEY* used by native_sign_impl / EVP_PKEY_sign
```

That is no longer a cryptography gap.

**STOP (repo hygiene):** do **not** commit plaintext passphrase, PKCS#8, or usable private
key material to this audit. Architecture + addresses + public cert fingerprints only.

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

## SAS signer linkage

Known sign path (parent audit / SAS docs):

```text
signChallenge → AudioModule.g → native_sign_impl → EVP_PKEY_sign
  → pad MD5(0x02000000) XOR challenge → MD5 → RSA-4096 PKCS#1 → 512 B
```

Field: **8/8** VERIFY vs APP_AUTH leaf.

| Claim | Level |
|-------|-------|
| This PFX/cert is TouchCommand APP_AUTH-shaped material | **FACT** |
| This key is the one used by SAS `EVP_PKEY_sign` | **STRONG INFERENCE** (cert + wire verify + co-location) |
| Exact `EVP_PKEY*` from `PKCS12_parse` ≡ pointer at `EVP_PKEY_sign` | **OPEN** |

---

## Status ladder

| Layer | Status |
|-------|--------|
| SAS protocol / challenge / RSA params | CLOSED |
| Local `EVP_PKEY_sign` path | CLOSED |
| Field 8/8 VERIFY | CLOSED |
| PFX location / structure / PBE / MAC | CLOSED |
| Local password reconstruction + MAC | CLOSED |
| `PKCS12_parse` / `verify_mac` / shrouded unwrap | CLOSED |
| Key RSA-4096 e=3 + cert SPKI match | CLOSED |
| Keystore/TEE / remote server as key source | REJECTED |
| `EVP_PKEY*` identity into signer | **OPEN** |
| Same key in every `libaudio.so` build | **UNKNOWN** (not compared) |
| PiDrive standalone SAS product-ready | **OPEN** (Weg B; pointer proof + policy) |

---

## Falsified / superseded

| Claim | Status |
|-------|--------|
| `0x19d860` / empty password explains SAS PFX | REJECTED |
| `0x51987` / `0x5210d` = SAS PFX | REJECTED |
| Password unknown / external | **SUPERSEDED** → local reconstruct + MAC FACT |
| Unwrap callsite unknown | **SUPERSEDED** → `0x164988` / `0x165b74` FACT |
| “Where is the key?” | **CLOSED** |

---

## Next step

Close object graph only:

```text
PKCS12_parse → EVP_PKEY*
      → storage / global / context field
      → native_sign_impl lookup
      → EVP_PKEY_sign
```

Relevant helpers: `EVP_PKCS82PKEY`, `EVP_PKEY_assign_RSA`, context table @ prior
`0x1eb108` / alias `com.bmwgroup.connected.bmw` (alias bind still INFERENCE).

**Not next for product:** publishing credentials; using this material as default PiDrive
auth. Menu work remains **Weg A** until an explicit Weg B decision.

Cross-links: [`README.md`](README.md) · [`FUNCTION-NOTES.md`](FUNCTION-NOTES.md) ·
bt-analyzer `SAS_STATUS_CRYPTO_CLOSED_20261120.md` · `SAS_SIGNER_CASE_A_CLOSED_20261119.md`
