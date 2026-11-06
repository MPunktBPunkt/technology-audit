# Evidence — bmw-connected-sas-auth-2026-11-06

Desk 2026-11-06 · **standard_version 0.7.1** · Fokus **SAS Authentication** (Etch).

**Abgrenzung:** Einträge hier belegen **nicht** automatisch G1/G2 Wire am NBT Evo.
AOA/BCL-Feldbelege bleiben in `usb-aoa-bmw-connected-2026-desk` / hu-probe Reports.

## Evidence Matrix

| ID | Claim | Source | Class | E | Conf |
|----|-------|--------|-------|---|------|
| `EVID-SAS-2026-11-06-001` | IDL definiert `sas_certificate`/`sas_login`/`sas_crl`/`sas_permission`/`sas_logout` | IDriveConnectKit `BMWRemoting.etch` @95492b0 L132–136 | FACT | E2 | high |
| `EVID-SAS-2026-11-06-002` | Analysis Mermaid: App↔SecurityService Binder + App↔Car Etch Cert→Challenge→Sign→Login | BMWConnectedAnalysis `docs/authentication.md` @9e96ac6 | FACT (Doc) | E1 | high |
| `EVID-SAS-2026-11-06-003` | AAIdrive MusicApp: getAppCertificate → sas_certificate → signChallenge → sas_login | AAIdrive `MusicApp.kt` @3e93419 | FACT | E2 | high |
| `EVID-SAS-2026-11-06-004` | Gleiche Sequenz in Calendar/Assistant/CarInfo/Addons screen_mirror | AAIdrive + IDriveConnectAddons | FACT | E2 | high |
| `EVID-SAS-2026-11-06-005` | CarProber mergeBMWCert + SAS + rhmi_getCapabilities | AAIdrive `CarProber.kt` | FACT | E2 | high |
| `EVID-SAS-2026-11-06-006` | Challenge observed 16 bytes; login response ~512 (RSA4096-size) in Doc | authentication.md; protocol-etch.md | INFERENCE (observed) | E1 | med |
| `EVID-SAS-2026-11-06-007` | SecurityAccess comment: challenge should be 16 bytes; empty → IllegalArgumentException | KitAndroid `SecurityAccess.kt`; TestSecurityAccess | FACT | E2+E4 | high |
| `EVID-SAS-2026-11-06-008` | Connected Classic instrumented test: signChallenge → 512-byte response | KitAndroid `TestSecurityAccess.kt` | FACT | E4 | high |
| `EVID-SAS-2026-11-06-009` | PrivateKeyHandling: XOR MD5(LE 2) + MD5withRSA; Dev-P12 response 192 B | KitAndroid `PrivateKeyHandling.kt` + Test | FACT | E2+E4 | high |
| `EVID-SAS-2026-11-06-010` | P7B APP/APP_AUTH; OID 1.3.6.1.4.1.513.59.4.x; Digests SHA256 | authentication.md | FACT (Doc) | E1 | high |
| `EVID-SAS-2026-11-06-011` | RHMI resource check `CRHMIAuthPermHandler::verifyResource` in libhmiremoting.so | authentication.md | FACT (Doc claim) | E1 | med |
| `EVID-SAS-2026-11-06-012` | Story: edited layout rejected; original accepted (hash whitelist) | hufman story | FACT (Narrative experiment) | E1 | med |
| `EVID-SAS-2026-11-06-013` | KnownSecurityServices packages incl. MyBMW mobile20.* | KitAndroid `KnownSecurityServices.kt` | FACT | E2 | high |
| `EVID-SAS-2026-11-06-014` | Binder path skips mobile20; Module reflection path for MyBMW | SecurityServiceManager / SecurityModuleManager | FACT | E2 | high |
| `EVID-SAS-2026-11-06-015` | Connected ≥5.1 / MyBMW export SecurityService nicht mehr | authentication.md; FAQ | FACT (Doc) | E1 | high |
| `EVID-SAS-2026-11-06-016` | AIDL ICarSecurityService create/load/sign/release | KitAndroid + Analysis aidl | FACT | E2 | high |
| `EVID-SAS-2026-11-06-017` | Simulator sas_*: ignore cert; login no-op; return ByteArray(16) | Simulator `BMWRemotingServerImpl.kt` | FACT | E2 | high |
| `EVID-SAS-2026-11-06-018` | MockBMWRemotingServer: same open stub | AAIdrive test mock | FACT | E2 | high |
| `EVID-SAS-2026-11-06-019` | CertMangling merges APP with connection cert (CN contains connection) | KitAndroid `CertMangling.kt` | FACT | E2 | high |
| `EVID-SAS-2026-11-06-020` | Etch over BCL dest 0x0FA4; SAS is Etch not BCL | BCL sheet + etch IDL | FACT | E1+E2 | high |
| `EVID-SAS-2026-11-06-021` | USB BCL Doc vs BclCarLink BT-only | prior EVID-AOA-013 | Contradiction / REJECTED as USB impl | E1+E2 | high |
| `EVID-SAS-2026-11-06-022` | Eigenes SAS Wire/Field Capture F20 | — | UNKNOWN | — | — |
| `EVID-SAS-2026-11-06-023` | Story RE path: BT sniff → BCL → Etch → FakeCar → SecurityService | hufman.github.io/stories/bmwconnectedapps | FACT (Narrative) | E1 | high |
| `EVID-SAS-2026-11-06-024` | AOA Enum field ≠ SAS | EVID-AOA-030 + this audit | FACT (separation) | E3+E0 | high |

## Langform (Auswahl)

### EVID-SAS-2026-11-06-001

```yaml
id: EVID-SAS-2026-11-06-001
source_repo: BimmerGestalt/IDriveConnectKit
source_ref: 95492b0
source_path: idriveconnectkit-etch/BMWRemoting.etch
claim: BMWRemoting IDL exposes sas_certificate returning byte[], sas_login void, plus sas_crl/permission/logout.
classification: FACT
evidence_level: E2
direct_observation: false
limitations: IDL reconstructed from APK symbols historically; matches AAIdrive usage
```

### EVID-SAS-2026-11-06-009

```yaml
id: EVID-SAS-2026-11-06-009
source_repo: BimmerGestalt/IDriveConnectKitAndroid
source_ref: 4a567bc
source_path: …/security/PrivateKeyHandling.kt
claim: Challenge response = MD5withRSA over challenge, optionally XORed with MD5(0x02,0x00,0x00,0x00) for APP_AUTH-era certs.
classification: FACT
evidence_level: E2+E4
note: Documents public reconstruction; does not publish private key material.
limitations: Equivalence to OEM JNI verified by upstream narrative/tests, not by our HU capture.
```

### EVID-SAS-2026-11-06-017

```yaml
id: EVID-SAS-2026-11-06-017
source_repo: BimmerGestalt/Simulator
source_path: android/…/BMWRemotingServerImpl.kt
claim: Fake HU ignores certificate and login payload; returns 16-byte challenge array without verification.
classification: FACT
evidence_level: E2
technology_audit_relevance: HIGH — prevents treating Simulator success as crypto proof
```

### EVID-SAS-2026-11-06-022

```yaml
id: EVID-SAS-2026-11-06-022
claim: SAS authentication observed on BMW F20 / NBT Evo USB or BT wire by this project
classification: UNKNOWN
evidence_level: —
related: FX-G3-01 in AUDIT-REPORT.md §22
```
