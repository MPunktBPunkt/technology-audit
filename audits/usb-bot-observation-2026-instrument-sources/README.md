# Audit Campaign: usb-bot-observation-2026-instrument-sources

```yaml
id: usb-bot-observation-2026-instrument-sources
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
    - "usbsnoop ohne erkannte Lizenz — nur Research-Kontrast, keine Implementierungsgrundlage."
    - "Adafruit-App-Callbacks sehen keinen CBW; echte bot_cbw/bot_csw-Events brauchen Stack-Hooks."
  process: "Desk-Vertiefung Instrumentierungshooks + Host-eBPF-Decode; kein paralleles Sheet."
  decisions_touched: [device-hook-map, host-lab-validate, no-new-bot-sheet]
```

## Ziel

Die offenen Instrumentierungsfragen aus
[`usb-bot-observation-2026-foreign`](../usb-bot-observation-2026-foreign/)
konkretisieren: wo im TinyUSB-Device echte CBW/CDB/CSW-Felder liegen, welche
Control-/STALL-/Reset-Pfade Epoch-Grenzen setzen, und wie ein Host-seitiger
eBPF-Sniffer (usbsnoop) Lab-Validierung liefern kann — ohne NBT-Capture und
ohne physische Paketebene.

## Scope

- **Im Scope:** gepinnte Fremdquellen (TinyUSB MSC Device, usbsnoop, Adafruit
  TinyUSB Arduino MSC, edk2 `UsbMassBot.h`, Wireshark `packet-usbms-bot.c`,
  Linux `f_mass_storage.c` als Recovery-Kontrast); Desk-Code und Doku;
  Reuse `usb-msc`; Wachstum Sheet/Method/Application.
- **Nicht im Scope:** Hardware, Build, Lab-Lauf, Fahrzeug, NBT-Timing,
  DATA0/1/ACK/NAK (Hardware-Sniffer), Code-Übernahme in Produktfirmware,
  paralleles BOT-/SCSI-Sheet.

## Bezug zur Vor-Kampagne

| Vorher ([`…-2026-foreign`](../usb-bot-observation-2026-foreign/)) | Diese Kampagne |
|------------------------------------------------------------------|---------------|
| Pfadvergleich Device / Inline / Host | Hook-Karte für Device-Logger + Host-Validate |
| TinyUSB Stages/Busy bereits `FACT` | Felder, Control, STALL, CSW-Bau, App-vs-Stack |
| USBProxy als Inline-Kandidat | usbsnoop als Host-Lab-Decode (kein usbmon) |
| Structs nur indirekt | edk2 + Wireshark Schema-Abgleich |

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1, Kampagnenartefakte | erfüllt |
| 2 | alle Primärquellen auf immutable SHA (pfadspezifisch wo nötig) | erfüllt |
| 3 | TinyUSB Hook-Karte: CBW-Empfang, CSW-Send, Control, NEED_RESET | erfüllt |
| 4 | usbsnoop: SETUP + BOT CBW/CSW Decode belegt; Lizenz `UNKNOWN` | erfüllt |
| 5 | Adafruit: Callback-Muster ohne CBW-Sicht; ESP32-Beispiel notiert | erfüllt |
| 6 | edk2/Wireshark Schema-Abgleich ohne neues Sheet | erfüllt |
| 7 | NBT / physische Paketebene / Transparenz weiter `UNKNOWN` | erfüllt |
| 8 | C10–C13; kein paralleles Technology Sheet | erfüllt |

## Decision Trace

Desk-Kampagne mit Go/No-Go für den nächsten Device-Logger-Entwurf (**C10**).

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|-----------------|
| Logger an TinyUSB `mscd_xfer_cb` / `send_csw` / Control hängen, nicht nur an App-`onRead` | Sind Tag, CDB und Residue im Stack vorhanden, bevor App-Callbacks laufen? | `EVID-USBBOT-INST-2026-10-14-001`–`004` | Ja — Hook nach CBW-`memcpy` und in `send_csw`; App-Layer unzureichend | `DISCOVERED DURING TEST` |
| usbsnoop als Lab-Host-Validate (PC), nicht als Fahrzeug-Capture | Kann Host BOT + SETUP ohne Hardware-Analyzer dekodieren? | `EVID-USBBOT-INST-2026-10-14-005`–`007` | Ja für kontrollierten Linux-Host; Lizenz/Fahrzeug offen | `DISCOVERED DURING TEST` |
| Kein neues `usb-bot-protocol`-Sheet | Unterscheidet sich der Contract von `usb-msc`? | Sheet-Reuse + `008`/`009` | Nein — Structs/Hooks wachsen in `usb-msc` A | `KNOWN BEFORE TEST` |
| Physische Paketebene out-of-scope lassen | Braucht die nächste Implementierung DATA0/1? | Scope + Vor-Kampagne | Nein — erst BOT-Semantik | `KNOWN BEFORE TEST` |

