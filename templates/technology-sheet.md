# Technology Sheet: \<Name\>

```yaml
slug: example-tech
title: Example Technology
primary: C
tags: [example-tag]
type: protocol   # technology | protocol | format | implementation | pattern
status: draft    # draft | active | deprecated
seen_in: []      # kanonische project_id, z.B. [pidrive] — nie projects/…
maturity:
  technology: R0
  implementation: R0
  field_evidence: R0
  reusability: W0
```

Nur Ebene **A** (allgemein). Projekt- und Host-Details gehören in die Project Application (B/C).

## Kurzfassung

1–3 Sätze: Was ist das, wofür braucht man es?

## Abgrenzung

- **Ist:** …
- **Ist nicht:** …

## Schnittstellen und Abhängigkeiten

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | … | … |
| unten | … | … |

## Typische Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| … | `FACT` / `HYPOTHESIS` / `REJECTED` | … |

## Transfer

Wann und wie lässt sich dieses Wissen in ein anderes Projekt übernehmen?

### Projektstart-Checkliste

- [ ] Sheet gelesen (Abgrenzung + Fallstricke)
- [ ] Entscheiden: bestehender Slug wiederverwenden vs. neuer Slug (Begründung)
- [ ] Application anlegen; nur B/C hier, kein A-Copy-Paste
- [ ] `seen_in` im Sheet ergänzen, wenn Application steht
- [ ] Offene Fragen aus dem Sheet, die dieses Projekt klären kann, notieren

## Referenzen

- Specs / Docs / RFCs
- Interne Quellrepos (nur Links, keine Rohdumps)

## Offene Fragen

- …

## Abweichungen

_(nur wenn nötig)_
