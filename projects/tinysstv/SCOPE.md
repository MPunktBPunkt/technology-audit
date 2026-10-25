# Project Scope: tinysstv (Fremd)

```yaml
project_id: tinysstv
title: TinySSTV — Martin M1 SSTV TX on ESP32-C3 (Fremd)
updated: 2026-10-25
profile_hint: lab-tool
reviewed_commit: "b9977a62d45dbd459d6bbec6e971383e721ddcf4"
repos:
  - https://github.com/JO3ALT/TinySSTV
status: active
```

## Zweck

Fremdrepo als Desk-Quelle für **Martin-M1-SSTV-AF-Synthese** auf ESP32-C3: Bild-Upload (Captive AP), DDS-Töne, Sigma-Delta/PDM-GPIO, Hardware-verifizierte Timing-Claims. Abgrenzung zu UKW-APLL-FM-Sheets.

**Recht:** On-Air nur mit gültiger Amateurfunk-Berechtigung und zulässigem Setup; Sheet/Audit beschreiben Technik, keinen Sendebetrieb.

## Systeme und Grenzen

| System | Rolle | Im Scope? |
|--------|-------|-----------|
| `sstv.rs` / `audio.rs` | Martin M1 + DDS/PDM | ja |
| Captive AP + Web Upload | Bild → Firmware | ja (Desk) |
| microSD RGB24 vs RAM RGB333 | Speicherpfade | ja |
| Externes LPF + Radio AF/PTT | Hardware | Application / Gate |
| PTT-GPIO-Ansteuerung | reserved, nicht implementiert | observed gap |
| Andere SSTV-Modes / Cardputer-Fork | — | FOLLOW-ON / Link |
| APLL UKW-FM | — | **nein** (anderer Contract) |

## Nicht-Ziele

- Anleitung zum unlizenzierten Funken
- PTT-Schaltplan als „fertig sicher“
- APLL-FM- oder Pi-GPIO-FM-Vermischung
- JPEG-Decoder auf dem Chip (Upstream: Browser croppt)

## Quellen

| Quelle | URL | Bemerkung |
|--------|-----|-----------|
| Code | https://github.com/JO3ALT/TinySSTV @ `b9977a6` | Rust + ESP-IDF |
| README | Hardware-Proof, Timing | Desk MEASURED → FACT |

## Prioritäten

1. Sheet `sstv-martin-m1` + Application
2. Kontrast `esp32-apll-fm-tx` / `rpi-gpio-fm-tx`
3. PDM≠Line-Audio Fallstrick; PTT-Lücke sichtbar
