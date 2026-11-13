# Secondary Note: supra-idrive6-android-auto-2026-secondary

```yaml
id: supra-idrive6-android-auto-2026-secondary
project_id: esp32-bt-analyzer
started: 2026-11-13
ended: 2026-11-13
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
source_kind: secondary-field-observation
reviewed_commit: "Sq00ky/Supra-iDrive6-Android-Auto@ac9a292"
upstream_pins:
  Sq00ky/Supra-iDrive6-Android-Auto: "ac9a292"
  BimmerTuner/Supra-iDrive6-Android-Auto: "fork (install automation; same lineage)"
reuse_outcomes:
  reused:
    - technologies/bmw-bcl
    - projects/bimmergestalt-idrive-refs/applications/bmw-bcl-rfcomm.md
    - projects/bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md
    - projects/esp32-bt-analyzer/applications/bmw-bcl.md
    - audits/bmw-bcl-rfcomm-role-2026-desk
  new: []
  not_helped: []
  process: "Secondary Evidence only — SPP contention + Transport-Owner confirmation; no native-AA / QNX / CarPlay desk audit."
  decisions_touched:
    - fact-hu-spp-manager-btspp
    - fact-mybmw-blocks-nbt-aad-spp
    - fact-aaidrive-parallel-warned
    - fact-looksLikeBmwBcl-heuristic
    - inference-mybmw-primary-spp-bcl-holder
    - inference-aaidrive-etch-consumer-on-mybmw-tunnel
    - messbedingung-disable-mybmw-aaidrive-for-b1
```

## Ziel

Öffentliche Quelle **NBT-AAD** (`Sq00ky/Supra-iDrive6-Android-Auto`, Fork `BimmerTuner/…`) als **Secondary Evidence** in die KB aufnehmen — ausschließlich für offene BCL-/RFCOMM-/Transport-Fragen (SPP-Contention, Transport-Owner vs. Etch-Consumer).

**Kein** Voll-Audit des nativen Android-Auto-Stacks, kein RE des QNX-Daemons, keine Wire-Level-Spekulation.

## Scope

| Im Scope | Out of Scope |
|----------|--------------|
| HU Bluetooth-SPP (`/dev/btspp*`, `SppUuidRegister`, BluetoothManager-Logs) | Native AA Video / mm-renderer / HMI / Overlay / Cluster |
| Kanal-Contention MyBMW / AAIdrive / nbt-aad | SSH-/ENET-Install, CarPlay, Wi-Fi-Direct-Details |
| Heuristik `looksLikeBmwBcl` | QNX-Prozessmanagement, Firewall, Autostart |
| Reihenfolge BT-Handshake → Wi-Fi-Credentials → AA-Session (nur wie geloggt) | Neue BCL-Header-/Kanal-/SABM-Claims jenseits expliziter Source-Zeilen |

## Klassifikation

| Feld | Wert |
|------|------|
| Typ | Secondary / Field-Observation (Issue-Logs + Daemon-Verhalten auf realen NBT-Evo-Einheiten) |
| Maturity | **R1** (mehrere Fahrzeuge; kein eigener Wire-Capture; kein eigener BCL-Parser) |
| Relation | bestätigt/ergänzt `bmw-bcl` Transport-Owner · RFCOMM-Rollen · A6/B1-Messbedingungen |

## Inventory (kurz)

```yaml
id: supra-idrive6-android-auto
name: Supra-iDrive6-Android-Auto (NBT-AAD)
url: https://github.com/Sq00ky/Supra-iDrive6-Android-Auto
fork: https://github.com/BimmerTuner/Supra-iDrive6-Android-Auto
type: secondary
relevance: high (SPP contention + transport ownership)
primary_topics:
  - bluetooth-spp-hu-side
  - channel-contention-mybmw-aaidrive
  - looksLikeBmwBcl-heuristic
status: observed
pin: ac9a292
```

## Mapping (Claims aktualisiert)

| Ort | Änderung |
|-----|----------|
| [`technologies/bmw-bcl/SHEET.md`](../../technologies/bmw-bcl/SHEET.md) | Abschnitt **Transport Owner vs. Etch Consumer** + Secondary-Fallstricke |
| [`bmw-bcl-rfcomm.md`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-rfcomm.md) | HU bietet SPP an; mehrere Parteien konkurrieren |
| [`bmw-bcl-handshake.md`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md) §3.1 | Secondary CROSSREF Owner/Consumer |
| [`esp32-bt-analyzer/bmw-bcl.md`](../../projects/esp32-bt-analyzer/applications/bmw-bcl.md) | A6/B1: MyBMW/AAIdrive während SDP/RFCOMM deaktivieren |

## Empfohlene nächste Aktion

- Kein weiterer Desk-Block für NBT-AAD nötig.
- In B1/B2-Messprotokoll: **MyBMW und AAIdrive während SDP/RFCOMM-Captures deaktivieren**, um Contention zu vermeiden und zu dokumentieren.

## Abgrenzung

- Native AA UUID/`/dev/btspp` ≠ BCL-Pfad von BclCarLink — **nicht** gleichsetzen.
- Hex-Checks in `looksLikeBmwBcl` belegen nur die **Heuristik im Secondary-Code**; BCL-Framing bleibt Desk-FACT aus BimmerGestalt (CROSSREF).
- Richtung „HU öffnet MyBMW-Link“ (nbt-aad) vs. „Phone = RFCOMM Client“ (BclCarLink) → **Spannung / UNKNOWN** bis eigenes Capture — nicht glätten.

## Bezug

[evidence](evidence.md) · Sheet [`bmw-bcl`](../../technologies/bmw-bcl/SHEET.md) · Prior [`bmw-bcl-rfcomm-role-2026-desk`](../bmw-bcl-rfcomm-role-2026-desk/)
