# Evidence — idriveconnectkit-securityaccess-2026-11-19

## FACT

| ID | claim | source_path | confidence |
|----|-------|-------------|------------|
| `EVID-SASACC-001` | README: erste Car-Connection = Security Challenge; OEM-App liefert Antwort; Special Cert + App-Cert | KitAndroid `README.md` | high |
| `EVID-SASACC-002` | `signChallenge` nutzt OEM `ICarSecurityService`; erwartet 16-B Challenge | `SecurityAccess.kt` | high |
| `EVID-SASACC-003` | Classic: `Intent(className).setPackage(packageName)` bind; skip `mobile20` | `SecurityServiceManager.kt` | high |
| `EVID-SASACC-004` | MyBMW: `createPackageContext` + reflect `SecurityModule`/`AudioModule` | `SecurityModuleManager.kt` | high |
| `EVID-SASACC-005` | Package-Katalog Classic + Mine ROW/CN/HK/KR/NA (+ Mini/J29) | `KnownSecurityServices.kt` | high |
| `EVID-SASACC-006` | AIDL: create/release/loadAppCert/signChallenge | `ICarSecurityService.aidl` | high |
| `EVID-SASACC-007` | `mergeBMWCert`: drop `a4a_root-ca`; keep BMW CN contains `connection` | `CertMangling.kt` | high |
| `EVID-SASACC-008` | AAIdrive MusicApp/CarProber: cert → sas_certificate → signChallenge → sas_login | AAIdrive `MusicApp.kt`, `CarProber.kt` | high |
| `EVID-SASACC-009` | BclCarLink: BT/USB serial BCL; requires OEM Security Module for AAIdrive | BclCarLink `README.md` | high |
| `EVID-SASACC-010` | BclCarLink `Knock(serial, btAddr, macAddr, wifiAddr, appType, param1)` | `BclPacket.kt`, `BclClientTransport.kt` | high |
| `EVID-SASACC-011` | IDL `sas_certificate`→`byte[]`, `sas_login`→void | `BMWRemoting.etch` | high |
| `EVID-SASACC-012` | PrivateKeyHandling: XOR MD5(LE2)+MD5withRSA; Dev 192 B | `PrivateKeyHandling.kt` + unit test | high |
| `EVID-SASACC-013` | Classic instrumented: signChallenge → 512 B | `TestSecurityAccess.kt` | high |
| `EVID-SASACC-014` | Analysis Doc Auth Mermaid + CertType APP/APP_AUTH + Digests | `authentication.md` | high |

## FIELD (CROSSREF, nicht neu gemessen in diesem Desk-Lauf)

| ID | claim | source | relation |
|----|-------|--------|----------|
| `EVID-SASACC-F01` | 16-B `_result_sas_certificate` Challenge am F20 | `DEEP_FORENSIC_ETCH_SAS_20261116` | SUPPORT 002 |
| `EVID-SASACC-F02` | `sas_login` 559 B = … + 512 RSA + … | same | SUPPORT/REFINE 013 |
| `EVID-SASACC-F03` | APP_AUTH CN `…BMWTouchCommand_Connection_…` | same | SUPPORT 007 |
| `EVID-SASACC-F04` | Lab mybmw-sim Cert → HU Auth REJECT | `DEEP_FORENSIC_FIELD_AUTH_REJECT_20261118` | SUPPORT Blocker-Lage |

## INFERENCE

| ID | claim |
|----|-------|
| `EVID-SASACC-050` | F20 Connected-Blocker nach BCL/Etch-OPEN = fehlende/ungültige OEM-`signChallenge`-Response (nicht HS/KNOCK) |
| `EVID-SASACC-051` | Auf aktuellem Phone-Stack ist MyBMW Module-Pfad der relevante Security-Provider (Classic Binder oft closed) |

## REJECTED

| Claim | Why |
|-------|-----|
| Security Challenge ≡ HS/KNOCK/ACK10 | Schichtentrennung |
| PrivateKeyHandling = Produktions-Login ohne OEM | Runtime uses OEM module |
| Credential-/Module-Hook als nächster Schritt | Leitplanke |
| NBT-AAD Wi-Fi/AA = SAS-Ersatz | Prior SDP audit |

## UNKNOWN

| Claim | Hinweis |
|-------|---------|
| Exact JNI inside OEM `.so` for production key material | Not in public Kit source |
| Welche Mine-Regional-Package auf unserem OnePlus installiert ist | Device inventory; not this desk |
| Ob Classic noch parallel installierbar/nutzbar am F20-Phone | Needs phone check |
