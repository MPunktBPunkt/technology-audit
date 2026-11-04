# Audit Campaign: esp32-bt-analyzer-host-profiles-2026-desk

```yaml
id: esp32-bt-analyzer-host-profiles-2026-desk
project_id: esp32-bt-analyzer
started: 2026-11-04
ended: 2026-11-04
status: closed
profile: lab-tool
standard_version: "0.7.1"
reviewed_commit: "desk-multi-2026-11-04"
upstream_pins:
  esp32.bt-analyzer: "0.3.0"
  btstack: "master docs + hog_host_demo"
  esp-idf: "examples/bluetooth (gatt_client, nimble/blecent, classic_bt)"
  zephyr: "docs LE Host + HOGP RFC #108582"
  python-pyftms: "v0.4.x / Apache-2.0"
  FTMS.NET: "0.7.0 GPL-3.0"
  HOGP-BLE-HID-EXAMPLE: "TI device demo"
  bluez: "reference only"
  bluetooth_stack: "6ef9436 prior pin"
reuse_outcomes:
  reused:
    - bluetooth-ftms
    - bluetooth-hid
    - bluetooth-hfp
    - bluetooth-a2dp
    - bluetooth-spp
    - bt-dual-mode-coex
    - ble-hrm-gatt
    - bt-passive-host-sniff
  new_candidates:
    - bt-analyzer-flavor-bus
    - ble-gatt-client-fsm
    - hogp-host-client
  not_helped:
    - "BTstack as vendored commercial host (non-commercial public license)"
    - "FTMS.NET code reuse (GPL-3)"
    - "TI HOGP example as Host reference (Device-only)"
    - "BlueZ as ESP32 port target"
    - "Full Classic A2DP/HFP on Analyzer Core capture path"
  process: "Desk multi-repo Pattern Audit for Analyzer-Core + Profile-Flavor design; no live MEASURED."
  decisions_touched:
    - fact-btstack-best-pattern-not-vendor
    - fact-nimble-runtime-for-ble-flavors
    - fact-flavor-stimulus-must-be-timeline-tagged
    - reject-full-host-on-analyzer-core
    - recommend-gatt-client-first-mvp
```

## Ziel

Structured technology audit of open-source Bluetooth Host / Profile stacks to extract **reusable patterns** (APIs, FSMs, parsers, layering) for **Profile Flavors** on `esp32.bt-analyzer` **0.3.0** — without turning the Analyzer Core into a general Host.

Preserved principle (upstream + project SCOPE):

- **Analyzer Core** = pure measurement (VHCI HCI capture, BTAC, PSRAM ring, loss metrics, timeline).
- **Profile Flavors** = optional Stimulus / Client modules, independently enableable.
- Any Host-side influence on the measurement path must stay **visible and measurable**.

## Scope

Desk only. No Lab MEASURED in this campaign. Builds on prior KB:

| Prior | Role here |
|-------|-----------|
| [`ble-gatt-bridge-refs-2026-foreign`](../ble-gatt-bridge-refs-2026-foreign/) | Dual-Role / CCCD / Control-Point patterns |
| [`bt-classic-gaps-2026-foreign`](../bt-classic-gaps-2026-foreign/) | HFP/SPP/HID/Dual-Mode taxonomy |
| [`bluetooth-stack-2026-foreign`](../bluetooth-stack-2026-foreign/) | Lightweight HCI-host contrast |
| Sheets `bluetooth-ftms`, `bluetooth-hid`, … | Profile contracts |
| Method [`ftms-capability-probe`](../../methods/ftms-capability-probe.md) | FTMS Flavor probe contract |

**Im Scope:** Architecture separation, GATT Client FSM, HOGP Host, FTMS parsers, Classic dependency graph, ESP32 integration fit, licensing.

**Nicht im Scope:** RF/Air (BT15), MITM, bond decryption, shipping a Flavor in this campaign.

## Exit-Kriterien

| # | Kriterium | Status |
|---|-----------|--------|
| 1 | Executive summary + adoption order | erfüllt |
| 2 | Per-repo findings (primary + secondary) | erfüllt |
| 3 | Flavor design recommendations (Core clean) | erfüllt |
| 4 | Risk matrix (capture / mem / dual-mode) | erfüllt |
| 5 | Next steps starting with GATT Client Flavor | erfüllt |
| 6 | Evidence desk-links in `evidence.md` | erfüllt |
| 7 | Project FOLLOW-ON updated | erfüllt |

