# Lab A0 Smoke

## Lauf 1 — vor Instrument (2026-10-26)

```yaml
result: FAIL
blocker: no CSI FW; rfmonitor on S3; no D1
```

Siehe vorherige Notiz: S3 = rfmonitor 1.10.2; Capture-Pipeline fehlte.

## Lauf 2 — nach Instrument (2026-10-26)

```yaml
result: FAIL
c1_executed: false
commit: none
session: projects/esp32-rf-sensing/instrument/sessions/a0_smoke_20261026
```

| Check | Ergebnis | Beobachtung |
|-------|----------|-------------|
| S3 startet reproduzierbar | **PASS** | `INSTR s3-csi-raw boot` |
| CSI-Capture / RAW-CB | **FAIL** | `csi_ok=0`; kein `CSI_RAW` |
| Device- + Host-Zeit | **FAIL** | keine Samples |
| Host-seq / Gaps | **FAIL** | n/a |
| `session.yaml` / `csi_raw.csv` / `session_stats.json` | **PASS** (Struktur) | Header-only CSV; stats `n_samples=0` |
| Session Start/Stop | **teilweise** | Host läuft; S3 nie `INSTR_READY` |
| D1 Traffic Profil N | **FAIL** | D1 nicht verbunden / nicht geflasht |

S3: `INSTR_ERR wifi_connect_timeout` (AP `RFSENSE_N` fehlt).

**C1 nicht gestartet.** Nächster Schritt: D1 anschließen + `d1-traffic-n` flashen → A0 wiederholen.
