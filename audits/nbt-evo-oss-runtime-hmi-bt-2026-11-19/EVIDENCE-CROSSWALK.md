# D — Existing Evidence Crosswalk

Format: NEW SOURCE → EXISTING FACT → SUPPORT / REFINE / CONTRADICT / UNRELATED.

| NEW SOURCE | EXISTING FACT | Relation | Notes |
|------------|---------------|----------|-------|
| `EVID-NBTOSS-003/004` BCL detect + AAIdrive-on-MyBMW tunnel | Secondary `EVID-SUPRA-2026-11-13-*`; Sheet `bmw-bcl` Transport Owner | **SUPPORT** + **REFINE** | Bestätigt Contention; Direction Phone-open-AA vs Car-open-BMW bleibt Spannung/`UNKNOWN` bis F20-Capture der Open-Richtung |
| `EVID-NBTOSS-001` AA UUID SPP | Feld: HU SPP SCN 6–10 + iAP ch5 (`bmw-nbt-evo` Sheet) | **UNRELATED** as protocol; **SUPPORT** as „HU has SPP manager“ | Andere UUID; nicht BCL-Endpoint |
| `EVID-NBTOSS-002` BT→Wi-Fi handoff | Feld Connected bleibt BT/BCL | **UNRELATED** / **REJECT** transfer | Nicht als Connected-Pfad übernehmen |
| Negativsuche HS/KNOCK/ACK10 | Feld MEASURED HS/KNOCK/ACK10 | **UNRELATED** (OSS silent) | Kein Widerspruch — OSS implementiert Pfad nicht |
| `EVID-NBTOSS-010…014` native Plugin RHMI ABI | Sheet `bmw-rhmi` lifecycle over Etch | **REFINE** (architecture) | Geteilte HMI-Begriffe; Wire bleibt Etch-over-BCL für Connected |
| Toolkit Plugin load / HmiMain3D | `bmw-nbt-evo` Plattform | **SUPPORT** INFRASTRUCTURE | Erklärt Host-Prozesse; kein USB-MSC Claim |
| `EVID-NBTOSS-020` MOST CarLife | unser BCL-Pfad | **UNRELATED** | Anderer Subsystem-Transport |
| `EVID-NBTOSS-022` HTTP:8765 | Connected/SAS | **UNRELATED** | Nicht als Auth-Bypass lesen |
| `EVID-NBTOSS-030` SSH Unlocker | SAS Auth audits | **UNRELATED** / **REJECT** substitute | Config-Plane ≠ Credentials |
| NBTApps SPP agent | BCL RFCOMM role desk | **UNRELATED** for BCL framing; mild **SUPPORT** multi-tenant SPP | „keine zusätzliche Evidenz“ für Connected Protokoll |
| Wayglass A4A_REMOTE_APPS / VIN / SWFL | Identifikation / Install | **UNRELATED** as protocol evidence | Closed; Kontrollquelle only |
| Issue #36 F20 multi-tap | F20 Touch / RHMI actions | **UNRELATED** to BCL; optional AA touch refine | F20-markiert |

## supports_existing_fact / contradicts / new_information (Kurz)

| ID | supports | contradicts | new_information | transferability_to_f20 | relevance_* |
|----|----------|-------------|-----------------|------------------------|-------------|
| 001–005 | HU SPP multi-user; state/control IPC | „NBT-AAD = BCL client“ | Control port + state file semantics | partial (NBT Evo family; node# UNKNOWN) | iDrive high; ArtiDrive RUNTIME; PiDrive low |
| 010–014 | RHMI as framework concept | setData-wire Gleichsetzung | Concrete PluginApp vtable usage in wild | high for ID5/ID6 plugin model if SWFL matches | ArtiDrive DOMAIN high |
| 020–022 | HMI↔external process patterns | MOST=BCL | CarLife FBlock + ARP phone discovery | conditional (CarLife.pbw / AA Wi-Fi) | ArtiDrive TRANSPORT optional |
| 030–032 | ENET/HSFZ platform | SSH helps SAS | LIVE-DIRECT / OPT_DEBUG map | F-series HSFZ yes; unlock risk separate | PiDrive/iDrive low; Infra only |
| 040 | — | — | **keine zusätzliche BCL-Evidenz** | n/a | document as such |

## SAS-Blocker

Keine Quelle liefert Credentials, Digest-Whitelist-Inhalt oder `sas_login`-Implementierung jenseits bekannter BimmerGestalt-Desk-FACTS.  
**REJECT:** ENET/SSH/Coding/FSC/Plugin-Install als Ersatzpfad.
