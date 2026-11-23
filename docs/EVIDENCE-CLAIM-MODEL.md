# Evidence / Claim Model (Retrieval Layer)

```yaml
status: active
standard_from: "0.7.2"
role: machine-readable evidence graph over existing SoT
```

Ziel: bei 50–100+ Audits **zuverlässig** die richtige Evidenz finden — inkl. negativer Evidence, Scope und Transfer-Grenzen — ohne eine zweite Wahrheitsdatei (`AI_KNOWLEDGE.md` ist **verboten**).

Wahrheit bleibt:

```text
SHEET / APPLICATION / AUDIT (+ optional claims.yaml)
        ↓  generate
 generated/retrieval/*   und   audits/INDEX.yaml
        ↓
       AI
```

## 1. Stabile IDs

| Art | Format | Stabilität | Beispiel |
|-----|--------|------------|----------|
| **Audit-ID** | `A-YYYY-NNN` | immutable (Index-assigniert) | `A-2026-087` |
| **Directory name** | `<project>-<year>-<topic>` | identifier, nicht Beschreibung | `bmw-sas-auth-field-crypto-2026-11-21` |
| **Display name** | frei in README | mutable | „SAS Field Crypto Closure“ |
| **Evidence-ID** | `EVID-<DOMAIN>-…` | immutable in Audit | `EVID-B3-SAS-CRYPTO-18-18` |
| **Claim-ID** | `C-<DOMAIN>-NNN` | immutable in `claims.yaml` | `C-SAS-001` |

**Regel:** Audit-IDs und Evidence-IDs ändern sich nicht, wenn Ordner-/Display-Namen sich später ändern. Bestehende Ordner **nicht** massenhaft umbenennen (P3).

Empfohlene Evidence-Form (neu):

```text
EVID-YYYY-<DOMAIN>-NNN
```

Bestehende IDs (`EVID-B3-…`, `EVID-SAS-2026-11-06-001`, …) bleiben gültig.

## 2. Epistemic Status

| Status | Bedeutung |
|--------|-----------|
| `FACT` / `MEASURED` | belegt (Desk/Lab/Field je Scope) |
| `INFERENCE` | abgeleitet, nicht direkt gemessen |
| `HYPOTHESIS` | prüfbar, offen |
| `UNKNOWN` | unklar — **mit reason** |
| `REJECTED` | widerlegt / nicht übernehmen |
| `NOT_PROVEN` / `NOT_OBSERVED` | negativ/abwesend in Capture |
| `OPEN` | bewusst offener Implementierungs-/Feldpunkt |
| `SUPERSEDED` | durch neuere Evidence ersetzt |

### UNKNOWN reasons (Pflicht bei neuen Claims)

| reason | Bedeutung |
|--------|-----------|
| `no_field_capture` | nicht im Feld gemessen |
| `protocol_not_observed` | in Capture nicht gesehen |
| `insufficient_sample_count` | zu wenig Samples |
| `conflicting_evidence` | widersprüchliche Belege |
| `implementation_unknown` | Mechanik bekannt, eigener Build fehlt |
| `scope_not_transferable` | nur unter anderem Scope belegt |
| `other` | Kurztext in `reason_note` |

## 3. Claim → Evidence Relation

Optional pro Audit: `audits/<dir>/claims.yaml`

```yaml
claims:
  - id: C-SAS-001
    statement: "18/18 HU-accepted SAS logins verify against TouchCommand leaf"
    status: FACT
    environment: field
    scope:
      vehicle: BMW F20
      hu: NBT Evo
      transport: BCL/RFCOMM
      protocol: SAS/APP_AUTH
    supported_by: [EVID-B3-SAS-CRYPTO-18-18]
    contradicted_by: []
    limited_by: [host_specific_f20]
    transfer_limits:
      - not_standalone_signer
      - leaf_pubkey_only
    unknown_reason: null
```

Relationen:

| Feld | Bedeutung |
|------|-----------|
| `supported_by` | stützt den Claim |
| `contradicted_by` | widerspricht / REJECTED-Beleg |
| `derived_from` | Claim-IDs, aus denen abgeleitet |
| `limited_by` | Scope-/Transfer-Tags |
| `transfer_limits` | was **nicht** generalisiert werden darf |

## 4. Scope-Block (standardisiert)

Für Field/Lab-Claims und Retrieval-Bundles:

```yaml
scope:
  vehicle: BMW F20          # optional
  hu: NBT Evo               # host
  firmware: unknown         # optional
  transport: BCL/RFCOMM     # USB | BT | …
  protocol: SAS             # MSC | AOA | RHMI | …
  device: esp32-bt-analyzer # optional DUT
  environment: field        # lab | field | replay | mixed | desk
  project: esp32-bt-analyzer
```

Ohne Scope kein Transfer-FACT.

## 5. Generated Retrieval View

Erzeugt durch `python3 tools/ta-assist index` (Modul `retrieval`):

| Artefakt | Inhalt |
|----------|--------|
| [`audits/INDEX.yaml`](../audits/INDEX.yaml) | alle Audits: `audit_id`, dir, project, status, profile, techs, env |
| [`generated/retrieval/index.yaml`](../generated/retrieval/index.yaml) | Master: bundles + topics |
| [`generated/retrieval/bundles/<slug>.yaml`](../generated/retrieval/bundles/) | pro Tech/Topic: facts, rejected, unknowns, audits, apps, methods, transfer_limits |
| Topic-Seeds | [`docs/retrieval-topics.yaml`](retrieval-topics.yaml) — **Query-Specs**, keine zweite Claim-Wahrheit |

**Hand-edit von `generated/` und `audits/INDEX.yaml` ist verboten** — regenerieren.

## 6. AI Entry Path

1. Frage → `docs/retrieval-tests.yaml` / Topic-Seed / Tech-Slug  
2. Bundle unter `generated/retrieval/bundles/` lesen  
3. Nur dann Sheets/Audits tief lesen  
4. Immer `rejected` + `transfer_limits` + `unknowns` mitliefern  

Siehe Repo-Root [`AGENTS.md`](../AGENTS.md).

## 7. Was wir nicht tun

- Kein zentrales `AI_KNOWLEDGE.md`
- Keine Massen-Umbenennung alter Audit-Ordner
- Keine manuell gepflegten Duplikate der Sheet-Fallstricke in Bundles (Bundles = Ableitung)
- Keine Vektordatenbank-Pflicht
