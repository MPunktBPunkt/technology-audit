# Technology Sheet: BlueZ Pairing Agent (org.bluez.Agent1)

```yaml
slug: bluez-pairing-agent
title: BlueZ Pairing Agent (org.bluez.Agent1)
primary: C
tags: [bluez, classic-bt, linux-userspace]
type: pattern
status: draft
seen_in: [pidrive, esp32-bt-analyzer]
maturity:
  technology: R3
  implementation: R2
  field_evidence: R0
  reusability: W3
```

Nur Ebene **A**. Geräte-/HU-Verhalten und Feldtests stehen in den Applications.

## Kurzfassung

BlueZ entscheidet Pairing-Rückfragen (Secure Simple Pairing: Numeric Comparison,
Passkey, Autorisierung) nicht selbst, sondern fragt einen über D-Bus registrierten
**Agenten** (`org.bluez.Agent1`, `AgentManager1.RegisterAgent` +
`RequestDefaultAgent`). Für headless Hosts (Pi, Proxmox, Car-Gateway) muss das ein
dauerhaft laufender Dienst sein, sonst scheitert jede vom Gegenüber begonnene Kopplung.

## Abgrenzung

- **Ist:** Host-seitige Pairing-Policy: IO-Capability, Bestätigungsregel, Trust, Service-Autorisierung.
- **Ist nicht:** SSP-Kryptografie im Controller; Link-Key-Speicherung (bluetoothd, `/var/lib/bluetooth/<Adapter-BD>/`); BLE-SMP-Details; Profilverbindung (A2DP/AVRCP) nach dem Pairing.

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Bestätigungsregel / UI | always · window · never; Passkey-Anzeige für den Menschen am Gegenüber |
| unten | bluetoothd `AgentManager1` | ein Default-Agent pro bluetoothd, gilt für **alle** Adapter |
| lateral | `Device1.Trusted` | ohne Trust fragt BlueZ bei jedem Reconnect erneut (AuthorizeService) |
| lateral | `Adapter1` Discoverable/PairableTimeout | Vorgabe 180 s; headless meist 0 |

## IO-Capability → SSP-Verfahren

| Agent-Capability | Gegenüber mit Display + Ja/Nein | Ergebnis |
|------------------|----------------------------------|----------|
| `DisplayYesNo` | Numeric Comparison | `RequestConfirmation(passkey)`; beide Seiten bestätigen |
| `KeyboardDisplay` | Numeric Comparison / Passkey Entry | je nach Gegenüber |
| `NoInputNoOutput` | Just Works | keine MITM-Protection; Gegenüber mit MITM-Anforderung kann ablehnen |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| `bluetoothctl agent X` als Einzelbefehl registriert einen dauerhaften Agenten | `REJECTED` | Agent lebt nur so lange wie der bluetoothctl-Prozess |
| Interaktive bluetoothctl-Sitzung beantwortet auch fremd-initiierte Kopplungen | `REJECTED` | nur wenn jemand die Prompts liest; per Pipe gesteuert landen Rückfragen ungelesen |
| Zwei Agenten mit `RequestDefaultAgent` koexistieren sauber | `REJECTED` | der zuletzt anfragende gewinnt; welcher fragt, wird zufällig |
| Ein `Pair()` nutzt immer den Default-Agenten | `REJECTED` | hat der aufrufende D-Bus-Client selbst einen Agenten, wird dieser gefragt (bluetoothctl-Sitzung); `busctl`/Einzelbefehl ohne eigenen Agenten → Default |
| Nach `Paired=true` ist alles erledigt | `REJECTED` | ohne `Trusted` erneute Autorisierung bei Profilverbindungen |
| Class of Device ist pro Adapter per D-Bus setzbar | `REJECTED` | `Adapter1.Class` read-only; `main.conf` global; pro Adapter nur per HCI (`hciconfig class`), bluetoothd ergänzt Service-Bits |
| Link-Keys hängen an `hciN` | `REJECTED` | an der Adapter-BD; Indexwechsel behält die Kopplung |

## Transfer

Jeder headless BlueZ-Host, mit dem ein Auto, Handy oder Kopfhörer von sich aus
koppelt. Muster: eigener systemd-Dienst (unabhängig vom App-Kern), DisplayYesNo,
Regel mit Zeitfenster, Trust nach Bestätigung, Ereignisprotokoll mit Passkey.

### Projektstart-Checkliste

- [ ] Wer beginnt die Kopplung (Host oder Gegenüber)?
- [ ] Capability passend zum Gegenüber (MITM-Anforderung?)
- [ ] Nur ein Default-Agent auf dem Host (keine konkurrierende bluetoothctl-Sitzung)
- [ ] Trust nach Kopplung, Discoverable/PairableTimeout bewusst gesetzt
- [ ] Passkey sichtbar für die Person am Gegenüber (Log/UI)
- [ ] Mehrere Adapter: Policy pro Adapter-BD, nicht pro `hciN`
- [ ] Application + `seen_in`

## Referenzen

- BlueZ `doc/org.bluez.Agent.rst`, `doc/org.bluez.AgentManager.rst`, `test/simple-agent`
- Bluetooth Core Spec Vol 3 Part C §5.2.2 (SSP association models)
- PiDrive `pidrive/modules/bluetooth/bt_agent_dbus.py`; esp32-bt-analyzer `tools/bt_pair_agent.py`

## Offene Fragen

- Fallback-Verhalten von bluetoothd, wenn der Default-Agent sich abmeldet (nächster registrierter Agent vs keiner) — Version prüfen.
- Hält eine per HCI gesetzte Class of Device einen Power-Zyklus durch bluetoothd? (`UNKNOWN`)
