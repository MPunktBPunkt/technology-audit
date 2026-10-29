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
| 7 | C1b B1: Phone-like Enum + 51/52/53 / Descriptor-Wechsel | **Feld 2026-10-29:** `04E8:6860` → HU „USB nicht unterstützt“ (Fingerprint NEGATIVE, kein AOA-Kill) | `usb-aoa`, [`C1b-PLAN`](../../audits/usb-aoa-bmw-connected-2026-desk/C1b-PLAN.md) |
| 8 | C1b B2: BCL-8-Byte-Header auf Bulk nach Switch | Rohr ja; **kein** HU-RX nach hex4 — Blind-B2 beendet bis #9 | `bmw-bcl` Wire; kein Auto-Framer vor Muster |
| 9 | **PRIORITÄT:** Referenz-Capture Phone + Official/MyBMW Connected USB | Sniff/Analyzer; Checkliste hu-probe `docs/feld/2026-10-29-c1b-massnahmen-nach-b1-b2b.md` | Enum ohne Bulk + B1/B2b Negativ |
| 10 | Kill-Kriterium C1b neu: „kein Bulk/Connected nach Accessory-Enum“ | Feld Already-Accessory (`EVID-AOA-030`) | ersetzt reines „kein Switch zu 0x18D1“ |
| 11 | BT-SPP als paralleler ITransport-Kandidat | **erst nach #9**, wenn Capture USB-BCL absent | `bluetooth-spp` / `bmw-bcl` |
| 12 | ~~hu-probe Knock hex4~~ | **done Feld 0.3.32** — TX ok, HU rx=0; kein weiteres Blind-Knock | Desk [`bmw-bcl-handshake`](applications/bmw-bcl-handshake.md) §5 |
| 13 | Referenz-PCAP erste BCL-Pakete (BT und/oder USB) für Handshake-Hex | Autorisierung; Wireshark `bmw_bcl.lua` | schließt G-HS-1/G-USB-2 |

Kampagne Knowledge Acquisition geschlossen; C1b = eigene Messkampagne (Plan only hier).
Lab-/Field-Messungen = eigene Audits / hu-probe Gates.
Handshake-Desk 2026-10-29: [`applications/bmw-bcl-handshake.md`](applications/bmw-bcl-handshake.md).

