# Audit Campaign: nbt-evo-oss-runtime-hmi-bt-2026-11-19

```yaml
id: nbt-evo-oss-runtime-hmi-bt-2026-11-19
project_id: esp32-bt-analyzer
started: 2026-11-19
ended: 2026-11-19
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
source_kind: public-oss-desk-audit
related:
  - audits/supra-idrive6-android-auto-2026-secondary/
  - audits/bimmergestalt-idrive-2026-foreign/
  - audits/bimmergestalt-rhmi-checkresource-2026-11-17/
  - audits/bmw-connected-sas-auth-2026-11-06/
  - audits/esp32-bt-analyzer-f20-connected-2026-11-17/
  - audits/bmw-bcl-rfcomm-role-2026-desk/
upstream_pins:
  Sq00ky/Supra-iDrive6-Android-Auto: "0941aec"
  deathwalker80/nbt-aa-tile: "55b5fe7"
  deathwalker80/idrive-plus: "5342dc7"
  vandelayautollc/nbt-evo-toolkit: "bce20cc"
  vandelayautollc/nbt-evo-reversing: "afb9a4e"
  Xayanix/nbt-evo-ssh-unlocker: "1791228"
  tom-pryor/nbtapps: "f709ef8"
reuse_outcomes:
  reused:
    - technologies/bmw-bcl
    - technologies/bmw-etch-rpc
    - technologies/bmw-rhmi
    - technologies/bmw-sas-auth
    - technologies/bmw-nbt-evo
    - audits/supra-idrive6-android-auto-2026-secondary
  new: []
  not_helped:
    - "SAS credential path (no public key material usable for Connected auth)"
    - "HS / KNOCK / ACK10 wire semantics (absent from OSS sources)"
  process: "Desk source audit only; no implementation; no SAS bypass; plane separation enforced."
  decisions_touched:
    - fact-planes-config-vs-runtime
    - fact-nbt-aad-aa-spp-not-bcl
    - fact-native-ra-plugin-rhmi-abi
    - fact-aaidrive-rides-mybmw-bcl-tunnel
    - reject-enet-ssh-as-sas-substitute
```

## Ziel

Öffentlich einsehbare NBT-Evo-Implementierungen gegen den **bestehenden F20 Connected-Pfad**
(Phone → BT → BCL/Etch/RHMI) diffen: was erklärt Runtime/HMI/BT belastbar, was ist nur
Config/Debug-Kontext, was ist für den ArtiDrive-/`f20_sim`-Simulator verwertbar — **ohne**
den SAS-Blocker spekulativ zu umgehen.

## Scope

| Im Scope | Out of Scope |
|----------|--------------|
| NBT-AAD Daemon + RHMI Plugin + BT/SPP/Wi-Fi handoff | SAS-Key-/Credential-Rekonstruktion |
| nbt-aa-tile MOST/DSI ↔ nbt-aad Control | ENET/SSH als Ersatz für Connected-Login |
| idrive-plus Plugin↔Phone HTTP-Modell | Neue Implementierung / Simulator-Code |
| nbt-evo-toolkit RA-Plugin SDK | Wayglass-RE-Hypothesen |
| nbt-evo-reversing / SSH-Unlocker als Config-Plane | PiDrive MSC-Forschung vermischen |
| NBTApps nur auf Zusatz-Evidenz prüfen | „probably same protocol“ ohne Beleg |

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Source Matrix (Plane + Relevanz + Qualität) | erfüllt → [SOURCE-MATRIX.md](SOURCE-MATRIX.md) |
| 2 | NBT-AAD Deep Dive + Vergleichsmatrix Feldpfad | erfüllt → [NBT-AAD-DEEP-DIVE.md](NBT-AAD-DEEP-DIVE.md) |
| 3 | HU Architecture Update (Config ≠ Runtime) | erfüllt → [HU-ARCHITECTURE.md](HU-ARCHITECTURE.md) |
| 4 | Evidence Crosswalk + Negativsuche | erfüllt → [EVIDENCE-CROSSWALK.md](EVIDENCE-CROSSWALK.md) · [evidence.md](evidence.md) |
| 5 | ArtiDrive-Relevanz + Research Decision | erfüllt → [ARTIDRIVE-RELEVANCE.md](ARTIDRIVE-RELEVANCE.md) · [RESEARCH-DECISION.md](RESEARCH-DECISION.md) |
| 6 | Kein SAS-Bypass / keine Credential-Ableitung | erfüllt (explizit REJECT) |

## Kernurteil

**Unabhängige NBT-Evo-OSS erklärt die native HMI-/Plugin-/BT-SPP-Plattform und bestätigt
Nebenbeobachtungen zum Connected-Transport — aber nicht den Connected-Protokollkern.**