---

## 1. Executive Summary

### Recommended primary sources

| Priority | Source | Use as | Do **not** use as |
|----------|--------|--------|-------------------|
| **P0** | **ESP-IDF NimBLE** (`blecent` + GATTC) | Runtime for BLE Flavors on `.88/.89` (and BLE half of `.87`) | Full product Host replacing Analyzer Core |
| **P0** | **BTstack** architecture + `hids_host` / GATT Service Clients | **Pattern bible**: Core protocols ↔ independent profile clients, async FSM, bounded descriptor storage | Vendored stack (public license = non-commercial) |
| **P1** | **Zephyr** LE Host + GATT Client APIs (+ HOGP Host RFC) | Clean callback/Kconfig layering; ATT-timeout→disconnect; multi-conn model | Drop-in ESP32 host (different RTOS) |
| **P1** | **python-pyftms** (Apache-2.0) | FTMS realtime + Control Point **parser models** | On-chip stack |
| **P2** | ESP-IDF **Bluedroid** `classic_bt` + prior Classic-gaps sheets | Classic Flavors on **`.87` only** | Default for S3 BLE analyzer path |
| **P3** | BlueZ / TI HOGP / FTMS.NET / bluetooth_stack | Spec/contrast / Device layout / learning | Product code paths on analyzer |

### Adoption order (Flavors)

1. **GATT Client Flavor (MVP)** — discovery + MTU + CCCD subscribe + long read; all TX tagged `STIMULUS`.
2. **HOGP Host Flavor** — on top of GATT Client; Report Map storage + Input Report notify path; Boot optional.
3. **FTMS (+ related) Flavor** — parser from pyftms models; Control Point Indicate/Notify quirks from existing FTMS sheet.
4. **Classic Profile Flavors** (`.87`) — SDP/RFCOMM first; HID Host; A2DP/HFP/AVRCP only as **opt-in heavy** flavors with hard capture-budget gates.

**Verdict:** Keep Analyzer Core; implement Flavors as **BTstack-style Service Clients** over the existing thin HCI/VHCI host — preferably NimBLE GATTC for BLE — with mandatory stimulus accounting into the capture timeline.

---

## 2. Per-repository findings

### 2.1 BTstack (primary) — https://github.com/bluekitchen/btstack

| Axis | Finding |
|------|---------|
| **Architecture** | Collection of cooperating **state machines**; single-threaded run loop; non-blocking; optional statically bounded memory. Clear layering: HCI → L2CAP/ATT/SM → **GATT Client** → **GATT Service Clients** (e.g. HOGP Host) → app packet handlers. Maps almost 1:1 to **Analyzer Core + Flavor**. |
| **Separation** | Profiles do not own HCI. Service clients sit **above** `gatt_client_*` and emit `GATTSERVICE_SUBEVENT_*`. Multi-connection via configurable max connections/channels. |
| **GATT Client** | Async queries; Service Clients encapsulate discovery→subscribe. Pairing via SM events before profile connect (see HOGP demo). |
| **HOGP** | `hids_host_init(descriptor_storage, len)` + `hids_host_connect(handle, handler, protocol_mode, &cid)`. Demo FSM: `W4_WORKING → … → W4_ENCRYPTED → W4_HID_CLIENT_CONNECTED → READY` with reconnect timers. Report Map buffered in caller-provided storage; Boot vs Report via `hid_protocol_mode_t`; reports via `GATTSERVICE_SUBEVENT_HID_REPORT` + `btstack_hid_parser_*`. |
| **Classic** | Full set: SDP, RFCOMM/SPP, A2DP, AVRCP, HFP HF/AG, Classic HID Host/Device. Mature dependency graph (AVDTP/AVCTP under A2DP/AVRCP). |
| **ESP32** | Official FreeRTOS port exists — but adopting whole stack **conflicts** with existing VHCI Analyzer Core + IDF controller ownership. |
| **License** | Public: BSD-like **+ clause 4 non-commercial**. Commercial license required for product shipping of **code**. |
| **Reuse** | **Extract patterns/FSM/API shape.** Do not vendor without commercial license. |
| **Weakness** | License; dual-runloop vs FreeRTOS tasks; would fight capture ring ownership if taken as whole host. |

**Evidence:** `EVID-BTHPF-2026-11-04-001` … `003`.

### 2.2 ESP-IDF (primary) — https://github.com/espressif/esp-idf

