# Method: KB Cross-Check / Blindtest

```yaml
slug: kb-cross-check
title: KB Cross-Check / Blindtest
status: active
tags: [quality, reuse]
```

## Zweck

Prüfen, ob Technology Sheets und Evidence als **Reasoning-Bausteine** nutzbar sind — nicht ob ein Modell denselben Fließtext produziert.

## Voraussetzungen

- Aktueller Repo-Stand (Commit bekannt)
- Klare Fragestellung (z. B. „Kann daraus ein ESP32-S3-FM-TX abgeleitet werden?“)
- Erlaubte Pfade (Sheets/Evidence/Apps) — Blindtest: **ohne** vorgegebene Zielarchitektur

## Ablauf

1. Prompt aus [`templates/prompts/kb-cross-check.md`](../templates/prompts/kb-cross-check.md) füllen.
2. Primärquelle = Audit-Repo; externe Docs nur gekennzeichnet.
3. Antwort muss FACT / INFERRED / HYPOTHESIS / UNKNOWN / REJECTED trennen.
4. Auswerten gegen Checkliste (unten); Absolutismen und Varianten-Transfers markieren.
5. Prozess-Delta (Checks, FOLLOW-ON, Sheet-Schärfung) — **nicht** fehlende Messung durch Text ersetzen.

## Artefakte

- Prompt unter `artifacts/prompts/kb-cross-check-…`
- Kurze Auswertungsnotiz (Kampagne Lessons oder `docs/KB-FIT.md`-Update)
- Optional: geschärfte Sheet-Fallstricke / Gates

## Pass / Fail

| Prüfaspekt | Pass | Fail |
|------------|------|------|
| Reproduzierbarkeit | gleiche FACT-Kerne aus Sheets | widersprüchliche „Facts“ ohne Quelle |
| Transfer-Bremse | Chip-Variante nicht automatisch übernommen | „ESP32 ⇒ S3“ ohne Gate |
| Epistemik | UNKNOWN dort, wo Lab fehlt | erfundene Messwerte |
| Absolutismen | als zu stark erkannt | „einziger Kandidat“ unwidersprochen übernommen |
| Architektur | aus Evidence abgeleitet oder als Hypothese | als bewiesen verkauft |

## Fallstricke

- Prompt verrät die gewünschte Architektur (kein echter Blindtest)
- Nur Zusammenfassung statt Ableitung
- Neues Sheet aus Hypothese ohne Gate

## Beispiel-Einsätze

| Projekt / Audit | Link / Hinweis |
|-----------------|----------------|
| 2026-10-11 ESP-FM Cross-Check | Prompt gegen `pi-fm-tx` + Hub; Ergebnis → Standard 0.6.6 + Audit `esp-fm-tx` |
| 2026-10-11 Pi-FM Revalidation | `pi-fm-tx-2026-foreign` unter 0.6.6; [DELTA](../audits/pi-fm-tx-2026-foreign/DELTA.md) |
