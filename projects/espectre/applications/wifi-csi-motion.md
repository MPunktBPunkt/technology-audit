# Project Application: wifi-csi-motion in espectre

```yaml
project_id: espectre
tech_slug: wifi-csi-motion
status: active
sheet: ../../../technologies/wifi-csi-motion/SHEET.md
audit: ../../../audits/espectre-2026-foreign/
maturity:
  technology: R1
  implementation: R2
  field_evidence: R0
  reusability: W1
```

## Rolle im Projekt

ESPectre macht aus einem unterstützten ESP32 einen **lokalen Wi-Fi-Motion-Sensor**: CSI messen, Temporal Admission, Lightweight- oder High-Accuracy-Detektor, Motion/Score an ESPHome/MQTT/Matter/HTTP — on-device, optional Roh-CSI nur für Research.

| Repo | Commit | Rolle |
|------|--------|-------|
| [francescopace/espectre](https://github.com/francescopace/espectre) | `5866bff` | SDK + Frontends + Docs |

## Architektur / Datenfluss

```text
Traffic (ping|dns|wifi_raw|external)
  → CSI capture (ESP-IDF runtime)
  → normalize / quality
  → TemporalCsiSampler (≤1 packet / slot @ csi_target_pps)
  → LightweightDetector | HighAccuracyDetector (MLP)
  → motion / score → Frontend (ESPHome | Native MQTT/HTTP | Matter | Micro)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `docs/CSI.md` | Traffic-Quellen, Capture, Compatibility |
| `docs/ALGORITHMS.md` | Detektoren, Timing, Admission |
| `docs/ARCHITECTURE.md` | core / runtime / frontend |
| `src/cpp/core/temporal_csi_sampler.*` | Fixed-grid Admission |
| `src/cpp/core/lightweight_detector.*` | Default statistisch |
| `src/cpp/core/high_accuracy_detector.*` + `ml_weights.h` | On-device MLP |
| `src/cpp/runtime/esp_idf/` | CSI + Traffic Adapter |
| `src/cpp/frontend/{esphome,native,matter}/` | Ecosystem |
| `docs/performance/README.md` | Upstream Replay-Metriken |

## Konfiguration und Parameter

| Parameter | Upstream (Desk) | Status |
|-----------|-----------------|--------|
| Default target rate | `csi_target_pps` **100** → 10 ms Slots | `FACT` |
| Detector window | 1000 ms; Eval 250 ms; min occupancy 70 % | `FACT` |
| Subcarriers | fixed 12 for turb/L1; 56-bin profile for shape/ML | `FACT` |
| Hardware | C6/C5/C3/S3/S2/Classic; Wi-Fi 4 2.4 GHz (C5 auch 5 GHz Pfade) | `FACT` |
| AGC | remains on; features scale-invariant | `FACT` |
| Privacy stance | local; raw CSI optional; consent guide | `FACT` |

## Ebene C

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| CSI Motion Sensor, no camera; on-device | `EVID-ESPECTRE-2026-10-25-001` | `FACT` |
| Temporal admission + 100 pps production timing | `EVID-ESPECTRE-2026-10-25-002` | `FACT` |
| Lightweight vs High-Accuracy MLP | `EVID-ESPECTRE-2026-10-25-003` | `FACT` |
| Managed traffic modes (ping/dns/wifi_raw/external) | `EVID-ESPECTRE-2026-10-25-004` | `FACT` |
| Upstream holdout replay metrics published | `EVID-ESPECTRE-2026-10-25-005` | `FACT` (Upstream report) |
| Eigene Raum-Lab-Zahlen | — | `UNKNOWN` |

## Offene Fragen

- Placement: ein Board/Raum vs. Peer-Null-Data-Geometrie im eigenen Lab?