| Axis | Finding |
|------|---------|
| **Architecture** | Controller ↔ Host via VHCI (same plane Analyzer already taps). Host choices: **Bluedroid** (Classic+BLE) or **NimBLE** (BLE). Profiles are Kconfig-gated modules; examples are BR/EDR-only for Classic (prior: IDF ≠ BTDM SoT). |
| **GATT Client (Bluedroid)** | Event FSM: connect → MTU req → `DIS_SRVC_CMPL` → `search_service` → char/descr → `register_for_notify` + CCCD write. Cache in NVS possible (`SERVICE_FROM_NVS_FLASH`). |
| **GATT Client (NimBLE blecent)** | Cleaner peer model: `peer_disc_all` → svcs → chrs → dscs → complete callback → read/write/subscribe. Encryption / EATT gating documented (ops after `ENC_CHANGE` / `EATT`). |
| **HOGP** | No first-class HOGP **Host** example equivalent to BTstack `hids_host`. HID examples skew Device / Classic. Host must be composed on GATTC. |
| **Classic** | A2DP Sink/Source, AVRCP, HFP HF/AG, SPP, HID Device. A2DP: typically SBC, one connection, heavy I2S/DMA; `mem_release(BLE)` in Classic-only examples. |
| **Fit** | **Best runtime** for Flavors that must share the on-chip controller with Analyzer Core — but Flavor code must sit **beside** capture, not replace VHCI sniff. |
| **License** | Apache-2.0. |
| **Weakness** | Bluedroid opaque + RAM-heavy; Classic examples teach wrong coex defaults; GATTC cache can hide live discovery cost from measurement unless forced refresh. |

**Evidence:** `EVID-BTHPF-2026-11-04-010` … `014`.

### 2.3 Zephyr (primary) — https://github.com/zephyrproject-rtos/zephyr

| Axis | Finding |
|------|---------|
| **Architecture** | HCI driver → GAP roles (Kconfig) → L2CAP/ATT/GATT/SM → services. Host callbacks must stay short; work deferred — matches “don’t block capture” rule. |
| **GATT Client** | Central samples (`central_hr`): scan → connect → discover → subscribe. ATT timeout ⇒ auto-disconnect (simplifies Flavor error path). Security levels L1–L4 via `bt_conn_set_security` / auth callbacks. |
| **HOGP** | Device/HID Service samples exist; **HOGP Host** is an active RFC (`#108582`): proposed 18-state discovery FSM, `bt_hogp_host_connect()`, BAS/DIS auto-discover, Input Report auto-subscribe. Treat as **design reference**, not stable merge pin. |
| **Multi-conn** | Connection objects + per-conn GATT; Kconfig buffer counts (`BT_ATT_TX_COUNT`, ACL RX size = MPS). |
| **License** | Apache-2.0. |
| **Reuse** | FSM shapes, callback discipline, Kconfig-style Flavor feature flags. Not a drop-in ESP port. |
| **Weakness** | Classic profiles secondary; HOGP Host not a frozen SoT yet. |

**Evidence:** `EVID-BTHPF-2026-11-04-020` … `022`.

### 2.4 python-pyftms (secondary) — https://github.com/dudanov/python-pyftms

| Axis | Finding |
|------|---------|
| **Role** | Async FTMS **client library** (Bleak). Models: Features, Machine Status, Training Status, Control Point, Spin-Down, per-machine realtime (Treadmill / Cross Trainer / Rower / Indoor Bike). |
| **Control Point** | Opcode/result model aligns with SIG; response `0x80` + result codes. |
| **Notify vs Indicate** | Client abstracts transport; our sheet already warns some devices Notify Control Point instead of Indicate. |
| **License** | **Apache-2.0** — preferred parser extraction source. |
| **Reuse** | Port **serializers / flag parsers / opcode tables** into FTMS Flavor; keep transport = our GATT Client Flavor. |

**Evidence:** `EVID-BTHPF-2026-11-04-030`.

### 2.5 FTMS.NET (secondary) — https://github.com/nilsauf/FTMS.NET

| Axis | Finding |
|------|---------|
| **Role** | .NET FTMS client; transport-agnostic via `IFitnessMachineServiceConnection`. Explicitly does **not** trust Feature flags for gating writes (matches our `REJECTED` claims). |
| **License** | **GPL-3.0** — reference / API shape only; **no code copy** into analyzer. |
| **Reuse** | Validate quirks (VanRysel etc.); reinforce “read Features, don’t blindly trust”. |

