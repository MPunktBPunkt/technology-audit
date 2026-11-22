# PKCS#12 / Crypto-Systems Addendum (rev. 2026-11-22e)

```yaml
parent: README.md
subject: libaudio.so crypto systems — Feature-PKI vs APP_AUTH/SAS
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
build_id: cf781dbc8425a5fe2cbbd02be5cfc7630398301f
elf: AArch64, stripped, size 1981072
scope: separate Feature Certificate PFX from APP_AUTH RSA-4096
status: >
  Feature-PKI (PFX @ 0x5249e, RSA-1536) CLOSED as its own system.
  Prior claim "this PFX is the APP_AUTH RSA-4096 signer key" REJECTED.
  APP_AUTH native PKEY + MD5/XOR/MD5 site + createSecurityContext = OPEN.
  Field SAS formula remains FACT (wire). Credentials withheld.
```

## Verdict (corrected)

Three **different** crypto layers must stay separated:

| Layer | What | APP_AUTH? |
|-------|------|-----------|
| **1. Feature Certificate PKI** | X.509 @ `0x51987` (RSA-**1536**) + PFX @ `0x5249e` + BMW pass decoder + `PKCS12_parse` + `EVP_SignFinal` (~**192** B) | **NO** |
| **2. Generic OpenSSL CMS/PKCS#7** | `EVP_PKEY_decrypt`, CMS `cms_sd.c`, many `EVP_SignFinal`/`EVP_PKEY_sign` sites | **NO** |
| **3. BMW Security / SAS APP_AUTH** | Must use RSA-**4096**, field prep `MD5(LE32(0x02000000))→XOR→MD5→PKCS#1`, 512 B sig | **OPEN** (native site) |

> **REJECTED (supersedes 2026-11-22b–d overclaim):**  
> «Embedded PKCS#12 @ `0x5249e` is the RSA-4096 APP_AUTH private key.»

It is the **Feature Certificate** shrouded key (RSA-1536).  
`EVP_PKEY_size` on that path = **192**, not 512.

**STOP:** no passphrase / private key in this repo.

---

## Field SAS (unchanged FACT)

Wire / field (F20):

```text
CertificateType 0x02000000 LE → MD5 → 16-B pad
  → Challenge XOR pad → MD5 → RSA-4096 PKCS#1 v1.5 → 512 B
```

Verified **8/8** against APP_AUTH leaf public key. Keystore/TEE / remote-only signer
**REJECTED** as primary source (field + prior CASE A). Binary must still locate the
**native** producer of that RSA-4096 `EVP_PKEY` and the prep block.

---

## Layer 1 — Feature Certificate + PFX (CLOSED as Feature-PKI)

### Certificates

| Item | Value |
|------|-------|
| Feature cert VA | `0x51987` (~969 B) |
| CN | `a4a_app_Android_FeatureCertificate_PIA_KML_VOICE_00.00.01` |
| Serial | `0x1BB` |
| Public key | **RSA-1536** |
| Extensions (excerpt) | `SAS.CertificateType=APP`, CDS/AVS/RHMI/… |
| Cert SHA-256 | `8C3359B8…3E3C1CAD` |
| SPKI SHA-256 | `c00b5bac4b136d50a404d58f1bd03e3cbe5d448d959e7c7aa9e95f93284baa98` |
| Nearby | `0x5210d` ~913 B self-signed BMW A4A root |

### PFX @ `0x5249e` / `0x10f2`

Same DER inventory as before (BER `30 80`, one `pkcs8ShroudedKeyBag`, two PBE salts
iter=1, MAC salt `38dbae…`, empty pw REJECTED). Belongs to **this Feature system**.

### Loader `0xbdf84` (FACT)

Called from `AudioModule_e` / `AudioModule_f` with alias
`com.bmwgroup.connected.bmw` (`0x407df`). Password via Base64-ish decode (`0xbe458`)
+ BMW deobfuscator (`0xbe59c`, XOR `0x17` + LUT @ `0x1e9af0`) → `PKCS12_parse`
(`0x164988`) → `EVP_PKEY` / `X509` / CA stack; password wiped after.

### Feature sign path (FACT — not APP_AUTH)

```text
AudioModule_f → 0xbdf84 → EVP_PKEY (RSA-1536)
  → EVP_PKEY_size (0x12d04c) = 192
  → EVP_SignFinal (0x12e564) @ bd938
```

