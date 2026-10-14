# KB Meta-Audit: messtechnisch bestimmte Fakten · 2026-10-14

**Standard:** 0.7.1  
**Kampagne:** [`technology-audit-2026-kb-measured`](../../audits/technology-audit-2026-kb-measured/)  
**Projekt:** [`technology-audit-kb`](../../projects/technology-audit-kb/)  
**Snapshot:** `5fab7f5`

## Verdict

Die KB **hat** einen echten Messkern — vor allem PiDrive/NBT (Feld+Lab) und
Ergo/FTMS/HR (Lab/Geräte). Zahlenmäßig dominieren aber Desk-`FACT` und offene
Fremd-Kampagnen; ohne Index wirkt die Basis „voll“, der **MEASURED**-Anteil bleibt
schwer sichtbar.

## Lage in Zahlen (Scan)

| Größe | Wert |
|-------|------|
| Unique Evidence-IDs (grob) | ~439 |
| Unique `MEASURED`-IDs | ~28 |
| Token in evidence.md | ~383 FACT · ~36 MEASURED-Vorkommen · ~110 UNKNOWN |
| Audits | ~50 active · ~7 closed |
| Sheet `field_evidence` | 49× R0 · 1× R3 (`bmw-nbt-evo`) |
| Apps `field_evidence` ≥ R3 | 10 |

## Messkerne (wo die Fakten herkommen)

1. **PiDrive / BMW NBT Evo** — Prefetch, Seed, C′, Lab≠Ohr, Busy-Pacing (~65 s vs. ~6 s Stall-off). Artefaktlinks in Ursprungsrepo.  
   Kampagnen: [`pidrive-2026-bmw-hu`](../../audits/pidrive-2026-bmw-hu/), [`pidrive-2026-msc`](../../audits/pidrive-2026-msc/).
2. **Ergo / FTMS-Probe / Heartrate** — Varon-Caps, Resistance, Scan, Polar H9.  
   Kampagnen: ergo / ftmsprobe / heartrate Pilots.

Epistemik-Stichprobe: Host-ms und Busy-Akzeptanz bleiben **C**/`MEASURED`; Sheet
`usb-msc` übernimmt sie nicht als A-FACT — Hygiene passt.

## Was schief wirkt (ohne den Messkern zu leugnen)

| Beobachtung | Bedeutung |
|-------------|-----------|
| Desk-Boom 13.–14.10. | Mehr FACT/UNKNOWN, kein neues MEASURED |
| Kein MEASURED-Ledger | „Wir haben gemessen“ ist wahr, aber nicht navigierbar |
| 50 active Kampagnen | PILOT-Warnung; Messkerne unter Desk-Rauschen |
| README-only MEASURED | Härtegradient (PL2) bei Teilen Heartrate |
| Sheet-R0 | **kein Bug** — Feld gehört in Applications |

## Empfohlene nächste Ops (kein neues Fremd-Audit)

1. Zentralen **MEASURED-Index** (ID → Claim → Lab/Feld → App).
2. Desk-complete Kampagnen **schließen**.
3. Schwache MEASURED **härten oder downgraden**.
4. README/KB-FIT: Kurzpfad „Messkerne“ (pidrive HU, ergo/ftms).

## Evidence

`EVID-KBMEAS-2026-10-14-001`–`008` in
[`audits/technology-audit-2026-kb-measured/evidence.md`](../../audits/technology-audit-2026-kb-measured/evidence.md).
