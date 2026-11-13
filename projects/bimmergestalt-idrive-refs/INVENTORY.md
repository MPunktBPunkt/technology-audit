# Project Inventory: bimmergestalt-idrive-refs

```yaml
project_id: bimmergestalt-idrive-refs
updated: 2026-11-13
reviewed_commit: "org-BimmerGestalt-2026-10-28+sas-auth-desk-2026-11-06+zip-2026-11-13-spotcheck"
profile: lab-tool
pilot_order: [bmw-bcl, bmw-etch-rpc, bmw-sas-auth, bmw-rhmi, bmw-nbt-evo]
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
| BCL+Etch Session-Handshake (AOA→App) | `bmw-bcl` (+ etch/aoa) | Desk 2026-10-29: [`applications/bmw-bcl-handshake.md`](applications/bmw-bcl-handshake.md) |
| SAS Auth (Cert/Challenge/SecurityService) | `bmw-sas-auth` | Desk 2026-11-06: [`applications/bmw-sas-auth.md`](applications/bmw-sas-auth.md); Audit [`bmw-connected-sas-auth-2026-11-06`](../../audits/bmw-connected-sas-auth-2026-11-06/) |

Kampagnen: [bimmergestalt-idrive-2026-foreign](../../audits/bimmergestalt-idrive-2026-foreign/) ·
[bmw-connected-sas-auth-2026-11-06](../../audits/bmw-connected-sas-auth-2026-11-06/) ·
Secondary SPP/Owner: [supra-idrive6-android-auto-2026-secondary](../../audits/supra-idrive6-android-auto-2026-secondary/).

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

### Lokaler Download 2026-11-13 (ZIP, `main`)

Sieben Repos als GitHub-ZIP (`<Repo>-main/<Repo>-main/`, **ohne** `.git` → Commit-SHA am Inhalt nicht feststellbar).
Ablage: `DataAnalysis/Bimmer/`; vollständiges Manifest (SHA-256 je Datei) `Bimmer/MANIFEST_2026-11-13.json`.
Aggregat-Hash = SHA-256 über die sortierten Zeilen `<relpath>\t<sha256>\n`.

| Repo | Dateien | Bytes | Aggregat-SHA-256 (16) |
|------|--------:|------:|-----------------------|
| AAIdrive | 793 | 36 704 967 | `aa5a4f7ab1bc6528` |
| BclCarLink | 102 | 228 717 | `ed0a248d486d5663` |
| IDriveConnectAddons | 186 | 662 430 | `01981afd8f8d1ef4` |
| IDriveConnectKit | 61 | 270 249 | `1c2aa7db08b8e6ad` |
| IDriveConnectKitAndroid | 40 | 154 952 | `db9547043445e05f` |
| IDriveExperiments | 55 | 10 633 165 | `3002d6d18e402cef` |
| Simulator-kt | 111 | 317 382 | `24368a0e6e03cda1` |

Nicht im Download: wireshark_bmw_bcl, BMWConnectedAnalysis, Simulator (Dart), HassGestalt, Pages, Forks.

Stichprobe gegen die Audit-Claims (Stand 2026-10-28) — **keine Abweichung**:

| Claim (Audit) | Fundstelle im Download | Ergebnis |
|---------------|------------------------|----------|
| `SDP_BCL` = SPP `00001101-…`, `createRfcommSocketToServiceRecord` (`EVID-BCLRF-2026-11-12-001/002`) | `bcl/android/BtConnection.kt:24/38` | gleich |
| Kein RFCOMM-Server in BclCarLink | kein `listenUsing*Rfcomm*` | gleich |
| Session-Init `decodeHex("12345678")`, ~1 s Wiederholung | `bcl/client/BclClientTransport.kt:18/65` | gleich |
| `SelectProto(3)` + Knock | `BclClientTransport.kt:85`, `BclPacket.kt:51/54` | gleich |
| Watchdog Dest 5001, `13 37 13 37` | `bcl/protocols/WatchdogProtocol.kt:12/13` | gleich |
| Etch-Proxy 4007 → HU-Dest 4004, A2DP-Proxy als Discovery-Hinweis (`EVID-BCLRF-2026-11-12-005`) | `bcl/android/BtClientService.kt:53/54/71` | gleich |
| `BclOutputStream`-Bugs `ByteArray(b)` / `sliceArray(off until len)` (C-D27) | `bcl/BclOutputStream.kt:7/20` | **weiterhin vorhanden** |
| Simulator-kt Etch-Server `:4006`, kein BT | `headunit/bcl/ServerHost.kt:14`; kein `rfcomm`/`BluetoothSocket` | gleich |
| `IDriveConnection` `maxPktSize=8388608` | `IDriveConnectKit/core/.../IDriveConnection.kt:20` | gleich |
| AAIdrive BMW-Accessory per `manufacturer.contains("BMW")`, Prober-Ports 4004–4008 | `connections/UsbStatus.kt:64`, `CarProber.kt:21` | gleich |

Neu für eigene Analysen (secondary, nicht F20-[B]):

- HU-UUID `00000000-deca-fade-deca-deafdecacaff` kommt in **keinem** Code vor — nur in `IDriveExperiments/logcat.crash`
  (Z. 41790–41798, 2022-03-29: Android-UUID-Fetch eines Geräts `…:49:60` mit 1101/111e/1105/110b/110e/1133/`d31fbf50-…`/`deca-fade`).
  Der eigene F20-Capture zeigt dieselbe Menge ohne `d31fbf50-…` →
  [`esp32-bt-analyzer/applications/bmw-nbt-evo.md`](../esp32-bt-analyzer/applications/bmw-nbt-evo.md).
- BclCarLink trifft auf dem F20 rechnerisch den ersten SPP-`0x1101`-Record (HU-Kanal 6), nicht `deca-fade` (Kanal 5).

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
| `bmw-sas-auth` | applied | partial | [SHEET](../../technologies/bmw-sas-auth/SHEET.md) | [app](applications/bmw-sas-auth.md) |
| `bmw-rhmi` | applied | partial | [SHEET](../../technologies/bmw-rhmi/SHEET.md) | [app](applications/bmw-rhmi.md) |
| `bmw-nbt-evo` | documented | partial | [SHEET](../../technologies/bmw-nbt-evo/SHEET.md) | hu-probe/pidrive apps — **nicht überschrieben** |
