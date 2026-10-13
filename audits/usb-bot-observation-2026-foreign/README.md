# Audit Campaign: usb-bot-observation-2026-foreign

```yaml
id: usb-bot-observation-2026-foreign
project_id: usb-bot-observation
started: 2026-10-13
ended: 2026-10-13
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: usb-msc
reuse_outcomes:
  reused: [usb-msc]
  new: []
  not_helped:
    - "Kein Repository liefert einen realen NBT-Capture."
  process: "Desk-only Vergleich von Device-, Inline- und Host-Kontrastpfaden."
  decisions_touched: [observation-path, transparent-capture-gate]
```

## Ziel

Sieben immutable Fremdquellen darauf prüfen, welche CBW/CDB/Data/CSW-Grenzen,
READ(10)-Parameter sowie Sense-/Reset-Pfade sie sichtbar machen — und welche
Lücken für einen späteren NBT-Beobachtungspfad bleiben.

## Scope

- **Im Scope:** die in
  [`projects/usb-bot-observation/SCOPE.md`](../../projects/usb-bot-observation/SCOPE.md)
  gepinnten Pfade; Desk-Code und Upstream-Dokumentation; Reuse `usb-msc`.
- **Nicht im Scope:** Hardware, Build, Lab, Fahrzeug, NBT-Capture,
  Timingmessung, neue Shared Sheets/Methods/Indexes.

## Ergebnis in drei Beobachtungspfaden

| Pfad | Zweck | Desk-Verdict |
|------|-------|--------------|
| **Device-Instrumentierung** | CBW/CDB, Datenfortschritt, CSW und Reset im MSC-Device korrelieren | bevorzugter nächster Engineering-Kandidat; noch ungebaut |
| **Inline-Proxy/Capture** | Busfolge unabhängig vom Device-Logger sehen | konzeptionell vollständigste Sicht; USBProxy-legacy nicht ungeprüft einsatzfähig, Transparenz `UNKNOWN` |
| **Host/Gadget-Kontrast** | Logger/Parser mit kontrollierten Commands validieren | geeignetes Vor-Gate; kein NBT-Beweis |

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Standard 0.7.1, Projekt- und Kampagnenartefakte | erfüllt |
| 2 | alle sieben Quellen auf immutable SHA | erfüllt |
| 3 | Linux/ESP-USB/TinyUSB ausdrücklich pfadspezifisch | erfüllt |
| 4 | CBW/CDB/Data/CSW und READ(10) getrennt | erfüllt |
| 5 | Sense-/Resetpfade und Capture-Grenzen dokumentiert | erfüllt |
| 6 | NBT-CDB/Sense/Timing ohne Capture als `UNKNOWN` | erfüllt |
| 7 | A/B/C, Decision Trace, Review Checks, Kill, C10–C13 | erfüllt / C13 bewusst n/a (Desk-only) |
| 8 | keine Shared Indexes/Technologies/Methods/`next-audits` geändert | erfüllt |

## Decision Trace

Desk-Kampagne mit Go/No-Go für einen späteren Instrumentierungspfad (**C10**).

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|-----------------|
| Device-Instrumentierung als ersten Engineering-Kandidaten führen | Lassen sich Commandgrenzen im Device-Stack explizit erhalten? | `EVID-USBBOT-2026-10-13-004`, `007`–`009` | Ja, als Implementierungs-Hypothese; Lab nötig | `DISCOVERED DURING TEST` |
| Inline-Pfad nicht direkt im Fahrzeug einsetzen | Ist USBProxy-legacy als transparenter Capture belegt? | `EVID-USBBOT-2026-10-13-002`, `003`, `012` | Nein; Build-/Baseline-Gates vor Fahrzeug | `DISCOVERED DURING TEST` |
| Host/Gadget-Kontrast als Vor-Gate verwenden | Können kontrollierte Hosts klare BOT-Folgen erzeugen? | `EVID-USBBOT-2026-10-13-005`, `006`, `010` | Ja; Parser/Logger zuerst dort prüfen | `DISCOVERED DURING TEST` |
| Block-I/O nicht als Command-Capture werten | Erhält `usb-tools` CBW/CDB/CSW? | `EVID-USBBOT-2026-10-13-001` | Nein; nur Workload/Throughput-Kontrast | `DISCOVERED DURING TEST` |
| Kein NBT-Claim | Existieren reale NBT-Captures in dieser Kampagne? | `EVID-USBBOT-2026-10-13-012`, `013` | Nein; CDB/Sense/Reset/Timing `UNKNOWN` | `KNOWN BEFORE TEST` |

## Engineering Review Checks

