# Follow-on ideas — esp-network-pcm-clock

```yaml
reuse_outcomes:
  reused: [pdap, esp-i2s-audio]
  new: []
  not_helped: []
```

Nur Folgearbeit; keine der Ideen ist in der Desk-Kampagne gemessen.

| Priorität | Idee | Gate / erwartetes Artefakt |
|-----------|------|----------------------------|
| 1 | A/B/C-Harness mit identischem PCM- und Störprofil | G-CLK + G-BUF; Rohdaten außerhalb dieser Wissensbasis |
| 2 | Reconnect→Mute-State-Machine testen | G-REC; Trace von Disconnect, Mute, Prefill, Unmute |
| 3 | Fill-Level, Sequenzlücken, Under-/Overflow gemeinsam loggen | zeitkorrelierter Trace ohne Protokollvermischung |
| 4 | C-Puffer hinter A und B separat einsetzen | Vergleich „gleicher Puffer, anderer Transport“ |
| 5 | Rate-Control gegen unveränderte PCM-Rate vergleichen | G-AUD; keine Qualitätsbehauptung ohne Lab |
| 6 | G17-Matrix ESP32-S3 vs. ESP32 classic ECO3 | eigener Build/Lab je SoC; kein impliziter Transfer |

## Vor Lab festzuhalten

- A (UDP/RTP) und B (TCP) erhalten getrennte Parser, Zähler und Fehlerklassen.
- C darf dieselbe Buffer-API verwenden, aber Transportereignisse müssen ihre
  Herkunft behalten.
- Nach Reconnect bleibt Ausgabe stumm, bis Framing validiert und Prefill
  abgeschlossen ist; Alt-PCM darf nicht ausgespielt werden.
- C13-Rückkanal: neue Lab-Evidence zuerst in `evidence.md`, danach in die
  jeweilige Application; Shared Sheets nur in separatem Review.
