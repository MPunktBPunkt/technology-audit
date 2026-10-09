# Project Application: pump-control-link in esp32.pidrive

```yaml
project_id: esp32-pidrive
tech_slug: pump-control-link
status: active
sheet: ../../../technologies/pump-control-link/SHEET.md
audit: ../../../audits/esp32-pidrive-2026-pilot/
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W2
```

## Rolle im Projekt

**PUMP** verbindet PiDrive (Gehirn) mit dem ESP-Gadget: Menü-Sync (`menu_set`), Play-UID → `activate:`, Live-MP3/ID3-Frames in den MSC-Overlay-Puffer. Bridge: `tools/pump_bridge.py`.

## Architektur / Datenfluss

```text
/tmp/pidrive_menu.json ──▶ pump_bridge (Soft-Paging ≤4)
        │  UART ttyACM*  oder  TCP :9090
        ▼
PumpServer ──line-JSON──▶ MenuStore / play_uid / diag
        ▲
ffmpeg/meta ──0x01 0x55 audio / 0x01 0x56 sticky ID3──▶ StreamBuffer
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `src/core/PumpServer.*` | Framing, hello/menu/audio, TCP |
| `src/core/UartLinkMonitor.*` | UART-Link-State |
| `tools/pump_bridge.py` | Pi-Bridge, Soft-Paging, Cover/APIC |
| `docs/planung/PUMP.md` | Contract-Doku |

## Konfiguration und Parameter

| Thema | Stand | Epistemic |
|-------|-------|-----------|
| UART | 115200 8N1 (Doku) | `FACT` (Doku) |
| TCP | Default Port 9090, SoftAP/STA | `FACT` |
| Soft-Paging | Slots 1–3 Items, Slot 4 `Mehr…` / Home | `FACT` |
| Ops | `play_uid`, `menu_set`, `hello`/`hello_ack`, `audio_start`/`stop`, `ping` | `FACT` |
| Binary | `0x01 0x55` Audio, `0x01 0x56` sticky ID3 ≤12 KiB (Doku) | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Gleiches Framing UART und TCP | `EVID-PUMP-2026-10-09-001` | `FACT` |
| Soft-Paging hält MSC bei 4 Slots | `EVID-PUMP-2026-10-09-002` | `FACT` |

## Abweichungen vom „Lehrbuch“

- `pump:page_*` bleibt ESP-/Bridge-lokal — nicht an PiDrive injizieren.
- play_uid kann bei TCP-Down gequeued und nach `hello` einmalig replayed werden.

## Verwandte

- Sheet: [`pump-control-link`](../../../technologies/pump-control-link/SHEET.md)
- MSC: [`usb-msc`](usb-msc.md)
