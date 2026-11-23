# Audit: BMW NBT Evo Bluetooth Control Plane — Closure & Reproducibility (2026-11-21)

```yaml
id: nbt-evo-bt-control-plane-closure-2026-11-21
type: closure-reproducibility-audit
scope: Bluetooth Control Plane only (SPP/BCL/Etch/SAS/RHMI/AM/CDS/AV)
not: USB-MSC · FAT/SCSI · PiDrive MSC · AOA-as-plane · generic A2DP/AVRCP deep-dive
status: closed
profile: ops-field
standard_version: "0.7.1"
claim_levels: [FIELD FACT, LAB FACT, DESK FACT, INFERENCE, HYPOTHESIS, UNKNOWN, OPEN, REJECTED]
primary_product_evidence: /home/martin/projects/bt-analyzer/docs/evidence/FIELD_B3_GATEB_20261121T112446Z/
primary_product_commit: 4d05169485930bed6dcd400517619c06a8e92df3
supersedes_status_of:
  - docs/analysis/F20_CONNECTED_GAP_AUDIT_20261120.md  # B3-next / Gate-B2 framing as P0
```

## 0. Verdict (one line)

**Fundamentales Bluetooth-Protokollwissen der NBT Evo HU ist geschlossen; offen sind vor allem Implementierungs-/Artefaktlücken für einen eigenen RHMI/AM-Client (Music DESCRIPTION, Feld-IDs, eigener App-PoC) plus Standalone-Signer.**

```text
Bluetooth Control Plane
        │
        ├── Transport       CLOSED
        ├── BCL             CLOSED
        ├── SAS             CLOSED*   (*live OEM/MyBMW path; standalone = OPEN)
        ├── RHMI            CLOSED*   (*presence/lifecycle; template bytes = GAP)
        ├── AM              CLOSED
        ├── CDS             CLOSED
        ├── AV              CLOSED
        │
        └── Own App         OPEN
              │
              ├── Music DESCRIPTION     IMPLEMENTATION GAP
              ├── field model/action IDs IMPLEMENTATION GAP
              ├── resource construction IMPLEMENTATION GAP
              └── minimal field PoC     OPEN
```

---

## 1. Evidence basis (priority order)

| Rank | Source | Role |
|------|--------|------|
| 1 | `bt-analyzer` `FIELD_B3_GATEB_20261121T112446Z/` (`EVAL.md`, `ADDENDUM_RHMI_AM_20261121.md`, `b3.jsonl`, `raw/*`, `AUTHENTICATED_SNAPSHOT.json`) | Gate B CLOSED field pack |
| 2 | Product commit `4d05169` | Evidence + `b3_profile_relay.py` |
| 3 | Prior field/lab: `DEEP_FORENSIC_ETCH_SAS_20261116`, SAS pad/RSA lab 2026-11-20, CASE A `libaudio` audits | Crypto + OEM golden path |
| 4 | This repo sheets/audits | Knowledge base — **partially stale** vs B3 |

**Repo lag (explicit):** `technology-audit` had **no** `docs/evidence/FIELD_B3_*` and still documented B3 as next step (`F20_CONNECTED_GAP_AUDIT_20261120.md`, `bmw-sas-auth/SHEET.md`). Product truth lives in `bt-analyzer`. This audit ingests that closure into the KB.

---

## 2. Decisive audit question

> Fehlt uns aktuell noch fundamentales technisches Wissen über das Bluetooth-Protokoll der NBT Evo HU, oder fehlen hauptsächlich noch konkrete Implementierungsartefakte für einen eigenen RHMI/AM-Client?

**Antwort: Implementierungsartefakte / eigener Client — nicht fundamentales Protokoll-RE.**

Begründung:

