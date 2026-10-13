# Audit Campaign: esp-network-pcm-clock-2026-foreign

```yaml
id: esp-network-pcm-clock-2026-foreign
project_id: esp-network-pcm-clock
started: 2026-10-13
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reuse_outcomes:
  reused: [pdap, esp-i2s-audio]
  new: []
  not_helped: []
  process: "Desk-only A/B/C; immutable SHAs; Lab UNKNOWN with preregistered gates"
```

## Ziel

Sechs feste Fremd-Snapshots darauf prüfen, welche Framing-, Puffer- und
Clock-Patterns einen späteren Netzwerk-PCM-Labvergleich tragen. Desk-Claims
werden von noch unbekannten Lab-/Feldclaims getrennt; UDP/RTP und TCP bleiben
unterschiedliche Varianten.

## Scope

[Project Scope](../../projects/esp-network-pcm-clock/SCOPE.md) — **Desk only**.
Keine Messwerte, kein Build, kein Geräte- oder Hörtest.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1, `lab-tool`, feste sechs SHAs | erfüllt |
| 2 | RTP/UDP, TCP und elastischer Puffer getrennt | erfüllt |
| 3 | Reuse `pdap` + `esp-i2s-audio`; Apps mit A/B/C-Ebenen | erfüllt |
| 4 | Framing, Watermarks, Drift, Under-/Overflow, Reconnect→Mute abgedeckt | erfüllt (Desk/UNKNOWN getrennt) |
| 5 | C10–C13, G17, Review Checks und Kill-Kriterien dokumentiert | erfüllt |
| 6 | G-CLK, G-BUF, G-REC, G-AUD, G17-SOC im Lab ausgeführt | offen |

## Varianten-Entscheidungsraum

| Variante | Transport/Framing | Buffer-/Clock-Ansatz | Aktueller Status |
|----------|-------------------|----------------------|------------------|
| RTP/UDP | RTP über UDP (`esp32-rtp`) | RTP timestamp + adaptiv wachsender Paketpuffer | Desk-Kandidat; Lab `UNKNOWN` |
| TCP | TCP/TLS mit eigenem `ELI1`-Record (StreamLine) | Host-Playout; TCP-Streamer/Snapcast als Kontrast | Desk-Kandidat; Lab `UNKNOWN` |
| Elastic Buffer | kein Transport; nach RTP/UDP oder TCP | vier Watermarks + Fill-Level-Speed-Control | Desk-Kandidat; Lab `UNKNOWN` |

## Decision Trace — C10

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neues Technology Sheet? | Sind `pdap`/`esp-i2s-audio` unzureichend? | `EVID-PCMNET-2026-10-13-001` | Nein; nur Applications | KNOWN BEFORE TEST |
| RTP/UDP und TCP gemeinsam behandeln? | Gleiche Wire-/Fehlersemantik? | `EVID-PCMNET-2026-10-13-002`, `-006` | Nein; Parser/Zähler/Gates getrennt | DISCOVERED DURING TEST |
| Elastic Buffer als Transport werten? | Implementiert Component Netzwerkframing? | `EVID-PCMNET-2026-10-13-004` | Nein; hinter RTP/UDP oder TCP einsetzen | DISCOVERED DURING TEST |
| Clockdrift als gelöst markieren? | Gibt es Zielboard-Labdaten? | `EVID-PCMNET-2026-10-13-012` | Nein; `UNKNOWN`, G-CLK nötig | KNOWN BEFORE TEST |
| Reconnect freigeben? | Mute, State-Reset und Prefill belegt? | `EVID-PCMNET-2026-10-13-013` | Nein; G-REC ist Freigabe-Gate | KNOWN BEFORE TEST |
| Snapcast übernehmen? | Ist Desktop-Multiroom-Sync ein ESP-Beleg? | `EVID-PCMNET-2026-10-13-010` | Nein; nur Kontrast | DISCOVERED DURING TEST |

