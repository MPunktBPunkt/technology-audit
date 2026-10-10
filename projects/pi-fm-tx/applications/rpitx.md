# Project Application: rpitx in pi-fm-tx

```yaml
project_id: pi-fm-tx
tech_slug: rpitx
status: active
sheet: ../../../technologies/rpitx/SHEET.md
audit: ../../../audits/pi-fm-tx-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

## Rolle

[F5OEO/rpitx](https://github.com/F5OEO/rpitx) @ `ee7ff57` — Multi-Mode-TX-Plattform (5 kHz–1500 MHz laut README), nicht nur UKW-WAV. FM+RDS ist **eine** Demo unter vielen (`testfmrds.sh`, `src/pifmrds`).

## Pfade

| Pfad | Rolle |
|------|-------|
| `README.md` | Legal, BPF-Warnung, Pi-Matrix (Pi4 beta) |
| `install.sh` | csdr, librpitx, `gpu_freq=250` Prompt |
| `src/librpitx/` (clone) | TX-Kern |
| `src/pifmrds/` | FM-RDS-Untermenge |
| `src/sendiq.cpp` / Mode-Dirs | IQ / SSB / SSTV / POCSAG / … |
| `easytest.sh` | Menü; Demos oft 434 MHz ISM |

## Abgrenzung in diesem Projekt

| Bedarf | Wohin |
|--------|-------|
| Nur WAV→UKW | `rpi-gpio-fm-tx` (markondej/pifm) |
| RDS-Felder/Protokoll | `fm-rds` |
| Viele Modulationsarten / Bänder | **diese** App |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| 5 kHz–1500 MHz + Bildungs-/Legal-Disclaimer | `EVID-RPITX-2026-10-10-001` | `FACT` |
| Filter/BPF-Warnung Hardware | `EVID-RPITX-2026-10-10-002` | `FACT` |
| Install ändert `/boot/config.txt` (`gpu_freq=250`) | `EVID-RPITX-2026-10-10-003` | `FACT` |
| Pi4 „In beta mode“ in Matrix | `EVID-RPITX-2026-10-10-004` | `FACT` |
| FM-RDS Demo + `src/pifmrds` | `EVID-RPITX-2026-10-10-005` | `FACT` |
| GPIO4 als Antennenpin | `EVID-RPITX-2026-10-10-006` | `FACT` |
