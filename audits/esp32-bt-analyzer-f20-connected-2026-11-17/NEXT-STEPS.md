# Nächste Schritte (gemeinsam aus Audit A + B) — Stand 2026-11-17

> **Superseded for prioritization:** nach Lab Soak/Seq PASS siehe
> [`../esp32-bt-analyzer-lab-field-transfer-2026-11-17/NEXT-STEPS.md`](../esp32-bt-analyzer-lab-field-transfer-2026-11-17/NEXT-STEPS.md)
> (Feld-Auth/Action-Semantik zuerst; write11/W0 nicht reopen).

Experimentplan-Mapping **W0–W5:** Watchdog → checkResource stabil → setResource →
initialize → setData(447) → Action.

Epistemik: Feld > Lab > Desk. Lab beweist Protokoll, **nicht** F20-Resource-Auth.

---

## P0 — kritisch für W0–W5

| # | Schritt | W | Ziel | Origin-Erwartung | Abhängigkeit |
|---|---------|---|------|------------------|--------------|
| P0.1 | **Watchdog Air stabil** | W0 | Kein `wd_echo_miss_limit` vor Etch-Ergebnis; WD-Echo-Policy an Wire (nicht nur Desk 5 s) | lab → dann f20-field | USB→`.131` PARTIAL-Fix; ggf. Phone-Client |
| P0.2 | **checkResource stabil wiederholen** | W1 | Deterministisch `result=true/false` mit bekanntem MD5 + Size + Type | lab / f20-field | P0.1; Auth-Session SAS ok |
| P0.3 | **Resource-Authorization / Digest-Match** | W2 | Nur Bytes deren SHA-256 in `SAS.Digests.*` des verwendeten APP-Certs steht; Cache-Miss → `setResource` | desk×lab; Feld-Korrelation OPEN | OEM-`*.p7b` + passende Resource-Packs (kein Blind-Upload) |
| P0.4 | **setResource → initialize** | W2–W3 | Nach Miss: Upload DESCRIPTION (dann TEXT/IMAGE laut App-Matrix); danach `rhmi_initialize(handle)` | lab zuerst, Feld beobachten | P0.3 |
| P0.5 | **setData(447) NowPlaying-Titel** | W4 | Ein kontrolliertes `setData(handle, 447, string)` nach init; kein ImageID←0 | lab (Codec-Fix beweist Decode); Feld braucht Hex/Relay | P0.4; Music RHMI aktiv (nicht A2DP-only) |
| P0.6 | **Action paced** | W5 | Ein `onActionEvent` → `ackActionEvent`; kein Flood | f20-field / lab | P0.5; Pace ≥80 ms (Lab-Lesson) |

**Hauptblocker über allen W2+:** Resource-Whitelist / APP_AUTH Digests.

---

## P1 — parallel / als Nächstes danach

| # | Thema | Warum |
|---|-------|-------|
| P1.1 | Transparent RFCOMM-Relay `.131`↔`.87` oder Host-HCI | Phone→HU Hex für setResource/setData-Korrelation |
| P1.2 | Digest-Korrelation Feld-Uploads ↔ p7b `SAS.Digests.*` | Whitelist am F20 beweisen |
| P1.3 | Dual-ESP Air-RFCOMM nach Coex/ACL-Härtung | Lab ohne USB-Dongle; derzeit FAIL trotz 0.3.20 |
| P1.4 | ServiceException Feld voll dekodieren (errorCode jenseits Byte 32) | 213 vs andere Ursachen |
| P1.5 | Screen-Mirror JPEG-Inhalt auf Wire | Burst von STRONG → FACT |
| P1.6 | Autonomer Pi-/Host-Client mit SAS | Unabhängigkeit von MyBMW/AAIdrive |
| P1.7 | USB-AOA→BCL am F20 | Alternativtransport |
| P1.8 | HU Watchdog-Timeout messen | W0-Parameter für eigene Clients |

---

## Explizit nicht P0

- A2DP-only Browse als RHMI-Ersatz (Lab `BROWSE_2002` widerlegt).
- Dual-ESP als einziger Pfad für W0–W5 (USB/Phone zuerst).
- HU `verifyResource`-Patch (Community-nur; Security-/Scope-Grenze).
- Spekulation „beliebige DESCRIPTION hochladen“ ohne Digest-Match.

---

## Referenzen

- Audit A: [`../bimmergestalt-rhmi-checkresource-2026-11-17/`](../bimmergestalt-rhmi-checkresource-2026-11-17/)
- Audit B: [`README.md`](README.md)
- Upstream Evidence: `LAB_P0P2_FW0320_RESULT_20261117`, `FIELD_RHMI_BROWSE_20261117`, `DEEP_FORENSIC_RHMI_SCREENMIRROR_20261117`
