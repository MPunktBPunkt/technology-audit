# Pack A–N Gesamtbericht — Auswertung (2026-11-23)

```yaml
parent: README.md
companion: PKCS12-ANATOMY.md
subject: claim hygiene after Pack A–N interim report
lib_sha256: 7bd16da13dc2662e505955425b16ce1facd78dbd81749356c3895d3f2b61ca90
status: archival evaluation — three chains must stay separated
product_next: NOT this path (Music/RHMI); binary O1–O6 = optional observe-only
```

## Urteil

Der Pack-A–N-Gesamtbericht ist als forensischer Zwischenstand brauchbar, vermischt aber an mehreren Stellen **zwei PKI-/Credential-Systeme**. Die entscheidende Korrektur (bereits in [`PKCS12-ANATOMY.md`](PKCS12-ANATOMY.md) rev. 2026-11-22e):

> Der eingebettete PFX ist **nicht** der APP_AUTH-/SAS-RSA-4096-Signer.

Damit wird „Paket O“ neu ausgerichtet: zuerst APP_AUTH-PKEY-Forensik (O1–O6), Credential-Provider erst danach (O7) — und **nicht** als Produktblocker.

---

## 1. Was der Bericht sicher zeigt — zwei getrennte Pfade

### System A — eingebetteter Feature-PFX

```text
PFX @ 0x5249e
   ↓ PKCS#12 → pkcs8ShroudedKeyBag → PBE/3DES → PrivateKeyInfo
   ↓ RSA-/RSA-PSS-Infrastruktur
```

| Claim | Level |
|-------|-------|
| Feature-PKI | **FACT** |
| RSA-1536 / `EVP_PKEY_size` = 192 | **FACT** |
| APP_AUTH-RSA-4096 | **REJECTED** |
| 512-Byte-SAS-Signer aus diesem PFX | **REJECTED** |

### System B — APP_AUTH/SAS

```text
AudioModule.g() → Challenge → MD5/XOR/MD5 → EVP_SignFinal → EVP_PKEY_sign
  → RSA path → 512-byte wire signature
```

Externe Evidenz: Lab **8/8**, Field **18/18**, Signatur **512 B**.

| Claim | Level |
|-------|-------|
| Wire-SAS = 512-Byte-Signaturen | **FACT** |
| SAS-Formel geschlossen | **FACT** |
| `AudioModule.g()` hat passenden lokalen Signaturpfad | **FACT** |
| Welcher RSA-4096-Private-Key im produktiven Pfad? | **OPEN** |
| Herkunft dieses Keys? | **OPEN** |

Diese Frage darf **nicht** über den Feature-PFX beantwortet werden.

---

## 2. Teil von Paket N — streichen

Bisherige Interpretation:

```text
PFX → PrivateKeyInfo → EVP_PKEY → F2103 → SAS
```

**streichen** als APP_AUTH-Kette.

Real bleibt die Binary-Kette `PFX → … → EVP_PKEY` (Feature).  
**REJECTED:** Feature-PFX `EVP_PKEY` → APP_AUTH SAS Signer.

Falsche Spur sauber eliminiert — gutes Ergebnis.

---

## 3. Was von Paket N wertvoll bleibt

Nicht: „APP_AUTH-Key aus diesem PFX“.  
Sondern: Credential-/Provider-Infrastruktur **unabhängig** davon:

```text
"PKCS12 import password" → F18c428 → Credential → PKCS#12-MAC
"PKCS8 decrypt password" → F18c428 → Credential → PKCS#8 decrypt
```

Echter Befund; beantwortet **nicht** automatisch die APP_AUTH-Key-Herkunft.

---

## 4–5. Paket O aufteilen

### O-A — Provider-Forensik (Fortsetzung N)

```text
F18c428 → F18ea00 → F18e76c → F190488/F190470 → VTable → Callback → Credentialquelle
```

Allgemeine Credential-Untersuchung — **nicht** APP_AUTH-Key-Suche.

### O-B — APP_AUTH-Signer-Forensik (eigentlich wichtig)

