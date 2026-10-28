# Follow-on Ideas: bimmergestalt-idrive-refs

Keine automatische Engineering-Action. Nur nach eigener Evidence → Decision.

| # | Idee | Voraussetzung | Bezug |
|---|------|---------------|-------|
| 1 | Eigenes BCL-Frame-Capture (BT RFCOMM oder USB/ENET) gegen NBT Evo | Autorisierung; Lab-Setup; kein Security-Bypass | `bmw-bcl`, hu-probe Gap |
| 2 | Etch-Session-Trace (nur legitimierte Connected-App / Simulator) | SAS-fähige Umgebung oder Simulator Port 4006 | `bmw-etch-rpc` |
| 3 | RHMI-Capability-Probe (`hmi.type` / `hmi.version`) auf Ziel-HU | Etch-Login möglich | `bmw-rhmi` vs ID4/5/6 |
| 4 | AV `av_requestConnection` vs USB-MSC Audio-Pfad vergleichen | Parallel nur Beobachtung; kein Architektur-Umbau | PiDrive Cross-Ref |
| 5 | USB/ENET-BCL verifizieren (Doc behauptet, BclCarLink nur BT) | Capture-Pfad | Contradiction Doc↔Code |
| 6 | CDS Content-Provider Muster (AAIdrive) nur als Knowledge, nicht als Dependency | Privacy/Permission-Gates | Addons |

Kampagne geschlossen als Knowledge Acquisition. Lab-/Field-Messungen = eigene Audits.
