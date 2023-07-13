from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
os.system('title TOOL GOP TIEN ICH')

time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
print('             ███████╗██████╗ ██╗██╗   ██╗███████╗')
print('             ██╔════╝██╔══██╗██║██║   ██║██╔════╝')
print('             █████╗  ██████╔╝██║██║   ██║█████╗  ')
print('             ██╔══╝  ██╔══██╗██║╚██╗ ██╔╝██╔══╝  ')
print('             ██║     ██║  ██║██║ ╚████╔╝ ███████╗')
print('             ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝')
print('           Copyright © FRIVE-Tool 2023 | Version 1.1')
print(f"                 Ngày: {ngay_hom_nay} Tháng: {thang_nay} Năm: {nam_}\n")
print("[•] Zalo group: https://zalo.me/g/cdcazh320")
print("[•] Email: fivetool.official@gmail.com")
print("[•] Youtube: https://www.youtube.com/@TOOLFRIVE")
print("┌─────┬────────────────────────────────────┬─────────┬─────────┐")
print("│ STT │             MENU TOOL              │ STATUS  │ VERSION │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  1  │ GET ID FACEBOOK                    │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  2  │ SPAM SMS                           │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  3  │ SPAM SMS & CALL                    │ ONLINE  │  [2.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  4  │ GET TOKEN PRO5                     │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  5  │ ADD FRIENDS                        │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  6  │ GET TOKEN                          │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  7  │ GET COOKIE PRO5                    │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  8  │ GET TOKEN OR COOKIE FACEBOOK       │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  9  │ ENC PYTHON                         │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  10 │ VIEW TIK TOK                       │ ONLINE  │  [1.0]  │")
print("├─────┼────────────────────────────────────┼─────────┼─────────┤")
print("│  11 │ QUAY LẠI                           │   =.=   │   NEXT  │")
print("└─────┴────────────────────────────────────┴─────────┴─────────┘\n")
chon = input("Nhập Lựa Chọn: ")
os.system("cls" if os.name == "nt" else "clear")
try:
        if chon == '1':
                run = requests.get('https://raw.githubusercontent.com/nobi101/getid/main/getid.py').text
        elif chon == '2':
                run = requests.get('https://raw.githubusercontent.com/nobi101/spamsms/main/spamsms.py').text
        elif chon == '3':
                run = requests.get('https://raw.githubusercontent.com/nobi101/spamcall/main/spamsms.py').text
        elif chon == '4':
                run = requests.get('https://raw.githubusercontent.com/nobi101/tokenpr5/main/tokenpr5.py').text
        elif chon == '5':
                run = requests.get('https://raw.githubusercontent.com/nobi101/add/main/add.py').text
        elif chon == '6':
                run = requests.get('https://raw.githubusercontent.com/nobi101/gettoken/main/gettoken.py').text
        elif chon == '7':
                run = requests.get('https://raw.githubusercontent.com/nobi101/getcookiepro5/main/getcookiepro5.py').text
        elif chon == '8':
                run = requests.get('https://raw.githubusercontent.com/nobi101/gettokenorcookie/main/gettokenorcookie.py').text
        elif chon == '9':
               run = requests.get('https://raw.githubusercontent.com/nobi101/enc/main/enc.py').text
        elif chon == '10':
               run = requests.get('https://raw.githubusercontent.com/nobi101/viewtiktok/main/viewtiktok.py').text
        elif chon == '11':
                run = requests.get('https://raw.githubusercontent.com/nobi101/nokey/main/Nokey.py').text
        else:
                run = print('Lựa Chọn Không Xác Định')
except:
        if not is_connected():
                print('Hãy Kiểm Tra Kết Nối Mạng !!! ')
        else:
                print('Sever Gặp Lỗi Hãy Liên Hệ Admin !!! ')
        exit()
exec(run)
