# Evidence — nbt-evo-oss-runtime-hmi-bt-2026-11-19

Desk OSS audit 2026-11-19 · `standard_version 0.7.1`.  
Pins: siehe [README.md](README.md) `upstream_pins`.

Feldschema (Audit-Auftrag §14) verkürzt in Tabellen; volle Crosswalk-Zeilen in [EVIDENCE-CROSSWALK.md](EVIDENCE-CROSSWALK.md).

## FACT

| ID | claim | source | source_path | confidence | plane | sim |
|----|-------|--------|-------------|------------|-------|-----|
| `EVID-NBTOSS-001` | NBT-AAD registriert SPP `AndroidAuto` / UUID `4de17a00-52cb-11e6-bdf4-0800200c9a66` via DSI `SppUuidRegister` | Sq00ky@0941aec | `milestone-7/include/bluetooth_manager.hpp`; `src/bluetooth_manager.cpp`; `readme.md` | high | RUNTIME | TRANSPORT |
| `EVID-NBTOSS-002` | Nach Phone-Open: `/dev/btsppN` → wireless handshake → Wi-Fi credentials / AA session | Sq00ky | `main.cpp` wireless; Issue #18 logs; `readme.md` | high | RUNTIME | TRANSPORT/RUNTIME |
| `EVID-NBTOSS-003` | `looksLikeBmwBcl` erkennt Fremdlink (`12 34 56 78`, DEADBEEF, 13371337, BCL frame) und gibt Node frei | Sq00ky | `wireless_setup.cpp`; `spp_link_policy.hpp` | high | RUNTIME | TRANSPORT (BCL detect only) |
| `EVID-NBTOSS-004` | Source: AAIdrive ohne eigenen BT-Link; fährt auf MyBMW BCL; HU A4AHandler `/dev/btspp0` wartet auf BCL magic | Sq00ky | `spp_link_policy.hpp`; `spp_direction.hpp`; `readme.md` | high (source claim) | RUNTIME | PROTOCOL (secondary) |
| `EVID-NBTOSS-005` | Control UDP `127.0.0.1:52790`; state `/dev/shmem/nbt-aad-state`; logs `nbt-aad.log` / `nbt-aad-app.log` | Sq00ky | `main.cpp`; `updating.md`; aa-tile README | high | RUNTIME | RUNTIME |
| `EVID-NBTOSS-006` | Plugin deploy path `/opt/hmi/ID5/data/ro/Plugins/NbtAad/` + `/opt/aa/nbt-aad` + `nbt-aad.env` + `pf_aa` | Sq00ky | `install.md`; `updating.md` | high | RUNTIME+CONFIG | INFRASTRUCTURE |
| `EVID-NBTOSS-010` | RA plugin: manifest + xml + `libNbtAad.so` / `pluginAppInfo` / create / onInit | Sq00ky | `rhmiapp/NbtAad.manifest`; `nbt_aad_app.cpp` | high | RUNTIME | DOMAIN |
| `EVID-NBTOSS-011` | Plugin APIs: `updateModel`, `setProperty`, `addHandler(raAction)` | Sq00ky + toolkit | `nbt_aad_app.cpp`; toolkit `06-runtime-api-reference.md` | high | RUNTIME | DOMAIN |
| `EVID-NBTOSS-012` | DescFile: `hmiState`s, `raAction` ids, models; blank overlay state pattern | Sq00ky | `NbtAad.xml`; readme | high | RUNTIME | DOMAIN |
| `EVID-NBTOSS-013` | Toolkit: `HmiMain3D` discovers Plugins/, `dlopen`, Etch **connector** in manifest | toolkit@bce20cc | `capabilities/plugins/docs/01-…` | high | RUNTIME/HMI | DOMAIN/INFRA |
| `EVID-NBTOSS-014` | Manifest `<type>Etch</type>` = pluginAppConnector, not phone BCL/Etch session | Sq00ky + toolkit | `NbtAad.manifest`; toolkit 01 § manifest | high | RUNTIME | DOMAIN (naming trap) |
| `EVID-NBTOSS-020` | aa-tile: MOST device `0x2471`, AppState `0xCF1`, press `0xCE8` → UDP `show` to nbt-aad | deathwalker80/nbt-aa-tile@55b5fe7 | `docs/protocol.md` | high | RUNTIME | TRANSPORT/RUNTIME |
| `EVID-NBTOSS-021` | aa-tile follows `/dev/shmem/nbt-aad-state`; needs `CarLife.pbw`; uses `dlopen(libsys_dsi_colibry)` | aa-tile | README; `src/aa_tile.c` | high | RUNTIME | RUNTIME/INFRA |
| `EVID-NBTOSS-022` | idrive-plus: plugins HTTP GET phone `:8765`; ARP/`172.16.224.x` discovery on AA Wi-Fi | idrive-plus@5342dc7 | `ponte_plugin.cpp`; README.en; README-v28 | high | RUNTIME | DOMAIN/TRANSPORT |
| `EVID-NBTOSS-030` | SSH Unlocker: HSFZ 6801/6811, UDS 0x27 L3, OPT_DEBUG LIVE-DIRECT, SSH22/Telnet23/qconn8000 | Xayanix@1791228 | README | high | CONFIG | INFRA |
| `EVID-NBTOSS-031` | Toolkit transport: ENET HSFZ/UDS for F-series incl. NBT Evo host | toolkit | `docs/01-transport-connect.md` | high | CONFIG | INFRA |
| `EVID-NBTOSS-032` | reversing: live-partition write / OPT_DEBUG path; FSC pubkey notes | reversing@afb9a4e | README; `nbt_optdebug_flash.py` | medium | CONFIG | INFRA |
| `EVID-NBTOSS-040` | NBTApps: HU agent + Android app; own SPP registration for package install | tom-pryor/nbtapps@f709ef8 | README; `agent/spp_service.cpp` | medium | RUNTIME | TRANSPORT (own) |
| `EVID-NBTOSS-041` | F20-specific community: multi-tap (#36); no-CarPlay USB AA (#132); SWFL notes | GitHub issues | #36 #132 #272 | community | RUNTIME | low (AA only) |

## INFERENCE

| ID | claim | Ableitung |
|----|-------|-----------|
| `EVID-NBTOSS-050` | Native RA-Plugin-Framework und Connected Remote-RHMI teilen HMI-Abstraktionen (states/actions/models), nicht denselben Wire | 010–014 + bmw-rhmi Sheet |
| `EVID-NBTOSS-051` | HU SPP-Manager bedient mehrere Parteien (AA UUID, BMW Apps, NBTApps, …) | 001–004 + NBTApps SPP + prior Secondary |
| `EVID-NBTOSS-052` | ArtiDrive sollte Plugin-Lifecycle + connection-state getrennt von BCL-Protokoll modellieren | 005, 010–014, 020 |

## UNKNOWN

| Claim | Hinweis |
|-------|---------|
| F20 hat identische `/dev/btspp` Nummerierung / A4AHandler-Bindung wie Supra/MINI Logs | Secondary ≠ F20 wire |
| F20 SWFL enthält `CarLife.pbw` | aa-tile Requirement; F20 untested here |
| Ob native `setProperty` IDs mit Connected Action-IDs korrelieren | keine Mapping-Tabelle in OSS |
| Wayglass interne Mechanismen | closed source |

## REJECTED (als Claim)

| Claim | Warum |
|-------|-------|
| NBT-AAD implementiert BCL/Etch/SAS Connected path | Eigene AA UUID + Wi-Fi; BCL nur Fremd-Detect |
| ENET/SSH/Plugin = SAS-Login-Ersatz | Andere Plane; keine Credentials |
| Manifest-Etch = Phone Etch session | Connector type only |
| HS/KNOCK/ACK10 aus NBT-AAD ableiten | **NO EVIDENCE** (rg leer) |
| idrive-plus HTTP = ConnectedDrive protocol | Explizit AA Wi-Fi + eigenes HTTP |

## NO EVIDENCE (Negativsuche §17)

Gesucht in allen Prioritätsrepos (ohne Tests/third_party):  
`ACK10`, `KNOCK`, `HS` handshake, `sas_login`, `APP_AUTH`, `RHMI over Bluetooth` payloads, Connected Bluetooth client framing.

**Ergebnis:** keine Treffer für Handshake-Tokens. BCL-Magic nur in NBT-AAD Detect/Docs.  
→ Connected Protokollkern bleibt an BimmerGestalt + eigenes F20-Feld gebunden.
