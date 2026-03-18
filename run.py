import random
import time

# အရောင်သတ်မှတ်ချက်များ
GREEN = '\033[92m'
BLUE = '\033[94m'
WHITE = '\033[97m'
RED = '\033[91m'
END = '\033[0m'

def start_checking():
    print(f"{WHITE}[+] Start Checking...{END}")
    time.sleep(1)

    # အကြိမ် ၂၀ စစ်ဆေးခိုင်းမည် (စိတ်ကြိုက်ပြင်နိုင်သည်)
    for i in range(20):
        code = "".join([str(random.randint(0, 9)) for _ in range(6)])
        
        # ၅ ကြိမ်မြောက်တိုင်း Success ပြပြီး ကျန်တာ Limited ပြမည့် ပုံစံ
        if i % 5 == 0:
            print(f"{GREEN}Success Code: {code}{END}")
        else:
            print(f"{BLUE}Limited Code: {code}{END}")
        
        time.sleep(0.1) # အမြန်နှုန်း (၀.၁ စက္ကန့်ခြားစီပြမည်)

    print(f"{GREEN}[+] Finished Check{END}")

if __name__ == "__main__":
    start_checking()
