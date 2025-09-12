from builtins import exec, input, len, print, int, range, str, open, exit
exec('')

# Màu sắc
den = '\033[1;90m'
luc = '\033[1;32m'
trang = '\033[1;37m'
red = '\033[1;31m'
vang = '\033[1;33m'
tim = '\033[1;35m'
lamd = '\033[1;34m'
lam = '\033[1;36m'
purple = '\033[1;35m'
hong = '\033[1;95m'

# Dấu prompt
thanh_xau = trang + '~' + red + '[' + vang + 'C25' + red + '] ' + trang + '➩ ' + luc
thanh_dep = trang + '~' + red + '[' + luc + 'C25' + red + '] ' + trang + '➩ ' + luc

import requests, json, os, sys
from sys import platform
from datetime import datetime
from time import sleep, strftime

# Thử import pystyle, cài nếu thiếu
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except ImportError:
    os.system('pip install pystyle bs4 requests colorama beautifulsoup4 Anime webdriver_manager selenium mechanize')
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

def is_connected():
    """Kiểm tra mạng."""
    try:
        import socket
        socket.create_connection(('1.1.1.1', 53))
        return True
    except OSError:
        return False

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Live 4) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.28 Mobile Safari/537.36'
}

# Banner ASCII art
banners = """
╔═════════════════════════════════════════════════════════════════
██████╗██████╗ ███████╗ ████████╗ ██████╗ ██████╗ ██╗ ██╔════╝
╚════██╗██╔════╝ ╚══██╔══╝██╔═══██╗██╔═══██╗██║ ██║
 █████╔╝███████╗   ██║   ██████╔╝██████╔╝███████╗
 ██╔═══╝ ╚════██║   ██║   ██╔═══╝ ██╔══██╗╚════██║
 ╚██████╗███████║   ██║   ╚██████╔╝██║  ██║███████║
  ╚═════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
╠═════════════════════════════════════════════════════════════════
║➢ Admin : Vũ Văn Chiến
║➢ Youtube : https://www.youtube.com/@c25tool
║➣ Nhóm Bot Zalo : https://zalo.me/g/elcygl942
║➣ Website : c25tool.net
╚═════════════════════════════════════════════════════════════════
"""

thongtin = """
Vượt Link Để lấy Key Free Hoặc Mua Key Vip Tại Web: C25TOOL.NET
Lưu ý: (key free đổi theo ip máy nên lần sau vào tool không thay wifi nhé)
"""

def lovec25(so):
    """Hiệu ứng thanh loading."""
    a = '────' * so
    for ch in a:
        sys.stdout.write(ch)
        sys.stdout.flush()
        sleep(0.003)
    print()

def clear():
    """Xóa màn hình."""
    os.system('clear' if platform.startswith('lin') else 'cls')

def banner():
    """In banner màu gradient."""
    clear()
    art = Colorate.Horizontal(Colors.blue_to_green, banners)
    for ch in art:
        sys.stdout.write(ch)
        sys.stdout.flush()
    print()
    print(thongtin)

# Hiển thị banner một lần
banner()

# Thiết lập màu tiếp theo
lam = "\033[1;36m"
hong = "\033[1;95m"
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"