Ausgangspunkt `AudioModule.g` → MD5/XOR/MD5 → `F2103` ≈ `EVP_SignFinal` → `EVP_PKEY_sign`.  
Rückwärts: woher kommt der an `F2103` übergebene `EVP_PKEY*`?

---

## 6. Wichtigster neuer Test

Nicht zuerst „RSA-4096“ als String. Den an `EVP_SignFinal` übergebenen PKEY rekonstruieren:

`F2103` → pkey → type → RSA → modulus `n` → `BN_num_bits` / Match gegen Field APP_AUTH SPKI.

Bei Match: Feature-PFX für APP_AUTH irrelevant.

---

## 7. Drei unabhängige Ketten (kanonisches Modell)

| Kette | Inhalt | Status |
|-------|--------|--------|
| **1 Feature-PKI** | PFX → RSA-1536 → Feature Cert | **CLOSED** |
| **2 APP_AUTH/SAS** | Challenge → MD5/XOR/MD5 → RSA → 512 B | Wire crypto **CLOSED**; Signer-Key-Origin **OPEN** |
| **3 Credential Provider** | PKCS12/PKCS8 password labels → `F18c428` → Provider | Provider existiert **CLOSED**; Quelle **OPEN** |

Diese drei Ketten dürfen nicht wieder zusammengezogen werden.

---

## 8. Aus dem Gesamtbericht streichen / ändern

| Aussage | Aktion |
|---------|--------|
| eingebetteter PKCS#12-Key → APP_AUTH-Signer | **REJECTED** |
| 2376 Byte Keybag → RSA-4096 | **REJECTED** |
| PFX → PrivateKeyInfo → APP_AUTH EVP_PKEY | **REJECTED** / nicht belegt |
| 512-Byte-Signatur REMOVED_FROM_MODEL | **falsch** — Field FACT bleibt |

Richtig: `512 B SAS` = Field FACT; Feature PFX = RSA-1536; Feature PFX ≠ APP_AUTH signer.

---

## 9. Offene technische Lücken

| Frage | Status |
|-------|--------|
| SAS-Formel | CLOSED |
| SAS-Wire-Signatur 512 B | CLOSED |
| Feature-PFX als separates System | CLOSED |
| Credential Provider existiert | CLOSED |
| konkrete Credentialquelle | OPEN |
| APP_AUTH-PKEY im Signaturpfad | OPEN |
| APP_AUTH-Keygröße (native) | OPEN |
| APP_AUTH-Modulus = Feld-SPKI | OPEN |
| Herkunft APP_AUTH-Private-Key | OPEN |

Wichtigste Untersuchung: **APP_AUTH-PKEY → Modulus-Match**.

---

## 10. Empfohlene Reihenfolge (optional binary, nicht Produkt-Next)

Nicht „Paket O Provider“ als Ganzes zuerst.

1. **O1** — `F2103` / `EVP_SignFinal`-Aufruf vollständig  
2. **O2** — Herkunft des übergebenen `EVP_PKEY*`  
3. **O3** — PKEY-Typ (RSA / RSA-PSS)  
4. **O4** — RSA-Größe via Objekt/`BN_num_bits`, nicht Containergröße  
5. **O5** — Binary-Modulus ↔ Field APP_AUTH SPKI  
6. **O6** — `0x02000000` MD5/XOR/MD5 mit produktivem Sign-Pfad verbinden  
7. **O7** — erst danach Credential Provider (`F18c428` → VTable → Quelle)

Zielzustand nach O1–O6: produktive `EVP_PKEY` = RSA-4096, gleicher Modulus wie Field-Cert, Prep + `EVP_SignFinal` verbunden. Erst dann: woher bekommt dieser PKEY den Private Key?

**STOP:** kein Passphrase-/Private-Key-Dump; kein PW-Brute.

---

## Produkt vs. Audit

- **bt-analyzer Produkt-Next:** Music NP spine / RHMI — Crypto Gate A+B CLOSED.  
- **Dieses Dokument:** Claim-Hygiene + optionale Binary-Backlog (O1–O6).  
- **Kein neues Parallel-Audit nötig**, solange PKCS12-ANATOMY + diese Auswertung die Trennung tragen; O1–O6 nur bei Bedarf als Fortsetzung **dieses** Audits.
