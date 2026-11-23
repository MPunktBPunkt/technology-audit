# Agent / AI entry (technology-audit)

This repo is a **layered knowledge base**. Do **not** invent a parallel `AI_KNOWLEDGE.md`.

## Start here (retrieval)

1. [`generated/retrieval/index.yaml`](generated/retrieval/index.yaml) — master index  
2. Topic or tech bundle under [`generated/retrieval/bundles/`](generated/retrieval/bundles/)  
3. [`audits/INDEX.yaml`](audits/INDEX.yaml) — stable `A-YYYY-NNN` ↔ directory  
4. Model: [`docs/EVIDENCE-CLAIM-MODEL.md`](docs/EVIDENCE-CLAIM-MODEL.md)

Then open the cited Sheets / Audits / `claims.yaml` for depth.

## Always return with the answer

- **facts** / measurements  
- **rejected** (negative evidence)  
- **unknowns** (+ reason if present)  
- **transfer_limits** / scope (host, environment, protocol)

If a bundle lists `transfer_limits: bmw_host_specific` (or similar), do **not** generalize to arbitrary USB/BT hosts.

## Regenerate indexes

```bash
python3 tools/ta-assist index
python3 tools/ta-assist check
```

Hand-editing `generated/` or `audits/INDEX.yaml` is forbidden.

## Human SoT (unchanged)

| Layer | Path |
|-------|------|
| Technology | `technologies/<slug>/SHEET.md` |
| Project use | `projects/<id>/applications/<slug>.md` |
| Observation | `audits/<dir>/` (+ optional `claims.yaml`) |
| Methods | `methods/` |

## Tests

[`docs/retrieval-tests.yaml`](docs/retrieval-tests.yaml) — expected paths + reject slugs.  
Prefer bundles for new BMW Connected / MSC questions.
