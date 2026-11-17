# Audit Campaign: esp32-bt-analyzer-lab-field-transfer-2026-11-17

```yaml
id: esp32-bt-analyzer-lab-field-transfer-2026-11-17
project_id: esp32-bt-analyzer
started: 2026-11-17
ended: 2026-11-17
status: closed
profile: ops-field
standard_version: "0.7.1"
standard_gaps: []
upstream: https://github.com/MPunktBPunkt/esp32.bt-analyzer
upstream_commit: "1100644"   # PiDrive UI seq PASS; soak a5187cb; write11 freeze 0b7f06e
fw: "0.3.20"
related:
  - audits/esp32-bt-analyzer-f20-connected-2026-11-17/
  - audits/bimmergestalt-rhmi-checkresource-2026-11-17/
  - audits/bmw-connected-sas-auth-2026-11-06/
reuse_outcomes:
  reused: [bmw-rhmi, bmw-etch-rpc, bmw-sas-auth, bmw-bcl]
  new: []
  process: "Evidence freeze Lab PASS (soak/seq/lifecycle) vs Field-OPEN; claim hygiene; no new RE."
```

## Ziel

Lab-PASS und F20-Feld **auseinanderziehen**, wo sie auseinanderlaufen — Claim-Grenze,
Action-/Resource-Semantik, Freeze-Hygiene. **Nicht** den bereits gewonnenen
Connected-Transport / write11-Ursachenkette erneut aufmachen.

## Scope

- Im Scope: Themen 1–6 (Claim-Grenze, Action→PiDrive, Resource-Lifecycle F20,
  Freeze-Hygiene, modelId 4 / SE 213, EAGAIN-Budget).
- Nicht im Scope: write11-/Panic-/Dual-ESP-Ursachenforschung; weitere Model-ID-
  Sammlungen; erneute 10‑min-Soak ohne neues Protokollziel; Transport-W0 als P0.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | LAB FACT Pin (`1100644`/`a5187cb`) vs Auto-OPEN klar | erfüllt |
| 2 | Action 200 / PI_DRIVE_TEST als Lab-Sink, nicht F20-Semantik | erfüllt |
| 3 | Resource-Lifecycle F20: Hit/Miss/Auth getrennt; Stub ≠ Feld | erfüllt |
| 4 | FREEZE_C5CB0E6 ESP/RFCOMM „OPEN P0“ gegen write11-Stand bereinigt | erfüllt |
| 5 | SE 213 / modelId 4 = Nebenpfad; EAGAIN = Dimensionierung | erfüllt |
| 6 | NEXT-STEPS ohne write11/W0-Reopen | erfüllt |

---

## Was ist gelöst / Was ist der nächste Engpass

**Gelöst (Lab Wire, mybmw-sim ↔ f20_sim):**

| Meilenstein | Commit / Evidence | claim_level |
|-------------|-------------------|-------------|
| EAGAIN-Retry → Lifecycle `RUNTIME_ACTIVE` ~90 s | `ffd28aa` · `0b7f06e` · `LAB_P0_RHMI_LIFECYCLE_PASS` | LAB FACT |
| 10‑min Soak: 97 setData, 105 Action/Ack | `a5187cb` · `LAB_P0_RHMI_SOAK_PASS` | LAB FACT |
| UI-Sequenz → `selected_action=PI_DRIVE_TEST` | `1100644` · `LAB_P0_RHMI_PIDRIVE_SEQ_PASS` | LAB FACT |
| write11: TX-pressure, nicht Panic; Retry = Lab-Default | `LAB_P0_WRITE11_MASTER` | LAB FACT |

**Nächster Engpass (vor Auto):** **Feld-Übertragbarkeit** — Resource-Auth
(Digest-Match), echte F20-Model-/Action-IDs/Handles, SAS/App-Kontext. Lab beweist
Protokoll + eigene Sink-Semantik; Lab beweist **nicht** F20-Autorisierung oder
F20-Action-Map.

```text
Lab PASS  ≠  F20 Auto-ready
Connected-Transport gewonnen  →  Claim-Freeze; nächster Nutzen = Semantik/Auth
```

---

## Epistemik-Schlüssel

| Tag | Bedeutung |
|-----|-----------|
| FIELD FACT | F20 / OnePlus Wire oder HCI gemessen |
| LAB FACT | f20_sim / Dummy / in-process auf Lab-Host gemessen |
| STRONG / INFERENCE | Konvergenz Feld×Lab×BG-Code |
| OPEN | gezielt ungeklärt |
| SUPERSEDED | älterer Freeze-Status durch späteren Stand ersetzt |

---

## 1. Claim-Grenze Lab vs Field (Hoher Nutzen)

**Frage:** Was gilt nach `1100644` / `a5187cb` als LAB FACT — und was gilt **noch
nicht** fürs Auto?

