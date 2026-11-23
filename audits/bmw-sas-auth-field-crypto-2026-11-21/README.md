# Audit: BMW SAS Field Crypto Closure (B3 Gate B)

```yaml
id: bmw-sas-auth-field-crypto-2026-11-21
project_id: esp32-bt-analyzer
related_projects: [bimmergestalt-idrive-refs, hu-probe, pidrive]
started: 2026-11-21
ended: 2026-11-23
status: closed
profile: ops-field
standard_version: "0.7.1"
primary_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
related_audits:
  - nbt-evo-bt-control-plane-closure-2026-11-21
  - bmw-connected-sas-auth-2026-11-06
  - libaudio-signchallenge-pipeline-2026-11-19
reuse_outcomes:
  reused: [technologies/bmw-sas-auth, technologies/bmw-etch-rpc, technologies/bmw-bcl]
  new: []
  not_helped: []
  process: "Ingest B3 raw crypto verify (18/18) into bmw-sas-auth sheet; close RSA-VERIFY OPEN from prior closure audit."
```

## Ziel

Vollständige kryptographische Schließung des live APP_AUTH-Pfads aus `FIELD_B3_GATEB_20261121T112446Z`: Pad, Digest-Konstruktion, RSA-4096-Verify gegen Wire-Leaf, Multi-Channel-Login.

## Scope

- Im Scope: Cert → Challenge → Login → Accept; Pad `0x02000000`; Digest-Formel; 18/18 VERIFY; Leaf CN; parallele BCL-src-Kanäle.
- Nicht im Scope: Private-Key-Extraktion; Standalone-Signer (Gate B2); RHMI/AM/AV Follow-on (andere Audits).

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | RSA-VERIFY aller HU-akzeptierten Logins dokumentiert | erfüllt — 18/18 VALID |
| 2 | Pad + Digest-Formel als FIELD/CRYPTO FACT im Sheet | erfüllt |
| 3 | Multi-Channel-Auth als FACT getrennt von Single-Session-Desk | erfüllt |
| 4 | Standalone bleibt explizit OPEN | erfüllt |

## Evidence-Basis

| Artefakt | Rolle |
|----------|-------|
| `raw/phone_to_hu.bin` / `hu_to_phone.bin` | Byte-autoritativ |
| `forensic/SAS_CRYPTO_VERIFY.json` | 18 pairs, `rsa_verify_ok` |
| `forensic/SAS_CERTIFICATE.{der,p7b}` | Leaf + PKCS#7 |
| `forensic/SAS_SIGNATURES/` | 512-B Sig blobs |
| `RAW_FORENSIC_ANALYSIS.md` §10–14 | Chronologie + Formel |
| `EVAL.md` / `SAS_EVAL.md` | Gate B CLOSED vs Arm-A stub reject |

## Claim-Level-Tabelle

| Claim | Level | Evidence |
|-------|-------|----------|
| Sequenz Cert → 16-B Challenge → 512-B Login → `_result_sas_login` Accept | **FIELD FACT** | Raw + VERIFY |
| Pad-u32 = `0x02000000` (≠ X509 serial `0x0AA9`) | **FACT** | 18/18 pairs |
| `Digest = MD5(challenge XOR MD5(pad))` + PKCS#1 v1.5 DigestInfo-MD5 | **FACT — CRYPTO VERIFIED** | VERIFY.json formula |
| RSA-4096 Verify gegen Leaf `a4a_app_BMWTouchCommand_Connection_00.00.10` | **FACT — CRYPTO VERIFIED** | 18/18 |
| 12× cert / 19× challenge / 18× login / 18× accept in diesem Capture | **FIELD FACT** | Raw counts |
| Parallele Auth über mehrere BCL `src`→dest 4004 | **FIELD FACT** | Multi OPEN 4004 |
| Private Key im Capture | **NOT PRESENT** | Public only |
| Lab-stub cert → F20 ACCEPT | **REJECTED** | `SAS_EVAL.md` CERTIFICATE_REJECTED |
| MyBMW zwingend für Protokollmathematik | **REJECTED** | Formel Wire-geschlossen |
| Standalone Credential Acceptance (Gate B2) | **OPEN** | kein ACCEPT ohne MyBMW/AAIdrive |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| RSA-VERIFY B3 CLOSED? | Verifizieren alle 18 HU-Logins? | `SAS_CRYPTO_VERIFY.json` | Ja — Sheet + Closure-OPEN schließen | DISCOVERED AFTER TEST |
| Pad = serial? | Ist `0x0AA9` der Pad? | VERIFY pad_u32 | Nein — REJECTED | KNOWN BEFORE + RETROFIT |
| Multi-Channel Pflicht? | Ein Cert/Login genügt? | Raw multi src | Parallel beobachtet; Single unbewiesen als Suffizienz | DISCOVERED DURING TEST |

## Kill-Kriterien

**Hypothese:** Alle HU-akzeptierten B3-Logins verifizieren gegen TouchCommand-Leaf mit Pad `0x02000000`.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | ≥1 HU-Accept ohne `rsa_verify_ok` | nicht eingetreten |
| 2 | Pad ≠ `0x02000000` für Accept-Paar | nicht eingetreten |

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| FIELD_B3 | `EVID-B3-SAS-CRYPTO-18-18` | `technologies/bmw-sas-auth/SHEET.md` |
| FIELD_B3 | `EVID-B3-SAS-LEAF-TOUCHCOMMAND` | same |
| FIELD_B3 | `EVID-B3-SAS-MULTICHANNEL` | same |

## Lessons → Transfer

- Desk 8/8 Lab-VERIFY und Field 18/18 teilen dieselbe Formel — Gate A + Gate B konsistent.
- `b3.jsonl` allein unterdekodiert Certs; Raw-Reassembly ist Primärquelle.
- Closure-Audit OPEN „RSA-VERIFY dieses Captures“ ist **superseded**.

## Offene Punkte

- Gate B2 Standalone-Signer
- Welcher Phone-Prozess hält den privaten Key (libaudio CASE A bleibt Codepfad-INFERENCE)
