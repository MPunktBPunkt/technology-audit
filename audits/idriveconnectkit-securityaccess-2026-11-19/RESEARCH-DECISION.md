# Research Decision

## Urteil

Der SAS-Blocker ist **Phone-seitiges OEM-`signChallenge`** nach erfolgreichem BCL/Etch — nicht der BCL-Handshake und nicht NBT-AAD. KitAndroid ist die richtige Referenz für Cert-Merge + Security-Provider; BclCarLink bleibt Transport/KNOCK.

## DO NEXT (≤5)

1. **Phone inventory:** Welche `KnownSecurityServices`-Packages auf dem OnePlus 12 installiert/verbunden sind (`SecurityAccess.discover` / AAIdrive debug).  
2. **Wire-only Vertiefung:** Bestehende Captures — Challenge-Hex ↔ `_result_sas_certificate` In-Reply-To / Session-Bindung (FX-G3-02: neue Challenge pro Session?).  
3. **Sheet/App sync:** `bmw-sas-auth` field_evidence auf F20 MEASURED halten; G3 in Prior-Audit als superseded markieren (dieser Commit).  
4. **ArtiDrive:** Auth-State explizit `UNSIGNED | CHALLENGE_RX | LOGIN_TX | AUTHENTICATED | REJECTED` — Lab stub getrennt von „OEM signed“.  
5. **Optional:** Bei Auth-REJECT Captures Exception-Strings weiter gegen Analysis Doc mappen (bereits 18.11 begonnen).

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
