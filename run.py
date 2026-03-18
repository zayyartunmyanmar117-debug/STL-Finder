import time
import random
import os
import sys

# အရောင်များ
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
END = '\033[0m'

def slow_print(text, delay=0.5):
    """စာသားများကို တစ်ကြောင်းချင်းစီ ဖြည်းဖြည်းချင်း ဖော်ပြရန်"""
    print(text)
    sys.stdout.flush()
    time.sleep(delay)

def clear_screen():
    os.system('clear')

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
        clear_screen()
        slow_print(f"{GREEN}[+] Checking Bypass...{END}")
        slow_print(f"{WHITE}[+] Done.{END}")
        slow_print(f"{WHITE}[+] Checking user key approval...{END}")
        slow_print(f"{YELLOW}[!] This action will take a few minutes...{END}")
        slow_print(f"{WHITE}[+] 1-Trying to connect server...{END}")
        # ရှေ့ကပုံထဲကလို Log ပုံစံပြရန်
        for _ in range(3):
            t = time.strftime("%H-%M-%S")
            p = random.randint(50, 70)
            slow_print(f"Log: {{time: {t}, status: 200, ping: {GREEN}{p}{WHITE}, IsInternetAccess: {GREEN}True{WHITE}}}")
            
    elif choice == '2':
        clear_screen()
        slow_print(f"{CYAN}[+] Starting...{END}")
        slow_print(f"{YELLOW}[!] If you are getting stuck, turn on/off your wifi{END}")
        # ပုံထဲကလိုမျိုး အနီရောင် Fail Code များပြရန်
        for _ in range(10):
            code = "".join([str(random.randint(0, 9)) for _ in range(6)])
            slow_print(f"{RED}Fail Code: {code}{END}", delay=0.2)
            
    elif choice == '0':
        exit()
    
    input(f"\n{YELLOW}Press Enter to return to Menu...{END}")
    show_menu()

if __name__ == "__main__":
    show_menu()
