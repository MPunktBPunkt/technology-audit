# FIELD-CROSSWALK

Ziel: Gibt es eine **identifizierbare lokale Komponente**, die die Feld-Response erzeugt?  
Nicht: Byte-für-Byte Reproduktion.

| Field | Phone implementation | Status |
|-------|----------------------|--------|
| 16-B Challenge | `_result_sas_certificate` → Kit `signChallenge(challenge)` Input | **MATCH** FACT/FIELD |
| XOR | Doc + `PrivateKeyHandling`; DEX string `XOR` / Status XOR | **Algorithm MATCH**; executor inside `libaudio` **INFERENCE** |
| MD5 | `md5WithRSA` / `md5WithRSAEncryption` in `libaudio.so` | **MATCH** naming FACT |
| RSA | OpenSSL RSA in `libaudio.so`; Feld CN `…TouchCommand_Connection…` | **MATCH** component + prior key identity SUPPORTS |
| 512-B Signature | `AudioModule.g` / `libaudio.so` return | **Size MATCH** FIELD; **producing `.so` IDENTIFIED** FACT |
| 559-B sas_login frame | BCL + Etch wrap outside signer | **MATCH** FIELD forensic |

## Identifizierbare Komponente?

| Kandidat | Identifiziert? |
|----------|----------------|
| Kit `SecurityAccess` | ja — ruft nur OEM |
| Classic Binder service | Interface ja (prior) |
| MyBMW `SecurityModule` | ja — Java wrapper |
| MyBMW `AudioModule` | ja — `native` JNI surface |
| Konkrete `.so` | **ja — `libaudio.so`** |

**Antwort:** Die Feld-Response wird auf dem Phone in **`libaudio.so`** (`Java_…_AudioModule_g`) erzeugt, erreicht über `SecurityModule.signChallenge` (Reflect) bzw. denselben Pfad hinter `CarSecurityService`.

## Fallmatrix Update

| Fall | Status nach diesem Lauf |
|------|-------------------------|
| A | **STRONG INFERENCE** (OpenSSL private-key load in `libaudio`); exact asset/path **UNKNOWN** |
| B | **UNLIKELY** for signChallenge (no Keystore evidence in `libaudio`) |
| C | Classic outer FACT; MyBMW Binder = thin wrapper → same native (**FACT**) |
| D | **CONFIRMED** |
