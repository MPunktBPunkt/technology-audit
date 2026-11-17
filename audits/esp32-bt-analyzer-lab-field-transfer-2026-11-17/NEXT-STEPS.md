# Nächste Schritte — Lab→Feld-Transfer (Stand 2026-11-17, post-`1100644`)

Epistemik: Feld > Lab > Desk. Lab beweist Protokoll + eigene Sink-Verdrahtung,
**nicht** F20-Resource-Auth und **nicht** F20-Action-/Model-Semantik.

Transport/write11/W0: **geschlossen (Lab)** — nicht erneut als P0 öffnen.

---

## P0 — vor kontrolliertem F20-Versuch

| # | Schritt | Ziel | Origin | Abhängigkeit |
|---|---------|------|--------|--------------|
| P0.1 | **Claim-Grenze einhalten** | Jeder Lauf: LAB FACT vs FIELD OPEN explizit; kein Lab-PASS→Auto | docs | dieser Audit |
| P0.2 | **Resource-Auth / Digest-Match** | Nur Bytes mit SHA-256 in `SAS.Digests.*` des APP-Certs; Miss→setResource | desk×lab; Feld-Korrelation OPEN | OEM-`*.p7b` + Packs |
| P0.3 | **F20 Resource-Lifecycle beobachten** | Hit/Miss DESCRIPTION/TEXTDB/IMAGEDB; kein setResource nach `true` erzwingen | f20-field | SAS ok; Relay/Hex wenn möglich |
| P0.4 | **F20 Action-/Model-IDs gewinnen** | actionId/handle/modelId aus DESCRIPTION oder Relay — **nicht** Lab-200/100 | f20-field | P0.3 |
| P0.5 | **Action→PiDrive mit Feld-IDs** | Ein paced onAction→ack→eigene Sink; Lab-`PI_DRIVE_TEST` nur als Muster | f20-field | P0.4 |

---

## P1 — parallel / Nebenpfade

| # | Thema | Warum |
|---|-------|-------|
| P1.1 | modelId 4 / SE 213 | Validierung vs Bug; blockiert Pfad nicht |
| P1.2 | Transparent RFCOMM-Relay für Phone→HU Hex | setResource/setData/Action-Bodies |
| P1.3 | SE Feld voll dekodieren (errorCode) | 213 vs andere |
| P1.4 | Autonomer Client mit SAS | Unabhängigkeit Phone-App |

---

## P2 — Dimensionierung (kein Blocker)

| # | Thema | Warum |
|---|-------|-------|
| P2.1 | EAGAIN-Histogramm / Retry-Budget | `BCL_WRITE_EAGAIN_S=2.0` kalibrieren; Backpressure-Quelle |
| P2.2 | Dual-ESP Coex/ACL | Lab ohne USB; derzeit sekundär |

---

## Explizit nicht P0 / nicht wieder öffnen

- write11- / Panic- / Dual-ESP-Ursachenkette (Lab: TX-pressure + fail-fast; Retry Default).
- W0 „HU erzeugt keinen Reply“ (Fall A `REJECTED`).
- FREEZE_C5CB0E6 ESP/RFCOMM als Connected-P0 (`SUPERSEDED`).
- Weitere Model-ID-Sammlungen ohne Feld-Hex.
- Erneute 10‑min-Soak ohne neues Protokollziel.
- A2DP-only als RHMI-Ersatz; actionId **200** als F20-universal.

---

## Referenzen

- Dieser Audit: [`README.md`](README.md)
- Prior Connected Freeze: [`../esp32-bt-analyzer-f20-connected-2026-11-17/`](../esp32-bt-analyzer-f20-connected-2026-11-17/)
- Desk Resource: [`../bimmergestalt-rhmi-checkresource-2026-11-17/`](../bimmergestalt-rhmi-checkresource-2026-11-17/)
- Upstream: `LAB_P0_RHMI_PIDRIVE_SEQ_PASS`, `LAB_P0_RHMI_SOAK_PASS`, `LAB_P0_WRITE11_MASTER` @ `1100644`
