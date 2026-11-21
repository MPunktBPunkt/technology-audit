# F20 Connected — Gap/Delta Audit nach Crypto Closure (2026-11-20)

```yaml
id: f20-connected-gap-audit-20261120
type: delta-gap-audit
scope: post-crypto-closure unknowns only
not: full technology re-audit
canonical_product_status: esp32.bt-analyzer docs/analysis/SAS_STATUS_CRYPTO_CLOSED_20261120.md
claim_levels: [FACT, FIELD FACT, LAB FACT, INFERENCE, HYPOTHESIS, UNKNOWN, OPEN, REJECTED]
primary_next: B3 field run with authorized APP/APP_AUTH context
superseded_p0_by: docs/analysis/F20_BT_CONTROL_PLANE_CLOSURE_20261121.md
closure_audit: audits/nbt-evo-bt-control-plane-closure-2026-11-21/
```

> **SUPERSEDED (P0 framing) — 2026-11-21:** Gate B / B3 ist **CLOSED**  
> (`bt-analyzer` `FIELD_B3_GATEB_20261121T112446Z`, commit `4d05169`).  
> Live MyBMW/AAIdrive → `_result_sas_login` → RHMI/AM/CDS/AV = **FIELD FACT**.  
> Was **OPEN** bleibt: Standalone-Signer (B2), Music DESCRIPTION-Blob, Feld-Model/Action-IDs, eigener RHMI-PoC.  
> Canonical status: [`F20_BT_CONTROL_PLANE_CLOSURE_20261121.md`](F20_BT_CONTROL_PLANE_CLOSURE_20261121.md).  
> Der historische Text unten dokumentiert den **Stand 2026-11-20** und wird nicht als aktuelle P0-Lage gelesen.

## 1. Executive Status

Nach Crypto Closure (20.11.2026) ist das **Kryptoprotokoll und die Wire-Cert↔Signer-Korrelation geschlossen**.  
Transport/BCL/Etch/SAS-Wire sind **nicht** erneut zu öffnen.

Was noch unbekannt ist, ist **nicht** „ob F20 Connected-Auth überhaupt kann“, sondern:

1. **Gate B1 (autorisierter OEM-Kontext)** — bereits **FIELD FACT**
2. **Gate B2 (reproduzierter / standalone Credential-Kontext)** — **OPEN**
3. **MyBMW als Runtime-/Signer-Träger** — Protokoll **REJECTED**, Implementierung **OPEN**
4. **F20 RHMI/AM/CDS unter unserem kontrollierten Client** — nach Auth **OPEN** *(historisch 20.11.; B3 21.11. CLOSED für Relay-Pfad)*
5. **F20 Model-/Action-IDs und echte PiDrive Control** — **UNKNOWN / OPEN** (LAB ≠ FIELD)

**Ein Experiment reduziert diese Unknowns am stärksten:**  
ein kontrollierter **B3-Feldlauf mit tatsächlich autorisiertem APP/APP_AUTH-Kontext** (live MyBMW/AAIdrive-Signer, keine Key-Extraktion).  
*(B3 ist gelaufen — siehe Closure-Status 2026-11-21.)*

---

## 2. Evidence Basis

Nur aktueller Repo-Stand + referenzierte Upstream-Artefakte (`esp32.bt-analyzer` / `bt-analyzer`):

| Artefakt | Rolle |
|----------|-------|
| `docs/analysis/SAS_STATUS_CRYPTO_CLOSED_20261120.md` (product) | Canonical Crypto + Dual-Gate |
| `docs/analysis/SAS_PAD_RSA_VERIFY_LAB_20261120.md` | Pad `0x02000000`, PKCS#1, RSA-VERIFY **8/8**, 2³² |
| `docs/analysis/SAS_SIGNER_CASE_A_CLOSED_20261119.md` | CASE A native Signer |
| `docs/analysis/GATE_APP_AUTH_ACCEPTANCE_20261118.md` | Field Gate (Acceptance) |
| `docs/analysis/GATE_E2E_COMPARISON.md` | Field vs Lab vs Replay |
| `docs/analysis/FIELD_DAY_ONE_VARIABLE_GATE.md` | Operator-Runbook B3 |
| `docs/analysis/DEEP_FORENSIC_ETCH_SAS_20261116.md` | OEM MyBMW/AAIdrive Golden Path am F20 |
| `docs/analysis/DEEP_FORENSIC_FIELD_AUTH_REJECT_20261118.md` | LABSIM Cert → HU Reject |
| `audits/libaudio-signchallenge-pipeline-2026-11-19/` | CASE A in diesem Repo |
| `audits/esp32-bt-analyzer-f20-connected-2026-11-17/` | Stack Freeze |
| `audits/esp32-bt-analyzer-lab-field-transfer-2026-11-17/` | Lab ≠ Field / PiDrive LAB ONLY |
| `audits/bimmergestalt-rhmi-checkresource-2026-11-17/` | RHMI Lifecycle Desk/Lab |

