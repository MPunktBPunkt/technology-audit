# Follow-on ideas (aus esp32-car-network-refs)

```yaml
reuse_outcomes:
  reused:
    - bt-dual-mode-coex
    - esp32-s3-usb-wifi-coex
    - iobroker-fritzwireguard-adapter
  new:
    - esp-wireguard
    - esp-wifi-nat-router
    - esp-tailscale-client
  not_helped:
    - "SoftAP-Wait als primäres Car-Rendezvous"
    - "reines WireGuard ohne erreichbaren Endpoint / ohne keepalive hinter NAT"
```

| Idee | Baut auf | Kurz |
|------|----------|------|
| Lab G-HOTSPOT: Phone AP → ESP STA → microlink DERP peer | esp-tailscale-client | A6 Reachability PoC |
| Lab G-WG-KA: esp_wireguard keepalive hinter Hotspot NAT | esp-wireguard | Peer-up vs connect ESP_OK trennen |
| Lab SoftAP+BT C1: nat_router SoftAP parallel Classic BT | esp-wifi-nat-router, bt-dual-mode-coex | Mess-Gate vor Car SoftAP |
| Optional Sheet `esp-wifi-bt-coex` | Espressif coexist C1 | wenn SoftAP+BT produktiv wird |
| bt-analyzer A6 hook: rendezvous statt SoftAP-Wait | esp-tailscale-client | Upstream `CAR_A6_B1` |
