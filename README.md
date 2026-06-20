# KillMI

KillMI is a lightweight Xiaomi/MIUI debloating tool that uses Android Debug Bridge (ADB) to remove or disable system applications related to telemetry, advertising, analytics, and background services.

It is designed to improve privacy, reduce background activity, and free system resources without requiring root access.

---

## Features

- No root required
- Uses ADB user-level package removal (`--user 0`)
- Works on any Android device with USB debugging enabled
- Targets MIUI telemetry, ads, and preinstalled bloatware
- Safe system partition (no flashing or modification of system image)
- Reversible changes via ADB

---

## How it works

KillMI communicates with Android devices through ADB (Android Debug Bridge), an official Google tool that allows command-line interaction with Android systems.

Using ADB, the script:

- Detects connected devices
- Executes shell commands remotely
- Removes applications for the current user only
- Leaves the system partition untouched

This means applications are not permanently deleted from the device, and can be restored later if needed.

---

## Requirements

### ADB (Android Debug Bridge)

ADB is part of the Android Platform Tools provided by Google.

---

### Linux (Debian / Ubuntu / Arch)

Install ADB:

```bash
sudo apt install adb
```

or:

```bash
sudo pacman -S android-tools
```

Verify installation:

```bash
adb version
```

---

### Windows

1. Download Android Platform Tools:
https://developer.android.com/tools/releases/platform-tools

2. Extract the ZIP file (example: `C:\platform-tools`)

3. Open CMD or PowerShell in the extracted folder:

```bash
adb version
```

4. (Optional) Add platform-tools to PATH for global usage

---

### Android setup

Enable USB debugging:

1. Open Settings
2. Go to About phone
3. Tap MIUI version 7 times to enable Developer Options
4. Go to Additional settings → Developer options
5. Enable USB debugging

---

## Usage

Run the tool:

```bash
python killmi.py
```

Steps:

1. Connect your Android device via USB
2. Authorize USB debugging on the phone
3. Confirm execution in the terminal
4. The debloating process will begin automatically

---

## What KillMI removes

KillMI targets packages commonly associated with telemetry, advertising, and preinstalled MIUI applications.

### MIUI telemetry and analytics

- MIUI Analytics services
- MIUI Daemon
- Bug report service
- Tracking provider framework
- Usage statistics collection services
- System performance logging services

---

### Advertising and promotional services

- MIUI Ads Service (MSA)
- GetApps (Xiaomi app store)
- Quick Apps framework
- Wallpaper Carousel ads module
- Mi Browser promotional components

---

### Cloud and sync services

- Mi Cloud service
- Mi Cloud backup
- Mi Sync framework
- Mi Share connectivity services

---

### Preinstalled Xiaomi applications

- Mi Video
- Mi Music
- Mi Health
- Mi Notes
- Mi Weather
- Mi Scanner
- Mi Compass
- Mi Gallery
- Mi Game Center
- Mi Wallet

---

### Third-party preinstalled services

- Facebook system services
- Netflix partner activation service
- Google feedback and telemetry components
- Android Auto projection services
- Print spooler services

---

## Important notes

- No root access is required
- Uses `pm uninstall --user 0`, which only removes apps for the current user
- System applications remain on the device and can be restored
- Some apps may return after system updates or factory reset
- Use at your own risk

---

## Restore removed applications

To restore a removed package:

```bash
adb shell cmd package install-existing <package.name>
```

---

## Disclaimer

This tool modifies user-level application availability using ADB commands. It does not modify system partitions or require root access. The author is not responsible for any unintended behavior, data loss, or system issues caused by usage.

Credits to Magnetron.
