# Evidence — esp32-s3-hw-limits-2026

Desk 2026-10-18 · **standard_version 0.7.1** · Profile `lab-tool` · keine Builds,
kein Lab, kein Fahrzeug.

## Quellen-Snapshots

| Quelle | Pin | Fokus | Lizenz / Hinweis |
|--------|-----|-------|------------------|
| https://github.com/espressif/esp-chip-errata | `b337299ce1313b669c3774e742b2336db5ce09af` | `docs/en/02-errata-summary/esp32s3-errata-summary.rst`, `docs/en/03-errata-description/esp32s3/*`, `shared/*` referenziert | Apache-2.0 |
| HTML Errata S3 | docs.espressif.com …/esp32s3/ (gelesen 2026-10-18) | Summary-Tabelle deckungsgleich mit Repo | — |
| https://github.com/huming2207/jumbo-s3 | `69179d1483a74ab990b23defc9a343753db2fc73` | README PoC 16 MB Octal-PSRAM | GitHub license `null` |
| https://github.com/cyber-murmel/esp-sdr-zephyr | `3214c16a7c9f136414cc5ae9d245ea290c98a6ce` | `doc/hardware-quirks.md` | GPL-3.0 |
| espressif/esp-idf#18640 | Issue (closed, Resolution: Won't Do) | GDMA I2S→AES/SHA | Tracker |
| espressif/esp-idf#18806 | Issue (open) | Octal AP PSRAM / flash fetch | Tracker |
| espressif/arduino-esp32#12782 | Issue (open) | HWCDC connected limbo | Tracker |

Offizielle Begleitdokumente (Errata `resources.rst`, nicht inhaltsgespiegelt):

