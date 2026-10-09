# Technology Sheet: ioBroker MB Repository Manager

```yaml
slug: iobroker-mbrepository-adapter
title: ioBroker MB Repository Manager
primary: F
tags: [iobroker, nodejs]
type: component
status: active
seen_in: [iobroker-mbrepository]
maturity:
  technology: R3
  implementation: R0
  field_evidence: R0
  reusability: W2
pilot: audits/iobroker-mbrepository-2026-pilot
```

## Kurzfassung

Ops-Adapter: **eigene GitHub-Adapter-Repos** scannen, Versionen vergleichen und Install/Upgrade/Downgrade aus dem Browser anstoßen — ergänzt den offiziellen Catalog, ersetzt ihn nicht.

## Abgrenzung

- **Ist:** GitHub→Host Install-Workflow + UI.
- **Ist nicht:** `ioBroker.repositories` / sources-dist (offizielle Liste); npm Registry selbst.

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Gleich official latest repository | `REJECTED` | privater Account-Scan |
| Install-API ohne Auth LAN-unkritisch | `REJECTED` | Remote-Code-Install-Risiko |
| Case der Repo-Namen egal überall | `HYPOTHESIS` | Adapter dokumentiert case-insensitive Find |

### Projektstart-Checkliste

- [ ] GitHub User/Token Rate-Limits
- [ ] sudo / Install-Rechte
- [ ] Abgrenzung zu Catalog-PRs
- [ ] Application + `seen_in`
