# Herkunft

Dieses Repository entstand aus der Absicht, Wissen aus konkreten Hobbyprojekten (zuerst **PiDrive**) so zu extrahieren, dass es für Folgeprojekte wiederverwendbar bleibt.

## Auslöser

In PiDrive liefen unter anderem zusammen: USB-MSC/SCSI und FAT/LBA-Verhalten, BMW-Headunit-Einlesen, AVRCP/Metadaten, Datenfluss ESP32 ↔ Bridge ↔ Producer, Echtzeit/Buffering, DAB+/SDR, PipeWire, systemd.

Die Frage war: Kann man daraus später etwas herausziehen — und wie analysiert man ein solches Projekt systematisch nach Technologien und deren konkreter Anwendung?

## Quellen

| Quelle | Rolle |
|--------|--------|
| [ChatGPT-Share (Konzept)](https://chatgpt.com/share/6ac2c503-efbc-83ed-a62c-cf7bf797d3c3) | Plan: Audit-Phasen, Kategorien, Trennung Audit vs. Wissensbasis |
| verwandter Share | `https://chatgpt.com/share/6ac2c171-67e4-83eb-ab90-0fdd2422c7f0` |
| [Cursor Cloud Agent](https://cursor.com/agents?selectedBcId=bc-a7ee3a40-c8c7-4816-98fe-d55f7e0ab353) | Erster Scaffold-Versuch; Push auf privates Repo scheiterte an App-Rechten |

## Namenswahl

`technology-audit` betont den **Analyseprozess**. Langfristig kann daraus eine breitere Wissensbasis werden (`technologies/`, `methods/`). PiDrive ist das erste große analysierte Projekt, nicht der Namensinhaber des Repos.

## Was hier bewusst nicht passiert

- Kein Ersatz für die Betriebsdoku in den Ursprungsrepos (`pidrive`, `esp32.pidrive`, …).
- Keine 1:1-Spiegelung aller Feldberichte — nur verdichtetes Technologie- und Anwendungswissen.