| Rolle | Quelle | Plane |
|-------|--------|-------|
| Connected Runtime (unmodifiziert) | AAIdrive / BclCarLink / unser F20-Feld | RUNTIME (BT→BCL→Etch→RHMI→SAS) |
| Native HU AA-Runtime | NBT-AAD | RUNTIME (AA-SPP→Wi-Fi→AA) + native RA-Plugin |
| HMI menu / CarLife tile | nbt-aa-tile, toolkit plugins | RUNTIME (HMI/MOST/DSI/IPC) |
| Plugin↔Phone over AA Wi-Fi | idrive-plus | RUNTIME (HTTP) — **nicht** BCL |
| Plugin development / ABI | nbt-evo-toolkit | INFRASTRUCTURE + HMI |
| Debug/filesystem | SSH Unlocker, reversing, toolkit flash | CONFIG/DEBUG |
| Installer (closed) | Wayglass | CONFIG — Kontrollquelle only |
| Package agent | NBTApps | RUNTIME (eigenes SPP) — wenig Zusatz zu BCL |

**Negativsuche:** `ACK10`, `KNOCK`, `HS` (Handshake), `sas_login`, `APP_AUTH` → **NO EVIDENCE**
in den auditierten OSS-Repos. BCL/`12 34 56 78`/`DEADBEEF`/`13371337` erscheinen nur als
**Fremdverkehr-Heuristik** in NBT-AAD (nicht als Connected-Client-Implementierung).

Leitplanke: *Kein hypothetischer ENET-/SSH-/Plugin-Weg ersetzt den echten SAS-Login.*

## Artefakte

| ID | Datei |
|----|-------|
| A | [SOURCE-MATRIX.md](SOURCE-MATRIX.md) |
| B | [NBT-AAD-DEEP-DIVE.md](NBT-AAD-DEEP-DIVE.md) |
| C | [HU-ARCHITECTURE.md](HU-ARCHITECTURE.md) |
| D | [EVIDENCE-CROSSWALK.md](EVIDENCE-CROSSWALK.md) |
| E | [ARTIDRIVE-RELEVANCE.md](ARTIDRIVE-RELEVANCE.md) |
| F | [RESEARCH-DECISION.md](RESEARCH-DECISION.md) |
| Evidence | [evidence.md](evidence.md) |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz |
|--------------|-----------------|-------------|------------|
| NBT-AAD ≠ Connected BCL-Pfad | Nutzt nbt-aad HS/KNOCK/Etch/SAS? | `EVID-NBTOSS-001`…`004`, Negativsuche | Ja: getrennte Runtime; Crosswalk nur Architektur |
| Native RA-Plugin ≠ Phone-RHMI über BCL | Gleiche `setData`/Etch-Wire? | `EVID-NBTOSS-010`…`014` | Plugin-ABI für Sim-Domain; nicht als Feld-Wire-Beleg |
| ENET/SSH ≠ Connected Auth | Liefert Unlocker SAS-Credentials? | `EVID-NBTOSS-030`…`032` | Nein — Config-Plane only |
| ArtiDrive: Plugin-Lifecycle modellieren? | Braucht Sim native Plugin-States? | Toolkit + NbtAad App | Ja (Domain/Runtime); Transport bleibt BCL |

## Kill-Kriterien

**Hypothese:** „Öffentliche NBT-Evo-OSS liefert den Connected SAS-/Etch-Pfad.“

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Keine Implementierung von HS/KNOCK/ACK10/sas_login in Prioritätsquellen | **getroffen** → Hypothese REJECT für Protokollkern |
| 2 | NBT-AAD nutzt eigene AA-UUID und Wi-Fi-Handoff statt BCL-Tunnel | **getroffen** |
| 3 | Manifest-`<type>Etch</type>` = Plugin-Connector, nicht Phone↔HU Etch | **getroffen** |

```text
NO JUSTIFIED KILL CRITERION (für weitergehenden SAS-Desk-Angriff)
Begründung: Audit zielt nicht auf Auth-Bypass; Kill gilt für die Vermischungshypothese oben.
```

## Bezug Inventar / Sheets

- [`bmw-bcl`](../../technologies/bmw-bcl/SHEET.md) · [`bmw-rhmi`](../../technologies/bmw-rhmi/SHEET.md) · [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md)
- Prior Secondary: [`supra-idrive6-android-auto-2026-secondary`](../supra-idrive6-android-auto-2026-secondary/)
- Feld: [`esp32-bt-analyzer-f20-connected-2026-11-17`](../esp32-bt-analyzer-f20-connected-2026-11-17/)

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk OSS 2026-11-19 | `EVID-NBTOSS-*` | dieses Audit; Sheets nur verlinken, keine Claim-Inflation ohne Feld |
