# Technology Sheet: BMW RHMI (Remote HMI)

```yaml
slug: bmw-rhmi
title: BMW RHMI — Remote HMI for Connected Apps
primary: H
tags: [automotive, ui, foreign-desk]
type: technology
status: active
seen_in: [bimmergestalt-idrive-refs, esp32-bt-analyzer]
maturity:
  technology: R2
  implementation: R2
  field_evidence: R3   # B3 Handle-23 Music NP catalog + DESCRIPTION extract
  reusability: W2
  evidence_scope: [LAB, FIELD]
```

Ebene **A**. Fremdquellen: `IDriveConnectKit` RHMI-Deserialization,
AAIdrive/HassGestalt/Addons, `BMWConnectedAnalysis` RHMI-Docs, Simulator-Renderer.
Eigene Evidence: esp32.bt-analyzer F20 Feld 16./17.11. + B3 Gate B 21.11. + f20_sim Lab
([`audits/esp32-bt-analyzer-f20-connected-2026-11-17`](../../audits/esp32-bt-analyzer-f20-connected-2026-11-17/),
[`audits/bimmergestalt-rhmi-checkresource-2026-11-17`](../../audits/bimmergestalt-rhmi-checkresource-2026-11-17/),
[`audits/esp32-bt-analyzer-lab-field-transfer-2026-11-17`](../../audits/esp32-bt-analyzer-lab-field-transfer-2026-11-17/),
[`audits/nbt-evo-bt-control-plane-closure-2026-11-21/`](../../audits/nbt-evo-bt-control-plane-closure-2026-11-21/),
[`audits/bmw-rhmi-music-handle23-field-2026-11-21/`](../../audits/bmw-rhmi-music-handle23-field-2026-11-21/)
— Lab Soak/Seq PASS ≠ Auto; Action 200 Lab-only; B3: Handle **23** Music NP catalog).

## Kurzfassung

**RHMI** ist die Remote-HMI-Schicht für Connected Apps: die App lädt eine
**UI-Beschreibung** (XML + Text-/Image-DBs), registriert sie per Etch
(`rhmi_create` → `checkResource`/`setResource` → `rhmi_initialize`) und aktualisiert
**Models/Properties**; die HU liefert **HMI-/Action-Events** zurück. Layout hängt an
Capabilities (`hmi.type` / `hmi.version` → ID4/ID5/ID6-Familien), nicht am
Marketing-Label „NBT“.

**Architektur:** A2DP allein ≠ RHMI. Connected + Browse/iDrive-Menü aktiviert RHMI-Wire.

## Abgrenzung

- **Ist:** App↔HU UI-Session über Etch.
- **Ist nicht:** natives iDrive-Menü der HU; USB-MSC Playlist-UI; Android-Phone-UI; A2DP-Audio.
- **Grenzt an:** [`bmw-etch-rpc`](../bmw-etch-rpc/SHEET.md) (Transport der Calls),
  AV-API für Audio-Fokus (Media ≠ nur RHMI-Widgets); Resource-Auth via [`bmw-sas-auth`](../bmw-sas-auth/SHEET.md) Digests.

## Lifecycle (Desk-FACT; Feld/Lab bestätigt Existenz)

```
Application
  → Connection (Etch + SAS)
    → rhmi_create → handle
      → für Typ in {DESCRIPTION, TEXTDB?, IMAGEDB?, WIDGETDB?}:
           checkResource(MD5, handle, size, name="", type)
           if false: setResource(handle, bytes, type)
      → rhmi_initialize(handle)
      → addAction/Hmi handlers
        → setData / setProperty
          → onActionEvent ↔ ack
```

Cache-Check = **MD5** der Bytes (`RHMIUtils.rhmi_setResourceCached`).  
Whitelist = **SHA-256** in `SAS.Digests.*` (`verifyResource` / `libhmiremoting.so`).  
Beide Prüfungen nicht vermischen.

## Komponenten / Events (Auszug)

