# Audit Campaign: signchallenge-native-localization-2026-11-19

```yaml
id: signchallenge-native-localization-2026-11-19
project_id: bimmergestalt-idrive-refs
started: 2026-11-19
ended: 2026-11-19
status: blocked   # missing MyBMW/Classic APK input
profile: planning
standard_version: "0.7.1"
continuation_of:
  - audits/signchallenge-pipeline-localize-2026-11-19/
  - audits/idriveconnectkit-securityaccess-2026-11-19/
apk_input: null
adb_devices: []
search_roots_checked:
  - /home/martin/projects
  - /home/martin/Downloads
  - /home/martin/.cursor/projects/.../uploads
  - /tmp
  - adb devices (empty)
```

## Fragestellung

Wo sitzt die Implementierungsgrenze von `SecurityModule.signChallenge(...)`?

```text
Java/Kotlin → JNI? → native .so? → RSA / Keystore / TEE / Binder?
```

Observe-only. Kein Key-Dump, kein Forge, kein Bypass.

## Status dieses Laufs

**INPUT BLOCKED:** Es wurden **keine** MyBMW- oder Connected-Classic-APKs im Workspace /
an diesem Chat gefunden. Ohne APK/Dex/`lib/*.so` kann JNI **nicht** als FACT bestätigt
werden — auch nicht „weil Tests native function sagen“.

| Geplant | Ergebnis |
|---------|----------|
| APK inventory | **BLOCKED** — keine APKs |
| signChallenge call-chain (OEM) | nur **externe** Kit-Oberfläche (Prior) |
| JNI/native mapping | **UNKNOWN** (keine `.so`) |
| Keystore/Binder inside OEM | **UNKNOWN** |
| Field crosswalk | strukturell (Prior MEASURED) — ohne Phone-Komponente-ID |

## Wichtigste FACTs (unverändert / Prior)

| FACT | Quelle |
|------|--------|
| Challenge 16 B nach `sas_certificate` | F20 DEEP_FORENSIC |
| `sas_login` 512-B Sig / 559-B Frame | F20 DEEP_FORENSIC |
| Kit ruft OEM `signChallenge(handle, challenge)` | KitAndroid `@4a567bc` |
| Classic = Binder `*.SECURITY_SERVICE`; MyBMW = in-process `SecurityModule` | Kit + Analysis |
| Analysis: JNI/NDK wird für Sign vorbereitet | `authentication.md` |
| Kit-Test Exception enthält `native function signChallenge` | androidTest |
| Algorithmus-Form XOR+MD5withRSA (Rekonstruktion) | Analysis + PrivateKeyHandling |

## Aktuelle Architektur (was lokalisiert ist)

```text
AAIdrive / Kit
  → SecurityAccess.signChallenge
      → [Classic] ICarSecurityService Binder     FACT (Kit)
      → [MyBMW]  SecurityModule via reflect      FACT (Kit surface)
          → ??? JNI / .so / Keystore / Binder    UNKNOWN ohne APK
              → 512-B signature
  → sas_login → HU
```

## Fall A/B/C/D (dieser Lauf)

| Fall | Status |
|------|--------|
| A Key in APK/managed | **UNKNOWN** (APK fehlt) |
| B Keystore/TEE | **UNKNOWN** |
| C OEM Binder (inner MyBMW) | Classic äußere IPC **FACT**; MyBMW-inner **UNKNOWN** |
| D JNI/native OEM lib | **STRONG INFERENCE** (Doc + Exception-String) — **nicht CONFIRMED** |

## Was weiterhin UNKNOWN

- Package/Version/ABI der installierten MyBMW-Build  
- `lib/*/*.so` Namen und `JNI_OnLoad` / `RegisterNatives`  
- Ob `signChallenge` selbst `native` deklariert ist  
- Keystore/KeyMint-Nutzung  
- Private-Key location  

## Nächster sinnvoller Schritt

1. MyBMW-APK (und optional Classic) bereitstellen: lokaler Pfad oder `adb pull $(adb shell pm path …)`.  
2. Diesen Audit mit Inventar + JADX/readelf-Katalog fortsetzen (observe-only).  
3. Parallel optional: Public-Key-Verify der Feld-512-B-Signatur (kein Key-Export).

## Artefakte

- [APK-INVENTORY.md](APK-INVENTORY.md)  
- [SIGNCHALLENGE-CALLCHAIN.md](SIGNCHALLENGE-CALLCHAIN.md)  
- [NATIVE-SECURITY-MAP.md](NATIVE-SECURITY-MAP.md)  
- [FIELD-CROSSWALK.md](FIELD-CROSSWALK.md)  

## Leitplanke

> Wir wollen wissen, **WO** die Signatur erzeugt wird — nicht den Schlüssel besitzen.
