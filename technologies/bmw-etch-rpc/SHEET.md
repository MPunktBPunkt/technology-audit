# Technology Sheet: BMW Etch RPC (BMWRemoting)

```yaml
slug: bmw-etch-rpc
title: BMW Etch RPC — BMWRemoting Connected-App API
primary: H
tags: [automotive, protocol, foreign-desk, rpc]
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

Ebene **A**. Fremdquellen: `IDriveConnectKit` (`BMWRemoting.etch`),
`BMWConnectedAnalysis/docs/protocol-etch.md`, AAIdrive/Simulator-Nutzung.
Wire: Apache Etch (Symbol-Hashes; `.ewh` für Wireshark).

## Kurzfassung

Nach BCL-Tunnel sprechen Connected Apps **Apache Etch RPC** gegen den Dienst
`BMWRemoting`. Die IDL definiert u. a. **SAS** (Auth), **CDS**, **AM** (App Manager),
**RHMI**, **AV**, **map**. Authentifizierung: App-Zertifikat → Challenge → Login
(`sas_certificate` / `sas_login`). Details der Signaturpfade sind Security-sensitiv —
dieses Sheet hält nur die **API-Existenz und Reihenfolge**, keine Bypass-Anleitung.

## Abgrenzung

- **Ist:** RPC-Surface, Session-Einstieg, Subsysteme.
- **Ist nicht:** BCL-Framing; RHMI-Widget-XML (→ `bmw-rhmi`); USB-MSC.
- **Grenzt an:** [`bmw-bcl`](../bmw-bcl/SHEET.md), [`bmw-rhmi`](../bmw-rhmi/SHEET.md).

## Subsysteme (IDL-FACT)

| Präfix | Rolle |
|--------|--------|
| `sas_*` | Security / Login |
| `cds_*` | Car Data Service (Properties/Events) |
| `am_*` | App Manager Registrierung |
| `rhmi_*` | Remote HMI |
| `av_*` | Audio/Video Connection & Player State |
| `map_*` | Map Import/Events (IDL; App-Nutzung selten) |

## Verbindungsmodell (Desk)

```
Discovery/Announce (Connected ATTACHED Intent: host, port, instanceId)
  → TCP Etch Client (häufig 127.0.0.1 via Connected/BclCarLink-Proxy)
  → sas_certificate → challenge → sas_login
  → rhmi_* / av_* / cds_* / am_*
```

Ports in Fremdcode (nicht universell): Proxy **4007**, HU-dest **4004**, App-Fallback
**8003**, Simulator-Server **4006**, Prober **4004–4008**.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| IDL = vollständige OEM-Spec | `REJECTED` | rekonstruiert/abgeleitet |
| `rhmi_create_version` wird von Apps genutzt | `REJECTED` (Nutzung) | in IDL, Kotlin-Aufrufe fehlen |
| Challenge immer 16 Bytes | `INFERENCE` | Doc „observed“ + Code-Kommentare |
| Ohne BMW Security-Modul kein Login | `INFERENCE` | Produktionspfad; Simulator stubbt SAS |
| Etch-Port immer 8003 | `REJECTED` | mehrere Ports je Pfad |

## Transfer

Für eigene Arbeit: IDL als **Hypothesenkatalog** für Captures; Simulator für UI ohne
Fahrzeug. Keine Übernahme von Auth-Implementierungsdetails in eigene Firmware ohne
rechtliche/Sicherheitsprüfung.

### Projektstart-Checkliste

- [ ] IDL-Methoden vs tatsächliche App-Aufrufe trennen (`rhmi_create_version`!)
- [ ] Port-Pfad (4004/4006/4007/8003) dokumentieren — kein „ein Port“-FACT
- [ ] SAS nur als API-Reihenfolge; keine Bypass-/Exploit-Schritte
- [ ] Application + Evidence-IDs; R0 bis eigene Session-Traces

## Offene Fragen (A)

- Welche `BMWRemoting`-Methoden sind auf NBT Evo vs ID6 tatsächlich exponiert?
- map_* in Feld jemals genutzt?

## Lessons

- Wire speichert Hashes → ohne `.ewh`/IDL schwer lesbar.
- Security-Service-Generationen (Classic vs MyBMW) parallel im Code → Versionsgate.
