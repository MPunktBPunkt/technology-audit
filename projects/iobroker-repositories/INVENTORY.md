# Project Inventory: ioBroker.repositories

```yaml
project_id: iobroker-repositories
updated: 2026-10-09
reviewed_commit: c7c096b
profile: ops-field
pilot_order: []
```

**Reuse / Match** ([REUSE.md](../../docs/REUSE.md), Standard [0.6.3](../../docs/STANDARD-CHANGELOG.md)):

| Signal | Ziel-Sheet | Aktion |
|--------|------------|--------|
| Official adapter catalog JSON | — | **kein Sheet** (Upstream-Prozess, nicht eigene Tech) |
| Eigene Adapter-Einträge | Projekte `iobroker-metermaster` / `iobroker-kostalpiko` | Status unten, kein Catalog-Sheet |

Ursprung: Fork [ioBroker.repositories](https://github.com/MPunktBPunkt/ioBroker.repositories) ← parent `ioBroker/ioBroker.repositories`.  
Kampagne: [iobroker-repositories-2026-ops](../../audits/iobroker-repositories-2026-ops/).

## Übersicht

Keine Technology-Sheets in diesem Projekt. Ops-Status eigener Adapter (Fork-Stand `c7c096b`):

| Adapter | latest (`sources-dist`) | stable | KB-Projekt |
|---------|-------------------------|--------|------------|
| `metermaster` | ja (MPunktBPunkt meta) | ja (Version-Pin im Fork) | [`iobroker-metermaster`](../iobroker-metermaster/) |
| `kostalpiko` | **nein** | **nein** | [`iobroker-kostalpiko`](../iobroker-kostalpiko/) |
| `kostal-piko-ba` | ja (fremd, hombach) | — | ≠ unser Adapter |
| `esp-hub` | **nein** (Fork-Scan) | **nein** | [`iobroker-esp-hub`](../iobroker-esp-hub/) |
| `fritzwireguard` | **nein** (Fork-Scan) | **nein** | [`iobroker-fritzwireguard`](../iobroker-fritzwireguard/) |
| `freeair100` | **nein** | **nein** | [`iobroker-freeair100`](../iobroker-freeair100/) |
| `kalender` | **nein** | **nein** | [`iobroker-kalender`](../iobroker-kalender/) |
| `linuxdashboard` | **nein** | **nein** | [`iobroker-linuxdashboard`](../iobroker-linuxdashboard/) |
| `mbrepository` | **nein** | **nein** | [`iobroker-mbrepository`](../iobroker-mbrepository/) |

## Coverage-Lücken

| Bereich | Warum offen | Nächster Schritt |
|---------|-------------|------------------|
| Fork hinter Upstream | 208 commits behind | Sync oder Upstream für PRs nutzen |
| `kostalpiko` listing | fehlt | addToLatest PR gegen **upstream** |
| Live-Catalog ≠ Fork | Fork veraltet | Evidence immer gegen ioBroker/… prüfen |

## Signale ohne Eintrag

- `npm run addToLatest` Hilfsskript
- adapter-check.iobroker.in
