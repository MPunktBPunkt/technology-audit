# Audit Campaign: usb-control-stall-recovery-2026

```yaml
id: usb-control-stall-recovery-2026
project_id: usb-bot-observation
started: 2026-10-14
ended: 2026-10-14
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: usb-msc
reuse_outcomes:
  reused: [usb-msc]
  new: []
  not_helped:
    - "usbsnoop / Hardware-Sniffer bewusst nicht priorisiert."
    - "Timing-Lücke und S1–S3 bleiben eigene Arbeit, kein Fremd-Audit."
    - "USB↔WiFi Issues liefern Korrelation/Hypothesen, keine Root-Cause für die Sonde."
  process: "Schmales Follow-on: Control/Enum/STALL-Hook-Karte + Port-/Enum-Semantik; kein Code-Import."
  decisions_touched: [control-epoch-hooks, mount-umount-coupling, no-vbus-replug, wifi-usb-hypothesis-only]
```

## Ziel

Die nach dem BOT-/Instrumentierungs-Audit **fehlenden GATE-01-Control-Pfade**
desk-schließen: `SET_ADDRESS`, `SET_CONFIGURATION` → `tud_mount_cb` /
`tud_umount_cb`, Endpoint-STALL / CLEAR_HALT, `MSC_STAGE_NEED_RESET`, plus
ESP-Port-Kopplung (esp_tinyusb) und praktische Enum-/Replug-Semantik
(EspUsbDevice). WiFi↔USB nur als Hypothesenregister.

## Scope

- **Im Scope:** TinyUSB `usbd.c` + `msc_device.c` (Control/STALL/NEED_RESET);
  `espressif/esp-usb` `device/esp_tinyusb/` (Mount/Umount, Descriptors);
  `tanakamasayuki/EspUsbDevice` Docs (Enum-Stufen, kein VBUS-Sense, Replug);
  ausgewählte esp-idf / arduino-esp32 Issues (USB↔WiFi Korrelation).
- **Nicht im Scope:** Code-Import; usbsnoop; Hardware-Sniffer; Eager/Prefetch;
  Timing-Messung; S1–S3-Leiter; NBT-Capture; paralleles Technology Sheet;
  Root-Cause-Behauptung für WiFi-Death der Sonde.

## Bezug zur Vor-Kampagne

| Vorher ([`…-instrument-sources`](../usb-bot-observation-2026-instrument-sources/)) | Diese Kampagne |
|-----------------------------------------------------------------------------------|----------------|
| CBW/CSW-Hooks in `msc_device.c` | Device-Stack Control in `usbd.c` |
| Class Clear-Halt / NEED_RESET skizziert | CLEAR_FEATURE-Interplay Stack↔MSC vertieft |
| Host-eBPF SETUP nur als Decode-Hinweis | Device-seitige Enum-Epochs + Mount-Kopplung |
| App-Callbacks ohne CBW | Port: `tud_mount_cb` → MSC-Storage / Events |

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1, Kampagnenartefakte | erfüllt |
| 2 | Primärquellen auf immutable SHA (pfadspezifisch) | erfüllt |
| 3 | Hook-Karte: SET_ADDRESS, SET_CONFIGURATION, STALL, CLEAR_HALT, NEED_RESET | erfüllt |
| 4 | esp_tinyusb: Mount/Umount + Descriptor-Control belegt | erfüllt |
| 5 | EspUsbDevice: Enum-Semantik / kein VBUS / Replug dokumentiert | erfüllt |
| 6 | USB↔WiFi nur als `HYPOTHESIS`-Register, keine Root-Cause | erfüllt |
| 7 | Timing / S1–S3 / NBT weiter `UNKNOWN` | erfüllt |
| 8 | C10–C13; kein paralleles Sheet | erfüllt |

## Decision Trace

Desk-Kampagne mit Go/No-Go für Control-/Enum-Instrumentierung der Sonde (**C10**).

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|-----------------|
| Enum-Epochs an `usbd.c` SET_ADDRESS / SET_CONFIGURATION + `tud_mount_cb`/`tud_umount_cb` hängen | Wo endet Enumeration und öffnen Klassen-EPs? | `EVID-USBCTRL-2026-10-14-001`–`003`, `006` | Ja — nach `SET_CONFIGURATION n`; cfg 0 = umount | `DISCOVERED DURING TEST` |
| CLEAR_HALT und NEED_RESET getrennt loggen | Löst Clear-Halt NEED_RESET? | `EVID-USBCTRL-2026-10-14-004`, `005` | Nein — bei NEED_RESET bleibt Stall; nur BOT Reset (`0xFF`) | `DISCOVERED DURING TEST` |
| Replug ohne VBUS: State auch bei Mount clearen | Feuert umount bei Replug? | `EVID-USBCTRL-2026-10-14-007`, `008` | Oft nein — nur `SET_CONFIGURATION n` zuverlässig | `DISCOVERED DURING TEST` |
| WiFi-Death nicht aus Fremd-Issues schließen | Belegen Issues Root-Cause der Sonde? | `EVID-USBCTRL-2026-10-14-009` | Nein — nur Hypothesen / Chip-Korrelation | `KNOWN BEFORE TEST` |