## Engineering Review Checks — C11

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-PCMNET-2026-10-13-002` | RTP-Version/Sequenz/timestamp/payload vor Enqueue validieren; UDP-Lücken nicht als TCP-Fehler modellieren | KNOWN BEFORE TEST |
| `EVID-PCMNET-2026-10-13-003` | Underflow-Rebuffer und Overflow-Drop dürfen keine alten Slots ausspielen | DISCOVERED DURING TEST |
| `EVID-PCMNET-2026-10-13-004` | `start <= capacity` und `low <= target <= high <= capacity`; Prefill nach leerem Puffer erneut setzen | DISCOVERED DURING TEST |
| `EVID-PCMNET-2026-10-13-005` | Speed-Grenzen, Format und State-Reset prüfen; Rate-Control nicht mit Peripheral-Clock-Fakt gleichsetzen | DISCOVERED DURING TEST |
| `EVID-PCMNET-2026-10-13-006` | TCP-Header und Payload über partielle Reads reassemblieren; Magic/Version/Längen vor PCM-Freigabe prüfen | DISCOVERED DURING TEST |
| `EVID-PCMNET-2026-10-13-007` | explizite Silence, fehlende Sequenz und Rebuffering als drei Zustände zählen | DISCOVERED DURING TEST |
| `EVID-PCMNET-2026-10-13-008` | Ringkapazität, Target-Füllung und End-to-end-Latenz nicht synonym behandeln | DISCOVERED DURING TEST |
| `EVID-PCMNET-2026-10-13-010` | Host-Sync-Kontrast nicht als ESP-/I2S-Beweis aufwerten | KNOWN BEFORE TEST |
| `EVID-PCMNET-2026-10-13-013` | Disconnect atomar: mute → parser/queue reset → reconnect → validate → prefill → unmute | KNOWN BEFORE TEST |
| `EVID-PCMNET-2026-10-13-014` | `esp32-rtp` nicht als lizenzgeklärte Implementierungsgrundlage übernehmen, bis eine Lizenz am Pin verifiziert ist | DISCOVERED AFTER TEST |

## Präregistrierte Lab-Gates

Keine Zeile ist ein Messergebnis.

| Gate | Aufbau / Beobachtung | PASS | STOP / FAIL |
|------|----------------------|------|-------------|
| G-CLK | konstante PCM-Quelle; Sequenz, Fill-Level, Sink-Clock und Korrekturereignisse zeitkorreliert | Fill-Level bleibt geregelt und erholt sich nach Störung ohne nachhaltigen Marsch zu 0/Capacity | reproduzierbarer nachhaltiger Marsch endet in Under-/Overflow oder unkontrolliertem Reset |
| G-BUF | identisches Störprofil getrennt für RTP/UDP und TCP; Elastic Buffer jeweils an/aus | Zustände und Zähler entsprechen tatsächlich injizierten Lücken/Bursts; Recovery erreicht Prefill/Normal | stale/dupliziertes PCM, unmarkierter Drop oder Zähler-/Zustandswiderspruch |
| G-REC | Verbindung während Nicht-Null-PCM trennen und wiederherstellen | Ausgabe ab Disconnect stumm; Alt-PCM verworfen; Unmute erst nach validiertem Framing und Prefill | irgendein Alt-PCM/Noise vor Freigabe oder Sessionzustand über Reconnect vermischt |
| G-AUD | Elastic Buffer gegen feste Bufferpolitik mit demselben Input vergleichen | keine Entscheidung ohne verlinktes Signal-/Hörartefakt | Rate-Control wird allein aufgrund Desk-Code als „transparent“ freigegeben |
| G17-SOC | Lauf je ausdrücklich benanntem SoC/Board/Codec | Claim bleibt auf geprüfte Kombination begrenzt | Ergebnis wird ohne eigenes Gate auf Classic↔S3 übertragen |

## Kill-Kriterien — C12

**Hypothese:** Mindestens eine getrennte RTP/UDP- oder TCP-Kette, jeweils
optional mit Elastic Buffer,
kann einen sicheren Netzwerk-PCM-Pfad zum I2S-Sink bilden.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Variante besitzt keinen eindeutig parsebaren Frame-/Record-Contract bis zur PCM-Grenze | präregistriert |
| 2 | G-REC spielt nach Disconnect und vor neuem Prefill Alt-PCM oder Nicht-Null-Daten aus | präregistriert |
| 3 | G-CLK zeigt bei stabiler Quelle reproduzierbar einen ungeregelten Fill-Level-Marsch bis Under-/Overflow | präregistriert |
| 4 | RTP/UDP und TCP benötigen gemeinsame, semantisch widersprüchliche Fehlerzähler oder Parserzustände | präregistriert |
| 5 | G17-SOC kann für den Ziel-SoC nicht ausgeführt oder der Peripheral-/Clockpfad nicht eindeutig benannt werden | präregistriert |

Die Kill-Kriterien werden **vor** dem ersten Messlauf eingefroren. `UNKNOWN`
allein ist kein STOP; ein eingetretenes Kriterium ist es.

## Review Checks — Kampagnenfreigabe

- [x] C10 Decision Trace vorhanden.
- [x] C11 aus entscheidungsrelevanter Evidence abgeleitet.
- [x] C12 vor Lab präregistriert.
- [x] C13-Rückkanal definiert; derzeit keine Lab-/Field-Evidence.
- [x] G17 nennt SoC-Scope oder `UNKNOWN`.
- [x] Desk-`FACT` wird nicht als `MEASURED` geführt.
- [x] UDP/RTP und TCP werden weder im Framing noch in Fehlerzählern vermischt.
- [x] Keine Shared Indexes, Technologies, Methods oder `next-audits` geändert.

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Clockdrift/Jitterbuffer | [`pcm-clock-drift-jitter-buffer`](../../methods/pcm-clock-drift-jitter-buffer.md) |

## Knowledge Feedback — C13

Noch kein Lab-/Field-Ergebnis; daher **C13 n/a für aktuelle Desk-Evidence**.
Beim ersten Lauf:

| Lab/Field | Neue Evidence-ID | Zurück in |
|-----------|------------------|-----------|
| G-CLK/G-BUF/G-REC/G-AUD | neue `EVID-PCMNET-YYYY-MM-DD-nnn` | `projects/esp-network-pcm-clock/applications/pdap.md` |
| G17-SOC/I2S | neue `EVID-PCMNET-YYYY-MM-DD-nnn` | `projects/esp-network-pcm-clock/applications/esp-i2s-audio.md` |

Ein Sheet-Delta wäre ein separater Review und ist nicht Teil dieser Kampagne.

## Bezug und Ergebnisse

[Inventory](../../projects/esp-network-pcm-clock/INVENTORY.md) ·
[pdap Application](../../projects/esp-network-pcm-clock/applications/pdap.md) ·
[esp-i2s-audio Application](../../projects/esp-network-pcm-clock/applications/esp-i2s-audio.md) ·
[Evidence](evidence.md)

## Lessons → Transfer

- Framing vor Pufferpolitik entscheiden; ein Puffer repariert keinen
  mehrdeutigen Bytestrom.
- TCP und RTP können ähnliche PCM-Nutzlasten tragen, haben aber verschiedene
  Zustell- und Fehlersemantik.
- Watermarks, Clockkorrektur und Reconnect-Mute sind getrennte
  Zustandsmaschinen und benötigen getrennte Observability.

## Offene Punkte nach Abschluss

- Lab-Gates ausführen und neue Evidence-IDs anlegen.
- Variantenentscheidung erst nach Gates treffen.
- Danach prüfen, ob generalisierbares A-Delta einen separaten Sheet-Review
  rechtfertigt.
