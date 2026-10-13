# Evidence — usb-bot-observation-2026-foreign

Desk 2026-10-13 · **standard_version 0.7.1** · Profile `lab-tool` · keine
Builds, keine USB-Hardware, kein NBT-Capture.

## Quellen-Snapshots

| Repository | SHA | Vertiefter Pfad |
|------------|-----|-----------------|
| https://github.com/felipebalbi/usb-tools | `08d4f3bc10bacde31484c945a9679ef38b844a77` | `README.md`, `src/msc.c`, `src/msc.sh` |
| https://github.com/usb-tools/USBProxy-legacy | `30c4c14150d8c33f9438b32efeb600ed1bcdb441` | `README.md`, `src/Plugins/Filters/PacketFilter_MassStorage.cpp` |
| https://github.com/torvalds/linux | `2c0f5ca48674a5b5f9fa4a9c3325aa48053af0bc` | nur `drivers/usb/gadget/function/f_mass_storage.c` |
| https://github.com/espressif/esp-usb | `f3408e8cfc0ca99bf8686a4acfd9d3de7522df81` | nur `host/class/msc/usb_host_msc/` |
| https://github.com/hathach/tinyusb | `3024dd2e31bc7d6dd27b708ad57f880a8d7f85ac` | nur `src/class/msc/` |
| https://github.com/ookaay/PartitionSchemeDetector → https://github.com/treblist/PartitionSchemeDetector | `63c8669dd0e59b91b7852e3111479282ca7b93cd` | `README.md`, `app.cpp` |
| https://github.com/schumilo/vUSBf | `bc1fb14551bbc97459cc3e2c36e337ad1060b06b` | `README.md`, Replay-/VM-Gerüst |

