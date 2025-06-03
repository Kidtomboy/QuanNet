import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser

# Dữ liệu app dạng dict: mã => (tên app, type (install/web), link/winget_id)
apps = {
    # Trình duyệt
    "A1": ("Brave", "winget", "Brave.Brave"),
    "A2": ("Google Chrome", "winget", "Google.Chrome"),
    "A3": ("Microsoft Edge", "winget", "Microsoft.Edge"),
    "A4": ("Mozilla Firefox", "winget", "Mozilla.Firefox"),
    "A5": ("Opera & Opera GX", "mixed", ("Opera.Opera", "https://www.operagx.com/")),
    "A6": ("Tor Browser", "web", "https://www.torproject.org/download/"),
    "A7": ("Yandex Browser", "web", "https://browser.yandex.com/"),
    # VPN
    "B1": ("ExpressVPN", "web", "https://www.expressvpn.com/vpn-download"),
    "B2": ("HideMyAss (HMA)", "web", "https://www.hidemyass.com/downloads"),
    "B3": ("Hotspot Shield", "web", "https://www.hotspotshield.com/vi/vpn/vpn-for-windows/"),
    "B4": ("NordVPN", "web", "https://nordvpn.com/download/"),
    "B5": ("OpenVPN", "web", "https://openvpn.net/community-downloads/"),
    "B6": ("ProtonVPN", "web", "https://protonvpn.com/download"),
    "B7": ("UrbanVPN", "web", "https://www.urban-vpn.com/"),
    # Mạng xã hội & Nhắn tin
    "C1": ("Arena", "web", "https://xarena.vn/"),
    "C2": ("CSPlay", "web", "https://csplay.vn/"),
    "C3": ("Discord", "winget", "Discord.Discord"),
    "C4": ("EGOPlay", "web", "https://ego-play.com/"),
    "C5": ("Facebook", "web", "https://www.facebook.com/"),
    "C6": ("GPlay", "web", "https://gplay.vn/"),
    "C7": ("Instagram", "web", "https://www.instagram.com/"),
    "C8": ("Messenger", "web", "https://www.messenger.com/"),
    "C9": ("Reddit", "web", "https://www.reddit.com/"),
    "C10": ("Steam", "web", "https://store.steampowered.com/"),
    "C11": ("Telegram", "winget", "Telegram.TelegramDesktop"),
    "C12": ("Threads", "web", "https://www.threads.net/"),
    "C13": ("X (Twitter)", "web", "https://twitter.com/"),
    "C14": ("YouTube", "web", "https://www.youtube.com/"),
    "C15": ("Zalo", "web", "https://zalo.me/pc"),
    # Media
    "D1": ("FL Studio 2024", "web", "https://www.image-line.com/fl-studio-download/"),
    "D2": ("iTunes", "winget", "Apple.iTunes"),
    "D3": ("SoundCloud", "web", "https://soundcloud.com/"),
    "D4": ("Spotify", "web", "https://www.spotify.com/download/"),
    "D5": ("VLC", "winget", "VideoLAN.VLC"),
    "D6": ("VirtualDJ", "web", "https://www.virtualdj.com/download/index.html"),
    "D7": ("Winamp", "web", "https://www.winamp.com/"),
    # Lập trình & Dev
    "E1": ("Cmder", "web", "https://cmder.net/"),
    "E2": ("Dev-C++", "web", "https://sourceforge.net/projects/orwelldevcpp/"),
    "E3": ("Docker", "web", "https://www.docker.com/get-started"),
    "E4": ("Git", "winget", "Git.Git"),
    "E5": ("JDK", "web", "https://www.oracle.com/java/technologies/javase-jdk11-downloads.html"),
    "E6": ("Node.js", "winget", "OpenJS.NodeJS.LTS"),
    "E7": ("Notepad++", "web", "https://notepad-plus-plus.org/downloads/"),
    "E8": ("Python", "winget", "Python.Python.3"),
    "E9": ("PyCharm", "web", "https://www.jetbrains.com/pycharm/download/"),
    "E10": ("Sublime Text", "web", "https://www.sublimetext.com/download"),
    "E11": ("Visual Studio", "winget", "Microsoft.VisualStudio.2022.Community"),
    "E12": ("Visual Studio Code", "winget", "Microsoft.VisualStudioCode"),
    "E13": ("XAMPP", "web", "https://www.apachefriends.org/download.html"),
    # Torrent
    "F1": ("BitTorrent", "winget", "BitTorrent.BitTorrent"),
    "F2": ("Deluge", "web", "https://deluge-torrent.org/downloads/"),
    "F3": ("qBittorrent", "winget", "qBittorrent.qBittorrent"),
    "F4": ("Transmission", "web", "https://transmissionbt.com/download/"),
    "F5": ("uTorrent", "winget", "uTorrent.uTorrent"),
    "F6": ("Vuze", "web", "https://www.vuze.com/download/"),
    # Live stream
    "G1": ("OBS Studio", "winget", "obsproject.obs-studio"),
    "G2": ("PRISM Live Studio", "web", "https://prismlive.com/en_us/lens.html"),
    "G3": ("Streamlabs", "web", "https://streamlabs.com/"),
    "G4": ("Twitch Studio", "web", "https://www.twitch.tv/broadcast/studio"),
    # App khác
    "H1": ("Advanced Renamer", "web", "https://www.advancedrenamer.com/download"),
    "H2": ("Bitwarden", "web", "https://bitwarden.com/download/"),
    "H3": ("Clownfish Voice Changer", "web", "https://clownfish-translator.com/voicechanger/"),
    "H4": ("CustomRP", "web", "https://www.customrp.xyz/"),
    "H5": ("Link Google Drive (Tải thủ công)", "web", "https://drive.google.com/drive/folders/1LKJwPfC2IyUHz8xkq69Gn4GRbLSttlfI?usp=sharing"),
    "H6": ("Tag&Rename", "web", "https://www.softpointer.com/tr.htm"),
    "H7": ("WPS Office", "web", "https://www.wps.com/"),
}

