# Technology Sheet: BMW RHMI (Remote HMI)

```yaml
slug: bmw-rhmi
title: BMW RHMI — Remote HMI for Connected Apps
primary: H
tags: [automotive, ui, foreign-desk]
type: technology
status: active
seen_in: [bimmergestalt-idrive-refs]
maturity:
  technology: R2
  implementation: R0
  field_evidence: R0
  reusability: W2
  evidence_scope: []
```

Ebene **A**. Fremdquellen: `IDriveConnectKit` RHMI-Deserialization,
AAIdrive/HassGestalt/Addons, `BMWConnectedAnalysis` RHMI-Docs, Simulator-Renderer.

## Kurzfassung

**RHMI** ist die Remote-HMI-Schicht für Connected Apps: die App lädt eine
**UI-Beschreibung** (XML + Text-/Image-DBs), registriert sie per Etch
(`rhmi_create` → `rhmi_setResource` → `rhmi_initialize`) und aktualisiert
**Models/Properties**; die HU liefert **HMI-/Action-Events** zurück. Layout hängt an
Capabilities (`hmi.type` / `hmi.version` → ID4/ID5/ID6-Familien), nicht am
Marketing-Label „NBT“.

## Abgrenzung

- **Ist:** App↔HU UI-Session über Etch.
- **Ist nicht:** natives iDrive-Menü der HU; USB-MSC Playlist-UI; Android-Phone-UI.
- **Grenzt an:** [`bmw-etch-rpc`](../bmw-etch-rpc/SHEET.md) (Transport der Calls),
  AV-API für Audio-Fokus (Media ≠ nur RHMI-Widgets).

## Lifecycle (Desk-FACT)

```
Application
  → Connection (Etch + SAS)
    → RHMI session (rhmi_create / initialize)
      → UI description (XML + DBs, digest-gebunden in Certs — Doc)
        → Model / Property updates (rhmi_setData / setProperty)
          → Action/HMI events ↔ ack
            → iDrive/HU display
```

## Komponenten / Events (Auszug)

- Komponenten: List, Label, Image, Gauge, EntryButton, ToolbarButton, Input, …
- HMI-Event-IDs in Kit-Code u. a.: Focus=1, RequestData=2, Visible=11 (Implementierungswissen).
- Media: oft RHMI-Views **plus** `av_*` für Entertainment-Connection.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| RHMI = BCL | `REJECTED` | RHMI über Etch über BCL |
| „NBT“ erscheint als Protokollfeld | `REJECTED` | Runtime: `hmi.type`/`hmi.version` |
| Alle Generationen gleiche Widgets | `UNKNOWN`/`HYPOTHESIS` | Dimensions-Code unterscheidet ID4/5/6 |
| RHMI ersetzt USB-MSC Audio | `REJECTED` (als Architektur-FACT) | anderer Kanal; PiDrive-MSC bleibt eigen |
| SmartThings-Assets = offizielle Spec | `INFERENCE` | HassGestalt extrahiert APK-Ressourcen |

## Transfer

Knowledge **HIGH** für Connected-App-UI; Reuse für PiDrive nur als **alternative
Architektur-Hypothese**, nicht als Drop-in für MSC. Eigene Evidence nötig vor
Engineering.

### Projektstart-Checkliste

- [ ] Capabilities (`hmi.type`/`hmi.version`) statt Marketing-„NBT“ verwenden
- [ ] Media: RHMI-Widgets und `av_*` getrennt tracken
- [ ] Keine PiDrive-/hu-probe-MSC-Claims aus RHMI ableiten
- [ ] Application + Pins; Feld-Caps der Ziel-HU vor Architekturentscheidung

## Offene Fragen (A)

- Welche RHMI-Capabilities liefert genau die Ziel-NBT-Evo im Feld?
- Richtext-List-Model: HU-seitig bestätigt?

## Lessons

- Marketing-Generation ≠ Capability-String.
- Resource-Digests in Certs (Analysis-Doc) erklären Upload-Grenzen — Desk-INFERENCE bis eigenes Feld.
