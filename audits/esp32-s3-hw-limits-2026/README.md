# Audit Campaign: esp32-s3-hw-limits-2026

```yaml
id: esp32-s3-hw-limits-2026
project_id: esp32-pidrive
started: 2026-10-18
ended: 2026-10-18
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: esp32-s3-silicon
related_audits:
  - esp32-s3-usb-wifi-coexistence-2026
  - pidrive-2026-storm-capture-tooling
  - usb-control-stall-recovery-2026
upstream_pins:
  - repo: https://github.com/espressif/esp-chip-errata
    commit: b337299ce1313b669c3774e742b2336db5ce09af
  - repo: https://github.com/huming2207/jumbo-s3
    commit: 69179d1483a74ab990b23defc9a343753db2fc73
  - repo: https://github.com/cyber-murmel/esp-sdr-zephyr
    commit: 3214c16a7c9f136414cc5ae9d245ea290c98a6ce
  - docs: "esp-chip-errata HTML ESP32-S3 (latest build referenced 2026-10-18)"
  - issue: "espressif/esp-idf#18640"
  - issue: "espressif/esp-idf#18806"
  - issue: "espressif/arduino-esp32#12782"
reuse_outcomes:
  reused:
    - esp32-s3-usb-wifi-coex
    - usb-msc
  new:
    - esp32-s3-silicon
  not_helped:
    - "Community-Thermik (Zero/SuperMini LDO) — kein pinned Repo-Artefakt in diesem Lauf"
    - "SPI ‚1/9/17/25/33 Bit‘ als Silicon-Erratum — in esp-chip-errata S3-Summary nicht vorhanden; Issue-Suche ohne klaren Pin"
    - "esp-sdr-zephyr quirks als MSC/Storm-Root-Cause — SDR-Capture-Engine, nicht USB-MSC"
  process: "Desk: offizielle S3-Errata vollständig gegen Summary; Fremd-Repos + Issue-Signale epistemisch getrennt; Sheet A nur Silicon/Workaround."
  decisions_touched:
    - errata-first-for-storm-sessions
    - no-light-sleep-with-usb-otg-without-lab
    - analog-160-sleep-config-gate
    - community-psram-gdma-not-sheet-a-without-pin
```

## Ziel

Autoritative **ESP32-S3 Silicon-/Hardware-Limits** (Errata + referenzierte Espressif-Docs)
für den Kontext `esp32.pidrive` / USB-MSC / lange MessCapture-Sessions kartieren —
und Community-/Issue-Signale (USB+Sleep, PSRAM, GDMA) klar von Silicon-FACT trennen.

## Scope

- **Im Scope:** `espressif/esp-chip-errata` S3-Summary + Beschreibungen am Pin;
  Ressourcen-Verweise (Datasheet/TRM/HW-Design-Guidelines); `jumbo-s3` als
  PSRAM-PoC-Grenze; `esp-sdr-zephyr` `doc/hardware-quirks.md` als Memory/USB-PHY-
  Kontrast; ausgewählte IDF/Arduino-Issues als **Signale** (nicht Root-Cause).
- **Nicht im Scope:** Lab-/Feldmessung; FW-Änderung; Root-Cause für Storm/Quiet;
  vollständige Issue-Tracker-Exhaustion; PDF-Spiegelung; Sheet-Claims aus Forums-
  Thermik ohne Beleg.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1 + Kampagne + Evidence | erfüllt |
| 2 | Alle 8 S3-Errata aus Summary mit Revision/Workaround/Fix-Status | erfüllt — `001`–`008` |
| 3 | USB-/Cache-/Sleep-relevante Errata für PiDrive-Kontext priorisiert | erfüllt |
| 4 | Sheet `esp32-s3-silicon` (A) + Application + Inventar | erfüllt |
| 5 | Community/Issue ≠ Silicon-Errata epistemisch getrennt | erfüllt — `010`–`014` |
| 6 | C10–C13 Desk | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Neues Sheet `esp32-s3-silicon` statt nur Coex wachsen | Ist Silicon-Errata generisch über USB↔WiFi hinaus? | Summary `001`–`008` | Ja — Coex bleibt PHY/Task; Silicon = Chip-Limits | `DISCOVERED DURING TEST` |
| Light-Sleep + USB-OTG für Storm-Sessions meiden bis Lab | Belegt Errata USB-Freeze? | `005`, `011`, Coex-Reuse | Errata deckt Download/eFuse + RTC nach Sleep; Freeze = Issue-Signal, kein Sheet-A-FACT | `DISCOVERED DURING TEST` |
| ANALOG-160 als hartes Sleep-Gate | Kann Fehlkonfig Chip zerstören? | `003` | Ja — kein ULP/Touch-Sleep-Experiment ohne IDF-Bypass-Version | `DISCOVERED DURING TEST` |
| GDMA/AES Issue nicht als Silicon-A | Errata oder Driver? | `012` | Issue closed Won't Do; Reporter = Driver; nicht Errata-Tabelle | `DISCOVERED DURING TEST` |
| jumbo-s3 nur PSRAM-Grenze | Offizielles >8 MB? | `009` | PoC + IDF-Timing-Warnung; keine Massenprodukt-Empfehlung | `DISCOVERED DURING TEST` |

