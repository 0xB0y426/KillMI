import subprocess
import re
import os
import time

os.system("cls" if os.name == "nt" else "clear")

def get_adb_devices():
    result = subprocess.run(
        ["adb", "devices"],
        capture_output=True,
        text=True
    )

    devices = []

    for line in result.stdout.splitlines():
        if not line.strip() or "List of devices" in line:
            continue

        match = re.match(r"(\S+)\s+(\S+)", line)
        if match:
            serial, status = match.groups()
            devices.append({
                "serial": serial,
                "status": status
            })

    return devices

def adb_exec(cmd):
    exec_command = subprocess.run(
        ["adb"] + cmd,
        capture_output=True,
        text=True
    )

    return exec_command.stdout

def main():
    print("\033[31m" + r"""
 ██ ▄█▀ ██▓ ██▓     ██▓     ███▄ ▄███▓ ██▓
 ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓██▒▀█▀ ██▒▓██▒
▓███▄░ ▒██▒▒██░    ▒██░    ▓██    ▓██░▒██▒
▓██ █▄ ░██░▒██░    ▒██░    ▒██    ▒██ ░██░
▒██▒ █▄░██░░██████▒░██████▒▒██▒   ░██▒░██░
▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░ ▒░   ░  ░░▓  
░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░░  ░      ░ ▒ ░
░ ░░ ░  ▒ ░  ░ ░     ░ ░   ░      ░    ▒ ░
░  ░    ░      ░  ░    ░  ░       ░    ░  
""" + "\033[0m")
    print("\033[31m        Debloat your xiaomi now.\033[0m")

    devices = get_adb_devices()
    
    if not devices:
        print("\n[!] Devices not found: Please, connect your device into your computer.")
        exit()

    print(f"\n[+] Device found: {devices[0]["serial"]}")

    print("\nReady to start debloat? This tool remove a lot of apps! y/n")
    choice = input(">> ")
    
    if choice == "y":
        debloat()
    elif choice == "n":
        print("[*] By3!")
        exit()
    else:
        print("\n[!] Invalid Option.")
        exit()


def debloat():
    print("[+] STARTING DEBLOAT")

    packages_to_remove = {
    "com.miui.msa.global": "Main system ads service",
    "com.miui.analytics": "Usage statistics and telemetry collection",
    "com.miui.daemon": "Background performance and usage tracking",
    "com.miui.bugreport": "Error logging and report uploading",
    "com.miui.extservices": "Additional data collection service",
    "com.miui.hybrid": "Quick Apps engine linked to persistent ads",
    "com.miui.hybrid.accessory": "Quick Apps accessory component",
    "com.miui.trackingprovider": "System tracking provider framework",
    "com.miui.cit": "Hardware test logging utility running in background",
    "com.miui.cleanmaster": "CleanMaster SDK inside Security app",
    "com.miui.klo.bugreport": "KLO bug reporting telemetry framework",
    "com.miui.vsimcore": "Virtual SIM background telemetry service",
    "com.google.android.as": "Android System Intelligence tracking usage habits",
    "com.google.android.feedback": "Google feedback and usage reporting stub",
    "com.google.android.apps.tachyon": "Google Duo / Meet video calling bloatware",
    "com.google.android.projection.gearhead": "Android Auto background connectivity logs",
    "com.google.android.marvin.talkback": "TalkBack accessibility screen-reading telemetry",
    "com.google.android.printservice.recommendation": "Print service recommendation engine",
    "com.android.printspooler": "System print spooler tracking local network documents",
    "com.miui.cloudservice": "Mi Cloud account syncing infrastructure",
    "com.miui.cloudservice.sysbase": "Core background cloud dependency",
    "com.miui.cloudbackup": "Automated remote backup scheduler",
    "com.miui.micloudsync": "Active synchronization manager",
    "com.miui.mishare.connectivity": "Mi Share proximity data transfer data logger",
    "com.xiaomi.miplay_client": "Mi Play media casting tool",
    "com.xiaomi.mi_connect_service": "Ecosystem connectivity background scanner",
    "com.milink.service": "Smart screen mirroring backend telemetry",
    "com.android.bips": "Default built-in printing share service",
    "com.xiaomi.mipicks": "GetApps alternative marketplace",
    "com.xiaomi.glgm": "Mi Games hub and promotions store",
    "com.xiaomi.gamecenter.sdk.service": "Game center tracking framework",
    "com.xiaomi.payment": "Mi Wallet transactional service",
    "com.facebook.system": "Pre-installed Facebook framework stub",
    "com.facebook.appmanager": "Background Facebook updater service",
    "com.facebook.services": "Pre-loaded Facebook background metrics",
    "com.netflix.partner.activation": "Netflix carrier stub activator",
    "com.netflix.mediaclient": "Pre-installed Netflix app",
    "com.tencent.soter.soterserver": "Tencent biometric authentication payment standard",
    "com.mi.globalbrowser": "Mi Browser default web navigation app",
    "com.miui.quicksearchbox": "Native search bar widget tracking queries",
    "com.miui.android.fashiongallery": "Wallpaper Carousel promotional lockscreens",
    "com.miui.yellowpage": "Dialer integrated yellow pages directory",
    "com.mi.health": "Mi Health activity and step tracker",
    "com.xiaomi.scanner": "Built-in QR and document scanner",
    "com.miui.player": "Mi Music streaming application",
    "com.miui.video": "Mi Video player and content feed",
    "com.miui.compass": "Stock utility compass app",
    "com.miui.notes": "Stock Mi Notes app",
    "com.miui.weather2": "Stock Mi Weather ad-heavy alternative",
    "com.android.soundrecorder": "Stock Sound Recorder app",
    "com.miui.screenrecorder": "Stock Screen Recorder app",
    "com.android.calendar": "Stock Calendar tracking events locally",
    "com.miui.gallery": "Stock Gallery"
}

    for package, description in packages_to_remove.items():
        print(f"Removing: {package} ({description})")
        adb_exec(["shell", "pm", "uninstall", "--user", "0", package])
        time.sleep(1)

    print("Debloat finished, please, now reboot your cellphone!")

if __name__ == "__main__":
    main()