Pfadspezifische Snapshots sind keine Aussage über den vollständigen Linux-,
ESP-USB- oder TinyUSB-Upstream.

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBBOT-2026-10-13-001` | `usb-tools` testet ein Linux-Blockdevice mit variablen Read-/Write-, Scatter/Gather- und Blockgrößen und wurde für `g_mass_storage` geschrieben; dieser Pfad liefert Workload/Throughput, aber im geprüften Code keine CBW-/CDB-/CSW-Sicht. | `FACT` | `usb-tools` README, `src/msc.c`, `src/msc.sh` |
| `EVID-USBBOT-2026-10-13-002` | USBProxy-MassStorage-Filter erkennt 31-Byte `USBC`-CBWs und 13-Byte `USBS`-CSWs, dekodiert READ(10)/WRITE(10)-LBA und Blockzahl und führt einen Zustandsautomaten COMMAND/READ/WRITE/STATUS. | `FACT` | `PacketFilter_MassStorage.cpp` |
| `EVID-USBBOT-2026-10-13-003` | Derselbe Filter nimmt Daten heuristisch bei `wLength > 64` an, cached feste 512-Byte-Blöcke; das README nennt den Projektstand Alpha, potenziell nicht funktional bzw. nicht kompilierbar | `FACT` | USBProxy README, Filter |
| `EVID-USBBOT-2026-10-13-004` | Linux `f_mass_storage` validiert CBW-Länge/Signatur, CDB-Länge und Flags, kopiert CDB/Tag/DataTransferLength, dispatcht u. a. READ(10), REQUEST SENSE und START STOP und erzwingt bei ungültigem CBW Reset-Recovery-Verhalten. | `FACT` | Linux `f_mass_storage.c`: `received_cbw`, `do_scsi_command`, Exception-/Resetpfad |
| `EVID-USBBOT-2026-10-13-005` | `esp-usb` modelliert BOT explizit als Command-, optionale Data- und Statusphase; CSW-Signatur, Tag, Residue und Status werden geprüft. Bei STALL im Statuspfad folgt Clear-Feature, erneutes CSW-Lesen und nötigenfalls Reset Recovery. | `FACT` | `msc_scsi_bot.c`: `bot_execute_command`, `check_csw` |
| `EVID-USBBOT-2026-10-13-006` | `esp-usb` READ(10) kodiert 32-Bit-LBA und 16-Bit-Sektorzahl im CDB und setzt die CBW-Datenlänge auf `num_sectors * sector_size`; bei Fehler wird REQUEST SENSE ausgelöst. Das ist ein ESP-Host-Kontrast, kein NBT-Profil. | `FACT` | `msc_scsi_bot.c`: `scsi_cmd_read10`, `scsi_cmd_sense` |
| `EVID-USBBOT-2026-10-13-007` | TinyUSB trennt CBW Command-, Data-, Status- und Status-Sent-Stages. Für READ(10) begrenzt `CFG_TUD_MSC_EP_BUFSIZE` jeden Callback-Chunk, während `cbw.total_bytes` und `xferred_len` die gesamte Datenphase halten. Callbackgröße ≠ CDB-Transferlänge. | `FACT` | TinyUSB `msc_device.c`: `mscd_xfer_cb`, `proc_read10_cmd` |
| `EVID-USBBOT-2026-10-13-008` | TinyUSB verlangt bei ungültigem CBW Reset Recovery, verarbeitet den BOT-Class-Reset separat und führt Sense Key/ASC/ASCQ; REQUEST SENSE kopiert und löscht danach den gespeicherten Sense-Zustand. | `FACT` | TinyUSB `msc_device.c`: CBW-Validierung, `proc_bot_reset`, `proc_builtin_scsi` |
| `EVID-USBBOT-2026-10-13-009` | TinyUSB `TUD_MSC_RET_BUSY` erzeugt keinen Datenfortschritt und ruft READ(10) später mit gleichen Parametern erneut auf; CSW folgt erst nach abgeschlossener/fehlgeschlagener Datenphase. | `FACT` | TinyUSB `msc_device.h`, `proc_read_io_data`; Reuse [`tinyusb-msc-busy-retry-2026`](../tinyusb-msc-busy-retry-2026/evidence.md) |
| `EVID-USBBOT-2026-10-13-010` | PartitionSchemeDetector konstruiert raw über libusb 31-Byte-CBWs für TEST UNIT READY, READ CAPACITY und einen Ein-Block-READ(10), liest 13-Byte-CSW und führt BOT Reset plus Clear-Halt beider Bulk-Endpunkte aus. | `FACT` | `treblist/PartitionSchemeDetector` `app.cpp` |
| `EVID-USBBOT-2026-10-13-011` | vUSBf ist ein Python-2-/QEMU-/usbredir-basiertes USB-Fuzzing-Gerüst mit exportier- und replaybaren Sequenzen und VM-Monitoring | `FACT` | vUSBf README |
| `EVID-USBBOT-2026-10-13-012` | Elektrische, zeitliche und semantische Transparenz eines Inline-Proxys oder Firmware-Loggers am konkreten NBT-Aufbau ist nicht belegt | `UNKNOWN` | Vergleich `001`–`011`; kein Messartefakt |
| `EVID-USBBOT-2026-10-13-013` | Reale NBT-CDBs, READ(10)-Commandgrenzen, Sense-/Reset-Folgen und Command-/Inaktivitäts-Timing wurden in dieser Kampagne nicht erfasst. | `UNKNOWN` | Desk-only Scope; keine Capture-Datei |
| `EVID-USBBOT-2026-10-13-014` | USBProxy-legacy oder vUSBf sind für einen transparenten Live-Capture am Fahrzeug geeignet | `UNKNOWN` | `003`, `011`, `012`; Build und Transparenzbaseline fehlen |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „4-KiB-Callback = READ(10) über 8 Sektoren“ | `REJECTED` | Callback wird durch EP-Buffer/Stack gechunkt; CDB muss separat erfasst werden (`007`) |
| „Blockdevice-Read = eine BOT-Commandgrenze“ | `REJECTED` | OS-/Block-Layer kann Requests teilen/zusammenführen; CBW/CSW fehlen (`001`) |
| „ESP-/libusb-Sequenz = NBT-Sequenz“ | `REJECTED` | kontrollierter Host ist nur Kontrast (`006`, `010`, `013`) |
| „Inline = transparent“ | `REJECTED` als unbelegte Annahme | Beobachterwirkung nicht gemessen (`003`, `012`) |
| „Sense allein erklärt den auslösenden Command“ | `REJECTED` | Fehler-CSW, nachfolgendes REQUEST SENSE und Reset-Epoch müssen korreliert werden |

## Engineering Review Checks aus Evidence

| Evidence-ID | Review Check |
|-------------|--------------|
| `002`, `004`–`007` | vollständigen CBW einschließlich Tag, CDB-Länge/-Bytes und DataTransferLength loggen |
| `007`, `009` | CDB-Gesamtlänge, kumulierte Datenbytes und Callback-Chunks als drei verschiedene Größen führen |
| `002`, `005` | CSW-Signatur, Tag, Residue und Status gemeinsam validieren |
| `004`, `005`, `008`, `010` | Reset/Clear-Halt als Epoch-Grenze erfassen; keine Tag-Korrelation über Reset hinweg |
| `005`, `006`, `008` | Sense zum unmittelbar auslösenden fehlgeschlagenen Command korrelieren |
| `003`, `011`, `012` | monotone Timestamps, Drop-/Overflow-Zähler und Baseline mit/ohne Beobachter verlangen |

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| NBT nutzt READ(10) mit bestimmter Sektorzahl | `UNKNOWN` | echter CBW/CDB-Capture |
| NBT sendet REQUEST SENSE nach bestimmtem Fehler | `UNKNOWN` | korrelierte CBW/CSW/Sense-Folge |
| NBT führt BOT Reset bei Timeout aus | `UNKNOWN` | Control-Transfer + Bulk-Epoch |
| NBT hat eine bestimmte Command-/Inaktivitätsgrenze | `UNKNOWN` | kontrollierte Timing-Leiter; neue Evidence-ID |
| Device-Logger ist ausreichend transparent | `UNKNOWN` | Baseline, Drop-Zähler, Latenz-/Sequenzvergleich |
| USBProxy-legacy ist praktisch einsetzbar | `UNKNOWN` | Build, Hardwareaufbau, kontrolliertes Lab |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-13 | sieben Quellen auf SHA geprüft; A/B/C-Pfade und Grenzen verdichtet |
| 2026-10-13 | Kampagne geschlossen; keine Lab-/Field-Evidence erzeugt |
