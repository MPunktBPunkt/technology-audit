# Research Decision

## Urteil

Der SAS-**Gate-Ort** ist **Phone-seitiges OEM-`signChallenge`** nach BCL/Etch — nicht HS/KNOCK, nicht NBT-AAD.  
**Nicht gelöst:** wo der private Schlüssel / die Signaturfähigkeit sitzt (A–D).  
→ [`../signchallenge-pipeline-localize-2026-11-19/`](../signchallenge-pipeline-localize-2026-11-19/).

## DO NEXT (≤5)

1. **signChallenge-Lokalisierung A–D** (MyBMW APK / native `.so` Katalog) — siehe Folge-Audit.  
2. **Phone inventory:** `KnownSecurityServices`-Packages auf dem OnePlus 12.  
3. **Public-Key Verify** Feld-`sas_login` gegen APP_AUTH leaf (Algorithmus-Check, kein Key-Export).  
4. **ArtiDrive:** `CHALLENGE_RX → OEM_SIGN_PENDING → …`; Lab-Stub ≠ OEM signed.  
5. **Wire:** Challenge-Session-Bindung (FX-G3-02) optional.

## DEFER (≤5)

1. Byte-for-byte Dissector-Vergleich jedes KNOCK-Felds — Transport schon MEASURED; kein SAS-Nutzen.  
2. Classic vs Mine Parallelbetrieb am gleichen Phone.  
3. iOS Cert-Pfad.  
4. CarAPI (deprecated).  
5. HU `verifyResource` Digests jenseits bekannter WHITELIST-Story.

## REJECT

| Item | Grund |
|------|-------|
| Security Challenge = HS/KNOCK/ACK10 | Falsch Schicht |
| OEM SecurityModule reverse / key extract | Leitplanke |
| „Response aus MyBMW abgreifen“ als Ops-Pfad | Wire zeigt Response schon; Hook = Bypass-adjacent |
| NBT-AAD BT als SAS-Einstieg | SDP NO-GO |
| ENET/SSH als Auth-Ersatz | Config-Plane |
| Lab Auth-PASS als F20-Beweis | FIELD REJECT 18.11 |

## Rollen (kurz)

| Komponente | Rolle |
|------------|-------|
| BclCarLink | BCL tunnel + KNOCK |
| IDriveConnectKit (etch) | `sas_*` IDL / client stubs |
| IDriveConnectKitAndroid | SecurityAccess + CertMangling + OEM bind/module |
| AAIdrive | Etch apps + Security consumer |
| MyBMW / Classic | Security Module / Binder (private key domain) |
| f20_sim | Mock verifier — nicht Produktion |
