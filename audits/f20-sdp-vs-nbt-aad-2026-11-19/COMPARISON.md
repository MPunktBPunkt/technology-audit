# NBT-AAD vs unsere F20-HU (SDP-Fokus)

Quellen: NBT-AAD `@0941aec` (Prior OSS-Audit) · F20 `FIELD_B1_FROM_A6_20261113T062824Z`.

## Entscheidungsmatrix

| Merkmal | NBT-AAD | Unsere F20-HU (stock) | Bewertung |
|---------|---------|----------------------|-----------|
| Bluetooth SPP / RFCOMM | **FACT** — `/dev/btsppN`, Connectivity | **FACT** — ch 5–10 (+ andere Profile) | **gemeinsame Transportklasse** |
| Service UUID | **FACT** `4de17a00-52cb-11e6-bdf4-0800200c9a66` | **MEASURED** `0x1101` (ch 6–10); `deca-fade` (ch 5); **kein** AA-UUID | **verschieden — Kill** |
| Service Name | **FACT** `AndroidAuto` | **MEASURED** `SPP Server 0…5` | **verschieden** |
| RFCOMM Channel | **UNKNOWN** fest verdrahtet (Connectivity vergibt Node); nicht im Daemon hardcodiert | **MEASURED** Connected → **6** (failover **10**); iAP → **5** | **nicht vergleichbar als „gleicher Einstieg“** |
| Protocol Descriptor | SPP über DSI `SppUuidRegister` | Attr `0x0004` present; L2CAP+RFCOMM | gleiche *Gattung*, anderer Record |
| HU-Daemon | **FACT** `nbt-aad` | Connected: OEM (`A4AHandler`/Media — Secondary Source-Claim); nicht nbt-aad | **verschieden** |
| RHMI Plugin | **FACT** native `NbtAad` RA-Plugin | **FACT** Remote RHMI over Etch nach SAS | ähnliche HMI-Idee, **anderer Wire** |
| Wi-Fi-Handoff | **FACT** erforderlich (AA session) | **nicht** im Connected-Feldpfad | **verschieden** |
| HS / KNOCK / ACK10 | **NO EVIDENCE** in NBT-AAD | **MEASURED** | **verschieden** |
| SAS | **NO EVIDENCE** | **beobachtet** (Blocker Credentials) | **verschieden** |

## Zwei Pfade (sauber getrennt)

```
NBT-AAD (modifizierte HU)
Phone ── SDP finds AA-UUID ──► RFCOMM ──► nbt-aad ──► Wi-Fi/TCP AA
                                      └── RHMI plugin (native)

Unsere F20 (stock Connected)
Phone ── SDP finds 0x1101 ──► RFCOMM SCN 6/10 ──► BMW HU
                                      ├── HS
                                      ├── KNOCK
                                      ├── ACK10
                                      └── SAS / Etch / RHMI
```

## Plausibler gemeinsamer Einstieg?

| Ebene | Urteil |
|-------|--------|
| SDP Service Record | **Nein** — UUID/Name fehlen auf Stock-F20 für NBT-AAD |
| RFCOMM Channel Binding | **Nein** — Connected = `0x1101`@6/10; AA-UUID nicht vorhanden |
| Connectivity SPP-Manager (Plattform) | **Ja, nur architektonisch** — HU kann mehrere SPP-Records hosten; NBT-AAD *fügt* einen hinzu |
| Post-SPP Session Protocol | **Nein** — AA WifiStart vs BCL/Etch/SAS |

**Antwort auf die Leitfrage:**  
Wenn SDP nicht zusammenpasst → NBT-AAD endgültig **Architektur-Referenz**, nicht Connected-Implementierung.  
Der „Unterschied nach gemeinsamem SPP-Einstieg“-Ansatz **fällt aus**: es gibt keinen gemeinsamen SDP-Service-Einstieg.

## Was von NBT-AAD trotzdem weiter gilt (ohne BT-Deep-Dive)

Bereits im Prior-Audit belegt, unverändert nützlich:

- Multi-Tenant `/dev/btspp*` + `looksLikeBmwBcl` (Fremdverkehr-Heuristik)
- Native PluginApp Lifecycle für ArtiDrive-Domain
- Plane-Trennung Config/Debug ≠ Runtime

**Nicht** gerechtfertigt: weiterer Dive in `wireless_setup` / AA-Handshake / Wi-Fi-Credential-Pfad als Connected-Proxy.

## Korrektur zur Entwurfstabelle

| Entwurf | Korrektur |
|---------|-----------|
| „RFCOMM Channel bekannt“ (NBT-AAD) | Channel# im Daemon **nicht** hardcodiert → **UNKNOWN** bis Feld auf modifizierter HU |
| „Service UUID … Feld messen“ | **bereits gemessen** (`FIELD_B1`) — kein neues Capture nötig für diesen Crosswalk |
| „wenn SDP gut zusammenpasst → NBT-AAD-BT lohnt“ | Bedingung **nicht erfüllt** → NO-GO |
