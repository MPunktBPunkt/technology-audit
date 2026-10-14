# Evidence — esp32-s3-usb-wifi-coexistence-2026

Desk 2026-10-14 · **standard_version 0.7.1** · Profile `lab-tool` · keine
Builds, keine Power-/RF-Messung, keine Root-Cause für hu-probe 0.2.15.

## Quellen-Snapshots

| Repository / Artefakt | SHA / Pin | Vertiefter Pfad | Lizenz / Hinweis |
|----------------------|-----------|-----------------|------------------|
| https://github.com/espressif/esp-idf | `ab95e70748f2eddac6f87217b0cf62533684a6ba` (master HEAD Desk) | Issues #7957/#8241/#15079/#12185; `components/esp_wifi/Kconfig`; `components/esp_phy/Kconfig` + `phy_init.c`; Docs USB-OTG-Console, performance/speed | Apache-2.0 |
| esp-idf tag `v4.4.5` | `29bb1d7d4328c41921df1368a7873c209b0f0893` | Fix-Kontext #8241 Backports; speed.rst Built-In Priorities | Apache-2.0 |
| Fix-Commit USB↔PHY S3 | `65f3bf4a8a21f6ef51649c3202ca282e9b04d124` | `esp_phy: fix esp32s3 phy work with USB-OTG issue` (#7957) | Apache-2.0 |
| https://github.com/espressif/esp-usb | `c40b86dc3a3e760b3dfdc28ec83010b9799a7e88` | nur `device/esp_tinyusb/` (`tinyusb_task.c`, `tinyusb.h`) | Apache-2.0 (SPDX; GitHub `NOASSERTION`) |
| https://github.com/espressif/arduino-esp32 tag `2.0.11` | `ae9dae4a6c063d95786d95b6770b70693e132a7d` | Kontrast-Upstream | LGPL-2.1-or-later |
| PlatformIO local package (hu-probe Pin) | `framework-arduinoespressif32` **3.20011.230801** (= Arduino-ESP32 **2.0.11**, IDF-Header **4.4.5**) | `cores/esp32/esp32-hal-tinyusb.c`, `USB.cpp`, `main.cpp`; `tools/sdk/esp32s3/*/include/sdkconfig.h`; `esp_task.h` | lokal installiert; entspricht Tag 2.0.11 |
| https://github.com/espressif/esp-faq | `d8a806e7887ed417ad73e34b27b200fde263d22b` | `docs/en/software-framework/coexistence.rst` | Abgrenzung WiFi↔BT |
| https://github.com/espressif/esp-iot-solution | `4962410c80a51cd5822da1d8d2041eb4285265f1` | `examples/usb/device/usb_dongle/` | Referenz „gleichzeitig möglich“ |
| hu-probe (Lokal, Kontext) | FW **0.2.15** · `platform = espressif32@6.4.0` | nur Stack-Pin / Symptom-Kontext — **kein** Ursachenclaim | eigenes Instrument |

**Hinweis:** esp-usb Device-SHA identisch zur Control-Kampagne
[`usb-control-stall-recovery-2026`](../usb-control-stall-recovery-2026/). Arduino-Pfad
von hu-probe nutzt **nicht** den aktuellen `esp-usb` Task-API-Pfad, sondern
`esp32-hal-tinyusb.c` im Arduino-Core 2.0.11.

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-USBWIFI-2026-10-14-001` | ESP32-S3: nach `esp_wifi_start()` konnte TinyUSB Device sterben (Host Enum-Fehler −71). Fix: `65f3bf4…` („esp32s3 phy work with USB-OTG“); Reporter bestätigt nach Update. | `FACT` (Issue+Commit) | [#7957](https://github.com/espressif/esp-idf/issues/7957) |
| `EVID-USBWIFI-2026-10-14-002` | S3: `esp_wifi_start` stoppte USB (CircuitPython). Log zeigt `wifi driver task … prio:23 … core=0`. Ursache/Fix-Schiene: `ESP_PHY_ENABLE_USB` / Kconfig-Dependency-Fehler in v4.4-Backport; behoben (u. a. `bf523af…`). | `FACT` (Issue+Log+Fix) | [#8241](https://github.com/espressif/esp-idf/issues/8241) |
| `EVID-USBWIFI-2026-10-14-003` | S3 USB-**Host** CDC-ACM + WiFi: ohne Menüoption „Keep USB PHY enabled when initializing WiFi“ kein Host-Betrieb; mit Option ok. **Host-Modus**, nicht Device-MSC — Chip-/Pfad-Korrelation, kein Transfer auf Device-Sonde. | `FACT` (Issue) / Scope-Grenze | [#15079](https://github.com/espressif/esp-idf/issues/15079) |
| `EVID-USBWIFI-2026-10-14-004` | Espressif: `phy_bbpll_en_usb()` ist Workaround für WiFi↔USB-Interferenz auf **S3 und C3** (nicht S2). Bei `CONFIG_ESP_PHY_ENABLE_USB` ruft `esp_phy_load_cal_and_init` `phy_bbpll_en_usb(true)` auf. | `FACT` | [#12185](https://github.com/espressif/esp-idf/issues/12185); `phy_init.c` @ `ab95e707` ~945–946 |
| `EVID-USBWIFI-2026-10-14-005` | Kconfig `ESP_PHY_ENABLE_USB`: auf betroffenen Targets deaktiviert PHY-Init sonst USB-PHY für bessere WiFi-Performance; Option hält USB-PHY an. Disable → „USB PHY cannot be used while WiFi is enabled“. Default u. a. `y` für S3/C3. | `FACT` | `components/esp_phy/Kconfig` @ `ab95e707` |
| `EVID-USBWIFI-2026-10-14-006` | S3 Docs: interner USB-PHY ist standardmäßig an **USB Serial/JTAG** gebunden; USB-OTG braucht externen PHY **oder** eFuse `USB_PHY_SEL`. OTG und Serial-JTAG teilen die interne PHY-Ressource (Umschaltung). | `FACT` (Doku) | `docs/en/api-guides/usb-otg-console.rst` @ `ab95e707` |
| `EVID-USBWIFI-2026-10-14-007` | WiFi-Task: Default **prio 23**, pinned **Core 0** (`CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_0` / rename `CONFIG_ESP32_WIFI_TASK_CORE_ID`). Dokumentiert in IDF performance/speed (v4.4.5) und Issue-Logs. | `FACT` | speed.rst v4.4.5; `esp_wifi/Kconfig`; sdkconfig Arduino S3 |
| `EVID-USBWIFI-2026-10-14-008` | lwIP `tcpip`: prio **18** (`ESP_TASK_TCPIP_PRIO` = `ESP_TASK_PRIO_MAX - 7`, `configMAX_PRIORITIES=25`). Arduino-S3-sdkconfig: Affinity **CPU0**. | `FACT` | `esp_task.h`; `lwipopts.h`; sdkconfig |
| `EVID-USBWIFI-2026-10-14-009` | esp-usb `tinyusb_task.c` @ `c40b86d`: Task via `xTaskCreatePinnedToCore(…, config->priority, …, config->xCoreID)`; `size`/`priority`/`xCoreID` konfigurierbar; Unicore erzwingt `xCoreID==0`. Docs: `tinyusb_task_config_t`. | `FACT` | esp-usb Device-Pfad |
| `EVID-USBWIFI-2026-10-14-010` | **hu-probe-relevanter Arduino-Pfad (2.0.11):** `tinyusb_driver_install` = nur HAL+`tusb_init` (kein Task). Danach `xTaskCreate(usb_device_task, "usbd", 4096, NULL, configMAX_PRIORITIES - 1, NULL)` → prio **24**, **keine** Core-Affinität. `tud_task()` forever. | `FACT` | `esp32-hal-tinyusb.c` ~81–92, 648–718 |
| `EVID-USBWIFI-2026-10-14-011` | Arduino `loopTask`: prio **1**, Core **`CONFIG_ARDUINO_RUNNING_CORE=1`**. `ESPUSB` Event-Loop Default: stack 2048, prio **5**, `tskNO_AFFINITY`. | `FACT` | `main.cpp`; `USB.h`/`USB.cpp`; sdkconfig |
| `EVID-USBWIFI-2026-10-14-012` | Arduino-S3 prebuilt sdkconfig: `CONFIG_ESP_PHY_ENABLE_USB 1`; WiFi Task Core 0; TinyUSB Klassen enabled (MSC/CDC/…). | `FACT` | sdkconfig.h qio_qspi (u. a.) |
| `EVID-USBWIFI-2026-10-14-013` | esp-faq `coexistence.rst`: behandelt **WiFi↔Bluetooth / BLE-Mesh** Software-Coex — **nicht** USB-OTG↔WiFi. | `FACT` (Abgrenzung) | esp-faq @ `d8a806e` |
| `EVID-USBWIFI-2026-10-14-014` | `esp-iot-solution` `usb_dongle`: Beispiel kombiniert TinyUSB Device (NCM/ECM/RNDIS, CDC, …) mit WiFi-Steuerung — zeigt „gleichzeitig vorgesehen“. **Keine** Last-/Bulk-MSC-Starve-Messung in diesem Desk. | `FACT` (Existenz) / Last=`UNKNOWN` | `examples/usb/device/usb_dongle/` @ `4962410` |
| `EVID-USBWIFI-2026-10-14-015` | Arduino Issues (Symptom-Schicht): C3 CDC stirbt bei WiFi (#6264); S2 MSC+CDC instabil (#9138). Andere Chips/Modi — nur Stack-Schicht-Kontrast, keine Root-Cause-Übertragung. | `HYPOTHESIS` / Kontrast | arduino-esp32 #6264, #9138 |
| `EVID-USBWIFI-2026-10-14-016` | hu-probe Pin: `espressif32@6.4.0` + FW 0.2.15; Arduino USB Mode 0 (OTG Device). Lab-Symptom „WiFi-Assoc tot unter OTG/Host-Reads“ ist **Projekt-Kontext**, nicht Desk-Beweis einer IDF-Root-Cause. | `FACT` (Pin) / Symptom außer Scope-Ursache | `firmware/platformio.ini`; Feldnotizen Lokal |

## Task / Core / Prio-Karte (Defaults)

Gültig für **hu-probe Stack-Pin** (Arduino-ESP32 2.0.11 / IDF 4.4.5 Headers /
`configMAX_PRIORITIES=25`), sofern nicht anders gebaut.

| Task / Rolle | Default-Prio | Core / Affinity | Beleg |
|--------------|-------------:|-----------------|-------|
| TinyUSB `usbd` (`tud_task`) | **24** (`MAX-1`) | keine (`xTaskCreate`) | `010` |
| WiFi driver | **23** | **Core 0** | `007`, `002` |
| esp_timer | 22 | Core 0 (Doku) | speed.rst |
| system event loop (default) | 20 | Core 0 (Doku) | speed.rst |
| lwIP `tcpip` | **18** | **Core 0** (Arduino sdkconfig) | `008` |
| Arduino `arduino_usb_events` | **5** | no affinity | `011` |
| Arduino `loopTask` | **1** | **Core 1** | `011` |
| esp-usb TinyUSB (IDF-Komponente, nicht hu-probe-Pfad) | konfigurierbar (Kconfig oft prio 5 / CPU1) | `xCoreID` | `009` — **Kontrast** |

**Lesart (Desk, keine Ursache):** Unter Arduino-Defaults liegt die USB-Device-Task
**über** WiFi (24 > 23). Ob Bulk-/SOF-Last dadurch WiFi verhungern lässt, ist
**`HYPOTHESIS`** — messbar, nicht aus Issues ableitbar.

## Hypothesen-Register (kein FACT)

| ID | Hypothese | Was sie *nicht* behauptet | Diskriminator (Lab) |
|----|-----------|---------------------------|---------------------|
| H1 | USB-Bulk / SOF-ISR-Last lässt WiFi-Task oder RF-Pfad verhungern | „Bulk = WiFi-Tod“ als FACT | CPU-Core-Last + Task-Runtime unter `dd` vs. Idle-OTG |
| H2 | PHY/BBPLL/USB-PHY-Interaktion trotz `ESP_PHY_ENABLE_USB=1` unter Dauerlast | Issue-Fix (#7957/#8241) sei unvollständig für MSC-Bulk | Assoc hält ohne Host-Reads; bricht nur bei Bulk |
| H3 | Versorgung / VBUS-/Brownout unter OTG+TX | Software-Starve | externe 5 V; Reset-Reason; siehe Method Power |
| H4 | App-Emit/TCP-Flush (JSON) allein killt Assoc | gilt nach 0.2.14/15-Mitigationen als unwahrscheinlicher *alleiniger* Faktor | WIFI_OFF während Drain vs. MSC-only Last |
| H5 | RF-Desense durch USB-Kabel/Gehäuse | Task-Prio | Antenne/Abstand; gleicher Soft-Stack |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „USB-Bulk verursacht WiFi-Tod“ als Desk-FACT | `REJECTED` | nur H1; Lab nötig |
| „IDF-Issue #7957/#8241/#15079 = Ursache hu-probe 0.2.15“ | `REJECTED` | andere Symptome/Modi/Versionen; Kill-Kriterium |
| „esp-faq Coex gilt für USB“ | `REJECTED` | `013` |
| „usb_dongle beweist Last-Stabilität“ | `REJECTED` | Existenz ≠ Lastmessung (`014`) |
| „Arduino usbd prio 24 *ist* der Kill“ | `REJECTED` | Default-FACT ja; Kausalität nein |
| Dieses Desk ersetzt Capture-Flush-Architektur | `REJECTED` | Scope |

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| RIOT-ähnliche Starve unter HU-Reads (Auto) | `UNKNOWN` | Feld nach Lab-Diskriminierung |
| SOF-IRQ-Anteil an CPU | `UNKNOWN` | ISR/Trace Lab |
| Exakte TinyUSB-ISR-Bindung Core 0/1 unter Arduino 2.0.11 | `UNKNOWN` | Port/TRM + Runtime |
| Power vs. Starve vs. RF Winner | `UNKNOWN` | Method `usb-wifi-coex-discrimination` |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-10-14 | Desk-Audit Primärquellen; Karte + Messplan; kein Lab |
| früher | Control-Kampagne: USB↔WiFi nur `HYPOTHESIS` (`EVID-USBCTRL-…-009`) — hier vertieft |
