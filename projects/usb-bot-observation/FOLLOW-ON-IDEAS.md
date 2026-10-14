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
  process: "Pfadvergleich + Hook-Karte; Device-Logger als nächster Engineering-Schritt."
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | `usb-msc`; BOT-Stufen, Busy-/Callback-Abgrenzung, Hook-/Schema-Desk |
| Neu | keine Shared Technology / Method (Method nur erweitert) |
| Nicht geholfen | Repos ersetzen weder Fahrzeug-Capture noch Transparenznachweis |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Device-seitiger BOT-Logger | `usb-msc` | Ring an TinyUSB `mscd_xfer_cb` / `send_csw` / Control: Tag, CDB, Residue, Status, Epoch |
| Kontrollierter Host/Gadget-Prüfstand | `usb-msc` | Host gegen TinyUSB-/Linux-Gadget; usbsnoop als Decode-Gegenprobe (Lizenz klären) |
| Transparenz-Baseline | `usb-msc` | identische Workload mit/ohne Beobachter; Latenz, Retries, Resets, Drops |
| Sense-/Reset-Negativleiter | `usb-msc` | Phase Errors, STALL, BOT Reset mit Tag-Korrelation |
| NBT-Capture-Gate | `usb-msc` | nur wenn Lab Tag-Match + begrenzte Beobachterwirkung |

## Nicht als Idee freigegeben

- USBProxy-legacy ungeprüft im Fahrzeug einschleifen
- TinyUSB-Callbackanzahl als READ(10)-CDB-Länge ausgeben
- aus Linux-/ESP-/libusb-/usbsnoop-Sequenzen ein NBT-Profil ableiten
- usbsnoop-Code ohne Lizenzklärung in Produkt übernehmen
- physische Paketebene (DATA0/1) als nächstes Muss behandeln
