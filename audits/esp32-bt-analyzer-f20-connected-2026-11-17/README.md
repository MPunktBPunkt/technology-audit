# Audit Campaign: esp32-bt-analyzer-f20-connected-2026-11-17

```yaml
id: esp32-bt-analyzer-f20-connected-2026-11-17
project_id: esp32-bt-analyzer
started: 2026-11-17
ended: 2026-11-17
status: closed
profile: ops-field
standard_version: "0.7.1"
standard_gaps: []
upstream: https://github.com/MPunktBPunkt/esp32.bt-analyzer
upstream_commit: "4b24cf4"   # FW 0.3.20 dual-align + USB→.131 Air PARTIAL
fw: "0.3.20"
related:
  - audits/bimmergestalt-rhmi-checkresource-2026-11-17/
  - audits/bmw-connected-sas-auth-2026-11-06/
  - audits/bmw-bcl-rfcomm-role-2026-desk/
reuse_outcomes:
  reused: [bmw-bcl, bmw-etch-rpc, bmw-sas-auth, bmw-rhmi, bluetooth-a2dp]
  new: []
  process: "Evidence freeze from existing field/lab/desk docs; no new RE; epistemic tags per topic."
```

## Ziel

Den bereits erarbeiteten Bluetooth- und Connected-Stack (F20 + Lab f20_sim + Desk)
systematisch festhalten, epistemisch einordnen und offene Gates für W0–W5 markieren.

## Scope

- Im Scope: Themen 1–22 aus dem Prompt; Evidence 16./17.11.; Codec-Fix; FW 0.3.20;
  USB→`.131` Air-PARTIAL; Architekturpunkt A2DP≠RHMI.
- Nicht im Scope: neues Feld; HU-Firmware-Patch; Spekulation ohne Beleg.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | 22 Themen mit Status + Origin | erfüllt |
| 2 | Gelöst / Engpass klar | erfüllt |
| 3 | Evidence-Index | erfüllt |
| 4 | Resource-Authorization als Hauptblocker | erfüllt |
| 5 | Gemeinsame P0/P1 Next Steps (mit Audit A) | erfüllt |

---

## Was ist gelöst / Was ist der nächste Engpass

**Gelöst (bis Wire/Protokoll):** Classic-Identität & Pairing; SDP/SCN-Map; RFCOMM
MTU; BCL Handshake/MUX/WD-Beobachtung; Etch-Hashing + Tiny-Int-Codec; SAS Challenge/
Login-Größen; AM/RHMI/CDS Feldbeobachtung; f20_sim Lab-Vollpfad inkl.
ServiceException(213) und Digest-Whitelist-Stub; Architektur **A2DP allein ≠ RHMI**.

**Nächster Engpass (P0):** **Resource-Authorization** — nur Digests aus dem APP-
Zertifikat (`SAS.Digests.*`) dürfen als DESCRIPTION/IMAGEDB/TEXTDB hochgeladen
werden. Lab beweist Protokollfähigkeit; Lab beweist **nicht** F20-Autorisierung
fremder Bytes. Parallel: stabiler Watchdog auf Air-Clients (USB→`.131` brach an
`wd_echo_miss_limit` vor Menu-Upload ab).

```text
A2DP allein  ≠  RHMI
Connected + Browse / iDrive-Menü  →  RHMI (create→check→set→init→setData/actions)
```

---

## Epistemik-Schlüssel

| Tag | Bedeutung |
|-----|-----------|
| FIELD FACT | F20 / OnePlus Wire oder HCI gemessen |
| LAB FACT | f20_sim / Dummy / in-process auf Lab-Host gemessen |
| STRONG / INFERENCE | Konvergenz Feld×Lab×BG-Code, nicht allein beweisend |
| OPEN | gezielt ungeklärt |
| Desk-only | nur BimmerGestalt/Code/Doc, kein eigenes Measure |

Origin-Labels: `f20-field` · `f20-sim` · `lab` · `desk`

---

## Themenliste (1–22)

