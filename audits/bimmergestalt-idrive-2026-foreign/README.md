# Audit Campaign: bimmergestalt-idrive-2026-foreign

```yaml
id: bimmergestalt-idrive-2026-foreign
project_id: bimmergestalt-idrive-refs
started: 2026-10-28
ended: 2026-10-28
status: closed
profile: lab-tool
standard_version: "0.7.1"
standard_gaps: []
reviewed_commit: "org-BimmerGestalt-2026-10-28"
upstream_pins:
  BclCarLink: "7cfd959"
  wireshark_bmw_bcl: "07b7982"
  BMWConnectedAnalysis: "9e96ac6"
  IDriveConnectKit: "95492b0"
  IDriveConnectKitAndroid: "4a567bc"
  AAIdrive: "3e93419"
  Simulator: "6a38086"
  Simulator-kt: "6984020"
  IDriveConnectAddons: "270032d"
  HassGestalt: "63da6a4"
  IDriveExperiments: "4b6d5fa"
  ReadYou: "readme-meta"
  breezy-weather: "readme-meta"
  BimmerGestalt.github.io: "readme-meta"
reuse_outcomes:
  reused:
    - bmw-nbt-evo
  new:
    - bmw-bcl
    - bmw-etch-rpc
    - bmw-rhmi
  not_helped:
    - "USB-MSC host timing from Connected-App repos"
    - "Overwrite hu-probe FACTS"
    - "USB/ENET BCL implementation (doc-only)"
  process: "Desk External Knowledge; Evidence≠W; BG≠own MEASURED; no engineering actions."
  decisions_touched:
    - fact-connected-app-stack-bcl-etch-rhmi
    - reject-merge-into-msc-host-c
    - fact-multi-port-etch-paths
    - contradiction-usb-enet-vs-bt-only
```

## Ziel

Vollständiger evidenzbasierter External-Knowledge-Audit aller **14** öffentlichen
Repos der Org **BimmerGestalt**: belastbares Wissen über iDrive / NBT /
Connected-App-Protokolle (BCL, Etch, RHMI, Media, Security/Transport) für
`technology-audit`, Querverweise zu `hu-probe` und `pidrive`.

Leitfrage: *Was wissen wir jetzt über die Connected-App-/iDrive-Protokollwelt —
mit Quelle und Klassifikation — das vorher im KB fehlte?*

## Scope

[SCOPE](../../projects/bimmergestalt-idrive-refs/SCOPE.md) — desk only.  
Keine Fahrzeugversuche, keine Firmware-Änderungen, keine Attack-How-tos.

Detail: [PROTOCOL.md](PROTOCOL.md) · [evidence.md](evidence.md) · [CROSSREF.md](CROSSREF.md)

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Alle 14 Repos zumindest gesichtet + inventarisiert | erfüllt |
| 2 | P0 BCL/Etch/RHMI/Media/Security extrahiert | erfüllt |
| 3 | Evidence Records + Matrix | erfüllt |
| 4 | Sheets `bmw-bcl`, `bmw-etch-rpc`, `bmw-rhmi` | erfüllt |
| 5 | hu-probe + PiDrive Cross-Ref ohne FACT-Overwrite | erfüllt |
| 6 | Widersprüche Doc↔Code markiert | erfüllt |
| 7 | C10–C13 + Lessons; Antworten A–H | erfüllt |
| 8 | `ta-assist check` 0 errors | erfüllt |
| 9 | Eigene Lab-/Field-Captures | FOLLOW-ON — nicht Exit dieser Kampagne |

---

## Executive Summary

**Wichtigste Erkenntnis:** BimmerGestalt dokumentiert und implementiert eine
**zweite HU-Integrationsschicht** neben unserem USB-MSC-Wissen:
`Transport → BCL → Etch(BMWRemoting) → SAS → RHMI|AV|CDS|AM`.

| Thema | Kurz |
|-------|------|
| iDrive-Protokoll | BCL-MUX + Etch-RPC; dest 4004 = Etch |
| Connected App | ATTACHED Intent → lokaler Etch-Proxy → SAS → RHMI-Apps |
| BCL | 8-Byte BE-Header; Handshake/SelectProto/Knock; Watchdog 5001 |
| Etch | IDL mit sas/cds/am/rhmi/av/map |
| RHMI | XML-UI + create/resource/initialize; Caps ID4/5/6 |
| Media | RHMI Music UI + `av_*` Entertainment; CDS Multimedia-Metadaten |
| Security/Transport | SAS cert/challenge/login; BT RFCOMM in Code; USB/ENET nur Doc |
| hu-probe | Complementary/Gap — MSC unberührt |
| PiDrive | Alternativkanal belegt als Knowledge; MSC-FACTS unberührt; Absolutclaim „nur MSC“ als Alleinstellung geschwächt |

