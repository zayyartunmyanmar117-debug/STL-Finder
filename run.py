import time
import random
import os

# အရောင်သတ်မှတ်ချက်များ
GREEN = '\033[92m'
CYAN = '\033[96m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
END = '\033[0m'

def clear_screen():
    os.system('clear')

def show_loading():
    print(f"{CYAN}Loading...{END}")
    time.sleep(1)
    clear_screen()

def check_internet():
    clear_screen()
    print(f"{GREEN}[1] Checking connectivity...{END}")
    time.sleep(1)
    print(f"{WHITE}[!] Checking Starlink Status...{END}")
    time.sleep(1)
    print(f"{WHITE}[+] Done.{END}")
    time.sleep(1)
    print(f"{WHITE}[+] Connection to Starlink API Successful.{END}")
    time.sleep(1)
    
    # Ping status နမူနာပြသရန်
    print(f"\n{CYAN}[*] Live Ping Status:{END}")
    for i in range(3):
        ping = random.randint(50, 100)
        print(f"{WHITE}Ping: {ping} ms | Status: {GREEN}Stable{WHITE}{END}")
        time.sleep(1)

def brute_force():
    clear_screen()
    print(f"{GREEN}[2] Brute-forcing Voucher Codes...{END}")
    time.sleep(1)
    print(f"{WHITE}[!] Preparing Threads...{END}")
    time.sleep(1)
    print(f"{WHITE}[*] Checking user key approval...{END}")
    time.sleep(1)
    print(f"{YELLOW}[!] This action will take a few minutes...{END}")
    time.sleep(1)
    
    # စတင်စမ်းသပ်တဲ့စာသား
    print(f"{WHITE}[+] 1-Trying to connect server...{END}")
    time.sleep(1)
    
    # Brute-force စတင်ခြင်း
    print(f"{CYAN}\n[>] Scanning...{END}")
    for i in range(10):
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        if i == 5: # success code နမူနာ
            print(f"{GREEN}Success Code: {code}{END}")
        else:
            print(f"Fail Code: {code}")
        time.sleep(0.5)

def recheck_codes():
    clear_screen()
    print(f"{GREEN}[3] Rechecking Saved Codes...{END}")
    time.sleep(1)
    print(f"{WHITE}[!] Accessing Database...{END}")
    time.sleep(1)
    print(f"{WHITE}[+] Found 1 Active Code.{END}")
    time.sleep(1)
    print(f"\n{CYAN}Status check complete.{END}")

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
        check_internet()
    elif choice == '2':
        brute_force()
    elif choice == '3':
        recheck_codes()
    elif choice == '0':
        exit()
    else:
        print(f"{RED}[!] Invalid Option!{END}")
        time.sleep(1)
    
    input(f"\n{YELLOW}Press Enter to return to Menu...{END}")
    show_menu()

if __name__ == "__main__":
    show_loading()
    show_menu()
