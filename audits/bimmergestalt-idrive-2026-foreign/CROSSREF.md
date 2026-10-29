# Cross Reference — hu-probe & PiDrive

Regel: **BimmerGestalt überschreibt keine hu-probe-/PiDrive-FACTS.**  
USB-MSC-Host-C bleibt SoT für NBT-Evo-Read-Verhalten.

## hu-probe

hu-probe misst **ESP32-S3 als USB-MSC-Gadget** gegen BMW NBT Evo (Transport S0/S2, Media-Leiter, Heimfahrt Remount/Scheduler, …).  
BimmerGestalt beschreibt **Connected-App Protokoll** (BT/BCL/Etch/RHMI).

| Kategorie | Thema | Kommentar |
|-----------|-------|-----------|
| **Confirmed** | Zielplattform-Label „NBT Evo“ | Beide nennen NBT Evo; hu-probe hat Field-MEASURED MSC; BG hat Doc/FAQ-Kompatibilität — Label bestätigt, **nicht** MSC-Verhalten |
| **Confirmed** | Generation-Vorsicht | BG: hmi.type/version; KB: kein stiller Transfer anderer HU — epistemisch aligned |
| **Complementary** | Protokollschicht | BCL/Etch/RHMI/AV/CDS fehlen in hu-probe (bewusst anderer Scope) |
| **Complementary** | Capability-Strings ID4/5/6 | Könnten spätere Host-Varianten-Gates informieren; **nicht** MSC-Timing |
| **Contradiction** | — | Keine direkte Aussage kollidiert mit MSC Prefetch/Remount/Head-Read FACTS |
| **Gap** | BCL/Etch am Fahrzeug | Lab-`BclFramer` PASS; **Wire-Bulk** noch absent (`EVID-AOA-030`) |
| **Gap** | AOA Handshake 51/52/53 | Zähler 0 bei Already-Accessory-Boot; Phone-like Enum offen (C1b B1) |
| **Gap** | Control-Vollsicht | Vendor-Tap sieht Standard/Class nicht vollständig (`EVID-AOA-031`) |
| **Gap** | AV multimedia buttons vs MSC | unverbunden |
| **Complementary** | C1b-P0 Enum/UI | NBT erkennt `aoa_observe` als Zubehör — kein Connected-Rohr |
| **No relation** | CDS ContentProvider, HassGestalt HA, RSS/Weather forks | |

**Fazit hu-probe:** BG = Wissensschicht *neben* MSC-Sonde. C1b-P0 liefert Enum-MEASURED, nicht BCL.
Kein Claim-Merge. Nächste Messung: [`C1b-PLAN`](../usb-aoa-bmw-connected-2026-desk/C1b-PLAN.md).

## PiDrive

PiDrive: Infotainment mit **USB-MSC** (+ separat BT A2DP/AVRCP) an NBT Evo.

| Kategorie | Thema | Kommentar |
|-----------|-------|-----------|
| **Direkt relevant** | Existenz Connected-App Stack | Belegt alternativen HU-Integrationskanal (RHMI/AV) |
| **Direkt relevant** | SAS-Auth-Gate | Connected-App-Pfad ≠ „einfach TCP“; MSC bleibt auth-frei auf USB-Ebene |
| **Möglicherweise relevant** | `av_*` Entertainment connection | Hypothese: Metadaten/Steuerung ohne MSC; **kein** Ersatz für MP3-via-MSC ohne eigene Evidence |
| **Möglicherweise relevant** | RHMI als UI-Oberfläche | Alternative UX-Architektur — nur Hypothese |
| **Nur Kontext** | Simulator :4006 | Lab ohne Fahrzeug für App-Clients; hilft PiDrive-Firmware nicht direkt |
| **Nur Kontext** | CDS Provider | Datenpfad Phone-Apps |
| **Neue Untersuchung** | USB/ENET BCL vs BT | Doc↔Code Widerspruch — Capture nötig |
| **Neue Untersuchung** | Korrelation instanceId / A2DP pairing mit HU-Zustand | BclCarLink knüpft an A2DP-Gerät |
| **Bestätigt** | NBT Evo als relevante HU | Marketing/FAQ aligned mit unserem Host-Scope |
| **Geschwächt** | „Einzige praktikable Medienintegration = MSC“ als Absolutclaim | Als *alleinige* Wahrheit geschwächt → **HYPOTHESIS**-Status für Absolutheit; MSC-Erfolg bleibt MEASURED |
| **Nicht widerlegt** | MSC Prefetch/Busy/Geometry FACTS | unberührt |
| **REJECTED** | BG-Code als PiDrive-Implementierungsvorlage ohne Lizenz/Auth-Prüfung | Stop-Gate |

**Architektur-Hinweis (kein Engineering-Auftrag):**  
Connected-App-Weg = höhere iDrive-Protokollebene; USB-MSC = Storage-Host-Verhalten. Ergänzung möglich (Steuerung/Metadaten), Ersatz unbewiesen.

## Knowledge vs Evidence vs Reuse (PiDrive-Beispiel)

| Aussage | evidence_max | knowledge_value | reuse |
|---------|--------------|-----------------|-------|
| BCL framing 8 B | R0 (fremd desk) | HIGH | HIGH (capture catalog) |
| AV Entertainment API exists | R0 | HIGH | MEDIUM (hypothesis) |
| Replace MSC with RHMI audio | R0 | MEDIUM | LOW — REJECTED as plan without evidence |
| NBT Evo MSC prefetch patterns | R3 (our field) | HIGH | HIGH — **unchanged** |
