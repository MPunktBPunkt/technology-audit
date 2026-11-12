# Method: BT HCI Host Attach (UART H4 → BlueZ)

```yaml
slug: bt-hci-host-attach
title: BT HCI Host Attach (btattach / hciattach an ESP32 H4)
status: active
tags: [bluetooth, hci, bluez, lab, esp-idf]
```

## Zweck

Einen ESP32 (oder kompatiblen) **HCI-Controller** über UART/USB-UART an einen Linux-Host-Stack (BlueZ) anbinden und die Attach-Session reproduzierbar dokumentieren — ohne RF-/Profil-Claims und ohne WiFi/TCP-Brücken-Zahlen zu vermischen.

## Voraussetzungen

- Controller-FW: CONTROLLER_ONLY / Bluedroid off; H4 UART konfiguriert
- Bekannte **Pins, Baud, Flow-Control** (HWFC vs `noflow`)
- Host: BlueZ-Tools (`btattach` und/oder `hciattach`), Rechte auf TTY
- VS HCI auf dem Controller **OFF**, wenn Third-Party-Host (BlueZ)
- Kein paralleler Anspruch „gleicher Pfad wie HCI-over-TCP Analyzer“

## Ablauf

1. **Freeze:** FW-Commit, Chip, UART-Device (`/dev/ttyUSBx` / `/dev/ttySx`), Baud, Flow, Pinmap notieren.
2. **Controller boot:** UHCI/UART bereit, dann Controller enable (BTDM) — Reihenfolge laut FW (z. B. redchenjs: UHCI+UART1 → `esp_bt_controller_enable`).
3. **Attach:**
   - HWFC / modernes BlueZ: `btattach -B <tty> -P h4 -S <baud>` (redchenjs/IDF: oft `921600`)
   - Legacy/`hciattach`-Pfad (dakhnod): `hciattach -s 921600 <tty> any 921600 noflow`
   - Zephyr-Docs-Referenz: `btattach -B … -S 1000000` (+ HWFC); `-R` nur QEMU-Proxy
4. **Sanity:** `hciconfig`/`bluetoothctl` zeigt Adapter; optional `btmon` Session starten.
5. **SCO (optional):** nur wenn FW `SCO_DATA_PATH_HCI` (o. ä.) gesetzt — sonst kein Host-SCO-Claim.
6. **Boundary schreiben:** Evidence = Host↔Controller HCI, nicht Air/PHY.

## Artefakte

| Artefakt | Naming |
|----------|--------|
| Session YAML | `YYYY-MM-DD-hci-attach-<board>.yaml` (tty, baud, flow, pin, commit) |
| `btmon` / btsnoop | `YYYY-MM-DD-hci-attach.pcapng` |
| Reset-Notiz | Host-first vs Controller-first; Tangle beobachtet? |

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Adapter up | `hciX` sichtbar, BD_ADDR lesbar | silent tty / wrong baud |
| Protocol | H4 Frames in `btmon` | Rohmüll / Framing errors |
| Flow | dokumentiertes HWFC oder bewusstes noflow | gemischt ohne Notiz |
| Epistemik | Desk/Lab getrennt; kein TCP-kB/s | Analyzer-WiFi-Zahlen als UART verkauft |

## Fallstricke

- Baud-Mismatch (Zephyr-Doc 1 M vs ESP-Default 921600) → Attach „hängt“.
- `noflow` an HWFC-FW oder umgekehrt → Drop/Reset-Tangle (dakhnod Note).
- VS HCI an → BlueZ versteht Vendor-Events falsch.
- SCO MTU-Tweaks (`hciconfig … sco mtus 255:4`) sind Examples, keine universellen FACTS.
- Reset-Reihenfolge Host↔ESP kann verhaken — als `UNKNOWN` bis Lab.

## Abgrenzung Capture-Pipelines

| Pfad | Sicht | Method / Sheet |
|------|--------|----------------|
| **UART H4 Attach** (diese) | Host↔ESP-Controller | dieses Dokument · `esp-hci-uart-controller` |
| **USB-HCI Observe** (fremder Dongle am S3) | Host↔Dongle am Instrument | `bt-usb-hci-observe-baseline` |
| **HCI snoop / nRF** | Phone/Air | `bt-passive-host-sniff` |
| **HCI-over-TCP + VHCI** | Analyzer WiFi-Pfad | `esp32-bt-analyzer` (nicht hier messen) |

## Beispiel-Einsätze

- Lab-Dongle: redchenjs/IDF Pins @ 921600 + `btattach -P h4`
- USB-UART Stick: dakhnod + `hciattach … noflow` (Flow-Gate beachten)
- Architektur-Kontrast: Zephyr hci_uart Docs (Host/Controller Split)

## Verwandt

- Sheet: `esp-hci-uart-controller`
- Kampagne: `esp32-hci-controller-2026-foreign`
- Kontrast: `projects/esp32-bt-analyzer` · Methods `bt-usb-hci-observe-baseline`, `bt-passive-host-sniff`
