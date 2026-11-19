# FIELD-CROSSWALK

Ziel: Gibt es eine **identifizierbare lokale Komponente**, die die Feld-Response erzeugt?  
Nicht: Byte-für-Byte Reproduktion.

| Field | Phone implementation | Status |
|-------|----------------------|--------|
| 16-B Challenge | `_result_sas_certificate` → Kit `signChallenge(challenge)` Input | **MATCH** (size + sequencing) FACT/FIELD |
| XOR | Doc + `PrivateKeyHandling` for APP_AUTH | **Algorithm MATCH** FACT; **executor component UNKNOWN** (no APK) |
| MD5 | part of `MD5withRSA` / XOR helper | same |
| RSA | RSA-4096 APP_AUTH | same; Feld CN `…TouchCommand_Connection…` SUPPORTS key identity |
| 512-B Signature | OEM `signChallenge` return; Classic/Module tests 512 B, first byte `0x15` on fixed challenge | **Size MATCH** FACT; **producing `.so`/class UNKNOWN** |
| 559-B sas_login frame | 8 BCL + 8 DEADBEEF + 30 Etch + 512 RSA + 1 END | **MATCH** FIELD forensic — wrapping outside signer |

## Identifizierbare Komponente?

| Kandidat | Identifiziert? |
|----------|----------------|
| Kit `SecurityAccess` | ja — ruft nur OEM |
| Classic Binder service | Interface ja; Implementierung nein |
| MyBMW `SecurityModule` | Klassenname ja; Bytecode/native nein |
| Konkrete `.so` | **nein** |

**Antwort:** Die Response wird von einer **OEM-Phone-Komponente hinter** `SecurityModule`/`ICarSecurityService` erzeugt — lokal auf dem Gerät. Die **genaue** Bibliothek/Klasse unterhalb dieser Grenze ist in diesem Lauf **nicht** identifiziert (APK fehlt).

## Fallmatrix Update

| Fall | Status nach diesem Lauf |
|------|-------------------------|
| A | UNKNOWN |
| B | UNKNOWN |
| C | Classic outer: FACT; MyBMW inner: UNKNOWN |
| D | **STRONG INFERENCE** — not CONFIRMED |