# Hiển thị menu
clear()
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃       Tool Cày Cuốc        ┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.1{lam}]{lam} Tool Cày Xu TDS Tiktok')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.2{lam}]{lam} Tool Cày Xu TDS Instagram')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.3{lam}]{lam} Tool Golike TikTok [ADR]')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.4{lam}]{lam} Tool Golike Instagram')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}1.5{lam}]{lam} Tool Cày Xu TDS Facebook')
print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃       Tool Profile         ┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.1{lam}]{lam} Tool Buff Share Ảo Cookie')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.2{lam}]{lam} Tool Get Token Facebook 16 Loại')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.3{lam}]{lam} Tool Lấy ID Bài Viết, ID Facebook')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.4{lam}]{lam} Tool CMT Bài Viết Dạo Facebook [bảo trì]')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.5{lam}]{lam} Tool Get Cookie Facebook Bằng TK MK')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}2.6{lam}]{lam} Tool Spam Tin Nhắn, War Messenger')
print(f'{luc}{lam}────────────────────────────────────────────────────────')
print(f"""{luc}┏━━━━━━━━━━━━━━━━━━━━━━━┓
{vang}┃        Tool Tiện Ích         ┃
{lam}┗━━━━━━━━━━━━━━━━━━━━━━━┛""")
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.1{lam}]{lam} Tool Doss Web + Doss IP')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.2{lam}]{lam} Tool Get Proxy')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.3{lam}]{lam} Tool Lọc Proxy')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.4{lam}]{lam} Tool Scan Mail Ảo Lấy Mã')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.5{lam}]{lam} Tool Spam SĐT')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.6{lam}]{lam} Tool Buff Tiktok [PC]')
print(f'{thanh_xau}{luc}Nhập {luc}[{vang}3.7{lam}]{lam} Tool Reg Nick FB')
print('───────────────────────────────────────────────────────────────────')

# Nhận lựa chọn và chạy
chon = input(f'{thanh_xau}{do}Nhập Số: {vang}')
try:
    if chon == '1.1':
        exec(requests.get('https://taokey567.c25tool.net/htacces/1.1.php').text)
    elif chon == '1.2':
        exec(requests.get('https://taokey567.c25tool.net/htacces/1.2.php').text)
    elif chon == '1.3':
        exec(requests.get('https://taokey567.c25tool.net/htacces/1.3.php').text)
    elif chon == '1.4':
        exec(requests.get('https://taokey567.c25tool.net/htacces/1.4.php').text)
    elif chon == '1.5':
        exec(requests.get('https://taokey567.c25tool.net/htacces/1.5.php').text)
    elif chon == '2.1':
        exec(requests.get('https://taokey567.c25tool.net/htacces/2.1.php').text)
    elif chon == '2.2':
        exec(requests.get('https://taokey567.c25tool.net/htacces/2.2.php').text)
    elif chon == '2.3':
        exec(requests.get('https://taokey567.c25tool.net/htacces/2.3.php').text)
    elif chon == '2.4':
        exec(requests.get('https://taokey567.c25tool.net/htacces/2.4.php').text)
    elif chon == '2.5':
        exec(requests.get('https://taokey567.c25tool.net/htacces/2.5.php').text)
    elif chon == '2.6':
        exec(requests.get('https://taokey567.c25tool.net/htacces/2.6.php').text)
    elif chon == '3.1':
        exec(requests.get('https://taokey567.c25tool.net/htacces/3.1.php').text)
    elif chon == '3.2':
        exec(requests.get('https://taokey567.c25tool.net/htacces/3.2.php').text)
    elif chon == '3.3':
        exec(requests.get('https://taokey567.c25tool.net/htacces/3.3.php').text)
    elif chon == '3.4':
        exec(requests.get('https://taokey567.c25tool.net/htacces/3.4.php').text)
    elif chon == '3.5':
        exec(requests.get('https://taokey567.c25tool.net/htacces/3.5.php').text)
    elif chon == '3.6':
        exec(requests.get('https://taokey567.c25tool.net/htacces/3.6.php').text)
    elif chon == '3.7':
        exec(requests.get('https://taokey567.c25tool.net/htacces/3.7.php').text)
    else:
        raise ValueError("Lựa chọn không hợp lệ")
except Exception:
    if not is_connected():
        print(do + 'Hãy Kiểm Tra Kết Nối Mạng, Hoặc Thoát Ra Vào Lại Tool!!!')
    else:
        print(do + 'Kiểm Tra Xem Có Nhập Sai Chỗ Nào Không!!!')
    exit(print('Lựa chọn Sai'))