Epistemik-Regeln (verbindlich):

| ≠ | |
|--|--|
| FIELD CAPTURE | FIELD ACCEPTANCE |
| SAS Request | SAS Authenticated |
| `checkResource(true)` | `setResource(...)` |
| LAB PASS | F20 FIELD PASS |

---

## 3. What Closed Since Previous Audit

| Bereich | Status | Evidence |
|---------|--------|----------|
| Pad-Input APP_AUTH | **CLOSED FACT** | `0x02000000` (= CertificateType-artig); **nicht** X509-Serial `0x0AA9` |
| Pad-Formel | **CLOSED FACT** | `pad = MD5(02 00 00 00)` = `f2dd0dedb2c260419ece4a9e03b2e828` |
| Challenge-Pipeline | **CLOSED FACT** | `xored = challenge XOR pad`; `digest = MD5(xored)` = `06fae79665b94ec3ccf5fa3fabd0e85e` (Lab-Session) |
| RSA | **CLOSED FACT** | RSA-4096, PKCS#1 v1.5, DigestInfo-MD5 → 512-B Sig |
| Wire Cert ↔ login_sig | **CLOSED FACT** | RSA-VERIFY **8/8** gegen Wire-Leaf Public Key |
| Pad-u32 Suche | **CLOSED FACT** | 2³² → eindeutiger Treffer `0x02000000` |
| Client Signer locus | **CLOSED FACT** | `SecurityModule.signChallenge` → `AudioModule.g` → `libaudio.so` → `EVP_PKEY_sign` |
| Key-Architektur CASE A | **CLOSED FACT** | Embedded PKCS#12; Keystore/TEE/Binder/Asset-Pfad **REJECTED** |
| VIN → Key als nächster Weg | **REJECTED** | Fixed-VA Universal-APK; kein VIN-Dataflow auf Sign-Pfad |
| AOA als SAS-Bypass / BT-Voraussetzung | **REJECTED** (für diesen Pfad) | BT SCN6 Golden Path ohne AOA **FIELD FACT** |
| Gate A — Crypto correctness | **CLOSED** | siehe oben |

**Nicht erneut öffnen** ohne neue Capture-Evidence: BT Classic/RFCOMM, SDP/SPP, BCL HS/MUX, Etch/BMWRemoting, SAS Payload-Struktur, weitere Pad-Spekulation, weitere CertificateType-Brute-Force.

---

## 4. Current Gate Model

### Basiskette (unverändert, Schichten getrennt)

```text
PHONE
  ├─ MyBMW / Connected SDK          ← Implementierung / Credential-Träger
  │    ↓
  │  SecurityModule.signChallenge()
  │    ↓
  │  AudioModule.g()
  │    ↓
  │  native signer / libaudio.so
  │
  └─ BCL client / localhost TCP     ← Client-Transport
       ↓
Bluetooth Classic → RFCOMM SCN 6 → BCL → Etch / BMWRemoting
       ↓
sas_certificate → 16-B challenge → sas_login (512-B RSA)
       ↓
F20 HU → AM / RHMI / CDS
```

### Gate A — Crypto correctness → **CLOSED**

```text
CertificateType / pad-u32 = 0x02000000
pad    = MD5(02 00 00 00)
xored  = challenge XOR pad
digest = MD5(xored)
sig    = RSA-4096 PKCS#1 v1.5 DigestInfo-MD5(digest)
```

### Gate B — sauber aufteilen (nicht „F20 Acceptance = offen“ kollabieren)

#### Gate B1 — F20 akzeptiert autorisierten MyBMW/AAIdrive-Kontext

**STATUS = FIELD FACT**

Evidence: `DEEP_FORENSIC_ETCH_SAS_20261116` Session S-B / verwandte Captures —

- `_result_sas_certificate` (16-B Challenge)
- `sas_login` 559-B Frame / 512-B RSA
- `_result_sas_login` positiv (~99 ms)
- anschließend `_result_rhmi_getCapabilities` **plen=5306**, AM, RHMI, CDS (37×)

