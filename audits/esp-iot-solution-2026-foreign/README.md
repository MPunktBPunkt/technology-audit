# Audit Campaign: esp-iot-solution-2026-foreign

```yaml
id: esp-iot-solution-2026-foreign
project_id: esp-iot-solution
started: 2026-10-13
ended: null
status: active
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "1d9a68a"
reuse_outcomes:
  reused: [esp-usb-host, usb-msc]
  new: [esp-usb-audio-uac]
  not_helped: []
  process: "Desk foreign USB/Audio focus under 0.7.1; no full component catalog"
```

## Ziel

Espressif IoT Solution (Commit `1d9a68a`) als offizielle Quelle für **USB Device UAC** und **USB Host Stream** in die KB — mit klarer Rollenabgrenzung zu MSC und zu Community-Headset-Beispielen.

## Scope

[SCOPE](../../projects/esp-iot-solution/SCOPE.md) — Desk only; kein Host-OS-Lab.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | `standard_version` 0.7.1 + Profil `lab-tool` | erfüllt |
| 2 | Sheet `esp-usb-audio-uac` + App; `esp-usb-host` gewachsen | erfüllt |
| 3 | Evidence auf Commit `1d9a68a` | erfüllt |
| 4 | C11 Review Checks aus Evidence; C12 Kill/n-a klar | erfüllt |
| 5 | Keine erfundene Lab-/Field-Facts | erfüllt |
| 6 | `ta-assist check` 0 errors | erfüllt (2026-10-13) |
| 7 | Host-OS UAC Labmatrix | offen (bewusst) |

## Decision Trace

Desk-Katalog / Slug-Entscheidung (kein Lab-Go/No-Go) — Trace optional; hier Kurzform:

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt (opt.) |
|--------------|-----------------|-------------|------------|-------------------------|
| Neuer Slug UAC Device? | Host-Sheet reicht? | `EVID-IOTSOL-UAC-2026-10-13-001` | Nein → `esp-usb-audio-uac` | KNOWN BEFORE TEST |
| Host-Stream unter `esp-usb-host`? | UVC+UAC Host = Device? | `EVID-IOTSOL-USBH-2026-10-13-001` | Ja reuse Host-Sheet | KNOWN BEFORE TEST |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt (opt.) |
|-------------|--------------|-------------------------|
| `EVID-IOTSOL-UAC-2026-10-13-001` | Vor Device-UAC-Claim: Chip in S2/S3/P4-Familie? | KNOWN BEFORE TEST |
| `EVID-IOTSOL-UAC-2026-10-13-003` | Vor „ein Descriptor für alle OS“: Win/Linux/macOS-Gates lesen | KNOWN BEFORE TEST |
| `EVID-IOTSOL-USBH-2026-10-13-001` | Host-`usb_stream` nicht als Device-Headset dokumentieren | KNOWN BEFORE TEST |

## Kill-Kriterien

**Hypothese:** Offizielle Components liefern belastbare Desk-Contracts für USB-Audio-Rollen.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Component behauptet Classic-ESP32 Device-UAC ohne OTG-Gate | nicht eingetreten (Targets explizit) |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Desk-Katalog ohne Messlauf; Chip-/Rollen-Gates sind Transfer-Bremsen, keine Falsifikation einer Lab-Hypothese. UNKNOWN Host-OS-Verhalten ≠ automatisches STOP.
```

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| Reuse / Chip-Transfer-Gates | [`docs/REUSE.md`](../../docs/REUSE.md) |
| hw-path-gate (Rollen/Chip) | [`methods/hw-path-gate.md`](../../methods/hw-path-gate.md) |

## Knowledge Feedback

Desk only — C13 n/a (kein Lab/Field-Ergebnis).

## Bezug

[INVENTORY](../../projects/esp-iot-solution/INVENTORY.md) · [evidence](evidence.md) · Community [`esp-usb-audio-example-2026-foreign`](../esp-usb-audio-example-2026-foreign/) · Host [`espusbhost-2026-foreign`](../espusbhost-2026-foreign/)

## Lessons → Transfer

- Device-UAC und Host-`usb_stream` sind **beide** in einem Repo — trotzdem getrennte Sheets/Apps.
- OS-Kompatibilität und fehlende dynamische Sample-Rate sind A-Fallstricke, keine Application-Kuriositäten.