## Engineering Review Checks

Zielcode eines künftigen Device-BOT-Loggers (**C11**).

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|-----------------|
| `001`–`003` | Event `bot_cbw`: Tag, Lun, `total_bytes`, `dir`, `cmd_len`, `command[0..cmd_len)` atomar nach gültigem CBW | `DISCOVERED DURING TEST` |
| `002` | Event `bot_csw`: Tag, `data_residue`, Status; Residue = `total_bytes - xferred_len` | `DISCOVERED DURING TEST` |
| `003`–`004` | BOT Reset (`0xFF`), Get Max LUN (`0xFE`), Clear-Halt und `MSC_STAGE_NEED_RESET` als Epoch | `DISCOVERED DURING TEST` |
| `004`, Vor-`008` | Sense Key/ASC/ASCQ mit auslösendem Command-Tag; `tud_msc_set_sense` | `DISCOVERED DURING TEST` |
| `010` | Adafruit/`onRead` nie als alleinige CBW-Quelle | `DISCOVERED DURING TEST` |
| `005`–`007` | Lab: Host-Decode (usbsnoop) gegen Device-Events; Tag-Korrelation | `DISCOVERED DURING TEST` |
| Vor-`013` | Hostlabel erzwingen; PC ≠ NBT | `KNOWN BEFORE TEST` |

## Kill-Kriterien

Präregistriert für einen **künftigen** Instrumentierungs-Lab (**C12**); hier
kein Messlauf.

**Hypothese:** Ein an TinyUSB-Hooks angebundener Logger liefert tag-konsistente
`bot_cbw`/`bot_csw`-Events, die ein Host-Sniffer am Kontrollhost bestätigt.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | CBW-Tag und CSW-Tag lassen sich Device↔Host nicht zuordnen | präregistriert — kein Messlauf |
| 2 | Logger sieht nur Callback-Chunks, keine CBW-CDB | präregistriert — kein Messlauf |
| 3 | Control-Reset/Clear-Halt fehlt in Device- oder Host-Spur | präregistriert — kein Messlauf |
| 4 | Drop-/Overflow oder Ringverlust | präregistriert — kein Messlauf |
| 5 | Beobachter ändert Enumeration/Commandfolge außerhalb Budget | präregistriert — Budget fehlt |
| 6 | PC-/ESP-Lab als NBT-Verhalten verkauft | permanenter Integritäts-Kill |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| BOT-Command-Beobachtung | [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md) |
| Trace-Korrelation | [`msc-trace-correlation`](../../methods/msc-trace-correlation.md) |

## Bezug Inventar

- Inventar: [`usb-bot-observation/INVENTORY.md`](../../projects/usb-bot-observation/INVENTORY.md)
- Application: [`applications/usb-msc.md`](../../projects/usb-bot-observation/applications/usb-msc.md)
- Sheet: [`technologies/usb-msc/SHEET.md`](../../technologies/usb-msc/SHEET.md)
- Vorläufer: [`usb-bot-observation-2026-foreign`](../usb-bot-observation-2026-foreign/)

## Ergebnisse

- [`evidence.md`](evidence.md) — `EVID-USBBOT-INST-2026-10-14-*`
- Hook-Karte und Schema-Abgleich → Sheet-/Application-Wachstum
- Nächster Engineering-Schritt: Device-Ring an TinyUSB-Hooks (Follow-on)

## Knowledge Feedback

**C13:** n/a für Lab/Field — Desk-only.

| Ergebnis | Evidence-ID | Zurück in |
|----------|-------------|-----------|
| Hook-/Schema-Desk | `EVID-USBBOT-INST-2026-10-14-001`–`011` | [`usb-msc` Application](../../projects/usb-bot-observation/applications/usb-msc.md) · Sheet A |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 präregistrierte Kill-Kriterien | PASS; Status offen (kein Messlauf) |
| C13 Knowledge Feedback | n/a dokumentiert |

## Lessons → Transfer

- Echte `bot_cbw`/`bot_csw`-Events sitzen im Class Driver, nicht in Adafruit-`onRead`.
- Host-eBPF (usbsnoop) ersetzt keinen Hardware-Analyzer und keinen NBT-Lauf.
- Struct-Felder TinyUSB ↔ edk2 ↔ Wireshark decken sich; Schema braucht kein Extra-Sheet.
- Lizenzlücken (`usbsnoop`) erzwingen Research-Kontrast, keine Code-Übernahme.

## Offene Punkte nach Abschluss

- Implementierung Device-Logger + kontrollierter Lab gegen usbsnoop (Lizenz klären)
- Transparenz-Baseline / Drop-Zähler
- NBT-CDB/Sense/Timing weiter `UNKNOWN`
