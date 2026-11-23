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

## Topic audits (ingested 2026-11-23)

| # | Audit | Sheet delta |
|---|-------|-------------|
| 1 | [`bmw-sas-auth-field-crypto-2026-11-21`](../../audits/bmw-sas-auth-field-crypto-2026-11-21/) | `bmw-sas-auth` — 18/18 VERIFY |
| 2 | [`bmw-bcl-bt-rfcomm-framing-2026-11-21`](../../audits/bmw-bcl-bt-rfcomm-framing-2026-11-21/) | `bmw-bcl` — frag 4000/5306 |
| 3 | [`bmw-etch-rpc-binary-reassembly-2026-11-21`](../../audits/bmw-etch-rpc-binary-reassembly-2026-11-21/) | `bmw-etch-rpc` — DEADBEEF |
| 4 | [`bmw-rhmi-music-handle23-field-2026-11-21`](../../audits/bmw-rhmi-music-handle23-field-2026-11-21/) | `bmw-rhmi` — H23 catalog |
| 5 | [`bmw-av-session-control-vs-audio-2026-11-21`](../../audits/bmw-av-session-control-vs-audio-2026-11-21/) | **new** `bmw-av` |
| 6–7 | CDS / AM field audits | `bmw-etch-rpc` + `bmw-rhmi` |
| 8 | [`esp32-bt-analyzer-b3-relay-topology-2026-11-21`](../../audits/esp32-bt-analyzer-b3-relay-topology-2026-11-21/) | project STATUS |
| 9 | [`method-raw-bcl-etch-forensic-2026-11`](../../audits/method-raw-bcl-etch-forensic-2026-11/) | `methods/raw-bcl-etch-forensic` |

## Next (ordered)

1. Dual-Plane Audio-Boundary nach PLAY (`bmw-av` / `NEXT_AUDIO_BOUNDARY_PROOF.md`)  
2. Lab minimal Music stub mit Field-IDs 444–447 / 336·248 / 660·661 → ein F20-Versuch  
3. Gate B2 Standalone-Signer (nicht Protokoll-RE)
