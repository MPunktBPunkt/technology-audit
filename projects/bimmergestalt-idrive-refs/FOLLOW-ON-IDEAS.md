# Follow-on Ideas: bimmergestalt-idrive-refs

Keine automatische Engineering-Action. Nur nach eigener Evidence → Decision.

| # | Idee | Voraussetzung | Bezug |
|---|------|---------------|-------|
| 1 | Eigenes BCL-Frame-Capture (BT RFCOMM oder USB/ENET) gegen NBT Evo | Autorisierung; Lab-Setup; kein Security-Bypass | `bmw-bcl`, hu-probe Gap |
| 2 | Etch-Session-Trace (nur legitimierte Connected-App / Simulator) | SAS-fähige Umgebung oder Simulator Port 4006 | `bmw-etch-rpc` |
| 3 | RHMI-Capability-Probe (`hmi.type` / `hmi.version`) auf Ziel-HU | Etch-Login möglich | `bmw-rhmi` vs ID4/5/6 |
| 4 | AV `av_requestConnection` vs USB-MSC Audio-Pfad vergleichen | Parallel nur Beobachtung; kein Architektur-Umbau | PiDrive Cross-Ref |
| 5 | USB/ENET-BCL verifizieren (Doc behauptet, BclCarLink nur BT) | Capture-Pfad | Contradiction Doc↔Code; Desk AOA: [`usb-aoa-bmw-connected-2026-desk`](../../audits/usb-aoa-bmw-connected-2026-desk/) |
| 6 | CDS Content-Provider Muster (AAIdrive) nur als Knowledge, nicht als Dependency | Privacy/Permission-Gates | Addons |
| 7 | C1b B1: Phone-like Enum + 51/52/53 / Descriptor-Wechsel | Autorisierung; Observation-Log (auch Standard/Class) | `usb-aoa`, [`C1b-PLAN`](../../audits/usb-aoa-bmw-connected-2026-desk/C1b-PLAN.md) |
| 8 | C1b B2: BCL-8-Byte-Header auf Bulk nach Switch | B1 positiv oder nachgewiesenes Rohr | `bmw-bcl` Wire; kein Auto-Framer vor Muster |
| 9 | Referenz-Capture Phone + Official/MyBMW Connected USB | Sniff/tcpdump localhost Proxy | Kontrast zu `aoa_observe`-Negativ (Enum ohne Bulk) |
| 10 | Kill-Kriterium C1b neu: „kein Bulk/Connected nach Accessory-Enum“ | Feld Already-Accessory (`EVID-AOA-030`) | ersetzt reines „kein Switch zu 0x18D1“ |
| 11 | BT-SPP als paralleler ITransport-Kandidat wenn USB-B1 dauerhaft negativ | BclCarLink RFCOMM-Pfad | `bluetooth-spp` / `bmw-bcl` |
| 12 | hu-probe Knock: **hex4** `12 34 56 78` (nicht ASCII-8) + optional voller Knock (len=12) | C1b Bulk-Rohr; Desk [`bmw-bcl-handshake`](applications/bmw-bcl-handshake.md) §5 | korrigiert Pattern-Mismatch |
| 13 | Referenz-PCAP erste BCL-Pakete (BT und/oder USB) für Handshake-Hex | Autorisierung; Wireshark `bmw_bcl.lua` | schließt G-HS-1/G-USB-2 |

Kampagne Knowledge Acquisition geschlossen; C1b = eigene Messkampagne (Plan only hier).
Lab-/Field-Messungen = eigene Audits / hu-probe Gates.
Handshake-Desk 2026-10-29: [`applications/bmw-bcl-handshake.md`](applications/bmw-bcl-handshake.md).

