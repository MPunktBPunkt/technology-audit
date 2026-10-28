/**
 * Minimal ESP32-S3 CSI RAW instrument (A0).
 * Pattern: esp-csi get-started/csi_recv (CSI config + CB; promiscuous required for set_csi).
 * No motion/presence/derived features. Not rfmonitor.
 */
#include <Arduino.h>
#include <WiFi.h>
#include <string.h>

#include "esp_wifi.h"
#include "esp_err.h"

#ifndef RFSENSE_SSID
#define RFSENSE_SSID "RFSENSE_N"
#endif
#ifndef RFSENSE_PASS
#define RFSENSE_PASS "rfsense_n"
#endif
#ifndef RFSENSE_CHANNEL
#define RFSENSE_CHANNEL 6
#endif

static volatile uint32_t g_device_seq = 0;
static volatile uint32_t g_csi_ok = 0;
static portMUX_TYPE g_mux = portMUX_INITIALIZER_UNLOCKED;

static void wifi_csi_rx_cb(void *ctx, wifi_csi_info_t *info) {
  (void)ctx;
  if (!info || !info->buf || info->len == 0) {
    return;
  }

  uint32_t seq;
  portENTER_CRITICAL(&g_mux);
  seq = g_device_seq++;
  g_csi_ok++;
  portEXIT_CRITICAL(&g_mux);

  const wifi_pkt_rx_ctrl_t *rx = &info->rx_ctrl;

  /* One line: CSI_RAW,...  Host adds host time / host seq. */
  Serial.printf(
      "CSI_RAW,%u,%u,%d,%d,%u,%u,%u,%u,%u,%u,%u,%02X%02X%02X%02X%02X%02X,%d,%u,",
      (unsigned)seq,
      (unsigned)rx->timestamp,
      (int)rx->rssi,
      (int)rx->noise_floor,
      (unsigned)rx->channel,
      (unsigned)rx->secondary_channel,
      (unsigned)rx->rate,
      (unsigned)rx->sig_mode,
      (unsigned)rx->mcs,
      (unsigned)rx->cwb,
      (unsigned)rx->sig_len,
      info->mac[0], info->mac[1], info->mac[2], info->mac[3], info->mac[4], info->mac[5],
      info->first_word_invalid ? 1 : 0,
      (unsigned)info->len);

  for (uint16_t i = 0; i < info->len; i++) {
    if (i) {
      Serial.print(',');
    }
    Serial.print((int)info->buf[i]);
  }
  Serial.print('\n');
}

static bool csi_start() {
  /* Required by IDF/esp-csi for esp_wifi_set_csi — not a Promiscuous-PCAP product path. */
  esp_err_t err = esp_wifi_set_promiscuous(true);
  if (err != ESP_OK) {
    Serial.printf("INSTR_ERR promiscuous %s\n", esp_err_to_name(err));
    return false;
  }

  wifi_csi_config_t cfg = {
      .lltf_en = true,
      .htltf_en = true,
      .stbc_htltf2_en = true,
      .ltf_merge_en = true,
      .channel_filter_en = false,
      .manu_scale = false,
      .shift = 0,
  };
  err = esp_wifi_set_csi_config(&cfg);
  if (err != ESP_OK) {
    Serial.printf("INSTR_ERR csi_config %s\n", esp_err_to_name(err));
    return false;
  }
  err = esp_wifi_set_csi_rx_cb(wifi_csi_rx_cb, NULL);
  if (err != ESP_OK) {
    Serial.printf("INSTR_ERR csi_cb %s\n", esp_err_to_name(err));
    return false;
  }
  err = esp_wifi_set_csi(true);
  if (err != ESP_OK) {
    Serial.printf("INSTR_ERR csi_enable %s\n", esp_err_to_name(err));
    return false;
  }
  return true;
}

void setup() {
  Serial.begin(921600);
  delay(200);
  Serial.println();
  Serial.println("INSTR s3-csi-raw boot");
  Serial.printf("INSTR join ssid=%s ch=%d\n", RFSENSE_SSID, RFSENSE_CHANNEL);

  WiFi.mode(WIFI_STA);
  WiFi.setSleep(false);
  WiFi.begin(RFSENSE_SSID, RFSENSE_PASS);

  uint32_t t0 = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - t0 < 20000) {
    delay(200);
    Serial.print('.');
  }
  Serial.println();

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("INSTR_ERR wifi_connect_timeout");
    return;
  }

  Serial.printf("INSTR wifi_ok ip=%s rssi=%d\n",
                WiFi.localIP().toString().c_str(), WiFi.RSSI());

  esp_wifi_set_ps(WIFI_PS_NONE);

  if (!csi_start()) {
    Serial.println("INSTR_ERR csi_start_failed");
    return;
  }

  Serial.println("INSTR_READY");
  Serial.println(
      "CSI_RAW_HEADER,device_seq,device_ts,rssi,noise_floor,channel,secondary,"
      "rate,sig_mode,mcs,cwb,sig_len,mac,first_word_invalid,len,iq...");
}

void loop() {
  static uint32_t last = 0;
  uint32_t now = millis();
  if (now - last >= 5000) {
    last = now;
    uint32_t ok, seq;
    portENTER_CRITICAL(&g_mux);
    ok = g_csi_ok;
    seq = g_device_seq;
    portEXIT_CRITICAL(&g_mux);
    Serial.printf("INSTR_STAT csi_ok=%u next_seq=%u wifi=%d\n",
                  (unsigned)ok, (unsigned)seq, (int)WiFi.status());
  }
}
