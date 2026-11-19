# APK Inventory

## Ergebnis

| Ziel | Status |
|------|--------|
| MyBMW (`de.bmw.connected.mobile20.*`) | **NOT FOUND** |
| BMW Connected Classic | **NOT FOUND** |
| adb device | **none attached** |

## Suche (2026-11-19)

| Ort | Ergebnis |
|-----|----------|
| `/home/martin/projects/**` | keine `*.apk` |
| `/home/martin/Downloads`, Desktop, Documents | leer / keine APK |
| `/home/martin/.cursor/projects/.../uploads` | kein uploads-Verzeichnis mit APK |
| `/tmp` | nur BimmerGestalt Git-Clones (kein OEM APK) |
| `adb devices` | leere Geräteliste |
| `find /home/martin -name '*.apk'` | keine Treffer |

Auftragstext: „Für die bereitgestellten APKs“ — im Chat/Workspace **keine** Anhänge gefunden.

## Erwartete Felder (leer — Template für Folge)

| Feld | MyBMW | Classic |
|------|-------|---------|
| package name | — | — |
| versionName / versionCode | — | — |
| ABI (`lib/<abi>/`) | — | — |
| `lib/*/*.so` (security-relevant) | — | — |
| Klassen hits: SecurityModule, signChallenge, … | — | — |

## Was wir **ohne** APK schon wissen (Package-Namen only)

Aus Kit `KnownSecurityServices` (nicht inventarisiert auf dem OnePlus):

| Region | MyBMW package |
|--------|---------------|
| ROW | `de.bmw.connected.mobile20.row` |
| NA | `de.bmw.connected.mobile20.na` |
| CN/HK/KR | `…cn` / `…hm` / `…kr` |
| Mini / J29 | `de.mini…` / `de.j29…` |

Klassennamen (Kit Reflect-Ziel):  
`com.bmwgroup.connected.core.security.SecurityModule`  
Fallback: `com.bmwgroup.connected.core.audio.AudioModule`

## Unblock

```bash
# auf dem Phone
adb shell pm path de.bmw.connected.mobile20.na   # oder .row
adb pull <path> ./mybmw.apk

# optional Classic
adb shell pm path com.bmwgroup.connected.bmw
```

APK-Pfad hier ablegen oder im nächsten Prompt nennen → Inventar nachziehen.
