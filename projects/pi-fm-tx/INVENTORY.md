# Project Inventory: Pi FM / RF Transmit (Fremd)

```yaml
project_id: pi-fm-tx
updated: 2026-10-10
reviewed_commit: "pifm@6c30d00 PiFmRds@2707ecc fm_transmitter@322500e rpitx@ee7ff57 Pi-Fm_transmitter@552f955 pi-fm-player@f602f42"
profile: lab-tool
pilot_order: [rpi-gpio-fm-tx, fm-rds, rpitx]
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Klassiker/DMA/Mailbox UKW-FM | `rpi-gpio-fm-tx` | Sheet + App (pifm, markondej, zoroxide, player) |
| PiFmRds PLL+RDS | `rpi-gpio-fm-tx` + `fm-rds` | wachsen |
| markondej aktiv / Pi4 GPIO21 / kein Pi5 | `rpi-gpio-fm-tx` | Fallstricke A |
| zoroxide Install-Fork | `rpi-gpio-fm-tx` | gleicher Slug (kein Fork-Sheet) |
| pi-fm-player systemd+ffmpeg | `rpi-gpio-fm-tx` | Ops in App; systemd observed |
| rpitx Multi-Mode 5kHz–1.5GHz | `rpitx` | **neu** (nicht FM-Sheet aufblasen) |
| rpitx FM-RDS Untermenge | `fm-rds` | seen / Evidence |
| Empfang PiDrive | `rtl-sdr`, `dab-plus`, … | **Abgrenzung** |

Kampagne: [`pi-fm-tx-2026-foreign`](../../audits/pi-fm-tx-2026-foreign/).  
Kontrast Empfang: [`pidrive`](../pidrive/).

## Übersicht

| Slug | Name | Primary | Tags | Status | Coverage | Sheet | Application |
|------|------|---------|------|--------|----------|-------|-------------|
| `rpi-gpio-fm-tx` | RPi GPIO/Clock FM TX | D | `radio-tx`, `lab-only` | applied | partial | [SHEET](../../technologies/rpi-gpio-fm-tx/SHEET.md) | [app](applications/rpi-gpio-fm-tx.md) |
| `fm-rds` | FM-RDS | C | `radio-tx`, `metadata` | applied | partial | [SHEET](../../technologies/fm-rds/SHEET.md) | [app](applications/fm-rds.md) |
| `rpitx` | rpitx Multi-Mode RF TX | D | `radio-tx`, `lab-only` | applied | partial | [SHEET](../../technologies/rpitx/SHEET.md) | [app](applications/rpitx.md) |
| `fm-broadcast-mpx` | FM Stereo MPX | B | `streaming` | observed | none | — | — |
| `bcm-mailbox-dma` | Mailbox / DMA mem | D | `fragile` | observed | none | — | — |
| `librpitx` | librpitx | D | `radio-tx` | observed | none | — | — |
| `systemd` | systemd unit wrapper | F | `linux-userspace` | observed | none | — | — |

## Nach Kategorie

### C — Protokolle

`fm-rds`

### D — Embedded

`rpi-gpio-fm-tx`, `rpitx` (+ observed mailbox/librpitx)

### F — Systemintegration

`systemd` (observed — pi-fm-player)

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Pi 5 / RP1 | markondej: unsupported | beobachten |
| Harmonic-/Filter-Messung | kein Lab | optional Method |
| rpitx Mode-für-Mode | Desk-Überblick | bei Bedarf vertiefen |

## Signale ohne Eintrag

- Syncthing / Uptime-Kuma in pi-fm-player README (Ops-Umgebung)
- csdr als DSP-Abhängigkeit (rpitx install)
