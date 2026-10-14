# Follow-on ideas (aus USB BOT Observation)

Ideen aus dem Desk-Vergleich und der Instrumentierungsquellen-Kampagne; keine
davon ist als funktionierender NBT-Capture belegt.

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [usb-msc]
  new: []
  not_helped:
    - "Kein Fremdrepo liefert ohne eigene Instrumentierung reale NBT-CDBs oder Timing."
    - "usbsnoop ohne erkannte Lizenz — keine ungeprüfte Übernahme."
    - "USB↔WiFi-Issues ersetzen kein Lab an der Sonde."
  process: "Pfadvergleich + BOT- und Control-Hook-Karten; Device-Logger + Timing eigene Arbeit."
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | `usb-msc`; BOT-Stufen, Busy-/Callback-Abgrenzung, Hook-/Schema-/Control-Desk |
| Neu | keine Shared Technology / Method (Method nur erweitert) |
| Nicht geholfen | Repos ersetzen weder Fahrzeug-Capture noch Transparenz-/Timing-Nachweis |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Device-seitiger BOT+Control-Logger | `usb-msc` | Ring: Enum (SET_ADDRESS/CONFIG/mount) + `mscd_xfer_cb` / `send_csw` / NEED_RESET / BOT Reset |
| Kontrollierter Host/Gadget-Prüfstand | `usb-msc` | Host gegen TinyUSB-/Linux-Gadget; usbsnoop als Decode-Gegenprobe (Lizenz klären) |
| Transparenz-Baseline | `usb-msc` | identische Workload mit/ohne Beobachter; Latenz, Retries, Resets, Drops |
| Sense-/Reset-Negativleiter | `usb-msc` | Phase Errors, STALL, BOT Reset mit Tag-Korrelation |
| Timing / S1–S3 | `usb-msc` | eigene Messung — kein Fremd-Audit |
| WiFi-Death unter USB-Last | `usb-msc` | Lab an der Sonde; Issues nur Hypothesenkontrast |
| NBT-Capture-Gate | `usb-msc` | nur wenn Lab Tag-Match + begrenzte Beobachterwirkung |

## Nicht als Idee freigegeben

- USBProxy-legacy ungeprüft im Fahrzeug einschleifen
- TinyUSB-Callbackanzahl als READ(10)-CDB-Länge ausgeben
- aus Linux-/ESP-/libusb-/usbsnoop-Sequenzen ein NBT-Profil ableiten
- usbsnoop-Code ohne Lizenzklärung in Produkt übernehmen
- physische Paketebene (DATA0/1) als nächstes Muss behandeln
