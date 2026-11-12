# Project Application: bluez-pairing-agent in esp32-bt-analyzer

```yaml
project_id: esp32-bt-analyzer
tech_slug: bluez-pairing-agent
status: draft
sheet: ../../../technologies/bluez-pairing-agent/SHEET.md
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

## Rolle im Projekt

Die D1 sind über HCI-TCP reine Controller; bluetoothd auf .108 führt das
Pairing für beide. Handy → .131 und HU → .87 beginnen die Kopplung selbst, also
braucht .108 einen dauerhaften Default-Agenten. Port des PiDrive-Agenten, erweitert
auf mehrere Adapter, die über ihre BD-Adresse erkannt werden (hci-Index wechselt
bei jedem Bridge-Reconnect).

## Architektur / Datenfluss

```text
Handy ──SSP──► .131 ─HCI/TCP─► bluetoothd .108 ◄─HCI/TCP─ .87 ◄──SSP── HU
                                   │ RequestConfirmation
                                   ▼
                    bt_pair_agent.py (DisplayYesNo, Regel, Trust)
                                   │ state/events
                                   ▼
                    Lab UI :8081 Karte „Pairing“ (SSH)
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `tools/bt_pair_agent.py` | Agent, `--status`, `--open-window` |
| `tools/bt-pair-agent.service` | Dienst, Adapter-Specs (BD=Rolle:Alias) |
| `tools/lab_pair_agent.py` | deploy / status / window / remove |
| `controller/pairing.py`, `web/app.js` | UI-Karte |
| `docs/PAIRING.md` | Kontrollaufteilung, Ablauf |

## Konfiguration und Parameter

| Adapter | Spielt | Alias | Class (Soll) |
|---------|--------|-------|--------------|
| .131 `C8:C9:A3:CB:7B:0A` | Autoradio fürs Handy | BT-Analyzer-Car | `0x200420` |
| .87 `C8:C9:A3:CB:37:96` | Smartphone für die HU | BT-Analyzer-Phone | `0x5A020C` |

Nicht konfigurierte Adapter auf .108 nur mit offenem Fenster (Abweichung zu PiDrive).

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| Vorheriges `ensure_agent()` (bluetoothctl-Einzelbefehl) registrierte keinen bleibenden Agenten | — | `FACT` (Code-Review) |
| A4 Handy/Kopfhörer gekoppelt — wer die Rückfrage beantwortete, ist nicht dokumentiert | `LAB_HCI_TCP_A1A5_20261111T204600Z` | `UNKNOWN` |
| Agent auf .108 beantwortet Handy- und HU-Kopplung | — | `UNKNOWN` (nicht deployt, .108 vom Desk nicht erreichbar) |
| HU akzeptiert Just Works von .87 | — | `UNKNOWN` (PiDrive: Numeric Comparison funktioniert) |

## Offene Fragen

- Bleibt die per `hciconfig` gesetzte Class nach Power-on (`cls_ok` im Status)?
- Filtert iDrive die Geräteliste nach Class of Device?

## Verwandte Applications / Methods

- [pidrive bluez-pairing-agent](../../pidrive/applications/bluez-pairing-agent.md) (Vorlage, Feldtest)
- [bmw-bcl](bmw-bcl.md) (B0.7/B2 brauchen den Agenten)
