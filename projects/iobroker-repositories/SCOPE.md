# Project Scope: ioBroker.repositories

```yaml
project_id: iobroker-repositories
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/ioBroker.repositories
reviewed_commit: c7c096b
profile: ops-field
reviewed_commit_note: Fork-Snapshot; parent ioBroker/ioBroker.repositories ist maßgeblich für Live-Catalog
```

## Grenzen

| | |
|--|--|
| **In scope** | `sources-dist.json` / `sources-dist-stable.json`, PR-Workflow README, Bezug zu eigenen Adaptern |
| **Nicht in scope** | Adapter-Quellcode; npm-Publish-Details jenseits Catalog-Einträgen; 1:1-Spiegel des Upstream-Trees als Wissensbasis |
| **Profil** | ops-field (Catalog/Betrieb), keine Firmware/Adapter-Logik |

## Systeme

```text
Adapter-Repo (npm + GitHub)
    │  PR: addToLatest / meta-URL in sources-dist*.json
    ▼
ioBroker.repositories (upstream) ──▶ ioBroker Adapter-Liste (latest/stable)
Lokaler Fork MPunktBPunkt/… ── oft nur Arbeitskopie / hinterher
```

## Ziel dieses Audit-Laufs

Einordnen: Fork vs. Upstream; welche eigenen Adapter bereits gelistet sind (`metermaster`) und welche nicht (`kostalpiko`); kein Deep-Dive in Catalog-Tooling.
