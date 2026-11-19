# C — HU Architecture Update

Nur **belegte** Übergänge. Keine spekulativen Brücken Config→SAS oder AA→BCL.

```
                         NBT EVO
                            │
              ┌─────────────┴─────────────┐
              │                           │
       CONFIG / DEBUG                  RUNTIME
              │                           │
     ENET (OBD RJ45)              Bluetooth Classic
     HSFZ UDP:6811 / TCP:6801     ┌───────┴────────┐
     UDS (incl. 0x27 L3)          │                │
     OPT_DEBUG starter.cfg   Connected/MyBMW    Native AA (NBT-AAD)
     LIVE-DIRECT write       BCL on btspp*      AA UUID SPP → Wi-Fi/TCP
     SSH:22 Telnet:23        Etch / SAS         aasdk session
     qconn:8000              RHMI remote apps   mm-renderer video
     Coding / FSC            AAIdrive consumer  │
              │                   │             │
              │                   └──────┬──────┘
              │                          │
              │                    HmiMain3D
              │                    RA Plugins (manifest/xml/so)
              │                    Bundle plugins (hmiremoting, A4A, …)
              │                          │
              └──────────┬───────────────┘
                         │
                    QNX OMAP runtime
                    /opt/hmi /opt/aa /dev/btspp* /dev/shmem
```

## Belegte Runtime-Nebenpfade (nicht Connected)

| Pfad | Beleg | Nutzung für uns |
|------|-------|-----------------|
| HMI ↔ MOST/DSI ↔ CarLife FBlock `0x2471` ↔ UDP `52790` | nbt-aa-tile `docs/protocol.md` | Sim: HMI trigger / process show — **nicht** BCL |
| Plugin ↔ ARP/HTTP `:8765` Phone (über AA Wi-Fi) | idrive-plus | Sim: phone discovery pattern — **nicht** ConnectedDrive |
| Agent ↔ eigenes SPP ↔ Phone packages | NBTApps | Parallel-SPP Muster; **keine** BCL-Zusatzevidenz |

## Explizit **nicht** eingezeichnet

- ENET/SSH → SAS login  
- NBT-AAD Wi-Fi → BCL tunnel  
- MOST CarLife → Etch  
- Coding/FSC → App credentials  

## Toolkit: Plugin-Loading (Runtime HMI, braucht oft CONFIG zum Deploy)

```
HmiMain3D
  scan Plugins/ | PluginsCoded/
  parse <Name>.manifest
  dlopen lib<Name>.so → pluginAppInfo
  create → onInit
  DescFile hmiStates / raActions / models
  updateModel | setProperty | addHandler
```

Quellen: `nbt-evo-toolkit/capabilities/plugins/docs/01-architecture-and-loading.md`, `06-runtime-api-reference.md`; NBT-AAD `rhmiapp/`.

## SSH Unlocker (Config only)

```
ENET → HSFZ discover :6811 → TCP :6801
  → UDS SecurityAccess 0x27 Level 3
  → LIVE-DIRECT write starter.cfg OPT_DEBUG
  → reboot → sshd:22 / telnetd:23 / qconn:8000
```

Quelle: `Xayanix/nbt-evo-ssh-unlocker@1791228` README.  
**≠** Connected Runtime.
