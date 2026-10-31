# Method: USB OTG Loop Baseline

```yaml
slug: usb-otg-loop-baseline
title: USB OTG Loop Baseline (Dual-ESP Host↔Device)
status: active
tags: [usb, esp32s3, lab, throughput, integrity, preregistered]
```

## Zweck

Vor Proxy-/MITM-Claims eine **kabelgebundene** Full-Speed Host↔Device Baseline messen: MSC Integrity/Throughput/RTT und parallel WiFi-TCP Integrity — damit Bottlenecks und False Positives getrennt werden.

## Voraussetzungen

- Zwei ESP32-S3 mit OTG (Host-Env + Device-Env), USB-C Host↔Device
- Lab-IPs / Status-API erreichbar; Repro-Scripts im Instrument-Repo
- Pattern-Generator auf Device und Verify auf Host (gleiche Spec, z. B. `lab_sector_v1`)
- Epistemic: Ergebnis = Stack/BOT Lab, **nicht** Wire-Rate, nicht transparent MITM

## Ablauf

1. **Enum-Sanity:** Host `/api/status` → DUT VID/PID/speed; Device enumeriert.
2. **MSC READ Sweep:** variiere `blocks` × `chunk`; erfasse kB/s + RTT p50/p95/max + `pattern_ok` / fail bytes.
3. **Sustained:** ≥3× volle Media (oder festes Blockbudget) bei Peak-Chunk; 0 fail bytes gefordert.
4. **MSC WRITE (optional):** WRITE + immediate readback; WRITE≪READ erwarten; Cache-Größe dokumentieren.
5. **WiFi TCP parallel:** Integrity both-ways; frame sizes; ack-each vs windowed rates.
6. **False-positive Gate:** bei `pattern_ok=false` zuerst Device multi-LBA Fill / Verify-Bug prüfen — nicht PHY diagnostizieren.
7. **Claim boundary schreiben:** In/Out-of-scope Tabelle; kein MITM-/HU-/L0-Claim aus dieser Method.

## Artefakte

- JSON Campaign dump (timestamped)
- MEASURED Markdown mit Tabellen + Firmware-Versionen beider Nodes
- Optional: Capture timeline markers (`msc_read` / `tcp_bulk`) mit `source` tags

## Pass / Fail

| Kriterium | Pass | Fail |
|-----------|------|------|
| Pattern integrity (clean LBA, chunk≤lab-max) | fail bytes = 0 | fail > 0 nach Fill-Fix |
| Enum | DUT visible, FS | kein Device / HS-only Phone |
| TCP integrity | 0 frame fails | gaps/errors ohne Erklärung |
| Documentation | FW versions + claim boundary | Zahlen ohne Boundary |

## Fallstricke

- Multi-LBA Callback nur mit Base-LBA füllen → Verify-Fail (kein USB-Verlust)
- OTG-Loop mit Proxy-MITM-Wiring verwechseln
- WiFi-Rate als USB-Ceiling lesen
- App-inferred BOT-Decode als Wire verkaufen

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| esp32-usb-analyzer | [`esp32-usb-analyzer-2026-pilot`](../audits/esp32-usb-analyzer-2026-pilot/) · `tools/lab_baseline_campaign.py` |
