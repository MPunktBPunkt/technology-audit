# Audit Campaign: f20-sdp-vs-nbt-aad-2026-11-19

```yaml
id: f20-sdp-vs-nbt-aad-2026-11-19
project_id: esp32-bt-analyzer
started: 2026-11-19
ended: 2026-11-19
status: closed
profile: ops-field
standard_version: "0.7.1"
standard_gaps: []
continuation_of: audits/nbt-evo-oss-runtime-hmi-bt-2026-11-19/
field_pins:
  FIELD_B1_FROM_A6: "FIELD_B1_FROM_A6_20261113T062824Z"
  source_capture: "FIELD_A6_HU_20261113T062824Z.btsnoop"
  source_sha256: "6806083f2d4534edc5c7e75fb9ca2e060ae77e83430c6e36633f9a168f55f8b7"
  hu: "BMW 38304 / D4:36:39:CF:E1:B5 / F20"
nbt_aad_pin: "Sq00ky/Supra-iDrive6-Android-Auto@0941aec"
reuse_outcomes:
  reused:
    - projects/esp32-bt-analyzer/applications/bmw-nbt-evo.md
    - audits/nbt-evo-oss-runtime-hmi-bt-2026-11-19/
    - audits/bmw-bcl-rfcomm-role-2026-desk/
    - technologies/bmw-bcl
  new: []
  process: "No new OSS scan; SDP crosswalk from existing F20 field decode only."
  decisions_touched:
    - reject-nbt-aad-as-connected-entry
    - fact-f20-sdp-no-aa-uuid
    - fact-connected-uses-0x1101-ch6
```

## Ziel

Feststellen, ob der **NBT-AAD-Bluetooth-Einstieg** (SDP UUID / SPP) mit dem, was unsere
**F20-HU tatsächlich advertisiert**, einen gemeinsamen Connected-Einstiegspunkt teilt —
oder nur die allgemeine SPP-Fähigkeit der Plattform.

## Scope

| Im Scope | Out of Scope |
|----------|--------------|
| `FIELD_B1_FROM_A6` HU SDP catalog | Neues Feld, neues Capture |
| Vergleich Service UUID / Name / RFCOMM / Profile vs NBT-AAD | NBT-AAD Wireless-/AA-Protokoll-Deep-Dive |
| Ableitung: weiterer NBT-AAD-BT-Code lohnt sich? | SAS / Etch Payload |

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Vollständiger HU-SDP-Katalog (Feld) | erfüllt → [SDP-CATALOG.md](SDP-CATALOG.md) |
| 2 | Vergleichsmatrix NBT-AAD vs F20 | erfüllt → [COMPARISON.md](COMPARISON.md) |
| 3 | Go/No-Go weiterer NBT-AAD-BT-Analyse für Connected | erfüllt → **NO-GO** |

## Kernurteil

**SDP passt nicht.** Stock-F20 advertisiert **kein** `4de17a00-52cb-11e6-bdf4-0800200c9a66`
(`AndroidAuto`). Connected landt über generisches SPP `0x1101` auf **SCN 6** (Failover 10).

```
Gemeinsam:     Bluetooth SPP/RFCOMM als Transportklasse der HU-Connectivity
Nicht gemeinsam: Service UUID, Service Name, Channel-Bindung, Session-Protokoll danach
```

→ NBT-AAD bleibt **Architektur-Referenz** (SPP-Multi-Tenant, RHMI-Plugin, Config≠Runtime).  
→ NBT-AAD ist **nicht** Connected-Implementierung und **kein** gemeinsamer SDP-Einstieg.  
→ Weiterer NBT-AAD-Bluetooth-/WifiStart-Code für den Connected-Pfad: **REJECT**.

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz |
|--------------|-------|----------|------------|
| Gemeinsamer SDP-Einstieg NBT-AAD ↔ Connected? | Advertised F20 die AA-UUID? | `FIELD_B1` classes list — AA absent | **Nein** |
| Welcher SDP-Record ist Connected? | Was trifft BclCarLink `0x1101`? | ch 6 first-match; Feld BCL SCN 6/10 | **0x1101 / SCN 6** |
| NBT-AAD-BT weiter analysieren? | Nur wenn SDP zusammenpasst | passt nicht | **NO-GO** |

## Kill

**Hypothese:** „NBT-AAD und F20-Connected teilen denselben SDP-Service-Einstieg.“

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | F20-SDP enthält AA-UUID nicht; Connected nutzt `0x1101` | **getroffen** |

## Artefakte

- [SDP-CATALOG.md](SDP-CATALOG.md) — alle HU-advertised Services  
- [COMPARISON.md](COMPARISON.md) — NBT-AAD vs F20  
- Prior: [`../nbt-evo-oss-runtime-hmi-bt-2026-11-19/`](../nbt-evo-oss-runtime-hmi-bt-2026-11-19/)
