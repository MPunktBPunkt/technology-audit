# Technology Sheet: Spotify Web API Remote (PKCE)

```yaml
slug: spotify-web-api-remote
title: Spotify Web API Remote (PKCE)
primary: F
tags: [esp-idf, arduino, fragile, streaming]
type: pattern
status: active
seen_in: [esp32-spotify-remote]
maturity:
  technology: R1
  implementation: R1
  field_evidence: R0
  reusability: W1
pilot: audits/esp32-spotify-remote-2026-foreign
```

Nur Ebene **A**. Client-ID, Board-Pins, UI-Layouts → Application.  
**Account:** Playback-Control braucht eligible Spotify-Account + aktiven Player (Upstream).

## Kurzfassung

ESP steuert Spotify über die **Web API** (Now-Playing, Play/Pause/Next, Cover): OAuth2 **Authorization Code + PKCE**, Refresh-Token in NVS, verified HTTPS — **ohne** Client-Secret in der Firmware und **ohne** On-Device-Audio-Decode.

## Abgrenzung

- **Ist:** HTTPS Web-API Remote + PKCE Token-Lifecycle.
- **Ist nicht:** Spotify Connect / cspot Decode (`lms-squeezelite` Add-on); LMS Multi-Room; A2DP Transport.
- **Grenzt an:** Loopback OAuth Helper auf Host; mDNS Setup-Page.

## Schnittstellen

| Richtung | Schnittstelle | Bemerkung |
|----------|---------------|-----------|
| oben | Spotify Web API | Bearer + Refresh |
| lateral | Browser + loopback bridge | PKCE callback |
| unten | NVS refresh token; TLS root bundle | kein Secret |
| UI | Touch/Display | optional |

## Fallstricke

| Claim | Status | Hinweis |
|-------|--------|---------|
| Client-Secret gehört in Firmware | `REJECTED` | PKCE; Secret vermeiden |
| Web-API-Remote ≡ Spotify Connect Player | `REJECTED` | Control ≠ Decode |
| Insecure TLS Fallback ok | `REJECTED` | Upstream: kein Fallback |
| Ohne aktiven Spotify-Player steuerbar | `REJECTED` / Gate | Account+Player nötig |
| HTTP `.local` als Spotify Redirect | `REJECTED` | Loopback IP literal |

### Projektstart-Checkliste

- [ ] PKCE vs Secret-Pfad entscheiden
- [ ] Redirect-URI exakt (loopback)
- [ ] TLS Bundle + Clock vor Requests
- [ ] Kontrast Connect/LMS geklärt
- [ ] Application + `seen_in`

## Transfer

Für sichere Cloud-API-Remotes auf ESP. Nicht still auf Connect-Decoder übertragen.

## Referenzen

- Spotify Authorization Code PKCE
- Pilot: [seichris/esp32-spotify-remote](https://github.com/seichris/esp32-spotify-remote)
