# Method: USB BOT Command Observation

```yaml
slug: usb-bot-command-observation
title: USB BOT Command Observation
status: active
tags: [usb-msc, bot, scsi, tracing, preregistered]
```

## Zweck

Reale BOT-Commandgrenzen, CDB-Längen, CBW/CSW-Zuordnung, Resets und
Sense-/StartStop-Sequenzen beobachten. Die Methode trennt Stack-Callbacks von
USB-BOT-Kommandos und deckt HU-A10 ab.

## Voraussetzungen

- passiver oder transparenter Capturepfad mit dokumentierter Hardware/
  Software und Zeitbasis
- BOT-Parser für CBW, Data-In/Out und CSW; Rohdaten unverändert aufbewahren
- bekannte Kontroll-Hosts vor Einsatz am Zielhost
- LBA-/Device-Telemetrie zur Korrelation, falls vorhanden
- optional Host-seitiger URB-Sniffer (z. B. eBPF an `usb_submit_urb` /
  `usb_hcd_giveback_urb`) für Lab-Validate — Lizenz und Truncation beachten

## Ablauf

1. Capturepfad an einem Kontrollhost mit INQUIRY, READ CAPACITY, READ10,
   REQUEST SENSE und START STOP UNIT validieren.
2. CBW über Signatur, Tag, Transferlänge, Flags, LUN und CDB-Länge erfassen;
   CDB nur innerhalb der deklarierten Länge dekodieren.
3. Data-Phase und CSW anhand des Tags zuordnen; Residue und Status erhalten.
4. BOT-Reset, Clear-Halt, Disconnect/Re-enumeration und Aborts als getrennte
   Ereignisse markieren. `SET_ADDRESS` ≠ Mount; Mount erst bei
   `SET_CONFIGURATION n`. `MSC_STAGE_NEED_RESET` gilt bis BOT Reset — Clear-Halt
   allein heilt nicht. Ohne VBUS-Sense: Umount bei Replug nicht voraussetzen.
5. Stack-Callbacksegmente mit CBW/CDB/CSW korrelieren. Mehrere Callback-
   Re-Entries dürfen nicht als mehrere READ10 gezählt werden.
6. Device-Logger (falls TinyUSB): an Class-Driver-Hooks nach CBW-Validierung
   und in CSW-Send hängen — nicht nur an App-`onRead`; Enum-Epochs in `usbd.c`
   / `tud_mount_cb`/`tud_umount_cb` mitlogen.
7. Optional: Host-Decode (SETUP + BOT) gegen Device-Events tag-korrelieren.
8. Kontrollsequenz wiederholen; erst danach denselben observe-only-Capture am
   Zielhost auswerten.
9. Timeout- oder Partial-Read-Aussagen nur treffen, wenn Commandgrenzen und
   Zeitbasis eindeutig sind.

## Artefakte

- unveränderter USB-Capture plus Tool-/Hardwareversion
- normalisierte Tabelle: Zeit, CBW-Tag, Opcode, CDB-Länge, LBA, Transfer,
  Data-Bytes, CSW/Residue, Reset/Sense
- Korrelationsnotiz zu Device-Callbacks
- Evidence erst im ausführenden Audit; diese Note vergibt keine ID

## Präregistrierte Gates

| Gate | Pass | Fail | Kill / Stop |
|------|------|------|-------------|
| B1 Kontrollhost | bekannte Sequenz vollständig und tag-konsistent dekodiert | fehlende CBW/CSW oder Tagkonflikt | kein Zielhostclaim |
| B2 Commandgrenze | READ10 und Callback-Re-Entries eindeutig zugeordnet | Grenzen nur geraten | keine Timeout-/Partial-Read-Auswertung |
| B3 Resetklasse | BOT-Reset, Clear-Halt, NEED_RESET und Re-enumeration unterscheidbar; Mount ≠ Address | Ereignisse vermischt | Resetursache `UNKNOWN` |
| B4 Observe-only | Capture verändert Enumeration/Timing nicht erkennbar | Proxy ändert Hostverhalten | Fahrzeuglauf stoppen; passiveren Pfad wählen |

## Fallstricke

- TinyUSB-Callbackgröße ist nicht die CDB-Länge.
- `return 0`-Retries können innerhalb desselben READ10 auftreten.
- Adafruit-/App-MSC-Callbacks exponieren keinen CBW; Offset kann im Wrapper
  verworfen werden.
- USB-Proxy- oder eBPF-Erfolg am PC belegt keine Transparenz am Fahrzeughost.
- Host-Sniffer ohne klare Lizenz sind Research-Kontrast, keine Copy-Paste-Basis.
- Fuzzing, Command-Injection, Flash und Protokolländerung gehören nicht zu
  dieser observe-only-Methode.

## Beispiel-Einsatz

[`pidrive-2026-bmw-hu`](../audits/pidrive-2026-bmw-hu/) — HU-A10 nur bei
Bedarf; präregistriert und derzeit `UNKNOWN`.  
Hook-/Schema-Desk:
[`usb-bot-observation-2026-instrument-sources`](../audits/usb-bot-observation-2026-instrument-sources/).  
Control/Enum/STALL:
[`usb-control-stall-recovery-2026`](../audits/usb-control-stall-recovery-2026/).