## Engineering Review Checks

Zielcode eines Device-Loggers / einer Sonde (**C11**).

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|-----------------|
| `001`–`003` | Events `usb_set_address`, `usb_set_config` (cfg_num), `usb_mount` / `usb_umount` | `DISCOVERED DURING TEST` |
| `004`–`005` | CLEAR_HALT vs. BOT Reset vs. NEED_RESET als getrennte Epochs; keine Tag-Korrelation über NEED_RESET | `DISCOVERED DURING TEST` |
| `006` | Auf ESP-Port: Mount↔MSC-Storage-Ownership und `TINYUSB_EVENT_ATTACHED/DETACHED` | `DISCOVERED DURING TEST` |
| `007`–`008` | Ohne VBUS-Sense: Detach nicht annehmen; State bei Mount und (falls) Umount clearen | `DISCOVERED DURING TEST` |
| `009` | WiFi+USB gleichzeitig: PHY/PLL-Workaround und Last als Lab-Dimension, nicht Desk-FACT | `DISCOVERED DURING TEST` |

## Kill-Kriterien

Präregistriert für künftigen Lab (**C12**); hier kein Messlauf.

**Hypothese:** Control-/Enum-Events am Device korrelieren mit Host-SETUP und
unterscheiden Mount, Clear-Halt und BOT-Reset-Recovery.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | `SET_CONFIGURATION n` ohne Mount-Event oder cfg≠n | präregistriert — kein Messlauf |
| 2 | NEED_RESET wird fälschlich als „geheilt durch Clear-Halt“ geloggt | präregistriert |
| 3 | Replug ohne VBUS als Umount-Sequenz behauptet | präregistriert |
| 4 | WiFi-Issue als Root-Cause der Sonde verkauft | permanenter Integritäts-Kill |
| 5 | Timing-/S1–S3 aus diesem Desk abgeleitet | permanenter Integritäts-Kill |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| BOT-Command-Beobachtung | [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md) |
| Trace-Korrelation | [`msc-trace-correlation`](../../methods/msc-trace-correlation.md) |

## Bezug Inventar

- Inventar: [`usb-bot-observation/INVENTORY.md`](../../projects/usb-bot-observation/INVENTORY.md)
- Application: [`applications/usb-msc.md`](../../projects/usb-bot-observation/applications/usb-msc.md)
- Sheet: [`technologies/usb-msc/SHEET.md`](../../technologies/usb-msc/SHEET.md)
- Vorläufer: [`usb-bot-observation-2026-instrument-sources`](../usb-bot-observation-2026-instrument-sources/)

## Ergebnisse

- [`evidence.md`](evidence.md) — `EVID-USBCTRL-2026-10-14-*`
- Control-/Enum-Hook-Karte → Sheet-/Application-Wachstum
- Bericht: [`docs/reports/2026-10-14-usb-control-stall-recovery.md`](../../docs/reports/2026-10-14-usb-control-stall-recovery.md)

## Knowledge Feedback

**C13:** n/a für Lab/Field — Desk-only.

| Ergebnis | Evidence-ID | Zurück in |
|----------|-------------|-----------|
| Control/Enum/STALL Desk | `EVID-USBCTRL-2026-10-14-001`–`009` | [`usb-msc` Application](../../projects/usb-bot-observation/applications/usb-msc.md) · Sheet A |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 präregistrierte Kill-Kriterien | PASS; Status offen (kein Messlauf) |
| C13 Knowledge Feedback | n/a dokumentiert |

## Lessons → Transfer

- Enumeration endet erst bei `SET_CONFIGURATION n` → `tud_mount_cb`; Address allein ≠ mounted.
- Clear-Halt heilt **nicht** `MSC_STAGE_NEED_RESET`; BOT Class-Reset ist Pflicht.
- Ohne VBUS-Sense: Replug oft ohne `tud_umount_cb` — Mount-Hook ist die sichere Epoch.
- USB↔WiFi-Fremdissues stützen Hypothesen (PHY/PLL, Last), ersetzen kein Lab an der Sonde.

## Offene Punkte nach Abschluss

- Device-Logger: Control-Events + BOT-Hooks gemeinsam implementieren
- Timing-Lücke / S1–S3 / Transparenz: eigene Messarbeit
- WiFi-Death der Sonde: Lab unter USB-Last, nicht Issue-Ableitung
