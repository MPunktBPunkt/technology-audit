# Technology Sheet: ESP PSRAM Heavy Port

```yaml
slug: esp-psram-heavy-port
title: ESP PSRAM Heavy App / Legacy Port
primary: D
tags: [esp-idf, lab-only, fragile, psram]
type: pattern
status: active
seen_in: [esp32-doom, squeezelite-esp32]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/esp32-doom-2026-foreign
```

Nur Ebene **A**. Doom-WAD-Lizenz, Pinouts, Menü-Bugs → Application.  
**Chip-Scope (Pilot):** Classic **ESP32 + PSRAM** (Wrover-Klasse). S3/C-Serie = Transfer-Gate (anderer SPIRAM-/Cache-Stack).

## Kurzfassung

Muster für **große Legacy-C-Ports** auf ESP: PSRAM als **allgemeiner Heap** (SPIRAM malloc), Assets oft in eigener Flash-Partition (mmap), CPU nahe Max-Takt, Grafik über SPI-LCD-Framebuffer. Entscheidend: was in **internal RAM** bleibt (DMA/Framebuffer) vs. was in PSRAM darf (Game-State/Heaps).

## Abgrenzung

- **Ist:** PSRAM-pflichtige schwere App/Port; Heap-/Framebuffer-Platzierung; Asset-Partition; hohe CPU-/Bus-Last.
- **Ist nicht:** Tiny Status-OLED (`ssd1306-oled-ui`); S3-Errata-Karte (`esp32-s3-silicon`); On-Device-LLM/PLE (`mcu-ple-inference`); CSI-Sensing (`wifi-csi-motion`); LMS-Protokoll allein (`lms-squeezelite` — PSRAM-Last teilen, Contract trennen).
- **Grenzt an:** SPI-LCD Treiber; FreeRTOS Task-Stack-Größe; Flash mmap Limits.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| unten | SPIRAM enable + malloc caps | ohne PSRAM = No-Go |
| lateral | Internal RAM für DMA/FB | oft bewusst nicht PSRAM |
| unten | Flash Partition + mmap | große Read-only Assets |
| oben | SPI LCD / Input | Frame Push, Controller |
| parallel | Max CPU freq | Last-Budget |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Ohne PSRAM „reicht schon“ für denselben Port | `REJECTED` | Upstream: needs PSRAM hardware |
| Alles in PSRAM legen inkl. Framebuffer/DMA | `REJECTED` / Gate | Pilot: 320×240 Screenbuf **internal**; LCD Double-Buffer IRAM |
| Classic-Wrover-PoC = S3-Port ohne Gate | `REJECTED` | anderer SPIRAM/Cache/IDF-Pfad |
| Tiny OLED-Sheet deckt Game-Framebuffer ab | `REJECTED` | anderer UI-Contract |
| PSRAM malloc = Errata gelöst | `REJECTED` | Cache-Workarounds / Caps separat prüfen |
| Sound/Save immer dabei | `REJECTED` | PoC kann Features weglassen |

### Projektstart-Checkliste

- [ ] Chip + PSRAM-Größe/Typ (4 MiB ESP-PSRAM32 vs S3 Octal/Quad)
- [ ] Was **muss** internal sein (FB/DMA)?
- [ ] Asset-Partition-Größe vs. Content
- [ ] CPU-Freq + Task-Stack/Core-Pin
- [ ] IDF/Toolchain-Lag bei historischen PoCs
- [ ] Application + `seen_in`; S3 nur mit Remessung

## Transfer

Nützlich für Emulatoren, große C-Engines, Framebuffer-Demos auf ESP+PSRAM. Lessons zu Internal-vs-PSRAM auch für andere Heavy Apps — Silicon-Sheet nicht ersetzen.

## Referenzen

- Pilot: [espressif/esp32-doom](https://github.com/espressif/esp32-doom) (unsupported PoC)
- ESP-IDF SPIRAM / heap caps

## Offene Fragen

- Welche FPS-Budgets bei 240 MHz + SPI LCD realistisch (Lab)?
- Moderne IDF `esp_heap_caps` vs. historisches `pvPortMallocCaps`-API?
