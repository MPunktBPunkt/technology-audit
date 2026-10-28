# Follow-on ideas (aus bt-classic-profile-refs)

```yaml
reuse_outcomes:
  reused: [bluetooth-a2dp, avrcp, bluetooth-stack]
  new: [bluetooth-hfp, bluetooth-spp, bluetooth-hid, bt-dual-mode-coex, hid-cross-transport-bridge]
  not_helped: ["esp32-hsp-hf als HSP-Quelle — Code ist HFP HF", "IDF classic_bt als BTDM-Bridge-Vorbild — Examples BR/EDR-only"]
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| bt-gateway: HFP HF + A2DP Mux Policy | `bluetooth-hfp`, `bluetooth-a2dp` | Call vs Media I2S |
| Dual-Host ESP32 (NimBLE+Classic) Gate | `bt-dual-mode-coex`, EspBle | ESP32-only |
| SPP vs BLE-UART Entscheidungstabelle | `bluetooth-spp`, transparent-bridge | Produktwahl |
| Classic HID Host Lab | `bluetooth-hid` | IDF Example fehlt |
| Sibling-Inventare a2dpsinkhfpclient/espble HFP → applied | `bluetooth-hfp` | Nachzug |