# Phân nhóm mã
groups = {
    "A": "Trình duyệt",
    "B": "VPN",
    "C": "Mạng xã hội & Nhắn tin",
    "D": "Media",
    "E": "Lập trình & Công cụ dev",
    "F": "Torrent",
    "G": "Live stream",
    "H": "App khác"
}

class AppInstallerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trình cài App tự động by Cherry")
        self.geometry("900x700")
        self.resizable(False, False)

        self.selected_apps = {}

        # Scrollable frame for checkboxes
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.frame = tk.Frame(canvas)

        self.frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Tạo checkbox theo nhóm
        self.vars = {}
        for group_code, group_name in groups.items():
            group_label = tk.Label(self.frame, text=f"{group_code}. {group_name}", font=("Arial", 14, "bold"), fg="blue")
            group_label.pack(anchor="w", pady=(10, 0))

            for code, (name, _, _) in apps.items():
                if code.startswith(group_code):
                    var = tk.BooleanVar()
                    cb = tk.Checkbutton(self.frame, text=f"{code} - {name}", variable=var)
                    cb.pack(anchor="w", padx=20)
                    self.vars[code] = var

        # Nút điều khiển
        btn_frame = tk.Frame(self)
        btn_frame.pack(fill="x", pady=10)

        btn_install = tk.Button(btn_frame, text="Install Selected", command=self.install_selected, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        btn_install.pack(side="left", padx=10)

        btn_install_all = tk.Button(btn_frame, text="Install All", command=self.install_all, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
        btn_install_all.pack(side="left", padx=10)

        btn_exit = tk.Button(btn_frame, text="Exit", command=self.destroy, bg="#f44336", fg="white", font=("Arial", 12, "bold"))
        btn_exit.pack(side="right", padx=10)

    def install_selected(self):
        selected = [code for code, var in self.vars.items() if var.get()]
        if not selected:
            messagebox.showwarning("Chưa chọn app", "Vui lòng chọn ít nhất một app để cài đặt.")
            return

        for code in selected:
            self.process_install(code)

        messagebox.showinfo("Hoàn tất", "Đã thực hiện lệnh cài đặt/mở link cho các app đã chọn.")

    def install_all(self):
        for code in apps.keys():
            self.process_install(code)
        messagebox.showinfo("Hoàn tất", "Đã thực hiện lệnh cài đặt/mở link cho tất cả app.")

    def process_install(self, code):
        name, tp, data = apps[code]
        try:
            if tp == "winget":
                cmd = ["winget", "install", "-e", "--id", data]
                subprocess.Popen(cmd)  # chạy nền, không chặn
            elif tp == "web":
                webbrowser.open(data)
            elif tp == "mixed":
                winget_id, url = data
                subprocess.Popen(["winget", "install", "-e", "--id", winget_id])
                webbrowser.open(url)
            else:
                print(f"Unknown install type for {code}")
        except Exception as e:
            print(f"Lỗi khi cài {name}: {e}")

if __name__ == "__main__":
    app = AppInstallerGUI()
    app.mainloop()