**Evidence vs Knowledge vs Reuse:** Framing/IDL = knowledge HIGH, evidence_max R0
(fremd desk), reuse HIGH als Capture-Katalog. Eigene R3-MSC-FACTS bleiben führend
für Host-C.

---

## Repository Inventory (Kurz)

Siehe [INVENTORY](../../projects/bimmergestalt-idrive-refs/INVENTORY.md).

| Prio | Repos |
|------|-------|
| P0 | BclCarLink, wireshark_bmw_bcl, BMWConnectedAnalysis, IDriveConnectKit(+Android), AAIdrive |
| P1 | Simulator(+kt), IDriveConnectAddons, HassGestalt, github.io (Hub) |
| P2 / irrelevant* | IDriveExperiments (richtext only); ReadYou; breezy-weather |

\*irrelevant = kein Protokollkern über Addon-Muster hinaus; Begründung im Inventar.

---

## Decision Trace (C10)

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| Neue Sheets? | Fehlt Connected-App-Schicht im KB? | Stack FACTS 001–015 | Neu: bmw-bcl, bmw-etch-rpc, bmw-rhmi | DISCOVERED |
| bmw-nbt-evo erweitern um BCL? | Gleiche Technology? | Layer-Trennung | Nein — reuse nur Abgrenzung | KNOWN BEFORE |
| hu-probe FACTS anpassen? | Widerspruch MSC? | CROSSREF | Nein — Gap/Complementary | DISCOVERED |
| USB/ENET als FACT? | Code-Pfad? | 020 | Contradiction; nicht als impl. FACT | DISCOVERED |
| Engineering an PiDrive? | Evidence genug? | reuse LOW für Ersatz | Nur FOLLOW-ON Vorschläge | KNOWN BEFORE |
| ReadYou/breezy deep clone? | Protokollwert? | 023 | Skip deep — irrelevant* | DISCOVERED |

## Engineering Review Checks (C11)

| Evidence | Check |
|----------|-------|
| 001–007 | BCL-Felder nur mit Pin zitieren; kein OEM-Spec-Claim |
| 010 | SAS nur API-Existenz; keine Bypass-Schritte in KB |
| 014 | Generation nur über hmi.* / Doc-Labels getrennt |
| 015 | AV ≠ MSC-Audio; Architektur-Hypothese markieren |
| 020 | Doc↔Code Widerspruch nicht glätten |
| CROSSREF | hu-probe R3 Claims unverändert |

