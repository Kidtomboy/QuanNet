import subprocess
import sys
from typing import List, Dict

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.text import Text
from rich.style import Style

console = Console()

# Màu cho nhóm
GROUP_STYLES = {
    "Trình duyệt": "bold blue",
    "VPN": "bold green",
    "Mạng xã hội & Nhắn tin": "bold yellow",
    "Media": "bold red",
    "Lập trình & Công cụ dev": "bold magenta",
    "Torrent": "bold cyan",
    "Live stream": "bold bright_cyan",
    "App khác": "bold bright_magenta",
}

# Dữ liệu app theo nhóm
APP_GROUPS: Dict[str, List[Dict[str, str]]] = {
    "Trình duyệt": [
        {"name": "Brave", "action": ["winget", "install", "-e", "--id=Brave.Brave"]},
        {"name": "Google Chrome", "action": ["winget", "install", "-e", "--id=Google.Chrome"]},
        {"name": "Microsoft Edge", "action": ["winget", "install", "-e", "--id=Microsoft.Edge"]},
        {"name": "Mozilla Firefox", "action": ["winget", "install", "-e", "--id=Mozilla.Firefox"]},
        {"name": "Opera", "action": ["winget", "install", "-e", "--id=Opera.Opera"]},
        {"name": "Opera GX", "action": ["start", "https://www.operagx.com/"]},
        {"name": "Tor Browser", "action": ["start", "https://www.torproject.org/download/"]},
        {"name": "Yandex Browser", "action": ["start", "https://browser.yandex.com/"]},
    ],
    "VPN": [
        {"name": "ExpressVPN", "action": ["start", "https://www.expressvpn.com/vpn-download"]},
        {"name": "HideMyAss (HMA)", "action": ["start", "https://www.hidemyass.com/downloads"]},
        {"name": "Hotspot Shield", "action": ["start", "https://www.hotspotshield.com/vi/vpn/vpn-for-windows/"]},
        {"name": "NordVPN", "action": ["start", "https://nordvpn.com/download/"]},
        {"name": "OpenVPN", "action": ["start", "https://openvpn.net/community-downloads/"]},
        {"name": "ProtonVPN", "action": ["start", "https://protonvpn.com/download"]},
        {"name": "UrbanVPN", "action": ["start", "https://www.urban-vpn.com/"]},
    ],
    "Mạng xã hội & Nhắn tin": [
        {"name": "Arena", "action": ["start", "https://xarena.vn/"]},
        {"name": "CSPlay", "action": ["start", "https://csplay.vn/"]},
        {"name": "Discord", "action": ["winget", "install", "-e", "--id=Discord.Discord"]},
        {"name": "EGOPlay", "action": ["start", "https://ego-play.com/"]},
        {"name": "Facebook", "action": ["start", "https://www.facebook.com/"]},
        {"name": "GPlay", "action": ["start", "https://gplay.vn/"]},
        {"name": "Instagram", "action": ["start", "https://www.instagram.com/"]},
        {"name": "Messenger", "action": ["start", "https://www.messenger.com/"]},
        {"name": "Reddit", "action": ["start", "https://www.reddit.com/"]},
        {"name": "Steam", "action": ["start", "https://store.steampowered.com/"]},
        {"name": "Telegram", "action": ["winget", "install", "-e", "--id=Telegram.TelegramDesktop"]},
        {"name": "Threads", "action": ["start", "https://www.threads.net/"]},
        {"name": "X (Twitter)", "action": ["start", "https://twitter.com/"]},
        {"name": "YouTube", "action": ["start", "https://www.youtube.com/"]},
        {"name": "Zalo", "action": ["start", "https://zalo.me/pc"]},
    ],
    "Media": [
        {"name": "FL Studio 2024", "action": ["start", "https://www.image-line.com/fl-studio-download/"]},
        {"name": "iTunes", "action": ["winget", "install", "--id=Apple.iTunes", "-e"]},
        {"name": "SoundCloud", "action": ["start", "https://soundcloud.com/"]},
        {"name": "Spotify", "action": ["start", "https://www.spotify.com/download/"]},
        {"name": "VLC", "action": ["winget", "install", "-e", "--id=VideoLAN.VLC"]},
        {"name": "VirtualDJ", "action": ["start", "https://www.virtualdj.com/download/index.html"]},
        {"name": "Winamp", "action": ["start", "https://www.winamp.com/"]},
    ],
    "Lập trình & Công cụ dev": [
        {"name": "Cmder", "action": ["start", "https://cmder.net/"]},
        {"name": "Dev-C++", "action": ["start", "https://sourceforge.net/projects/orwelldevcpp/"]},
        {"name": "Docker", "action": ["start", "https://www.docker.com/get-started"]},
        {"name": "Git", "action": ["winget", "install", "-e", "--id=Git.Git"]},
        {"name": "JDK", "action": ["start", "https://www.oracle.com/java/technologies/javase-jdk11-downloads.html"]},
        {"name": "Node.js", "action": ["winget", "install", "-e", "--id=OpenJS.NodeJS.LTS"]},
        {"name": "Notepad++", "action": ["start", "https://notepad-plus-plus.org/downloads/"]},
        {"name": "Python", "action": ["winget", "install", "-e", "--id=Python.Python.3"]},
        {"name": "PyCharm", "action": ["start", "https://www.jetbrains.com/pycharm/download/"]},
        {"name": "Sublime Text", "action": ["start", "https://www.sublimetext.com/download"]},
        {"name": "Visual Studio", "action": ["winget", "install", "-e", "--id=Microsoft.VisualStudio.2022.Community"]},
        {"name": "Visual Studio Code", "action": ["winget", "install", "-e", "--id=Microsoft.VisualStudioCode"]},
        {"name": "XAMPP", "action": ["start", "https://www.apachefriends.org/download.html"]},
    ],
    "Torrent": [
        {"name": "BitTorrent", "action": ["winget", "install", "-e", "--id=BitTorrent.BitTorrent"]},
        {"name": "Deluge", "action": ["start", "https://deluge-torrent.org/downloads/"]},
        {"name": "qBittorrent", "action": ["winget", "install", "-e", "--id=qBittorrent.qBittorrent"]},
        {"name": "Transmission", "action": ["start", "https://transmissionbt.com/download/"]},
        {"name": "uTorrent", "action": ["winget", "install", "-e", "--id=uTorrent.uTorrent"]},
        {"name": "Vuze", "action": ["start", "https://www.vuze.com/download/"]},
    ],
    "Live stream": [
        {"name": "OBS Studio", "action": ["winget", "install", "-e", "--id=obsproject.obs-studio"]},
        {"name": "PRISM Live Studio", "action": ["start", "https://prismlive.com/en_us/lens.html"]},
        {"name": "Streamlabs", "action": ["start", "https://streamlabs.com/"]},
        {"name": "Twitch Studio", "action": ["start", "https://www.twitch.tv/broadcast/studio"]},
    ],
    "App khác": [
        {"name": "Advanced Renamer", "action": ["start", "https://www.advancedrenamer.com/download"]},
        {"name": "Bitwarden", "action": ["start", "https://bitwarden.com/download/"]},
        {"name": "Clownfish Voice Changer", "action": ["start", "https://clownfish-translator.com/voicechanger/"]},
        {"name": "CustomRP", "action": ["start", "https://www.customrp.xyz/"]},
        {"name": "Link Google Drive (Tải thủ công)", "action": ["start", "https://drive.google.com/drive/folders/1LKJwPfC2IyUHz8xkq69Gn4GRbLSttlfI?usp=sharing"]},
        {"name": "Tag&Rename", "action": ["start", "https://www.softpointer.com/tr.htm"]},
        {"name": "WPS Office", "action": ["start", "https://www.wps.com/"]},
    ],
}


