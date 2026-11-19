# F20 HU SDP Catalog (MEASURED)

| Feld | Wert |
|------|------|
| Evidence | `FIELD_B1_FROM_A6_20261113T062824Z` |
| Capture | `FIELD_A6_HU_20261113T062824Z.btsnoop` |
| SHA-256 | `6806083f2d4534edc5c7e75fb9ca2e060ae77e83430c6e36633f9a168f55f8b7` |
| HU | BMW 38304 · `D4:36:39:CF:E1:B5` · Class `0x340408` · Provider strings `ALPS_*` |
| State | A (HU idle, no phone Connected app); SDP exchange während A6 Pairing |
| Tool | `tools/btsnoop_decode.py` (upstream `esp32.bt-analyzer` / lokal `bt-analyzer`) |
| KB mirror | [`projects/esp32-bt-analyzer/applications/bmw-nbt-evo.md`](../../projects/esp32-bt-analyzer/applications/bmw-nbt-evo.md) |

Epistemik: **FIELD FACT** für diesen F20-Termin. Kein Transfer auf andere NBT-SWFL ohne Capture.

## Alle advertised Records

Attribute-IDs: `0x0000` Handle · `0x0001` ServiceClassIDList · `0x0004` ProtocolDescriptorList ·
`0x0005` BrowseGroup · `0x0006` LanguageBase · `0x0009` BluetoothProfileDescriptorList ·
`0x0100` ServiceName · (+ profilspezifisch).

| Handle | Service Name | Service Class UUID(s) | RFCOMM ch | L2CAP PSM | Profile / Version | Features | Attr IDs |
|--------|--------------|----------------------|-----------|-----------|-------------------|----------|----------|
| 6 | `ALPS_MNS_SERVER1` | `0x1133` MAP-MNS | **1** | — | MAP `0x1134` **1.2** | — | 0000 0001 0004 0005 0006 0009 0100 0200 0317 |
| 2 | `ALPS_HFM` | `0x111e` HFP, `0x1203` GenericAudio | **2** | — | HFP **1.6** | `0x003f` | 0000 0001 0004 0005 0006 0009 0100 0311 |
| 1 | `SPP Server 0` | `00000000-deca-fade-deca-deafdecacaff` | **5** | — | same UUID **1.2** | — | 0000 0001 0004 0005 0006 0009 0100 |
| 9 | `SPP Server 1` | `0x1101` SPP | **6** | — | SPP **1.2** | — | 0000 0001 0004 0005 0006 0009 0100 |
| 10 | `SPP Server 2` | `0x1101` SPP | **7** | — | SPP **1.2** | — | …same… |
| 11 | `SPP Server 3` | `0x1101` SPP | **8** | — | SPP **1.2** | — | …same… |
| 12 | `SPP Server 4` | `0x1101` SPP | **9** | — | SPP **1.2** | — | …same… |
| 13 | `SPP Server 5` | `0x1101` SPP | **10** | — | SPP **1.2** | — | …same… |
| 7 | `OBEX Object Push` | `0x1105` OPP | **11** | — | OPP **1.2** | — | + 0200 0303 |
| 8 | *(none)* | `0x1200` PnP | — | — | — | — | 0000 0001 0005 0006 0200–0205 |
| 4 | `A2DP SNK` *(ALPS label)* | `0x110e` AVRCP, `0x110f` CT | — | **23** | AVRCP **1.5** | `0x004d` | + 000d 0102 0311 |
| 3 | `A2DP SNK` | `0x110b` A2DP-Sink | — | **25** | A2DP **1.3** | `0x000f` | + 0102 0311 |

## Protocol Descriptor (SPP-relevante)

Für alle SPP-/`deca-fade`-Records ist Attr `0x0004` (ProtocolDescriptorList) vorhanden.
Decoder speichert den Kanal als `rfcomm_channel` — typisches **L2CAP → RFCOMM(SCN)** Muster
(kein zusätzliches OBEX auf ch 5–10). Exakte Byte-Sequenz der Descriptor-Liste ist im JSON
nicht separat expandiert; Kanalzuordnung ist MEASURED.

## Was **nicht** advertisiert wird (Negativ, MEASURED)

| UUID / Name | Present on stock F20 SDP? |
|-------------|---------------------------|
| `4de17a00-52cb-11e6-bdf4-0800200c9a66` (Android Auto / NBT-AAD) | **Nein** |
| Service Name `AndroidAuto` | **Nein** |
| Proprietäre BMW-„BCL“-UUID (nicht `0x1101`) | **Nein** (Connected nutzt generisches SPP) |
| `d31fbf50-5d57-2797-a240-41cd484388ec` (Fremd-Logcat secondary) | **Nein** in state A/B |

## Connected-Zuordnung (CROSSREF Feld, nicht SDP allein)

| Claim | Status | Quelle |
|-------|--------|--------|
| Android `createRfcommSocketToServiceRecord(0x1101)` → first match = **ch 6** | FACT/MEASURED | B1 decode + BclCarLink `SDP_BCL` |
| BCL Session auf **SCN 6**, Failover **SCN 10** | MEASURED | `FIELD_P0_HOLD_*`, Deep Forensic 2026-11-16 |
| ch 5 `deca-fade` = Apple iAP2/MFi, nicht Android BCL | FACT/MEASURED | B2 + Sheet |
| State A: kein SABM auf ch 5–10 | MEASURED | B1 RFCOMM sessions (nur HFP) |

## UUID-Mengen-Übersicht

```
Stock F20 (this capture):
  0x1101, 0x1105, 0x110b, 0x110e, 0x110f, 0x111e, 0x1133, 0x1200, 0x1203,
  00000000-deca-fade-deca-deafdecacaff

NBT-AAD registers (daemon, modified HU):
  4de17a00-52cb-11e6-bdf4-0800200c9a66  name=AndroidAuto
  (on top of whatever stock + Connectivity already has)

BclCarLink / Connected client lookup:
  00001101-0000-1000-8000-00805F9B34FB  (= 0x1101)
```