Zielcode einer späteren Instrumentierung (**C11**); noch keine
Implementierungsbehauptung.

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|-----------------|
| `EVID-USBBOT-2026-10-13-002`, `004`–`007` | CBW-Tag, CDB-Länge/-Bytes und CBW DataTransferLength atomar erfassen | `DISCOVERED DURING TEST` |
| `EVID-USBBOT-2026-10-13-007`, `009` | Callback-Chunks kumulieren; nie `bufsize` als READ(10)-CDB-Länge ausgeben | `DISCOVERED DURING TEST` |
| `EVID-USBBOT-2026-10-13-002`, `005` | CSW-Tag, Residue und Status gegen denselben CBW-Tag prüfen | `DISCOVERED DURING TEST` |
| `EVID-USBBOT-2026-10-13-004`, `005`, `008` | BOT Reset, Clear-Halt und Re-Enumeration als neue Epoch markieren | `DISCOVERED DURING TEST` |
| `EVID-USBBOT-2026-10-13-005`, `006`, `008` | REQUEST SENSE nur zusammen mit auslösendem Fehler/CSW interpretieren | `DISCOVERED DURING TEST` |
| `EVID-USBBOT-2026-10-13-003`, `011`, `012` | Drop-Zähler, monotone Zeitstempel und Beobachter-Baseline vor Transparenzclaim | `DISCOVERED DURING TEST` |
| `EVID-USBBOT-2026-10-13-013` | Hostlabel und Evidence-Schicht erzwingen; kontrollierter Host ≠ NBT | `KNOWN BEFORE TEST` |

## Kill-Kriterien

Präregistriert für einen **künftigen** Beobachtungslauf (**C12**); in dieser
Desk-Kampagne wurde kein Messlauf durchgeführt.

**Hypothese:** Ein instrumentierter Pfad kann reale BOT-Commandgrenzen
korrelieren, ohne die Zielsequenz materiell zu verändern.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | CBW-Tag/CDB und CSW-Tag/-Status lassen sich nicht verlustfrei korrelieren | offen — kein Lab |
| 2 | READ(10)-CDB-Transferlänge bleibt von Callback-/Endpoint-Chunks ununterscheidbar | offen — kein Lab |
| 3 | Control-Reset/Clear-Halt oder Sense-Folge fehlt im Capture | offen — kein Lab |
| 4 | Drop-/Overflow-Zähler zeigt verlorene Events | offen — kein Lab |
| 5 | Beobachter verändert Enumeration, Commandfolge, Resetanzahl oder Latenz außerhalb eines vorab gesetzten Budgets | offen — Budget und Baseline fehlen |
| 6 | Daten stammen nur aus PC/ESP/VM, werden aber als NBT-Verhalten interpretiert | permanenter Integritäts-Kill |

`UNKNOWN` ist kein automatisches STOP. Hier erzwingt es das nächste Gate:
kontrollierter Lab-Kontrast und Transparenzbaseline vor einem NBT-Claim.

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| BOT-Command-Beobachtung | [`usb-bot-command-observation`](../../methods/usb-bot-command-observation.md) |
| LBA-/Timing-Instrument | [`msc-lba-timing-instrument`](../../methods/msc-lba-timing-instrument.md) |
| Trace-Korrelation | [`msc-trace-correlation`](../../methods/msc-trace-correlation.md) |
| Busy-/Retry-Semantik | [`msc-busy-retry-semantics`](../../methods/msc-busy-retry-semantics.md) |

## Bezug Inventar

- Inventar: [`usb-bot-observation/INVENTORY.md`](../../projects/usb-bot-observation/INVENTORY.md)
- Application: [`applications/usb-msc.md`](../../projects/usb-bot-observation/applications/usb-msc.md)
- Reuse: [`technologies/usb-msc/SHEET.md`](../../technologies/usb-msc/SHEET.md)

## Ergebnisse

- [`evidence.md`](evidence.md) — Desk-Evidence `EVID-USBBOT-2026-10-13-*`
- Device-Instrumentierung bevorzugt als nächster Engineering-Kandidat; der
  Inline-Pfad bleibt Hardware-/Baseline-Gate; Host/Gadget ist der
  kontrollierte Vorprüfpfad.
- Keine reale NBT-Capture- oder Timingbehauptung.

## Knowledge Feedback

**C13:** n/a für Lab/Field — diese Kampagne ist Desk-only.

| Ergebnis | Evidence-ID | Zurück in |
|----------|-------------|-----------|
| Desk-Pfadvergleich | `EVID-USBBOT-2026-10-13-001`–`013` | [`usb-msc` Application](../../projects/usb-bot-observation/applications/usb-msc.md) |

Desk-Evidence ≠ Lab-Fact ≠ Field-Fact. Ein späterer Lab-/Feldlauf braucht neue
Evidence-IDs; diese Kampagne darf nicht als dessen Feedback ausgegeben werden.

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 präregistrierte, falsifizierbare Kill-Kriterien | PASS; Status offen, weil kein Messlauf |
| C13 Knowledge Feedback | n/a dokumentiert; keine Lab-/Field-Evidence |

## Lessons → Transfer

- Eine Callback-Grenze ist keine BOT-Commandgrenze.
- Ein Hostgenerator validiert Parser, aber nicht NBT-Verhalten.
- Ein Inline-Pfad ist erst nach gemessener Beobachterwirkung „transparent“.
- Tags, Residue, Sense und Reset-Epoch sind für belastbare Korrelation
  gemeinsam nötig.

## Offene Punkte nach Abschluss

- Implementierung und Lab-Validierung der Device-Instrumentierung
- Baseline/Budget für Beobachterwirkung
- Entscheidung, ob der Inline-Pfad danach noch nötig und praktikabel ist
- alle NBT-spezifischen CDB-/Sense-/Reset-/Timingfragen bleiben `UNKNOWN`
