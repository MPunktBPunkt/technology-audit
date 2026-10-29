# Project Inventory: bimmergestalt-idrive-refs

```yaml
project_id: bimmergestalt-idrive-refs
updated: 2026-10-29
reviewed_commit: "org-BimmerGestalt-2026-10-28+c1b-desk-continuation"
profile: lab-tool
pilot_order: [bmw-bcl, bmw-etch-rpc, bmw-rhmi, bmw-nbt-evo]
```

**Reuse / Match** (Standard [0.7.1](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel | Aktion |
|--------|------|--------|
| BCL 8-Byte Framing / MUX / Handshake | `bmw-bcl` | **neu** |
| Apache Etch `BMWRemoting` IDL + SAS/AV/CDS/AM | `bmw-etch-rpc` | **neu** |
| RHMI XML + `rhmi_*` Lifecycle | `bmw-rhmi` | **neu** |
| NBT Evo als USB-MSC-Host | `bmw-nbt-evo` | **reused** (Abgrenzung Connected-App) |
| USB-MSC / Prefetch | `usb-msc` / hu-probe apps | **no overwrite** |
| USB AOA (Handshake/Rohr unter BCL) | `usb-aoa` | Desk 2026-10-28; Feld Enum 2026-10-29; Handshake/Bulk noch Gap → C1b B1/B2 |

Kampagne: [bimmergestalt-idrive-2026-foreign](../../audits/bimmergestalt-idrive-2026-foreign/).

## 14-Repo-Inventar (Org-Stand 2026-10-28 via `gh api`)

| Repo | Pin (short) | Sprache | Relevanz | iDrive/Protokoll |
|------|-------------|---------|----------|------------------|
| **BclCarLink** | `7cfd959` | Kotlin | **P0** | BCL Client, BT RFCOMM, MUX, Handshake |
| **wireshark_bmw_bcl** | `07b7982` | Lua | **P0** | Dissector; Captures → Command/Dest-Namen |
| **BMWConnectedAnalysis** | `9e96ac6` | Docs/AIDL | **P0** | BCL/Etch/Auth/RHMI/CDS RE-Doku |
| **IDriveConnectKit** | `95492b0` | Kotlin | **P0** | `BMWRemoting.etch`, RHMI-Deserialization |
| **IDriveConnectKitAndroid** | `4a567bc` | Kotlin | **P0** | ATTACHED-Intent, Connection-Listener |
| **AAIdrive** | `3e93419` | Kotlin | **P0** | SAS→RHMI/AV End-to-End Apps |
| **Simulator** | `6a38086` | Dart/Kotlin | **P1** | Fake-HU Etch :4006 |
| **Simulator-kt** | `6984020` | Kotlin | **P1** | Compose Fake-HU :4006 |
| **IDriveConnectAddons** | `270032d` | Kotlin | **P1** | CDS-Provider + RHMI Addons |
| **HassGestalt** | `63da6a4` | Kotlin | **P1** | RHMI-Listen/Tables; SmartThings-Assets |
| **IDriveExperiments** | `4b6d5fa` | Kotlin | **P2** | nur `richtext`-List-Model |
| **BimmerGestalt.github.io** | README-only | Ruby | **P2** | Pages-Hub (nicht geklont; Metadaten) |
| **ReadYou** | README-only | Kotlin | **irrelevant*** | RSS-Fork; BMW-Support nur App-Schicht |
| **breezy-weather** | README-only | Kotlin | **irrelevant*** | Wetter-Fork; BMW-Support schmal |

\*„irrelevant“ = kein belastbares Protokollwissen über BCL/Etch jenseits des generischen Addon-Musters; Begründung: Upstream-Consumer-Apps, Protokollkern liegt in Kit/BclCarLink/Analysis.

## Stack (rekonstruiert, Evidenz im Audit)

```
Transport (BT RFCOMM; Doc: USB/ENET)
    → BCL (8-Byte Header, virtuelle Kanäle)
        → Etch TCP (dest 0x0FA4 / 4004)
            → SAS Auth
            → RHMI / AV / CDS / AM / map
```

## Übersicht Sheets

| Slug | Status | Coverage | Sheet | Application |
|------|--------|----------|-------|-------------|
| `bmw-bcl` | applied | partial | [SHEET](../../technologies/bmw-bcl/SHEET.md) | [app](applications/bmw-bcl.md) |
| `bmw-etch-rpc` | applied | partial | [SHEET](../../technologies/bmw-etch-rpc/SHEET.md) | [app](applications/bmw-etch-rpc.md) |
| `bmw-rhmi` | applied | partial | [SHEET](../../technologies/bmw-rhmi/SHEET.md) | [app](applications/bmw-rhmi.md) |
| `bmw-nbt-evo` | documented | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | hu-probe/pidrive apps — **nicht überschrieben** |