### LAB FACT (Pin)

| Claim | Beleg | Gilt für Auto? |
|-------|-------|----------------|
| checkResource→(Miss)setResource→initialize→setData→`RUNTIME_ACTIVE` ~90 s Dual+Single | `LAB_P0_RHMI_LIFECYCLE_PASS` | **Nein** — nur Lab-HU |
| 10 min Soak, 97× setData(100/101), 105× Action/Ack, 0 Session-Abort | `LAB_P0_RHMI_SOAK_PASS` / `a5187cb` | **Nein** |
| setData(100,"PiDrive") → actionId **200** → Sink `PI_DRIVE_TEST` | `LAB_P0_RHMI_PIDRIVE_SEQ_PASS` / `1100644` | **Nein** — Lab-Sink |
| EAGAIN transient; Retry/Poll (Budget 2 s) stellt Session wieder her | `ffd28aa` · WRITE11 CAP_RETRY | Lab-Write-Policy; Feld-Stack unbekannt |
| WATCHDOG_MISS als primäre Lab-Ursache (nach Retry) | `REJECTED` | — |
| ESP Panic / Dual-ESP als primäre write11-Ursache | `REJECTED` | — |
| ServiceException 213 auf modelId 4 (Image-Ident) non-fatal | Lifecycle + Soak | Nebenpfad |

### Noch nicht fürs Auto (OPEN / Desk)

| Gap | Warum Lab nicht reicht | Origin-Erwartung |
|-----|------------------------|------------------|
| **Resource-Auth** — SHA-256 in `SAS.Digests.*` | f20_sim Whitelist = Stub; fremde Bytes am F20 unbewiesen | f20-field × p7b |
| **Echte F20-Model-IDs** | Lab 100/101 / Demo-XML ≠ Multimedia 445/446/447 Feld-Hex | f20-field Relay |
| **Echte F20-Action-IDs / Handles** | Lab inject `actionId=200` / handle 12 = Sim-Konvention | f20-field |
| **SAS/App-Kontext** | Lab mybmw-sim Cert/Digests ≠ Phone APP_AUTH am F20 | f20-field |
| Phone→HU Payload-Hex | Oppo oft nur Länge | Relay / btmon |

**Kill:** Lab-PASS als „F20 Auto-ready“ behaupten → `REJECTED` (Claim-Transfer).

---

## 2. RHMI Action → PiDrive-Mapping (Hoher Nutzen)

**Risiko:** Schein-PASS ohne Feld-Semantik.

### Lab-Kette (FACT)

```text
setData(100, "PiDrive")
    → HU MENU_TEST_ACTION (actionId=200)     # f20_sim / DEMO_PIDRIVE_XML
    → phone rhmi_onActionEvent
    → pidrive_action_sink → selected_action = PI_DRIVE_TEST
    → rhmi_ackActionEvent
```

Pin: Dual-ESP ~94 s · `LAB_P0_RHMI_PIDRIVE_SEQ_DUAL_20261117T220723Z` · commit `1100644`.

| Element | Lab-Wert | Epistemik |
|---------|----------|-----------|
| modelId Label | 100 | LAB (Demo-XML) |
| actionId | **200** (`MENU_TEST_ACTION`) | LAB — hardcodiert in `bcl_dummy_hu` / Seq-Harness |
| handle | 12 (Beispiel-Lauf) | LAB — session-lokal |
| Sink | `PI_DRIVE_TEST` | LAB — **eigene** Semantik, nicht HU-OEM |

### Feld (was fehlt)

| Beobachtung | Status | Beleg |
|-------------|--------|-------|
| `rhmi_onActionEvent` ×2 + 1× ack im Browse-Lauf | FIELD FACT (Existenz) | `FIELD_RHMI_BROWSE` / `19188` |
| Konkrete actionId / Handle / Model-Map | **OPEN** | Phone→HU oft ohne Hex |
| Mapping Action → PiDrive-Produktaktion am F20 | **OPEN** | kein Feldversuch |

**Schluss:** Lab beweist *dass* Action→interne Sink deterministisch verdrahtbar ist.
Lab beweist **nicht**, welche F20-Action-IDs welche PiDrive-Aktionen auslösen.
Vor Feld: Action-IDs aus DESCRIPTION/Caps oder Relay-Hex gewinnen — nicht 200
als universell übernehmen.

---

## 3. Resource-Lifecycle am echten F20 (Hoher Nutzen)

Drei Mechanismen getrennt halten (Audit A + Lifecycle-Audit Upstream):

| Mechanismus | Rolle | Lab | Feld |
|-------------|-------|-----|------|
| `checkResource` (MD5) | Cache Hit/Miss | PASS Timeline Miss→set | `checkResource result=true` beobachtet; Folge OPEN |
| `verifyResource` / Digests | Auth | Stub whitelist PASS | fremde Bytes **nicht** bewiesen |
| `setResource` | Upload nur bei Miss | PASS bei DESCRIPTION Miss | Pflicht nur bei `false`; Hit ≠ Fehler |

