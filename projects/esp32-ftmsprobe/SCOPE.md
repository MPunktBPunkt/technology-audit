# Project Scope: esp32.ftmsprobe

```yaml
project_id: esp32-ftmsprobe
updated: 2026-10-11
source_repo: https://github.com/MPunktBPunkt/esp32.ftmsprobe
reviewed_commit: 70c3c25
```

## Grenzen

| | |
|--|--|
| **In scope** | Firmware `src/` (BleProbe, ProbeGuard, Hub, Web), `tools/probe-run.py` / `ftms.py` / deploy, `docs/ergometer/*` inkl. Scan-Artefakte |
| **Nicht in scope** | Produkt-Coach (`esp32.ergo` Logik); Hub-Internals; dauerhafter Feld-Betrieb als Consumer-App |
| **Hardware** | `probe` (D1 Mini) · `probe-s3` (ESP32-S3); Zielgeräte Varon + optional Polar H9 |
| **Version** | `FW_VERSION` 0.1.4 (`platformio.ini`) |

## Systeme

```text
CLI (LXC) ──HTTP──▶ ESP-Sonde ──BLE Central──▶ Varon / H9
                 ▲
ESP-Hub OTA ─────┘
```

## Ziel dieses Audit-Laufs

Sonde als **wiederverwendbares Lab-Muster** + Method Note verankern; FTMS/Varon-Evidence dem Wissenswachstum zuordnen (kein zweites Spec-Sheet). Transferpfad Sonde → Ergo (`BleProbe` → `BleCentral`/`FtmsClient`, `ftms.py` → Codec) dokumentieren.

**Revalidation 0.6.6:** Chip-/Build-Scope `probe` vs `probe-s3` + Dual-Link-Budget ([DELTA](../../audits/esp32-ftmsprobe-2026-pilot/DELTA.md)).