Das ist **OEM-autorisierter** Connected-Kontext am echten F20 — kein Lab-Stub.

#### Gate B2 — F20 akzeptiert unseren reproduzierten / standalone Credential-Kontext

**STATUS = OPEN**

Evidence: `DEEP_FORENSIC_FIELD_AUTH_REJECT_20261118` + `GATE_E2E_COMPARISON` —

- LABSIM / `mybmw-sim` Bundle → HU: **„Certificate is invalid or expired.“**
- Login → **„Client has not sent an app certificate yet.“**
- AM/RHMI/CDS → **„Session is not logged in.“** / invalid handle

**INFERENCE verboten:** daraus nicht ableiten, dass der F20 generell keine Connected-Auth akzeptiert (widerspricht B1).

### Dual-Gate Kurzform

```text
Gate A   Crypto / Cert↔Sig (Wire)                         🟢 CLOSED
Gate B1  F20 akzeptiert autorisierten OEM-Kontext         🟢 FIELD FACT
Gate B2  F20 akzeptiert reproduzierten Credential-Kontext 🟡 OPEN
```

---

## 5. Remaining Open Questions

### MyBMW — drei getrennte Fragen

| Frage | Antwort | Klasse |
|-------|---------|--------|
| **Protokollabhängigkeit** — braucht der nachgewiesene BT/BCL/Etch/SAS-*Wire*-Pfad technisch die MyBMW-App? | **Nein.** Formel + PKCS#1 + Cert↔Sig sind öffentlich nachrechenbar; Wire trägt Cert+Sig, nicht die App. | **REJECTED** als Protokoll-Notwendigkeit |
| **Implementierungsabhängigkeit** — braucht unsere *bekannte* Signierfähigkeit MyBMW/`libaudio.so`? | **Ja, derzeit.** Bekannter Signer + embedded PKCS#12 sitzen dort; AAIdrive lädt MyBMW-SecurityModule per Package-Context. | **FACT** (aktueller Stand) |
| **Standalone** — ist ein kompletter Connected-Client ohne MyBMW bereits nachgewiesen? | **Nein.** Lab-Accept ≠ F20; LABSIM-Reject am F20; kein lawful Standalone-Signer ohne Key-Extraktion gebaut. | **OPEN** |

Aus „MyBMW ist nicht Teil des Wire-Protokolls“ **nicht** ableiten: „MyBMW wird nicht benötigt“.

### Remaining-Unknowns-Matrix

| Bereich | Status | Evidence | Was fehlt? | Nächstes Experiment |
|---------|--------|----------|------------|---------------------|
| Crypto | **CLOSED** | SAS_PAD 8/8 + 2³² | nichts | — |
| Wire Cert ↔ Signer | **CLOSED** | RSA-VERIFY 8/8 | nichts | — |
| F20 akzeptiert autorisierten Kontext (B1) | **FIELD FACT** | DEEP_FORENSIC 16.11. | — | — |
| Reproduzierter Credential-Kontext (B2) | **OPEN** | AUTH_REJECT 18.11. | F20 Acceptance unter kontrolliertem Auth-Kontext | **B3** |
| MyBMW als Protokollinstanz | **REJECTED** | Crypto closed | — | — |
| MyBMW als Runtime-/Signer-Träger | **FACT / OPEN** | CASE A; Standalone unbewiesen | Standalone ohne Key-Extract | nach positivem B3 evaluieren |
| RHMI Lifecycle im LAB | **CLOSED** | LAB_P0_RHMI_LIFECYCLE_PASS | — | — |
| RHMI/AM/CDS auf realem F20 (OEM) | **FIELD FACT** | DEEP_FORENSIC Caps/AM/CDS | — | — |
| RHMI/AM/CDS unter *unserem* Client am F20 | **OPEN** | AUTH_REJECT stoppt vor Auth | positive Auth + Snapshot | **B3** dann Run B |
| F20 Model-/Action-IDs | **UNKNOWN** | Lab 100/200 = LAB ONLY | Feld-IDs | nach positiver Auth |
| PiDrive Action-Sequenz im LAB | **LAB ONLY** | `PI_DRIVE_TEST` / actionId 200 | — | nicht als F20 übernehmen |
| Echte F20 PiDrive Control | **OPEN** | kein Feldversuch | Feldbeweis | nach positiver Auth + ID-Map |
| PKCS#12 passphrase / unwrap | **UNKNOWN** | OID only | — | **STOP** (kein Unwrap) |
| embedded PKCS#12 ↔ Wire leaf Identität | **INFERENCE** | observe-only bags | dynamischer Alias-Beweis optional | nicht P0 |