**Lab-Sequenz (nach EAGAIN-Retry):**

```text
checkResource(DESCRIPTION) → miss → setResource
checkResource(TEXTDB) → reply
checkResource(IMAGEDB) → reply
initialize → setData → RUNTIME_ACTIVE
```

**f20_sim-Stub vs F20:** Simulator akzeptiert bekannte Digests / Demo-Packs.
Echter F20 enforce `CRHMIAuthPermHandler::verifyResource` gegen Cert-Digests —
Lab-PASS ≠ Cache-Hit-Semantik am Auto und ≠ Auth-PASS.

**Feld-Fokus (nicht erneut: Transport):**

1. Hit/Miss-Matrix DESCRIPTION / TEXTDB / IMAGEDB (messageId / inReplyTo).
2. setResource **nur** bei Miss; Bytes vs `SAS.Digests.*`.
3. initialize korreliert; kein erzwungenes setResource nach `true`.

---

## 4. Epistemik / Freeze-Hygiene (Hoher Nutzen)

### Problem

`FREEZE_C5CB0E6_HOME_SESSION_20261117` markierte **ESP panics** und **RFCOMM flaps**
noch als **OPEN (P0)** und empfahl, F20 `WATCHDOG_MISS` nicht neu zu lesen, bis
Flaps korreliert sind. Das lädt dazu ein, write11/W0 erneut als Connected-Blocker
zu behandeln.

### Bereinigung (dieser Audit)

| Älterer Status (c5cb0e6) | Aktueller Stand | Tag |
|-------------------------|-----------------|-----|
| ESP panics = OPEN P0 | write11-Batches: bootGen unverändert; Panic **nicht** primär | **SUPERSEDED** → nicht P0 Connected |
| RFCOMM flaps = OPEN P0 | `write_error:11` = EAGAIN/TX-pressure; Retry → Lifecycle PASS | **SUPERSEDED** → Lab-Default Retry; Backpressure-Quelle = P2 |
| checkResource return path unexplained | Lab: reply nach Retry sichtbar; Fall A „HU kein Reply“ bleibt REJECTED | Lab PASS; Feld-Miss weiter transport-kandidatisch, **nicht** W0-Reopen |
| Preferred class: RFCOMM/ESP loses session | Primär: fail-fast close bei EAGAIN | **SUPERSEDED** durch WRITE11_MASTER + RETRY |

**Freeze-Regel für die KB:**

```text
DO NOT reopen: write11 Ursachenkette · Dual-ESP Panic · W0 „HU antwortet nicht“
DO track:     Resource-Auth · F20 Action/Model-IDs · SAS/App-Kontext
P2 only:      EAGAIN backpressure source / Histogramm (Dimensionierung)
```

Verweis Upstream: `docs/evidence/LAB_P0_WRITE11_MASTER_20261117.md`,
`LAB_P0_RHMI_LIFECYCLE_PASS_20261117.md`. Home-Session Connected/Pairing/CDS/RHMI
PASS aus c5cb0e6 **bleibt** gültig; nur die P0-Transport-Hypothesen sind ersetzt.

---

## 5. modelId 4 / ServiceException 213 (Mittlerer Nutzen)

| Aspekt | Befund | Epistemik |
|--------|--------|-----------|
| Lab bootstrap setData modelId **4** (`RHMIResourceIdentifier` / Image-Pfad) | `rhmi_setdata_reject` errorCode **213** „SetData was not successful.“ | LAB FACT |
| Session | bleibt `RUNTIME_ACTIVE`; Soak/Seq ungestört | LAB FACT |
| Desk Mock | ImageID←0 → SE 213 (AAIdrive Mock, MY2019) | Desk FACT |
| Feld | SE-Typ `0x5A6F115C` beobachtet; errorCode jenseits Byte 32 oft undekodiert | STRONG/OPEN |
| Blockiert Lifecycle / Action-Pfad? | **Nein** | — |

**Bewertung:** Validierung bekannter ImageID-Semantik vs. Client-Bug am Demo-Model 4 —
**Nebenpfad**. Kein P0 vor F20; keine Blockade für Action/Resource-Auth-Arbeit.
Vollständige Feld-Dekode = P1 parallel (wie Audit B Gate).

---

## 6. EAGAIN-Histogramm / Retry-Budget (Mittlerer Nutzen)

