# Instrumentierungsbericht — A0-Enabler (2026-10-26)

```yaml
campaign: esp32-rf-sensing-2026-desk
scope: A0 instrumentation only
status: suspended
rfmonitor_touched: false
c1_executed: false
commit: none
note: "Kein CSI-Projektentscheid; siehe ARTIFACT-INSTRUMENT-2026-10-26.md"
```

## Reuse-Check

| Quelle | Nutzung |
|--------|---------|
| `espressif/esp-csi` `examples/get-started/csi_recv` | **CSI-Init-Muster** übernommen: `wifi_csi_config_t` (S3 Non-HE), CB, `esp_wifi_set_csi(true)`; **`esp_wifi_set_promiscuous(true)` technisch nötig** für CSI (kein PCAP-Produkt) |
| esp-csi ESP-NOW TX/RX Paar | **nicht** geklont — D1-Pfad = SoftAP+UDP Profil N (PHASE3) |
| `esp32.rfmonitor` | **unverändert** |

## Gebaut

| Komponente | Pfad | Build |
|------------|------|-------|
| S3 CSI-RAW | `projects/esp32-rf-sensing/instrument/s3-csi-raw/` | **SUCCESS** (pio) |
| D1 Traffic N | `projects/esp32-rf-sensing/instrument/d1-traffic-n/` | **SUCCESS** (pio) |
| Host Capture | `projects/esp32-rf-sensing/instrument/host/capture_session.py` | lauffähig (pyserial) |

## Flash-Verifikation

| Gerät | Port | Ergebnis |
|-------|------|----------|
| ESP32-S3 | `/dev/ttyACM0` | **Flash OK** → Banner `INSTR s3-csi-raw boot`, Join `RFSENSE_N` |
| D1 Mini | — | **nicht am Host** → FW gebaut, **nicht geflasht** |

## A0-Smoke (nach Instrument)

Session: `instrument/sessions/a0_smoke_20261026/`

| Check | Ergebnis |
|-------|----------|
| S3 startet | **PASS** |
| Session-Dateien erzeugt | **PASS** (`session.yaml`, `csi_raw.csv`, `session_stats.json`) |
| CSI-RAW / CB | **FAIL** — `n_samples=0` |
| Device-/Host-Zeit / seq | **FAIL** — kein Sample |
| D1 Profil-N Traffic | **FAIL** — kein zweites Serial; AP `RFSENSE_N` fehlt |
| S3 Log | `INSTR_ERR wifi_connect_timeout` |

**A0 = FAIL** (Instrumentierungsblocker, nicht Messhypothese).

## Konkreter Blocker

1. **D1 Mini physisch anschließen** (zweites USB-Serial).
2. `d1-traffic-n` flashen (`pio run -t upload --upload-port <D1>`).
3. Bestätigen: D1 loggt `INSTR_READY` / `TX_COUNT,...`; S3 erreicht `INSTR_READY`.
4. Host-Capture erneut → erst bei `n_samples>0` A0 PASS.

## Nicht gebaut (bewusst)

Motion/Presence · Feature-Pipeline · ML · Promiscuous-PCAP-Produkt · rfmonitor-Änderung · C1/C2-Logik
