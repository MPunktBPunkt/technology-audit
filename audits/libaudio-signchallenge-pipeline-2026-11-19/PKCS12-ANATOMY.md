# PKCS#12 Anatomy Addendum (2026-11-21 / revised 2026-11-22)

```yaml
parent: README.md
subject: embedded PKCS#12 @ 0x5249e (len 0x10f2 / 4338 B) in libaudio.so
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
build_id: cf781dbc8425a5fe2cbbd02be5cfc7630398301f
elf: AArch64, stripped, size 1981072
scope: DER inventory + call-path corrections — observe-only
status: PFX location/structure/PBE CLOSED; password + unwrap callsite OPEN
```

## Verdict

The SAS private key is **structurally found** as an embedded `pkcs8ShroudedKeyBag`
inside PKCS#12 @ `0x5249e`. It is **not** plaintext in the .so.

The remaining gap is narrow and explicit:

> How does `libaudio.so` unwrap that shrouded bag (passphrase origin + exact
> `PKCS12_*` / `EVP_PKCS82PKEY` callsite)?

**STOP:** no shrouded-key decrypt, no private-key export, no passphrase brute-force
tooling in this audit.

---

## Binary identity (FACT)

| Item | Value |
|------|-------|
| Path | MyBMW ROW `libaudio.so` (arm64-v8a) |
| Size | 1 981 072 B |
| SHA-256 | `7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90` |
| Build ID | `cf781dbc8425a5fe2cbbd02be5cfc7630398301f` |
| ELF | AArch64, stripped |

---

## Embedded PFX (FACT)

| Item | Value |
|------|-------|
| VA / length | `0x5249e` / `0x10f2` (4338 B) |
| Code load | `0xbe448`: `adr x0,#0x5249e` ; `mov w1,#0x10f2` ; `b 0xca93c` |
| Structure | PKCS#12 v3, BER `30 80`, AuthenticatedSafe |
| Key bag | exactly one `pkcs8ShroudedKeyBag` |
| Also | `pkcs7-data`, `pkcs7-encryptedData` |
| Metadata (printable) | e.g. `app_BMWTouchCommand_Connection_00.00.010` + PKCS#9 attrs |

---

## PBE + MAC inventory (FACT)

PBE: `pbeWithSHA1And3-KeyTripleDES-CBC` (×2 content areas), OpenSSL PKCS#12 KDF.

| Region | Salt | Iter |
|--------|------|-----:|
| PBE #1 | `8d 61 88 b3 6b f0 49 74` | **1** |
| PBE #2 | `4b 7f 30 5e 4f 95 97 33` | **1** |
| **MAC** (SHA-1) | `38 db ae 69 8b 76 e6 56` | **1** |

MAC digest length 20 B. Empty / NULL-style password → MAC verify fail
(`invalid password?`) → empty password **REJECTED**.

**Note:** MAC salt ≠ PBE salts. Earlier single-salt shorthand was incomplete.

Iter=1 ⇒ KDF cost per candidate is negligible (**FACT-math**).  
“Passphrase is therefore easy to find” remains **INFERENCE/UNKNOWN** — obvious
string candidates (`""`, `password`, `changeit`, `bmw`, `BMW`,
`com.bmwgroup.connected.bmw`, …) did **not** succeed (report 2026-11-22).

---

## Init path corrections (FACT / REJECTED)

```text
AudioModule_a / init
  → 0xbc7ec  bl 0xbe448          ; load pointer+len of embedded PFX
  → 0xbe448  → 0xca93c           ; resource/blob registration
  → 0xbc808  bl 0xc8484
  → 0xbc814  bl 0x167184         ; generic resource/container consumer
```

| Claim | Level |
|-------|-------|
| `0xbe448` passes `0x5249e` / `0x10f2` into `0xca93c` | **FACT** |
| `0xca93c` = resource / blob **registration** (ingest), not PKCS#12 parse | **FACT** (revised) |
| `0xca93c` decrypts / parses the PFX | **REJECTED** |
| `0x167184` (via `0xe6cb4` → `0xbf3c8`/`0xbf4b0`) = generic container consumer | **FACT** (revised) |
| `0xbe448 → … → 0x167184` ≡ `PKCS12_parse` / unwrap | **REJECTED** |
| Embedded OpenSSL has `PKCS12_parse`, `PKCS12_verify_mac`, `PKCS12_item_decrypt_d2i`, `EVP_PKCS82PKEY`, … | **FACT** (symbols/strings) |
| Exact unwrap callsite for **this** PFX located | **OPEN** |

Prior wording “`0xbe448` → parsed crypto state via `0xca93c`” is **superseded**:
registered/ingested resource state, not proven parse/unwrap.

---

## Signing path (CLOSED — cross-ref)

Unchanged; see parent README + SAS status docs:

```text
signChallenge → AudioModule.g → native_sign_impl
  → pad MD5(0x02000000) XOR challenge → MD5 → EVP_PKEY_sign
  → RSA-4096 PKCS#1 v1.5 DigestInfo-MD5 → 512 B
```

Field: **8/8** RSA-VERIFY against APP_AUTH leaf. Alias string
`com.bmwgroup.connected.bmw` present (**FACT**); bind to this PFX/EVP_PKEY =
**INFERENCE** until runtime/static closure.

---

## Falsified assumptions (REJECTED)

| Assumption | Status |
|------------|--------|
| Android Keystore / TEE is SAS private-key source | **REJECTED** |
| Remote BMW server required for the RSA sign itself | **REJECTED** (for this path) |
| `0x19d860` / `x1=xzr` proves NULL password for **this** SAS PFX | **REJECTED** (other resource/cert path) |
| Feature-certificate Base64/XOR path = PKCS#12 password | **REJECTED** (not shown) |
| `0xca93c` parses/decrypts PFX | **REJECTED** |
| `0x167184` is the PFX unwrap | **REJECTED** |

---

## Status ladder

| Layer | Status |
|-------|--------|
| SAS protocol / challenge / RSA params | CLOSED |
| Local signer (`EVP_PKEY_sign`) | CLOSED |
| Field signature verify 8/8 | CLOSED |
| PFX location + structure | CLOSED |
| `pkcs8ShroudedKeyBag` present | CLOSED |
| PBE algorithm + salts + iter=1 + MAC | CLOSED |
| Empty password | REJECTED |
| PFX password / derivation | **OPEN** |
| Exact `PKCS12_*` unwrap callsite for this blob | **OPEN** |
| `EVP_PKCS82PKEY` / EVP_PKEY binding | **OPEN** |
| Alias ↔ this PFX | INFERENCE |
| PiDrive standalone SAS | **OPEN** (Weg B) |

---

## Next step (observe-only)

Do **not** more password guessing as primary method.

Locate the AArch64 call that passes a **password pointer** into
`PKCS12_verify_mac` / `PKCS12_item_decrypt_d2i` / `PKCS12_parse` for the
`0x5249e` bag (PLT break + registers). Then classify origin:

- static embed  
- derived from other credential material  
- alias/cert-derived  
- runtime resource  
- computed by another native function  

No key dump required for that classification.

---

## Relation to product

- Closes “where is the key?” → opens “how is it unwrapped?”
- Does **not** close Weg B Standalone-Signer.
- PiDrive menu work stays on **Weg A** / Music RHMI; this audit is optional Weg B prep.

Cross-links: [`README.md`](README.md) · [`FUNCTION-NOTES.md`](FUNCTION-NOTES.md) ·
bt-analyzer `SAS_STATUS_CRYPTO_CLOSED_20261120.md` · `SAS_SIGNER_CASE_A_CLOSED_20261119.md`
