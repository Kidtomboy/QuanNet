import sys
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea,
    QGroupBox, QCheckBox, QPushButton, QMessageBox, QHBoxLayout,
    QFrame, QSizePolicy
)
from PyQt6.QtGui import QFont, QColor, QPalette, QIcon
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize

# Dữ liệu app
apps = {
    "🌐 Trình duyệt": {
        "Brave": "winget install -e --id=Brave.Brave",
        "Google Chrome": "winget install -e --id=Google.Chrome",
        "Microsoft Edge": "winget install -e --id=Microsoft.Edge",
        "Mozilla Firefox": "winget install -e --id=Mozilla.Firefox",
        "Opera & Opera GX": "winget install -e --id=Opera.Opera && start https://www.operagx.com/",
        "Tor Browser": "start https://www.torproject.org/download/",
        "Yandex Browser": "start https://browser.yandex.com/"
    },
    "🛡️ VPN & Bảo mật": {
        "ExpressVPN": "start https://www.expressvpn.com/vpn-download",
        "HideMyAss (HMA)": "start https://www.hidemyass.com/downloads",
        "Hotspot Shield": "start https://www.hotspotshield.com/vi/vpn/vpn-for-windows/",
        "NordVPN": "start https://nordvpn.com/download/",
        "OpenVPN": "start https://openvpn.net/community-downloads/",
        "ProtonVPN": "start https://protonvpn.com/download",
        "UrbanVPN": "start https://www.urban-vpn.com/"
    },
    "🖥️ Phần mềm văn phòng": {
        "Adobe Acrobat Reader": "winget install -e --id=Adobe.Acrobat.Reader.64-bit",
        "Adobe Photoshop": "winget install -e --id=Adobe.Photoshop.2021",
        "Microsoft Office": "winget install -e --id=Microsoft.Office",
        "WPS Office": "winget install -e --id=Kingsoft.WPSOffice",
        "LibreOffice": "winget install -e --id=TheDocumentFoundation.LibreOffice"
    }
}

# Màu chủ đạo
COLOR_PRIMARY = "#4A90E2"
COLOR_PRIMARY_DARK = "#357ABD"
COLOR_BG = "#F5F7FA"
COLOR_CARD = "#FFFFFF"
COLOR_TEXT = "#2E3440"
COLOR_ACCENT = "#D81159"

class HoverCheckBox(QCheckBox):
    def __init__(self, text):
        super().__init__(text)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QCheckBox {
                spacing: 10px;
                font-size: 16px;
                color: """ + COLOR_TEXT + """;
            }
            QCheckBox::indicator {
                width: 22px;
                height: 22px;
            }
            QCheckBox::indicator:unchecked {
                border: 2px solid """ + COLOR_PRIMARY + """;
                background-color: transparent;
                border-radius: 5px;
            }
            QCheckBox::indicator:checked {
                background-color: """ + COLOR_PRIMARY + """;
                border: 2px solid """ + COLOR_PRIMARY + """;
                border-radius: 5px;
            }
            QCheckBox:hover {
                color: """ + COLOR_PRIMARY_DARK + """;
            }
        """)

class FancyButton(QPushButton):
    def __init__(self, text, color=COLOR_PRIMARY):
        super().__init__(text)
        self.color = color
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedHeight(50)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                font-weight: bold;
                font-size: 18px;
                border-radius: 12px;
                padding: 10px 20px;
                transition: background-color 0.3s ease;
            }}
            QPushButton:hover {{
                background-color: {COLOR_PRIMARY_DARK};
            }}
            QPushButton:pressed {{
                background-color: {COLOR_ACCENT};
            }}
        """)