- ESP32-S3 Datasheet / TRM (Espressif Doc-IDs via Errata-Build)
- [Hardware Design Guidelines S3](https://docs.espressif.com/projects/esp-hardware-design-guidelines/en/latest/esp32s3/index.html) (HTTP 200, 2026-10-18)

## Evidence-Register

| ID | Claim (Kurz) | Status | Quelle |
|----|--------------|--------|--------|
| `EVID-S3HW-2026-10-18-001` | **CACHE-126:** Während Cache-Write-Back kann Zugriff auf dieselbe Cache-Line als Miss behandelt werden → doppelte Einträge / falsche Hits; ggf. Write-Back-Verlust. Betrifft v0.0/v0.1/v0.2. **No fix.** Workaround: Interrupts aus + Cache-Freeze; in IDF v4.4.6+, v5.0.4+, v5.1.1+, v5.2+ automatisch. | `FACT` | `cache-hit-error-during-writeback.rst` @ `b337299` |
| `EVID-S3HW-2026-10-18-002` | **RTC-126:** Nach Light-Sleep können RTC-Register falsch gelesen werden, wenn RTC-Peripherie im Sleep abgeschaltet war. **No fix.** Workaround: RTC-Peripherie nicht power-down; IDF v4.4+ Bypass. | `FACT` | `shared/rtc-reg-read-error-from-light-sleep.rst` |
| `EVID-S3HW-2026-10-18-003` | **ANALOG-160:** BIAS_SLEEP=0 und PD_CUR=1 kann den Chip **dauerhaft zerstören** (ULP/Touch in Light-/Deep-sleep). **No fix.** IDF v4.4.2+/v5.0+ deaktiviert diese Konfiguration. | `FACT` | `analog-power-config-might-damage-chip.rst` |
| `EVID-S3HW-2026-10-18-004` | **LCD-239:** Unzuverlässiges LCD bei bestimmten Clock-Dividern (RGB EQU_SYSCLK / I8080 ahead_cycle≤2). **No fix.** IDF-Bypass v4.4.5+/v5.0.3+/v5.1+. | `FACT` | `lcd-equ-sysclk-issue.rst` |
| `EVID-S3HW-2026-10-18-005` | **USBOTG-4289:** Vor Date Code 2219 / PW vor PW-2022-06-XXXX ist `EFUSE_DIS_USB_OTG_DOWNLOAD_MODE` gesetzt → USB-OTG Download unavailable. Workaround: USB-Serial-JTAG. Teilweise behoben in manchen v0.2-Batches ab Date Code 2219. | `FACT` | `usb-otg-download-func-bug.rst` |
| `EVID-S3HW-2026-10-18-006` | **RMT-176:** Continuous TX Idle-Level nicht durch End-Marker-Level gesteuert. **No fix.** IDF setzt Idle über Register (`RMT_IDLE_OUT_EN`). | `FACT` | `shared/rmt-idle-level-cannot-be-controlled.rst` |
| `EVID-S3HW-2026-10-18-007` | **TOUCH-100:** Rohdaten der ersten zwei `TOUCH_SCAN_DONE_INT` undefined → skip. **No fix.** | `FACT` | `shared/tchsen-scan-done-int-raw-data-undefined.rst` |
| `EVID-S3HW-2026-10-18-008` | **ADC-183:** DIG/DMA-Controller SAR ADC2 kann inoperativ werden. Workaround S3: RTC-Controller für ADC2. **No fix.** | `FACT` | `shared/sar-adc-adc2-not-work.rst` |
| `EVID-S3HW-2026-10-18-009` | `jumbo-s3`: PoC ESP32-S3FN8 + 16 MB APS12808L Octal-PSRAM @ 80 MHz; Boot-Log „Found 16MB PSRAM“ und Warnung „DO NOT USE FOR MASS PRODUCTION! Timing parameters will be updated“. Lizenz am Pin `UNKNOWN`. | `FACT` (README/Log) | jumbo-s3 @ `69179d1` |
| `EVID-S3HW-2026-10-18-010` | Errata-`resources.rst` verweist auf Datasheet, TRM, Hardware Design Guidelines und Advisories als verbindliche Begleitquellen — Limits (Spannung/Timing/Pin) liegen dort, nicht in der Errata-Tabelle allein. | `FACT` | `docs/en/resources.rst` @ `b337299` |
| `EVID-S3HW-2026-10-18-011` | Arduino-ESP32 #12782 (open): HWCDC `connected` bleibt nach ~2 min in Limbo — **Issue-Signal**, kein Eintrag in S3-Errata-Summary. | `FACT` (Issue existiert) / Semantik `HYPOTHESIS` für MSC | arduino-esp32#12782 |
| `EVID-S3HW-2026-10-18-012` | esp-idf#18640 (closed, Won't Do): I2S-GDMA-Aktivität korreliert mit späteren falschen HW-AES/SHA; Reporter-Root-Cause = unvollständiger `gdma_reset_channel` (Driver), **nicht** Errata-Tabelle. PR #19125 erwähnt Reset crypto GDMA TX. | `FACT` (Tracker) | esp-idf#18640 / #19125 |
| `EVID-S3HW-2026-10-18-013` | esp-idf#18806 (open): Octal AP PSRAM auf S3 rev v0.2 — Array-Zugriff korreliert mit Flash-Instruction-Fetch-Korruption (RTCWDT / IllegalInstruction) über mehrere IDF-Versionen. | `FACT` (Issue) / Ursache `UNKNOWN` | esp-idf#18806 |
| `EVID-S3HW-2026-10-18-014` | `esp-sdr-zephyr` `hardware-quirks.md`: S3 Capture-Engine belegt 64 KiB SRAM-Banks exklusiv; PSRAM atomics nicht SMP-sicher ohne Emulation; Flash-Zugriff von PSRAM-Stack hängt; USB OTG braucht frühe `RTC_CNTL_SW_*_USB_PHY_SEL`. SDR-spezifisch — Transfer nur als Memory/USB-PHY-Kontrast. | `FACT` (Doku am Pin) | `doc/hardware-quirks.md` @ `3214c16` |
| `EVID-S3HW-2026-10-18-015` | S3-Errata-Summary enthält genau die acht IDs CACHE-126, RTC-126, ANALOG-160, LCD-239, USBOTG-4289, RMT-176, TOUCH-100, ADC-183 — kein SPI-Bitlängen- und kein „USB Light-Sleep Freeze“-Erratum. | `FACT` (Negativ) | `esp32s3-errata-summary.rst` + HTML Summary |

## Claim-Grenzen

| Nicht zulässige Ableitung | Status | Begründung |
|---------------------------|--------|------------|
| „USBOTG-4289 = USB-MSC Bulk bricht im Feld“ | `REJECTED` | nur Download/eFuse (`005`) |
| „Light-Sleep + USB Freeze ist Silicon-Errata“ | `REJECTED` | nicht in Summary (`015`); Issues ≠ Errata |
| „GDMA-AES = Silicon-Erratum“ | `REJECTED` | Tracker Won't Do / Driver-Hypothese (`012`) |
| „16 MB PSRAM offiziell supported“ | `REJECTED` | jumbo PoC + Timing-Warnung (`009`) |
| „SDR quirks erklären MessCapture-Drops“ | `REJECTED` | andere Engine (`014`) |
| „SPI 1/9/17/25/33 Bit = S3-Errata“ | `REJECTED` / `UNKNOWN` | nicht in Summary (`015`); kein klarer Issue-Pin in diesem Lauf |

## PiDrive / Storm-Capture Relevanz (Desk)

| Thema | Gate | Evidence |
|-------|------|----------|
| Lange Sessions ohne Sleep | ANALOG-160 + RTC-126 | `002`, `003` |
| USB-OTG Device aktiv | Download-Errata ≠ Bulk; Coex separat | `005` + Coex-Audit |
| Dual-Core + Cache | CACHE-126 / IDF-Version | `001` |
| PSRAM für große Buffer | #18806 beobachten; DMA eher internal | `013`, `014` |
| WiFi+USB | Sheet `esp32-s3-usb-wifi-coex` | Reuse |

## Offene Claims

| Claim | Status | Nötige Evidence |
|-------|--------|-----------------|
| Light-Sleep unter USB-MSC zerstört Session | `UNKNOWN` | Lab (Coex-Method) |
| Octal-PSRAM in produktiver PiDrive-FW | `UNKNOWN` | Build-Config + #18806 Repro |
| Modul Date Code der Feldgeräte | `UNKNOWN` | Hardware-Inventar |

## Wissens-Chronik

| Zeitpunkt | Label |
|-----------|-------|
| Während Desk | Volle S3-Errata-Tabelle + Priorisierung USB/Cache/Sleep |
| Während Desk | Community-Claims ohne Errata-Pin als Signal markiert |
