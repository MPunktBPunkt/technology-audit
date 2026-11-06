# Project Scope: esp32.usb-analyzer

```yaml
project_id: esp32-usb-analyzer
title: Dual ESP32-S3 USB Protocol Analyzer / MITM Lab
updated: 2026-11-06
source_repo: https://github.com/MPunktBPunkt/esp32.usb-analyzer
reviewed_commit: 688a40b
profile_hint: lab-tool
status: active
repos:
  - https://github.com/MPunktBPunkt/esp32.usb-analyzer
```

## Zweck

Lab- und Feld-Instrument: zwei ESP32-S3 (OTG Host + OTG Device) und Debian (Discovery `:9750`, Lab-UI `:8080`) für Capture, Proxy-Slices, Protokoll-Lab (MSC/AOA/BCL-Framing/HID) und **Fremd-Host-MSC-Fingerprints** — **ohne** USB-IF-Compliance, Live-L0-Wire, transparente MITM-Claims oder AOA/BCL-Wire-FACTS aus MSC-Identity allein.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| ESP-A `.88` Host OTG | Enum / MSC Host-Probe / AOA Host / Capture | ja |
| ESP-B `.89` Device OTG | MSC(+Vendor+HID) Gadget / Responder / Capture | ja |
| Debian Control | Discovery, dual Capture-Proxy, Lab-UI (`:8080`) | ja |
| WiFi TCP `:9752` Mode A | Integrity / MSC-proxy / EP0-forward / pipeline | ja (lab) |
| OTG-Kabel Host↔Device | Baseline MSC READ/WRITE + Pattern | ja — MEASURED 0.0.50 |
| Capability / Gate10 Harness | Regressionstor Soft-Lab | ja — MEASURED |
| Path A GPIO19/20 peek | Feasibility | ja — **REJECTED** als Sniffer |
| Soft Path-B / L0-Sim | Decoder/Correlator Pipeline | ja (synth/GPIO lab) |
| PC / Fremd-Hosts als Device-Host | Enum Device-Gadget + Fingerprint | ja — Feldmatrix 2026-11-06 |
| BMW NBT als MSC-Host | P-MOUNT / Soft-Reenum / AOA-Negativ unter MSC-ID | ja — Evidence-Update; Prefetch/Media ≠ dieses Repo |
| BMW AOA positiv / BCL / Etch Wire | Connected-Apps Transport | **nein** bis C1-Positiv |
| Passives Live-D+/D− | Path-B soldered PHY | **nein** — HW offen |
| Transparent MITM PC↔Stick / Phone↔HU | Observer beyond OTG-Loop | **noch nicht** claimed |

## Nicht-Ziele

- Hard µs-Clock-Lock zwischen beiden ESPs (nur Offset-Estimate)
- High-Speed USB
- HU Connected / BCL-on-Bulk als Feld-FACT (vor C1)
- GENERAL Host-Klassen aus n=1 Consumer-Geräten
- Write-Cache-Eviction als FACT ohne LBA-Audit
- Gleichsetzung App-Callback / Class-Hook / Soft-L0-Sim mit Wire-Packets
- Soft-Unplug als Ersatz für VBUS-Unplug
- Dritter Full-USB-System-Audit ohne Knowledge-Sprung

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code | `firmware/`, `controller/`, `web/`, `tools/` | Upstream |
| Soft-Lab pin | `60244b3` / FW 0.0.50 | Capability / OTG Baseline |
| Feld pin | `688a40b` / FW 0.0.52 | Host-Matrix MEASURED |
| Gates / Architektur | `docs/GATES.md`, `GATE10_STATUS.md`, `ARCHITECTURE.md` | Claim-Grenzen |
| Feld Evidence | `docs/evidence/LAB_FIELD_HOST_MATRIX_*` + `field_host_matrix_2026-11-06/` | Evidence-Update |
| Feldbericht / Actions | `docs/reports/2026-11-06-field-host-matrix.md` · `…-field-matrix-actions.md` | NEXT C0/C1 |

## Prioritäten für die Analyse

1. Evidence-Update: Host-Fingerprint + BMW P-MOUNT + AOA/MSC-Gate (diese Kampagne)
2. Soft-Lab Revalidation bleibt Referenz (0.0.50) — kein Parallel-Full-Audit
3. **NEXT Feld:** C0 FAT Content · **C1** AOA phone-like Identity → dann Full Audit prüfen
4. Software P0: SCSI Aggregate Counters + Write-LBA-Audit
5. Offene Gates (Live-L0, transparent MITM) als UNKNOWN/REJECTED belassen

## Offene Scope-Fragen

- Wann Mode-A + Pipeline für MSC-Proxy unter Last ausreicht vs. Store-and-Forward?
- Observer-effect: welcher Kontroll-Host vor erstem „transparent“-Claim (jenseits OTG-Loop)?
- Path-B Bring-up: erste echten `.l0samp` Korrelation n≥100?
- C1: welche Identity startet BMW AOA / Connected-Apps?