## Kill-Kriterien (C12)

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | BG-Claims als eigene Field-FACTS übernommen | `REJECTED` |
| 2 | MSC-Host-C durch RHMI ersetzt ohne Messung | `REJECTED` |
| 3 | Attack-How-to für SAS | `REJECTED` |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk Knowledge Acquisition ohne Messhypothese zum Verwerfen.
Widerspruch USB/ENET und fehlende eigene Captures sind Gaps, keine Kill-Kriterien.
```

## Knowledge Feedback (C13)

Desk only — kein neuer MEASURED-Claim in hu-probe/PiDrive Applications.
Neue Sheets: `field_evidence: R0`. Application maturity `implementation: R2`
= Desk-Pin-Verifikation, nicht Feld.

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.

## Lessons → Transfer

- Connected-App-Stack und USB-MSC sind **orthogonale** HU-Schnittstellen.
- Mehrere Etch-Ports (4004/4006/4007/8003) = Pfadabhängigkeit, kein Widerspruch per se.
- Dissector + Client-Code + Analysis konvergieren auf Framing → starke Desk-Lage; trotzdem R0 bis eigenes Capture.
- Marketing „NBT Evo“ ≠ on-wire `hmi.type`.
- Consumer-Forks (RSS/Wetter) nicht mit Protokoll-RE verwechseln.

---

## Experiments

| Experiment | Frage | Ergebnis | Class | Grenzen |
|------------|-------|----------|-------|---------|
| IDriveExperiments/richtext | Richtext List-Model + Markup? | Code setzt modelType Richtext / Tags | FACT Code; HU `UNKNOWN` | Ein Modul; kein Log des HU-Erfolgs |
| BclCarLink (Exploration) | Direkter BT-BCL-Talk | Client-Implementierung vorhanden | FACT impl | Kein Feld-Trace hier |
| Simulator SAS stub | App ohne Security-Modul? | Login no-op, 16 Null-Challenge | FACT lab | ≠ Produktions-HU |
| Analysis historical captures | BCL/Etch beobachtet? | Docs + Dissector behaupten Observation | INFERENCE für *dieses* Audit | Captures nicht erneut geprüft |

Keine Hypothese dieser Kampagne als `REJECTED` durch Experiment widerlegt;
`REJECTED` nur für unzulässige Claim-Transfers (s. Kill).

---

## Reverse-Engineering-Arten (nicht mischen)

| Art | Beispiele in BG |
|-----|-----------------|
| Direct observation | Analysis/Dissector *historisch* (Captures); **diese Kampagne:** keine neuen Captures |
| Static inference | `BMWRemoting.etch`, `BclPacket`, AIDL Security |
| Behavioural inference | „nach Handshake SelectProto“ in Client-State-Machine |
| Implementation assumption | USB/ENET „supported“ in README ohne Code |

---

## Antworten A–H

**A — Neu im technology-audit?**  
Connected-App-Protokollkarte BCL→Etch→RHMI/AV/CDS/AM; SAS-Reihenfolge; Port-/Intent-Modell; ID4/5/6 via Capabilities; Sheets neu.

**B — Connected-App-/iDrive-Protokollebene?**  
Phone-Apps tunneln über BCL (oft via Connected/BclCarLink), sprechen Etch `BMWRemoting`, authentisieren per SAS, dann RHMI/AV/…

**C — Rekonstruierbare Zustandsmaschinen?**  
BCL: OPENING→HANDSHAKE→(SELECTPROTO/KNOCK)→ACTIVE→HANGUP.  
App: Announce→TCP Etch→SAS→rhmi_create…→event loop.  
AV: create→requestConnection→granted/denied/playerState/buttons.

**D — Empirisch belegt (in BG-Sinn)?**  
Code+IDL+Dissector-Konvergenz = starke **Desk-FACTS**. Eigene Feld-Empirie: **nein** (R0). Analysis „observed challenge 16 B“ = INFERENCE hier.

**E — Nur Implementierung / Inferenz?**  
Init-Bytes `12345678`, erzwungenes Proto 3, Proxy-4007, Simulator-Stubs, AppType-Namen, USB/ENET-Behauptung.

**F — Ergänzung hu-probe?**  
Complementary/Gap-Protokollschicht; bestätigt nur Plattform-Label/Generationsvorsicht; **keine** MSC-Messergänzung.

**G — PiDrive-Annahmen?**  
Bestätigt: NBT Evo relevant. Geschwächt: „MSC ist der einzige denkbare Medienkanal“ als Absolutclaim. Unberührt: MSC Prefetch/Busy/Geometry FACTS. Nicht empfohlen: RHMI als Drop-in ohne Evidence.

**H — Wertvolle neue Untersuchungen?**  
(1) Eigenes BCL-Capture BT und/oder USB. (2) Etch-Session gegen Ziel-HU oder Simulator. (3) `hmi.*` Capabilities der Feld-HU. (4) AV vs MSC Parallelbeobachtung. Siehe FOLLOW-ON.

---

## Vorgeschlagene Engineering Actions (nur Vorschläge)

1. KB: Sheets gepflegt halten; bei eigenem Capture Application `field_evidence` anheben.  
2. Optional Lab: Simulator-kt als Fake-HU für Client-Tests.  
3. **Nicht:** PiDrive auf Connected-App umbauen; hu-probe FACTS ändern; Security bypassen.

## Bezug

[INVENTORY](../../projects/bimmergestalt-idrive-refs/INVENTORY.md) ·
[PROTOCOL](PROTOCOL.md) · [evidence](evidence.md) · [CROSSREF](CROSSREF.md) ·
Host-C: [`bmw-nbt-evo`](../../technologies/bmw-nbt-evo/SHEET.md)
