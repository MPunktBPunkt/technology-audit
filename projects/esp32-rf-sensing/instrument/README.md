# Instrument — A0 only (`MV-ESP32-CSI-RAW-v0`)

Minimal stack so A0 smoke can run. **Not** a product. Does **not** touch `esp32.rfmonitor`.

## Reuse

CSI enable pattern adapted from Espressif `esp-csi` `examples/get-started/csi_recv` (config + CB + **promiscuous required for `esp_wifi_set_csi`**). Traffic path is SoftAP+UDP (D1), not ESP-NOW (simpler for D1 Mini / profile N).

## Components

| Dir | Role |
|-----|------|
| `s3-csi-raw/` | ESP32-S3 STA → AP `RFSENSE_N`; CSI I/Q + RX-meta lines |
| `d1-traffic-n/` | ESP32 D1 Mini SoftAP + UDP @ Δt=20 ms (50 pkts/s); `tx_count` |
| `host/capture_session.py` | Session start/stop → `session.yaml` + `csi_raw.csv` + `session_stats.json` |
| `sessions/` | Capture output |

## Fixed link

- SSID `RFSENSE_N` · password `rfsense_n` · channel **6** · UDP port **5000**

## Flash

```bash
# S3 (UART — typically /dev/ttyACM0 on this desk)
cd s3-csi-raw && pio run -t upload --upload-port /dev/ttyACM0

# D1 Mini (plug second USB; adjust port)
cd ../d1-traffic-n && pio run -t upload --upload-port /dev/ttyUSB0
```

## A0 smoke (host)

```bash
# terminals: D1 monitor optional; S3 captured by script
python3 host/capture_session.py \
  --port /dev/ttyACM0 --baud 921600 \
  --duration 15 --profile N \
  --out sessions/a0_smoke
```

Expect: three files under `sessions/a0_smoke/`, `n_samples > 0`, monotone `device_seq` / host gaps reported.
