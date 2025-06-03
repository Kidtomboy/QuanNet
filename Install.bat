@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM === ANSI màu cho từng nhóm ===
set "CLR_RESET=[0m"
set "CLR_A=[34m"  REM xanh dương - Trình duyệt
set "CLR_B=[32m"  REM xanh lá - VPN
set "CLR_C=[33m"  REM vàng - Mạng xã hội
set "CLR_D=[31m"  REM đỏ - Media
set "CLR_E=[35m"  REM tím - Lập trình
set "CLR_F=[36m"  REM cyan - Torrent
set "CLR_G=[91m"  REM cam sáng - Live stream
set "CLR_H=[95m"  REM hồng tím - App khác
set "CLR_I=[90m"  Rem đen - Thoát


:MENU
cls
echo ╔═══════════════════════════════════════════════╗
echo ║ %CLR_A%       TRÌNH CÀI APP TỰ ĐỘNG BY CHERRY       %CLR_RESET% ║
echo ╚═══════════════════════════════════════════════╝
echo %CLR_A%A.%CLR_RESET% Trình duyệt
echo %CLR_A%    A1.%CLR_RESET% Brave
echo %CLR_A%    A2.%CLR_RESET% Google Chrome
echo %CLR_A%    A3.%CLR_RESET% Microsoft Edge
echo %CLR_A%    A4.%CLR_RESET% Mozilla Firefox
echo %CLR_A%    A5.%CLR_RESET% Opera ^& Opera GX
echo %CLR_A%    A6.%CLR_RESET% Tor Browser
echo %CLR_A%    A7.%CLR_RESET% Yandex Browser

echo %CLR_B%B.%CLR_RESET% VPN
echo %CLR_B%    B1.%CLR_RESET% ExpressVPN
echo %CLR_B%    B2.%CLR_RESET% HideMyAss ^(HMA^)
echo %CLR_B%    B3.%CLR_RESET% Hotspot Shield
echo %CLR_B%    B4.%CLR_RESET% NordVPN
echo %CLR_B%    B5.%CLR_RESET% OpenVPN
echo %CLR_B%    B6.%CLR_RESET% ProtonVPN
echo %CLR_B%    B7.%CLR_RESET% UrbanVPN

echo %CLR_C%C.%CLR_RESET% Mạng xã hội ^& Nhắn tin
echo %CLR_C%    C1.%CLR_RESET% Arena
echo %CLR_C%    C2.%CLR_RESET% CSPlay
echo %CLR_C%    C3.%CLR_RESET% Discord
echo %CLR_C%    C4.%CLR_RESET% EGOPlay
echo %CLR_C%    C5.%CLR_RESET% Facebook
echo %CLR_C%    C6.%CLR_RESET% GPlay
echo %CLR_C%    C7.%CLR_RESET% Instagram
echo %CLR_C%    C8.%CLR_RESET% Messenger
echo %CLR_C%    C9.%CLR_RESET% Reddit
echo %CLR_C%    C10.%CLR_RESET% Steam
echo %CLR_C%    C11.%CLR_RESET% Telegram
echo %CLR_C%    C12.%CLR_RESET% Threads
echo %CLR_C%    C13.%CLR_RESET% X ^(Twitter^)
echo %CLR_C%    C14.%CLR_RESET% YouTube
echo %CLR_C%    C15.%CLR_RESET% Zalo

echo %CLR_D%D.%CLR_RESET% Media
echo %CLR_D%    D1.%CLR_RESET% FL Studio 2024
echo %CLR_D%    D2.%CLR_RESET% iTunes
echo %CLR_D%    D3.%CLR_RESET% SoundCloud
echo %CLR_D%    D4.%CLR_RESET% Spotify
echo %CLR_D%    D5.%CLR_RESET% VLC
echo %CLR_D%    D6.%CLR_RESET% VirtualDJ
echo %CLR_D%    D7.%CLR_RESET% Winamp