| # | Thema | Status | Origin | Beleg (kurz) |
|---|-------|--------|--------|--------------|
| 1 | Fahrzeug-/BT-Identität (BMW 38304, `D4:36:39:CF:E1:B5`, TI/ALPS, LMP, LE Host OFF, CoD, EIR, Features) | FIELD FACT | f20-field | `FIELD_A6_HU_*`, `DEEP_FORENSIC_ETCH_SAS_20261116`, BQR/HCI Events |
| 2 | Pairing/Bonding (SSP Numeric Comparison, ACL-Master, Role-Switch rejected, LSTO 5 s, 128-bit enc) | FIELD FACT | f20-field | `FIELD_A6_HU_20261113T062824Z`; BQR `mLsto`; HCI Key Size 16 B |
| 3 | SDP/Profile (ch 1–11; PSM 23/25; SCN 5=`deca-fade`; SCN 6=Connected-SPP; SCN 10 failover) | FIELD FACT | f20-field | `FIELD_B1_FROM_A6_*`; `FIELD_P0_HOLD_*` |
| 4 | RFCOMM (SABM/UA, DLCI, Credit-Based, MTU 666/667 asym, Fragmentierung) | FIELD FACT | f20-field | UIH `buf_len` 667/645 Caps-Arithmetik `FIELD_RHMI_BROWSE` |
| 5 | BCL (Header, INIT `12 34 56 78`, HS v5/iid14/buf 0x4000, SELECTPROTO, KNOCK, WD, Pair(src,dest), Payload) | FIELD FACT | f20-field | `FIELD_P0_HOLD_*`, `FIELD_BURST_*`, HS Hex L13940 in `19188` |
| 6 | BCL-Watchdog Desk vs Wire | FIELD FACT + Desk-only | f20-field / desk | Wire p50≈159,5 ms (`FIELD_P0_HOLD`); Desk BclCarLink 5 s/20 s / Port 5001 |
| 7 | Etch / BMWRemoting (DEADBEEF, sdbm 5381, Tiny-Int 0x00–0x7F/0xC0–0xFF, msgId, dest 4004, src 10–19) | FIELD FACT + LAB FACT | f20-field / f20-sim / lab | `etch_codec.py`; `DEEP_FORENSIC_*`; Tiny-Int-Fix 2026-11-17 |
| 8 | SAS (cert → 16-B challenge → 559-B login / 512-B RSA; APP_AUTH; SecurityModule) | FIELD FACT | f20-field | `DEEP_FORENSIC_ETCH_SAS_20261116`; 2×559 B in `19188` |
| 9 | AM (registerApp, addAppEventHandler, Loading-Hints; YouTube/Alexa/ScreenMirror/… — **nicht** Spotify als `am_registerApp`) | FIELD FACT + LAB FACT | f20-field / f20-sim | Frame-Rosetta `DEEP_FORENSIC_RHMI_SCREENMIRROR` §4; Lab 4× AM P0–P2; **ERRATUM 2026-11-21:** B3 zeigt genau fünf `am_registerApp` (Google/Alexa/BT/YouTube/ScreenMirror); Spotify ≠ AM — Media via `me.hufman.androidautoidrive.music` ([closure audit](../nbt-evo-bt-control-plane-closure-2026-11-21/)) |
| 10 | RHMI Lifecycle + Caps ~149 + Whitelist + ServiceException | FIELD FACT + LAB FACT + Desk | all | Caps 5306; setData×21 Feld; Lab setResource/initialize; BG Audit A |
| 11 | CDS (create, getPropertyAsync, PropertyChanged, Entertainment) | FIELD FACT + LAB FACT | f20-field / f20-sim | 37× CDS forensic; Lab inject speed/RPM sichtbar |
| 12 | AV (Fokus, PlayerState, Buttons — kein PCM über Etch) | STRONG / LAB FACT | f20-sim / desk | Lab AV path; Feld parallel A2DP ≠ Etch-PCM |
| 13 | A2DP (Sink 1.3, SBC, Bitpool, 44,1 kHz) | FIELD FACT + LAB FACT | f20-field / lab | Spotify stream `19188`; Dual-relay choppy Lab |
| 14 | AVRCP (CT 1.5, Browse, Meta; kein Cover-Art; kein Abs Volume) | FIELD FACT | f20-field | `cover art supported false` L9468; Meta tags size 0 (Source-Rolle) |
| 15 | HFP 1.6 (AT, mSBC, NREC=0, Disconnect bei unvollständigem AG) | FIELD FACT + LAB FACT | f20-field / lab | `lab_hfp_stack.py hfp-off`; B2 ohne AT+ |
| 16 | MAP / OPP (SDP) | FIELD FACT | f20-field | SDP decode B1 |
| 17 | AOA / USB-Accessory | Desk-only + OPEN | desk / lab | `usb-aoa-bmw-connected-2026-desk`; F20 AOA→BCL **OPEN** |
| 18 | BT/USB Cross-Plane (CDS Play-Intent?) | OPEN / INFERENCE | — | Hypothese; nicht F20-bewiesen |
| 19 | Screen-Mirror (~216 KiB nach onActionEvent) | STRONG | f20-field × desk | Burst 324×666 @07:32:08; Addon JPEG/`RaImageModel` |
| 20 | Tooling & Methodik | LAB FACT + Desk | lab | `METHODIK_LOG_FORENSIK.md`; HCI-TCP; btmon; BTSnoop; Golden Captures |
| 21 | Simulator f20_sim vs Simulator-kt | LAB FACT + Desk | f20-sim / desk | f20_sim 11c PASS / 121–127 host tests; BG Simulator-kt = Fake-HU Stub-Grenzen |
| 22 | Offene Gates (s. unten) | OPEN | — | § Offene Gates |

