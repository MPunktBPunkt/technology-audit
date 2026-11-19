# B — NBT-AAD Deep Dive

Source: `Sq00ky/Supra-iDrive6-Android-Auto@0941aec` (2026-11-19).  
Prior Secondary (SPP-Contention only): [`../supra-idrive6-android-auto-2026-secondary/`](../supra-idrive6-android-auto-2026-secondary/).

## Belegter Pfad (nicht Connected BCL)

```
Phone (Android Auto)
  ↓ BT Classic — SDP finds UUID 4de17a00-52cb-11e6-bdf4-0800200c9a66
  ↓ RFCOMM / SPP — Connectivity creates /dev/btsppN
  ↓
nbt-aad daemon (/opt/aa/nbt-aad)
  · SppUuidRegister("AndroidAuto", …) via DSI
  · wireless_setup: AA WifiStartRequest / credentials
  · skip links that looksLikeBmwBcl(...)
  ↓ Wi-Fi (CarPlay AP / hotspot handoff) + TCP AA session
  ↓ video/audio (mm-renderer / aasdk)
  │
  ├─ UDP 127.0.0.1:52790  control ("show", "quit", "media", …)
  ├─ /dev/shmem/nbt-aad-state   idle|connecting|connected <pid> <overlay>
  ├─ /dev/shmem/nbt-aad.log , nbt-aad-app.log
  └─ /opt/aa/nbt-aad.env
        ↕
RHMI Plugin  /opt/hmi/ID5/data/ro/Plugins/NbtAad/
  libNbtAad.so + NbtAad.manifest + NbtAad.xml + Texts/Images zips
  pluginAppInfo → create → onInit → updateModel / setProperty / raAction
        ↕
HmiMain3D (native HMI)
```

**FACT:** Das ist eine **native HU-Android-Auto-Runtime**, nicht der MyBMW/AAIdrive-Connected-Stack.

## Antworten auf die Audit-Fragen