## Engineering Review Checks

Zielcode: `esp32.pidrive` / künftige Storm-Sessions (**C11**).

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `001` | IDF ≥ Bypass für CACHE-126 (v4.4.6+/v5.0.4+/v5.1.1+/v5.2+) wenn Write-Back-Pfade aktiv | `DISCOVERED DURING TEST` |
| `003` | Sleep/ULP/Touch: nie BIAS_SLEEP=0∧PD_CUR=1; IDF ≥ v4.4.2+/v5.0 | `DISCOVERED DURING TEST` |
| `005` | Chip Date Code / PW Number prüfen wenn USB-OTG Download benötigt | `DISCOVERED DURING TEST` |
| `002` | Light-Sleep: RTC-Peripherie nicht power-down (IDF ≥ v4.4 Bypass) | `DISCOVERED DURING TEST` |
| `010`–`011` | Kein automatisches Light-Sleep unter aktivem USB-MSC ohne Lab-Baseline | `DISCOVERED DURING TEST` |
| `012` | Hardware-AES/SHA + I2S-GDMA-Sequenzen: Channel-Reuse / Won't-Do beachten | `DISCOVERED DURING TEST` |
| `013` | Octal-PSRAM: Issue #18806 als Beobachtungs-Gate, nicht als Fixed-Errata | `DISCOVERED DURING TEST` |

## Kill-Kriterien

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Kartierung ohne Messlauf. Silicon-Errata sind dokumentierte
Faktenquellen, keine Hypothesentests. Issue-Signale werden nicht als Kill für
HU-Storm umgedeutet.
```

Für künftige Labs: präregistrieren, ob Light-Sleep oder PSRAM-DMA MessCapture
verfälscht — getrennt von Errata-FACT.

## Errata-Kurzkarte (S3, alle Rev. sofern nicht anders)

| ID | Kern | Fix | IDF-Bypass (laut Errata) | PiDrive-Relevanz |
|----|------|-----|--------------------------|------------------|
| CACHE-126 | Cache-Hit-Fehler bei Write-Back | No fix | v4.4.6+ / v5.0.4+ / v5.1.1+ / v5.2+ | Mittel (Dual-Core + Cache) |
| RTC-126 | RTC-Reg nach Light-Sleep falsch | No fix | v4.4+ | Hoch wenn Sleep |
| ANALOG-160 | Chip-Zerstörung Sleep-Analog | No fix | v4.4.2+ / v5.0+ | Hoch (Safety) |
| LCD-239 | LCD Clock-Divider | No fix | v4.4.5+ / v5.0.3+ / v5.1+ | Niedrig (kein LCD) |
| USBOTG-4289 | OTG Download eFuse alt | Teil-Batches v0.2 | USB-Serial-JTAG | Mittel (Flash/Debug) |
| RMT-176 | Idle-Level Continuous TX | No fix | ab Continuous-TX-Support | Niedrig |
| TOUCH-100 | erste Scan-Done-INTs | No fix | Skip first two | Niedrig |
| ADC-183 | SAR ADC2 DIG/DMA | No fix | RTC-Controller für ADC2 | Niedrig |

HTML: https://docs.espressif.com/projects/esp-chip-errata/en/latest/esp32s3/

## Genutzte Methoden / Bezug

| | Pfad |
|--|------|
| Sheet | [`technologies/esp32-s3-silicon/SHEET.md`](../../technologies/esp32-s3-silicon/SHEET.md) |
| Application | [`projects/esp32-pidrive/applications/esp32-s3-silicon.md`](../../projects/esp32-pidrive/applications/esp32-s3-silicon.md) |
| Coex (Reuse) | [`esp32-s3-usb-wifi-coexistence-2026`](../esp32-s3-usb-wifi-coexistence-2026/) |
| Storm-Tooling | [`pidrive-2026-storm-capture-tooling`](../pidrive-2026-storm-capture-tooling/) |

## Knowledge Feedback

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| Desk | `EVID-S3HW-2026-10-18-*` | Sheet A + Application |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact.

## Lessons → Transfer

- **Errata zuerst**, dann Datasheet/TRM/HW-Guidelines, dann Issues.
- USB-MSC Storm-Sessions: Sleep und ANALOG-160 sind härtere Gates als LCD/RMT/Touch.
- Community-USB-Freeze und PSRAM-Korruption bleiben **Signale** bis Lab — nicht Sheet-A.
- `hardware-quirks.md` (SDR) liefert Memory/USB-PHY-Kontrast, keine MSC-Semantik.

## Offene Punkte

- Lab: Light-Sleep aus vs. an unter USB-MSC + WiFi (Coex-Method).
- Feld: Chip-Revision / Date Code der eingesetzten Module dokumentieren.
- PSRAM-Pfad in `esp32.pidrive` (falls Octal): #18806 beobachten.

Evidence: [`evidence.md`](evidence.md).
