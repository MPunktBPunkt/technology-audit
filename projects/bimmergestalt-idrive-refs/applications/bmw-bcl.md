# Project Application: bmw-bcl in bimmergestalt-idrive-refs

```yaml
project_id: bimmergestalt-idrive-refs
tech_slug: bmw-bcl
status: active
sheet: ../../../technologies/bmw-bcl/SHEET.md
audit: ../../../audits/bimmergestalt-idrive-2026-foreign/
maturity:
  technology: R2
  implementation: R2
  field_evidence: R0
  reusability: W2
```

Desk-verifiziert gegen Pins: BclCarLink@`7cfd959`, wireshark_bmw_bcl@`07b7982`,
BMWConnectedAnalysis@`9e96ac6`. `field_evidence: R0` — keine eigenen Captures.

## Evidenz

| Claim | Evidence-ID | Status |
|-------|-------------|--------|
| 8-Byte Header command/src/dest/len BE | `EVID-BG-2026-10-28-001` | `FACT` |
| dest 0x0FA4 = Etch | `EVID-BG-2026-10-28-002` | `FACT` |
| Handshake version/instanceId/bufferSize | `EVID-BG-2026-10-28-003` | `FACT` |
| SelectProto(3)+Knock bei version>3 | `EVID-BG-2026-10-28-005` | `FACT` |
| Watchdog dest 0x1389 / 5001 | `EVID-BG-2026-10-28-007` | `FACT` |
| USB/ENET in Doc, nur BT in BclCarLink | `EVID-BG-2026-10-28-020` | Contradiction Doc↔Code |
| `BclClientTransport` über Streams; RFCOMM nur in `BtConnection` | `EVID-AOA-2026-10-29-029` | `FACT` Code |
| Session-Init Phone: Hex `12345678` dann auf Handshake warten | `EVID-BG-2026-10-28-004` | `FACT` |
| Nach BCL: Multiplex → Dest-Protokolle (Etch-Proxy) | `EVID-BG-2026-10-28-006` / `012` | `FACT` |
| USB-Bulk BCL am NBT Evo | `EVID-AOA-2026-10-28-026` | `UNKNOWN` → C1b **B2** |
