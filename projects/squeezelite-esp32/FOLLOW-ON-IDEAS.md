# Follow-on ideas (aus squeezelite-esp32)

```yaml
reuse_outcomes:
  reused: [esp-i2s-audio, esp-psram-heavy-port, bluetooth-a2dp, webradio-browser-host]
  new: [lms-squeezelite]
  not_helped: []
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Multi-room Sync Lab | `lms-squeezelite` | Zwei Boards + LMS |
| AirPlay/Spotify Sheets | observed | nur bei Bedarf |
| S3-only I2S build checklist | Sheet + silicon | kein BT |
| Kontrast esp32-webradio | `webradio-browser-host` | Browser vs On-device decode |
