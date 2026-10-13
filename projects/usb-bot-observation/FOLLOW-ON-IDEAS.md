# Follow-on ideas (aus USB BOT Observation)

Ideen aus dem Desk-Vergleich; keine davon ist durch diese Kampagne als
funktionierender NBT-Capture belegt.

## Transfer-Nachweis

```yaml
reuse_outcomes:
  reused: [usb-msc]
  new: []
  not_helped:
    - "Kein Fremdrepo liefert ohne eigene Instrumentierung reale NBT-CDBs oder Timing."
  process: "Desk-Vergleich trennt Device-, Inline- und Host-Kontrastpfade."
```

| Kategorie | Einträge |
|-----------|----------|
| Übernommen | `usb-msc`; BOT-Stufen und Busy-/Callback-Abgrenzung |
| Neu | keine Shared Technology / Method |
| Nicht geholfen | Repos ersetzen weder Fahrzeug-Capture noch Transparenznachweis |

## Ideen

| Idee | Baut auf | Kurz |
|------|----------|------|
| Device-seitiger BOT-Logger | `usb-msc` | CBW-Tag, CDB-Bytes, erwartete Datenlänge, CSW-Residue/-Status und Reset-Epoch in einem Ring |
| Kontrollierter Host/Gadget-Prüfstand | `usb-msc` | `esp-usb`/libusb-Host gegen Linux- oder TinyUSB-Gadget; erst ohne NBT |
| Transparenz-Baseline | `usb-msc` | identische Workload mit/ohne Beobachter; Latenz, Retries, Resets und Datenverlust vergleichen |
| Sense-/Reset-Negativleiter | `usb-msc` | definierte Phase Errors, STALL und Reset Recovery mit Tag-Korrelation |
| NBT-Capture-Gate | `usb-msc` | nur starten, wenn Desk-/Lab-Pfad CDB-Grenzen korrekt erhält und Beobachterwirkung begrenzt ist |

## Nicht als Idee freigegeben

- USBProxy-legacy ungeprüft im Fahrzeug einschleifen
- TinyUSB-Callbackanzahl als READ(10)-CDB-Länge ausgeben
- aus Linux-/ESP-/libusb-Sequenzen ein NBT-Profil ableiten