---

## 6. Explicitly Rejected / No-Longer-Useful Paths

| Pfad | Status | Begründung |
|------|--------|------------|
| VIN → Key als nächster Forschungsweg | **REJECTED** | Fixed PKCS#12 in Universal-APK; kein VIN-Dataflow |
| Weitere Brute-Force auf CertificateType/Pad-u32 | **REJECTED** | 2³² bereits eindeutig `0x02000000` |
| Weitere SAS-Pad-Spekulation (`0x0AA9`, raw serial XOR, …) | **REJECTED** | Wire FACT widerspricht |
| Erneute BCL-Protokollanalyse ohne neue Capture | **REJECTED** | Transport FIELD PASS; Auth-Reject ist Credential |
| AOA als Voraussetzung des BT Connected-Pfads | **REJECTED** | SCN6 Golden Path ohne AOA |
| Weitere SDP-Suche nach alternativem Connected Entry | **REJECTED** (aktuell) | SCN 6 MEASURED; SCN 5 idle; kein neuer Entry belegt |
| Binder / TEE / Keystore / `/data/Asset` als Sign-Pfad | **REJECTED** | CASE A |
| PKCS#12 Unwrap / Private-Key-Export | **REJECTED / STOP** | Architekturwert erschöpft; rechtlich/ethisch STOP |
| Weitere `libaudio.so`-Formel-Digs | **REJECTED** | Wire-closed |
| Lab `modelId=100` / `actionId=200` als F20-IDs | **REJECTED** Transfer | LAB ONLY |
| `checkResource(true)` ⇒ Upload fehlt = Fehler | **REJECTED** | Hit ≠ Auth-Fail |
| lokaler `rhmi_state=SAS_AUTHENTICATED` ⇒ Wire-Auth | **REJECTED** | Field AUTH_REJECT |

Neue Capture-Evidence kann einzelne Punkte wieder öffnen — dann **begründen**, nicht spekulieren.

---

## 7. B3 Field Experiment

**Bewertung:** B3 ist das **informationsmaximierende** nächste Experiment.

Es verändert **eine** Variable (Credential-/Signer-Kontext) und liefert gleichzeitig:

- Gate-B2-nahe Aussage unter **autorisiertem** Kontext (live Signer, kein Key auf Pi)
- vollständige Wire-Beobachtbarkeit (Cert / Challenge / Sig / HU-Result)
- Offline-RSA-VERIFY (`sas_pad_crosscheck.py`) gegen Gate-A-Baseline
- klaren Stop vor AM/RHMI-Expansion

### Zielkette

```text
autorisierter APP/APP_AUTH-Kontext
        ↓
realer F20
        ↓
sas_certificate
        ↓
challenge
        ↓
sas_login
        ↓
HU-Ergebnis  ← Gate-B-Messpunkt
        ↓
(nur bei ACCEPT, separate Run B) AM / RHMI / CDS
```

### Erforderliche Beobachtungen

1. verwendetes Certificate / Credential (CN, Bundle-Quelle, App/Build)
2. CertificateType bzw. vollständiger relevanter Kontext (`effective_serial_u32` / APP_AUTH)
3. Challenge (16 B hex)
4. 512-Byte-Signatur
5. RSA-Verifikation gegen Wire-Certificate (`verdict=VALID`, pad `0x02000000`)
6. exaktes HU-Ergebnis (`CERTIFICATE_REJECTED` / `LOGIN_REJECTED` / `AUTHENTICATED`, `inReplyTo`-korreliert)
7. Übergang nach erfolgreicher Auth zu AM/RHMI/CDS (**nur Run B**, nach Snapshot)

### Konstant halten

Phone/BT-Link, BCL, Etch, Timing, Payloads außer Credential; **kein** PiDrive / Resource-Soak / Lab-ID-Mapping in Run A.

Runbook: product `FIELD_DAY_ONE_VARIABLE_GATE.md` · Gate-Doc `GATE_APP_AUTH_ACCEPTANCE_20261118.md`.

---

## 8. Success / Failure Criteria