echo %CLR_E%E.%CLR_RESET% Lập trình ^& Công cụ dev
echo %CLR_E%    E1.%CLR_RESET% Cmder
echo %CLR_E%    E2.%CLR_RESET% Dev-C++
echo %CLR_E%    E3.%CLR_RESET% Docker
echo %CLR_E%    E4.%CLR_RESET% Git
echo %CLR_E%    E5.%CLR_RESET% JDK
echo %CLR_E%    E6.%CLR_RESET% Node.js
echo %CLR_E%    E7.%CLR_RESET% Notepad++
echo %CLR_E%    E8.%CLR_RESET% Python
echo %CLR_E%    E9.%CLR_RESET% PyCharm
echo %CLR_E%    E10.%CLR_RESET% Sublime Text
echo %CLR_E%    E11.%CLR_RESET% Visual Studio
echo %CLR_E%    E12.%CLR_RESET% Visual Studio Code
echo %CLR_E%    E13.%CLR_RESET% XAMPP

echo %CLR_F%F.%CLR_RESET% Torrent
echo %CLR_F%    F1.%CLR_RESET% BitTorrent
echo %CLR_F%    F2.%CLR_RESET% Deluge
echo %CLR_F%    F3.%CLR_RESET% qBittorrent
echo %CLR_F%    F4.%CLR_RESET% Transmission
echo %CLR_F%    F5.%CLR_RESET% uTorrent
echo %CLR_F%    F6.%CLR_RESET% Vuze

echo %CLR_G%G.%CLR_RESET% Live stream
echo %CLR_G%    G1.%CLR_RESET% OBS Studio
echo %CLR_G%    G2.%CLR_RESET% PRISM Live Studio
echo %CLR_G%    G3.%CLR_RESET% Streamlabs
echo %CLR_G%    G4.%CLR_RESET% Twitch Studio

echo %CLR_H%H.%CLR_RESET% App khác
echo %CLR_H%    H1.%CLR_RESET% Advanced Renamer
echo %CLR_H%    H2.%CLR_RESET% Bitwarden
echo %CLR_H%    H3.%CLR_RESET% Clownfish Voice Changer
echo %CLR_H%    H4.%CLR_RESET% CustomRP
echo %CLR_H%    H5.%CLR_RESET% Link Google Drive ^(Tải thủ công^)
echo %CLR_H%    H6.%CLR_RESET% Tag^&Rename
echo %CLR_H%    H7.%CLR_RESET% WPS Office
echo.
echo %CLR_D%ALL.%CLR_RESET% Cài tất cả app
echo.
echo %CLR_I%0.%CLR_RESET% Thoát
echo.
echo ================= Cách Nhập Mã =================
echo %CLR_I%C1         : Tải app có mã C1%CLR_RESET%
echo %CLR_I%C1,C2,C3   : Tải các app có mã C1, C2, C3%CLR_RESET%
echo %CLR_I%Nhập C     : Tải tất cả app thuộc nhóm C%CLR_RESET%
echo %CLR_I%Nhập ALL   : Tải tất cả các mã app ^(Nguy Hiểm^)%CLR_RESET%
echo ================================================
echo.
set /p input=Nhập mã app hoặc nhóm:


if /I "%input%"=="0" exit

for %%x in (%input:,= %) do (
    set code=%%x
    call :PROCESS !code!
)

pause
goto MENU

:PROCESS
set "code=%~1"

REM ======= Trình duyệt =======
if /I "%code%"=="A1" winget install -e --id=Brave.Brave
if /I "%code%"=="A2" winget install -e --id=Google.Chrome
if /I "%code%"=="A3" winget install -e --id=Microsoft.Edge
if /I "%code%"=="A4" winget install -e --id=Mozilla.Firefox
if /I "%code%"=="A5" (
    winget install -e --id=Opera.Opera
    start https://www.operagx.com/
)
if /I "%code%"=="A6" start https://www.torproject.org/download/
if /I "%code%"=="A7" start https://browser.yandex.com/

