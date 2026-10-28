/**
 * D1 Mini — profile N traffic only (Δt=20 ms → 50 pkts/s).
 * SoftAP RFSENSE_N; UDP to broadcast / connected STA. Logs tx_count.
 */
#include <Arduino.h>
#include <WiFi.h>
#include <WiFiUdp.h>

#ifndef RFSENSE_SSID
#define RFSENSE_SSID "RFSENSE_N"
#endif
#ifndef RFSENSE_PASS
#define RFSENSE_PASS "rfsense_n"
#endif
#ifndef RFSENSE_CHANNEL
#define RFSENSE_CHANNEL 6
#endif
#ifndef RFSENSE_UDP_PORT
#define RFSENSE_UDP_PORT 5000
#endif
#ifndef RFSENSE_DT_MS
#define RFSENSE_DT_MS 20
#endif

static WiFiUDP g_udp;
static uint32_t g_tx_count = 0;
static uint32_t g_next_tx_ms = 0;
static uint8_t g_payload[64];

void setup() {
  Serial.begin(115200);
  delay(200);
  Serial.println();
  Serial.println("INSTR d1-traffic-n boot");
  Serial.printf("INSTR profile=N dt_ms=%d port=%d ch=%d\n",
                RFSENSE_DT_MS, RFSENSE_UDP_PORT, RFSENSE_CHANNEL);

  WiFi.mode(WIFI_AP);
  WiFi.setSleep(false);
  bool ok = WiFi.softAP(RFSENSE_SSID, RFSENSE_PASS, RFSENSE_CHANNEL, false, 4);
  Serial.printf("INSTR softAP %s ip=%s\n", ok ? "ok" : "FAIL",
                WiFi.softAPIP().toString().c_str());

  memset(g_payload, 0xA5, sizeof(g_payload));
  g_udp.begin(RFSENSE_UDP_PORT);
  g_next_tx_ms = millis();
  Serial.println("INSTR_READY");
}

void loop() {
  uint32_t now = millis();
  if ((int32_t)(now - g_next_tx_ms) >= 0) {
    g_next_tx_ms += RFSENSE_DT_MS;
    if ((int32_t)(now - g_next_tx_ms) > 100) {
      /* avoid catch-up burst after stall */
      g_next_tx_ms = now + RFSENSE_DT_MS;
    }

    /* Broadcast on SoftAP subnet — S3 STA receives → CSI. */
    IPAddress bcast = WiFi.softAPIP();
    bcast[3] = 255;

    memcpy(g_payload, &g_tx_count, sizeof(g_tx_count));
    g_udp.beginPacket(bcast, RFSENSE_UDP_PORT);
    g_udp.write(g_payload, sizeof(g_payload));
    g_udp.endPacket();
    g_tx_count++;
  }

  static uint32_t last_log = 0;
  if (now - last_log >= 1000) {
    last_log = now;
    Serial.printf("TX_COUNT,%u,stations=%u\n",
                  (unsigned)g_tx_count, (unsigned)WiFi.softAPgetStationNum());
  }
}
