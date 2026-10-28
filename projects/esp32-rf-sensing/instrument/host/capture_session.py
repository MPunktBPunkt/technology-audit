#!/usr/bin/env python3
"""A0 host capture: session.yaml + csi_raw.csv + session_stats.json. No C1/C2 logic."""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    import serial
except ImportError as e:
    raise SystemExit("pyserial required: pip install pyserial") from e

CSI_RE = re.compile(r"^CSI_RAW,")
HEADER = [
    "host_seq",
    "host_t_mono",
    "host_t_utc",
    "device_seq",
    "device_ts",
    "rssi",
    "noise_floor",
    "channel",
    "secondary",
    "rate",
    "sig_mode",
    "mcs",
    "cwb",
    "sig_len",
    "mac",
    "first_word_invalid",
    "len",
    "iq",
]


def parse_csi_line(line: str) -> dict | None:
    if not CSI_RE.match(line):
        return None
    # CSI_RAW,seq,ts,rssi,nf,ch,sec,rate,sig,mcs,cwb,sig_len,mac,fwi,len,iq...
    parts = line.strip().split(",")
    if len(parts) < 16:
        return None
    try:
        meta = {
            "device_seq": int(parts[1]),
            "device_ts": int(parts[2]),
            "rssi": int(parts[3]),
            "noise_floor": int(parts[4]),
            "channel": int(parts[5]),
            "secondary": int(parts[6]),
            "rate": int(parts[7]),
            "sig_mode": int(parts[8]),
            "mcs": int(parts[9]),
            "cwb": int(parts[10]),
            "sig_len": int(parts[11]),
            "mac": parts[12],
            "first_word_invalid": int(parts[13]),
            "len": int(parts[14]),
            "iq": ",".join(parts[15:]),
        }
    except ValueError:
        return None
    return meta


def main() -> int:
    ap = argparse.ArgumentParser(description="RF-sensing A0 session capture")
    ap.add_argument("--port", required=True, help="S3 serial port")
    ap.add_argument("--baud", type=int, default=921600)
    ap.add_argument("--duration", type=float, default=15.0, help="seconds")
    ap.add_argument("--profile", default="N")
    ap.add_argument("--out", required=True, help="output session directory")
    ap.add_argument("--session-id", default=None)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    session_id = args.session_id or datetime.now(timezone.utc).strftime(
        "sess_%Y%m%dT%H%M%SZ"
    )

    t0_wall = datetime.now(timezone.utc)
    t0_mono = time.monotonic()

    session = {
        "contract_id": "MV-ESP32-CSI-RAW-v0",
        "session_id": session_id,
        "profile_id": args.profile,
        "rx_node": "esp32-s3",
        "traffic_peer": "d1-mini",
        "path": "D1 SoftAP UDP -> S3 CSI RX",
        "ssid": "RFSENSE_N",
        "channel": 6,
        "delta_t_ms_nominal": 20 if args.profile == "N" else None,
        "port": args.port,
        "baud": args.baud,
        "duration_s_request": args.duration,
        "start_utc": t0_wall.isoformat(),
        "instrument": {
            "s3": "projects/esp32-rf-sensing/instrument/s3-csi-raw",
            "d1": "projects/esp32-rf-sensing/instrument/d1-traffic-n",
            "host": "projects/esp32-rf-sensing/instrument/host/capture_session.py",
        },
        "notes": "A0/capture only; no motion/presence",
    }
    try:
        import yaml  # type: ignore

        (out / "session.yaml").write_text(
            yaml.safe_dump(session, sort_keys=False), encoding="utf-8"
        )
    except Exception:
        (out / "session.yaml").write_text(
            "# JSON fallback (PyYAML not installed)\n"
            + json.dumps(session, indent=2)
            + "\n",
            encoding="utf-8",
        )

    csv_path = out / "csi_raw.csv"
    rows = []
    gap_count = 0
    last_device_seq = None
    instr_lines = []
    ready = False

    ser = serial.Serial(args.port, args.baud, timeout=0.2)
    try:
        # optional reset
        try:
            ser.dtr = False
            time.sleep(0.05)
            ser.dtr = True
        except Exception:
            pass
        time.sleep(0.5)
        ser.reset_input_buffer()

        deadline = time.monotonic() + args.duration + 25.0  # include join wait
        capture_deadline = None
        host_seq = 0

        print(f"CAPTURE start session_id={session_id} port={args.port}")
        while time.monotonic() < deadline:
            raw = ser.readline()
            if not raw:
                if capture_deadline and time.monotonic() >= capture_deadline:
                    break
                continue
            try:
                line = raw.decode("utf-8", "replace").strip()
            except Exception:
                continue
            if not line:
                continue

            if line.startswith("INSTR"):
                instr_lines.append(line)
                print(line)
                if "INSTR_ERR" in line and capture_deadline is None and not ready:
                    print("CAPTURE abort: instrument error before READY")
                    break
                if "INSTR_READY" in line and capture_deadline is None:
                    ready = True
                    capture_deadline = time.monotonic() + args.duration
                    print(f"CAPTURE armed duration={args.duration}s")
                continue

            meta = parse_csi_line(line)
            if meta is None:
                continue
            if capture_deadline is None:
                # CSI before READY — still accept if already streaming
                ready = True
                capture_deadline = time.monotonic() + args.duration
                print(f"CAPTURE armed(on first CSI) duration={args.duration}s")

            now_mono = time.monotonic()
            if now_mono > capture_deadline:
                break

            dseq = meta["device_seq"]
            if last_device_seq is not None and dseq != last_device_seq + 1:
                gap_count += 1
            last_device_seq = dseq

            row = {
                "host_seq": host_seq,
                "host_t_mono": f"{now_mono - t0_mono:.6f}",
                "host_t_utc": datetime.now(timezone.utc).isoformat(),
                **{k: meta[k] for k in meta if k != "iq"},
                "iq": meta["iq"],
            }
            rows.append(row)
            host_seq += 1
    finally:
        ser.close()

    t1_wall = datetime.now(timezone.utc)
    duration = time.monotonic() - t0_mono

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    n = len(rows)
    observed_pps = (n / args.duration) if args.duration > 0 else 0.0
    device_seqs = [int(r["device_seq"]) for r in rows]
    stats = {
        "session_id": session_id,
        "ready_seen": ready,
        "n_samples": n,
        "duration_s_wall": (t1_wall - t0_wall).total_seconds(),
        "duration_s_request": args.duration,
        "observed_pps": observed_pps,
        "gap_count_device_seq": gap_count,
        "device_seq_min": min(device_seqs) if device_seqs else None,
        "device_seq_max": max(device_seqs) if device_seqs else None,
        "host_seq_last": n - 1 if n else None,
        "end_utc": t1_wall.isoformat(),
        "instr_tail": instr_lines[-10:],
        "a0_checks": {
            "csi_samples_gt_0": n > 0,
            "files_written": True,
            "device_seq_present": n > 0,
            "host_time_present": n > 0,
        },
    }
    (out / "session_stats.json").write_text(
        json.dumps(stats, indent=2) + "\n", encoding="utf-8"
    )

    print(f"CAPTURE done n_samples={n} gaps={gap_count} out={out}")
    print(json.dumps(stats["a0_checks"], indent=2))
    return 0 if n > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