REM ======= VPN =======
if /I "%code%"=="B1" start https://www.expressvpn.com/vpn-download
if /I "%code%"=="B2" start https://www.hidemyass.com/downloads
if /I "%code%"=="B3" start https://www.hotspotshield.com/vi/vpn/vpn-for-windows/
if /I "%code%"=="B4" start https://nordvpn.com/download/
if /I "%code%"=="B5" start https://openvpn.net/community-downloads/
if /I "%code%"=="B6" start https://protonvpn.com/download
if /I "%code%"=="B7" start https://www.urban-vpn.com/

REM ======= Mạng xã hội & Nhắn tin =======
if /I "%code%"=="C1" start https://xarena.vn/
if /I "%code%"=="C2" start https://csplay.vn/
if /I "%code%"=="C3" winget install -e --id=Discord.Discord
if /I "%code%"=="C4" start https://ego-play.com/
if /I "%code%"=="C5" start https://www.facebook.com/
if /I "%code%"=="C6" start https://gplay.vn/
if /I "%code%"=="C7" start https://www.instagram.com/
if /I "%code%"=="C8" start https://www.messenger.com/
if /I "%code%"=="C9" start https://www.reddit.com/
if /I "%code%"=="C10" start https://store.steampowered.com/
if /I "%code%"=="C11" winget install -e --id=Telegram.TelegramDesktop
if /I "%code%"=="C12" start https://www.threads.net/
if /I "%code%"=="C13" start https://twitter.com/
if /I "%code%"=="C14" start https://www.youtube.com/
if /I "%code%"=="C15" start https://zalo.me/pc

REM ======= Media =======
if /I "%code%"=="D1" start https://www.image-line.com/fl-studio-download/
if /I "%code%"=="D2" winget install --id=Apple.iTunes -e
if /I "%code%"=="D3" start https://soundcloud.com/
if /I "%code%"=="D4" start https://www.spotify.com/download/
if /I "%code%"=="D5" winget install -e --id=VideoLAN.VLC
if /I "%code%"=="D6" start https://www.virtualdj.com/download/index.html
if /I "%code%"=="D7" start https://www.winamp.com/

REM ======= Lập trình & Công cụ dev =======
if /I "%code%"=="E1" start https://cmder.net/
if /I "%code%"=="E2" start https://sourceforge.net/projects/orwelldevcpp/
if /I "%code%"=="E3" start https://www.docker.com/get-started
if /I "%code%"=="E4" winget install -e --id=Git.Git
if /I "%code%"=="E5" start https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
if /I "%code%"=="E6" winget install -e --id=OpenJS.NodeJS.LTS
if /I "%code%"=="E7" start https://notepad-plus-plus.org/downloads/
if /I "%code%"=="E8" winget install -e --id=Python.Python.3
if /I "%code%"=="E9" start https://www.jetbrains.com/pycharm/download/
if /I "%code%"=="E10" start https://www.sublimetext.com/download
if /I "%code%"=="E11" winget install -e --id=Microsoft.VisualStudio.2022.Community
if /I "%code%"=="E12" winget install -e --id=Microsoft.VisualStudioCode
if /I "%code%"=="E13" start https://www.apachefriends.org/download.html

REM ======= Torrent =======
if /I "%code%"=="F1" winget install -e --id=BitTorrent.BitTorrent
if /I "%code%"=="F2" start https://deluge-torrent.org/downloads/
if /I "%code%"=="F3" winget install -e --id=qBittorrent.qBittorrent
if /I "%code%"=="F4" start https://transmissionbt.com/download/
if /I "%code%"=="F5" winget install -e --id=uTorrent.uTorrent
if /I "%code%"=="F6" start https://www.vuze.com/download/

REM ======= Live stream =======
if /I "%code%"=="G1" winget install -e --id=obsproject.obs-studio
if /I "%code%"=="G2" start https://prismlive.com/en_us/lens.html
if /I "%code%"=="G3" start https://streamlabs.com/
if /I "%code%"=="G4" start https://www.twitch.tv/broadcast/studio

