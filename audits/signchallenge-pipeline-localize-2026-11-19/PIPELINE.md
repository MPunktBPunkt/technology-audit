# signChallenge() Pipeline — Lokalisierung A–D

## Bekannte Pipeline (ohne Key-Ort)

```text
16 B Challenge  (HU → Phone, Etch _result_sas_certificate)
      │
      ▼
OEM Security entry
  Classic:  ICarSecurityService.signChallenge(handle, challenge)   [Binder]
  MyBMW:    SecurityModule.signChallenge(handle, challenge)        [in-process reflect]
      │
      ├── createSecurityContext(packageName, appName)
      │     loads P7B / prepares JNI (Analysis FACT)
      │
      ▼
[NATIVE — Hypothese D]  „native function signChallenge“ (Kit Test FACT)
      │
      ├── preprocess (APP_AUTH): challenge ⊕ MD5(02 00 00 00)   [Doc + PrivateKeyHandling]
      ├── digest/sign: MD5withRSA with APP_AUTH private key     [Doc + Kit]
      └── output: 512 B signature                               [Tests + Feld]
      │
      ▼
sas_login(512 B) → Wire frame 559 B (BCL+Etch wrapping)         [Feld MEASURED]
```

### Was feststeht (Algorithmus / Format)

| Frage | Antwort | Klassifikation | Quelle |
|-------|---------|----------------|--------|
| Input exakt? | 16 Bytes raw challenge | FACT + FIELD | Kit comment; DEEP_FORENSIC |
| Hashing / Preprocess? | XOR mit MD5(LE u32=2) bei APP_AUTH | FACT | Analysis `authentication.md`; `PrivateKeyHandling.signChallenge(applyXor=true)` |
| Padding / Algorithmus? | `MD5withRSA` (Java Name) | FACT (recon) | same |
| Rückgabeformat? | 512 B raw RSA-4096 signature bytes | FACT + FIELD | Classic/Module tests; Feld 512 in 559-Frame |
| Zertifikatsbindung? | Public key = APP_AUTH leaf; CN enthält `connection` | FACT + FIELD | CertMangling; Feld CN TouchCommand_Connection |
| Determinismus? | Gleiche Challenge → gleiche Response (Tests first byte `0x15`) | FACT (E4) | TestSecurityAccess/Module |
| Context-Abhängigkeit Signatur? | Analysis: Response „isn't dependent on previous setup values“ (nach Context-Init) | FACT (Doc) | authentication.md |

### Was **nicht** feststeht (Schlüsselort)

| Frage | Stand |
|-------|-------|
| Schlüsselquelle (APK asset / PKCS12 / Keystore / TEE / OEM service) | **UNKNOWN** |
| Hardware/TEE? | **UNKNOWN** |
| Welche `.so`? | **UNKNOWN** |
| MyBMW vs Classic gleiche native Lib? | **UNKNOWN** |
| Zusätzlicher Binder hinter SecurityModule? | **UNKNOWN** |

---

## Fallmatrix A–D

| Fall | Beschreibung | Aktuelle Evidence | Stand |
|------|--------------|-------------------|-------|
| **A** | Schlüssel liegt softwareseitig im APK/Package (ladbar) | Dev-P12 + `PrivateKeyHandling` beweisen nur **Rekonstruktionspfad**; Produktions-APP_AUTH-Key **nicht** öffentlich | **möglich**, unbewiesen |
| **B** | SecurityModule → Android Keystore / KeyMint / TEE | Kein Kit-Code, kein Trace | **UNKNOWN** |
| **C** | SecurityModule → weiterer OEM-/Vendor-Binder | Classic **ist** bereits Binder (Fall C-ähnlich an App-Grenze); MyBMW in-process — innerer Binder **UNKNOWN** | Classic: äußere IPC FACT; innere: UNKNOWN |
| **D** | Native Bibliothek mit Kryptologik (JNI/NDK, Story: OpenSSL) | Analysis: „prepares the JNI/NDK library“; Kit Exception „native function signChallenge“; Prior Audit Story OpenSSL | **primäre Arbeitshypothese** (INFERENCE) |

**Kombinationsfälle möglich:** z. B. Java lädt Key aus Asset (**A**) und signiert in JNI (**D**), oder JNI wrappt Keystore (**B+D**).

---

## Evidenz pro Untersuchungspunkt (Plan)

| # | Gegenstand | Bereits jetzt | Braucht |
|---|------------|---------------|---------|
| 1 | MyBMW APK/Dex | Package-Namen bekannt | APK vom Gerät / Store-Build (Inventar) |
| 2 | SecurityModule class | Reflect-Surface in Kit FACT | Decompile Klasse (ohne Key-Dump) |
| 3 | signChallenge Call-Chain | Kit → Module/Binder FACT | Inner chain in OEM |
| 4 | Java/Kotlin → JNI | Error string + Analysis FACT | `native` Methoden-Namen |
| 5 | native `.so` | UNKNOWN | `lib/` listing / `JNI_OnLoad` map |
| 6 | Keystore / KeyMint / TEE | UNKNOWN | API-Trace (strace/frida **observe-only**) |
| 7 | Binder/AIDL hinter Module | Classic outer AIDL FACT | MyBMW inner services |
| 8 | Certificate-/Key-Loading | `loadAppCert` / createContext FACT | Wo PKCS12/PEM liegt |
| 9 | 512-B Format | MEASURED | Optional: Verify mit APP_AUTH **public** key (Verify ≠ Extract) |
| 10 | Feld `sas_login` Vergleich | 512-B Nutzlast MEASURED | Gleiche Challenge lab↔field nur mit OEM |

### Erlaubt vs. verboten in Folgearbeiten

| Erlaubt | Verboten |
|---------|----------|
| Call-Graph, Symbolnamen, `.so`-Namen katalogisieren | Private Key exportieren |
| Public-Key Verify einer Feld-Signatur | Forge / Simulator als „echte Auth“ verkaufen |
| Feststellen Fall A vs B vs C vs D | Bypass-Anleitung |
| Observe-only Traces (welche API getroffen) | Credential theft |

---

## Cert-Mangling bleibt relevant

Selbst wenn Fall D/B geklärt ist: ohne korrektes **merged P7B** (APP + APP_AUTH/`connection`) akzeptiert die HU die Session nicht (Login ohne Cert → FIELD AUTH REJECT Texte).  
Signatur-Ort und Cert-Identität sind **zwei** Gates — Signatur allein reicht nicht ohne akzeptiertes Bundle.