def run_action(action: List[str]) -> None:
    """Chạy hành động: winget install hoặc mở URL"""
    try:
        if action[0].lower() == "start":
            url = action[1]
            if sys.platform == "win32":
                subprocess.run(["start", url], shell=True, check=True)
            else:
                # Linux / MacOS fallback
                subprocess.run(["xdg-open", url], check=True)
        else:
            subprocess.run(action, check=True)
        console.print(f"[green]Đã thực thi: {' '.join(action)}[/green]")
    except Exception as e:
        console.print(f"[red]Lỗi khi thực thi {' '.join(action)}: {e}[/red]")


def print_header() -> None:
    header_text = Text("TRÌNH CÀI APP TỰ ĐỘNG BY CHERRY", style="bold white on dark_blue")
    console.rule(header_text)


def print_group_menu() -> None:
    table = Table(title="Chọn nhóm ứng dụng để cài đặt", show_lines=True)
    table.add_column("STT", justify="center", style="bold cyan")
    table.add_column("Nhóm", style="bold")

    for idx, group in enumerate(APP_GROUPS.keys(), 1):
        style = GROUP_STYLES.get(group, "white")
        table.add_row(str(idx), f"[{style}]{group}[/{style}]")

    console.print(table)


def select_group() -> str:
    group_keys = list(APP_GROUPS.keys())
    while True:
        print_group_menu()
        choice = Prompt.ask("Nhập số thứ tự nhóm (hoặc '0' để thoát)")
        if choice == "0":
            return ""
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(group_keys):
                return group_keys[idx - 1]
        console.print("[red]Lựa chọn không hợp lệ. Vui lòng thử lại.[/red]")


