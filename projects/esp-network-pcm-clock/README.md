# esp-network-pcm-clock (Fremdvergleich)

Desk-Aufnahme von sechs unveränderlichen Quell-Snapshots zu Netzwerk-PCM,
Framing, elastischen Puffern und Clockdrift. Standard **0.7.1**; keine
Lab- oder Feldmessung.

| | |
|--|--|
| Scope | [SCOPE.md](SCOPE.md) |
| Inventar | [INVENTORY.md](INVENTORY.md) |
| Applications | [pdap](applications/pdap.md) · [esp-i2s-audio](applications/esp-i2s-audio.md) |
| Audit | [`esp-network-pcm-clock-2026-foreign`](../../audits/esp-network-pcm-clock-2026-foreign/) |
| Folge | [FOLLOW-ON-IDEAS.md](FOLLOW-ON-IDEAS.md) |

## Varianten

- **A — UDP/RTP:** `esp32-rtp`; RTP-Sequenz/Zeitstempel und Paketpuffer.
- **B — TCP:** StreamLine mit eigenem `ELI1`-Framing; TCP-Streamer und
  Snapcast nur als Host-/Synchronisationskontrast.
- **C — elastisch:** `esp_elastic_pcm_buffer` als transportunabhängige
  Watermark-/Rate-Control-Schicht; Arduino Audio Tools als I2S-Pipeline-Kontrast.

UDP/RTP und TCP sind getrennte Varianten. TCP-Bytestrom-Framing wird nicht als
RTP bezeichnet und RTP-Verlustsemantik nicht auf TCP übertragen.
