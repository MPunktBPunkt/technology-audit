# generated/retrieval/

**GENERATED** by `python3 tools/ta-assist index`. Do not hand-edit.

SoT remains `technologies/`, `projects/`, `audits/`.
Model: [`docs/EVIDENCE-CLAIM-MODEL.md`](../../docs/EVIDENCE-CLAIM-MODEL.md).

## Layout

| Path | Role |
|------|------|
| `index.yaml` | Master retrieval index |
| `bundles/<slug>.yaml` | Per-technology evidence bundle |
| `bundles/topic-*.yaml` | Cross-cutting topic bundles |
| `../../audits/INDEX.yaml` | Stable audit_id ↔ directory map |

## AI usage

1. Open `index.yaml` or a topic/tech bundle.
2. Read **`current:`** first (status, open_points, next_evidence, rejected_highlights).
3. Honor `rejected`, `unknowns`, `transfer_limits`.
4. Follow `source_of_truth` / audit paths only for depth.
