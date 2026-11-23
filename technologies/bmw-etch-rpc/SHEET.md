# Technology Sheet: BMW Etch RPC (BMWRemoting)

```yaml
slug: bmw-etch-rpc
title: BMW Etch RPC — BMWRemoting Connected-App API
primary: H
tags: [automotive, protocol, foreign-desk, rpc]
type: technology
status: active
seen_in: [bimmergestalt-idrive-refs, hu-probe, esp32-bt-analyzer]
maturity:
  technology: R2
  implementation: R1
  field_evidence: R3   # B3 FIELD_B3_GATEB — BinaryTaggedData reassembly + method registry
  reusability: W2
  evidence_scope: [LAB, FIELD]
```

Ebene **A** + F20-Feld. Fremdquellen: `IDriveConnectKit` (`BMWRemoting.etch`),
`BMWConnectedAnalysis/docs/protocol-etch.md`, AAIdrive/Simulator-Nutzung.
Wire: Apache Etch BinaryTaggedData v3 (Symbol-Hashes; `.ewh` für Wireshark).  
Field: [`bmw-etch-rpc-binary-reassembly-2026-11-21`](../../audits/bmw-etch-rpc-binary-reassembly-2026-11-21/) ·
Methode [`raw-bcl-etch-forensic`](../../methods/raw-bcl-etch-forensic.md).

## Kurzfassung

Nach BCL-Tunnel sprechen Connected Apps **Apache Etch RPC** gegen den Dienst
`BMWRemoting`. Die IDL definiert u. a. **SAS** (Auth), **CDS**, **AM** (App Manager),
**RHMI**, **AV**, **map**. Authentifizierung: App-Zertifikat → Challenge → Login
(`sas_certificate` / `sas_login`). Vertiefung (Cert, Crypto, SecurityService, Gates):
[`bmw-sas-auth`](../bmw-sas-auth/SHEET.md) und Audit
`bmw-connected-sas-auth-2026-11-06`. Dieses Sheet hält die **API-Oberfläche** und die
**Wire-Reassembly-Regeln**; keine Bypass-Anleitung.

## Abgrenzung

- **Ist:** RPC-Surface, Session-Einstieg, Subsysteme.
- **Ist nicht:** BCL-Framing; RHMI-Widget-XML (→ `bmw-rhmi`); USB-MSC.
- **Grenzt an:** [`bmw-bcl`](../bmw-bcl/SHEET.md), [`bmw-rhmi`](../bmw-rhmi/SHEET.md).

## Subsysteme (IDL-FACT + B3 Field)

| Präfix | Rolle | B3 Field |
|--------|--------|----------|
| `sas_*` | Security / Login | 18/18 Accept — [`bmw-sas-auth`](../bmw-sas-auth/SHEET.md) |
| `cds_*` | Car Data Service | create/handlers/get-set; menu visCtx **50034**; track-bus **NOT PROVEN** — [`bmw-cds-menu-path-field-2026-11-21`](../../audits/bmw-cds-menu-path-field-2026-11-21/) |
| `am_*` | App Manager | 5× registerApp; Spotify **REJECTED** — [`bmw-am-bootstrap-field-2026-11-21`](../../audits/bmw-am-bootstrap-field-2026-11-21/) |
| `rhmi_*` | Remote HMI | Handle 23 Music — [`bmw-rhmi`](../bmw-rhmi/SHEET.md) |
| `av_*` | Session Control (≠ Audio transport) | PLAY @ `P@0x315a6` — [`bmw-av`](../bmw-av/SHEET.md) |
| `map_*` | Map Import/Events (IDL; App-Nutzung selten) | nicht B3-Schwerpunkt |

## Wire Envelope & Reassembly (FIELD FACT — B3)

```
ETCH := DE AD BE EF | u32BE(body_len) | body
body := 03 | 86 <type_hash_u32BE> | …   # BinaryTaggedData v3
```

- Fragmentierung über mehrere BCL-DATA auf gleichem `(src,dest)`; nur erstes Fragment hat Magic.
- Mehrere Etch-Msgs im Rest eines BCL-Payloads möglich → byte-weise Substream-Reassembly.
- Offsets: `P@`/`H@` = Magic-Start; CSV oft BCL-Header (Etch ≈ csv+8 contiguous).
- B3: alle erfolgreichen Methoden mappten auf HASH_REGISTRY (keine unknown hashes).
- `b3.jsonl` unterdekodiert vs Raw (kein Cert) — **Raw ist Primärquelle**.

## Verbindungsmodell (Desk + Field)

```
Discovery/Announce (Connected ATTACHED Intent: host, port, instanceId)
  → TCP Etch Client (häufig 127.0.0.1 via Connected/BclCarLink-Proxy)
     oder BT BCL dest 4004 (F20 Field)
  → sas_certificate → challenge → sas_login
  → am_* / rhmi_* / cds_* / av_*
```

Ports in Fremdcode (nicht universell): Proxy **4007**, HU-dest **4004**, App-Fallback
**8003**, Simulator-Server **4006**, Prober **4004–4008**.

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| IDL = vollständige OEM-Spec | `REJECTED` | rekonstruiert/abgeleitet |
| `rhmi_create_version` wird von Apps genutzt | `REJECTED` (Nutzung) | in IDL, Kotlin-Aufrufe fehlen |
| Challenge immer 16 Bytes | `MEASURED` F20/B3; andere HUs `UNKNOWN` | |
| Ohne BMW Security-Modul kein Login | `INFERENCE` | Produktionspfad; Simulator stubbt SAS |
| Etch-Port immer 8003 | `REJECTED` | mehrere Ports je Pfad |
| Naive DEADBEEF-Suche ohne BCL = vollständiger Decode | `REJECTED` | Fragmentierung |
| Live-jsonl = vollständige Methodenliste | `REJECTED` | B3 Dissector-Gap |
| CDS = Track-Metadaten-Bus | `NOT PROVEN` | Tracks via RHMI H23 |
| Spotify = `am_registerApp` | `REJECTED` | fünf AM-Apps ohne Spotify |

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

- Welche `BMWRemoting`-Methoden sind auf NBT Evo vs ID6 tatsächlich exponiert? (B3 deckt SAS/AM/RHMI/CDS/AV auf F20)
- map_* in Feld jemals genutzt?
- Payload-Felder `ver_getVersion` / `info_getSystemInfo`

## Lessons

- Wire speichert Hashes → ohne `.ewh`/IDL schwer lesbar.
- Security-Service-Generationen (Classic vs MyBMW) parallel im Code → Versionsgate.
- Fragment-aware BCL→Etch ist Pflicht; jsonl allein reicht nicht für Cert/Crypto.