### Tiny-Int-Codec-Fix (explizit)

| | vor Fix | nach Fix (2026-11-17) |
|--|---------|------------------------|
| `rhmi_setData` Modelle (Lab `LIVE_1741`) | len-only / Abbruch | **40 Modelle** (445/446/447/451/452/456/458/462…) |
| Decode-Fehler | Abbruch | **0** |
| Track-Timeline | leer | **80** Klartext-Einträge |
| Tests | — | **122/122** (+ später 127 mit P0–P2) |

Beleg: `DEEP_FORENSIC_RHMI_SCREENMIRROR_20261117.md` §5; `tools/etch_codec.py`;
Commit-Kontext in Upstream `4b24cf4` / vorangehende Codec-Commits.

### FW 0.3.20 + USB→`.131` Air-PARTIAL

| Check | Result | Origin |
|-------|--------|--------|
| `.87` + `.131` beide 0.3.20 / sketch 1919808 | PASS | lab |
| In-process P0–P2 (SE 213, digest whitelist, menu 13598 B, 4× AM) | PASS | lab / f20-sim |
| Dual-ESP Air `.87`↔`.131` RFCOMM | FAIL | lab |
| USB `hci0` → `.131` f20_sim: RFCOMM→HS→SAS→CDS→AM→`checkResource` TX | PARTIAL | lab |
| Abort | `wd_echo_miss_limit` vor `_result_checkResource` / kein Menu-Upload | lab |

Beleg: `LAB_P0P2_FW0320_RESULT_20261117.md` + `.json`; Upstream commit `4b24cf4`.

### A2DP ≠ RHMI (Architektur)

| Lauf | A2DP Spotify | Music RHMI / setData | Beleg |
|------|--------------|----------------------|-------|
| Lab browse `BROWSE_2002` | an | **0** setData / 0 initialize (nur Calendar/News DESC) | `LAB_RHMI_BROWSE_20261116T2002Z.md` |
| Feld `19188` Connected+Browse | an | **21** `_result_rhmi_setData`, 2× `onActionEvent` | `FIELD_RHMI_BROWSE_20261117.md` |

**Schluss:** A2DP-Audioquelle allein aktiviert kein Music-RHMI. Connected-Menü /
Browse aktiviert den RHMI-Wire.

### Resource-Authorization = Hauptblocker

| Ebene | Befund |
|-------|--------|
| Desk | SHA-256 Digests in `SAS.Digests.*`; `verifyResource` in HU | Audit A |
| Lab | f20_sim `F20_STRICT_WHITELIST` / known_digests erzwingt Upload nur bekannter Digests; unknown → setResource; ImageID←0 → SE 213 | `LAB_P0_P2_RESULT_*`, FW0320 |
| Feld | `checkResource result=true` beobachtet; fremde DESCRIPTION-Autorisierung **nicht** bewiesen | `19188` L30396 |
| Gate | W2–W3 brauchen **autorisierte** Bytes (OEM-Digest-Match), nicht nur korrekte Etch-Calls | — |

---

## Offene Gates (aus Thema 22)