class GroupBoxFancy(QGroupBox):
    def __init__(self, title):
        super().__init__(title)
        self.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        self.setStyleSheet(f"""
            QGroupBox {{
                background-color: {COLOR_CARD};
                border-radius: 15px;
                border: 1.5px solid {COLOR_PRIMARY};
                margin-top: 20px;
                padding: 15px;
                color: {COLOR_PRIMARY_DARK};
            }}
            QGroupBox:title {{
                subcontrol-origin: margin;
                subcontrol-position: top center;
                padding: 0 10px;
                background-color: {COLOR_BG};
            }}
        """)

class InstallerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✨ Trình Cài App Siêu Xịn Xò by Cherry ✨")
        self.setGeometry(150, 50, 720, 820)
        self.setMinimumSize(720, 800)
        self.checkboxes = {}
        self.setup_ui()
        self.setStyleSheet(f"background-color: {COLOR_BG}; color: {COLOR_TEXT};")

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        # Tiêu đề chính
        title = QLabel("🌟 TRÌNH CÀI APP TỰ ĐỘNG BY CHERRY 🌟")
        title.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {COLOR_PRIMARY};")
        main_layout.addWidget(title)

        # Giới thiệu ngắn
        desc = QLabel("Chọn các app bạn muốn, bấm cài đặt và để mình lo phần còn lại nhé!")
        desc.setFont(QFont("Segoe UI", 13))
        desc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        desc.setStyleSheet(f"color: {COLOR_PRIMARY_DARK}; font-style: italic;")
        main_layout.addWidget(desc)

        # Scroll area chứa nhóm app
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("border: none;")
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(20)

        # Tạo nhóm ứng dụng
        for group_name, apps_dict in apps.items():
            groupbox = GroupBoxFancy(group_name)
            group_layout = QVBoxLayout()
            for app_name in apps_dict.keys():
                cb = HoverCheckBox(app_name)
                self.checkboxes[app_name] = cb
                group_layout.addWidget(cb)
            groupbox.setLayout(group_layout)
            scroll_layout.addWidget(groupbox)

        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

        # Nút chức năng
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(30)

        btn_install = FancyButton("🚀 CÀI ĐẶT NGAY")
        btn_install.clicked.connect(self.install_selected_apps)

        btn_exit = FancyButton("❌ THOÁT", color="#E63946")
        btn_exit.clicked.connect(self.close)

        btn_layout.addStretch()
        btn_layout.addWidget(btn_install)
        btn_layout.addWidget(btn_exit)
        btn_layout.addStretch()

        main_layout.addLayout(btn_layout)

        # Footer nhẹ nhàng
        footer = QLabel("By Cherry 🐾 | Phát triển với ❤️ và thơ ca")
        footer.setFont(QFont("Segoe UI", 10))
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setStyleSheet(f"color: {COLOR_PRIMARY_DARK}; margin-top: 15px;")
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

    def install_selected_apps(self):
        selected_apps = [app for app, cb in self.checkboxes.items() if cb.isChecked()]
        if not selected_apps:
            QMessageBox.warning(self, "⚠️ Cảnh báo", "Bạn chưa chọn app nào để cài cả! 🐱‍👤")
            return

        reply = QMessageBox.question(
            self, "Xác nhận cài đặt",
            f"Bạn có chắc chắn muốn cài các app này không?\n\n" + "\n".join(selected_apps),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        errors = []
        for app in selected_apps:
            command = self.lookup_command(app)
            if not command:
                errors.append(f"Không tìm thấy lệnh cho {app}")
                continue

            try:
                cmds = [cmd.strip() for cmd in command.split("&&")]
                for cmd in cmds:
                    subprocess.run(cmd, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                errors.append(f"Lỗi khi cài {app}: {e}")

        if errors:
            QMessageBox.critical(self, "❌ Lỗi", "\n".join(errors))
        else:
            QMessageBox.information(self, "✅ Hoàn thành", "Đã cài xong tất cả app bạn chọn! 🥳")

    def lookup_command(self, app_name):
        for group in apps.values():
            if app_name in group:
                return group[app_name]
        return None


def main():
    app = QApplication(sys.argv)
    gui = InstallerGUI()
    gui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
