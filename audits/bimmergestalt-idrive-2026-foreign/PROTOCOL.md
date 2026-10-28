# Protocol Knowledge — BimmerGestalt Desk

Herkunft: Fremdcode/Docs @ Pins 2026-10-28. Keine eigenen Captures.
Klassifikation pro Aussage; W ≠ Evidenz.

## Stack

```
Discovery / Announce (Android Intent ATTACHED)
        ↓
Transport: BT RFCOMM (code); USB / ENET (doc only — contradiction)
        ↓
BCL multiplex (8-byte header, virtual channels)
        ↓
Etch TCP stream on dest 0x0FA4
        ↓
SAS authentication
        ↓
Session APIs: RHMI | AV | CDS | AM | map
```

---

## BCL

**Was:** Multiplex-Tunnel Phone↔HU (`protocol-bcl.md`, `BclPacket`).

**Framing (FACT):** command, src, dest, dataLen (u16 BE each) + data.  
**Commands (FACT):** OPEN 1, DATA 2, CLOSE 3, HANDSHAKE 4, SELECTPROTO 5, DATAACK 6, ACK 7, KNOCK 8, LAUNCH 9, HANGUP 10, BROADCAST 11, REGISTER 12.  
**Dest (FACT):** 0x0FA4 Etch; 0x1389 Watchdog.  
**Handshake (FACT):** 8-byte payload version/instanceId/bufferSize; client may send init `12345678` hex; version>3 → SelectProto(3)+Knock.  
**Knock (FACT):** length-prefixed serial/bt/mac/wifi + appType/param1; AppTypes in lua: A4A, TouchCommand, Carplay, AndroidAuto.  
**MUX (FACT):** OPEN binds (src,dest) → stream; DATA/CLOSE.  
**RE-Art:** Static inference (code) + Analysis claims packet observation historically; Dissector = capture-derived names. This audit: **no new Direct observation**.

---

## Etch / RPC

**Was:** Apache Etch service `BMWRemoting` (`BMWRemoting.etch`).  
**Wire (FACT/Doc):** Symbol hashes on wire; `.ewh` aids Wireshark.  
**Client (FACT):** `IDriveConnection.getEtchConnection` → TCP URI with large maxPktSize.  
**Subsystems (FACT):** sas_*, cds_*, am_*, rhmi_*, av_*, map_*.  
**Ports (FACT, multiple):** HU dest 4004; BclCarLink proxy 4007; app fallback 8003; simulator listen 4006; CarProber 4004–4008.

---

## RHMI

**UI (FACT):** XML `pluginApps` → models, actions, events, components, states.  
**Lifecycle (FACT):** sas → rhmi_create → setResource(DESCRIPTION/TEXTDB/IMAGEDB) → initialize → handlers → setData/setProperty/triggerEvent; car → onHmiEvent/onActionEvent + ack.  
**Caps (FACT):** `hmi.type` / `hmi.version` / display size → ID4/ID5/ID6 layout paths.  
**Enums (FACT):** `RHMI_VERSION_ID5`, `_ID6_LIGHT`, `_ID6`.  
**RE-Art:** Implementation + Analysis docs; Simulator renders client apps.

---

## Connection / Security / Transport

| Step | Beleg | Class |
|------|-------|-------|
| A2DP-paired BMW/MINI + SPP UUID RFCOMM | BclCarLink BtConnection | FACT (impl) |
| Connected ATTACHED broadcast | KitAndroid | FACT |
| Cert P7B + merge APP_AUTH | Analysis + SecurityAccess | FACT (existence) |
| Challenge/response SAS | IDL + apps + Analysis | FACT (API) |
| USB/ENET path | Analysis README | Doc FACT; **impl absent** in BclCarLink → Contradiction |

Keine Bypass-/Exploit-Schritte in diesem Audit.

---

## Media / Audio

| Mechanismus | Schicht | Class |
|-------------|---------|-------|
| RHMI Music views (browse/playback) | RHMI widgets | FACT |
| `av_create` / `av_requestConnection` / playerState / multimediaButtonEvent | Etch AV | FACT |
| Android MediaController | Phone-local | FACT |
| CDS ENTERTAINMENT_MULTIMEDIA (scrobbler) | CDS metadata | FACT |
| Audio-focus Intents in Analysis `rhmi-audio.md` | Doc | INFERENCE until re-verified in AAIdrive |

**INFERENCE:** HU-Audio-Fokus ≠ USB-MSC Decode-Pfad (PiDrive).

---

## Input / Controller

RHMI HMI events (focus, visible, …) + `av_multimediaButtonEvent` for media keys.  
Hardware iDrive controller mapping: **UNKNOWN** beyond event IDs in Kit.

---

## Generations matrix (only belegte Zellen)

| Feature | NBT | NBT Evo | ID4 | ID5 | ID6 | Evidence |
|---------|-----|---------|-----|-----|-----|----------|
| Marketing support AAIdrive | Doc | Doc | — | — | — | README/FAQ |
| Speedlock / incompatibility notes | — | — | Doc (iDrive4/7 FAQ) | — | — | FAQ |
| `hmi.type` layout branch | — | — | Code | Code | Code | RHMIDimensions |
| RHMIVersion enum | — | — | — | IDL | IDL | BMWRemoting.etch |
| USB-MSC host C (our KB) | — | **our** R3 | UNKNOWN | UNKNOWN | UNKNOWN | bmw-nbt-evo / hu-probe — **not from BG** |

Leere Zellen = nicht belegt (nicht „nein“).

---

## Knowledge Graph (relational)

```
BclCarLink ──implements──► BCL ──carries──► Etch@4004
wireshark_bmw_bcl ──names──► BCL commands/dests
BMWConnectedAnalysis ──documents──► BCL/Etch/Auth/RHMI
IDriveConnectKit ──defines──► BMWRemoting.etch + RHMI models
IDriveConnectKitAndroid ──announces──► ATTACHED
AAIdrive ──uses──► SAS+RHMI+AV (+CDS provider)
Simulator* ──fakes──► HU Etch:4006
Addons/HassGestalt/Experiments ──reuse──► RHMI/CDS patterns
```

Unabhängigkeit: Dissector + BclCarLink + Analysis beschreiben dieselbe Framing-Struktur → **stärkere** Desk-Konvergenz; README-Kopien allein zählen nicht.
