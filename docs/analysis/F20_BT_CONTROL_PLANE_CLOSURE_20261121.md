# F20 Bluetooth Control Plane — Closure Status (2026-11-21)

```yaml
id: f20-bt-control-plane-closure-20261121
type: status-freeze
scope: NBT Evo Connected Bluetooth Control Plane
evidence: bt-analyzer FIELD_B3_GATEB_20261121T112446Z (commit 4d05169)
full_audit: audits/nbt-evo-bt-control-plane-closure-2026-11-21/
supersedes_p0_of: docs/analysis/F20_CONNECTED_GAP_AUDIT_20261120.md
```

## Verdict

**Protokoll-RE für den BT Control Plane ist geschlossen.** Offen sind Implementierungsartefakte (Music DESCRIPTION, Feld-IDs, eigener RHMI-PoC) und Standalone-Signer — nicht die Wire-Mechanik.

```text
Transport / BCL / Etch     CLOSED
SAS live OEM path          CLOSED*   (standalone OPEN)
RHMI / AM / CDS / AV       CLOSED*   (template bytes GAP)
Own App                    OPEN
```

## Gate model (post-B3)

| Gate | Status |
|------|--------|
| A — Crypto / Cert↔Sig | CLOSED |
| B — F20 accepts live authorized MyBMW/AAIdrive (B3 relay) | **CLOSED** FIELD FACT |
| B2 — standalone / reproduced credential without MyBMW | OPEN |
| Own RHMI/AM field PoC | OPEN |

## Anti-claims (do not reintroduce)

- MyBMW is protocol-mandatory → **REJECTED**
- Spotify is an `am_registerApp` → **REJECTED** (B3)
- SAS pad = X509 serial `0x0AA9` → **REJECTED**
- `setResource` always required → **REJECTED**
- Lab `modelId=100` / `actionId=200` = F20 → **REJECTED**

## Next (ordered)

1. Extract Music DESCRIPTION `e9e31c31…` (92085 B)  
2. Catalog field model/action/event IDs  
3. Lab minimal template → one field variable (Weg A)
