# E — ArtiDrive / f20_sim Relevanz

Bezug: `esp32-bt-analyzer` Full F20 HU Simulator (`f20_sim`, Lab UI `:8081`) — siehe Projekt-STATUS.  
**Noch keine Implementierung** — nur Anpassungsvorschläge.

## SIM-DOMAIN

| Vorschlag | Quelle | Nutzen |
|-----------|--------|--------|
| PluginApp-Abstraktion: `manifest → DescFile → pluginAppInfo → onInit → models/actions` | NBT-AAD rhmiapp; toolkit 01/06 | HMI State / ControllerAction / Resources realistischer |
| `hmiState` + `raAction` + `updateModel`/`setProperty` als Domain-Events trennen von Etch-Wire-`setData` | NbtAad.xml; nbt_aad_app.cpp | Vermeidet Naming-Collision mit Connected RHMI |
| Resource bundles: TextDB/ImageDB zip neben DescFile | NbtAad_* zips; toolkit | checkResource-ähnliche Domain ohne SAS zu faken |

## SIM-RUNTIME

| Vorschlag | Quelle | Nutzen |
|-----------|--------|--------|
| Process lifecycle: daemon single-instance, boot autostart, restart recreates SPP | main.cpp; Issue #18 | `HuRuntime` / app state |
| Connection state enum: `idle \| connecting \| connected` (+ overlay) | `/dev/shmem/nbt-aad-state` | phone/app/HMI state machine |
| Parallel consumers on serial links (foreign hold / silence policy) | spp_link_policy | erklärt Lab Contention ohne Protokollwechsel |

## SIM-TRANSPORT

| Vorschlag | Quelle | Nutzen |
|-----------|--------|--------|
| SPP multi-node scan abstraction (`btspp0..N`) | main.cpp | Transport-Owner Tests |
| Optional Wi-Fi handoff transport **als separates Profil** (AA), nicht default Connected | wireless_setup | verhindert false Connected success |
| Optional MOST/DSI stub + localhost UDP control | aa-tile protocol | nur wenn HMI-trigger-Szenarien nötig |
| **Nicht** ARP/HTTP:8765 als Connected transport | idrive-plus | eigenes Profil oder weglassen |

## SIM-PROTOCOL

| Vorschlag | Quelle | Nutzen |
|-----------|--------|--------|
| BCL detect heuristics as **negative test** (simulator emits magic → client must not treat as AA) | looksLikeBmwBcl | Regression |
| Connected stack bleibt BCL→Etch→SAS→RHMI aus BimmerGestalt + Feld | prior audits | **keine** OSS-Substitution |
| SAS: weiterhin echter Blocker — Simulator darf Auth **mocken**, aber nicht als „aus NBT-AAD abgeleitet“ verkaufen | Negativsuche | Epistemik |

## SIM-INFRASTRUCTURE

| Vorschlag | Quelle | Nutzen |
|-----------|--------|--------|
| QNX path map: `/opt/hmi/ID5/…`, `/opt/aa/`, `/dev/shmem/`, `/dev/btspp*` | install/updating; toolkit architecture | filesystem fidelity in sim docs |
| `HmiMain3D` as sole UI process; appreset reload | toolkit hmi-debugging; install OnOffDSICommander | process model |
| Config plane (HSFZ/SSH) nur in Ops-Doku, nicht in protocol sim | Unlocker | klare Trennung |

## Explizit nicht übernehmen

- CarPlay-AP-Zwang als Connected-Requirement  
- MOST CarLife als BCL-Ersatz  
- OPT_DEBUG/SSH als Auth  
- Supra/MINI Cluster/HUD Eth-Adressen als F20-Default  
