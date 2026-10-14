# Audit Campaign: esp32-s3-usb-wifi-coexistence-2026

```yaml
id: esp32-s3-usb-wifi-coexistence-2026
project_id: hu-probe
started: 2026-10-14
ended: 2026-10-14
status: closed
profile: lab-tool
standard_version: "0.7.1"
tech_slug: esp32-s3-usb-wifi-coex
reuse_outcomes:
  reused: [usb-msc]
  new: [esp32-s3-usb-wifi-coex]
  not_helped:
    - "esp-faq coexistence.rst = WiFi↔BT, nicht USB."
    - "usb_dongle zeigt Gleichzeitigkeit, nicht Bulk-Last."
    - "IDF-Issues ≠ Root-Cause der Sonde."
  process: "Enges Desk: Coex-unter-Last-Karte (Task/Core/Prio + PHY/BBPLL + Diskriminierungs-Messplan); keine Ursachenbehauptung."
  decisions_touched: [no-bulk-kill-as-fact, idf-issue-not-probe-cause, lab-discrimination-next]
```

## Ziel

Navigationskarte für **ESP32-S3 · USB OTG Device (MSC Bulk) · WiFi STA+TCP unter Last**:
bekannte PHY/Start-Interaktionen, Default-Task/Core/Prio (Arduino-Pin vs. esp-usb),
Abgrenzung zu BT-Coex — **ohne** Root-Cause für hu-probe 0.2.15.

## Scope

- **Im Scope:** esp-idf Issues #7957/#8241/#15079 (+ #12185 Kontext); WiFi-/SMP-/PHY-Kconfig;
  USB-OTG vs. Serial-JTAG PHY-Doku; esp-usb `tinyusb_task`; Arduino-ESP32 2.0.11
  (hu-probe PlatformIO-Pin); esp-faq Coex-Abgrenzung; usb_dongle als Existenz-Referenz;
  Hypothesen-Register + Diskriminierungs-Messplan.
- **Nicht im Scope:** Root-Cause-Claim; Fix-Implementierung; Wire-/NBT-Capture; S1–S3;
  Power-Lab-Ergebnisse; Ersetzen der Capture-Flush-Architektur.

```text
kill: "USB-Bulk verursacht WiFi-Tod" als FACT; IDF-Issue = unsere Sonde
```

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Evidence-IDs auf immutable SHAs / Issue-IDs | erfüllt |
| 2 | Tabelle Default-Prio + Core: WiFi / TinyUSB / tcpip / Arduino | erfüllt |
| 3 | S3 PHY/BBPLL/USB-Start-Interaktionen dokumentiert | erfüllt |
| 4 | Messplan Power vs. Starve vs. RF (ohne Ergebnis) | erfüllt |
| 5 | Explizit: keine Ursache für hu-probe 0.2.15 | erfüllt |
| 6 | C10–C13 Desk; Sheet + Method + Application | erfüllt |

## Decision Trace

| Entscheidung | Benötigte Frage | Evidence-ID | Konsequenz | Wissenszeitpunkt |
|--------------|-----------------|-------------|------------|------------------|
| Neuer Slug `esp32-s3-usb-wifi-coex` statt nur `usb-msc` wachsen | Ist Coex A-Wissen oder nur MSC? | Kampagnenziel | Ja — eigener Navigations-Slug; `usb-msc` reused | `KNOWN BEFORE TEST` |
| Arduino-Pin (2.0.11) als Primär-Default-Tabelle | Reicht esp-usb HEAD? | `010`–`012`, `016` | Nein — hu-probe läuft Arduino-HAL, nicht esp-usb Task-API | `DISCOVERED DURING TEST` |
| Lab-Diskriminierung vor weiteren Hub-Drosseln | Reicht App-Mitigation? | Kontext 0.2.15; H1–H5 | Nein — Matrix Power/Starve/RF | `KNOWN BEFORE TEST` |
| IDF-Issue nicht als Kill-Ursache | Belegen Issues unsere Sonde? | `001`–`003`, Grenzen | Nein | `KNOWN BEFORE TEST` |

## Engineering Review Checks