| Gate | Status | Blockiert |
|------|--------|-----------|
| Phone→HU Payload-Hex (Oppo loggt oft nur Länge) | OPEN | volle setResource/setData-Inhalte Feld |
| Resource-Hash-Korrelation Feld↔p7b Digests | OPEN | Whitelist-Beweis am F20 |
| ServiceException Ursache Feld (nur Typ beweisbar; 213 Lab-STRONG) | STRONG/OPEN | Cover/ImageID-Semantik |
| Vollständiger Bildnachweis Screen-Mirror | STRONG | JPEG-Inhalt auf Wire |
| Autonomer Pi-Client mit SAS | OPEN | eigener Stack ohne Phone-App |
| Action-Rückweg am F20 (ack stabil, paced) | PARTIAL | 2× onAction + 1× ack beobachtet; kontrolliert OPEN |
| USB-AOA→BCL am konkreten F20 | OPEN | Transport-Alternative |
| Dual-ESP Air-RFCOMM | FAIL (noch) | Lab-End-to-End ohne USB-Dongle |
| HU Watchdog-Timeout | OPEN | Air-Client Lifetime (USB-Lauf WD-abort) |

---

## Evidence-Index (wichtigste Docs)

Alle Pfade relativ zum Upstream-Repo **esp32.bt-analyzer** (`4b24cf4`), sofern nicht anders.

| Doc | Rolle |
|-----|-------|
| `docs/METHODIK_LOG_FORENSIK.md` | Methodik / Anti-Anchoring |
| `docs/analysis/FIELD_RHMI_BROWSE_20261117.md` | Feld RHMI Browse + Errata |
| `docs/analysis/DEEP_FORENSIC_RHMI_SCREENMIRROR_20261117.md` | YouTube/SM/SE/Codec-Fix |
| `docs/analysis/DEEP_FORENSIC_ETCH_SAS_20261116.md` | SAS/Etch/Caps Feld |
| `docs/evidence/LAB_RHMI_BROWSE_20261116T2002Z.md` | A2DP≠RHMI Lab |
| `docs/evidence/LAB_P0_P2_RESULT_20261117.md` | P0–P2 in-process PASS |
| `docs/evidence/LAB_P0P2_FW0320_RESULT_20261117.md` | FW align + USB PARTIAL |
| `docs/evidence/FIELD_P0_HOLD_20261115T132501Z.*` | BCL hold / WD timing |
| `docs/evidence/FIELD_A6_HU_20261113T062824Z.*` | Pairing / Identität |
| Commit `4b24cf4` | FW 0.3.20 dual + Retest |
| KB companion | [`bimmergestalt-rhmi-checkresource-2026-11-17`](../bimmergestalt-rhmi-checkresource-2026-11-17/) · [`NEXT-STEPS.md`](NEXT-STEPS.md) |

---

## Decision Trace (C10)

| Entscheidung | Evidence | Konsequenz |
|--------------|----------|------------|
| Resource-Auth = P0 Blocker | Audit A + Lab whitelist + Feld checkResource | W2/W3 nur mit Digest-Match |
| A2DP≠RHMI festhalten | BROWSE_2002 vs FIELD_19188 | Experimente brauchen Connected-Browse |
| Dual-ESP nicht P0 | FW0320 Air FAIL | USB/Phone-Pfad für W0–W5; Dual-ESP parallel P1 |
| WD Air zuerst | USB abort `wd_echo_miss_limit` | W0 = Watchdog stabil |

## Kill-Kriterien (C12)

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | Lab-PASS als F20-Auth behauptet | `REJECTED` |
| 2 | A2DP-only als RHMI-Beweis | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION für Stack-Existenz — Stack ist FIELD MEASURED.
Kill nur für unzulässige Claim-Transfers (Auth, A2DP=RHMI).
```

## Knowledge Feedback (C13)

| Lab/Field | Evidence | Zurück in |
|-----------|----------|-----------|
| Feld RHMI/YouTube/SM | DEEP_FORENSIC + FIELD_RHMI | `projects/esp32-bt-analyzer/STATUS.md`, `applications/bmw-bcl.md` |
| Codec-Fix | DEEP §5 | Sheet `bmw-etch-rpc` (Application-Hinweis) |
| FW0320 PARTIAL | LAB_P0P2_FW0320 | STATUS Gate matrix |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact. Lab ≠ F20-Autorisierung.
