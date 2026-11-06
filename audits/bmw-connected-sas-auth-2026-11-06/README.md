# Audit Campaign: bmw-connected-sas-auth-2026-11-06

```yaml
id: bmw-connected-sas-auth-2026-11-06
project_id: bimmergestalt-idrive-refs
related_projects: [hu-probe, esp32-usb-analyzer]
started: 2026-11-06
ended: 2026-11-06
status: closed
profile: planning
standard_version: "0.7.1"
reuse_outcomes:
  reused:
    - technologies/bmw-bcl
    - technologies/bmw-etch-rpc
    - technologies/bmw-rhmi
    - technologies/usb-aoa
    - audits/bimmergestalt-idrive-2026-foreign
    - audits/usb-aoa-bmw-connected-2026-desk
    - projects/bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md
  new:
    - technologies/bmw-sas-auth
    - audits/bmw-connected-sas-auth-2026-11-06/AUDIT-REPORT.md
  not_helped: []
  process: "Quellenkritisches Desk-Audit (S1–S6 + Nachfolge-Repos). Keine Firmware, keine Protokoll-Implementierung, keine Secrets-Extraktion."
```

## Ziel

Vollständiges, evidenzklassifiziertes Reverse-Engineering-/Source-Audit des
**BMW Connected Apps Authentication**-Verfahrens (SAS über Etch), als technische
Grundlage für einen späteren F20/NBT-Evo-Feldtest mit Android + MyBMW/Connected +
AAIdrive + ESP32-Analyzer.

## Scope

- Im Scope: öffentliche Quellen (hufman Story, BMWConnectedAnalysis, AAIdrive,
  IDriveConnectKit(+Android), BclCarLink, Addons, Simulator, Wireshark-Dissector),
  Rekonstruktion der Auth-Sequenz, Abgrenzung Auth/Authz, Mapping auf Gates G1–G4
  (dieses Audit), Messmatrix ESP32, Feld-Run-Sheet.
- Nicht im Scope: Firmware-Änderungen, neue Protokoll-Stacks, Extraktion/Publikation
  privater Schlüssel, Wire-Captures erzeugen.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Sieben Leitfragen beantwortet mit Evidenzgrad | erfüllt → `AUDIT-REPORT.md` §24 |
| 2 | SAS-Sequenz aus IDL + Code + Doc rekonstruiert | erfüllt |
| 3 | AOA/BCL ≠ SAS explizit getrennt | erfüllt |
| 4 | Feld-Run-Sheet für G3-Erstbeleg | erfüllt §22 |
| 5 | Technology Sheet `bmw-sas-auth` angelegt | erfüllt |

## Artefakte

| Datei | Inhalt |
|-------|--------|
| [`AUDIT-REPORT.md`](AUDIT-REPORT.md) | Vollbericht Struktur 1–24 |
| [`evidence.md`](evidence.md) | Evidence-IDs `EVID-SAS-*` |
| [`../../../technologies/bmw-sas-auth/SHEET.md`](../../technologies/bmw-sas-auth/SHEET.md) | Technology Sheet |
| [`../../projects/bimmergestalt-idrive-refs/applications/bmw-sas-auth.md`](../../projects/bimmergestalt-idrive-refs/applications/bmw-sas-auth.md) | Project Application |

## Pins (shallow clone 2026-11-06)

| Repo | Commit |
|------|--------|
| AAIdrive | `3e93419` |
| IDriveConnectKit | `95492b0` |
| IDriveConnectKitAndroid | `4a567bc` |
| BclCarLink | `7cfd959` |
| BMWConnectedAnalysis | `9e96ac6` |
| Simulator | HEAD shallow (SAS stub in `BMWRemotingServerImpl.kt`) |
| Narrative | https://hufman.github.io/stories/bmwconnectedapps |

## Wichtige Abgrenzung

**AOA/BCL evidence ≠ SAS authentication evidence.**  
Bestehende hu-probe AOA-Enum-/MSC-Messungen belegen **nicht** G3.
