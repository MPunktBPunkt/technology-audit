# Evidence — esp32-usb-analyzer-2026-field-host-matrix

Feld 2026-11-06 · Upstream FW **0.0.52** @ `688a40b` · Device `.89` Identity **`303a:1001`** · Pattern `lab_sector_v1` (512×512 B).  
Basis: [LAB_FIELD_HOST_MATRIX_2026-11-06_MEASURED](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/LAB_FIELD_HOST_MATRIX_2026-11-06_MEASURED.md) · [Feldbericht](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/reports/2026-11-06-field-host-matrix.md) · [MATRIX_SUMMARY.json](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/field_host_matrix_2026-11-06/MATRIX_SUMMARY.json)

Rohdaten bleiben im Quellenrepo — hier Claims + Links.  
**Nicht claimed:** AOA-Erfolg heute · AAIdrive-USB-Funktion · BCL/Etch on wire · transparent MITM · FAT-UI · Flash-Persist · GENERAL Host-Klassen aus n=1.

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBA-2026-11-06-001` | Fingerprint-Dimensionen (Opcode-Seq, READ cadence/size, mount/remount, WRITE, recovery) sind am Analyzer-Gadget messbar | `FACT` (Messachsen) | MEASURED.md · Method |
| `EVID-USBA-2026-11-06-002` | BMW NBT/HU mountet `303a:1001` als MSC; Session-READs kumulativ (Watch Δ + Soft-Reenum); UI Media **nicht** sichtbar (Pattern-Stick) | `MEASURED` | [bmw_hu/](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/field_host_matrix_2026-11-06/bmw_hu/) · watch/fault_phases |
| `EVID-USBA-2026-11-06-003` | Windows Laptop: volle MSC-Nutzung; nach Format+Datei **writeOps=31 / writeBytes=54272** (=106×512 B); Datei überlebt USB-Replug bei ESP-Power | `MEASURED` | [windows_laptop/](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/field_host_matrix_2026-11-06/windows_laptop/) |
| `EVID-USBA-2026-11-06-004` | Ergometer-USB-Port: **kein** Host-Verhalten (waiting, Δ reads=0) — Negativkontrolle | `MEASURED` | [ergometer/](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/field_host_matrix_2026-11-06/ergometer/) |
| `EVID-USBA-2026-11-06-005` | TV / Soundbar / FRITZ!Box: je Mount + READ-Traffic, `aoa51=0` — **Project Evidence**; keine GENERAL Host-Klassen | `MEASURED` (n=1 each) / GENERAL `REJECTED` | MATRIX_SUMMARY · host folders |
| `EVID-USBA-2026-11-06-006` | BMW P-MOUNT / CBW-Ring (class-hook): **TUR**, **MODE_SENSE(6)**, **PREVENT/ALLOW**, **READ_CAPACITY(10)**, **READ(10)** (tl=8 im Ring-Sample) | `MEASURED` | [capture_scsi_ring.json](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/field_host_matrix_2026-11-06/bmw_hu/capture_scsi_ring.json) · MEASURED § BMW |
| `EVID-USBA-2026-11-06-007` | Soft-Reenum → Remount + weitere READs (fault_phases: after_reenum reads 104→115); Identity bleibt `303a:1001` | `MEASURED` | [fault_phases.json](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/field_host_matrix_2026-11-06/bmw_hu/fault_phases.json) |
| `EVID-USBA-2026-11-06-008` | **FACT:** Unter MSC-Identity `303a:1001` (AOA-respond on/off) am NBT: **`aoa51/52/53 = 0`** trotz Mount + SCSI | `FACT` / `MEASURED` | watch.json · MATRIX_SUMMARY · Feldbericht §2.1 |
| `EVID-USBA-2026-11-06-009` | **INFERENCE:** AOA erfordert Bedingungen jenseits eines responding MSC-Endpoints. **UNKNOWN:** welche Identity/Config/State BMW-AOA startet. **REJECTED:** „HU kann kein AOA“ aus `008` allein | `INFERENCE` / `UNKNOWN` / `REJECTED` | Feldbericht §4 · Actions-Doc Korrektur #3 |
| `EVID-USBA-2026-11-06-010` | Write-Cache: Code `kWriteCache=64` Sektoren (≈32 KiB); Windows schrieb **106** Sektoren (54272 B) — Eviction/„Datenloch“ = **UNKNOWN / Test Gap** bis Write-LBA-Audit | `UNKNOWN` | after_format_file.json · [field-matrix-actions](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/8b80196/docs/reports/2026-11-06-field-matrix-actions.md) |
| `EVID-USBA-2026-11-06-011` | Phone an Analyzer Host `.88`: `dut.present=false` / `boardSourcesVbus=false` — VBUS-Gap vor Phone-Enum/MITM | `MEASURED` | [phone_on_host88_vbus_gap.json](https://github.com/MPunktBPunkt/esp32.usb-analyzer/blob/688a40b/docs/evidence/field_host_matrix_2026-11-06/phone_on_host88_vbus_gap.json) |

## Epistemic Snapshot (AOA / MSC)

```text
FACT:      MSC identity 303a:1001 did not produce AOA initiation (aoa51/52/53=0).
INFERENCE: AOA requires conditions beyond a responding MSC endpoint.
UNKNOWN:   Which exact identity / configuration / state causes BMW AOA initiation?
REJECTED:  "Host has no AOA" derived only from MSC-identity negative.
```

## BMW NBT Evo — P-MOUNT (Feld)

Beobachtet am F20 / NBT Evo gegen Analyzer-Gadget (nicht Spec-Default):

| SCSI | Ring-Count (overflow sample) | Status |
|------|------------------------------|--------|
| TEST UNIT READY (0x00) | 4 | `MEASURED` |
| MODE SENSE(6) (0x1A) | 2 | `MEASURED` — Evidenzsprung vs. „nur erwartet“ |
| PREVENT/ALLOW (0x1E) | 4 | `MEASURED` — Evidenzsprung vs. „nur erwartet“ |
| READ CAPACITY(10) (0x25) | 1 | `MEASURED` |
| READ(10) (0x28) | 10 (tl=8) | `MEASURED` |
| INQUIRY (0x12) | nicht im Overflow-Ring-Sample | `UNKNOWN` dieser Capture (Ring `dropped≈2476`) |

## Host-Matrix (Kurz — Project Evidence)

| Host | USB Host? | Mount | Δ Reads (Slice) | AOA | KB-Rolle |
|------|-----------|-------|-----------------|-----|----------|
| BMW NBT/HU | yes | yes | Watch Δ11; Soft-Reenum +11 | 0 | Tech: `bmw-nbt-evo` + Fingerprint-Ref |
| Windows | yes | yes | large READ; WRITE 31/54272 B | 0 | Fingerprint-Ref (OS host) |
| FRITZ!Box | yes | yes | +37 / ~148 KiB | 0 | Project only |
| Soundbar | yes | yes | +10 / replug +20 | 0 | Project only |
| TV | yes | yes | +1 / 4 KiB | 0 | Project only |
| Ergometer | **no** | no | 0 | 0 | Negativkontrolle |

## Offene Claims / Test Gaps

| Claim | Status | Nächster Schritt |
|-------|--------|------------------|
| Write-Cache Eviction / 64 vs 106 Sektoren | `UNKNOWN` | Upstream Write-LBA-Audit (P0-F) |
| C0 Identity vs FAT Content am BMW | offen | P0-A |
| C1 AOA phone-like Identity | offen | P0-B → dann Full Audit prüfen |
| Phone Enum an `.88` | VBUS-Gap `011` | Self-powered Hub |
| Host-Klassen (minimal/scanner/FS/OS) | noch nicht | Wiederholung n≥3 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-02 | Soft-Lab 0.0.50 Capability / OTG Baseline (`60244b3`) |
| 2026-11-06 | Feld Host-Matrix @ `688a40b` — Evidence-Update diese Kampagne |
| nach C1 | geplanter Zeitpunkt für nächsten Full Audit (AOA→BCL→Etch) |