1. **Transport→BCL→Etch→SAS→AM/RHMI/CDS/AV** ist am echten F20 unter kontrolliertem B3-Profile-Relay als Kette gemessen (`Challenge → 512-B login → _result_sas_login → rhmi_* / am_* / cds_* / av_*`).
2. SAS-Mathematik (Pad `0x02000000`, MD5-XOR, RSA-4096 PKCS#1 v1.5 DigestInfo-MD5) ist Lab-geschlossen (8/8 VERIFY, 2³²).
3. Verbleibende Lücken sind: **Music DESCRIPTION-Blob** (Fingerprint bekannt, Bytes fehlen), **Feld-Model/Action/Event-IDs** für eigene App, **Resource-Konstruktion**, **minimaler PiDrive-RHMI-Feld-PoC**, **Standalone-Signer** (Weg B). Das sind Artefakt-/Implementierungslücken auf bekannter Mechanik — keine offenen Transport-/Framing-Rätsel.

---

## 3. Audit matrix

| Aussage | Status | Evidence | Reproduzierbar? | Wichtigkeit |
|---------|--------|----------|-----------------|-------------|
| Bluetooth Classic | FIELD FACT | F20 pairing/ACL; B3 topology | Ja (Feld) | P0 |
| SPP UUID `0x1101` | FIELD FACT | B3 SDP + profile_registered uuid | Ja | P0 |
| RFCOMM SCN 6 | FIELD FACT | SDP Channel 6; B3 listen/peer ch6 | Ja | P0 |
| RFCOMM fallback SCN 10 | FIELD FACT | SDP Channel 10; prior F20 map | Ja (SDP) | P1 |
| iAP2 `deca-fade` SCN 5 | FIELD FACT | Prior SDP map (nicht B3-Schwerpunkt) | Ja (SDP) | P2 |
| BCL INIT `12 34 56 78`, v5, iid 14, buf `0x4000` | FIELD FACT | Prior F20 HS + B3 BCL frames | Ja | P0 |
| BCL ports 4004/4007/4008/5001 | FIELD FACT / DESK FACT | Wire dest 4004+WD; 4007/4008 Desk+INFERENCE path labels | Ports auf Wire: ja | P0 |
| BCL mux Pair(src 10–19, dest 4004) | FIELD FACT | B3 `bcl_frame` src/dest | Ja | P0 |
| SAS algorithm (pad/XOR/MD5) | LAB FACT | SAS_PAD lab; CASE A native | Ja (offline) | P0 |
| SAS CertificateType / pad-u32 `0x02000000` | LAB FACT + FIELD (transform) | 2³²; B3 pad crosscheck | Ja | P0 |
| RSA-4096 PKCS#1 v1.5 DigestInfo-MD5, 512-B sig | LAB FACT | 8/8 VERIFY vs APP_AUTH pubkey | Ja (lab wire) | P0 |
| MyBMW/AAIdrive live login am F20 (Gate B) | FIELD FACT | B3 EVAL; `_result_sas_login` ×2 | Ja (Feld + Relay) | P0 |
| RSA-VERIFY **dieses** B3-Captures | **CLOSED** (superseded 2026-11-22) | `SAS_CRYPTO_VERIFY.json` 18/18 — [`bmw-sas-auth-field-crypto-2026-11-21`](../bmw-sas-auth-field-crypto-2026-11-21/) | Ja (offline Raw) | P0 |
| RHMI create/check/init/setData | FIELD FACT | B3 method histogram | Ja (Methoden) | P0 |
| AM `am_registerApp` ×5 | FIELD FACT | B3 jsonl + addendum packages | Ja | P0 |
| CDS properties / handlers | FIELD FACT | B3 cds_* + raw property names | Ja (Namen) | P1 |
| AV create/requestConnection | FIELD FACT | B3 `av_create` / `av_requestConnection` | Ja | P1 |
| RHMI cache behavior (11 check, 0 set, 5 init) | FIELD FACT (obs.) / INFERENCE („cached“) | jsonl methods; addendum True-claim | Methoden: ja; alle `True`: siehe §7 | P0 |
| Music app = `…music` Handle 23 | FIELD FACT (ID) / STRONG (UI-Rolle) | Addendum deep-decode | Handle-Map: deep-decode | P0 |
| Music DESCRIPTION `e9e31c31…` / 92085 B | FIELD FACT (fingerprint) / OPEN (blob) | checkResource meta in raw; **kein** Blob | Fingerprint: ja; XML: **nein** | **P0 gap** |
| Own RHMI app am F20 | OPEN | Lab stub only | Nein | P0 |
| Standalone signer (Weg B) | OPEN | AUTH_REJECT LABSIM; no standalone accept | Nein | P1 (nicht Protokoll) |

---

## 4. Layer findings (no new protocol assumptions)

### 4.1 Transport — CLOSED

- Classic + SPP `00001101-…` + SCN **6** (BCL) erneut in B3 SDP/`rfcomm_listening` bestätigt.
- SCN **10** in SDP vorhanden (Failover-Katalog bleibt FIELD FACT aus F20-Map).
- SCN **5** iAP2: Abgrenzung, nicht Control-Plane-Primärpfad.

### 4.2 BCL — CLOSED

- Handshake/INIT/SELECTPROTO/KNOCK/OPEN/WD und Multiplex dest **4004** Etch sind FIELD-gesichert.
- **KB-Widerspruch:** `technologies/bmw-bcl/SHEET.md` meldete noch `field_evidence: R0` / „keine eigene HU-Wire-FACT“ — das widerspricht F20/B3 Evidence. Sheet wird mit diesem Audit nachgezogen.

### 4.3 SAS — CLOSED* (live path) / OPEN (standalone)

| Claim | Level |
|-------|-------|
| Pad ≠ X509 serial `0x0AA9` | REJECTED (als Pad) |
| Pad-u32 = `0x02000000` | LAB FACT; B3 transform FIELD |
| Live MyBMW/AAIdrive Cert+Sig → F20 ACCEPT | FIELD FACT (Gate B CLOSED) |
| Signer CASE A in `libaudio.so` / embedded PKCS#12 | DESK/LAB FACT |
| MyBMW zwingend für Wire-Protokoll | REJECTED |
| MyBMW aktuell bekannter Signer-Träger | FACT |
| Standalone Credential Acceptance (Gate B2 / Weg B) | OPEN |
| RSA-VERIFY B3 raw cert reassembled | **CLOSED** 18/18 — see `bmw-sas-auth-field-crypto-2026-11-21` |

`*` = CLOSED für **akzeptierten autorisierten Live-Pfad**; nicht für Standalone-Reproduktion ohne MyBMW.

### 4.4 RHMI — CLOSED* (wire presence) / IMPLEMENTATION GAP (templates)

B3 method counts (jsonl, phone→hu etch):  
`rhmi_setData` 105 · `rhmi_setProperty` 16 · `rhmi_checkResource` 11 · `rhmi_initialize` 5 · `rhmi_create` 8 · `rhmi_ackActionEvent` 3 · `rhmi_onActionEvent` **0** (in diesem jsonl).

Handles (ADDENDUM STRONG deep-decode) — Handle ≠ Package-ID:

| Handle | App-ID |
|-------:|--------|
| 21 | `me.hufman.androidautoidrive.notification.readout` |
| 22 | `…calendar` |
| 23 | `…music` |
| 24 | `…mapview` |
| 25 | `io.bimmergestalt…screenmirror` |

Handle 24/25 teilen denselben DESCRIPTION/IMAGEDB-Hash → **Beobachtung**, keine gesicherte Ursache.

Event-handler IDs gesehen: `…assistant`, `…screenmirror`, `…music`.

Lab stub `modelId=100` / `actionId=200` / `PI_DRIVE_TEST` bleiben **LAB ONLY** — nicht F20-universal.

### 4.5 AM — CLOSED

Genau fünf `am_registerApp` (FIELD FACT):

| Name | Category | Package |
|------|----------|---------|
| Google | OnlineServices | `…googlequicksearchbox` |
| Screen Mirroring | Multimedia | `…screenmirror` |
| Amazon Alexa | OnlineServices | `…amazon.dee.app` |
| Bluetooth | Multimedia | `com.android.bluetooth` |
| YouTube | Multimedia | `com.google.android.youtube` |

**Spotify ≠ AM-App** in B3 (FIELD FACT). Media über `me.hufman.androidautoidrive.music` + MediaSession-Pfad (**MediaSession→RHMI-Implementierungsdetail = INFERENCE** ohne direkten Trace).

Field 5 (u16-Werte inkl. ScreenMirror `1500`): beobachtete Integer-Werte = FIELD FACT; pauschale Semantik „priority/weight“ für alle Apps = **nicht** gesichert (ScreenMirror-Source kennt `1500` als weight — DESK für diese eine App). Product-Addendum-Spalte „weight“ ist **zu stark** generalisiert → Konsistenzfund.

### 4.6 CDS / AV — CLOSED

- CDS: create/get/set/handlers + konkrete Property-Namen im Raw (FIELD FACT).
- AV: `av_create` + `av_requestConnection` (FIELD FACT). PCM weiterhin nicht über Etch.

### 4.7 Media / Cover

- ASCII `Halestorm, I Prevail`, `Spotify`, Cover-/Bildgrößen im Capture = FIELD FACT.
- „Cover = AVRCP-fed“ ohne korrelierenden Trace = **nicht** FACT → höchstens INFERENCE; B3 zeigt Connected RHMI/raw media path parallel zu klassischen Profilen.

---

## 5. Music DESCRIPTION — primary remaining BT artifact gap

| Item | Status |
|------|--------|
| Fingerprint Handle 23 DESCRIPTION `e9e31c31…` size **92085** | FIELD FACT (checkResource metadata in `phone_to_hu.bin` @ offset ~84281; size `0x0167b5`) |
| TEXTDB `1a1f84fb…` 393 B / IMAGEDB `0b010109…` 162483 B | FIELD FACT (fingerprint table) |
| Reassembled DESCRIPTION XML/bytes in repo | **ABSENT** |
| Lab fixtures `rhmi_description_lab_13598.xml` / `_13943.xml` | Match Handle 21/22 sizes — **nicht** Music 92085 |
| XML markers in B3 raw | 0× `<?xml` — Session hatte Cache-Hit, **kein** Upload |

**Evidence-Lücke (nicht durch Annahme ersetzen):** Blob muss aus AAIdrive/APK-Assets, älterem Upload-Capture oder Raw-Reassembly (falls irgendwo fragmentiert) gewonnen werden — **nicht** aus B3 Raw als vollständige DESCRIPTION.

Ohne diesen Blob: kein vollständiger Katalog Models/Actions/Events/Widgets für Music → blockiert minimalen eigenen Menü-PoC aus Music-Template.

---

## 6. Own RHMI app — what is still missing

```text
Weg A (MyBMW/AAIdrive Session + eigene Funktion)
  AUTH / RHMI / AM / CDS / AV = FIELD PROVEN
  eigener App-Eintrag am F20     = OPEN

Weg B (standalone Client)
  Protocol                     = weitgehend bekannt
  Signer credential            = OPEN
  F20 standalone acceptance    = OPEN
```

Minimal PoC needs (epistemic):

| Need | Status |
|------|--------|
| SAS auth (Weg A live) | FIELD PROVEN |
| RHMI DESCRIPTION (+ ggf. TEXT/IMAGE) mit akzeptierten Digests | IMPLEMENTATION GAP (Music blob fehlt; Whitelist-Semantik Desk/Lab) |
| AM register payload (name/icon/category/fields) | Schema FIELD; eigene App unproven |
| create → checkResource → (setResource if miss) → initialize | Mechanik CLOSED; Feld-IDs OPEN |
| Field-specific modelId / actionId / eventId | OPEN (Lab 100/200 ≠ F20) |
| Resource hashes matching HU expectation | Fingerprints known for OEM apps; own hashes OPEN |
| Reuse from Music DESCRIPTION / ScreenMirror source | Music blob missing; SM source usable as DESK pattern only |
| Lab-proven action sink | LAB ONLY |

---

## 7. RHMI cache / checkResource — evidence hygiene

| Observation | Level |
|-------------|-------|
| 11× `rhmi_checkResource` TX, 0× `rhmi_setResource`, 5× `rhmi_initialize` | FIELD FACT (`b3.jsonl` methods) |
| Addendum: 11× `_result_…=True` | FIELD claim in product pack (STRONG deep-decode) |
| Named `_result_rhmi_checkResource` in B3 jsonl | **nicht** vorhanden (HU→phone etch stark unterdekodiert: 4 etch vs 318 phone→hu; 93 decode_errors) |
| „HU hatte alle Ressourcen gecached“ | **INFERENCE** (stark): erklärt Hit→init ohne Upload; alternative „bereits whitelisted/known“ nicht ausgeschlossen |
| „check→set→init zwingend“ | REJECTED |

**Reproduzierbarkeit:** Methoden-Sequenz ohne Upload ist aus jsonl reproduzierbar. Die booleane `True`-Detailbehauptung ist im Pack dokumentiert, aber in dieser Audit-Pass nicht als benannte jsonl-Result-Events nachgezogen → **CLOSED BUT NOT FULLY REPRODUCED** für das reine Result-Bit.

---

## 8. Consistency findings (repo vs evidence)

| Finding | Severity | Location | Action |
|---------|----------|----------|--------|
| Gate B / B3 still „next“ / B2 as P0 acceptance framing | high | `F20_CONNECTED_GAP_AUDIT_20261120.md`, `bmw-sas-auth/SHEET.md` | Supersede / update |
| Spotify listed inside `am_registerApp` FIELD FACT | high | `audits/esp32-bt-analyzer-f20-connected-2026-11-17/README.md` §9 | Erratum |
| `bmw-bcl` sheet `field_evidence: R0` | high | `technologies/bmw-bcl/SHEET.md` | Upgrade to F20/B3 |
| Cache-hit still OPEN / „Vermutung“ | high | lab-field-transfer / STATUS framing | Recalibrate |
| Lifecycle blurbs imply unconditional `setResource` | medium | bimmergestalt PROTOCOL / bmw-rhmi apps | Caveat |
| AM field 5 labeled „weight“ for all apps | medium | B3 ADDENDUM (product) | Flag; don’t copy as FACT |
| FUNCTION-NOTES „XOR pad from serial“ without Wire caveat | medium | libaudio FUNCTION-NOTES | Keep REJECTED pad=serial elsewhere |
| `DEADBEEF` as F20 discovery vs Etch magic | low | f20-connected topic 7 | Frame as Etch magic |
| Lab 100/200 as F20 | — | already REJECTED | keep |
| MyBMW protocol-mandatory | — | already REJECTED | keep |
| Pad = `0x0AA9` | — | already REJECTED | keep |

---

## 9. Five-way closure classification

### CLOSED

- BT Classic identity/pairing (F20)
- SDP/SPP `0x1101`, SCN 6 (+ catalog SCN 10/5)
- BCL framing, handshake, mux, WD port, Etch dest 4004
- Etch/BMWRemoting presence (incl. DEADBEEF = Etch framing magic)
- SAS wire sequence + algorithm + pad `0x02000000` (lab) + live OEM/MyBMW acceptance (B3 Gate B)
- AM five-app register set; Spotify ≠ that set
- RHMI/AM/CDS/AV post-auth stack presence on F20
- Plane separation: BT Connected ≠ USB-MSC ≠ AOA-as-required

### CLOSED BUT NOT FULLY REPRODUCED

- B3 offline RSA-VERIFY against reassembled wire cert (pending)
- `_result_rhmi_checkResource=True` ×11 as named events (deep-decode vs jsonl gap)
- Full independent re-implementation of BCL/Etch client without AAIdrive (protocol known; own stack not field-proven end-to-end)
- Handle 21–25 map (STRONG deep-decode; not a second independent tool chain in this pass)

### IMPLEMENTATION GAP

- Music DESCRIPTION / TEXTDB / IMAGEDB **bytes** for `e9e31c31…` / related hashes
- Catalog of Music model/action/event/widget IDs from DESCRIPTION
- Own RHMI resource construction + digest alignment
- Field-specific model/action/event IDs for PiDrive entry
- Structured decode of all B3 `rhmi_setData` payloads (105× method-only in jsonl)
- Standalone signer credential path (Weg B) — implementation, not unknown wire math

### OPEN PROTOCOL QUESTION

- Full semantic definition of AM register **field 5** across all apps (values observed; meaning incomplete)
- Exact HU-side meaning of checkResource hit (cache vs whitelist-known) beyond behavioral inference
- Whether foreign (non-OEM-digest) DESCRIPTION can ever be authorized on this F20 without matching `SAS.Digests.*`
- RHMI handle allocation lifecycle rules (session-dependence) beyond one B3 observation
- Cover-art transport correlation (RHMI vs AVRCP vs other) without dedicated trace

### NOT REQUIRED (for current PiDrive Connected path)

- USB-MSC / READ10 / PiDrive storage plane as Connected control prerequisite
- AOA as BT Connected SAS prerequisite
- Further CertificateType/pad brute force
- VIN→key research
- PKCS#12 unwrap / private key export
- Re-opening BCL framing RE without new capture anomaly
- Treating Lab `100`/`200` as F20 IDs
- Screen-Mirroring-first as mandatory next step (Music template preferred)

---

## 10. Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz |
|--------------|-----------------|-------------|------------|
| Gate B CLOSED ingest | Akzeptiert F20 live APP_AUTH über B3 Relay? | `FIELD_B3_GATEB_20261121T112446Z` / `4d05169` | Ja — KB nachziehen |
| Protokoll vs Artefakt | Fehlt Wire-Semantik oder Bytes/IDs? | Matrix §3 + Music §5 | Artefakt/IDs — kein neues Protokoll-RE P0 |
| Own App next | Was blockiert PiDrive-Menü? | DESCRIPTION absent; Lab IDs REJECTED | Extract Music blob → catalog IDs → lab → one field var |
| Standalone | Blockiert Signer das Protokollverständnis? | CASE A + AUTH_REJECT | Nein — OPEN implementation only |

---

## 11. Related updates in this campaign

- `docs/analysis/F20_CONNECTED_GAP_AUDIT_20261120.md` — supersession banner
- `docs/analysis/F20_BT_CONTROL_PLANE_CLOSURE_20261121.md` — canonical short status
- `technologies/bmw-sas-auth/SHEET.md`, `bmw-bcl/SHEET.md`, `bmw-rhmi/SHEET.md` — Gate B / field_evidence
- Erratum note on Spotify/AM in `audits/esp32-bt-analyzer-f20-connected-2026-11-17/README.md`
- `audits/README.md` index row

## Primärer nächster Schritt (nicht Teil dieses Audits)

1. Music DESCRIPTION `e9e31c31…` / 92085 B extrahieren und Hash verifizieren  
2. Model/Action/Event-Katalog + Korrelation zu B3 `setData`  
3. Minimal-Template in Lab → **eine** Feldvariable (Weg A)