| # | Frage | Antwort | Klassifikation | Quelle |
|---|-------|---------|----------------|--------|
| 1 | Welches BT-Profil? | SPP / RFCOMM über HU-Connectivity; Service-Name `AndroidAuto` | FACT | `include/bluetooth_manager.hpp`, `bluetooth_manager.cpp`, readme Wireless |
| 2 | UUID / Channel / Nodes? | UUID `4de17a00-52cb-11e6-bdf4-0800200c9a66`; Nodes `/dev/btspp0..7` (scan); RFCOMM-Kanalnummer **nicht** fest im Daemon verdrahtet (Connectivity vergibt) | FACT / UNKNOWN(channel#) | readme § Bluetooth; `main.cpp` spp scan |
| 3 | Nachrichten über BT? | Android Auto wireless setup (WifiStart / AP credentials); **kein** BCL-HS/KNOCK | FACT | `wireless_setup.cpp`, readme |
| 4 | Nach Pairing? | Daemon registriert SPP; wartet auf Phone-Open von `/dev/btsppN`; dann Handshake → Wi-Fi | FACT | Issue #18 logs; readme |
| 5 | Daten Phone→HU (BT-Phase)? | AA setup / Wi-Fi params — nicht RHMI Models | FACT | wireless_setup + readme |
| 6 | Wann Wi-Fi? | Nach erfolgreichem BT-Setup; nutzt typ. CarPlay AP (`install.md`: CarPlay temporarily required) | FACT | install.md, main.cpp wireless |
| 7 | Host-Prozessor? | OMAP/QNX Daemon `nbt-aad` | FACT | README build Armv7LE/QNX |
| 8 | HMI-Teile? | RA Plugin in `HmiMain3D` | FACT | rhmiapp/, install paths |
| 9 | Daemon↔Plugin? | State-Datei, Control-UDP, Process start/stop via menu actions; logs in shmem | FACT | main.cpp, nbt_aad_app.cpp, updating.md |
| 10 | Events Plugin→Daemon? | Start / Force Stop / Restart / show overlay / settings flags | FACT | NbtAad.xml raActions; app logs Issue #37 |
| 11 | Events von iDrive? | raAction / focus handlers; MENU; CDS (gear, PDC) | FACT | nbt_aad_app.cpp; Issue #37 |
| 12 | Beobachtbare States? | `idle\|connecting\|connected`; overlay; GapErrorCode; btspp open | FACT | `/dev/shmem/nbt-aad-state`; logs |
| 13 | Ähnlichkeit zu BCL/Etch/RHMI? | **Strukturell:** BT serial + separates HMI-Plugin. **Protokollisch:** AA ≠ BCL; native Plugin-RHMI ≠ Phone-RHMI-over-Etch | INFERENCE (ähnlich) / REJECTED (gleich) | siehe Matrix |

## PluginApp-Lifecycle (rekonstruiert)

```
HmiMain3D scans /opt/hmi/ID5/data/ro/Plugins/NbtAad/
  ↓ NbtAad.manifest  (pluginAppConnector type=Etch id=210 — in-process connector)
  ↓ DescFile NbtAad.xml  (hmiStates, raActions, models)
  ↓ dlopen libNbtAad.so → pluginAppInfo {abi, name, vendor, create, destroy}
  ↓ create(...) → onInit: addHandler(raAction…), updateModel, setProperty
  ↓ User Action → spawn/control /opt/aa/nbt-aad
  ↓ HMI state / overlay blank state (hmiState 13 pattern like CarPlay)
```

| Stufe | Klassifikation | Beleg |
|-------|----------------|-------|
| Discovery + three-file anatomy | FACT | install/updating; toolkit docs (parallel); NbtAad.manifest |
| `pluginAppInfo` / create / onInit | FACT | `rhmiapp/nbt_aad_app.cpp` header comments + symbols |
| `updateModel` / `setProperty` / `addHandler` | FACT | same + toolkit `06-runtime-api-reference.md` |
| Manifest `<type>Etch</type>` = Phone↔HU Etch over BCL | **REJECTED** | Connector für RA-Plugin-Framework; nicht BCL-Kanal |
| Native `setData` wire == Connected RHMI `setData` über Etch | **UNKNOWN** / nicht gleichsetzen | Shared framework names ≠ same transport |

## Vergleichsmatrix: NBT-AAD vs unser F20-Feldpfad

| Merkmal | NBT-AAD | Unser Feldpfad (F20 Connected) | Bewertung |
|---------|---------|--------------------------------|-----------|
| Bluetooth Pairing | Voraussetzung; Re-pair bei fehlendem btspp | Voraussetzung; direkte Phone↔HU | **ähnlich** (Vorbedingung) — Issue #18 / Feld |
| SDP | HU registered AA UUID via `SppUuidRegister` | HU bietet SPP (+ iAP); Phone/App als Client | **teilweise** — andere UUID/Rolle |
| RFCOMM/SPP | `/dev/btsppN` message-oriented | SCN 6/10 SPP MEASURED | **ähnlich** Transportklasse; **anders** Nutzung |
| UUID | `4de17a00-52cb-11e6-bdf4-0800200c9a66` | Companion/BCL SPP (nicht diese AA-UUID) | **verschieden** |
| Channel | Connectivity-vergeben; nicht hardcodiert | Field SCN 6 (failover 10) | **verschieden** / nicht vergleichbar 1:1 |
| Initialisierung | AA wireless setup on btspp | BCL `INIT 12345678` → HS → … | **verschieden** |
| Session | aasdk over Wi-Fi/TCP | BCL OPEN ports + Etch | **verschieden** |
| HS | **NO EVIDENCE** | MEASURED | **NO EVIDENCE** in NBT-AAD |
| KNOCK | **NO EVIDENCE** | MEASURED | **NO EVIDENCE** |
| ACK10 | **NO EVIDENCE** | MEASURED | **NO EVIDENCE** |
| Etch (Phone↔HU) | Nur als **Fremdverkehr** erkannt (`looksLikeBmwBcl`) | Kerntransport | **detect-only** ≠ implement |
| RHMI | Native RA Plugin in HmiMain3D | Remote RHMI over Etch nach SAS | **ähnliche UI-Abstraktion, anderer Transport** |
| setData | Framework `updateModel`/`setProperty` in-process | Etch `setData` wire | **nicht gleichsetzen** |
| Actions | `raAction` / `addHandler` | Action Events over Etch | **architektonisch verwandt, Wire anders** |
| HMI Plugin | Ja (`NbtAad`) | Connected Apps erscheinen remote | Plugin-SDK relevant für Sim-Domain |
| Wi-Fi handoff | Kernpfad nach BT setup | Connected bleibt auf BT/BCL (unser Feld) | **NBT-AAD-spezifisch** |
| TCP | AA session | nicht unser Feld-Connected-Kern | unrelated for BCL |
| Screen/video | AA video path | Screen-Mirror-Burst over RHMI/Etch | **andere Mechanismen** |
| Auth/SAS | **kein** SAS; Konflikt mit MyBMW/AAIdrive | SAS Blocker | **NO EVIDENCE** for SAS solution |

Quellen je Zeile: NBT-AAD `milestone-7/readme.md` Wireless + Plugin; `wireless_setup.cpp`; Feld CROSSREF `esp32-bt-analyzer-f20-connected-2026-11-17` / `bmw-nbt-evo` Sheet BT-Zeile.

## BCL-Heuristik (Secondary — bestätigt Prior)

`looksLikeBmwBcl`: `12 34 56 78`, Etch-ish `DEADBEEF`, WD `13371337`, self-consistent 8-byte BCL header.  
Source-Kommentar: AAIdrive hat **keinen** eigenen BT-Link; fährt auf MyBMW BCL; HU `A4AHandler` auf `/dev/btspp0`.

→ **supports** bestehende Transport-Owner-INFERENCE; **kein** neuer SAS-/Etch-Wire-FACT.

## Firewall / Lifecycle

| Artefakt | Rolle |
|----------|-------|
| `pf_aa` | Packet-filter helper für AA Wi-Fi path (`--install`/`--check`) |
| Single-instance | UDP bind `52790`; zweites Start sendet `show` |
| Autostart | Plugin + flag / settings; Restart recreates SPP registration |

## Abgrenzung zu AAIdrive

README/install: paralleles AAIdrive **bricht** NBT-AAD. Das bestätigt Contention am SPP-Raum — **kein** Beweis, dass NBT-AAD denselben Protokollstack spricht.