| Evidence-ID | Review Check | Wissenszeitpunkt |
|-------------|--------------|------------------|
| `010`, `007` | Vor Prio-Experimenten: Ist `usbd` wirklich prio 24 / WiFi 23 im laufenden Image? (`uxTaskPriorityGet`) | `DISCOVERED DURING TEST` |
| `005`, `012` | `CONFIG_ESP_PHY_ENABLE_USB` im Build verifizieren — nicht annehmen | `DISCOVERED DURING TEST` |
| `009` vs `010` | Keine esp-usb-Kconfig-Annahmen auf Arduino-Pfad übertragen | `DISCOVERED DURING TEST` |
| Hypothesen | Kein Merge von H1–H5 zu einem FACT-Satz in Commit-Messages/Docs | `KNOWN BEFORE TEST` |

## Kill-Kriterien

Präregistriert für künftigen Lab (**C12**); hier kein Messlauf.

**Hypothese (Lab):** Unter kontrollierter Diskriminierung lässt sich Power vs. CPU-Starve
vs. RF als dominanter Faktor eingrenzen — nicht „Bulk killt WiFi“ als Desk-Wahrheit.

| # | Kill / Widerlegt wenn | Status |
|---|----------------------|--------|
| 1 | Desk behauptet „USB-Bulk verursacht WiFi-Tod“ als FACT | Integritäts-Kill |
| 2 | IDF-Issue als Root-Cause von hu-probe 0.2.15 verkauft | Integritäts-Kill |
| 3 | Lab: Assoc stirbt auch bei OTG ab / ohne Host-Traffic genauso → „unter Last“-Framing falsch | präregistriert |
| 4 | Lab: externe 5 V + gleiche Software → Tod verschwindet → Power-Pfad priorisieren (H3) | präregistriert |
| 5 | Lab: WiFi-Task-Runtime bleibt hoch, Assoc stirbt trotzdem → reine CPU-Starve unwahrscheinlich | präregistriert |

## Genutzte Methoden

| Method | Pfad |
|--------|------|
| USB↔WiFi Diskriminierung | [`usb-wifi-coex-discrimination`](../../methods/usb-wifi-coex-discrimination.md) |
| Power/Reset-Isolation (Reuse) | [`plug-power-reset-isolation`](../../methods/plug-power-reset-isolation.md) |

## Bezug Inventar

- Projekt: [`hu-probe`](../../projects/hu-probe/)
- Sheet: [`esp32-s3-usb-wifi-coex`](../../technologies/esp32-s3-usb-wifi-coex/SHEET.md)
- Application: [`applications/esp32-s3-usb-wifi-coex.md`](../../projects/hu-probe/applications/esp32-s3-usb-wifi-coex.md)
- Reuse: [`usb-msc`](../../technologies/usb-msc/SHEET.md)
- Vorläufer-Hypothese: [`usb-control-stall-recovery-2026`](../usb-control-stall-recovery-2026/) `EVID-USBCTRL-…-009`

## Ergebnisse

- [`evidence.md`](evidence.md) — `EVID-USBWIFI-2026-10-14-*`
- Bericht: [`docs/reports/2026-10-14-esp32-s3-usb-wifi-coexistence.md`](../../docs/reports/2026-10-14-esp32-s3-usb-wifi-coexistence.md)

## Knowledge Feedback

**C13:** n/a Lab/Field — Desk-only. Rückkanal: Sheet A + Application B (Pin) + Method.

| Ergebnis | Evidence-ID | Zurück in |
|----------|-------------|-----------|
| Coex-Karte Desk | `001`–`016` | Sheet · Application · Method |

## Review C10–C13

| Check | Ergebnis |
|-------|----------|
| C10 Decision Trace | PASS |
| C11 Engineering Review Checks | PASS |
| C12 präregistrierte Kill-Kriterien | PASS; Messlauf offen |
| C13 Knowledge Feedback | n/a dokumentiert |

## Lessons → Transfer

- S3 USB↔WiFi ist **offiziell heikel** (PHY/BBPLL, Start-Interferenz) — das ist Korrelation, kein Sonde-Verdict.
- Arduino 2.0.11: `usbd` prio **24** > WiFi **23** — Strukturfakt für Starve-Hypothesen.
- BT-Coex-Doku nicht auf USB anwenden.
- Nächster Schritt ist Lab-Diskriminierung, nicht weitere reine Hub-Drossel-Docs.

## Offene Punkte nach Abschluss

- Lab nach Method `usb-wifi-coex-discrimination`
- Runtime-Prios im hu-probe-Image bestätigen
- Auto-HU: derselbe Kill? (Feld, nach Lab)
