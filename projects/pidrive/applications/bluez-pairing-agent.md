# Project Application: bluez-pairing-agent in PiDrive

```yaml
project_id: pidrive
tech_slug: bluez-pairing-agent
status: active
sheet: ../../../technologies/bluez-pairing-agent/SHEET.md
maturity:
  technology: R3
  implementation: R3
  field_evidence: R2
  reusability: W3
```

## Rolle im Projekt

Der BMW (NBT Evo) beginnt die Kopplung selbst. Ein eigener Dienst
`pidrive_btagent` beantwortet sie über D-Bus, unabhängig vom PiDrive-Kern
(überlebt Kern-Neustarts, läuft vor dem Kern, berührt die GLib-Schleife von
`mpris2.py` nicht).

## Architektur / Datenfluss

```text
BMW Inquiry → SDP (0x110A, 0x110C) → Numeric Comparison
  → bluetoothd → RequestConfirmation → bt_agent_dbus.py (Regel) → yes
  → Link-Key + Trusted → A2DP + AVRCP
```

## Relevante Pfade

| Pfad (Ursprungsrepo) | Rolle |
|----------------------|-------|
| `pidrive/modules/bluetooth/bt_agent_dbus.py` | Agent (DisplayYesNo, Regel, Trust, Ereignisse) |
| `systemd/pidrive_btagent.service` | Dienst, `PIDRIVE_BT_CONFIRM` |
| `docs/fahrzeug/iDriveBt.md` §8 | Pairing-Ablauf |
| `docs/archiv/fahrzeug/BMW-BT-FELDTEST-2026-09-16.md` | Feldtest mit Fotos |

## Konfiguration und Parameter

| Key | Wert | Status |
|-----|------|--------|
| Capability | `DisplayYesNo` | `FACT` (Code) |
| Regel | `always` (Vorgabe), `window` über `/tmp/pidrive_bt_pair_window` | `FACT` (Code) |
| DiscoverableTimeout / PairableTimeout | 0 | `FACT` (Code) |
| Audio-UUIDs ohne Rückfrage | 0x110A–0x110F, AVDTP, AVCTP | `FACT` (Code) |

## Ebene C — Host- / Feld-Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| BMW nutzt Numeric Comparison; Passkey im iDrive bestätigt, Gerät danach gelistet | Kandidat ohne ID (Feldtest 2026-09-16, „BMW 38304“) | `MEASURED` |
| Alter bluetoothctl-Agent beantwortete BMW-initiierte Kopplung nicht | Kandidat ohne ID (Docstring `bt_agent_dbus.py`) | `FACT` (Projekt-Doku) |
| BMW verbindet ~30 s nach Zündung neu | Kandidat ohne ID (Dienst-Kommentar) | `HYPOTHESIS` |

## Abweichungen vom „Lehrbuch“

Unbekannte Regel wird wie `always` behandelt (bewusst: erste Kopplung darf nicht an der Regel scheitern).

## Verwandte Applications / Methods

- [esp32-bt-analyzer bluez-pairing-agent](../../esp32-bt-analyzer/applications/bluez-pairing-agent.md) (Port für mehrere Adapter)
- [bmw-nbt-evo](bmw-nbt-evo.md)