**Evidence:** `EVID-BTHPF-2026-11-04-031`.

### 2.6 TI HOGP-BLE-HID-EXAMPLE (secondary)

| Axis | Finding |
|------|---------|
| **Role** | **HID Device** (keyboard/mouse/consumer) on CC26x2 — Report Map layout, Report Reference descriptors, Boot characteristics. |
| **Not** | HID Host / Report Map parser Host. |
| **Reuse** | Golden peer for HOGP Flavor Lab; document expected GATT tree. |

**Evidence:** `EVID-BTHPF-2026-11-04-040`.

### 2.7 BlueZ (secondary, reference)

| Axis | Finding |
|------|---------|
| **Role** | Linux Host reference (D-Bus profiles, mgmt/HCI). Excellent for **expected Host behavior** and PCAP comparison vs BTAC. |
| **Not** | ESP32 port. GPL-2.0. |
| **Reuse** | Lab oracle: same peer session BlueZ vs Analyzer+Flavor. |

### 2.8 sj157…/bluetooth_stack (secondary)

| Axis | Finding |
|------|---------|
| **Role** | Educational dual-mode HCI-up stack (STM32/Linux); A2DP/HFP/GATT present. Prior audit: “ESP32” in matrix can mean **controller-only**. |
| **License** | No clear OSI license in README — treat as **read-only contrast**. |
| **Reuse** | Teaching HCI layering; not production Flavor source. |

---

## 3. Answers to audit questions (cross-cutting)

### 3.1 Architecture & Separation

| Source | Core ↔ Profile | Multi-conn |
|--------|----------------|------------|
| BTstack | Best explicit Service-Client boundary | Configured maxima |
| Zephyr | Kconfig roles + service modules | `bt_conn` objects |
| ESP-IDF | Host monolithic; apps compose events | Bluedroid apps / NimBLE peers |
| Analyzer target | **Core owns VHCI RX/TX accounting**; Flavors own profile FSMs only | Cap connections per Flavor Kconfig |

**Map:** BTstack Service Client ≈ our **Profile Flavor**. Analyzer Core ≈ HCI capture + thin GAP already present — **not** Bluedroid BTC.

### 3.2 GATT Client

Canonical FSM to implement (compose NimBLE peer_disc + BTstack service-client habit):

```text
IDLE → SCAN/FILTER → CONNECT → (optional MTU) → (optional PAIR/ENCRYPT)
    → DISCOVER_PRIMARY → DISCOVER_CHARS → DISCOVER_DESCS
    → SUBSCRIBE_CCCD → READY
Error anywhere → DISCONNECT / BACKOFF → IDLE|RECONNECT
```

| Concern | Pattern |
|---------|---------|
| Long reads | ATT Read Blob / iterative offset; log each HCI exchange as stimulus |
| MTU | Exchange before heavy discovery; record negotiated MTU in timeline |
| Notifications | Write CCCD after `register_for_notify` / NimBLE subscribe; never silent |
| Pairing | Explicit Flavor policy: none / JustWorks / bonded; SM complete **before** secure chars |
| Errors | Prefer Zephyr-like collapse: ATT timeout → disconnect → measurable gap in capture |
| Reconnect | BTstack HOG timers + bonded addr TLV pattern (our NVS) |

### 3.3 HOGP / HID Host

| Topic | Recommendation |
|-------|----------------|
| Report Map | Caller-owned buffer (BTstack `hid_descriptor_storage[]`); fail loud on overflow |
| Boot vs Report | Mode enum at connect; fallback Report→Boot optional (BTstack Classic HID has explicit fallback mode) |
| Subscribe | Auto-subscribe Input Reports after map read (Zephyr RFC / BTstack host) |
| Parser | Keep HID usage parser in Flavor; dump raw reports to JSONL always |
| Footprint | Descriptor buffer dominates (hundreds of bytes–KB per device); bound instances |
| RT | Report notify callbacks must not block capture task — queue to Flavor worker |

### 3.4 Fitness (FTMS etc.)

| UUID | Role |
|------|------|
| `0x1826` FTMS | Core |
| `0x2ACC` Features | Capability |
| `0x2AD2` Indoor Bike Data | Notify stream |
| `0x2AD9` Control Point | Write + Indicate (sometimes Notify) |
| `0x1818` CPS / `0x1816` CSC / `0x180D` HR | Related Flavors or sibling services |