def print_app_menu(apps: List[Dict[str, str]], group_name: str) -> None:
    table = Table(title=f"Ứng dụng trong nhóm [bold]{group_name}[/bold]", show_lines=True)
    table.add_column("STT", justify="center", style="cyan")
    table.add_column("Tên ứng dụng", style="bold magenta")

    for idx, app in enumerate(apps, 1):
        table.add_row(str(idx), app["name"])

    console.print(table)


def select_apps(apps: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Cho phép chọn nhiều app, nhập nhiều số cách nhau bằng dấu phẩy hoặc 'all'"""
    while True:
        print_app_menu(apps, "Nhóm ứng dụng")
        choice = Prompt.ask(
            "Nhập số thứ tự ứng dụng cần cài (cách nhau dấu phẩy), hoặc 'all' để chọn tất"
        ).strip().lower()

        if choice == "all":
            return apps

        selections = [c.strip() for c in choice.split(",")]
        selected_apps = []
        valid = True

        for s in selections:
            if s.isdigit():
                idx = int(s)
                if 1 <= idx <= len(apps):
                    selected_apps.append(apps[idx - 1])
                else:
                    valid = False
                    break
            else:
                valid = False
                break

        if valid and selected_apps:
            return selected_apps
        else:
            console.print("[red]Lựa chọn không hợp lệ, vui lòng thử lại.[/red]")


def confirm_run(apps: List[Dict[str, str]]) -> bool:
    names = ", ".join(app["name"] for app in apps)
    answer = Prompt.ask(f"Bạn có chắc muốn cài/mở các app: {names}? (y/n)", choices=["y", "n"], default="n")
    return answer == "y"


def main():
    print_header()

    while True:
        group = select_group()
        if not group:
            console.print("[yellow]Đã thoát chương trình. Chào Cherry![/yellow]")
            break

        apps = APP_GROUPS[group]
        selected_apps = select_apps(apps)

        if confirm_run(selected_apps):
            for app in selected_apps:
                console.print(Panel(f"Đang xử lý: [bold green]{app['name']}[/bold green]", style="blue"))
                run_action(app["action"])

            console.print("[bold green]Hoàn tất cài đặt/mở app trong nhóm này![/bold green]\n")
        else:
            console.print("[yellow]Bỏ qua nhóm ứng dụng này.[/yellow]")


if __name__ == "__main__":
    main()