- Komponenten: List, Label, Image, Gauge, EntryButton, ToolbarButton, Input, …
- HMI-Event-IDs in Kit-Code u. a.: Focus=1, RequestData=2, Visible=11 (Implementierungswissen; B3 Wire bestätigt 1/2/11).
- Media: RHMI-Views **plus** [`bmw-av`](../bmw-av/SHEET.md) Session-Control (≠ Audio-Transport).

### Music Handle 23 (FIELD FACT — B3)

| Item | Wert |
|------|------|
| App-ID | `me.hufman.androidautoidrive.music` |
| Handles (create) | 21 calendar · 22 readout · **23 music** · 24 mapview · 25 screenmirror |
| DESCRIPTION | MD5 `e9e31c31110680e13b7a112a7d77eb55`, 92085 B — extract CLOSED |
| NP models | **444**/655 `"Spotify"` · **445** artist · **446/447** title · **456** cover · **458** playlist |
| Actions | **336**, **248** |
| Events | **660** multimediaInfo · **661** statusbar |
| Cache | 11× `checkResource` True · 0× `setResource` · then `initialize` |

Audit: [`bmw-rhmi-music-handle23-field-2026-11-21`](../../audits/bmw-rhmi-music-handle23-field-2026-11-21/).  
CDS menu path (Media/Radio → visCtx **50034**) ist separat — Track-Bus bleibt RHMI, nicht CDS.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| RHMI = BCL | `REJECTED` | RHMI über Etch über BCL |
| „NBT“ erscheint als Protokollfeld | `REJECTED` | Runtime: `hmi.type`/`hmi.version` |
| Alle Generationen gleiche Widgets | `UNKNOWN`/`HYPOTHESIS` | Dimensions-Code unterscheidet ID4/5/6 |
| RHMI ersetzt USB-MSC Audio | `REJECTED` (als Architektur-FACT) | anderer Kanal; PiDrive-MSC bleibt eigen |
| SmartThings-Assets = offizielle Spec | `INFERENCE` | HassGestalt extrahiert APK-Ressourcen |
| Lab `RUNTIME_ACTIVE` / Soak / Seq = F20 Auto-ready | `REJECTED` | Auth CLOSED; eigener Client PoC weiter OPEN |
| `checkResource(true)` ⇒ Upload zwingend | `REJECTED` | B3: 11× check / 0× set / initialize |
| Spotify = `am_registerApp` | `REJECTED` | Media = `…music` RHMI + AV |
| Lab actionId **200** / Sink `PI_DRIVE_TEST` = F20-Map | `REJECTED` | Field: **336/248** |
| Lab modelId **100** = F20 NP | `REJECTED` | Field: **444–447** (+655/458/…) |
| modelId 4 / SE 213 blockiert Session | `REJECTED` (Lab) | non-fatal; Nebenpfad |
| RHMI PLAY-UI = hörbares Audio | `REJECTED` | siehe [`bmw-av`](../bmw-av/SHEET.md) |

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

- F20: exakte SHA-256-Digest-Liste der akzeptierten Resources (Whitelist-Korrelation).
- Eigener RHMI-Client PoC mit Field-IDs 444/445/446·447/660/661/336/248.
- TEXTDB/IMAGEDB Extract (DESCRIPTION CLOSED).
- Richtext-List-Model: HU-seitig bestätigt?
- Home/Launcher Entry Object-ID (**NOT OBSERVED** in B3).

## Lessons

- Marketing-Generation ≠ Capability-String.
- Resource-Digests in Certs sind der **Hauptblocker** für eigene Uploads (Desk Doc + Lab whitelist + Feld checkResource) — autorisierte Bytes nötig, nicht nur korrekte Etch-Calls.
- `checkResource(true)` ⇒ kein `setResource` für diesen Typ; danach `initialize`.
- Sneaky-Apps senden oft nur DESCRIPTION (keine TEXTDB/IMAGEDB), um Unsigned-Rejects zu vermeiden.
- Lab Action→eigene Sink beweist Verdrahtbarkeit, nicht OEM-Semantik am F20 — Field-IDs jetzt bekannt.
- Ältere Freezes (ESP/RFCOMM „OPEN P0“ in FREEZE_C5CB0E6) durch write11-Retry-Stand **SUPERSEDED** — Connected-Transport nicht erneut aufmachen.
