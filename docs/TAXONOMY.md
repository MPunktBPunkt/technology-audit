# Taxonomie

Einheitliche Einordnung von Technologien. Primärkategorie = genau eine; Secondary-Tags = beliebig viele.

## Hauptkategorien

| ID | Name | Beispiele |
|----|------|-----------|
| **A** | Empfangstechnologien | DAB+, FM, Airband, SDR, Webradio |
| **B** | Audiotechnologien | PCM, MPEG, ALSA, PipeWire, Bluetooth-Audio |
| **C** | Kommunikationsprotokolle | USB, MSC, SCSI, UART, TCP, Bluetooth, AVRCP, A2DP |
| **D** | Embedded-Technologien | ESP32, FreeRTOS, TinyUSB, DMA, Ringbuffer, Interrupts |
| **E** | Datenformate und Speicher | FAT, LBA, Metadaten, JSON, Binärprotokolle |
| **F** | Systemintegration | Linux, systemd, udev, Netzwerk, Dienste |
| **G** | Steuerung und UI | iDrive, Trigger, WebUI, CLI, AVRCP-Bedienung |
| **H** | Test und Analyse | Tracing, Logging, Replay, Korrelation, Feldtests |
| **I** | Fahrzeug- und Geräteintegration | BMW NBT Evo, USB-Host-Verhalten, Feldbetrieb |
| **J** | Softwarearchitektur | Producer-Consumer, IPC, Zustandsmaschinen, APIs |

## Zwei Arten von Einträgen

Nicht alles ist eine „Technologie“. Im Inventar und in Sheets klar trennen:

| Typ | Beispiel |
|-----|----------|
| Technologie | USB Mass Storage Class |
| Protokoll | USB BOT, SCSI, AVRCP |
| Datenstruktur / Format | FAT32, LBA-Geometrie |
| Implementierung | ESP32-MSC-Firmware |
| Komponente | MSC-Bridge, PipeWire-Graph |
| Anwendung (projektspezifisch) | BMW-NBT-Evo-Medienquelle |
| Methode / Test | Feldtest Q3b, Trace-Korrelation |
| Erkenntnis | Host liest feste LBA-Fenster |

Technology Sheets eignen sich für Technologie/Protokoll/Format/Implementierungsmuster. Projektspezifische Anwendungen und einzelne Feldtests gehören in Applications bzw. Audits/Methods.

## Secondary-Tags (frei, aber konsistent)

Empfohlene Tags (erweiterbar):

`realtime` · `automotive` · `bluetooth-classic` · `usb-device` · `usb-host` · `sdr` · `linux-userspace` · `esp-idf` · `streaming` · `metadata` · `field-verified` · `lab-only` · `fragile`

Schreibweise: `kebab-case`, Plural vermeiden.

## Slug-Beispiele

| Slug | Primary | Typische Secondary |
|------|---------|-------------------|
| `dab-plus` | A | `sdr`, `streaming` |
| `rtl-sdr` | A | `sdr`, `usb-host` |
| `usb-msc` | C | `usb-device`, `automotive` |
| `scsi` | C | `usb-device` |
| `fat` | E | — |
| `bluetooth-a2dp` | C | `bluetooth-classic`, `streaming` |
| `avrcp` | C | `bluetooth-classic`, `metadata` |
| `pipewire` | B | `linux-userspace`, `realtime` |
| `esp32` | D | `esp-idf` |
| `mpris2` | G | `metadata`, `linux-userspace` |
| `systemd` | F | `linux-userspace` |

## Konflikte lösen

1. Primär = wo die Technologie *fachlich zu Hause* ist (AVRCP → C, nicht G).
2. Steuerungsaspekt als Tag oder in der Project Application vertiefen.
3. Neue Hauptkategorie nur nach Eintrag hier — nicht ad hoc in Einzeldateien.