| Outcome | Bedeutung | Danach |
|---------|-----------|--------|
| **SUCCESS** — `AUTHENTICATED` + korrelierter HU-Login + offline `VALID` | Kontrollierter autorisierter Kontext am F20 unter B3 belegt | Snapshot einfrieren; **Run B** (AM→RHMI→CDS); Standalone-Signer *ohne* Key-Extract evaluieren |
| **REJECT** — Cert/Login Exception trotz autorisiertem Kontext | B1-FACT vs. B3-Setup-Differenz klären (falsches Bundle / Relay / Session) | Credential-Identität prüfen — **nicht** Crypto/BCL reopen |
| **TRANSPORT FAIL** | ACL/RFCOMM/BCL bricht vor SAS | Transport-Incident — nicht als Auth-Reject lesen |
| **CRYPTO MISMATCH** — offline `INVALID` bei Capture | Capture/Reassembly-Fehler oder unerwarteter Kontext | erst Capture-Qualität, **nicht** neue Pad-Theorie |

Lab-`AUTHENTICATED` oder RSA-VERIFY allein ≠ B3-SUCCESS.

---

## 9. What Becomes Next After Positive B3

Strikt sequenziell, **Connected-Auth ≠ PiDrive**:

```text
B3 ACCEPT
  → AUTHENTICATED_SNAPSHOT
  → Run B: AM → Resource (check≠set) → RHMI → CDS
  → F20 Model-/Action-IDs messen          (UNKNOWN → FACT)
  → erst dann: PiDrive Control am F20     (OPEN)
```

Parallel (nicht blockierend für Run B): Standalone-Signierfähigkeit **ohne** Private-Key-Extraktion bewerten — Protokoll braucht MyBMW nicht; Implementierung aktuell schon.

---

## 10. What Must NOT Be Investigated Yet

Bis B3 positiv und Snapshot gesichert:

- PiDrive Field-Integration / Lab-ID-Übernahme
- Resource-Upload-Soak / RHMI-Soak am Auto
- write11/EAGAIN / Dual-ESP Discovery als Auth-Ersatz
- Fake-Auth / Unsigned-Challenge-Forge
- PKCS#12 Unwrap / Key Dump
- VIN→Key, Pad-Brute, BCL-Reopen, SDP-Alternativsuche, AOA-als-SAS
- weitere native Formel-Forensik in `libaudio.so`

---

## 11. Final FACT / INFERENCE / HYPOTHESIS / UNKNOWN Table

| Aussage | Klasse |
|---------|--------|
| Pad-u32 APP_AUTH = `0x02000000`; Pad = `MD5(02 00 00 00)` | **FACT** |
| RSA-4096 PKCS#1 v1.5 DigestInfo-MD5; Wire Cert↔Sig 8/8 | **FACT** |
| 2³² findet eindeutig `0x02000000` | **FACT** |
| Signer-Pfad CASE A in `libaudio.so` / embedded PKCS#12 | **FACT** |
| F20 akzeptiert OEM MyBMW/AAIdrive Connected-Auth (B1) | **FIELD FACT** |
| F20 zeigt nach OEM-Auth AM/RHMI/CDS auf Wire | **FIELD FACT** |
| LABSIM/reproduziertes Cert am F20 rejected (B2) | **FIELD FACT** (Reject); Gate B2 Acceptance = **OPEN** |
| Lab `f20_sim` Accept + `rhmi_*` | **LAB FACT** ≠ Field |
| MyBMW nötig für Protokollmathematik | **REJECTED** |
| MyBMW aktuell Träger der bekannten Signierfähigkeit | **FACT** |
| Kompletter Client ohne MyBMW am F20 möglich | **UNKNOWN / OPEN** |
| Alias `"com.bmwgroup.connected.bmw"` = embedded PKCS#12 identity | **INFERENCE** |
| PKCS#12 passphrase | **UNKNOWN** — **STOP** |
| VIN→private key | **REJECTED** (planning) |
| RHMI Lifecycle Lab | **CLOSED** (LAB FACT) |
| PiDrive seq Lab (`100`/`200`/`PI_DRIVE_TEST`) | **LAB ONLY** |
| F20 Model-/Action-IDs | **UNKNOWN** |
| Echte F20 PiDrive Control | **OPEN** |
| AOA Voraussetzung für BT Connected SAS | **REJECTED** |

---

## Primärer nächster Schritt

> **Ein kontrollierter B3-Feldlauf mit einem tatsächlich autorisierten APP/APP_AUTH-Kontext ist der nächste informationsmaximierende Test.**

Repository-Evidence widerspricht dieser Aussage **nicht**.  
Sie korrigiert lediglich die grobe Formel „F20 Acceptance = offen“ → **B1 FACT / B2 OPEN**, ohne den Suchraum wieder auf geschlossene Crypto-/Transport-Themen auszuweiten.
