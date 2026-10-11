# Follow-on ideas (aus welle-io)

```yaml
reuse_outcomes:
  reused: [dab-plus, rtl-sdr]
  process: "parity 0.6.5 → 0.6.6; DELTA in audits/welle-io-2026-foreign/"
  new: []
  not_helped: []
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Upstream-Gain-Tabelle in PiDrive-Docs spiegeln | `dab-plus`, `rtl-sdr` | Index ≠ dB mit Code-Link |
| Web-Carousel als Scan-Ersatz prüfen | `dab-plus` | `-C N -w` vs. eigener Scanner |
| rtl_tcp Remote-Stick | `rtl-sdr` | `-F rtl_tcp,host:port` für getrennten Host |
| Spektrum bleibt DAB-kanalgebunden | `sdr-spectrum-fft` | Allzweck-FFT nicht durch welle ersetzen |
| DLS vs. FM-RDS Meta-Bridge | `dab-plus`, `fm-rds` | Protokoll-Vergleich (siehe pi-fm-tx) |
| Soapy/Airspy nur bei Bedarf vertiefen | observed | kein Sheet ohne Transfer |

Nachbar: [`pidrive`](../pidrive/) · Kampagne [`welle-io-2026-foreign`](../../audits/welle-io-2026-foreign/).
