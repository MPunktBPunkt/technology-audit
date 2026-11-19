# Audit Campaign: idriveconnectkit-securityaccess-2026-11-19

```yaml
id: idriveconnectkit-securityaccess-2026-11-19
project_id: bimmergestalt-idrive-refs
started: 2026-11-19
ended: 2026-11-19
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
continuation_of:
  - audits/bmw-connected-sas-auth-2026-11-06/
  - audits/nbt-evo-oss-runtime-hmi-bt-2026-11-19/
  - audits/f20-sdp-vs-nbt-aad-2026-11-19/
upstream_pins:
  BimmerGestalt/IDriveConnectKitAndroid: "4a567bc"
  BimmerGestalt/IDriveConnectKit: "95492b0"
  BimmerGestalt/BMWConnectedAnalysis: "9e96ac6"
  BimmerGestalt/BclCarLink: "7cfd959"
  BimmerGestalt/AAIdrive: "cc81d8e"
field_crossref:
  - DEEP_FORENSIC_ETCH_SAS_20261116
  - DEEP_FORENSIC_FIELD_AUTH_REJECT_20261118
reuse_outcomes:
  reused: [bmw-sas-auth, bmw-bcl, bmw-etch-rpc]
  new: []
  process: "Focused SecurityAccess/CertMangling dependency map; no SAS bypass; BCL≠SAS layers."
  decisions_touched:
    - fact-sas-after-etch-not-bcl-hs
    - fact-signChallenge-oem-module-blocker
    - fact-certmangling-app-plus-connection
    - refine-g3-field-now-measured
    - reject-challenge-equals-knock
```

## Ziel

Den von BclCarLink/AAIdrive verwiesenen **Security-Pfad** in IDriveConnectKitAndroid
systematisch auslesen und gegen unseren F20-Feldstand legen — **ohne** HS/KNOCK/ACK10 mit
der SAS-Challenge gleichzusetzen und **ohne** Credential-/Key-Rekonstruktion.

## Scope

| Im Scope | Out of Scope |
|----------|--------------|
| `SecurityAccess`, `CertMangling`, `KnownSecurityServices`, Binder vs Module | Private-Key-Extraktion / Bypass |
| Package-Namen, Intents, AIDL | Neuer NBT-AAD / ENET Audit |
| Korrelation Challenge/Login-Größen Code↔Feld | „Response abgreifen“-How-to |
| Schichtentrennung BCL vs Etch-SAS | Implementierung |

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | SecurityAccess Call-Graph + Abhängigkeiten | erfüllt → [SECURITY-PATH.md](SECURITY-PATH.md) |
| 2 | CertMangling Regeln | erfüllt → [SECURITY-PATH.md](SECURITY-PATH.md) § Cert |
| 3 | Layer-Map BCL ≠ SAS + Feld-Crosswalk | erfüllt → [LAYER-CROSSWALK.md](LAYER-CROSSWALK.md) |
| 4 | Research Decision (kein Bypass) | erfüllt → [RESEARCH-DECISION.md](RESEARCH-DECISION.md) |

## Kernurteil

```
BCL  INIT / HS / KNOCK / ACK10 / OPEN(4004)     ← Transport (BclCarLink)
                 ↓
Etch  BMWRemoting session
                 ↓
SAS   sas_certificate(merged p7b)
                 ↓  16-B challenge   ← FIELD MEASURED
      signChallenge(...)            ← OEM Security Module / Binder  ★ BLOCKER
                 ↓
      sas_login(RSA-4096 sig)       ← 512-B sig in 559-B wire frame  FIELD MEASURED
```

**BclCarLink** = Tunnel + KNOCK-Struktur.  
**IDriveConnectKitAndroid** = SAS-Client + OEM-Security-Anbindung.  
**AAIdrive** = Consumer beider.  
Lab/`f20_sim` mockt `signChallenge`-Verifikation → Lab PASS ≠ F20 Auth (FIELD REJECT 2026-11-18).

## Leitplanke

Kein Credential-Diebstahl, keine Key-Ableitung, kein „SecurityModule hooken“-Playbook.  
Dokumentiert wird nur, **wo** die Response erzeugt wird und **warum** unser Blocker dort sitzt.

## Artefakte

| Datei | Inhalt |
|-------|--------|
| [SECURITY-PATH.md](SECURITY-PATH.md) | Code-Deep-Dive |
| [LAYER-CROSSWALK.md](LAYER-CROSSWALK.md) | BCL vs SAS vs Feld |
| [evidence.md](evidence.md) | Evidence-IDs |
| [RESEARCH-DECISION.md](RESEARCH-DECISION.md) | DO NEXT / REJECT |

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Security Challenge = HS/KNOCK? | Gleiche Schicht/Bytes? | BCL before OPEN 4004; SAS after Etch | **REJECTED** Gleichsetzung |
| Wo sitzt F20-Blocker? | Was fehlt nach Tunnel PASS? | AUTH_REJECT 18.11; Kit `signChallenge` | OEM Security Module Response |
| G3 Feld? | sas_* sichtbar? | DEEP_FORENSIC 16.11 | **MEASURED** (Prior-Audit G3 absent → refine) |
