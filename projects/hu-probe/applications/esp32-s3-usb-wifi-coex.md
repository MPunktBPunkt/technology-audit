# Project Application: esp32-s3-usb-wifi-coex in hu-probe

```yaml
project_id: hu-probe
tech_slug: esp32-s3-usb-wifi-coex
status: active
sheet: ../../../technologies/esp32-s3-usb-wifi-coex/SHEET.md
audit: ../../../audits/esp32-s3-usb-wifi-coexistence-2026/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R1
  reusability: W2
```

## Rolle im Projekt

Die Sonde streamt MSC-Host-Events per **WiFi/TCP**, während sie gleichzeitig als
**USB-OTG MSC Device** am HU-Host hängt. Unter Host-Enum/Reads stirbt die
WiFi-Datenebene oft (Zombie-Assoc möglich). **Offline-Capture** (WiFi aus) ist der
Mess-Workaround. PSRAM verbessert Heap, **heilt Coex nicht**.

## Architektur / Datenfluss

```text
HU Host ──USB MSC Bulk──► TinyUSB usbd (Arduino)
                              │
                              ├─ EventBus / Ring (Slots in PSRAM)
                              ├─ coex-hold / soft-detach / zombie-restart (0.2.37+)
                              └─ TcpStreamer ──WiFi STA──► Collector
                                   (oder WIFI_OFF während ram_offline)
```

## Relevante Pfade (Ursprungsrepo)

| Pfad | Rolle |
|------|-------|
| `firmware/platformio.ini` | `espressif32@6.4.0`, `ARDUINO_USB_MODE=0`, PSRAM |
| `firmware/src/app/App.cpp` | `superviseWifi`, coex-hold |
| `docs/feld/2026-10-14-wifi-otg-0.2.15.md` | frühes Lab-Symptom |
| `docs/feld/2026-10-19-lab-wifi-otg-coex-freeze.md` | Recovery 0.2.32–0.2.39 |

## Konfiguration und Parameter

| Parameter | Wert (Pin) | Status |
|-----------|------------|--------|
| Platform | `espressif32@6.4.0` | `FACT` |
| USB Mode | OTG Device (`ARDUINO_USB_MODE=0`) | `FACT` |
| TinyUSB `usbd` / WiFi prio | 24 / 23 | `FACT` Desk |
| PSRAM | aktiv N8R2; Ring+Capture | `MEASURED` — **≠ Coex-Fix** |
| Lab Recovery 0.2.37–0.2.39 | Stall-Gate, Zombie-Clock, Lab-Detach | `MEASURED` Lab PASS |
| WiFi-Death Root-Cause | — | `UNKNOWN` |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Lab: OTG Enum/Reads → WiFi-Datenebene tot | Feld/Lab-Notizen | Projekt-`FACT` |
| PSRAM heilt Coex | `EVID-HUPROBE-2026-10-21-015` | `REJECTED` |
| Desk: IDF erklärt Ursache allein | — | `REJECTED` |

## Offene Fragen

- Lab-Diskriminierung Power vs. Starve vs. RF ([`usb-wifi-coex-discrimination`](../../../methods/usb-wifi-coex-discrimination.md))
- Feld-HU: gleicher Kill unter tcp_live Dauerlast?
