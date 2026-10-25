# Project Scope: espectre (Fremd)

```yaml
project_id: espectre
title: ESPectre — Wi-Fi CSI Motion Sensing (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "5866bff6aa3a8ac41ed70d2476c115ea6285b277"
repos:
  - https://github.com/francescopace/espectre
status: active
```

## Zweck

Fremdrepo als Desk-Quelle für **Wi-Fi CSI (Channel State Information) Motion Sensing** auf ESP32-Familie: Echtzeit-CSI, Temporal Admission bei hohem `csi_target_pps`, on-device Detektoren (statistisch + kleines NN), lokale Frontends (Native/ESPHome/Matter/Micro). Wissen in A-Sheet + Application; **keine** Rohdatensätze spiegeln.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `src/cpp/core` Detektoren + Temporal Sampler | Sensing-Contract | ja |
| `runtime/esp_idf` CSI Capture + Traffic | ESP-IDF Adapter | ja (Desk) |
| Frontends Native / ESPHome / Matter / Micro | Ecosystem | angrenzend (Transport-Kontrast) |
| Dataset / ML-Training Tools | Research | Links only; keine `data/`-Spiegelung |
| Browser Flash/Monitor | Ops UX | out of depth |
| Person-ID / People-Count / Safety-Zert | — | **nein** (Upstream-Grenze) |
| Marauder CSI-UI | Kontrast | nur Inventar-Querverweis |

## Nicht-Ziele

- Roh-CSI-NPZ / Model-Weights in die KB kopieren
- Promiscuous-PCAP-Sniff mit CSI vermischen (`esp-wifi-promiscuous-pcap`)
- LLM-Inference mit CSI-MLP vermischen (`mcu-ple-inference`)
- Unautorisierte Überwachung fremder Räume (Consent/Privacy Upstream beachten)

## Quellen für das Audit

| Quelle | Pfad / URL | Bemerkung |
|--------|------------|-----------|
| Code | https://github.com/francescopace/espectre @ `5866bff` | Fremd, Desk |
| Docs | `docs/CSI.md`, `ARCHITECTURE.md`, `ALGORITHMS.md` | SoT Architektur |
| Performance | `docs/performance/README.md` | Upstream Metrics → Desk-`FACT` |

## Prioritäten

1. Neues Sheet `wifi-csi-motion` + Application
2. Kontrast: Promiscuous/PCAP, RF-Environment-Monitor, Marauder CSI-observed
3. pps / Temporal Admission + Lightweight vs High-Accuracy als A-Fallstricke
4. Chip-Matrix C3/C5/C6/S2/S3/Classic — Gate, kein Universal-Claim

## Offene Scope-Fragen

- MQTT/HA Discovery als eigenes Application-Sheet später?
- Marauder `CsiMotion*` — Vertiefung oder nur Kontrast-Zeile?
