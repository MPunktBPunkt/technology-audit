# Audit Campaign: signchallenge-pipeline-localize-2026-11-19

```yaml
id: signchallenge-pipeline-localize-2026-11-19
project_id: bimmergestalt-idrive-refs
started: 2026-11-19
ended: 2026-11-19
status: closed
profile: planning
standard_version: "0.7.1"
standard_gaps: []
continuation_of:
  - audits/idriveconnectkit-securityaccess-2026-11-19/
  - audits/bmw-connected-sas-auth-2026-11-06/
upstream_pins:
  BimmerGestalt/IDriveConnectKitAndroid: "4a567bc"
  BimmerGestalt/BMWConnectedAnalysis: "9e96ac6"
field_crossref:
  - DEEP_FORENSIC_ETCH_SAS_20261116
  - DEEP_FORENSIC_FIELD_AUTH_REJECT_20261118
reuse_outcomes:
  reused: [bmw-sas-auth]
  new: []
  process: "Localize signChallenge key/signing locus (A–D). No key extraction, no forge, no bypass."
  decisions_touched:
    - refine-gate-located-not-solved
    - fact-algorithm-form-known
    - hypothesis-fall-d-jni-primary
    - reject-rsa-crack-as-next
```

## Framing (streng)

| Aussage | Status |
|---------|--------|
| Ort des SAS-Gates identifiziert (`signChallenge` / OEM Security) | **FACT** (PR #40 + Feld) |
| Kryptographische Erzeugung einer **gültigen** Produktion-Response vollständig verstanden | **NEIN** — Algorithmus-Form bekannt, Schlüsselort **UNKNOWN** |
| „SAS-Rätsel gelöst“ | **REJECTED** als Formulierung |

```text
Transport / BCL / Etch / Challenge-RX   →  kein Blocker mehr (MEASURED)
signChallenge()-Pipeline / Key-Locus    →  verbleibender unbekannter Baustein
```

## Ziel

Die `signChallenge()`-Pipeline so weit rekonstruieren, dass Fall **A/B/C/D** (Schlüsselort)
entscheidbar wird — **ohne** Private Keys zu extrahieren und **ohne** Auth-Umgehung.

## Scope

| Im Scope | Out of Scope |
|----------|--------------|
| Bekannte Call-Chain Kit → SecurityModule/Binder → native | Key dump / forge tool |
| Algorithmus-Form (XOR + MD5withRSA) vs Feld 512-B | RSA „knacken“ |
| A–D Hypothesenmatrix + Evidence gaps | Server-Auth-Hypothese als Default |
| Plan für MyBMW-APK/Device-Lokalisierung | Bypass Playbook |

## Kernurteil (Desk, ohne MyBMW-APK)

| Pipeline-Schritt | Stand |
|----------------|------|
| Input | 16-B Challenge — FIELD + Kit FACT |
| Preprocess | `challenge ⊕ MD5(LE 0x00000002)` für APP_AUTH — Doc + `PrivateKeyHandling` FACT |
| Signatur | `MD5withRSA` → **512 B** (RSA-4096) — Doc + Classic/Module Tests FACT; Feld Frame 559 = …+512… |
| Public key Bindung | APP_AUTH Cert (CN `…Connection…`) — Doc + Feld CN MATCH |
| Ausführungsort | OEM `signChallenge` → Fehlertext **„native function signChallenge“** → **Fall D primär (HYPOTHESIS/INFERENCE)** |
| Native `.so` Name | **UNKNOWN** (kein APK in diesem Lauf) |
| Android Keystore/TEE | **UNKNOWN** (kein Trace) |
| Separater OEM Binder hinter Module | **UNKNOWN** (MyBMW) |
| Schlüssel in APK-Klartext | **UNKNOWN**; Dev-P12 existiert nur als Test-Rekonstruktion |

**Nicht naheliegend:** „unbekannter BMW-Cloud-Server für jede Challenge“ — Signing läuft lokal im Phone-OEM-Pfad (Analysis + Kit + Tests). Cloud kann für App-Lifecycle relevant sein, ist aber nicht der gemessene Wire-Schritt Challenge→Response.

## Artefakte

- [PIPELINE.md](PIPELINE.md) — bekannte Schritte + A–D Matrix  
- [RESEARCH-DECISION.md](RESEARCH-DECISION.md)  
- Prior: [`../idriveconnectkit-securityaccess-2026-11-19/`](../idriveconnectkit-securityaccess-2026-11-19/)

## Leitplanke

> Verstehen, **wo** die Signaturfähigkeit sitzt — nicht sie extrahieren oder umgehen.
