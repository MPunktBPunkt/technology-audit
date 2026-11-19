# F — Research Decision

## Urteil (eine Zeile)

Öffentliche NBT-Evo-OSS **ordnet die Plattform** (HMI-Plugins, SPP-Multi-Tenant, Config-Plane) ein und **bestätigt** BCL als Fremdverkehr auf HU-SPP — sie **erklärt nicht** unseren Connected-Protokollkern und **löst SAS nicht**.

## DO NEXT (≤5)

1. **ArtiDrive Domain:** PluginApp-Lifecycle + `hmiState`/`raAction`/`updateModel` als eigene Schicht modellieren (getrennt von Etch-Wire `setData`) — Spec only.  
2. **Sim Runtime:** `idle|connecting|connected` + overlay + foreign-SPP hold als States aus NBT-AAD übernehmen (ohne AA-Protokollpflicht).  
3. **Feld/Lab:** Open-Richtung SPP (Phone vs Car) am F20 mit Capture klären — bleibt Spannung Secondary vs BclCarLink.  
4. **Negativ festhalten in Sheets:** Verweis dieses Audits unter `bmw-bcl` / `bmw-rhmi` als „native RA ≠ remote RHMI; AA UUID ≠ BCL“.  
5. ~~**CarLife.pbw…**~~ / **SDP-Crosswalk:** erledigt → [`../f20-sdp-vs-nbt-aad-2026-11-19/`](../f20-sdp-vs-nbt-aad-2026-11-19/) — Stock-F20 hat keine AA-UUID; NBT-AAD-BT für Connected **NO-GO**.

## DEFER (≤5)

1. NBTApps Deep Dive / Protocol reverse — **keine zusätzliche BCL-Evidenz**.  
2. Wayglass Internals — closed; Kontrollquelle genügt.  
3. MOST/DSI vollständige FBlock-Map (aa-tile beantwortet nur 0xCF1).  
4. Toolkit Coding/FSC Minting — Config-Plane, irrelevant für SAS-Feldblocker.  
5. Supra/MINI Cluster/HUD Ethernet profiles — nicht F20-Connected.

## REJECT

| Item | Grund |
|------|-------|
| ENET/SSH/OPT_DEBUG als SAS-Ersatz | Config ≠ Auth |
| NBT-AAD Wi-Fi/AA als Connected-Beleg | Anderer Stack |
| HS/KNOCK/ACK10 aus OSS „ableiten“ | NO EVIDENCE |
| Manifest-Etch = Phone-Etch | Naming trap |
| idrive-plus HTTP = ConnectedDrive | Anderes Modell |
| Credential-/Digest-Rekonstruktion aus Plugins | Leitplanke + kein Material |
| „probably same protocol“ | explizit verboten |
| Weitere NBT-AAD Desk-Blöcke nur für BCL-Wire | Prior Secondary + dieses Audit ausreichend |
| NBT-AAD Bluetooth/WifiStart als Connected-Einstieg | SDP-Crosswalk: AA-UUID fehlt auf Stock-F20 ([`f20-sdp-vs-nbt-aad`](../f20-sdp-vs-nbt-aad-2026-11-19/)) |

## Rollenkarte (kurz)

| System | Rolle |
|--------|-------|
| AAIdrive / Feld F20 | Connected Runtime Wahrheit |
| NBT-AAD | Native AA Runtime + HMI plugin reference |
| nbt-aa-tile / idrive-plus | HMI↔process / Plugin↔phone patterns |
| Toolkit | Plugin ABI / HmiMain3D |
| SSH Unlocker / reversing | Config/Debug only |
| NBTApps | eigene Agent-SPP; kein BCL-Zusatz |
| Wayglass | Installer control only |
