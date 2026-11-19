# Research Decision

## Urteil

**Gate lokalisiert, Erzeugung nicht gelöst.**  
Algorithmus/Format der Response sind desk-seitig rekonstruiert; der **Schlüsselort** (A/B/C/D) ist der nächste konkrete Untersuchungsgegenstand — primär Hypothese **D (JNI/native)**, unbewiesen ohne MyBMW/Classic-APK.

## DO NEXT (≤5)

1. **Phone inventory:** installierte Mine/Classic-Packages + APK-Pfad (`pm path de.bmw.connected.mobile20.*`).  
2. **APK Lokalisierung (observe):** `lib/*.so` Namen + `SecurityModule` / `native` Methodenliste — **nur Katalog**, kein Key-Export.  
3. **Public-Key Verify:** Feld-`sas_login`-512 gegen APP_AUTH Public Key aus gemergtem Cert (Verify bestätigt Algorithmus; ersetzt keinen Key).  
4. **Fall B/C Screen:** kurze Suche nach Keystore/KeyMint/Binder-Aufrufen in SecurityModule-Call-Chain.  
5. **ArtiDrive:** Auth-State `CHALLENGE_RX → OEM_SIGN_PENDING → LOGIN_TX` explizit; Lab-Stub nie als Fall A verkaufen.

## DEFER (≤5)

1. Volle native Crypto-RE der `.so`  
2. Classic vs MyBMW Diff der native Libs  
3. iOS Signing-Pfad  
4. Cloud/Account-Lifecycle der MyBMW-App (nicht Wire-Challenge)  
5. RHMI Digest-Whitelist-Vertiefung

## REJECT

| Item | Grund |
|------|-------|
| „SAS-Rätsel gelöst“ | Nur Gate-Ort bekannt |
| RSA/ECDSA knacken als Next | Falsches Problem; Key-Ort zuerst |
| Key-Extraktion / Forge | Leitplanke |
| Challenge = KNOCK | Schichtentrennung (PR #40) |
| Unbekannter Server als Default-Erklärung | Lokaler OEM-Sign-Pfad belegt |
| NBT-AAD / ENET als Auth-Ersatz | Prior Audits |

## Erfolgskriterium nächster Phase

Fall A/B/C/D ist **entschieden oder auf ≤2 Kandidaten reduziert**, mit zitierbaren Symbol-/API-Belegen — ohne dass ein Private Key dieses Repos betritt.
