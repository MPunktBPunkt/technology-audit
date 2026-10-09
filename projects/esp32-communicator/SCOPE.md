# Project Scope: esp32.communicator

```yaml
project_id: esp32-communicator
updated: 2026-10-09
source_repo: https://github.com/MPunktBPunkt/esp32.communicator
reviewed_commit: 429f20e
profile: firmware
```

## Grenzen

| | |
|--|--|
| **In scope** | `esp32.communicator.ino`, README (ESP-NOW, SSE, WebRTC/Hub) |
| **Nicht in scope** | A2DP; LAN-Subnet-Scan; Hub-Internals WebRTC-Server |
| **Hardware** | ESP32, Arduino-ESP ≥ 3.0 |
| **Version** | 1.8.0 |

## Systeme

```text
ESP-NOW Peers ◀──▶ Messages/Call-Signals
Browser Chat/SSE ◀── ESP Web
Browser WebRTC ◀── Hub /api/webrtc Signaling
ESP ──Hub ios peers/sent/recv──▶ esp-hub
```

## Ziel dieses Audit-Laufs

Desk-Audit unter **Audit-Standard 0.6.2** (Hub ohne fwType, Scan-Schichten, Reuse).
