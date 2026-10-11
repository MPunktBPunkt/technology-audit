# AUDIT DELTA — pidrive-2026-radio-bt

```yaml
campaign: pidrive-2026-radio-bt
old_standard: "0.6.3"
new_standard: "0.6.6"
revalidated: 2026-10-11
method: desk revalidation (same commit b61df4d) + 0.6.4–0.6.6 process rules
contrasts: [pi-fm-tx-2026-foreign, esp-fm-tx-2026-foreign, welle-io-2026-foreign, esp32-bt-gateway]
```

## OLD AUDIT (0.6.3)

| Bereich | Stand |
|---------|--------|
| Claims | DAB+/RTL/PMR/Airband/FFT + A2DP/AVRCP; RX≠TX; Pi BlueZ vs ESP-Gateway |
| UNKNOWNs | Antennenvergleich verdichtet; DAB→BT hörbar |
| Sheets | 5 neu (DAB/RTL/PMR/Airband/FFT) + A2DP/AVRCP gewachsen |
| Process gaps | kein formales Chip-/Stack-Scope; Lag zu 0.6.4–0.6.6 undokumentiert |

## NEW AUDIT (0.6.6 Revalidation)

| Bereich | Delta |
|---------|--------|
| geschärft | RX-Sheets ≠ TX (`rpi-gpio-fm-tx` / `esp32-apll-fm-tx`); welle-Spektrum ≠ Allzweck-FFT; RTL Gain Index≠dB |
| Stack-Scope | A2DP/AVRCP: Pi BlueZ/PipeWire ≠ ESP Classic-Controller — getrennte Applications, kein stiller Transfer |
| Tuner-Scope | RTL2832U+R820T-Familie als belegter Stick-Contract; andere SDR nicht automatisch |
| Gates | Freenet/LPD/CB / UKW-WBFM bleiben observed (G19); kein Pi-TX-Sheet aus Empfang |
| Cross-Project | Bidirektional `welle-io`, `pi-fm-tx`, `esp32-bt-gateway` |

## Quantitativ

| Metrik | 0.6.3 | nach 0.6.6 | Δ |
|--------|-------|------------|---|
| Radio/BT Pilot-Sheets | 7 applied | 7 | 0 |
| Evidence-IDs | 14 | 17 | +3 Scope/Match |
| `standard_gaps` | undokumentiert | keine | Parität |

## Urteil

0.6.6 liefert hier vor allem **Abgrenzungs- und Stack-Schärfe** (RX/TX, Spektrum-Rollen, Pi≠ESP-BT), nicht neue Feld-FACTs. Passt als großer fachlicher Audit nach dem ESP-Fitness-Block.

## Artefakte

| Artefakt | Pfad |
|----------|------|
| Kampagne | [README.md](README.md) |
| Kontrast TX | [`pi-fm-tx`](../pi-fm-tx-2026-foreign/), [`esp-fm-tx`](../esp-fm-tx-2026-foreign/) |
| Kontrast RX-Upstream | [`welle-io-2026-foreign`](../welle-io-2026-foreign/) |