Parsers: **pyftms models** + existing Method `ftms-capability-probe` + sheet `bluetooth-ftms` pitfalls (Success ≠ Wirkung; Feature bits ≠ IBD fields).

### 3.5 Classic Profiles (.87)

Dependency sketch:

```text
SDP
 └─ RFCOMM ─ SPP / HFP AT
L2CAP
 ├─ AVDTP ─ A2DP (+ SBC codec path)
 ├─ AVCTP ─ AVRCP
 └─ HID Control/Interrupt ─ Classic HID
```

| Profile | Analyzer suitability |
|---------|----------------------|
| SDP browse / RFCOMM echo | High (low bandwidth stimulus) |
| Classic HID Host | Medium (report rate vs ring) |
| AVRCP CT | Medium (commands, little audio) |
| A2DP Sink/Source | **Low on capture node** — audio DMA + ACL flood vs PSRAM ring |
| HFP + SCO | **Low** — realtime voice path; prior gaps already warn I2S mux |

Dual-mode: prior sheet `bt-dual-mode-coex`; Classic IDF examples often **release BLE memory** — incompatible with BLE capture Flavors unless deliberately BTDM-built.

### 3.6 Integration fit (esp32.bt-analyzer)

| Reuse almost directly | Adapt heavily |
|----------------------|---------------|
| BTstack HOG app FSM + reconnect | Whole BTstack as host |
| NimBLE `peer_disc_*` | Bluedroid as only path on S3 |
| pyftms opcode/flag parsers | pyftms Bleak transport |
| Zephyr ATT-timeout policy | Zephyr HCI driver |
| Existing thin ATT probe | Expand in-core without Flavor boundary |

**Interference risks (HCI capture / PSRAM / BTAC):**

1. Flavor TX floods ACL → ring pressure / loss metrics rise (**desired if tagged**; bad if silent).
2. Shared host task priority > capture consumer → delayed enqueue / soft loss.
3. Enabling Bluedroid Classic+A2DP on same node as high-rate HCI dump → CPU + DMA contention.
4. GATTC NVS cache → fewer discovery HCI packets → **understates** discovery cost unless `cache_refresh`.
5. Pairing/bonding flash writes during capture → jitter spikes.

### 3.7 Licensing, maintenance, practicality

| Repo | License | Activity | Portability |
|------|---------|----------|-------------|
| BTstack | Non-commercial public | High | ESP32 port exists; license blocks casual vendor |
| ESP-IDF | Apache-2.0 | Very high | Native |
| Zephyr | Apache-2.0 | Very high | Pattern only |
| pyftms | Apache-2.0 | Active | Parser port |
| FTMS.NET | GPL-3.0 | Niche | Reference |
| TI HOGP | TI example | Static | Device peer |
| BlueZ | GPL-2.0 | High | Host oracle |
| bluetooth_stack | Unclear | Niche | Learning |

---

## 4. Concrete recommendations for Profile Flavor design

### 4.1 Flavor Bus (minimal contract)

```text
Analyzer Core
  ├─ VHCI tap (RX+TX) → PSRAM ring → BTAC/JSONL/PCAPNG
  ├─ Timeline tags: CAPTURE | STIMULUS | METRIC
  └─ Flavor Bus API
        register / enable / disable
        on_hci_visible_tx(reason)   // Core stamps STIMULUS
        metrics_hook(loss, queue_hwm)
        Flavor N: FSM + parsers only
```

Rules:

1. Flavors **never** bypass the VHCI tap.
2. Every Flavor-initiated command carries a **reason code** into the timeline.
3. Flavors run on a **worker task** ≤ capture priority.
4. Compile-time flags: `FLAVOR_GATT_CLIENT`, `FLAVOR_HOGP`, `FLAVOR_FTMS`, `FLAVOR_CLASSIC_*`.
5. Runtime enable via lab UI / UART — default **off** for measurement purity.

### 4.2 MVP — GATT Client Flavor

Minimal viable size:

- Connect by addr / filter UUID
- Full primary discovery dump (handles + UUIDs → JSONL)
- MTU exchange
- Read / Write / Write-cmd
- CCCD subscribe + notify dump
- Optional JustWorks bonding gate
- Stimulus counters: cmds, bytes TX, notify RX, errors

Defer: multi-service parallel ops, EATT, robust bonding UI.

### 4.3 Then HOGP / FTMS

