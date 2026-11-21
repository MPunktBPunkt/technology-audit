# PKCS#12 Anatomy Addendum (2026-11-21)

```yaml
parent: README.md
subject: embedded PKCS#12 @ 0x5249e (len 0x10f2 / 4338 B) in libaudio.so
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
scope: DER inventory + epistemic levels — observe-only
status: FACT for PBE parameters; passphrase origin still OPEN/INFERENCE
```

## Verdict

The embedded bag’s **PBE parameters are now inventory-FACT**. Empty/NULL passphrase is
**REJECTED** via MAC fail. The remaining gap is **not** “unknown crypto”, but
**“where does the passphrase string come from?”** — until a register observation at
`PKCS12_parse` promotes Alias↔PKCS#12 / password origin to FACT.

**STOP:** no shrouded-key decrypt, no private-key export, no passphrase brute-force tooling
in this audit.

---

## DER / PBE inventory (FACT)

| Item | Value | Level |
|------|-------|-------|
| Blob VA / length | `0x5249e` / `0x10f2` (4338 B) | FACT (prior README) |
| Salt | `8d6188b36bf04974` | FACT (DER) |
| Iteration count | **1** | FACT (DER) |
| Ciphertext size | 2376 B | FACT (DER) |
| PBE | SHA-1 + 3-Key TripleDES-CBC (OpenSSL PKCS#12 KDF convention) | FACT (OID + prior) |
| MAC check | HMAC-SHA1, iter=1 over MAC bytes in `macData` | FACT (structure) |

Offline verify shape (documentation only — not an attack procedure):

```text
candidate → PKCS12-KDF(SHA1, salt, iter=1) → Key+IV
         → 3DES-CBC decrypt → MAC-Check (HMAC-SHA1, iter=1)
```

MAC check alone can accept/reject a candidate without decoding the 2376 B payload.

**Iter=1 ⇒ KDF cost per candidate is negligible (FACT-Mathematik).**  
“Therefore the passphrase is easily found in practice” remains **INFERENCE** until a
source string is observed — not a license to brute-force.

---

## Empty / NULL passphrase

| Claim | Level |
|-------|-------|
| Empty / NULL passphrase unlocks the bag | **REJECTED** (MAC fail — FACT, given macData offset identified) |
| A real passphrase exists (not OpenSSL null-vs-`""` quirk alone) | **STRONG** from REJECT |

---

## Call hotspot (INFERENCE until PLT)

Static chain of interest (init / unwrap path — not every step is password prep):

```text
… → 0xbc7ec → 0xc8484 → 0x167184
      (context: AudioModule_a → 0xbc7b4 → 0xbe448 → PKCS#12 parse @ blob)
```

| Address | Plausible role | Level |
|---------|----------------|-------|
| `0xbe448` | Wrapper: blob pointer + length + password argc → `PKCS12_parse` | INFERENCE (prior FUNCTION-NOTES) |
| `0xc8484` | Intermediate (possibly decrypt/`PKCS12_item_decrypt_d2i` path) | INFERENCE |
| `0x167184` | Password provenance candidate: (a) encrypted string pool, (b) derived bytes, (c) forward from above | **INFERENCE** |

Do **not** treat the hotspot chain as proven password preparation without wire/register proof.

### Preferred next observation (observe-only)

Break at the **PLT call to `PKCS12_parse`** and capture **password string pointer + length**
(registers conventionally carrying the passphrase arg — e.g. r1/r2 / x1/x2 depending on ABI
of the linked OpenSSL). One clean hit decides (a)/(b)/(c) and can promote
**Alias↔PKCS#12** from INFERENCE → FACT — **without dumping the private key**.

---

## Claim table (canonical)

| Claim | Level |
|-------|-------|
| Salt / Iter=1 / Ciphertext 2376 B / SHA1-3DES-PBE | **FACT** (DER inventory) |
| Empty/NULL password | **REJECTED** (MAC fail — FACT) |
| Password from `0x167184` chain | **INFERENCE** until PLT registers |
| Iter=1 ⇒ offline MAC test is cheap (math) | **FACT**; “trivial in practice” = **INFERENCE** |
| Passphrase is a known ASCII literal / “FUSS”-style string | **UNKNOWN** |
| PiDrive can standalone-sign without MyBMW | **OPEN** (unchanged — anatomy ≠ signer) |

---

## Relation to SAS / Weg B

- SAS **challenge formula** and Gate B Accept remain **CLOSED** elsewhere.
- This addendum only narrows the **embedded PKCS#12 unlock** gap for a future
  Standalone-Signer (Weg B).
- Until passphrase origin is FACT **or** Weg A (ride authenticated session) is used,
  “PiDrive authenticates alone” stays **OPEN**.

Cross-links:

- Parent: [`README.md`](README.md) §F Remaining Gap  
- Notes: [`FUNCTION-NOTES.md`](FUNCTION-NOTES.md)  
- bt-analyzer: `docs/analysis/SAS_STATUS_CRYPTO_CLOSED_20261120.md`  
- bt-analyzer: `docs/analysis/SAS_SIGNER_CASE_A_CLOSED_20261119.md`