| Knob / Signal | Lab-Wert | Rolle |
|---------------|----------|-------|
| `BCL_WRITE_EAGAIN_S` | default **2.0** s (`0` = fail-fast) | Budget |
| `BCL_WRITE_EAGAIN_POLL_S` | **0.02** s | Poll |
| CAP_RETRY Dual | recovered 2×; max ~11 retries / ~0.20 s Wait | Dimensionierung |
| CAP_RETRY Single | recovered 2×; max ~6 / ~0.12 s | Dimensionierung |
| Soak 10 min | EAGAIN events 4 / recovered 2 | unter Last ok |
| Backpressure *source* (Queue/Bridge/Credits) | **OPEN** | P2 — nicht Ursachen-P0 |

**Schluss:** Dimensionierung, nicht Ursachenforschung. Fail-fast war der Lab-Bug;
Retry ist Default. Histogramm-Vertiefung lohnt nur für Budget-Tuning eigener
Clients — **nicht** um Connected-Transport erneut zu „gewinnen“.

---

## Offene Gates (nach diesem Freeze)

| Gate | Status | Blockiert |
|------|--------|-----------|
| F20 Digest-Korrelation Upload ↔ p7b | OPEN | W2 Auth |
| F20 Action-ID / Handle / Model-Map | OPEN | W5 Semantik |
| Lab actionId 200 → Feld übernehmen | **REJECTED** as claim | Schein-PASS |
| FREEZE_C5CB0E6 ESP/RFCOMM als Connected-P0 | **SUPERSEDED** | — |
| write11 / Dual-ESP Panic als P0 | **CLOSED** (Lab) | nicht wieder öffnen |
| SE 213 modelId 4 | Nebenpfad | nicht W0–W5 |
| EAGAIN source | P2 OPEN | Dimensionierung |

---

## Evidence-Index

Pfade relativ Upstream **esp32.bt-analyzer** (`1100644`), sofern nicht anders.

| Doc | Rolle |
|-----|-------|
| `docs/evidence/LAB_P0_RHMI_PIDRIVE_SEQ_PASS_20261117.md` | Action→PiDrive Lab |
| `docs/evidence/LAB_P0_RHMI_SOAK_PASS_20261117.md` | 10‑min Soak |
| `docs/evidence/LAB_P0_RHMI_LIFECYCLE_PASS_20261117.md` | Lifecycle nach Retry |
| `docs/evidence/LAB_P0_WRITE11_MASTER_20261117.md` | write11 Freeze |
| `docs/evidence/LAB_P0_WRITE11_CAP_RETRY_*/ANALYSIS.md` | EAGAIN Budget |
| `docs/analysis/FREEZE_C5CB0E6_HOME_SESSION_20261117.md` | älterer Freeze (P0 SUPERSEDED) |
| `docs/analysis/AUDIT_RHMI_RESOURCE_LIFECYCLE_20261117.md` | check≠set≠verify |
| `docs/analysis/FIELD_RHMI_BROWSE_20261117.md` | Feld Action-Existenz |
| KB prior | [`esp32-bt-analyzer-f20-connected-2026-11-17`](../esp32-bt-analyzer-f20-connected-2026-11-17/) · [`bimmergestalt-rhmi-checkresource-2026-11-17`](../bimmergestalt-rhmi-checkresource-2026-11-17/) |
| [`NEXT-STEPS.md`](NEXT-STEPS.md) | Feld-Semantik zuerst |

---

## Decision Trace (C10)

| Entscheidung | Evidence | Konsequenz |
|--------------|----------|------------|
| Lab-PASS ≠ Auto-ready | Soak/Seq + Auth OPEN | Claim-Grenze P0 dokumentieren |
| actionId 200 nicht F20-universell | Harness hardcode + Feld ohne Hex | Mapping-Audit vor Feld-Action |
| FREEZE_C5CB0E6 P0 Transport SUPERSEDED | WRITE11_MASTER + Lifecycle PASS | write11/W0 nicht reopen |
| SE 213 / EAGAIN nachrangig | non-fatal; Budget gemessen | mittlere Priorität |

## Kill-Kriterien (C12)

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Lab Soak/Seq als F20-Feld-Semantik behauptet | `REJECTED` |
| 2 | actionId 200 / PI_DRIVE_TEST als OEM-F20-Map | `REJECTED` |
| 3 | write11/ESP-Panic wieder als Connected-P0 ohne neue Evidence | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION für Lab-Stack-Existenz — Lab Connected RHMI ist MEASURED.
Kill nur für unzulässige Claim-Transfers (Lab→Auto, Sink→OEM-Action).
```

## Knowledge Feedback (C13)

| Lab/Field | Evidence | Zurück in |
|-----------|----------|-----------|
| Claim-Grenze + Freeze-Hygiene | dieser Audit | `STATUS.md`, `bmw-rhmi` Sheet, NEXT-STEPS |
| Action 200 Lab-only | SEQ_PASS | Sheet Fallstricke |
| Resource Hit/Miss/Auth | Lifecycle + Audit A | Sheet Lifecycle-Hinweis |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact. Lab ≠ F20-Autorisierung ≠ F20-Action-Map.
