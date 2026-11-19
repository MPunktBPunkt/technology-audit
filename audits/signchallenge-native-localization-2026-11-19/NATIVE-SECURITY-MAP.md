# NATIVE-SECURITY-MAP

## OEM libraries

| Library | ABI | Exports | JNI registration | Strings/Symbols |
|---------|-----|---------|------------------|-----------------|
| *(none — no APK)* | — | — | — | — |

**Status:** empty map. Native localization **not performed**.

## Secondary signals (not `.so` evidence)

| Signal | Klassifikation | Implication |
|--------|----------------|-------------|
| Analysis: „prepares the JNI/NDK library to be ready to sign“; JNI gets packageName, appName, cert bundle | FACT (Doc) | Signing path involves native code **somewhere** in Classic/Connected era |
| Kit androidTest: exception text contains `native function signChallenge` | FACT (E4 string) | OEM path surfaces a *native* failure mode — still not a library name |
| Story / prior SAS audit: OpenSSL symbols in native lib | E1 narrative | **UNKNOWN** filename; do not treat as mapped |
| Kit `PrivateKeyHandling` MD5withRSA in Java | FACT (recon helper) | Algorithm form — **not** the production executor |

## Keystore / TEE screen

| API | In OEM APK this run? | Nutzung für signChallenge? |
|-----|----------------------|----------------------------|
| AndroidKeyStore | not searched (no APK) | **UNKNOWN** |
| KeyMint / Keymaster | — | **UNKNOWN** |
| StrongBox / TEE | — | **UNKNOWN** |

**Antwort:** „Wird die Signatur durch einen Android-/OEM-Sicherheitsdienst erzeugt?“ → **UNKNOWN** (keine Architektur-Evidence aus Binary).

Nicht aus Kit-Code schließen: Kit reflektiert nur Module-Methoden, ruft kein Keystore selbst.

## Binder / OEM-Service screen

| Interface | Status |
|-----------|--------|
| Classic `*.SECURITY_SERVICE` + `ICarSecurityService` | **FACT** — Fall C an der **App-Grenze** (Consumer→Classic) |
| MyBMW exported Binder for security | Analysis: ab 5.1 / MyBMW oft **nicht** exportiert; Kit skips `mobile20` binds | **FACT** (Kit policy + Doc) |
| Inner Binder behind `SecurityModule` | **UNKNOWN** ohne APK/Service dump |

Fall C für **MyBMW-innere** Signatur: weder bestätigt noch verworfen.

## Crypto step ownership (wanted vs known)

| Step | Expected owner | Known executor |
|------|----------------|----------------|
| XOR preprocess | OEM signer | Documented algorithm; **component UNKNOWN** |
| MD5 | OEM signer | same |
| RSA-4096 | OEM signer (APP_AUTH key) | same |
| 512-B output | OEM `signChallenge` return | FACT (tests + field size) |

## STOP

Spur endet am Kit Reflect / Binder Stub. Nächster Observe-Schritt = APK `lib/` + JADX `native` / `System.loadLibrary`.