| Claim | Level |
|-------|-------|
| This PFX/key signs in Feature path | **FACT** |
| This is APP_AUTH / 512-B SAS | **REJECTED** |

---

## Layer 2 — OpenSSL wrappers (do not confuse with BMW SAS)

| Addr | Role | APP_AUTH? |
|------|------|-----------|
| `0x12e564` | **`EVP_SignFinal`** (calls `EVP_PKEY_sign` @ `0x12ef34`) | infrastructure FACT; site decides |
| `0x12d04c` | `EVP_PKEY_size` | — |
| `0x13048c` | `EVP_PKEY_CTX_new` | — |
| `0x12ee9c` | `EVP_PKEY_sign_init` | — |
| `0x130a68` | `EVP_PKEY_CTX_ctrl` | — |
| `0x12ef34` | `EVP_PKEY_sign` | — |
| `0xf247c` / `0xf2408` | CMS (`crypto/cms/cms_sd.c`) | **REJECTED** as APP_AUTH |
| `0x168374` | **`EVP_PKEY_decrypt`** / PKCS#7 (`pk7_doit.c`, OAEP strings) | **REJECTED** as APP_AUTH |
| `mov w9,#0x200` in that context | PKEY method control, **not** sig length 512 | **REJECTED** as RSA-4096 proof |
| `0x168920` | another `EVP_SignFinal` site | UNKNOWN / not proven APP_AUTH |
| `0x19e494` | `EVP_SignFinal` with external `EVP_PKEY*` | **interesting candidate**, APP_AUTH **UNKNOWN** |

---

## Layer 3 — APP_AUTH / SAS (OPEN)

Still missing as a **united** native proof:

1. RSA-**4096** `EVP_PKEY` whose modulus matches the field APP_AUTH public key  
2. Adjacent prep: `0x02000000` → MD5 → XOR challenge → MD5  
3. Sign → 512 B  

Highest-probability entry: string **`createSecurityContext`**
(“Error while calling native function createSecurityContext”) → security object
(cert + key + SAS params + sign).

```text
createSecurityContext
  → Native Security Object
  → EVP_PKEY (size 512?) + CertificateType + sign
```

Prior 2026-11-22d narrative that closed APP_AUTH E2E via Feature PFX +
`AudioModule.g`/`0xbd73c` MD5/XOR path is **superseded / under re-audit**: that
material mixed Feature-PKI facts with APP_AUTH aspirations. Re-bind only after
modulus match + prep co-location.

---

## Status ladder

| Layer | Status |
|-------|--------|
| Field SAS formula + 8/8 VERIFY | CLOSED (wire) |
| Feature cert + PFX + local pass + parse + Feature `EVP_SignFinal` | CLOSED (Feature-PKI) |
| OpenSSL `EVP_SignFinal` / `EVP_PKEY_sign` / CMS / PKCS#7 decrypt IDs | CLOSED (infra) |
| PFX @ `0x5249e` = APP_AUTH RSA-4096 | **REJECTED** |
| `0x168374` = APP_AUTH | **REJECTED** |
| Native APP_AUTH PKEY load | **OPEN** |
| Native SAS MD5/XOR/MD5 co-located with that PKEY | **OPEN** |
| `0x19e494` = APP_AUTH | UNKNOWN |
| `createSecurityContext` chain | **OPEN** (priority) |
| PiDrive standalone SAS product-ready | OPEN |

---

## Next step

Do **not** broaden-hunt more RSA wrappers.

1. Resolve **`createSecurityContext`** → security object → `EVP_PKEY*`  
2. Require `EVP_PKEY_size == 512` and modulus ↔ APP_AUTH SPKI fingerprint  
3. Find prep `CertificateType` / MD5 / XOR next to that sign call  
4. Keep Feature-PKI documented but **out of** the APP_AUTH claim set  

**Product:** Weg A / Music RHMI unchanged; Weg B waits on Layer-3 closure.

Cross-links: [`README.md`](README.md) · [`FUNCTION-NOTES.md`](FUNCTION-NOTES.md) ·
bt-analyzer `SAS_STATUS_CRYPTO_CLOSED_20261120.md` · `SAS_SIGNER_CASE_A_CLOSED_20261119.md`
