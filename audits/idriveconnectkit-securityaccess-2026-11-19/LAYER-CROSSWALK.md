# Layer Crosswalk: BCL vs SAS vs F20 Feld

## Schichten (verbindlich)

| Layer | Tokens / API | Quelle | Feld F20 |
|-------|--------------|--------|----------|
| BT / SDP | SPP `0x1101` SCN 6/10 | FIELD_B1 | MEASURED |
| BCL Transport | `INIT 12345678`, HS, KNOCK, ACK/DATAACK, OPEN, WD 5001 | BclCarLink + Feld | MEASURED |
| Etch | `0xDEADBEEF`, dest **4004** | Kit etch + Feld | MEASURED |
| **SAS** | `sas_certificate` → challenge → `sas_login` | KitAndroid + IDL | MEASURED (`DEEP_FORENSIC_ETCH_SAS_20261116`) |
| Phone Security | Binder / SecurityModule `signChallenge` | KitAndroid | **nicht** im BT-Capture (nur Response-Bytes) |
| RHMI/AM/CDS | nach erfolgreichem Login | AAIdrive | MEASURED nach Auth |

## Explizit REJECTED

| Claim | Warum |
|-------|-------|
| „Security Challenge = HS / KNOCK / ACK10“ | Andere Schicht: BCL vor Etch; SAS ist Etch-RPC nach OPEN(4004) |
| „BclCarLink implementiert SAS“ | Nur Tunnel; README fordert Security Module separat |
| „NBT-AAD erklärt SAS“ | Anderer SDP/Stack ([f20-sdp-vs-nbt-aad](../f20-sdp-vs-nbt-aad-2026-11-19/)) |
| „Lab f20_sim Auth = F20 Auth“ | Simulator stub; FIELD AUTH REJECT 2026-11-18 |

## Was **passt** (Code ↔ Feld)

| Desk / Code | Feld | Relation |
|-------------|------|----------|
| Challenge **16 B** (`SecurityAccess` Kommentar; Analysis Doc) | `_result_sas_certificate` 16-B Challenge | **SUPPORT** → Challenge-Länge jetzt FIELD FACT |
| Login-Signatur **512 B** RSA-4096 (Classic test; Doc) | `sas_login` Wire **559 B** = 8 BCL + 8 DEADBEEF + 30 Etch + **512 RSA** + 1 END | **SUPPORT / REFINE** (512 Payload; 559 Frame) |
| APP_AUTH CN enthält „connection“ / TouchCommand Connection | Feld CN `a4a_app_BMWTouchCommand_Connection_00.00.10` | **SUPPORT** |
| XOR-Variante für APP_AUTH (`PrivateKeyHandling` / Analysis) | Deep Forensic: XOR zwingend auf diesem F20 | **SUPPORT** |
| Ohne gültiges Cert/Signatur → Auth fail | `FIELD_AUTH_REJECT_20261118` Lab-sim Cert abgewiesen | **SUPPORT** |
| KNOCK struct serial/bt/mac/wifi/appType | BclCarLink `BclPacket.Knock`; Feld KNOCK | **SUPPORT** Transport — **nicht** SAS |

## Sequenz-Zeitachse (Feld Golden Path, verkürzt)

```text
RFCOMM SCN 6
  BCL INIT → HS v5 → … → KNOCK → OPEN 5001 (WD) → OPEN 4004
       │                                              │
       │  ← alles BCL / multiplexing                  │
       │                                              ▼
       │                                    Etch BMWRemoting
       │                                    sas_certificate(p7b)
       │                                    ← 16-B challenge
       │                                    [Phone: OEM signChallenge]  ★
       │                                    sas_login(512-B sig)
       │                                    ← _result_sas_login
       ▼                                    rhmi_getCapabilities / …
```

★ = nicht im RFCOMM-Klartext als „Signing-Algorithmus“ sichtbar; nur Response-Bytes.

## G3-Status-Update (gegenüber Audit 2026-11-06)

| Gate | 2026-11-06 | 2026-11-19 |
|------|------------|------------|
| G3 Desk | FACT | FACT (dieser Deep-Dive präzisiert Dependencies) |
| G3 Field | **absent** | **MEASURED** — `DEEP_FORENSIC_ETCH_SAS_20261116` (+ Auth reject 18.11) |

Sheet `bmw-sas-auth` `field_evidence` entsprechend anheben (siehe Commit).

## „Response abgreifen“ — epistemische Einordnung

| Aussage | Klassifikation |
|---------|----------------|
| Response wird nur von OEM Security Service/Module erzeugt | FACT |
| Erfolgreiche Sessions zeigen Response bereits auf dem Wire (`sas_login`) | FIELD FACT |
| Ohne OEM-App keine gültige Signatur für echte HU | INFERENCE → SUPPORT durch AUTH_REJECT |
| Neuer operativer Abgreif-/Hook-Pfad als Forschungsziel | **REJECT** (Leitplanke; kein Nutzen über Wire-Capture hinaus) |