REM ======= App khác =======
if /I "%code%"=="H1" start https://www.advancedrenamer.com/download
if /I "%code%"=="H2" start https://bitwarden.com/download/
if /I "%code%"=="H3" start https://clownfish-translator.com/voicechanger/
if /I "%code%"=="H4" start https://www.customrp.xyz/
if /I "%code%"=="H5" start https://drive.google.com/drive/folders/1LKJwPfC2IyUHz8xkq69Gn4GRbLSttlfI?usp=sharing
if /I "%code%"=="H6" start https://www.softpointer.com/tr.htm
if /I "%code%"=="H7" start https://www.wps.com/

REM ======= Cài tất cả =======
if /I "%code%"=="ALL" (
    call :INSTALL_ALL
)

goto :EOF

:INSTALL_ALL
REM Trình duyệt
winget install -e --id=Brave.Brave
winget install -e --id=Google.Chrome
winget install -e --id=Microsoft.Edge
winget install -e --id=Mozilla.Firefox
winget install -e --id=Opera.Opera
start https://www.operagx.com/
start https://www.torproject.org/download/
start https://browser.yandex.com/

REM VPN
start https://www.expressvpn.com/download
start https://www.hidemyass.com/download
start https://www.hotspotshield.com/
start https://nordvpn.com/download/
start https://openvpn.net/community-downloads/
start https://protonvpn.com/download
start https://www.urban-vpn.com/download/

REM Mạng xã hội & nhắn tin
winget install -e --id=Discord.Discord
winget install -e --id=Telegram.TelegramDesktop
start https://xarena.vn/
start https://csplay.vn/
start https://ego-play.com/
start https://www.facebook.com/
start https://gplay.vn/
start https://www.instagram.com/
start https://www.messenger.com/
start https://www.reddit.com/
start https://store.steampowered.com/
start https://www.threads.net/
start https://twitter.com/
start https://www.youtube.com/
start https://zalo.me/pc

REM Media
start https://www.image-line.com/fl-studio-download/
start https://www.apple.com/itunes/download/
start https://soundcloud.com/
start https://www.spotify.com/download/
winget install -e --id=VideoLAN.VLC
start https://www.virtualdj.com/download/index.html
start https://www.winamp.com/

REM Lập trình & dev
start https://cmder.net/
start https://sourceforge.net/projects/orwelldevcpp/
start https://www.docker.com/get-started
winget install -e --id=Git.Git
start https://www.oracle.com/java/technologies/javase-jdk11-downloads.html
winget install -e --id=OpenJS.NodeJS.LTS
start https://notepad-plus-plus.org/downloads/
winget install -e --id=Python.Python.3
start https://www.jetbrains.com/pycharm/download/
start https://www.sublimetext.com/3
winget install -e --id=Microsoft.VisualStudio.2022.Community
winget install -e --id=Microsoft.VisualStudioCode
start https://www.apachefriends.org/download.html

REM Torrent
winget install -e --id=BitTorrent.BitTorrent
start https://deluge-torrent.org/downloads/
winget install -e --id=qBittorrent.qBittorrent
start https://transmissionbt.com/download/
winget install -e --id=uTorrent.uTorrent
start https://www.vuze.com/download/

REM Live stream
winget install -e --id=obsproject.obs-studio
start https://prismlive.com/download/
start https://streamlabs.com/
start https://www.twitch.tv/broadcast/studio

REM App khác
start https://www.advancedrenamer.com/download
start https://bitwarden.com/download/
start https://clownfish-translator.com/voicechanger/
start https://customrp.com/download/
start https://drive.google.com/drive/folders/1LKJwPfC2IyUHz8xkq69Gn4GRbLSttlfI?usp=sharing
start https://www.softpointer.com/tr.htm
start https://www.wps.com/

exit /b