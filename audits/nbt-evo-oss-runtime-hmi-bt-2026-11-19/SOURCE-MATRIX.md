# A — Source Matrix

Pins = shallow HEAD zum Audit-Zeitpunkt 2026-11-19. Evidence quality: `code` > `docs` > `issue-log` > `community` > `closed-source`.

| Source | Pin | Plane | Runtime | HMI | BT | Simulator | Evidence quality | Rolle (nicht vermischen) |
|--------|-----|-------|---------|-----|----|-----------|------------------|--------------------------|
| **Sq00ky/Supra-iDrive6-Android-Auto** (NBT-AAD) | `0941aec` | RUNTIME (+ needs CONFIG to install) | **high** — AA daemon lifecycle, SPP, Wi-Fi handoff, state file, control port | **high** — `libNbtAad.so`, DescFile, `updateModel`/`setProperty`/`raAction` | **high** — AA UUID SPP, `/dev/btsppN`, BCL-foreign detect | **high** SIM-DOMAIN/RUNTIME/TRANSPORT; **low** SIM-PROTOCOL (Connected) | code + docs + issue-logs | Native HU AA application |
| **deathwalker80/nbt-aa-tile** | `55b5fe7` | RUNTIME (HMI↔MOST↔IPC) | medium — boot launch, state follow | **high** — CarLife tile lifecycle | none (no BT protocol) | **medium** SIM-RUNTIME/TRANSPORT (MOST/DSI/IPC) | code + protocol.md | CarLife MOST shim → nbt-aad |
| **deathwalker80/idrive-plus** | `5342dc7` | RUNTIME (Plugin↔Phone HTTP) | medium — plugin↔phone data | **high** — five RA plugins | none for Connected | **medium** SIM-DOMAIN (plugin pages); **not** BCL | code + README | Phone discovery over AA Wi-Fi |
| **vandelayautollc/nbt-evo-toolkit** | `bce20cc` | CONFIG/DEBUG + HMI SDK | low for Connected | **very high** — Plugin discovery/ABI/API | none | **high** SIM-DOMAIN/INFRASTRUCTURE | docs (carve/proof tagged) | HU plugin development |
| **vandelayautollc/nbt-evo-reversing** | `afb9a4e` | CONFIG/DEBUG | none for Connected | low | none | **low** SIM-INFRASTRUCTURE only | docs + flash script | OPT_DEBUG / FSC notes |
| **Xayanix/nbt-evo-ssh-unlocker** | `1791228` | CONFIG/DEBUG only | **none** | none | none | **low** (QNX access model) | README + scripts | HSFZ→OPT_DEBUG→SSH |
| **tom-pryor/nbtapps** | `f709ef8` | RUNTIME (own agent SPP) | medium — agent lifecycle | medium — NbtApp plugin | medium — own SPP register | **low–medium** (parallel SPP pattern) | code + README | App-store agent; **kein** BCL-Zusatz |
| **Wayglass** | n/a (closed) | CONFIG (installer) | Kontrollquelle | Kontrollquelle | unknown | **none** as evidence | closed / marketing | HU modification installer |
| **BimmerGestalt / AAIdrive** (Referenz) | prior audits | RUNTIME Connected | **canonical** for our path | RHMI over Etch | BCL/SPP | **canonical** SIM-PROTOCOL | prior desk+field | Unmodifizierter Connected-Pfad |

## Plane-Trennung (verbindlich)

```
CONFIG / DEBUG PLANE          ≠          RUNTIME PLANE (Connected)
ENET / HSFZ / UDS / SSH / QNX            BT / BCL / Etch / RHMI / SAS
Coding / FSC / OPT_DEBUG / LIVE-DIRECT   Phone ↔ HU apps
```

SSH Unlocker und Toolkit-Flash belegen **nur** die linke Spalte.

## F20-Transfer-Hinweis

| Beobachtung | Quelle | Transfer |
|-------------|--------|----------|
| F20 NBT Evo ID6 Touch multi-tap | NBT-AAD Issue #36 | F20-markiert; Touch-Kalibrierung, nicht BCL |
| F20 ohne CarPlay / USB-AA | Issue #132 | F20-markiert; AA-Transport-Variante |
| MINI F60 `/dev/btspp` cold-start | Issue #18 | **nicht** automatisch F20 |
| G30/Supra/MINI Cluster/HUD | diverse Issues | **nicht** F20-Default |
| CarLife.pbw required (aa-tile) | nbt-aa-tile README; F30 `NBTevo_L17193I` fails | F-Series SWFL-abhängig; F20 `UNKNOWN` bis `ls` |

Softwarestände in Community-Logs u. a.: `NBTevo_ID5_2111`, `NBTevo_Q1849I`, `NBTevo_Y21432J`, `NBTevo_P18362I`, `NBTevo_R19144I` — jeweils an Issue binden, nicht generalisieren.
