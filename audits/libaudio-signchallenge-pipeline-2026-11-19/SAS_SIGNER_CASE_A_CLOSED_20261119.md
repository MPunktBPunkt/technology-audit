# SAS Signer CASE A — consolidation (2026-11-19/20)

```yaml
audit: libaudio-signchallenge-pipeline-2026-11-19
status: CASE A closed for client sign architecture
companion_product_docs: esp32.bt-analyzer docs/analysis/SAS_SIGNER_CASE_A_CLOSED_20261119.md
```

This file consolidates claim hygiene that belongs next to the audit README so shared repos do not depend on unpushed product-tree notes.

## Crypto (FACT)

```text
pad16  = MD5(cert_serial_u32)     # 4-byte BE serial → 16 B pad
xored  = challenge[16] XOR pad16
digest = MD5(xored)
sig    = RSA EVP_PKEY_sign(digest) → typically 512 B
```

Do **not** write “XOR with cert_serial.”

## Key source

| Claim | Class |
|-------|-------|
| Embedded PKCS#12 @ `0x5249e` / `pkcs8ShroudedKeyBag` | **FACT** |
| PKEY lookup `"com.bmwgroup.connected.bmw"` | **FACT** |
| Alias ↔ embedded PKCS#12 identity | **INFERENCE** |
| Keystore / TEE / Binder / `/data/Asset` on sign path | **REJECTED** |
| VIN-derived private key | **not evidenced** (incompatible with fixed-VA universal APK binary) |
| PKCS#12 passphrase / unwrap | **UNKNOWN** — **STOP** |

## Dual gate

```text
(A) Sign mechanism  FACT
(B) HU acceptance   OPEN
```

## Preferred next step

**Test A** — B3/wire: capture `serial_u32` + `challenge[16]` (+ login sig), verify pad recipe. No key extraction.  
Optional: dynamic observe-only for alias↔PKCS#12 promotion.

## Product tooling (esp32.bt-analyzer)

- `tools/sas_pad_crosscheck.py`
- `tools/b3_rfcomm_relay.py` → `etch.sas` fields
- `tools/etch_codec.py` → `extract_pkcs7_cert_serials` / `summarize_sas_wire_fields`