- HOGP = GATT Client + Report Map buffer + Input subscribe + optional Boot.
- FTMS = GATT Client + pyftms-derived parsers + Control Point indication waiter + capability probe mode (reuse Method).

### 4.4 Classic Flavors

- Separate binary or hard gate: only `.87`.
- Start SDP + RFCOMM; treat A2DP/HFP as **bench flavors** with explicit “capture degraded” banner.

---

## 5. Risk matrix

| Risk | Impact on measurement | Complexity | Memory | Dual-mode | Mitigation |
|------|----------------------|------------|--------|-----------|------------|
| Silent Host TX | High (false “air” narrative) | L | — | — | Mandatory `STIMULUS` tag |
| Capture task starved | High (loss) | M | — | — | Priority + queue HWM metrics |
| Full Bluedroid+A2DP on analyzer | High | H | H | H | Reject on Core; `.87` opt-in only |
| Vendoring BTstack | Legal | M | M | L | Patterns only / commercial license |
| GPL FTMS.NET copy | Legal | L | — | — | Use pyftms |
| GATTC cache hides discovery | Medium (wrong cost) | L | L | — | Force refresh in Flavor lab mode |
| HOGP Report Map overflow | Medium | M | M | — | Bounded storage + status event |
| FTMS Indicate vs Notify | Medium (stuck CP) | M | L | — | Dual CCCD strategy from sheet |
| Classic mem_release(BLE) | High (kills BLE capture) | L | — | H | BTDM build checklist |
| Multi-conn HID+FTMS | Medium | H | H | M | Cap `MAX_FLAVOR_CONNS=1` MVP |

Legend: L/M/H = Low/Medium/High.

---

## 6. Proposed next implementation steps

| Step | Deliverable | Exit |
|------|-------------|------|
| **S0** | Upstream doc: Flavor Bus contract + `STIMULUS` timeline tag schema | Review vs `SCOPE_HOST_VS_ANALYZER` |
| **S1** | GATT Client Flavor MVP (NimBLE path on `.88`) | Lab: discovery JSONL + notify with stimulus tags; loss metrics vs Flavor-off baseline |
| **S2** | Bonding policy + reconnection FSM (from BTstack HOG) | Bonded reconnect MEASURED |
| **S3** | HOGP Flavor (Report Map + Input) | Against TI/phone keyboard peer |
| **S4** | FTMS Flavor parsers (pyftms port) + capability probe mode | Cross-check vs `esp32.ftmsprobe` |
| **S5** | Classic SDP/RFCOMM Flavor on `.87` | HCI Classic stimulus tagged |
| **S6** | Gate A2DP/HFP as heavy flavors | Explicit degradation MEASURED or REJECTED for capture duty |

---

## Decision Trace

| Entscheidung | Frage | Evidence | Konsequenz | Zeitpunkt |
|--------------|-------|----------|------------|-----------|
| BTstack = pattern, not vendor | License OK to ship? | `…-001` | Patterns only | DISCOVERED |
| NimBLE = BLE Flavor runtime | Bluedroid or NimBLE? | `…-011` | NimBLE first | DISCOVERED |
| pyftms > FTMS.NET for code | GPL? | `…-030`/`…-031` | Apache parsers | DISCOVERED |
| TI HOGP ≠ Host | Host code? | `…-040` | Device peer only | DISCOVERED |
| A2DP not on Core | Capture interference? | prior Classic + IDF A2DP | Heavy Flavor / REJECTED default | KNOWN BEFORE |
| GATT Client first | Smallest Flavor? | cross-cut §3 | MVP order | DISCOVERED |

## Kill-Kriterien

| # | Kill wenn | Status |
|---|-----------|--------|
| 1 | No Core/Flavor separation found in sources | nicht eingetreten (BTstack/Zephyr) |
| 2 | Only GPL/non-commercial code as sole path | nicht eingetreten (IDF + Zephyr + pyftms) |

```text
NO JUSTIFIED KILL CRITERION
Begründung: Pattern sources + Apache runtime/parsers exist; Flavors remain design FOLLOW-ON for upstream FW.
```

## Bezug

- Project: [`esp32-bt-analyzer`](../../projects/esp32-bt-analyzer/)
- Evidence: [`evidence.md`](evidence.md)
- Prior: [`bt-classic-gaps-2026-foreign`](../bt-classic-gaps-2026-foreign/), [`ble-gatt-bridge-refs-2026-foreign`](../ble-gatt-bridge-refs-2026-foreign/)
