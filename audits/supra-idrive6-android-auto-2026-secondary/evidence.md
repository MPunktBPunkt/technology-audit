# Evidence — supra-idrive6-android-auto-2026-secondary

Secondary 2026-11-13 · **standard_version 0.7.1** · Pin: `Sq00ky/Supra-iDrive6-Android-Auto@ac9a292`.

Nur In-Scope (SPP / Contention / Transport-Owner). Native AA / QNX / CarPlay: nicht erfasst.

## Inventory

```yaml
id: supra-idrive6-android-auto
name: Supra-iDrive6-Android-Auto (NBT-AAD)
url: https://github.com/Sq00ky/Supra-iDrive6-Android-Auto
type: secondary
relevance: high (SPP contention + transport ownership)
primary_topics:
  - bluetooth-spp-hu-side
  - channel-contention-mybmw-aaidrive
  - looksLikeBmwBcl-heuristic
status: observed
```

## FACT (direkt Source / Issue / Log)

| ID | Claim | Status | Quelle |
|----|-------|--------|--------|
| `EVID-SUPRA-2026-11-13-001` | Daemon registriert SPP-Service `AndroidAuto` via `SppUuidRegister`; Antwort `GapErrorCode=0 (OK)` in Feld-Logs | `FACT` | Issue [#18](https://github.com/Sq00ky/Supra-iDrive6-Android-Auto/issues/18) Log; `milestone-7/src/bluetooth_manager.cpp`; `milestone-7/readme.md` § Bluetooth |
| `EVID-SUPRA-2026-11-13-002` | Nach erfolgreicher Phone-Öffnung: `[Wireless] opened /dev/btspp0` → Wireless-Handshake; danach Wi-Fi-Details / Session-Pfad | `FACT` | Issue #18 Log (`opened /dev/btspp0 … starting handshake`); `milestone-7/readme.md` Wireless setup → Session |
| `EVID-SUPRA-2026-11-13-003` | Aktives **MyBMW** auf dem Phone verhindert Wireless-AA-Session von nbt-aad (Contention auf `/dev/btspp*`); Force-Stop / Disable stellt Verbindung wieder her | `FACT` | Issue [#37](https://github.com/Sq00ky/Supra-iDrive6-Android-Auto/issues/37); `milestone-7/readme.md` Troubleshooting („Force-stop MyBMW …“) |
| `EVID-SUPRA-2026-11-13-004` | Paralleler Betrieb von **AAIdrive** und nbt-aad wird ausdrücklich als problematisch beschrieben | `FACT` | `README.md` Common Problems #1; `install.md` Known Limitations („AAIDrive cannot be running/installed“) |
| `EVID-SUPRA-2026-11-13-005` | Heuristik `looksLikeBmwBcl`: Hex-Sequenz-Check auf SPP-Rohbytes (u. a. `12 34 56 78`, Payload `DEADBEEF` / `13371337`, self-consistent 8-Byte-Frame) → Link als Companion/BCL markieren und freigeben | `FACT` (Heuristik-Existenz) | `milestone-7/src/wireless_setup.cpp` `looksLikeBmwBcl`; Issue #37 erwähnt denselben Namen |
| `EVID-SUPRA-2026-11-13-006` | Source-Kommentar/Docs: AAIdrive hat **keinen** eigenen BT-Link; Apps erreichen die HU über den MyBMW/Connected-**BCL**-Tunnel; HU-Seite A4AHandler auf `/dev/btspp0` wartet auf BCL-Startup-Magic | `FACT` (Source-Behauptung) | `spp_link_policy.hpp`; `spp_direction.hpp`; `milestone-7/readme.md` MyBMW/AAIdrive-Absatz |

**Hinweis zu 005:** belegt nur, dass der Secondary-Daemon diese Bytes als BCL-ähnlich behandelt. Framing-/Watchdog-Semantik bleibt CROSSREF BimmerGestalt — **kein** neuer Wire-FACT.

## INFERENCE (klar markiert)

| ID | Claim | Status | Ableitung |
|----|-------|--------|-----------|
| `EVID-SUPRA-2026-11-13-007` | Connected/MyBMW ist der **primäre Beleger** des SPP-/BCL-Kanals auf der HU | `INFERENCE` | 003+006 + Owner-Tabelle Handshake §3.1; Field-Contention wenn MyBMW aktiv |
| `EVID-SUPRA-2026-11-13-008` | AAIdrive und native AA (nbt-aad) sind **Consumer**/Konkurrenten amselben HU-SPP-Raum; AAIdrive = Etch-Consumer auf MyBMW-Tunnel | `INFERENCE` | 004+006; deckt sich mit Lab `NO_RFCOMM` für AAIdrive allein gegen Dummy-HU |
| `EVID-SUPRA-2026-11-13-009` | Die HU hat einen aktiven Bluetooth-SPP-Manager (`/dev/btsppN`, UUID-Register), den mehrere Parteien nutzen | `INFERENCE` | 001+002+003; HU-seitige Nodes/Logs, kein eigener SDP-Capture |

## UNKNOWN / nicht behauptet

| Claim | Status | Hinweis |
|-------|--------|---------|
| Konkreter RFCOMM-Kanal **X** der OEM-BCL-Session | `UNKNOWN` | Lab-Kanal 5 ≠ Field |
| SABM-Richtung / L2CAP-Details | `UNKNOWN` | nicht im Scope |
| BCL-Init / Handshake-Version / Watchdog-Pong als **eigenes** Field-MEASURED | `UNKNOWN` | Heuristik-Bytes ≠ Capture |
| F20 nutzt denselben Kanal/Node wie NBT-Evo-Units in den Issues | `UNKNOWN` | Secondary ≠ F20-Wire |
| Native AA = derselbe BCL-Pfad wie BclCarLink | `REJECTED` as claim | AA-UUID `4DE17A00-…` vs. BCL/SPP-Companion; bewusst getrennt |
| nbt-aad „CAR öffnet MyBMW-Link“ vs. BclCarLink „Phone = RFCOMM Client“ | **Spannung** | beide Source-FACTS; nicht glätten bis Capture |

## CROSSREF (nicht neu)

| Thema | Ort |
|-------|-----|
| BCL Framing / Init `12 34 56 78` / Watchdog 5001 | [`bimmergestalt-idrive-2026-foreign`](../bimmergestalt-idrive-2026-foreign/) · [`bmw-bcl-rfcomm-role-2026-desk`](../bmw-bcl-rfcomm-role-2026-desk/) |
| Phone RFCOMM Client (BclCarLink) | `EVID-BCLRF-2026-11-12-001`–`003` |
| Transport Owner vs. Etch Consumer (Desk) | [`bmw-bcl-handshake.md`](../../projects/bimmergestalt-idrive-refs/applications/bmw-bcl-handshake.md) §3.1 |

## Wissens-Chronik

| Datum | Ereignis |
|-------|----------|
| 2026-11-13 | Secondary Note aufgenommen; Sheet/Applications/Messbedingungen verlinkt |
